class Pokemon:
    """
        This class is a template for Pokémon in the game.

        Attributes:
        - name: The name of the Pokémon.
        - type: The type of the Pokémon (e.g., Fire, Water).
        - hp: The health points of the Pokémon.
        - attack: The attack stat of the Pokémon.
        - defense: The defense stat of the Pokémon.
        - moves: A list of moves available to the Pokémon.
        """

    def __init__(self, name, pokemonType, hp, attack, defense, moves):
        """
        Initialize a Pokémon instance.

        :param name: The Pokémon name.
        :param pokemonType: The Pokémon type.
        :param hp: The Pokémon HP.
        :param attack: The Pokémon attack number.
        :param defense: The Pokémon defense number.
        :param moves: The moves of the Pokémon.
        """
        self.name = name
        self.pokemonType = pokemonType
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.moves = moves







