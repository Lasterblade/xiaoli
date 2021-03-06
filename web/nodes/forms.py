#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

from wtforms import validators as v
from .models import NodeEoc, NodeOlt, NODE_STATUS_DICT, Area, Vendor, Model,SNMP_VER_DICT

from wtforms.ext.sqlalchemy.fields import QuerySelectField
from flask_wtf import TextField,RadioField,TextAreaField, required, HiddenField
from wtforms.validators import IPAddress, NoneOf

from tango.ui.form.forms import FormPro
from tango.ui.form.fields import SelectFieldPro, AreaSelectField, DateFieldPro, DecimalFieldPro
from tango.ui.tables.utils import Attrs
from tango.models import  Category
from tango.login import current_user

class NodeSearchForm(FormPro):
    keyword         = TextField()
    name            = TextField(u'IP 地址')
    area            = AreaSelectField(u'所属区域')
    category_id     = SelectFieldPro(u'节点类型',
        choices=lambda: [('', u'请选择节点类型')] + [(unicode(r.id), r.alias) for r in Category.query.filter(Category.obj=="node").filter(Category.is_valid==1)])
    vendor_id       = SelectFieldPro(u'生产厂商',
        choices=lambda: [('', u'请选择生产厂商')] + [(unicode(r.id), r.alias) for r in Vendor.query])
    model_id        = SelectFieldPro(u'设备型号',
        choices=lambda: [('', u'请选择设备型号')] + [(unicode(r.id), r.alias) for r in Model.query])
    status          = SelectFieldPro(u'状态',
        choices=lambda: [('',u'请选择状态')]+NODE_STATUS_DICT.items())

    class Meta():
        attrs = Attrs(
            label={'style':'width:80px;text-align: right;padding-bottom: 10px;'},
            field={'style':'padding-left: 10px;padding-bottom: 10px;'}
        )
        list_display = ('area','category_id','vendor_id','model_id')

class OltNewForm(FormPro):
    cityid          = SelectFieldPro(u'所属地市', choices=lambda : area_choices(1, u'请选择地市'))
    town         = SelectFieldPro(u'',choices=lambda : area_choices(2, u'请选择区县'))
    area_id         = SelectFieldPro(u'所属区域', validators=[required(message=u'必填')],
        choices=lambda : area_choices(3, u'请选择分局'))
    name            = TextField(u'OLT名称', validators=[required(message=u'必填')])
    alias           = TextField(u'OLT别名', validators=[required(message=u'必填')])
    addr            = TextField(u'IP 地址', validators=[required(message=u'必填'), IPAddress(message=u'IP地址格式不正确'), NoneOf(['0.0.0.0','255.255.255.255'], message=u'IP地址格式不正确')])
    snmp_comm       = TextField(u'读团体名', validators=[required(message=u'必填')])
    snmp_wcomm      = TextField(u'写团体名', validators=[required(message=u'必填')])
    snmp_ver       = RadioField(u'SNMP版本',default=SNMP_VER_DICT.keys()[0], validators=[required(message=u'必填')],
        choices=[(value, label) for value, label in SNMP_VER_DICT.items()])
    vendor_id       = SelectFieldPro(u'OLT厂商', validators=[required(message=u'必填')],
        choices=lambda: [('', u'请选择厂商')] + [(unicode(r.id), r.alias) for r in Vendor.query.filter(Vendor.is_valid==1)])
    model_id        = SelectFieldPro(u'OLT型号', validators=[required(message=u'必填')],
        choices=lambda: [('', u'请选择型号')] + [(unicode(r.id), r.alias) for r in Model.query.filter(Model.is_valid==1).filter(Model.category_id==20)])
    mask            = TextField(u'子网掩码')
    location        = TextField(u'位置')
    remark          = TextAreaField(u'备注信息')

