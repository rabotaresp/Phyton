class C1(object):
    x1 = 'text_x1'
    def m1(self):
        self.name = 'Igor'

    def rename(self, vvod):
        self.x1 = vvod

    def adding(self,vvod):
        self.d1 = vvod

class C2():
    y1 = 'text_y1'


class X1(C1, C2):
    x1 = 'def'
# x_obj = X1()
c_obj = C1()
# print(x_obj.x1)
print(c_obj.x1)
c_obj.m1()
print(c_obj.name)
c_obj.rename('sjdefkjsdf')
print(c_obj.x1)
c_obj.adding('ddd')
print(c_obj.d1)