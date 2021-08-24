## string concatenation
#adding strings together
"""
i= "Ishi"
print ("Heyy"+ " " + i)
print ("Heyy {}".format(i))
print (f"Heyy {i}")
"""
name=input("Name:")
year=input("Year:")
favmain=input("What do you like? :")
favsubt=input("what do you like about this particular thing?")
madlib=f"Hey Everyone!! My name is {name}.I am in my {year} year of engineering.This is my first project in Python.My favourite {favmain} \
is {favsubt}."
print(madlib)