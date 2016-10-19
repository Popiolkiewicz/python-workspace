'''
Created on 31.05.2016

@author: Hubert
'''

class Robot:
    __secretMission = "KILL_ALL_HUMANS"
    name = ""  # __ == private
    hp = 0 
    ep = 0
    targets = []
    
    def __init__(self, name, hp, ep, targets):
        self.name = name
        self.hp = hp
        self.ep = ep
        self.targets = targets

    def __str__(self):
        return "Name: %s, Hp : %s, ep: %s, targets: %s" % (self.name, self.hp, self.ep, self.targets)
        
    def attack(self, target):
        if target in self.targets:
            print("Attacked: " + target)
        else:
            print("Not found")
        
    def sayYourName(self):
        print("My name is " + self.name)
        
    def addEnemy(self, enemy):
        self.targets.append(enemy)
        
    def whatIsYourSecterMission(self):
        print(self.__secretMission)
        
def make_robot(name, hp, ep, targets):
    robot = Robot(name, hp, ep, targets)
    return robot 

myRobot = make_robot("Robot1", 100, 200, ["t1", "t2"])
enemy = input("Podaj nazwe wroga: ")
myRobot.addEnemy(enemy)

print(myRobot.__str__())
myRobot.attack(enemy)


class Android (Robot):
    hp = 200
    
    def __init__(self):
        print("No data in constructor")
        
    def whatIsYourSecterMission(self):
        print("Nothing important")
        
android = Android("Android1", 100, 200, ["t1", "t2"])

android.whatIsYourSecterMission()