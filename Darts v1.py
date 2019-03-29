p1_name = input("Enter name for player 1: ")
p2_name = input("Enter name for player 2: ")
p1_score = 501
p2_score = 501
temp_score = 0
print(p1_name, "starts.")
while p1_score != 0 and p2_score != 0:
    print(p1_name)
    for i in range(0, 3):
        temp_score = int(input("Enter score from dart: "))
        p1_score -= temp_score
    print(p1_score)
    print(p2_name)
    for i in range(0, 3):
        temp_score = int(input("Enter score from dart: "))
        p2_score -= temp_score
    print(p2_score)
