# ***
# * Working with numbers
#

# init a variable with a number
my_age = 35


# make a list (array) with numbers
# hard codded
ages = [10, 9, 50, 12, 32, 33, 50, 50, 22]


# find oldest
oldest = max(ages)


# find youngest
youngest = min(ages)


# find sum of all ages
sum_of_ages = sum(ages)


# find count of ages
count_of_ages = len(ages)


# find average age in ages
avg_age = sum(ages) / len(ages)


# sort ages in ascending order
asc_ages = sorted(ages)


# find the second age ( if len(ages) >= 2 )
second_age = ages[1]


# find the age next to the last ( if len(ages) >= 2 )
penultimate = ages[-1]


# find the most common age
# algo draft
# 1. make histogram of ages
# 2. find the key with biggest value

ages_histogram = {}

for age in ages:
    ages_histogram[age] = ages_histogram.get(age, 0) + 1


# find the most common age
most_common_age = max(ages_histogram, key=lambda age: ages_histogram[age])


# find the least common age 
least_common_age = min(ages_histogram, key=lambda age: ages_histogram[age])


# find unique value in ages
unique_ages = list(set(ages))


# make a list with different / unique ages 
def unique_ages_list(ages):
    unique = []
    for age in ages:
        if age not in unique:
            unique.append(age)
    return unique



# Gambling functions 
def make_a_bet(_from, to, size):
    """Make a lottery bet like 5/35, 6/42, 6/49. Result is stored in sorted list"""
    mybet = set()
    while len(mybet) != size:
        mybet.add( randint(_from, to) )
    return sorted(mybet)



class Arr:
    def __init__(self, size=0, default=None):
        self.__arr = [default] * size
        self.__size = size


    def __del__(self):
        del self.__arr
        del self.__size


    def add(self, value):
        self.__arr.append(value)
        self.__size += 1
        return self


    def remove(self, rem_value):
        """Remove all occurance of rem_value from self in place"""
        self.__arr = [ v for v in self.__arr if v != rem_value]
        self.__size = len(__arr)
        return self


    def set(self, idx, value):
        if -1 < idx < self.__size:
            self.__arr[idx] = value
            return self
        else:
            raise IndexError


    def map(self, func):
        for idx, elem in enumerate(self.__arr):
            self.__arr[idx] = func(elem)
        return self


    def filter(self, func):
        """Return a new list of filtered values from self"""
        return list(filter(func, self.__arr))


    def filter_(self, func):
        """Inplace filter of elements"""
        self.__arr = list(filter(func, self.__arr))
        return self


    def encounter(self, value):
        return sum( 1 for v in self.__arr if v == value)


    def clean(self):
        self.__arr.clear()
        self.__size = 0
        return self


    def is_empty(self):
        return self.__arr == []


    def __repr__(self):
        return repr(self.__arr)


    def __str__(self):
        return str(self.__arr)


    def __contains__(self, value):
        """Return index of first occurance of value in self"""
        for idx, elem in enumerate(self.__arr):
            if elem == value:
                return True
        return None


    def __bool__(self):
        return not self.is_empty()



    def size(self):
        return self.__size



