# path : $SPHOME/etc/apps/myapps/controllers/my_script.py

import logging
import os
import sys
import json

import splunk.appserver.mrsparkle.controllers as controllers
import splunk.appserver.mrsparkle.controllers as util
from splunk.appserver.mrsparkle.lib.util import make_splunkhome_path
from splunk.appserver.mrsparkle.lib.decorators import expose_page

_APPNAME = 'LGD'

logger = logging.basicConfig(level=logging.INFO
                             format='%(asctime)s - $(message)s',
                             datefmt='%Y-%m-%d %H:%M:%S',
                             filename='/opt/splunk/var/log/splunk/endpoint_test.log')

logger = logging.getLogger('endpoint_test')

class Controller(controllers.BaseController) :
    
    #/custom/MyAppName/my_script/my_endpoint
    @expose_page(must_login=False, methods=['GET'])
    def my_function(self, **kwargs) :
        arg1 = kwargs.get('arg1', 'a')
        if arg1 == 'btn1' :
            response = arg1 + ' is clicked'
        else :
            response = 'click nothing'
            
    value = {"name" : arg1, "content": response }
    jstring = json.dumps(value)
    return jstring
