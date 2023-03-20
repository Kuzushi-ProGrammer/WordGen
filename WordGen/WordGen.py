import random, time
target = input("Enter word to randomly generate: ")
gen = ""
alphabet = "abcdefghijklmnopqrstuvwxyz"
wordFound = False
countedTime = time.time_ns()
while wordFound == False:
    if gen == target:
        countedTime = time.time_ns() - countedTime
        print(f"Success! The program generated the word {gen} in {countedTime} nanoseconds, {round(countedTime*0.000000001, 4)} seconds or {round((countedTime*0.000000001)/60, 4)} minutes!")
        break
    elif len(gen) >= len(target):
        gen = ""
    else:
        gen = gen + alphabet[random.randrange(0, 24)]