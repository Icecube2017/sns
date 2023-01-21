import assets, classes


dice = classes.dice


def get_func(func: str, *args):
    def _group_attack_judge(player: classes.Player) -> bool:
        _ = True
        _ = _ & (player.character.id in ["奈普斯特"])
        _ = _ & (("闪避" in player.character.status.keys()) & ("凛冰之拥" not in player.character.status.keys()))

    def end_crystal(player: classes.Player, game: classes.Game):
        _empty_pl = classes.Player(5364, -100, "None")
        _damage = classes.Damage(_empty_pl, player)
        _damage.ishplost = True
        _damage.damage_point = 30 + dice(4, 2) * 15
        _damage.damage()
        _dmg_point = 40 + dice(8, 1) * 15
        # player.character.hp -= 30 + dice(4, 2) * 15
        for pl in game.players.values():
            if player.name != pl.name\
                and pl.character.status.values() not in ["咕了"]\
                and not (pl.character.status.values() in ["梦境"] and player.character.id == "卿别") :
                _damage2 = classes.Damage(player, pl)
                _damage2.isaoe = True
                _damage2.damage_point = _dmg_point
                _damage2.damage()


    def hero_legend(player: classes.Player, game: classes.Game, damage: classes.Damage):
        player.character.hp += 100
        damage.atk_plus += 20
        player.character.hidden_status["hero"] = -1
    
    def wood_sword(player: classes.Player):
        player.character.attack += 10

    def shield(player: classes.Player):
        player.character.armor += 100
        player.character.defense += 5
    
    def ascension_stairs(player: classes.Player, game: classes.Game):
        _empty_pl = classes.Player(1013, -101, "None")
        _damage = classes.Damage(_empty_pl, player)
        _damage.ishplost = True
        _damage.damage_point = 0.1*player.character.max_hp
        _damage.damage()
        _min = 6
        _max = 1
        _target = []
        # player.character.hp -= 0.1*player.character.max_hp
        for pl in game.players.values():
            if player.name != pl.name\
                and pl.character.status.values() not in ["咕了"]\
                and not (pl.character.status.values() in ["梦境"] and player.character.id == "卿别") :
                _dice = dice(6, 1)
                if _dice < _min: 
                    _min = _dice
                    _target = [pl]
                elif _dice == _min: _target.append(pl)
                if _dice > _max: _max = _dice
        _dmg_point = _max * 50
        for pl2 in _target:
            _damage2 = classes.Damage(player, pl2)
            _damage2.isaoe = True
            _damage2.damage_point = _dmg_point
            _damage2.damage()


    
    def critical_strike(player: classes.Player, damage: classes.Damage):
        player.character.hidden_status["piercing"] = -1
        damage.ispierce = True

    def self_curing(player: classes.Player, damage: classes.Damage):
        damage.isheal = True
        damage.damage_point = 120

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

    def hexastal(player: classes.Player, damage: classes.Damage):
        damage.dice_size = 6

    def octastal(player: classes.Player, damage: classes.Damage):
        damage.dice_size = 8

    def decastal(player: classes.Player, damage: classes.Damage):
        damage.dice_size = 10

    def camelias_drill(player: classes.Player):
        player.character.hidden_status["_pre_drill"] = -1

    def fragment(player: classes.Player, game: classes.Game, damage: classes.Damage):
        player.character.hidden_status["frag"] = -1
        damage.dmg_plus += 45
        game.draw(player.name, 2)

    def data(player: classes.Player):
        for _s in player.skill.keys():
            try:
                player.skill[_s] = assets.SKILL[_s]
            except KeyError:
                player.skill[_s] = assets.PRIVATE_SKILL[_s]

    def deterrent_radiance(player: classes.Player, game: classes.Game, damage: classes.Damage):
        _empty_pl = classes.Player(3496, -135, "None")
        _damage = classes.Damage(_empty_pl, player)
        _damage.ishplost = True
        _damage.damage_point = 50
        _damage.damage()
        damage.isheal = True
        damage.damage_point = 0
        # player.character.hp -= 50
        for pl in game.players.values():
            if dice(2) == 1:
                pl.character.status["浴霸"] = 1

    def netherite_axe(player: classes.Player, target_player:classes.Player, damage: classes.Damage):
        damage.dmg_plus += 90
        player.character.hidden_status["ne_axe"] = -1
        target_player.character.status["破盾"] = 2

    def redstone(target_player: classes.Player, status: str):
        target_player.character.status[status] += 1

    def nanosword(player: classes.Player, damage: classes.Damage):
        player.character.hidden_status["nano"] = -1

    def lead(player: classes.Player, target_player: classes.Player, damage: classes.Damage):
        damage.isheal = True
        damage.damage_point = 0
        player.character.hidden_status["lead"] = -1
    
    def spectral_arrow(target_player: classes.Player):
        target_player.character.hidden_status["spectral"] = -1
    
    def hologram(player: classes.Player, game: classes.Game, damage: classes.Damage):
        damage.isheal = True
        damage.damage_point = 0
        _skill = game.choose_skill(player.name)
        _cd = game.skill_deck.get(_skill)
        player.skill[_skill] = _cd + 1

    def pyrotheum(target_player: classes.Player):
        target_player.character.status["熔岩之触"] = 3
    
    def breath_of_reaper(target_player: classes.Player, damage: classes.Damage):
        damage.dmg_plus += 100
        target_player.character.status["死灵"] = 2
    
    def cryotheum(target_player: classes.Player):
        target_player.character.status["凛冰之拥"] = 2

    def heart_locket(player: classes.Player):
        player.character.defense += 10

    def corrupt_pendant(player: classes.Player, target_player: classes.Player):
        player.character.hp += 60
        player.character.attack += 5
        target_player.character.hp -= 60
        target_player.character.attack -= 5

    def amethyst(player: classes.Player, damage: classes.Damage, decide:bool):
        damage.dmg_plus += 35
        if decide == True:
            _dice = dice(2, 1)
            if _dice == 2: damage.dmg_plus -= 45
            elif _dice == 1: damage.dmg_plus += 45

    def bow(player: classes.Player, damage: classes.Damage):
        pass

    def tracking_arrow(player: classes.Player, damage: classes.Damage):
        damage.ispierce = True

    def penetrating_arrow(player: classes.Player, damage: classes.Damage):
        damage.ispierce = True

    def end_halberd(player: classes.Player, damage: classes.Damage):
        damage.dmg_multi *= 1.5

    def slowness(player: classes.Player):
        player.character.status["迟缓"] = 2

    def swiftness(player: classes.Player):
        player.character.status["迅捷"] = 2

    def invisibility(player: classes.Player):
        player.character.status["闪避"] = 2

    funcs = {"末影水晶":end_crystal, "木剑": wood_sword, "英雄传说": hero_legend, "登神的长阶":ascension_stairs,
    "无敌贯通":critical_strike, "盾牌": shield, "自疗": self_curing, "再生":regeneration, "力量药水":strength, 
    "力量药水II":strength_ii, "六方棱":hexastal, "八重镜":octastal, "十面璃":decastal,"山茶花的电钻":camelias_drill,
    "残片":fragment, "Data":data, "慑敌辉光":deterrent_radiance, "下界合金斧":netherite_axe,"红石":redstone, 
    "纳米剑":nanosword, "栓绳":lead, "光灵箭":spectral_arrow, "全息投影":hologram,
    "烈焰之炽焱":pyrotheum, "死神之息":breath_of_reaper, "极寒之凛冰":cryotheum, "心形挂坠盒": heart_locket, 
    "堕灵吊坠": corrupt_pendant, "紫水晶":amethyst, "弓":bow, "追踪箭":tracking_arrow, "破甲箭":penetrating_arrow, 
    "终焉长戟":end_halberd, "迟缓药水":slowness, "迅捷药水":swiftness, "隐身药水":invisibility}
    return funcs[func]
