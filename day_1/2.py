#We need to calculate the amount of fuel needed to launch modules.
#Fuel required is based on mass.

masses=[]

with open('input.txt') as fp:
    for _, line in enumerate(fp):
        masses.append(float(line))

#To get the fuel needed for a given mass, divide the mass by three, round down, and subtract 2.
def calculate_fuel(mass):
    return max(0, int(mass / 3.0) - 2)

sum=0

for mass in masses:
    fuel_needed=calculate_fuel(mass)

    while fuel_needed > 0.0:
        sum+=fuel_needed
        fuel_needed=calculate_fuel(fuel_needed)

print(sum)
