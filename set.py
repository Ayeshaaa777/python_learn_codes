# set= collection which is unordered, unindexed, no duplicate values
# faster than a list to check if an element is present
# utensils.add(), utensils.remove(), utensils.difference() .intersection(),.union(). update()
utensils = {"fork", "spoon", "knife"}
dishes = {"bowl", "plate", "cup"}
utensils.add("napkin")
utensils.remove("fork")
# utensils.clear()
utensils.update(dishes)  # adds all the elemts of dishes to update
dinner_table = utensils.union(dishes)
print(dinner_table)
# for x in utensils:
#   print(x)
print(utensils.difference(dishes))
# what do utensils have that dishes dont
print(utensils.intersection(dishes))
