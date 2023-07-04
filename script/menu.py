import filter
import os

def title():
    print("""\
  ___          _             _____ _                  ______                     _____ ___  ________ 
 / _ \        | |           /  ___| |                 |  ___|                   /  __ \|  \/  |  _  |
/ /_\ \_ __ __| | ___  ___  \ `--.| |__   ___  _ __   | |_ _ __ ___  _ __ ___   | /  \/| .  . | | | |
|  _  | '__/ _` |/ _ \/ __|  `--. \ '_ \ / _ \| '_ \  |  _| '__/ _ \| '_ ` _ \  | |    | |\/| | | | |
| | | | | | (_| |  __/\__ \ /\__/ / | | | (_) | |_) | | | | | | (_) | | | | | | | \__/\| |  | | |/ / 
\_| |_/_|  \__,_|\___||___/ \____/|_| |_|\___/| .__/  \_| |_|  \___/|_| |_| |_|  \____/\_|  |_/___/  
                                              | |                                                    
                                              |_|                                                    """)


def menu():
    clear = lambda: os.system('cls')

    clear()

    title()

    print("Choose a computer by city availability:\n"
        "\t1. I will shop online\n"
        "\t2. Varna\n"
        "\t3. Sofia\n"
        "\t4. Plovdiv\n"
        "\t5. Burgas\n"
        )

    city = input("Choose from the options above: ")

    try:
        city = int(city)
    except:
        menu()

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
    else:
        menu()

    clear()

    title()

    print("Choose a manufacturer:\n"
        "\t1. Show me every manfucaturer\n"
        "\t2. Ardes\n"
        "\t3. Powered by ASUS\n"
        "\t4. Powered by Fractal Design\n"
        "\t5. Acer\n"
        "\t6. ASUS\n"
        "\t7. Lenovo\n"
        )

    manufacturer = input("Choose from the options above: ")

    try:
        manufacturer = int(manufacturer)
    except:
        menu()

    if manufacturer == 1:
        manufacturer = ""
    elif manufacturer == 2:
        manufacturer = "ardes"
    elif manufacturer == 3:
        manufacturer = "powered-by-asus"
    elif manufacturer == 4:
        manufacturer = "powered-by-fractal-design"
    elif manufacturer == 5:
        manufacturer = "acer"
    elif manufacturer == 6:
        manufacturer = "asus"
    elif manufacturer == 7:
        manufacturer = "lenovo"
    else:
        menu()

    clear()

    title()

    print("Choose a graphics card:\n"
        "\t1. Show me every graphics card\n"
        "\t2. Nvidia GeForce RTX 4080\n"
        "\t3. Nvidia GeForce RTX 4070\n"
        "\t4. Nvidia GeForce RTX 3070\n"
        "\t5. Nvidia GeForce RTX 3060\n"
        "\t6. Nvidia GeForce RTX 3050\n"
        "\t7. Nvidia GeForce RTX 1660\n"
        )

    gcard = input("Choose from the options above: ")

    try:
        gcard = int(gcard)
    except:
        menu()

    if gcard == 1:
        gcard = ""
    elif gcard == 2:
        gcard = "nvidia-geforce-rtx-4080"
    elif gcard == 3:
        gcard = "nvidia-geforce-rtx-4070"
    elif gcard == 4:
        gcard = "nvidia-geforce-rtx-3070"
    elif gcard == 5:
        gcard = "nvidia-geforce-rtx-3060"
    elif gcard == 6:
        gcard = "nvidia-geforce-rtx-3050"
    elif gcard == 7:
        gcard = "nvidia-geforce-gtx-1660"
    else:
        menu()

    clear()

    filter.filter(city, manufacturer, gcard)