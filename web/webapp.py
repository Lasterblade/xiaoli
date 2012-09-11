#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
   XiaoLi
   ~~~~~~~

   Integrated Access Network Monitoring.
   :copyright: (c) 2012 by Ery Lee(ery.lee@gmail.com)
"""

from repoze.what.plugins.ip import ip_from

from flask import Flask, session, url_for, redirect, \
    render_template, g, request, abort

from tango.ui import menus

from tango import db, login_mgr

from tango.login import login_required, current_user

from users.models import User

app = Flask(__name__)

app.config.from_pyfile('settings.py')

db.init_app(app)
db.app = app

login_mgr.login_view = "/login"

login_mgr.login_message = u"请先登录系统."

login_mgr.refresh_view = "/reauth"

@login_mgr.user_loader
def load_user(id):
    return User.query.get(int(id))

login_mgr.init_app(app)

from dashboard.views import homeview
from topo.views import topoview
from nodes.views import nodeview
from alarms.views import alarmview
from perf.views import perfview
from report.views import reportview
from users.views import userview
from system.views import sysview

blueprints = [homeview,
              #topoview,
              nodeview,
              alarmview,
              #perfview,
              #reportview,
              userview,
              sysview]

for bp in blueprints:
    app.register_blueprint(bp)

@app.route('/')
@login_required
def index():
    return redirect('/dashboard')


allowed_ips = ['192.168.1.1/24',
               '127.0.0.1',]
ip_checker = ip_from(allowed=allowed_ips)
    
def check_ip():
    if ip_checker.is_met({'REMOTE_ADDR':request.remote_addr}) is False:
        abort(403)

def auth_all():
    pass
    
def check_permissions():
    permissions = current_user.role.permissions
    for p in permissions:
        if p.endpoint == request.endpoint:
            return
    abort(403)
    
#FIXME
@app.before_request
def before_request():
    #check_ip()
    #auth_all()
    if current_user:
        g.menus = menus
        #OUTER_ENDPOINTS = (None, 'static', 'login')
        #if request.endpoint not in OUTER_ENDPOINTS:
        #    print request.endpoint, type(current_user), current_user.role.permissions
        #    check_permissions()


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(e):
    return render_template('500.html'), 500

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)

