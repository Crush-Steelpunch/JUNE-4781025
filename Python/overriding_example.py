class Animal:
    babies = 0
    def reproduce(self):
        self.babies += 1

class dog(Animal):
    def reproduce(self):
        self.babies += 6

rover = dog()
rover.reproduce()
rover.reproduce()
rover.reproduce()
print(rover.babies)

axiolotl = Animal()
axiolotl.reproduce()
axiolotl.reproduce()
axiolotl.reproduce()
print(axiolotl.babies)

