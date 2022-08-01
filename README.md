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

The problem does not specify what units to convert between. So below is a list of all the units you can do. Do not feel as if you have to complete all of these conversions, only choose the ones you feel comfortable with first.
In our solution, we will only be tackling the Metric Mass conversion as it's the easiest to explain.
- Time conversions: Centuries, Decades, Years, Months, Weeks, Days, Hours, Minutes, Seconds, Milliseconds
- Imperial Liquid conversions: Gallon, Quart, Pint, Cup, Ounce, Tablespoon, Teaspoon
- Imperial Mass conversions: Ton, Stone, Pound, Ounce
- Metric Liquid conversions: Cubic meter, Litre, Milliliter
- Metric Mass conversions: Tonne, Kilogram, Gram, Milligram, Microgram
- Temperature conversions: Celsius, Fahrenheit, Kelvin

## Solution
In order to perform the conversions, first we need a few bits of data: we need the quantity the user is entering, the unit the quantity is in, and then the unit the user wants the quantity converted into. 
This is simple as we can just ask the user for this information. After that, we must convert the quantity into the new unit.

For metric mass, to convert up and down we simply divide or multiply by 1000.
So, given our units are micrograms, milligrams, grams, kilograms, and tonnes.
To convert gram to kilograms we divide by 1000.
To convert grams to milligrams we multiply by 1000.
For each unit we want to convert "up" we divide by 1000, and for each unit we want to convert "down" we multiply by 1000.

This is a consistent pattern we can use to make conversions very easy.
We find the difference between the user's unit index and the user's convert to unit index, and that's the number of times
we multiply/divide. In order to know whether to divide or multiply we just need to find which index is bigger.

For example, say the user wants to convert 100 grams to micrograms.
"gram" is index 2 and "microgram" is index 0. The difference is 2-0=2. 
We multiply the quantity x1000 twice to get the converted value.
So, `100 grams x 1000 x 1000 = 100000000 micrograms`.

That's enough explaining let's get on with some code!
The first part of our code is simple enough, we get the inputs for `quantity` `units` and `new_units` (the units we'll be converting to).
We also define `metric_mass` which is a list of all the units our program can convert between.
```
quantity = INPUT
units = INPUT

metric_mass = ["microgram", "milligram", "gram", "kilogram", "tonne"]

new_units = INPUT
```

Next, we get the index of `units` and `new_units` in `metric_mass`. We need the index to find the difference.
Our difference is defined by subtracting `units` from `new_units` or `new_units` from `units` depending on which is bigger.
We use `MAX` and `MIN` functions most programming languages have to get the biggest and smallest value out of the two.
```
units_index = INDEX OF units IN metric_mass
new_units_index = INDEX OF new_units IN metric_mass
difference = MAX VALUE OF units_index AND new_units_index - MIN VALUE OF units_index AND new_units_index
```

Finally, it's time to start converting our quantity!
We begin by defining a storage place for our converted value called `new_quantity`.
Next, we loop until the difference is 0 and either divide by 1000 or multiply by 1000 depending on whether `units_index` or `new_units_index` is bigger.
After each cycle of the loop we subtract 1 from difference otherwise our loop will be infinite!
At last, once the loop ends, we output our converted value!
```
new_quantity = quantity

LOOP UNLESS difference = 0
    IF units_index < new_units_index THEN
        new_quantity = new_quantity / 1000
    ELSE IF units_index > new_units_index THEN
        new_quantity = new_quantity * 1000
    difference = difference - 1

OUTPUT new_quantity
```
