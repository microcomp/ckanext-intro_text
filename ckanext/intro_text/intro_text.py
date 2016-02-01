import ckan.lib.base as base
import ckan.lib.helpers as h
import ckan.plugins as p
import ckan.lib.navl.dictization_functions as df
import ckan.logic as logic
from ckan.lib.base import BaseController, config

import logging
import ckan.model as model
from ckan.common import _, c
import ckan.plugins.toolkit as toolkit
import sys
reload(sys)  # Reload does the trick!
sys.setdefaultencoding('UTF8')
import jinja2
from ckan.common import _, c, g, request
abort = base.abort
render = base.render
_check_access = logic.check_access
def print_intro(lang):
    text = '' 

    if lang == 'en':
        try:
            en = open('en_intro.txt', 'r')
            en_text = en.read()
            en.close()
            text = en_text
        except IOError as e:
            pass
    if lang == 'sk':
        try:
            sk = open('sk_intro.txt', 'r')
            sk_text = sk.read()
            sk.close()
            text = sk_text
        except IOError as e:
            pass
    return text

class IntroTextController(base.BaseController):
    def editor(self, context=None):
        context = {'model': model, 'session': model.Session,
                   'user': c.user or c.author,
                   'auth_user_obj': c.userobj,
                   'for_view': True}
        try:
            _check_access('is_data_curator', context)
        except toolkit.NotAuthorized, e:
            toolkit.abort(401, e.extra_msg)

        return base.render('intro_text/index.html')

    def save_content(self, context=None):
        context = {'model': model, 'session': model.Session,
                   'user': c.user or c.author,
                   'auth_user_obj': c.userobj,
                   'for_view': True}
        try:
            _check_access('is_data_curator', context)
        except toolkit.NotAuthorized, e:
            toolkit.abort(401, e.extra_msg)
        all_data = logic.clean_dict(df.unflatten(logic.tuplize_dict(logic.parse_params(base.request.params))))
        en_txt = all_data.get('intro_en','')
        sk_txt = all_data.get('intro_sk','')
        fail = False
        extra_vars = {}
        if en_txt == '':
            fail = True
            extra_vars['fail'] = True
            extra_vars['en_version'] = _('English version required')
        if sk_txt == '': 
            fail = True
            extra_vars['fail'] = True
            extra_vars['sk_version'] = _('Slovak version required')
        if fail:
            return base.render('intro_text/index.html', extra_vars = extra_vars)
        sk_file = open('sk_intro.txt', 'w')
        sk_file.write(sk_txt.decode('utf-8', 'ignore'))
        sk_file.close()
        en_file = open('en_intro.txt', 'w')
        en_file.write(en_txt)
        en_file.close()

        extra_vars['sucess'] = True

        return toolkit.redirect_to(controller='ckanext.intro_text.intro_text:IntroTextController', action='editor')

