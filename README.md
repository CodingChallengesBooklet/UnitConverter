# Unit Converter
In this code challenge, we write a program that converts between different units.

![GitHub followers](https://img.shields.io/github/followers/hrszpuk?style=social)
![Twitter Follow](https://img.shields.io/twitter/follow/hrszpuk?style=social)
<br>
![GitHub language count](https://img.shields.io/github/languages/count/CodingChallengesBooklet/UnitConverter?style=for-the-badge)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/CodingChallengesBooklet/UnitConverter?style=for-the-badge)
![GitHub issues](https://img.shields.io/github/issues/CodingChallengesBooklet/UnitConverter?style=for-the-badge)
![GitHub last commit](https://img.shields.io/github/last-commit/CodingChallengesBooklet/UnitConverter?style=for-the-badge)
![GitHub branch checks state](https://img.shields.io/github/checks-status/CodingChallengesBooklet/UnitConverter/main?style=for-the-badge)

## Problem
Converts various units between one another. The user enters the type of unit being entered, the type of unit they want to convert to and then the value. The program will then make the conversion

The problem does not specify what units to convert between. So below I will list the units the program in this repostiory will cover. Do not feel as if you have to complete all of these conversions, only choose the ones you feel confortable with first, after completing some of the easier ones try a hard one!
- Time conversions: Centuries, Decades, Years, Months, Weeks, Days, Hours, Minutes, Seconds, Milliseconds
- Imperial Liquid conversions: Gallon, Quart, Pint, Cup, Ounce, Tablespoon, Teaspoon
- Imperial Mass conversions: Ton, Stone, Pound, Ounce
- Metric Liquid conversions: Cubic meter, Litre, Milliliter
- Metric Mass conversions: Tonne, Kilogram, Gram, Milligram, Microgram
- Temperature conversions: Celsius, Fahrenheit, Kelvin

## Solution
In order to perform the conversions, first we needs a few bits of data: we need the quantity the user is entering, the unit the quantitiy is in, and then the unit the user wants the quantity converted into. This is simple as we can just ask the user for this information. After that, we must convert the quantity into the new unit. For metric units, I think the easiest way would be to store the units in an array where the conversion is `quantity * 10^index+1` or `quantity / 10^index+1`.
```
quantity = INPUT
quantity_units = INPUT

metric_mass = ["Tonne", "Kilogram", "Gram", "Milligram", "Microgram"]

new_units = INPUT

x = INDEX OF quantity_units IN metric_mass
y = INDEX OF new_units IN metric_mass
value = 0

IF x < y THEN
    value = quantity * 10^metric_mass[y]+1
ELSE IF x > y THEN
    value = quantity / 10^metric_mass[y]+1
ELSE
    value = quantity

OUTPUT value
```
We can "run" this pesudocode by simply assigning values to variables and then going thorugh the logic either in our head or on paper. Below we assign the variables values.
```
quantity = 100
quantity_units = "Kilogram"
new_units = "Gram"
```
We tell the program we want to convert 100 Kg to grams. The program will then get the index of the units entered in `metric_mass`. 
```
x = 1  # Remember arrays start at 0, so Kilogram in metric_mass is at index 1
y = 2  # Gram in metric_mass is at index 2
```
We then check if `x` is smaller than `y`, it is, and then run the following calculation. I've shown how the calculation is evaluated so it's easier to understand where we are getting some of our values from.
```
value = quantity * 10^metric_mass[y]+1
value = 100 * 10^metric_mass[y]+1
value = 100 * 10^2+1
value = 100 * 10^3
value = 100 * 1000
value = 100000
```
