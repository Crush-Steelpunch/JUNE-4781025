# Class example

#class ExampleClass:
#    attribute1 = 'somedata'
#    attribute1 = 123
#
#    def examplefunction(self, inputvar):
#        examplecode_here
class Addanumbers:

    thenumber = 1

    def addthenumber(self,inputvar):
        outputvar = inputvar + self.thenumber
        return outputvar


object1 = Addanumbers()
object2 = Addanumbers()
object3 = Addanumbers()

object2.thenumber = 2
object3.thenumber = 3

print(object1.thenumber)
print(object2.thenumber)
print(object3.thenumber)

print(object1.addthenumber(5))
print(object2.addthenumber(5))
print(object3.addthenumber(5))

