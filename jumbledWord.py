import random
myDict = {"unicorn": "a fantasy animal", "Jerry": "Tom and ___?" , "pomegranate": "shrub or small tree having large red many-seeded fruit", "hefty": "of considerable weight and size", "cordial": "politely warm and friendly", "utopian": "of or pertaining to or resembling a utopia"}
score = 0

def shuffle(word):
    word = ''.join(random.sample(word, len(word)))
    return word

while True:
    print("Wanna play a game of Guess the jumbled word? (y/n)")
    reply = input()
    if reply == "n":
        break
    elif reply == "y":
        for k,v in myDict.items():
            print("Word : " + shuffle(k) + ". Hint : " + v)
            print("Whats the word?")
            guess = input()
            if guess == k:
                print("You got it right! The word is " + k)
                score += 1
                print("Your score is " + str(score))
            else:
                print("Sorry, you got it wrong. The right word is: " + k)
                print("Your score is " + str(score))
            print("Wanna play again? (y/n)")
            reply = input()
            if reply == "n":
                break
            elif reply == "y":
                continue
            else:
                print("Please reply 'y' or 'n' for Yes or No, respectively")
                reply= input()
                if reply == "y":
                    continue
                else:
                    break

    else:
        print("Please reply 'y' or 'n' for Yes or No, respectively")
        reply= input()
        if reply == "y":
            continue
        else:
            break
    print("Your total score is " + str(score) + ". Thank you for playing.")

    break
 
