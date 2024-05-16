from Pokemon import Pokemon
import DataHandler
import random
import math


class Team:
    """
    This class is responsible for managing team operations,
    as well as managing the game flow.

    Attributes:
        name (str): The name of the team.
        Pokémon (list) The 3 Pokémon objects in each team.
    """

    def __init__(self, name, pokemon):
        """""
        Initialize a Team instance.

        :param name: The name of the team.
        :param pokemon: List of Pokémon objects.
        """

        self.name = name
        self.pokemon = pokemon
        self.used_moves = {pokemon_obj: [] for pokemon_obj in pokemon}  # assigns an empty move list for each Pokémon

    def print_team(self):
        """
        Print the team and its Pokémon.

        :return: None.
        """
        print("Team " + self.name + " enters with " + self.pokemon[0].name + ", " + self.pokemon[1].name + ", and " +
              self.pokemon[2].name + ".\n")

    def attack(self, other_team):
        """
        A method that serves as a template for an attacking team.

        :param other_team: The enemy team.
        :return: None.
        """
        if self.name == "Rocket":  # if team is team Rocket
            if self.pokemon:  # if team instance has Pokémon left
                move_list = self.pokemon[0].moves
                element = random.choice(move_list)

                print(
                    "Team " + self.name + "'s " + self.pokemon[0].name + " cast " + element + " to " +
                    other_team.pokemon[
                        0].name + ":")

                damage_one = self.damage_calculator(element, other_team)
                self.handle_damage(damage_one, other_team)

        else:  # if team is team ally
            if self.pokemon:  # if team instance has Pokémon left
                moves_list = self.pokemon[0].moves
                self.print_menu(moves_list)
                choice = self.player_choice(moves_list)
                move = moves_list[choice - 1]
                print(self.pokemon[0].name + " cast " + move + " to " + other_team.pokemon[
                    0].name)
                damage = self.damage_calculator(move, other_team)
                self.handle_damage(damage, other_team)

    def player_choice(self, moves):
        """
        Handles and validates player move input.
        :param moves: The moves available to the player.
        :return: An integer move choice.
        """
        # this block of code validates that user entered an integer in range
        print("Team " + self.name + "'s choice: ")
        choice = input()
        if not choice.isnumeric() or int(choice) < 1 or int(choice) > len(moves):
            while not choice.isnumeric() or int(choice) < 1 or int(choice) > len(moves):
                choice = input("Not a valid choice. Please enter a number corresponding to a move:\n")
        # this block of code validates that user chose a valid move
        if len(moves) != len(self.used_moves[self.pokemon[0]]):  # if every move hasn't been used
            if choice in self.used_moves[self.pokemon[0]]:
                while choice in self.used_moves[self.pokemon[0]]:
                    choice = input(moves[int(choice) - 1] + " has already been used. Please choose a different move:\n")
            else:
                self.used_moves[self.pokemon[0]].append(choice)
        else:
            self.used_moves[self.pokemon[0]] = []
            self.used_moves[self.pokemon[0]].append(choice)

        self.used_moves[self.pokemon[0]].append(choice)
        return int(choice)

    def handle_damage(self, damage, other_team):
        """
        Handles the damage to enemy Pokémon. If enemy Pokémon faints,
        it is popped from queue.
        :param damage: The numerical damage to enemy Pokémon.
        :param other_team: The other team object.
        :return: None.
        """
        other_team.pokemon[0].hp -= damage
        print("Damage to " + other_team.pokemon[0].name + " is " + str(damage) + " points.")

        # if enemy Pokémon hasn't fainted
        if other_team.pokemon[0].hp > 0:
            print(
                "Now " + self.pokemon[0].name + "has " + str(self.pokemon[0].hp) + " HP, and " +
                other_team.pokemon[
                    0].name + " has " + str(other_team.pokemon[0].hp) + " HP.\n")
        # If enemy Pokémon has fainted
        else:
            print(
                "Now " + self.pokemon[0].name + " has " + str(self.pokemon[0].hp) + " HP, and " +
                other_team.pokemon[
                    0].name + " faints back to poke ball.\n")
            other_team.pokemon.pop(0)  # pops enemy pokemon from queue
            if other_team.pokemon:
                print("Next for Team " + other_team.name + ", " + other_team.pokemon[
                    0].name + " enters battle!\n")
            else:
                print(
                    "All of Team " + other_team.name + "'s Pokemon fainted, and Team " + self.name + " prevails!")

    def print_menu(self, moves_list):
        """
        Prints the move menu to player.
        :param moves_list: The available moves to player.
        :return: None.
        """
        print("Choose the move for " + self.pokemon[0].name + ":\n")

        for index, move in enumerate(moves_list, start=1):
            print(index, move)

    def damage_calculator(self, move, other_team):
        """
        Calculates the damage to the other team's Pokémon.
        :param move: The move causing damage.
        :param other_team: The other team object.
        :return: None.
        """
        move_power = DataHandler.moves_data[move]['Power']
        move_type = DataHandler.moves_data[move]['Type']
        attack = self.pokemon[0].attack
        defense = other_team.pokemon[0].defense
        pokemon_type = self.pokemon[0].pokemonType
        random_number = random.uniform(0.5, 1.0)

        if move_type == "Normal" and other_team.pokemon[
            0].pokemonType in ["Normal", "Fire", "Water", "Electric", "Grass"]:
            te = 1
        elif move_type == "Fire" and other_team.pokemon[0].pokemonType in ["Normal", "Electric"]:
            te = 1
        elif move_type == "Fire" and other_team.pokemon[0].pokemonType in ["Fire" or "Water"]:
            te = 0.5
        elif move_type == "Fire" and other_team.pokemon[0].pokemonType == "Grass":
            te = 2
        elif move_type == "Water" and other_team.pokemon[0].pokemonType in ["Normal", "Electric"]:
            te = 1
        elif move_type == "Water" and other_team.pokemon[0].pokemonType in ["Water", "Grass"]:
            te = 0.5
        elif move_type == "Water" and other_team.pokemon[0].pokemonType == "Fire":
            te = 2
        elif move_type == "Electric" and other_team.pokemon[0].pokemonType in ["Normal", "Fire"]:
            te = 1
        elif move_type == "Electric" and other_team.pokemon[0].pokemonType == "Water":
            te = 2
        elif move_type == "Electric" and other_team.pokemon[0].pokemonType in ["Electric", "Grass"]:
            te = 0.5
        elif move_type == "Grass" and other_team.pokemon[0].pokemonType in ["Normal", "Electric"]:
            te = 1
        elif move_type == "Grass" and other_team.pokemon[0].pokemonType in ["Fire", "Grass"]:
            te = 0.5
        elif move_type == "Grass" and other_team.pokemon[0].pokemonType == "Water":
            te = 2
        else:
            te = 1

        if pokemon_type == move_type:
            stab = 1.5
        else:
            stab = 1

        ratio = attack / defense
        damage = math.ceil(move_power * ratio * stab * te * random_number)
        return damage
