'''
Created on 31.05.2016

@author: Hubert
'''

class Robot:
    name = "MyRobot"
    hp = 100
    ep = 300
    targets = ["target1", "target2", "target3"]
    
    def attack(self, target):
        print("Attacked: " + target)
        
    
def attack(target):
    robot = Robot
    robot.attack(target)
    
attack("target4")

