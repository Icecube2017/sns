import assets, classes

def get_func(func: str, *args):
    def wood_sword(player: classes.Player):
        player.character.attack += 10

    def hero_legend(player: classes.Player, game: classes.Game):
        player.character.hp += 100
        game.data_temp["damage_add_temp"] = 10

    def shield(player: classes.Player):
        player.character.armor += 100
        player.character.defense += 5

    def self_cure(player: classes.Player):
        player.character.hp += 120

    def heart_locket(player: classes.Player):
        player.character.defense += 10

    def corrupt_pendant(player: classes.Player, target_player: classes.Player):
        player.character.hp, player.character.attack += 60, 5
        target_player.character.hp, target_player.character.attack -= 60, 5

    funcs = {"木剑": wood_sword, "英雄传说": hero_legend, "盾牌": shield, "自疗": self_cure, 
    "心形挂坠盒": heart_locket, "堕灵吊坠": corrupt_pendant}
    return funcs[func]