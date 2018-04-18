class C1():

    def __init__(self,form='blue',colour='oval'):
        self.form = form
        self.colour = colour

    def pr(self):
        print('I am'+' '+self.colour+' '+self.form)


obj = C1('red', 'circle')
obj1 = C1()
obj.pr()
obj1.pr()