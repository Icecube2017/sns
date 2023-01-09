from .classes import *
from .assets import *


def get_func(func: str, *args) -> function:
    def wood_sword(player: Player):
        player.character.attack += 10

    def hero_legend(player: Player, game: Game):
        player.character.hp += 100
        game.data_temp["damage_add_temp"] = 10

    def shield(player: Player):
        player.character.armor += 100
        player.character.defense += 5

    def self_cure(player: Player):
        player.character.hp += 120

    def heart_locket(player: Player):
        player.character.defense += 10

    def corrupted_pendant(player: Player, target_player: Player):
        player.character.hp += 60
        player.character.attack += 5
        target_player.character.hp -= 60
        target_player.character.attack -= 5

    funcs = {"木剑": wood_sword, "英雄传说": hero_legend, "盾牌": shield, "自疗": self_cure, "心形挂坠盒": heart_locket,
             "堕灵吊坠": corrupted_pendant}
    return funcs[func]
