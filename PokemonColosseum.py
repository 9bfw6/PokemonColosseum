import DataHandler
from Pokemon import Pokemon
import random
from Team import Team

"""

The driver python module. This python module manages the logic of the game.
It starts the program, builds the teams, and manages the game flow.

Author: Brooks Woelfel
N01501458
"""


def main():
    """
    The main function to execute the game.
    :return: None.
    """
    print("Welcome to Pokemon Colosseum!\n")

    DataHandler.read_pokemon_data()  # read in csv Pokémon data
    DataHandler.read_move_data()  # read in csv Pokémon move data

    DataHandler.make_pokemon()  # instantiate Pokémon

    ally_name, enemy_name = DataHandler.gather_team_names()  # gather team players
    ally_pokemon, enemy_pokemon = DataHandler.gather_pokemon()  # gather Pokémon per team, both stored in queues
    team_ally = Team(ally_name, ally_pokemon)  # instantiate ally team
    team_rocket = Team(enemy_name, enemy_pokemon)  # instantiate team rocket

    team_ally.print_team()  # print team ally
    team_rocket.print_team()  # print team rocket
    winner = DataHandler.coin_toss(ally_name, enemy_name)  # start battle and print winner of toss

    if winner.lower() == ally_name.lower():  # assign winner of toss with team one
        team_one = team_ally
        team_two = team_rocket
    else:  # assign winner of toss with team two
        team_one = team_rocket
        team_two = team_ally

    while team_one.pokemon and team_two.pokemon:  # while both teams Pokémon queues are not empty,
        team_one.attack(team_two)
        team_two.attack(team_one)


if __name__ == "__main__":
    main()
