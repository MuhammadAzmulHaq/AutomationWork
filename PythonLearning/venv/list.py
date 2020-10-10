fruits = ["peaches", "Pears", "Apples"]
years = [3, "1998",2.5, 983, "1993"]

fruits.append("oranges")
fruits.extend(years)
print(fruits)

fruits.remove("peaches")
print(fruits)

years.pop(2)
print(years)

years.pop(-2)
print(years)