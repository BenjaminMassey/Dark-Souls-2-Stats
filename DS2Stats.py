# Copyright (c) 2014 Benjamin Massey
# Dark Souls II stats calculator

# This program is available under the MIT License.
# Please see the file COPYING in this distribution
# for license information.

# Level

level = int(input("Please enter your soul level: "))

if level < 21:
    LevelHealth = (2 * level)

if level > 21:
    LevelHealth = 40 + (level - 20)

# Vigor

vigor = int(input("Please enter your vigor: "))

lowvigor = (30 * vigor) + LevelHealth

if vigor < 21:
    print("Your character should have around " + str(lowvigor) + " HP.")

midvigor = (30 * (vigor - 20)) + 500 + 600 + LevelHealth

if vigor > 20 and vigor < 51:
        print("Your character should have around " + str(midvigor) + " HP.")

#Endurance

endurance = int(input("Please enter your endurance: "))

if endurance < 21:
    stamina = 80 + (2 * endurance)

if endurance > 20:
    stamina = 80 + 40 + (endurance - 20)

print("Your character should have " + str(stamina) + " total stamina.")


#Vitality
        
vitality = int(input("Please enter your vitality: "))

CarryWeight = (1.5 * vitality) + 38.5

if vitality > 29:
    print("Your vitality is too high to perfectly calculate, however it may be around " + str(CarryWeight) + " pounds.")

if vitality <= 29:
    print("You can hold: " + str(CarryWeight) + " pounds.")

carrying = float(input("How many pounds are you carrying?: "))

CarryPercent = round((100 * carrying / CarryWeight), 1)

print("Since you are carrying about " + str(carrying) + " pounds, you should have around " + str(CarryPercent) + "% carry capacity.")

#Attunement

attunement = int(input("Please enter your attunement: "))

if attunement < 10:
    print("You should have no attunement slots")

elif attunement < 14:
    print("You should have one attunement slot")

elif attunement < 16:
    print("You should have two attunement slots")

elif attunement < 20:
    print("You should have three attunemnet slots")

elif attunement < 25:
    print("You should have four attunement slots")

elif attunement < 30:
    print("You should have five attunemnet slots")
    
elif attunement < 40:
    print("You should have six attunement slots")

elif attunement < 50:
    print("You should have seven attunemnet slots")

elif attunement < 60:
    print("You should have eight attunement slots")
    
elif attunement < 75:
        print("You should have nine attunement slots")

else:
        print("You have the maximum attunement slots, 10")
