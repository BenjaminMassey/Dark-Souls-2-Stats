# Copyright (c) 2014 Benjamin Massey
# Dark Souls II stats calculator

# This program is available under the MIT License.
# Please see the file COPYING in this distribution
# for license information.

# Level

level = int(input("Please enter your soul level: "))

LevelHealth = 0

# Vigor
# The calculations for health are very strange, so these
# are purely estimates.

vigor = int(input("Please enter your vigor: "))

#Endurance

endurance = int(input("Please enter your endurance: "))

if endurance < 21:
    stamina = 80 + (2 * endurance)

if endurance > 20:
    stamina = 80 + 40 + (endurance - 20)

print("Your character should have " + str(stamina) + " total stamina.")

if endurance <= 20:
    LevelHealth = LevelHealth + (2 * endurance)

elif endurance < 51:
    LevelHealth = LevelHealth + 40 + endurance

else:
    LevelHealth = LevelHealth + 70 + 0


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

if vitality <= 20:
    LevelHealth = LevelHealth + (2 * vitality)

elif vitality < 51:
    LevelHealth = LevelHealth + 40 + vitality

else:
    LevelHealth = LevelHealth + 70 + 0

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

if attunement <= 20:
    LevelHealth = LevelHealth + (2 * attunement)

elif attunement < 51:
    LevelHealth = LevelHealth + 40 + attunement

else:
    LevelHealth = LevelHealth + 70 + 0

#Strength

strength = int(input("Please enter your strength: "))

if strength <= 20:
    LevelHealth = LevelHealth + (2 * strength)

elif strength < 51:
    LevelHealth = LevelHealth + 40 + strength

else:
    LevelHealth = LevelHealth + 70 + 0

#Dexterity

dexterity = int(input("Please enter your dexterity: "))

if dexterity <= 20:
    LevelHealth = LevelHealth + (2 * dexterity)

elif dexterity < 51:
    LevelHealth = LevelHealth + 40 + dexterity

else:
    LevelHealth = LevelHealth + 70 + 0

#Adaptability

adaptability = int(input("Please enter your adaptability: "))

if adaptability <= 20:
    LevelHealth = LevelHealth + (2 * adaptability)

elif adaptability < 51:
    LevelHealth = LevelHealth + 40 + adaptability

else:
    LevelHealth = LevelHealth + 70 + 0

#Intelligence

intelligence = int(input("Please enter your intelligence: "))

if intelligence <= 20:
    LevelHealth = LevelHealth + (2 * intelligence)

elif intelligence < 51:
    LevelHealth = LevelHealth + 40 + intelligence

else:
    LevelHealth = LevelHealth + 70 + 0

#Faith

faith = int(input("Please enter your faith: "))

if faith <= 20:
    LevelHealth = LevelHealth + (2 * faith)

elif faith < 51:
    LevelHealth = LevelHealth + 40 + faith

else:
    LevelHealth = LevelHealth + 70 + 0

#Final Health Calculations

lowvigor = (30 * vigor) + 500 + LevelHealth

if vigor < 20:
    print("Your character should have around " + str(lowvigor) + " HP.")

midvigor = (20 * (vigor - 20)) + 500 + 600 + LevelHealth

if vigor >= 20 and vigor < 50:
    print("Your character should have around " + str(midvigor) + " HP.")

highvigor = (5 * (vigor - 50)) + 500 + 600 + 600 + LevelHealth

if vigor >= 50 and vigor < 100:
    print("Your character should have around " + str(highvigor) + " HP.")

if vigor >= 100:
    print("There must have been an error, since it appears that you have an impossible amount of vigor. Please try again.")
