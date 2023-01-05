from .classes import *
from .assets import *

def get_func(func: str, *args) -> function:
    def wood_sword(player: Player):
        player.character.attack += 10

    def hero_legend(player: Player, game: Game):
        player.character.hp += 100
        game.data_temp["damage_add_temp"] = 10

    funcs = {"木剑": wood_sword}
    return funcs[func]