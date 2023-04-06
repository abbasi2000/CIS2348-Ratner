# 2095022 # EMAD ABBASI
def output_roster(players):
    print("ROSTER")
    for jersey, rating in sorted(players.items()):
        print(f"Jersey number: {jersey}, Rating: {rating}")


def add_player(players):
    jersey = int(input("Enter a new player's jersey number:\n"))
    rating = int(input("Enter the player's rating:\n"))
    players[jersey] = rating


def remove_player(players):
    jersey = int(input("Enter a jersey number:\n"))
    if jersey in players:
        del players[jersey]


def update_player_rating(players):
    jersey = int(input("Enter a jersey number:\n"))
    if jersey in players:
        new_rating = int(input("Enter a new rating for player:\n"))
        players[jersey] = new_rating


def output_players_above_rating(players):
    rating_threshold = int(input("Enter a rating:\n"))
    print(f"\nABOVE {rating_threshold}")
    for jersey, rating in sorted(players.items()):
        if rating > rating_threshold:
            print(f"Jersey number: {jersey}, Rating: {rating}")


def main():
    players = {}

    for i in range(1, 6):
        jersey = int(input(f"Enter player {i}'s jersey number:\n"))
        rating = int(input(f"Enter player {i}'s rating:\n"))
        print()  # Adding a newline after each input prompt
        players[jersey] = rating

    output_roster(players)

    while True:
        print("\nMENU")
        print("a - Add player")
        print("d - Remove player")
        print("u - Update player rating")
        print("r - Output players above a rating")
        print("o - Output roster")
        print("q - Quit\n")

        option = input("Choose an option:\n")

        if option == 'a':
            add_player(players)
        elif option == 'd':
            remove_player(players)
        elif option == 'u':
            update_player_rating(players)
        elif option == 'r':
            output_players_above_rating(players)
        elif option == 'o':
            output_roster(players)
        elif option == 'q':
            break


if __name__ == "__main__":
    main()