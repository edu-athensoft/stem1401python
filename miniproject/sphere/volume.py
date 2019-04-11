import miniproject.sphere.myconstant as myconstant

# V = 4/3 * PI * radius ^3

radius = myconstant.RADIUS_EARTH

volumeOfEarth = 4 / 3 * myconstant.PI * radius * radius * radius


print("volumeOfEarth = "+str(volumeOfEarth)+" cube km")