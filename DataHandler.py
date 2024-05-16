import csv
import ast
from Pokemon import Pokemon
from random import sample
from random import randint

"""

The DataHandler module. This module contains functionality for tasks such
as reading data from both Pokemon-data.csv and moves-data.csv, instantiating
Pokemon objects, and gathering information about both teams.

"""

pokemon_data = {}  # dictionary holding pokemon data
moves_data = {}  # dictionary holding move data
pokemon_instances = []  # list containing every Pokémon instance


def read_pokemon_data():
    """
    This function reads in Pokémon data from Pokemon-data.csv and stores it
    in the dictionary pokemon_data.
    :return: None.
    """
    filename = 'pokemon-data.csv'
    header = []

    # Read in Pokémon data to dictionary
    with open(filename) as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        header = next(reader)

        for row in reader:
            name = row[0]
            pokemon_type = row[1]
            hp = int(row[2])
            attack = int(row[3])
            defense = int(row[4])
            moves = ast.literal_eval(row[7])

            pokemon_data[name] = {'Type': pokemon_type, 'HP': hp, 'Attack': attack, 'Defense': defense,
                                  'Moves': moves}


def read_move_data():
    """
    This function reads in Pokémon move data from moves-data.csv and stores it
    in the dictionary moves_data.
    :return: None.
    """
    filename = 'moves-data.csv'
    header = []
    # Read in Moves data to dictionary
    with open(filename) as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        header = next(reader)

        for row in reader:
            name = row[0]
            move_type = row[1]
            move_power = int(row[5])

            moves_data[name] = {'Type': move_type, 'Power': move_power}


def make_pokemon():
    """
    This function creates a list of Pokémon instances from the Pokémon stored
    in pokemon_data.
    :return: None.
    """
    for pokemon in pokemon_data:
        name = pokemon
        pokemon_type = pokemon_data[pokemon]['Type']
        hp = pokemon_data[pokemon]['HP']
        attack = pokemon_data[pokemon]['Attack']
        defense = pokemon_data[pokemon]['Defense']
        moves = pokemon_data[pokemon]['Moves']

        # instantiates new Pokémon object and adds it to pokemon_instances
        new_pokemon = Pokemon(name, pokemon_type, hp, attack, defense, moves)
        pokemon_instances.append(new_pokemon)


def randomize():
    """
    This functions draws three random Pokémon from pokemon_instances and
    returns them to caller.
    :return: A list of three random Pokémon.
    """
    random_pokemon = sample(pokemon_instances, 3)

    for pokemon in random_pokemon:
        pokemon_instances.remove(pokemon)

    return random_pokemon


def gather_team_names():
    """
    This function gathers the names of both teams and returns them to
    the caller.
    :return: Names of both teams.
    """
    ally = input("Enter Player Name: ")
    print("\n")
    enemy = "Rocket"
    return ally, enemy


def gather_pokemon():
    """
    This function gathers the Pokémon for both teams.
    :return: Two lists of three randomly selected Pokémon to caller.
    """
    ally_pokemon = randomize()
    enemy_pokemon = randomize()

    return ally_pokemon, enemy_pokemon


def coin_toss(ally, enemy):
    """
    This function handles coin toss of the game.
    :param ally: The user's team.
    :param enemy: Team Rocket.
    :return: Returns the name of the winner of the coin toss.
    """
    print("Let the battle begin!\n")
    number = randint(0, 1)
    if number == 0:
        print("Coin toss goes to ----- Team " + ally + " to start the attack!")
        print("\n")
        return ally

    else:
        print("Coin toss goes to ----- Team " + enemy + " to start the attack!")
        print("\n")
        return enemy
