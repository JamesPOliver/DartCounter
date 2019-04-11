import os
p1_name = input("Enter name for player 1: ")
p2_name = input("Enter name for player 2: ")
p1_score = 501
p2_score = 501
temp_score = 0
print(p1_name, "starts.")
while p1_score != 0 and p2_score != 0:
    print(p1_name)
    for i in range(0, 3):
        if p1_score == 0:
            print(p1_name, "wins.")
            os._exit
        elif p2_score == 0:
            print(p2_name, "wins.")
            os.exit
        temp_score = int(input("Enter score from dart: "))
        score_type = int(input("If single, enter 1. If double, enter 2. If treble, enter 3:"))
        if score_type == 1:
            p1_score -= temp_score
        elif score_type == 2:
            p1_score -= (temp_score * 2)
        else:
            p1_score -= (temp_score * 3)
        print(p1_score)
    print(p2_name)
    for i in range(0, 3):
        if p1_score == 0:
            print(p1_name, "wins.")
        elif p2_score == 0:
            print(p2_name, "wins.")
        temp_score = int(input("Enter score from dart: "))
        score_type = int(input("If single, enter 1. If double, enter 2. If treble, enter 3:"))
        if score_type == 1:
            p2_score -= temp_score
        elif score_type == 2:
            p2_score -= (temp_score * 2)
        else:
            p2_score -= (temp_score * 3)
        print(p2_score)
