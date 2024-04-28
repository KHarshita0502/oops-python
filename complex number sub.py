class ComplexNumber:
  def _init_(self,real,imaginary):
    self.real=real
    self.imaginary=imaginary
  def _sub_(self,other):
    return(f"{self.real-other.real}-{self.imaginary-other.imaginary}i")

c1=ComplexNumber(4,3)
c2=ComplexNumber(2,1)
print(c1-c2)