class EocNewForm(FormPro):
    cityid          = SelectFieldPro(u'所属地市',choices=lambda : area_choices(1, u'请选择地市'))
    town         = SelectFieldPro(u'', choices=lambda : area_choices(2, u'请选择区县'))
    area_id         = SelectFieldPro(u'所属区域', validators=[required(message=u'必填')],
        choices=lambda : area_choices(3, u'请选择分局'))
    name            = TextField(u'EOC名称', validators=[required(message=u'必填')])
    alias           = TextField(u'EOC别名', validators=[required(message=u'必填')])
    addr            = TextField(u'IP 地址', validators=[required(message=u'必填'), IPAddress(message=u'IP地址格式不正确'), NoneOf(['0.0.0.0','255.255.255.255'], message=u'IP地址格式不正确')])
    snmp_comm       = TextField(u'读团体名', validators=[required(message=u'必填')])
    snmp_wcomm      = TextField(u'写团体名', validators=[required(message=u'必填')])
    snmp_ver       = RadioField(u'SNMP版本',default=SNMP_VER_DICT.keys()[0], validators=[required(message=u'必填')],
        choices=[(value, label) for value, label in SNMP_VER_DICT.items()])
    vendor       = QuerySelectField(u'EOC厂商', query_factory=lambda: Vendor.query.filter(Vendor.is_valid==1),
        allow_blank=True, blank_text=u'请选择厂商',get_label='alias')
    model        = QuerySelectField(u'EOC型号', query_factory=lambda: Model.query.filter(Model.is_valid==1).filter(Model.category_id==50),
        allow_blank=True, blank_text=u'请选择型号',get_label='alias')
    mask            = TextField(u'子网掩码')
    esn             = TextField(u'ESN')
    owner           = TextField(u'维护人员')
    contact_tel     = TextField(u'联系电话')
    location        = TextField(u'安装地址')
    install_time    = DateFieldPro(u'安装时间')
    remark          = TextAreaField(u'备注信息')

class CpeNewForm(FormPro):
    ctrl_id      = SelectFieldPro(u'所属EOC', validators=[required(message=u'必填')],
        choices=lambda: eoc_choices(3, u'请选择EOC'))
    area_id         = SelectFieldPro(u'接入点', validators=[required(message=u'必填')],
        choices=lambda: area_choices(4, u'请选择接入点'))
    name            = TextField(u'CPE名称', validators=[required(message=u'必填')])
    alias           = TextField(u'CPE别名', validators=[required(message=u'必填')])
    mac            = TextField(u'MAC地址', validators=[required(message=u'必填')])
    vendor       = QuerySelectField(u'CPE厂商', query_factory=lambda: Vendor.query.filter(Vendor.is_valid==1),
        allow_blank=True, blank_text=u'请选择厂商',get_label='alias')
    model        = QuerySelectField(u'CPE型号', query_factory=lambda: Model.query.filter(Model.is_valid==1).filter(Model.category_id==51),
        allow_blank=True, blank_text=u'请选择型号',get_label='alias')
    esn             = TextField(u'ESN')
    owner           = TextField(u'用户名')
    card_id         = TextField(u'身份证号')
    contact_tel     = TextField(u'联系电话')
    location        = TextField(u'安装地址')
    install_time    = DateFieldPro(u'安装时间')
    remark          = TextAreaField(u'备注信息')

class SwitchNewForm(FormPro):
    cityid          = SelectFieldPro(u'所属地市',choices=lambda : area_choices(1, u'请选择地市'))
    town         = SelectFieldPro(u'',choices=lambda : area_choices(2, u'请选择区县'))
    area_id         = SelectFieldPro(u'所属区域', validators=[required(message=u'必填')],
        choices=lambda : area_choices(4, u'请选择接入点'))
    name            = TextField(u'交换机名称', validators=[required(message=u'必填')])
    alias           = TextField(u'交换机别名', validators=[required(message=u'必填')])
    addr            = TextField(u'IP 地址', validators=[required(message=u'必填'), IPAddress(message=u'IP地址格式不正确'), NoneOf(['0.0.0.0','255.255.255.255'], message=u'IP地址格式不正确')])
    snmp_comm       = TextField(u'读团体名', validators=[required(message=u'必填')])
    snmp_wcomm       = TextField(u'写团体名', validators=[required(message=u'必填')])
    snmp_ver       = RadioField(u'SNMP版本',default=SNMP_VER_DICT.keys()[0], validators=[required(message=u'必填')],
        choices=[(value, label) for value, label in SNMP_VER_DICT.items()])
    mask            = TextField(u'子网掩码')
    location        = TextField(u'位置')
    remark          = TextAreaField(u'备注信息')

class RouterNewForm(FormPro):
    cityid          = SelectFieldPro(u'所属地市',choices=lambda : area_choices(1, u'请选择地市'))
    town         = SelectFieldPro(u'',choices=lambda : area_choices(2, u'请选择区县'))
    area_id         = SelectFieldPro(u'所属区域', validators=[required(message=u'必填')],
        choices=lambda : area_choices(4, u'请选择接入点'))
    name            = TextField(u'路由器名称', validators=[required(message=u'必填')])
    alias           = TextField(u'路由器别名', validators=[required(message=u'必填')])
    addr            = TextField(u'IP 地址', validators=[required(message=u'必填'), IPAddress(message=u'IP地址格式不正确'), NoneOf(['0.0.0.0','255.255.255.255'], message=u'IP地址格式不正确')])
    snmp_comm       = TextField(u'读团体名', validators=[required(message=u'必填')])
    snmp_wcomm       = TextField(u'写团体名', validators=[required(message=u'必填')])
    snmp_ver       = RadioField(u'SNMP版本',default=SNMP_VER_DICT.keys()[0], validators=[required(message=u'必填')],
        choices=[(value, label) for value, label in SNMP_VER_DICT.items()])
    mask            = TextField(u'子网掩码')
    location        = TextField(u'位置')
    remark          = TextAreaField(u'备注信息')

