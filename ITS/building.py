from room import Room
class Building:
    def __init__(self, name: str, address: str, floors: int):
        self.name: str = name
        self.address: str = address
        self.floors: int = floors
        self.rooms: list[Room] = []
    
        def add_room(room: Room) -> bool:
            if room not in self.get_rooms() and room.floor <= self.get_rooms():
                self.rooms.append(room)
                return True
            return False
    
    def get_name(self) -> str:
        return self.name
    
    def get_address(self) -> str:
        return self.address
    
    def get_floors(self) -> int:
        return self.floors

    def get_rooms(self) -> list[Room]:
        return self.rooms