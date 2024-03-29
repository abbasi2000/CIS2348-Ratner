# 2095022 # EMAD ABBASI
class Team:
    def __init__(self, team_name='none', team_wins=0, team_losses=0):
        self.team_name = team_name
        self.team_wins = team_wins
        self.team_losses = team_losses

    def get_win_percentage(self):
        return self.team_wins / (self.team_wins + self.team_losses)


def main():
    team_name = input()
    team_wins = int(input())
    team_losses = int(input())

    team = Team(team_name, team_wins, team_losses)
    win_percentage = team.get_win_percentage()

    if win_percentage >= 0.5:
        print(f"Congratulations, Team {team_name} has a winning average!")
    else:
        print(f"Team {team_name} has a losing average.")
