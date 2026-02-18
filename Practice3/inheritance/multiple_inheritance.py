class Father:
    def skills(self):
        print("Plays football")

class Mother:
    def talents(self):
        print("Cooks well")

class Child(Father, Mother):
    pass

child = Child()
child.skills()
child.talents()