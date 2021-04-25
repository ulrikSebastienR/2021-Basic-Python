# Getter, Setter and Deleter
#https://www.youtube.com/watch?v=jCzT9XFZ5bw&t=303s
class Employee:
    def __init__(self,first,last):
        self.first = first
        self.last = last
        #self.email = first+"."+last+"@rmail.com"

    def show(self):
       return self.email

    @property
    def email(self):
        return "{}.{}@kmail.com".format(self.first,self.last)

    @property
    def fullname(self):
        return "{} {}".format(self.first,self.last)

    @fullname.setter
    def fullname(self, name):
        first, last = name.split(" ")
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        print("No such employee anymore with us")
        self.first = None
        self.last = None
    
    def pr(self):
        print(self.first)

    


E1 = Employee("jacob", "dancer")
#E1.first = "Jim"
#print(E1)
print(E1.first)
#print(E1.email)
print(E1.show())
#print(E1.pr)
#print(E1.pr())
#print(E1.fullname())
print(E1.email)
print(E1.fullname)

E1.fullname = "Emile Menier"
print(E1.fullname)

del E1.fullname
print(E1.fullname)
