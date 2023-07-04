import sortByCity
import os

clear = lambda: os.system('cls')

print("Choose by city availability:\n"
      "1. I will shop online\n"
      "2. Varna\n"
      "3. Sofia\n"
      "4. Plovdiv\n"
      "5. Burgas\n"
      )

city = input("Choose from the options above: ")

city = int(city)

if city == 1:
    city = ""
elif city == 2:
    city = "varna"
elif city == 3:
    city = "sofia"
elif city == 4:
    city = "plovdiv"
elif city == 5:
    city = "burgas"

clear()
sortByCity.cities(city)