class OnuNewForm(FormPro):
    ctrl_id      = SelectFieldPro(u'所属OLT', validators=[required(message=u'必填')],
        choices=lambda : olt_choices(3, u'请选择OLT'))
    area_id         = SelectFieldPro(u'接入点', validators=[required(message=u'必填')],
        choices=lambda : area_choices(4, u'请选择接入点'))
    name            = TextField(u'ONU名称', validators=[required(message=u'必填')])
    alias           = TextField(u'ONU别名', validators=[required(message=u'必填')])
    addr            = TextField(u'IP 地址', validators=[required(message=u'必填'), IPAddress(message=u'IP地址格式不正确'), NoneOf(['0.0.0.0','255.255.255.255'], message=u'IP地址格式不正确')])
    snmp_comm       = TextField(u'读团体名', validators=[required(message=u'必填')])
    snmp_wcomm      = TextField(u'写团体名', validators=[required(message=u'必填')])
    snmp_ver       = RadioField(u'SNMP版本',default=SNMP_VER_DICT.keys()[0], validators=[required(message=u'必填')],
        choices=[(value, label) for value, label in SNMP_VER_DICT.items()])
    vendor_id       = SelectFieldPro(u'ONU厂商', validators=[required(message=u'必填')],
        choices=lambda: [('', u'请选择厂商')] + [(unicode(r.id), r.alias) for r in Vendor.query.filter(Vendor.is_valid==1)])
    model_id        = SelectFieldPro(u'ONU型号', validators=[required(message=u'必填')],
        choices=lambda: [('', u'请选择型号')] + [(unicode(r.id), r.alias) for r in Model.query.filter(Model.is_valid==1).filter(Model.category_id==21)])
    mask            = TextField(u'子网掩码')
    location        = TextField(u'位置')
    remark          = TextAreaField(u'备注信息')

class OltSearchForm(FormPro):
    keyword         = TextField()
    area            = AreaSelectField(u'所属区域')
    vendor_id       = SelectFieldPro(u'生产厂商',
        choices=lambda: [('', u'请选择生产厂商')] + [(unicode(r.id), r.alias) for r in Vendor.query])
    model_id        = SelectFieldPro(u'设备型号',
        choices=lambda: [('', u'请选择设备型号')] + [(unicode(r.id), r.alias) for r in Model.query])
    status          = SelectFieldPro(u'状态',
        choices=lambda: [('',u'请选择状态')]+NODE_STATUS_DICT.items())

class EocSearchForm(FormPro):
    keyword         = TextField()
    area            = AreaSelectField(u'所属区域')
    vendor_id       = SelectFieldPro(u'生产厂商',
        choices=lambda: [('', u'请选择生产厂商')] + [(unicode(r.id), r.alias) for r in Vendor.query])
    model_id        = SelectFieldPro(u'设备型号',
        choices=lambda: [('', u'请选择设备型号')] + [(unicode(r.id), r.alias) for r in Model.query])
    status          = SelectFieldPro(u'状态',
        choices=lambda: [('',u'请选择状态')]+NODE_STATUS_DICT.items())

class CpeSearchForm(FormPro):
    keyword         = TextField()
    area            = AreaSelectField(u'所属区域')
    vendor_id       = SelectFieldPro(u'生产厂商',
        choices=lambda: [('', u'请选择生产厂商')] + [(unicode(r.id), r.alias) for r in Vendor.query])
    model_id        = SelectFieldPro(u'设备型号',
        choices=lambda: [('', u'请选择设备型号')] + [(unicode(r.id), r.alias) for r in Model.query])
    status          = SelectFieldPro(u'状态',
        choices=lambda: [('',u'请选择状态')]+NODE_STATUS_DICT.items())

class OnuSearchForm(FormPro):
    keyword         = TextField()
    area            = AreaSelectField(u'所属区域')
    vendor_id       = SelectFieldPro(u'生产厂商',
        choices=lambda: [('', u'请选择生产厂商')] + [(unicode(r.id), r.alias) for r in Vendor.query])
    model_id        = SelectFieldPro(u'设备型号',
        choices=lambda: [('', u'请选择设备型号')] + [(unicode(r.id), r.alias) for r in Model.query])
    status          = SelectFieldPro(u'状态',
        choices=lambda: [('',u'请选择状态')]+NODE_STATUS_DICT.items())

