
# The units we are going to convert between are stored here!
mass = ["microgram", "milligram", "gram", "kilogram", "tonne"]


# This is just a helper function - this function doesn't have anything to do with the process it's just here to
# help make our life a bit easier.
def prompt(message):
    print(message)

    # This displays all the options in mass with number next to them
    i = 1
    for unit in mass:
        print(f"{i}. {unit}")
        i += 1

    # We then ask the user to input a number, subtract 1 because indexes start at 0, and get the units the user wanted.
    return mass[int(input("Number: ")) - 1]


# Here we get the quantity, the units of the quantity, and the units to convert to
quantity = int(input("Please enter the quantity you wish to convert: "))

# These two use our prompt function because it's easier for the user to enter a number correlated with the units they
# want than entering the exact value we have stored in mass.
# What if the user enters a typo or the wrong unit? This solves that issue.
units = prompt("Choose the units of the quantity you just entered!")
new_units = prompt("Choose the units you want to convert to!")

new_quantity = quantity  # This is the conversion value

# We need to convert the values below because we need to know how many conversions need to take place.
# In this program, we convert based to the next unit up until we get the unit the user wants.
# So to convert from grams to tonnes we convert the grams to kilograms then to tonnes (so we x1000 twice)
units_index = mass.index(units)  # Convert the units to mass index
new_units_index = mass.index(new_units)  # Convert the new units to the mass index

# Here is the difference which is the number of iterations in our loop
difference_count = max(units_index, new_units_index) - min(units_index, new_units_index)

# Here is our conversion.
# It is relatively simple compared to 100s of ifs and elses.
# We /1000 or x1000 depending on whether our original units has a lower mass index than the conversion units.
for _ in range(difference_count):
    if units_index < new_units_index:
        new_quantity /= 1000
    elif units_index > new_units_index:
        new_quantity *= 1000

# We display the conversion
print(f"{quantity} {units}(s) = {new_quantity} {new_units}(s)")







