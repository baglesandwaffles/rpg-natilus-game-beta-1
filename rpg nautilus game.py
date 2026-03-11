import random as rand
import time as gmt
from colorama import init, Fore, Style
init(autoreset=True)
red = Fore.RED      # red text
green = Fore.GREEN    # green text
yellow = Fore.YELLOW   # yellow text
cyan = Fore.CYAN     # cyan text
magenta = Fore.MAGENTA  # purple-ish text
white = Fore.WHITE    # normal white
blue = Fore.BLUE 
lime = Style.BRIGHT + Fore.GREEN
purple = Style.DIM + Fore.MAGENTA
orange = Style.BRIGHT + Fore.RED
dark_cyan = Style.DIM + Fore.CYAN
light_blue = Style.BRIGHT + Fore.BLUE
print(f"This is relice {magenta}1 {blue}beta")
crit_chance = 10 # 10 = 10%, 9 = 20% ect to 0 = 100%
crit_damage = 0
sword = rand.randint(0, 1000)
common = white + "common"
uncommon = lime + "uncommon"
rare = blue + "rare"
epic = purple + "epic"
legendary = orange + "LEGENDARY"
mythic = dark_cyan + "MYTHIC"
ADMIN = red + "[ADMIN]"
def no_keep():
    rarity = "fail"
    player_damage = 2
mode = input(f"pick difficulty: \n{light_blue}baby{white}, {lime}easy{white}, normal, {red}hard{white}, {orange}extreem{white} or {red}HARDCORE(hc){yellow}Comeing soon{white}")
admin_password = "¬TURt;e@cps"
pass_gess = input("I love turtles")
if admin_password == pass_gess:
    sword = 1000
    rarity = ADMIN
    print(f"Hi {cyan}[{red}ADMIN{cyan}]{white}You Got An {cyan}[{red}ADMIN{cyan}]{white} Item!!!")
else:
    print("roling sword")
    gmt.sleep(1)
    print("chances(to 10 d.p): \nCommon = 76.8693567900% \nUncommon = 19.9800199800% \nRare = 2.7254745300% \nEpic = 0.4755289700 \nLegendary: 0.0494000500% \nMythic: 0.0001098900 \nADMIN = 0.0000000000000001%")
    gmt.sleep(1)
    print("picking")
    gmt.sleep(5)
    rarity = "fallback.err.woof"
    player_damage = 1
    if sword <= 100:
        rarity = common
        player_damage = sword / 10
    elif sword >= 101 and sword <= 500:
        keep = rand.randint(0, 1)
        if keep == 1:
            rarity = uncommon
            player_damage = 2 * sword
        else:
             no_keep()
    elif sword >= 501 and sword <= 800:
        keep = rand.randint(0, 10)
        if keep == 10:
            rarity = rare
            player_damage = 2 * sword
        else:
            no_keep()
    elif sword >= 801 and sword <= 900:
        keep = rand.randint(0, 20)
        if keep == 20:
            rarity = epic
            player_damage = 2 * sword
        else:
             no_keep()
    elif sword >= 901 and sword <= 950:
        keep = rand.randint(0, 100)
        if keep == 100:
            rarity = legendary
            player_damage = 2 * sword
        else:
            no_keep()
    elif sword >= 951 and sword <= 961:
        keep = rand.randint(0, 10000)
        if keep == 777:
            keep = rand.randint(1,10**18)
            if keep == 777:
                print(f"{red}YOU GOT AN {ADMIN} ITEM WITH OUT ADMIN {cyan}GG")
                rarity = ADMIN
                player_damage = 10 * sword
            else:
                raise ValueError("FAILED TO KEEP ADMIN ITEM")
        elif keep == 10000:
            rarity = mythic
            player_damage = 2 * sword
        else:
            no_keep()
    else:
        pass

def role():
    role = rand.randint(20, 100)
    return role
player_hp = role()
nautilus_hp = 1
if mode == "baby":
    nautilus_hp = 1
elif mode == "easy":
    nautilus_hp = rand.randint(0, 10)
elif mode == "normal":
    nautilus_hp = role()
elif mode == "hard":
    nautilus_hp = role() * 10
elif mode == "extreem":
    nautilus_hp = role() ** role()
nautilus_hearts = nautilus_hp // 2
player_hearts = player_hp // 2
def crit_output():
    if crit_chance != 0:
        crit_y_n = rand.randint(0, crit_chance)
        if crit_y_n == 0:
            crit_damage = player_damage * 2
            nautilus_hp = nautilus_hp - crit_damage
        else:
            pass
    elif crit_chance == 0:
        crit_damage = player_damage * 2
    return player_damage
gmt.sleep(1)
print(f"You got a {rarity} item")
gmt.sleep(1)
if nautilus_hp <= 50:
    print(f"you have {player_hp}hp\nThe nautilus has showed up with {nautilus_hp}hp")
elif nautilus_hp >= 51:
    print(f"You have {player_hp}hp\n{red}THE BOSS HAS SHOWED UP WITH {nautilus_hp}\033[0mhp")
help_q = input("want a starting guide")
if help_q == "yes":
    print("to hit type H")
    print("to do a crit type C but at start there is a 10% chance to crit but you can get upgrades")
else:
     pass
while player_hp > 0 and nautilus_hp > 0:
    c_or_h = input("your turn: ")
    gmt.sleep(1)
    if c_or_h == "c":
        crit_output()
    elif c_or_h == "h":
        nautilus_hp = nautilus_hp - player_damage
    print(f"You did {player_damage}hp\nTHE NAUTILUS NOW HAS {nautilus_hp}hp")
    nautilus_damage = 1
    if mode == "baby":
        pass
    elif mode == "easy":
        nautilus_damage = rand.randint(1, 10)
    elif mode == "normal":
        nautilus_damage = role()
    elif mode == "hard":
        nautilus_damage = role() * rand.randint(2, 7)
    elif mode == "extreem":
        nautilus_damage = role() ** role()
    player_hp = player_hp - nautilus_damage
    print(f"The nautilus did {nautilus_damage}hp \nyou now have {player_hp}hp")
if player_hp <= 0:
    print(f"{red}------------------------------------------------YOU LOSE------------------")
    print(f"THE {yellow}PUFFERFISH {white}HAD TO {red}EVACUATE {white}BUT SOME {yellow}PUFFERFISH {red}DIDN'T MAKE IT OUT ALIVE")
elif nautilus_hp <= 0:
    print(f"{lime}-----{green}YOU WIN{lime}-----")
    print(f"THE {yellow}PUFFERFISH{white} CAN LIVE A LONG HAPPY LIFE IN THE CORAL REAF")
input("Press enter to end...")
