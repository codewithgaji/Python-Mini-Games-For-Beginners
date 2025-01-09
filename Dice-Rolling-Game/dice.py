import random
import time


# This function is used to make the outputs display lively
def type_text(text, delay=0.009):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(delay)
    print()


def dice_rolling():
    type_text("WELCOME TO THE DICE ROLLING COMPETITION 🎲")
    type_text("You have 3 attempts to learn something from Albert Einstein :) ")
    type_text("In order to make this a fun game, if you are able to roll a'6'")
    type_text("you will be told 3 different facts you most likely didn't know\n")
    type_text(
        "If you are able to roll a 5 as in (2025), You will be told 2 different Facts you most likely didn't know")
    type_text("If you roll any other numbers apart from this, you will be told 1 Fact\n")
    type_text("Einstein: Hello there friend, in my recent researches, I can tell, you are the next lucky winner")
    type_text("Einstein: Good Luck!")

    number_of_rolls = 0
    attempts = 0
    keep_rolling = True

    interesting_facts = [
        'Fact: Sharks Have Been Around Longer Than Trees:\n Sharks appeared over 400 million years ago, predating the first trees by about 50 million years.\n They’ve survived multiple mass extinction events! 🦈🌲',
        'Fact: A Day on Venus Is Longer Than Its Year:\n Venus takes 243 Earth days to rotate once on its axis but only 225 Earth days to complete one orbit around the Sun.\n That means a day is longer than a year on Venus. 🪐🕰️',
        "Fact: Nigeria Is Home to the World's Largest Diversity of Butterflies: \nThe country boasts one of the richest collections of butterflies in the world,\n especially in the Cross River State rainforest, a biodiversity hotspot. 🦋🌴",
        "Fact: Nigeria Has the Longest Bridge in West Africa: \nThe Third Mainland Bridge in Lagos spans 11.8 kilometers (7.3 miles) and was the longest bridge in Africa until 1996. \n It connects Lagos Island to the mainland and is a vital part of the city's \nbustling transportation network. 🌉🇳🇬",
        "Fact: Nigeria Is Almost Evenly Split Between Christianity and Islam: \nNigeria is unique in its religious diversity, \nwith Islam being predominant in the north and Christianity in the south.\n This makes it one of the few countries in the world with such a nearly equal balance between the two major religions. \nTraditional African religions are also practiced by some communities, \nadding to the country’s rich cultural and religious mosaic. 🕌⛪✨",
        "Fact: There Are More Stars in the Universe Than Grains of Sand on Earth:\n Astronomers estimate there are 1 sextillion stars (that’s a 1 followed by 21 zeros), outnumbering all the grains of sand on every beach and desert. 🌌✨",
        "Fact: Octopuses Have Three Hearts:Two hearts pump blood to the gills, \nwhile the third pumps it to the rest of the body. Fun twist: \nThe heart that supplies the body stops beating when the octopus swims. 🐙❤️",
        "Fact: Bananas Are Berries, But Strawberries Aren't: \nBotanically, bananas qualify as berries because they develop from a single flower with one ovary. \nStrawberries, however, don’t meet the criteria because their seeds form on the outside,\n and they come from a flower with multiple ovaries. 🍌🍓",
        "Fact: The Yoruba Have a Special Greeting for Almost Every Situation:\nIn Yoruba culture, there’s a specific greeting for practically every activity or scenario\n—whether you’re eating, working, waking up, or even sneezing! For example:\n“E ku ise” (Well done) when someone is working.\n“E ku oru” (Well done for enduring the heat) during hot weather.\n“E ku irin” (Well done for walking) if you’re just walking by! \nIt’s both funny and heartwarming how much effort goes into acknowledging daily activities. :) "]

    player_name = input("Please input your name? ").upper()
    print(f"Welcome {player_name}")

    while keep_rolling:
        player_attempt = input("Would you like to roll the dice, (yes/no)? ").lower()
        if player_attempt.lower() in ["yes", 'okay', 'sure', 'yeah', 'definetly']:
            dice_num = random.randint(1, 6)  # This is going to choose numbers between 1 and 6(inclusive)
            print("rolling....")
            time.sleep(1)
            type_text("rolling....")
            time.sleep(1)
            type_text("......")
            print(dice_num)
            print("\n")

            number_of_rolls += 1
            attempts += 1

            if dice_num == 6:
                print(f"Awesome {player_name}, You've got the biggest number, enjoy learning :) \n")
                for _ in range(3):
                    type_text(random.choice(interesting_facts) + "\n")
            elif dice_num == 5:
                for _ in range(2):
                    type_text(random.choice(interesting_facts) + "\n")
            else:
                type_text(random.choice(interesting_facts) + "\n")


        elif player_attempt == "no":
            print(f"You rolled the dice {number_of_rolls} times ")
            print("Einstein: Hope you learnt something new today? Until next time, bye :) ")
            print("Thanks for playing!")
            break

        else:
            print("Invalid input, please enter 'yes' or 'no' ")
            attempts -= 1  # This would ensure the invalid input isn't counted as an attempt

        if attempts >= 3:
            print("You've used all your attempts! Thanks for playing!")
            break


dice_rolling()