class SwitchSearchForm(FormPro):
    keyword         = TextField()
    area            = AreaSelectField(u'所属区域')
    vendor_id       = SelectFieldPro(u'生产厂商',
        choices=lambda: [('', u'请选择生产厂商')] + [(unicode(r.id), r.alias) for r in Vendor.query])
    model_id        = SelectFieldPro(u'设备型号',
        choices=lambda: [('', u'请选择设备型号')] + [(unicode(r.id), r.alias) for r in Model.query])
    status          = SelectFieldPro(u'状态',
        choices=lambda: [('',u'请选择状态')]+NODE_STATUS_DICT.items())

class RouterSearchForm(FormPro):
    keyword         = TextField()
    area            = AreaSelectField(u'所属区域')
    vendor_id       = SelectFieldPro(u'生产厂商',
        choices=lambda: [('', u'请选择生产厂商')] + [(unicode(r.id), r.alias) for r in Vendor.query])
    model_id        = SelectFieldPro(u'设备型号',
        choices=lambda: [('', u'请选择设备型号')] + [(unicode(r.id), r.alias) for r in Model.query])
    status          = SelectFieldPro(u'状态',
        choices=lambda: [('',u'请选择状态')]+NODE_STATUS_DICT.items())

class AreaStatisticsForm(FormPro):
    area            = AreaSelectField(u'统计区域')
    query_gran       = SelectFieldPro(u'统计粒度',choices=[('1', u'地市'),('2', u'区县'),('3', u'分局'),('4', u'接入点'),])

class CityNewForm(FormPro):
    name            = TextField(u'地市名称', validators=[required(message=u'必填')])
    alias           = TextField(u'地市别名', validators=[required(message=u'必填')])
    longitude       = DecimalFieldPro(u'经度')
    latitude        = DecimalFieldPro(u'纬度')
    remark          = TextAreaField(u'备注')

class TownNewForm(FormPro):
    parent_id       = SelectFieldPro(u'所属地市', validators=[required(message=u'必填')],
        choices=lambda : area_choices(1, u'请选择地市'))
    name            = TextField(u'区县名称', validators=[required(message=u'必填')])
    alias           = TextField(u'区县别名', validators=[required(message=u'必填')])
    longitude       = DecimalFieldPro(u'经度')
    latitude        = DecimalFieldPro(u'纬度')
    remark          = TextAreaField(u'备注')

class BranchNewForm(FormPro):
    cityid          = SelectFieldPro(u'所属地市',choices=lambda : area_choices(1, u'请选择地市'))
    parent_id       = SelectFieldPro(u'所属区县', validators=[required(message=u'必填')],
        choices=lambda : area_choices(2, u'请选择区县'))
    name            = TextField(u'分局名称', validators=[required(message=u'必填')])
    alias           = TextField(u'分局别名', validators=[required(message=u'必填')])
    longitude       = DecimalFieldPro(u'经度')
    latitude        = DecimalFieldPro(u'纬度')
    remark          = TextAreaField(u'备注')

class EntranceNewForm(FormPro):
    cityid          = SelectFieldPro(u'所属地市',choices=lambda : area_choices(1, u'请选择地市'))
    town            = SelectFieldPro(u'所属区县',choices=lambda : area_choices(2, u'请选择区县'))
    parent_id       = SelectFieldPro(u'所属分局', validators=[required(message=u'必填')],
        choices=lambda : area_choices(3, u'请选择分局'))
    name            = TextField(u'接入点名称', validators=[required(message=u'必填')])
    alias           = TextField(u'接入点别名', validators=[required(message=u'必填')])
    longitude       = DecimalFieldPro(u'经度')
    latitude        = DecimalFieldPro(u'纬度')
    remark          = TextAreaField(u'备注')

def area_choices(area_type, blank_option=''):
    areas = Area.query.filter(Area.area_type==area_type)
    if not current_user.is_province_user: areas = areas.filter(current_user.domain.clause_permit)
    return [('', blank_option)] + [(unicode(r.id), r.alias) for r in areas]

def olt_choices(area_type, blank_option=''):
    olts = NodeOlt.query
    if not current_user.is_province_user: olts = olts.outerjoin(Area, NodeOlt.area_id==Area.id).filter(current_user.domain.clause_permit)
    return [('', blank_option)] + [(unicode(r.id), r.alias+' <'+r.addr+'>') for r in olts]

def eoc_choices(area_type, blank_option=''):
    eocs = NodeEoc.query
    if not current_user.is_province_user: eocs = eocs.outerjoin(Area, NodeEoc.area_id==Area.id).filter(current_user.domain.clause_permit)
    return [('', blank_option)] + [(unicode(r.id), r.alias+' <'+r.addr+'>') for r in eocs]