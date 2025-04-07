from api.models import Hotel, Room
from datetime import date

# Create Hotels
hotel1 = Hotel.objects.create(name="Sea Breeze", loc_id_id=1, image_path="hotels/seabreeze.jpg")
hotel2 = Hotel.objects.create(name="Mountain Lodge", loc_id_id=2, image_path="hotels/mountainlodge.jpg")
hotel3 = Hotel.objects.create(name="City Inn", loc_id_id=3, image_path="hotels/cityinn.jpg")
hotel4 = Hotel.objects.create(name="Harbour View", loc_id_id=1, image_path="hotels/harbourview.jpg")
hotel5 = Hotel.objects.create(name="Skyline Suites", loc_id_id=3, image_path="hotels/skylinesuites.jpg")
hotel6 = Hotel.objects.create(name="Coastline Hotel", loc_id_id=2, image_path="hotels/coastlinehotel.jpg")
hotel7 = Hotel.objects.create(name="Sunset Bay", loc_id_id=1, image_path="hotels/sunsetbay.jpg")
hotel8 = Hotel.objects.create(name="Aurora Stay", loc_id_id=2, image_path="hotels/aurorastay.jpg")
hotel9 = Hotel.objects.create(name="Urban Comfort", loc_id_id=3, image_path="hotels/urbancomfort.jpg")

# Create Rooms (composite PK: hotel_id + room_number)
Room.objects.bulk_create([
    Room(hotel_id=hotel1, room_number=101, pricePerNight=120, roomType="Standard", availableFom=date(2025, 5, 1), availableTo=date(2025, 5, 10)),
    Room(hotel_id=hotel1, room_number=102, pricePerNight=150, roomType="Deluxe", availableFom=date(2025, 5, 3), availableTo=date(2025, 5, 12)),
    Room(hotel_id=hotel2, room_number=201, pricePerNight=200, roomType="Suite", availableFom=date(2025, 6, 1), availableTo=date(2025, 6, 15)),
    Room(hotel_id=hotel2, room_number=202, pricePerNight=180, roomType="Standard", availableFom=date(2025, 6, 5), availableTo=date(2025, 6, 20)),
    Room(hotel_id=hotel3, room_number=301, pricePerNight=180, roomType="Executive", availableFom=date(2025, 7, 5), availableTo=date(2025, 7, 20)),
    Room(hotel_id=hotel3, room_number=302, pricePerNight=160, roomType="Standard", availableFom=date(2025, 7, 6), availableTo=date(2025, 7, 25)),
    Room(hotel_id=hotel4, room_number=101, pricePerNight=140, roomType="Standard", availableFom=date(2025, 5, 10), availableTo=date(2025, 5, 15)),
    Room(hotel_id=hotel4, room_number=102, pricePerNight=155, roomType="Deluxe", availableFom=date(2025, 5, 11), availableTo=date(2025, 5, 18)),
    Room(hotel_id=hotel5, room_number=401, pricePerNight=220, roomType="Penthouse", availableFom=date(2025, 8, 1), availableTo=date(2025, 8, 10)),
    Room(hotel_id=hotel5, room_number=402, pricePerNight=200, roomType="Suite", availableFom=date(2025, 8, 2), availableTo=date(2025, 8, 12)),
    Room(hotel_id=hotel6, room_number=501, pricePerNight=170, roomType="Standard", availableFom=date(2025, 6, 10), availableTo=date(2025, 6, 20)),
    Room(hotel_id=hotel6, room_number=502, pricePerNight=190, roomType="Deluxe", availableFom=date(2025, 6, 12), availableTo=date(2025, 6, 22)),
    Room(hotel_id=hotel7, room_number=101, pricePerNight=160, roomType="Standard", availableFom=date(2025, 5, 15), availableTo=date(2025, 5, 25)),
    Room(hotel_id=hotel7, room_number=102, pricePerNight=180, roomType="Suite", availableFom=date(2025, 5, 16), availableTo=date(2025, 5, 26)),
    Room(hotel_id=hotel8, room_number=601, pricePerNight=175, roomType="Deluxe", availableFom=date(2025, 6, 20), availableTo=date(2025, 6, 30)),
    Room(hotel_id=hotel8, room_number=602, pricePerNight=165, roomType="Standard", availableFom=date(2025, 6, 21), availableTo=date(2025, 7, 1)),
    Room(hotel_id=hotel9, room_number=701, pricePerNight=210, roomType="Executive", availableFom=date(2025, 8, 10), availableTo=date(2025, 8, 20)),
    Room(hotel_id=hotel9, room_number=702, pricePerNight=190, roomType="Standard", availableFom=date(2025, 8, 11), availableTo=date(2025, 8, 21)),
])
