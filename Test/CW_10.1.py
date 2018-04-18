class C1():
    form = 'circle'
    colour = 'red'

    def vyvod(self):
        print('I am'+' '+self.colour+' '+self.form)

    def change_object(self,obj,vvod):
        obj.changeform(vvod)

class C2():
    form = 'square'
    colour = 'green'

    def vyvod(self):
        print('I am'+' '+self.colour+' '+self.form)

    def changeform(self,vvod):
        self.form = vvod

obj1 = C1()
obj2 = C2()

obj1.vyvod()
obj2.vyvod()
obj2.changeform('oval')
obj2.vyvod()
obj1.change_object(obj2,'romb')
obj2.vyvod()

for q in dir(obj2):
    print(q)