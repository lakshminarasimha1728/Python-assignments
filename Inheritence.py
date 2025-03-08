'''A, B and C are classes

A is a super class. B is a sub class of A. C is a sub class of B.

Create three methods in each class, 2 methods are specific to each class and third
method (override method) should be in all three Classes A, B and C

Create a class with main method. Create an object for each class A, B and C in main
method and call every method of each class using its own object/instance.

Call an overridden method with super class reference to B and C class’s objects

Runtime Polymorphism with Data Members/Instance variables, Repeat the above
process only for data members'''
class A():  
    def display(dp):
        print("Display Inside class A ")
 # class A show method    
    def show(self):
        print("Show Inside class A")
    
# Inherited or Sub class (Note A in bracket) 
class B (A): 
    def print(pt):
        print("Print Inside class B")    
    # class B show method
    def show(self):
        print("Show Inside class B")
    
# Inherited or Sub class (Note B in bracket) 
class C (B): 
          
    # class C show method
    def show(self):
        print("Show Inside class C ")         
    
# Driver code 
s = A()
s.display()
k= B()
k.print()
g = C()   
g.show()
