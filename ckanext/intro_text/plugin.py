import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit
import ckan.logic as logic
import json
import os

import ckan.logic
import ckan.model as model
from ckan.common import _, c
import logging
import intro_text

class IntroTextPlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.IConfigurer)
    plugins.implements(plugins.IRoutes, inherit=True)
    plugins.implements(plugins.ITemplateHelpers, inherit=False)

    def update_config(self, config):
        toolkit.add_template_directory(config, 'templates')
        toolkit.add_public_directory(config, 'public')
    def before_map(self, map):
        map.connect('intro_editor', '/intro_editor',
            controller='ckanext.intro_text.intro_text:IntroTextController',
            action='editor')
        map.connect('intro_save', '/intro_save',
            controller='ckanext.intro_text.intro_text:IntroTextController',
            action='save_content')
        return map  
    def get_helpers(self):
        return {'print_intro': intro_text.print_intro}