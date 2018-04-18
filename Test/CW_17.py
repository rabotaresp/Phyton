class perviy():
    color = 'Green'
    form = 'Cube'
    def view(self):
        return perviy.color, perviy.form
    def re_view_c(self, cr):
        self.cr = 'Blue'
        return self.cr
    def re_view_f(self, fm):
        self.fm = 'GGG'
        return self.fm
class vtoroy():
    color = 'Red'
    form = 'Round'
    def view_c(self):
        return vtoroy.color
    def view_f(self):
        return vtoroy.form
obj_perviy = perviy()
obj_vtoroy = vtoroy()
a = obj_vtoroy.view_c()
b = obj_vtoroy.view_f()
print(obj_perviy.view())
print(obj_perviy.re_view_f(b))