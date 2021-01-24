
def ask_ques_1():
    print('[1] Who is the father of computer ?')
    return input('ans : ')
def check_ques1_ans(answer):
    return answer == 'charles babbage'

def ask_ques_2():
    print('[2] Who is the father of India ?')
    return input('ans : ')
def check_ques2_ans(answer):
    return answer == 'mahatma gandhi'

def ask_ques_3():
    print('[3] Who is the father of history ?')
    return input('ans : ')
def check_ques3_ans(answer):
    return answer == 'herodotus'

# Quiz game
score = 0
questions = 3
game_running = True

print("")
print("[ Quiz Game ] made by Badal Singhania")
print("")

player = input("Enter your Name : ")

while (game_running):
    print("")
    if check_ques1_ans(ask_ques_1()):
        score += 1
    else:
        pass

    print("")

    if check_ques2_ans(ask_ques_2()):
        score += 1
    else:
        pass

    print("")

    if check_ques3_ans(ask_ques_3()):
        score += 1
    else:
        pass

    print("")

    print("Score : " + str(score) + " out of 3")
    print("")

    if score == questions:
        print("You win! " + player + " :(")
    else:
        print("You loose! " + player + " :)")

    while (True):
        print("")
        game_restart = input("Do you wanna restart (y/n) : ")

        if game_restart == "y":
            break
        elif game_restart == "n":
            game_running = False
            break
        else:
            pass
