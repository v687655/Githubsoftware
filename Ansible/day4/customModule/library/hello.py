#!usr/bin/bash

from ansible.module_utils.basic import *;

class Hello:
 def sayHello(self,myName):
     return "Hello, ",myName

def mycode():
        module = AnsibleModule(argument_spec=dict(Name=dict(required=True,type='str')))
    
        hello=Hello()
        Nameval=module.params["Name"]
    
        result={"Result": hello.sayHello(Nameval)}
        module.exit_json(changed=False, meta=result)

mycode()
