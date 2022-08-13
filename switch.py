
# This is a switcher. A sample switch for python. 


def monday():
    print("Monday")
def tuesday():
    print("Tuesday")
def wednesday():
    print("Wednesday")
    
def week(i):
    din={
        1:monday(),
        2:tuesday(),
        3:wednesday()
        }
    return din.get(i, lambda: print(f"{i} is not in the switch case."))

week(1)

class Sample:
    
    def sample(self, operator, num1, num2):
        
        method_name = operator
        method = getattr(self, method_name, lambda: print("Errorrrr"))
        return method(num1, num2)
        
    def add(self, num1, num2):
        print(num1 + num2)   
        
a = Sample()
a.sample("add", 2,3)