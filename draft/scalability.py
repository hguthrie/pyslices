__author__ = 'hguthrie'

# Working with Classes


class Example:  # demo scalability
    def __init__(self, **kwargs):
        self.variables = kwargs

    def set_vars(self, key, val):
        self.variables[key] = val

    def get_vars(self, key):
        return self.variables.get(key, None)

# set variables in two ways
var = Example(Age=21, Location='I am here')
var.set_vars('name','Silly')

# Prints None if the variable is not set
print(var.get_vars('Age'))
print(var.get_vars('name'))
