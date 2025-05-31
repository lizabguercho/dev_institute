human_years = 10
dog_years = 0
cat_years = 0

for year in range (1, human_years + 1):
    if year == 1:
        cat_years += 15
        dog_years += 15
    elif year == 2:
        cat_years += 9
        dog_years += 9
    else :
        cat_years += 4
        dog_years += 5
print(cat_years)
print(dog_years)