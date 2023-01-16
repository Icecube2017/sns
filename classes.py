import random, math

from typing import List, Dict

import assets

# 自带技能角色忽略技能抽取
SKILL_EXCLUSIVE: Dict[str, list] = {"黯星": ["屠杀", 0], "恋慕": ["氤氲", 4], "卿别": ["窃梦者", 3],
                                    "时雨": ["冰芒", 1], "敏博士": ["异镜解构", 3], "赐弥": ["数据传输", -2]}


def dice(size: int, times: int = 1) -> int:
    _d: int = 0
    for i in range(times):
        _d += random.randint(1, size)
    return _d


class Logger(object):
    def __init__(self, level: str) -> None:
        self.level = f"[{level.upper}]"

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            print(self.level, func(*args, **kwargs))
            return
        return wrapper


# 定义角色类
class Character:
    def __init__(
            self, id: str = "", max_hp: int = 0, attack: int = 0, defense: int = 0,
            max_move: int = 0, move_regenerate: int = 0, regenerate_type: int = 0, regenerate_turns: int = 1
    ) -> None:
        self.id = id
        self.hp = max_hp
        self.max_hp = max_hp
        self.attack = attack
        self.defense = defense
        self.armor: int = 0  # 角色护甲值

        self.damage: Damage = Damage()
        self.damage_recieved_total: int = 0
        self.damage_dealed_total: int = 0

        self.move_point: int = 0
        self.max_move = max_move
        self.move_regenerate = move_regenerate
        self.regenerate_type = regenerate_type
        self.regenerate_turns = regenerate_turns

        self.status: Dict[str, int] = {}  # 初始化角色状态
        self.hidden_status: Dict[str, int] = {}


# 定义玩家类
class Player:
    def __init__(
            self, qq: int, id: int = 0, name: str = "", card_count: int = 0,
            # skill_1: str = "", skill_1_cd: int = 0, skill_2: str = "", skill_2_cd: int = 0, skill_3: str = "", skill_3_cd: int = 0
    ) -> None:  # 初始化玩家数据
        self.id = id  # 玩家编号
        self.name = name  # 玩家昵称
        self.qq = qq  # 玩家QQ号
        self.team: int = 0  # 玩家所在队伍id

        self.character: Character = Character()  # 传入角色数据

        self.skill: Dict[str, int] = {}

        self.card_count = card_count  # 玩家手牌数量
        self.card: List[str] = ['']  # 初始化玩家手牌

        self.attacked: bool = False
        self.data_temp: list = []

    def regenerate(self, round: int) -> str:            # 行动点回复方法
        if round == 0:
            pass
        if round % self.character.regenerate_turns == 0:
            _move_temp = self.character.move_point
            self.character.move_point += self.character.move_regenerate
            if self.character.move_point > self.character.max_move:
                self.character.move_point = self.character.max_move
            return f"行动点已回复 {_move_temp} -> {self.character.move_point}"

    def move_init(self) -> None:
        _rt = self.character.regenerate_type
        _c = self.character
        if _rt == 0:
            _c.move_point = _c.move_regenerate
        elif _rt == 1:
            _c.move_point = 3
        elif _rt == 2:
            _c.move_point = _c.max_move
        elif _rt == 3:
            _c.move_point = math.ceil(float(self.card_count) / 2)
        elif _rt == 4:
            _c.move_point = _c.max_move

    def count_card(self) -> None:
        self.card_count = len(self.card)
        return

    def _has_card(self, card: str) -> bool:  # 判断玩家是否持有手牌
        return True if card in self.card else False

    def set_character(self, c: list) -> str:  # 设置玩家角色
        self.character = Character(c[0], c[1], c[2], c[3], c[4], c[5], c[6], c[7])
        if c[0] == "洛尔":
            self.character.attack = 60 + dice(4, 2) * 5
            self.character.defense = 25 + dice(6) * 5
        return f"{self.name} 选择了角色 {c[0]}"

    def play_card(self, card: str):
        if not self._has_card(card):
            return f"你的手上没有 {card} 哦"
        self.card.remove(card)
        return None

    def player_info(self) -> str:
        _c = self.character
        _st = ""
        if not _c.status:
            _st = "无"
        else:
            for _k, _v in _c.status.items():
                _st += f"{_k}({_v}) "
        if not self.team:
            _t = "无"
        else:
            _t = self.team
        _ret = f"""{_c.id}({self.name}):  手牌:{self.card_count}  队伍:{_t}
  -hp:{_c.hp}({_c.armor})/{_c.max_hp}  atk:{_c.attack}  def:{_c.defense}  mp:{_c.move_point}/{_c.max_move}
  -状态:{_st}"""
        return _ret


