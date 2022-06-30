class Time:
    """Represents the time of day.
       
    attributes: hour, minute, second
    """
    def __init__(self, hour=0, minute=0, second=0):
        """Initializes a time object.
        hour: int
        minute: int
        second: int or float
        """
        self.hour = hour
        self.minute = minute
        self.second = second

    def print_time(self):
        """Prints a string representation of the time."""

        print('%.2d:%.2d:%.2d' % (self.hour, self.minute, self.second))

    def is_after(self, time):
        """Returns True if t1 is after t2; false otherwise."""
        
        time1=3600*self.hour+60*self.minute+self.second
        time2=3600*time.hour+60*time.minute+time.second
        return time1 > time2
    
    def increment(self, seconds):
        """Time increment that doesnt contain any loops or if statement. Returns new time"""

        a=self.second+seconds
        b=self.minute+a/60
        self.hour+=int(b/60)
        self.minute=int(b%60)
        self.second=a%60
        return '%.2d:%.2d:%.2d' % (self.hour, self.minute, self.second)
    
    def pureinc(self,seconds):
        """Pure version of increment that creates and returns a new Time object rather than modifying the parameter"""

        import copy
        time2=copy.copy(self)
        time2.increment(seconds)
        return '%.2d:%.2d:%.2d' % (time2.hour, time2.minute, time2.second)

    def time_to_int(self):
        """Computes the number of seconds since midnight. Time: Time object"""
        minutes = self.hour * 60 + self.minute
        seconds = minutes * 60 + self.second
        return seconds

    def __str__(self):
        """Special method for string and useful for debugging. Returns a string representation of the time."""

        return '%.2d:%.2d:%.2d' % (self.hour, self.minute, self.second)

    def __add__(self, other):
        """Adds two Time objects or a Time object and a number.
        other: Time object or number of seconds
        """

        #The built-in function isinstance takes a value and a class object, and returns True if the value is an instance of the class.
        if isinstance(other, Time):
            return self.add_time(other)
        else:
            return self.increment2(other)

    def __radd__(self, other):
        """Adds two Time objects or a Time object and a number."""
        return self.__add__(other)

    def add_time(self, other):
        """Adds two time objects. Self (for example Object t1), t2: Time. Returns: Time
        assert: checks a given invariant and raises an exception if it fails
        replace:
        if not valid_time(t1) or not valid_time(t2):
            raise ValueError('invalid Time object in add_time')"""

        assert self.valid_time() and other.valid_time(), "Time is not valid"
        seconds = self.time_to_int() + other.time_to_int()
        return int_to_time(seconds)
    
    def increment2(self, seconds):
        """Return new Time by adding seconds"""
        seconds += self.time_to_int()
        return int_to_time(seconds)
    
    def valid_time(self):
        """Return False if time is not correct, if time is correct return true"""
        if self.hour < 0 or self.minute < 0 or self.second < 0:
            return False
        if self.minute >= 60 or self.second >= 60:
            return False
        return True
    
    def print_attributes(self):
        """print_attributes traverses the dictionary and prints each attribute name and its corresponding value, 
        If you are not sure whether an object has a particular attribute.
        The built-in function getattr takes an object and an attribute name (as a string) and returns the attribute’s value."""

        for attr in vars(self):
            print(attr, getattr(self, attr))

    
def int_to_time(seconds):
    """Makes a new Time object. Seconds: int seconds since midnight."""

    minutes, second = divmod(seconds, 60)
    hour, minute = divmod(minutes, 60)
    time = Time(hour, minute, second)
    return time



#creation of an object 
time = Time(11, 59, 30)

#calling print_time method to print the Time object to a string as time
time.print_time()

#creation of two further time object, t1, t2
t1 = Time(16, 59, 59)
t2 = Time(13, 54, 20)

#calling method t1 is after t2 --> true
print("is_after:", t1.is_after(t2))

#increment method. t2 will increase to 60 seconds 
print("increment:", t2.increment(60))

#pure function same as increment method
print("pureinc:", t2.pureinc(10))

#convert interger to time!
print("int_to_time:", int_to_time(43170))

#convert time to integer
print("time_to_int():", time.time_to_int())

#t1 add with t2
print("add_time:", t1.add_time(t2))

#shorter and easier than increment method
print("increment2:", time.increment2(1337))

#special method __str__: print_time is not necessary anymore
specialMethodTime = Time(9,45)
print("__str__ special method:", specialMethodTime)

#__add__ special method check: + operator on Time objects
m1 = Time(9, 3, 5)
m2 = Time(10, 27, 5)
print("__add__ special method:", m1+m2)
print(m1 + 1345)
print(1345 + m1)

#functions that work with several types are called polymorphic! Example of polymorphism with the built-in function sum:
z1 = Time(7, 43)
z2 = Time(7, 41)
z3 = Time(7, 37)
total = sum([z1, z2, z3])
print("Example of Polymorphism sum([z1, z2, z3]:", total)

#calling method valid_time, check if time is valid
print("Time is:", t1.valid_time())

#calling print_attributes 
print(t1.print_attributes())

#Another way to access attributes is the built-in function vars, which takes an object and returns a dictionary that maps from attribute names (as strings) to their values:
print(vars(t2))