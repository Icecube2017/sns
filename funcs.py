import assets, classes


dice = classes.dice


def get_func(func: str, *args):
    def _group_attack_judge(player: classes.Player) -> bool:
        _ = True
        _ = _ & (player.name in ["奈普斯特"])
        _ = _ & (("闪避" in player.character.status.keys()) & ("凛冰之拥" not in player.character.status.keys()))

    def end_crystal(player: classes.Player, game: classes.Game):
        player.character.hp -= 30 + dice(4, 2) * 15
        for pl in game.players.values():
            if player.name != pl.name\
                and pl.name not in ["奈普斯特"]\
                and pl.character.status.values():...

    def wood_sword(player: classes.Player):
        player.character.attack += 10

    def hero_legend(player: classes.Player, game: classes.Game):
        player.character.hp += 100
        player.character.hidden_status["hero"] = -1

    def shield(player: classes.Player):
        player.character.armor += 100
        player.character.defense += 5

    def self_curing(player: classes.Player):
        player.character.hp += 120

    def regeneration(player: classes.Player):
        player.character.status["持续再生"] = 2

    def strength(player: classes.Player):
        if "力量" in player.character.status.keys():
            player.character.status["力量"] += 2
        else:
            player.character.status["力量"] = 2

    def strength_ii(player: classes.Player):
        if "力量II" in player.character.status.keys():
            player.character.status["力量II"] += 2
        else:
            player.character.status["力量II"] = 2

    def hexastal(player: classes.Player):
        player.character.damage.dice_type = 6

    def octastal(player: classes.Player):
        player.character.damage.dice_type = 8

    def decastal(player: classes.Player):
        player.character.damage.dice_type = 10

    def camelias_drill(player: classes.Player):
        player.character.hidden_status["_pre_drill"] = -1

    def fragment(player: classes.Player, game: classes.Game):
        player.character.hidden_status["frag"] = -1
        game.draw(player.name, 2)

    def data(player: classes.Player):
        for _s in player.skill.keys():
            try:
                player.skill[_s] = assets.SKILL[_s]
            except KeyError:
                player.skill[_s] = assets.PRIVATE_SKILL[_s]

    def deterrent_radiance(player: classes.Player, game: classes.Game):
        player.character.hp -= 50
        for pl in game.players.values():
            if dice(2) == 1:
                pl.character.status["浴霸"] = 1

    def netherite_axe(player: classes.Player, target_player:classes.Player):
        player.character.hidden_status["ne_axe"] = -1
        target_player.character.status["破盾"] = 2

    def redstone(target_player: classes.Player, status: str):
        target_player.character.status[status] += 1

    def heart_locket(player: classes.Player):
        player.character.defense += 10

    def corrupt_pendant(player: classes.Player, target_player: classes.Player):
        player.character.hp, player.character.attack += 60, 5
        target_player.character.hp, target_player.character.attack -= 60, 5

    funcs = {"木剑": wood_sword, "英雄传说": hero_legend, "盾牌": shield, "自疗": self_curing, 
    "心形挂坠盒": heart_locket, "堕灵吊坠": corrupt_pendant}
    return funcs[func]
