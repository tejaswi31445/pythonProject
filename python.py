str = "welcome"
print(str)
list=["headlines"]
print(list)
l=[{'id':243,'title':'RRR movie','description':'released on 17th jan'}]
print(l)
l=[{'id':231,'title':'ssr movie','description':'released on 24th dec'}]
print(l)
l=[{'id':289,'title':'bahubali movie','description':'released on 15th dec'}]
print(l)
class Student:
    def init(self,m1,m2,m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

# setter method(mutator)
def set(self):
    m1=85
# getter method(accessor)
def avg(self):
    return(self.m1+self.m2+self.m3)/3

s1=Student(84,97.99)
s2=Student(96,85,82)

s1.set()

print(s1.avg())
print(s2.avg())




