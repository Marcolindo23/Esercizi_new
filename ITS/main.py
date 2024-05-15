from room import Room
from building import Building

r = Room(name = "213", floor = 2, num_seats = 30)
print(r)
print("#" * 50)
b = Building(name = "SMI", address = "Via della Sierra Nevada 60", floors = 5)
print(len(b.get_rooms()))
