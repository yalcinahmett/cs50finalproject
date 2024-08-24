import random

def main():
    names = user()
    teamSelect(names)
    selection(names)

def teamSelect(names):
    teams = [
        "Real Madrid",
        "Barcelona",
        "Bayern Munich",
        "Manchester United",
        "Manchester City",
        "Atletico Madrid",
        "Liverpool",
        "Chelsea",
        "Arsenal",
        "Inter Milan",
        "AC Milan",
        "Juventus",
        "Paris Saint Germain",
        "Borussia Dortmund",
        "Bayer Leverkusen",
        "Ajax",
        "Porto",
        "Benfica",
    ]
    while True:
        prompt = input("Do you want to choose teams(t) or make it random(r)? ")
        if prompt == "r":
            print("You chose random")
            team1 = random.choice(teams)
            teams.remove(team1)
            print(f"{names[0]}: {team1}")

            team2 = random.choice(teams)
            teams.remove(team2)
            print(f"{names[1]}: {team2}")

            team3 = random.choice(teams)
            teams.remove(team3)
            print(f"{names[2]}: {team3}")

            team4 = random.choice(teams)
            teams.remove(team4)
            print(f"{names[3]}: {team4}")
            return team1, team2, team3, team4
        elif prompt == "t":
            print("You can choose teams")
            team1 = input("Write the first team: ")
            team2 = input("Write the second team: ")
            team3 = input("Write the third team: ")
            team4 = input("Write the fourth team: ")
            print(f"{names[0]}: {team1}")
            print(f"{names[1]}: {team2}")
            print(f"{names[2]}: {team3}")
            print(f"{names[3]}: {team4}")
            return team1, team2, team3, team4
        else:
            print("Please write 'r' or 't'")
            continue


def user():
    names = []
    name1 = input("Who is the first player: ")
    names.append(name1)
    name2 = input("Who is the second player: ")
    names.append(name2)
    name3 = input("Who is the third player: ")
    names.append(name3)
    name4 = input("Who is the fourth player: ")
    names.append(name4)
    return names

def group(names):
    scores = {name: 0 for name in names}

    # Match 1: Team 1 vs Team 2
    print(f"First match is '{names[0]} vs {names[1]}'")
    score1 = int(input(f"{names[0]} scored: "))
    score2 = int(input(f"{names[1]} scored: "))
    if score1 > score2:
        print(f"{names[0]} won!")
        scores[names[0]] += 3
    elif score1 < score2:
        print(f"{names[1]} won!")
        scores[names[1]] += 3
    else:
        print("Draw!")
        scores[names[0]] += 1
        scores[names[1]] += 1

    # Match 2: Team 3 vs Team 4
    print(f"Second match is '{names[2]} vs {names[3]}'")
    score1 = int(input(f"{names[2]} scored: "))
    score2 = int(input(f"{names[3]} scored: "))
    if score1 > score2:
        print(f"{names[2]} won!")
        scores[names[2]] += 3
    elif score1 < score2:
        print(f"{names[3]} won!")
        scores[names[3]] += 3
    else:
        print("Draw!")
        scores[names[2]] += 1
        scores[names[3]] += 1

    # Match 3: Team 1 vs Team 3
    print(f"Third match is '{names[0]} vs {names[2]}'")
    score1 = int(input(f"{names[0]} scored: "))
    score2 = int(input(f"{names[2]} scored: "))
    if score1 > score2:
        print(f"{names[0]} won!")
        scores[names[0]] += 3
    elif score1 < score2:
        print(f"{names[2]} won!")
        scores[names[2]] += 3
    else:
        print("Draw!")
        scores[names[0]] += 1
        scores[names[2]] += 1

    # Match 4: Team 2 vs Team 4
    print(f"Fourth match is '{names[1]} vs {names[3]}'")
    score1 = int(input(f"{names[1]} scored: "))
    score2 = int(input(f"{names[3]} scored: "))
    if score1 > score2:
        print(f"{names[1]} won!")
        scores[names[1]] += 3
    elif score1 < score2:
        print(f"{names[3]} won!")
        scores[names[3]] += 3
    else:
        print("Draw!")
        scores[names[1]] += 1
        scores[names[3]] += 1

    # Match 5: Team 1 vs Team 4
    print(f"Fifth match is '{names[0]} vs {names[3]}'")
    score1 = int(input(f"{names[0]} scored: "))
    score2 = int(input(f"{names[3]} scored: "))
    if score1 > score2:
        print(f"{names[0]} won!")
        scores[names[0]] += 3
    elif score1 < score2:
        print(f"{names[3]} won!")
        scores[names[3]] += 3
    else:
        print("Draw!")
        scores[names[0]] += 1
        scores[names[3]] += 1

    # Match 6: Team 2 vs Team 3
    print(f"Sixth match is '{names[1]} vs {names[2]}'")
    score1 = int(input(f"{names[1]} scored: "))
    score2 = int(input(f"{names[2]} scored: "))
    if score1 > score2:
        print(f"{names[1]} won!")
        scores[names[1]] += 3
    elif score1 < score2:
        print(f"{names[2]} won!")
        scores[names[2]] += 3
    else:
        print("Draw!")
        scores[names[1]] += 1
        scores[names[2]] += 1

    # Display final points
    print("\nFinal Points Table:")
    for name, score in scores.items():
        print(f"{name}: {score} points")

    # Determine the winner based on points
    winner = max(scores, key=scores.get)
    print(f"\nThe winner of the group stage is {winner}!")

def knockout(names):
    print("\n--- Knockout Stage ---")
    
    # Semi-Finals
    print(f"Semi-Final 1: {names[0]} vs {names[1]}")
    score1 = int(input(f"{names[0]} scored: "))
    score2 = int(input(f"{names[1]} scored: "))
    if score1 > score2:
        finalist1 = names[0]
        print(f"{names[0]} advances to the final!")
    elif score1 < score2:
        finalist1 = names[1]
        print(f"{names[1]} advances to the final!")
    else:
        print("It's a draw! Deciding by random choice.")
        finalist1 = random.choice([names[0], names[1]])
        print(f"{finalist1} advances to the final!")
    
    print(f"Semi-Final 2: {names[2]} vs {names[3]}")
    score1 = int(input(f"{names[2]} scored: "))
    score2 = int(input(f"{names[3]} scored: "))
    if score1 > score2:
        finalist2 = names[2]
        print(f"{names[2]} advances to the final!")
    elif score1 < score2:
        finalist2 = names[3]
        print(f"{names[3]} advances to the final!")
    else:
        print("It's a draw! Deciding by random choice.")
        finalist2 = random.choice([names[2], names[3]])
        print(f"{finalist2} advances to the final!")
    
    # Final
    print(f"\n--- Final: {finalist1} vs {finalist2} ---")
    score1 = int(input(f"{finalist1} scored: "))
    score2 = int(input(f"{finalist2} scored: "))
    if score1 > score2:
        winner = finalist1
        print(f"{finalist1} wins the championship!")
    elif score1 < score2:
        winner = finalist2
        print(f"{finalist2} wins the championship!")
    else:
        print("It's a draw! Deciding by random choice.")
        winner = random.choice([finalist1, finalist2])
        print(f"{winner} wins the championship!")
    
    print("\nCongratulations to the champion!")

def selection(names):
    while True:
        mode = input("1-Group Stage / 2-Knockout Stage: ")
        if mode == '1':
            print("You chose Group Stage")
            group(names)
            break
        elif mode == '2':
            print("You chose Knockout Stage")
            knockout(names)
            break
        else:
            print("Write '1' or '2'")
            continue

if __name__ == "__main__":
    main()
