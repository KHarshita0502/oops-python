class ComplexNumber:
  def _init_(self,real,imaginary):
    self.real=real
    self.imaginary=imaginary

  def _add_(self,other):
    return(f"{self.real+other.real}+{self.imaginary+other.imaginary}i")

c1=ComplexNumber(2,2)
c2=ComplexNumber(1,2)

print(c1+c2)

