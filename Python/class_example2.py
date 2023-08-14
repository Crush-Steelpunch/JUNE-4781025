class Dog:


    def __init__(self,colourvar,breedvar,energyvar,speakvar='woof'):
        self.colour = colourvar
        self.breed = breedvar
        self.energy = energyvar
        self.speak = speakvar

    def speak(self):
        return self.speak

WoofyMcWoofface = Dog('gold','labrador','high')
ScoobyDoo = Dog('Brown','GreatDane','low','ScoobyScoobyDooooo')
Rosie = Dog('Black','Whippet','Superhigh','yipyipyipyipyipyip')




