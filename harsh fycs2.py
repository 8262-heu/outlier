class Numbers:
 MULTIPLIER=3.5
 def _init_(self,x,y):
    self.x=x
    self.y=y
 def add(self):
    return self.x+self.y
    @classmethod
 def multiply(cls,a):
    return cls.MULTIPLIER*a
    @staticmethod
 def subtract(b,c):
    return b-c
    @property
 def value(self):
    return(self.x,self.y)
    @value.setter
 def value(self,xy_tuple):
        self.x,self.y = xy_tuple

T=Numbers(2,4)
print(T.add())
print(T.multiply(5))
print(Numbers.subtract(5,4))
tp=T.value
print(tp)









