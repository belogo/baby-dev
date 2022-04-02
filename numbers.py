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
count_of_ages = len(age)


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