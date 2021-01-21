#! /usr/bin/env python

from codecs import xmlcharrefreplace_errors
from logging import error

from task_generator.task_generator_tool.tasks import get_predefined_task
import rospy
from std_srvs.srv import Empty,EmptyResponse


class TaskGenerator:
    def __init__(self):
        mode = rospy.get_param("task_mode")
        self.task=get_predefined_task(mode)

        #declare new service task_generator, request are handled in callback task generate
        self.task_service_server= rospy.Service('task_generator', Empty,self.callback_task_generate)
        
    def callback_task_generate(self,req):
        print("RESET")
        self.task.reset()
        return EmptyResponse()
    
        
        


if __name__ == '__main__':
    rospy.init_node('task_generator')
    task_generator=TaskGenerator()
    rospy.spin()
    
    
    
    
    

    
    
    

    
    
    
    
    
    
    

