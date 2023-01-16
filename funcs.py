import assets, classes


dice = classes.dice


def get_func(func: str, *args):
    def _group_attack_judge(player: classes.Player) -> bool:
        _ = True
        _ = _ & (player.character.id in ["奈普斯特"])
        _ = _ & (("闪避" in player.character.status.keys()) & ("凛冰之拥" not in player.character.status.keys()))

    def end_crystal(player: classes.Player, game: classes.Game):
        player.character.hp -= 30 + dice(4, 2) * 15
        for pl in game.players.values():
            if player.name != pl.name\
                and pl.name not in ["奈普斯特"]\
                and pl.character.status.values():...

    def hero_legend(player: classes.Player, game: classes.Game):
        player.character.hp += 100
        player.character.hidden_status["hero"] = -1
    
    def wood_sword(player: classes.Player):
        player.character.attack += 10

    def shield(player: classes.Player):
        player.character.armor += 100
        player.character.defense += 5
    
    def ascension_stairs(player: classes.Player, game: classes.Game):
        player.character.hp -= 0.1*player.character.max_hp
        for pl in game.players.values():
            if player.name != pl.name\
                and pl.name not in ["奈普斯特"]\
                and pl.character.status.values():...
    
    def critical_strike(player: classes.Player):
        player.character.hidden_status["piercing"] = -1

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

    def nanosword(player: classes.Player):
        player.character.hidden_status["nano"] = -1

    def lead(player: classes.Player, target_player: classes.Player):
        player.character.hidden_status["lead"] = -1
    
    def spectral_arrow(target_player: classes.Player):
        target_player.character.hidden_status["spectral"] = -1
    
    def hologram(player: classes.Player, game: classes.Game):
        _skill = game.choose_skill(player)
        _cd = game.skill_deck.get(_skill)
        player.skill[_skill] = _cd + 1

    def pyrotheum(target_player: classes.Player):
        target_player.character.status["熔岩之触"] = 3
    
    def breath_of_reaper(target_player: classes.Player):
        target_player.character.status["死灵"] = 2
    
    def cryotheum(target_player: classes.Player):
        target_player.character.status["凛冰之拥"] = 2

    def heart_locket(player: classes.Player):
        player.character.defense += 10

    def corrupt_pendant(player: classes.Player, target_player: classes.Player):
        player.character.hp, player.character.attack += 60, 5
        target_player.character.hp, target_player.character.attack -= 60, 5

    def amethyst(player: classes.Player):
        pass

    def bow(player: classes.Player):
        pass

    funcs = {"末影水晶":end_crystal, "木剑": wood_sword, "英雄传说": hero_legend, "登神的长阶":ascension_stairs,
    "无敌贯通":critical_strike, "盾牌": shield, "自疗": self_curing, "再生":regeneration, "力量药水":strength, 
    "力量药水":strength_ii, "六方棱":hexastal, "八重镜":octastal, "十面璃":decastal,
    "山茶花的电钻":camelias_drill, "残片":fragment, "Data":data, "慑敌辉光":deterrent_radiance, "下界合金斧":netherite_axe,
    "红石":redstone, "心形挂坠盒": heart_locket, "堕灵吊坠": corrupt_pendant}
    return funcs[func]
