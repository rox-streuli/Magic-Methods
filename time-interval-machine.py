# TIME INTERVAL
# Scenario

# Create a class representing a time interval;
# the class should implement its own method for addition, subtraction on
# time interval class objects;
# the class should implement its own method for multiplication of time
# interval class objects by an integer-type value;
# the __init__ method should be based on keywords to allow accurate and
# convenient object initialization, but limit it to hours, minutes, and
# seconds parameters;
# the __str__ method should return an HH:MM:SS string, where HH represents
# hours, MM represents minutes and SS represents the seconds attributes of
# the time interval object;
# check the argument type, and in case of a mismatch, raise a TypeError
# exception.

# HINT
# just before doing the math, convert each time interval to a corresponding
# number of seconds to simplify the algorithm;
# for addition and subtraction, you can use one internal method, as subtraction
# is just ... negative addition.
# Test data:
#
# the first time interval (fti) is hours=21, minutes=58, seconds=50
# the second time interval (sti) is hours=1, minutes=45, seconds=22
# the expected result of addition (fti + sti) is 23:44:12
# the expected result of subtraction (fti - sti) is 20:13:28
# the expected result of multiplication (fti * 2) is 43:57:40

# HINT
# you can use the assert statement to validate if the output of the
# __str__ method applied to a time interval object equals the expected value.


class TimeInterval:

    def __init__(self, hours=0, minutes=0, seconds=0):
        self.hh = hours
        self.mm = minutes
        self.ss = seconds
        try:
            self.tt = (self.hh * 3600) + (self.mm * 60) + self.ss
        except TypeError:
            print("A TypeError occurred")

    def __add__(self, other):
        """Adding method for time intervals"""
        try:
            if isinstance(other, TimeInterval):
                ts = self.tt + other.tt
            else:
                ts = self.tt + other
            return "{:2}:{:2}:{:2}".format((ts // 3600) % 24, (ts // 60) % 60,
                                           ts % 60)
        except TypeError:
            print("TypeError")

    def __sub__(self, other):
        """Subtracting method for time intervals"""
        try:
            if isinstance(other, TimeInterval):
                if self.tt < other.tt:
                    return "00:00:00"
                else:
                    ts = self.tt - other.tt
            else:
                ts = self.tt - other
            return "{:2}:{:2}:{:2}".format((ts // 3600) % 24, (ts // 60) % 60,
                                           ts % 60)
        except TypeError:
            print("TypeError")

    def __mul__(self, other):
        try:
            if isinstance(other, TimeInterval):
                # self.tt = (self.hh * 3600) + (self.mm * 60) + self.ss
                ts = self.tt * other.tt
            else:
                ts = self.tt * other
            return "{:2}:{:2}:{:2}".format((ts // 3600) % 24, (ts // 60) % 60,
                                           ts % 60)
        except TypeError:
            print("TypeError")


t1 = TimeInterval(hours=21, minutes=58, seconds=50)
t2 = TimeInterval(1, 45, 22)
t3 = TimeInterval(9, 0, 4)
# t4 = TimeInterval(9, '0', 4)
print(t1 + t2)
print(t1 - t2)
print(t1 * t2)
print(t1 * 2)
#
# assert str(t1 + t2) == '23:44:12'
# assert str(t1 - t2) == '20:13:28'
# assert str(t1 * 2) == '43:57:40'
