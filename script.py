destinations = ["Paris, France", "Shanghai, China", "Los Angeles, USA", "São Paulo, Brazil", "Cairo, Egypt"]

traveler = ['Erin Wilkes', 'Shanghai, China', ['historical site', 'art']]


#def get_destination_index(destination):
#  for destination_index in range(len(destinations)):
#    if destinations[destination_index] == destination:
#      return destination_index

def get_destination_index(destination):
  
      return destinations.index(destination)



   
print(get_destination_index("Los Angeles, USA"))

print(get_destination_index("Paris, France"))

#print(get_destination_index("Hyderabad, India"))



def get_traveler_location(traveler):
    traveler_destination = traveler[1]
    traveler_destination_index = get_destination_index(traveler_destination)

    return traveler_destination_index

test_destination_index = get_traveler_location(traveler)

print(test_destination_index)