# 定义boss类
class Boss:
    def __init__(
            self, max_hp: int = 0, attack: int = 0, defense: int = 0,
            # skill_1: str = "", skill_1_cd: int = 0, skill_2: str = "", skill_2_cd: int = 0, skill_3: str = "", skill_3_cd: int = 0
    ) -> None:
        self.name: str = ""
        self.health_point = max_hp
        self.max_health = max_hp
        self.attack = attack
        self.defense = defense

        self.skill: Dict[str, int] = {}

        self.status: List[int] = []


# 定义队伍类
class Team:
    def __init__(self, *players) -> None:
        self.team_member: List[str] = list(players)  # 队伍成员


"""
class Scene:
    pass
"""


class Damage:
    def __init__(self, source: str, target: Player) -> None:
        self.damage_point: int = 0
        self.source: str = source
        self.target: Player = target
        self.isaoe: bool = False
        self.ispierce: bool = False
        self.ishealthlost: bool = False
        self.isheal: bool = False

        def damage():
            if self.isaoe == True:
                if target.character.id == '奈普斯特':
                    return
            if self.ispierce == False:
                pass
            if self.ishealthlost == True:
                target.character.hp -= self.damage_point
                return
            target.character.hp -= self.damage_point
            return


# 定义游戏类
class Game:
    def __init__(self, game_id: str, starter: str, starter_qq: int, game_type: int, ) -> None:
        self.game_id = game_id  # 局次id作为每场对局的唯一识别码
        self.starter = starter  # 发起人和qq号
        self.starter_qq = starter_qq
        self.game_type = game_type  # 对局类型:0-个人战 1-团队战 2-Boss战

        self.game_status: int = 0  # 游戏状态:0-准备阶段 1-进行中 2-已结束 3-暂停中 4-中途取消
        self.game_sequence: List[int] = []  # 出牌次序
        self.player_count: int = 0  # 玩家数量
        self.round: int = 0  # 游戏轮次
        self.turn: int = 0  # 玩家轮次

        self.players: Dict[str, Player] = {}  # 玩家列表(名字 + 玩家实例)
        self.died: Dict[str, Player] = {}  # 阵亡列表
        self.team_count: int = 0  # 队伍数量
        self.teams: Dict[int, Team] = {}  # 队伍id和队伍列表
        self.scene_on: bool = False  # 场景是否开启
        self.scene: str = ""  # 场景名称

        self.deck: List[str] = []  # 摸牌堆
        self.discard: List[str] = []  # 出牌堆
        self.skill_deck: Dict[str, int] = {}  # 技能及已获取技能
        self.skill_banned: List[str] = []
        self.character_available: Dict[str, list] = {}  # 可用角色
        self.character_banned: List[str] = []  # ban/已使用的角色

        self.cancel_ensure: int = 1  # 确认取消对局
        self.data_temp: dict = {}  # 储存额外数据

    def add_player(self, player_name: str, player_qq):
        self.players[player_name] = Player(qq=player_qq,
            id=self.player_count + 1, name=player_name)
        self.player_count += 1
        return f"{player_name} 加入了对局 {self.game_id}\n目前已有 {self.player_count} 名玩家"

    def move_player(self, player_name: str):
        if self.game_status != 0:  # 判断对局是否在准备状态
            return "你现在不能退出哦"
        try:  # 确认玩家是否在对局中 否则不执行
            _player = self.players[player_name]
        except KeyError:
            return "你还没加入对局哦"
        _id = _player.id
        for player in self.players.values():   # 更改其余玩家的编号
            if player.id > _id:
                player.id -= 1
        self.player_count -= 1  # 对局玩家总数
        if self.game_type == 1:  # 团队战模式中移出团队
            ret = self.quit_team(player_name)
        self.players.pop(player_name)  # 将玩家移出对局

    def player_died(self, player_name: str):
        self.died[player_name] = self.players[player_name]
        self.players.pop(player_name)
        return f"%{player_name} 已阵亡"

    def set_character(self, player_name: str, character: str):
        try:
            _player = self.players[player_name]
        except KeyError:
            return "你还没加入对局哦"
        if self.game_status == 1:
            return "对局已开始"
        if character not in self.character_available:
            return "该角色不存在哦"
        if character in self.character_banned:
            return "该角色已被占用/禁用"
        if _player.character.id:  # 玩家已选择角色时
            # 禁用玩家当前角色 撤销禁用玩家选择的上一个角色
            self.character_banned.append(character)
            _ = self.unban_character(_player.character.id)
            return _player.set_character(self.character_available[character]) + "\n" + _
        else:
            self.character_banned.append(character)
            return _player.set_character(self.character_available[character])

    def ban_character(self, character: str):
        self.character_banned.append(character)
        return f"已禁用角色 {character}"

    def unban_character(self, character: str):
        self.character_banned.remove(character)
        return f"{character} 目前可用"

    def save(self, is_complete: bool, is_canceled: bool = False):
        pass

    def quit_team(self, player_name: str):
        try:  # 确认玩家是否在对局中 否则不执行
            _player = self.players[player_name]
        except KeyError:
            return "你还没加入对局哦"
        if not _player.team:
            return "你还没加入任何队伍哦"
        _id = _player.team
        self.teams[_id].team_member.remove(player_name)
        _player.team = 0
        ret = f"{player_name} 已退出队伍 {_id}"
        if len(self.teams[_id].team_member) == 0:
            for id in self.teams.keys():
                if id > _id:
                    id -= 1
            self.teams.pop(_id)
            self.team_count -= 1
            ret += f"\n队伍 {_id} 人数为0，已清除"
        return ret

    def set_team(self, player_name: str, team_id: int = 0, to_player: str = ""):
        try:
            _player = self.players[player_name]
        except KeyError:
            return "你还没加入对局哦"
        if self.game_type != 1:
            return "当前对局不是团队战哦"
        ret = ""
        if _player.team != 0:
            ret += self.quit_team(player_name) + "\n"
        if not team_id and not to_player:
            team_id = self.team_count + 1
            self.team_count += 1
            self.teams[team_id] = Team(player_name)
            _player.team = team_id
            ret += f"{player_name} 已创建队伍 {team_id}"
        elif team_id and not to_player:
            try:
                self.teams[team_id].team_member.append(player_name)
                _player.team = team_id
                ret += f"{player_name} 已加入队伍 {team_id}"
            except KeyError:
               return f"队伍 {team_id} 不存在"
        elif to_player and not team_id:
            try:
                _player2 = self.players[to_player]
            except KeyError:
                return "玩家不存在"
            if _player2.team:
                team_id = _player2.team
                _player.team = team_id
                self.teams[team_id].team_member.append(player_name)
                ret += f"已加入 {to_player} 所在的队伍 {team_id}"
            else:
                team_id = self.team_count + 1
                self.teams[team_id] = Team(player_name, to_player)
                self.team_count += 1
                _player.team = team_id
                _player2.team = team_id
                ret += f"{player_name} 与 {to_player} 已创建队伍 {team_id}"
        return ret

    def choose_skill(self, player_name: str) -> str:
        _pl = self.players[player_name]
        _s = ""
        _cd = 0
        while not _s and _s not in self.skill_banned:
            _s = random.choice(list(self.skill_deck.keys()))
            _cd = self.skill_deck.get(_s)
        _pl.skill[_s] = _cd + 1
        self.skill_banned.append(_s)
        return _s

    def start_game(self, player_name: str) -> tuple:
        if self.starter != player_name:
            return False, "你不是对局发起人哦"
        if self.player_count < 2:
            return False, "玩家人数小于2，不能开启对局"
        if self.game_status == 1:
            return False, "对局已经开始啦"
        for pl in self.players.values():
            if not pl.character.id:
                return False, "还有玩家没选好角色呢"
        if self.game_type == 0:
            pass
        elif self.game_type == 1:
            if self.team_count < 2:
                return False, "队伍数量小于2 不能开启对局"
            for pl in self.players.values():
                if not pl.team:
                    return False, "还有玩家没有加入队伍哦"
        self.game_status = 1
        self.round = 1
        self.turn = 1
        return True, self._init_game()

    def _init_game(self):
        _ret: Dict[str, dict] = {"group": "", "player": {}}
        self.deck = assets.PROPCARD
        random.shuffle(self.deck)
        self.game_sequence = [i for i in range(1, self.player_count + 1)]
        random.shuffle(self.game_sequence)
        _ret["group"] += "战斗开始！出牌顺序如下——"
        for name, player in self.players.items():
            if player.character.id not in [k for k in SKILL_EXCLUSIVE.keys()]:
                _s1, _s2 = self.choose_skill(name), self.choose_skill(name)
                _ret["player"][player.qq] = {"skill": f"{_s1} {_s2}"}
            else:
                player.skill[SKILL_EXCLUSIVE[player.character.id][0]] = SKILL_EXCLUSIVE[player.character.id][1]
                _ret["player"][player.qq] = {"skill": f"{SKILL_EXCLUSIVE[player.character.id][0]}"}
            _c = self.draw(name, 2)
            _ret["player"][player.qq]["card"] = _c
            if player.id == self.game_sequence[0]:
                _c2 = self.draw(name, 2)
                _ret["player"][player.qq]["card"] += _c2
            player.move_init()
        for i in self.game_sequence:
            for pl in self.players.values():
                if i == pl.id:
                    _ret["group"] += f"\n{pl.player_info()}"
        return _ret

    def draw(self, player_name: str, num: int) -> str:
        _pl = self.players[player_name]
        _ret = ""
        for i in range(num):
            _c = self.deck.pop()
            _pl.card.append(_c)
            _pl.count_card()
            _ret += _c + " "
        return _ret

    def recall(self, card: str):
        self.discard.append(card)
        return

    def recharge(self):
        random.shuffle(self.discard)
        self.deck.extend(self.discard)
        self.discard.clear()
        return
    
    def play_card(self):
        pass
