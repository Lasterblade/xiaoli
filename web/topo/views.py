#coding: utf-8

from flask import Blueprint, request, url_for, \
    render_template, json

from tango.ui import navbar
from nodes.models import Node, Area, AREA_PROVINCE

topoview = Blueprint('topo', __name__)

@topoview.context_processor
def inject_navid():
    return dict(navid = 'topo')

@topoview.route('/topo/')
def index():
    return render_template('topo/index.html')

@topoview.route('/topo/test2')
def test2():
    return render_template('topo/test2.html')

@topoview.route('/topo/olts.json', methods=['GET', 'POST'])
def olts_json():
    return 'OK'
    #return json.dumps({'children':[data,data]})

@topoview.route('/topo/directory.json')
def json_load_directory():
    spath = request.args.get('path', '')
    data = None
    lvs_all = ['ROOT', 'OLT', 'ONU', 'EOC', 'CPE']
    
    if spath:
        data = []
        path = spath.split(',')
        pre_id = '-'.join(path[-1].split('-')[1:])
        print 'pre_id:', pre_id
        if len(path) >= len(lvs_all):
            return json.dumps([])
        lvs = [i.split('-')[0].upper() for i in path]
        lv = lvs_all[len(lvs)]
        for i in range(1, 8):
            name = '%s-%s-%d' % (lv, pre_id, i)
            node = {
                'name'     : name,
                'children' : None,
                'level'    : len(lvs),
                'id'       : name.lower(),
            }
            node['_children'] = [] if  (len(path) < len(lvs_all)-1) else None
            data.append(node)
    else:
        data = {
            'name'     : 'ROOT-0',
            'children' : [],
            'level'    : 0,
            'id'       : 'root-0',
        }
        for i in range(1, 100):
            name = 'OLT-' + str(i)
            node = {
                'name'     : name,
                'children' : [],
                'level'    : 1,
                'id'       : name.lower()
            }
            data['children'].append(node)
    return json.dumps(data)
    
@topoview.route('/topo/nodes.json')
def json_load_nodes():
    # 1. 缩放           DONE
    # 2. 拖拽           DONE
    # 3. 链接           DONE
    # 4. 显示图片       DONE
    # 5. 表达节点的状态 DONE
    # 6. 右键菜单       DONE
    # 7. 搜索跳转       DONE
    from random import Random
    rand = Random()
    
    spath = request.args.get('path', 'olt-0')
    na    = request.args.get('na', 7, type=int)
    nb    = request.args.get('nb', 7, type=int)
    nnc   = request.args.get('nc', 7, type=int)

    ca = cb = cc = 0;
    onu_lv, eoc_lv, cpe_lv = 2, 3, 4
    path = spath.split(',')[1:]
    lvs = [i.split('-')[0].upper() for i in path]
    
    data = {
        'name'     : path[0].upper(),
        'children' : [],
        'level'    : 1,
        'maxlevel' : 1,
        'maxpath'  : len(path) - 1,
        'id'       : path[0]
    }
    c0 = path[0].split('-')[-1]
    def selected(s, name):
        if s in lvs and name.lower() not in path:
            return False
        return True
    print '========================================'
    print spath, path, lvs
    print '--------------------'
    
    for a in range(na):         # ONU
        ca = a+1
        aname = 'ONU-%s-%d' % (c0, ca)
        A = {'name': aname, 'children': [],
             'level': onu_lv, 'id': aname.lower(), "size": ca * 30}
        A['status'] = rand.randint(0, 5)
        for b in range(nb):     # EOC
            cb = b+1
            bname = 'EOC-%s-%d-%d' % (c0, ca, cb)
            B = {'name': bname, 'children': [],
                 'level': eoc_lv, 'id': bname.lower(), "size": cb * 30}
            B['status'] = rand.randint(0, 5)
            nc = nnc
            for c in range(nc): # CPE
                cc = c+1
                cname = 'cpe-%s-%d-%d-%d' % (c0, ca, cb, cc)
                C = {'name': cname, 'url': 'http://www.stackoverflow.com',
                     'level': cpe_lv, 'id': cname.lower() , "size": cc * 30}
                C['status'] = rand.randint(0, 5)
                C['lstatus'] =  1 if c % 5 > 1 else 0
                if selected('CPE', cname):
                    if data['maxlevel'] < cpe_lv:
                        data['maxlevel'] = cpe_lv;
                    B['children'].append(C)
            if selected('EOC', bname):
                if data['maxlevel'] < eoc_lv:
                    data['maxlevel'] = eoc_lv;
                A['children'].append(B)
        if selected('ONU', aname):
            if data['maxlevel'] < onu_lv:
                data['maxlevel'] = onu_lv;
            data['children'].append(A)

    def pdict(d):
        print d['id'],
        if 'children' in d:
            print len(d['children'])
            for c in d['children']:
                pdict(c)
    # pdict(data)
    return json.dumps(data)


from tango.login import current_user    
from tango.cache import cache
from tango.profile import cached_profile
from tango import db, update_profile, get_profile
@topoview.route('/topo/dump-drag-history', methods=['POST'])
def ajax_dump_drag_history():
    args = request.values
    path = args.get('path','')
    nodes = args.get('nodes', '') #
    print 'path, nodes:', path, nodes
    if path and nodes:
        update_profile('topo.drag', path, nodes)
        db.session.commit()
    return 'ERROR:%s:%s' % (path, nodes)

    
@topoview.route('/topo/load-drag-history.json')
def json_load_drag_history():
    path = request.args.get('path', '')
    data = {}
    cache.delete_memoized(cached_profile, current_user.id, 'topo.drag')
    if path:
        nodes = get_profile('topo.drag').get(path, '') # get from database by path
        if nodes:
            nodes = nodes.split(';')
            nodes = [node.split(',') for node in nodes]
            for node in nodes:
                data[node[0]] = {'x':float(node[1]), 'y':float(node[2])}
            return json.dumps(data)
        data['error'] = 'No nodes'
    data['error'] = 'Path empty!'
    return json.dumps(data)
    
navbar.add('topo', u'拓扑', 'random', '/topo')

