# TODO: Extend car_kwargs to correctly use kwargs and have the same results as the above class.
# Question: Where this kind of initalization is used? Any real projects examples?

# Sample class defined using *args
class car_args():
    def __init__(self, *args):
        # Assigning values
        self.speed = args[0]
        self.color = args[1]

# Initiating sample object
audi = car_args(200, 'red')
bmw = car_args(250, 'black')
mercedes = car_args(190, 'white')

# Checking results
print(audi.color)
print(bmw.speed)
print(mercedes.speed, mercedes.color)

# Sample class defined using *kwargs
class car_kwargs():
    def __init__(self, **kwargs):
        # Rewrite the class to have the same init results as car_args
        self.speed = 'speed'
        self.color = 'color'

audi = car_kwargs()
bmw = car_kwargs()
mercedes = car_kwargs()


# Checking results
print(audi.color)
print(bmw.speed)
print(mercedes.speed, mercedes.color)