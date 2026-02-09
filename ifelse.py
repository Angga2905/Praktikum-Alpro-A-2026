#if
a = 33
b = 200
if b > a:
  print("b is greater than a")

#elif
a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")

#else
a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")

#shorthand if
a = 5
b = 2
if a > b: print("a is greater than b")

#logical operator
#and
a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")

#or
a = 200
b = 33
c = 500
if a > b or a > c:
  print("At least one of the conditions is True")

#not
a = 33
b = 200
if not a > b:
  print("a is NOT greater than b")

#combination
age = 25
is_student = False
has_discount_code = True

if (age < 18 or age > 65) and not is_student or has_discount_code:
  print("Discount applies!")

#Using Parentheses for Clarity
temperature = 25
is_raining = False
is_weekend = True

if (temperature > 20 and not is_raining) or is_weekend:
  print("Great day for outdoor activities!")

#Nested if
temperature = 25
is_sunny = True

if temperature > 20:
  if is_sunny:
    print("Perfect beach weather!")

#pass statement
a = 33
b = 200

if b > a:
  pass

