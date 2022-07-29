#Copy your Burrito class from the last exercise. Now, add
#a method called "get_cost" to the Burrito class. It should
#accept zero arguments (except for "self", of course) and
#it will return a float. Here's how the cost should be
#computed:
#
# - The base cost of a burrito is $5.00
# - If the burrito's meat is "chicken", "pork" or "tofu", 
#   add $1.00 to the cost
# - If the burrito's meat is "steak", add $1.50 to the cost
# - If extra_meat is True and meat is not set to False, add
#   $1.00 to the cost
# - If guacamole is True, add $0.75 to the cost
#
#Make sure to return the result as a float even if the total
#is a round number (e.g. for burrito with no meat or
#guacamole, return 5.0 instead of 5).


#Write your code here!
class Burrito:
    def __init__(self, meat, to_go, rice, beans, extra_meat=False, guacamole=False, cheese=False, pico=False, corn=False):
        self.meat = self.set_meat(meat)
        self.to_go = self.set_to_go(to_go)
        self.rice = self.set_rice(rice)
        self.beans = self.set_beans(beans)
        self.extra_meat = self.set_extra_meat(extra_meat)
        self.guacamole = self.set_guacamole(guacamole)
        self.cheese = self.set_cheese(cheese)
        self.pico = self.set_pico(pico)
        self.corn = self.set_corn(corn)
        
    def set_meat(self, meat):
        possible_meats = ["chicken", "pork", "steak", "tofu"]
        if meat in possible_meats:
            self.meat = meat
            return self.meat
        else:
            self.meat = False
            return self.meat
            
    def set_to_go(self, to_go):
        possible_to_go = [True, False]
        if to_go in possible_to_go:
            self.to_go = to_go
            return self.to_go
        else:
            self.to_go = False
            return self.to_go
            
    def set_rice(self, rice):
        possible_rice = ["brown", "white"]
        if rice in possible_rice:
            self.rice = rice
            return self.rice
        else:
            self.rice = False
            return self.rice
            
    def set_beans(self, beans):
        possible_beans = ["black", "pinto"]
        if beans in possible_beans:
            self.beans = beans
            return self.beans
        else:
            self.beans = False
            return self.beans
            
    def set_extra_meat(self, extra_meat):
        possible_extra_meat = [True, False]
        if extra_meat in possible_extra_meat:
            self.extra_meat = extra_meat
            return self.extra_meat
        else:
            self.extra_meat = False
            return self.extra_meat
            
    def set_guacamole(self, guacamole):
        possible_guacamole = [True, False]
        if guacamole in possible_guacamole:
            self.guacamole = guacamole
            return self.guacamole
        else:
            self.guacamole = False
            return self.guacamole
            
    def set_cheese(self, cheese):
        possible_cheese = [True, False]
        if cheese in possible_cheese:
            self.cheese = cheese
            return self.cheese
        else:
            self.cheese = False
            return self.cheese
            
    def set_pico(self, pico):
        possible_pico = [True, False]
        if pico in possible_pico:
            self.pico = pico
            return self.pico
        else:
            self.pico = False
            return self.pico
            
    def set_corn(self, corn):
        possible_corn = [True, False]
        if corn in possible_corn:
            self.corn = corn
            return self.corn
        else:
            self.corn = False
            return self.corn
    
    def get_cost(self):
        self.cost = 5.00
        if self.meat in ["chicken", "pork", "tofu"]:
            self.cost += 1.00
        elif self.meat == "steak":
            self.cost += 1.50
        if self.extra_meat and self.meat:
            self.cost += 1.00
        if self.guacamole:
            self.cost += 0.75
        return float(self.cost)
    
    def get_meat(self):
        return self.meat
    
    def get_to_go(self):
        return self.to_go
    
    def get_rice(self):
        return self.rice
    
    def get_beans(self):
        return self.beans
    
    def get_extra_meat(self):
        return self.extra_meat
    
    def get_guacamole(self):
        return self.guacamole
    
    def get_cheese(self):
        return self.cheese
    
    def get_pico(self):
        return self.pico
    
    def get_corn(self):
        return self.corn


#Below are some lines of code that will test your class.
#You can change the value of the variable(s) to test your
#class with different inputs.
#
#If your function works correctly, this will originally
#print: 7.75
a_burrito = Burrito("pork", False, "white", "black", extra_meat = True, guacamole = True)
print(a_burrito.get_cost())
