import random

def game():
    print("You are playing a game")
    score = random.randint(1,100)
    with open("scorefile.txt") as f:
        hiscore = f.read()
        if(hiscore != ""):
            hiscore = int(hiscore)
        else:
            hiscore = 0
    
    print(f"Your Score: {score}")
    if(score>hiscore):
        with open("scorefile.txt","w") as f:
            f.write(str(score))

    return score

game()
        
        