import pickle
import time
import random

from pathlib import Path
from typing import List, Dict

from .assets import alias


# 初始化游戏存档系统，记录已经进行/正在进行的游戏局次
game_history: List[int, Dict[int, List[str]]] = [0, {0: ["000000-0000"]}]         # [已经进行/正在进行/中途取消的游戏场数, 群号:[局次id]]
saves_path = Path(__file__).parent / "saves"    # 定义存档目录
try:                                            # 读取/新建游戏局次列表
    with open(saves_path / "saves.pkl", mode="rb") as _temp:
        game_history = pickle.load(_temp)
except FileNotFoundError:
    with open(saves_path / "saves.pkl", "wb") as _temp:
        pickle.dump(game_history, _temp)


# 定义玩家类
class Player:
    def __init__(
            self, order: int=0, name:str="", character:str="", card_count: int=0,
            skill_1:str="", skill_1_cd:int=0, skill_2:str="", skill_2_cd:int=0, skill_3:str="", skill_3_cd:int=0
            ) -> None:     # 初始化玩家数据
        self.order = order          # 玩家编号
        self.name = name            # 玩家昵称
        self.character: Character = Character()     # 传入角色数据
        self.card_count = card_count                # 玩家手牌数量
        self.skill_1 = skill_1
        self.skill_1_cd = skill_1_cd
        self.skill_2 = skill_2
        self.skill_2_cd = skill_2_cd
        self.skill_3 = skill_3
        self.skill_3_cd = skill_3_cd
        self.status: List[int] = []     # 初始化玩家状态
        self.card: List[str] = ['']     # 初始化玩家手牌


# 定义角色类
class Character:
    def __init__(
            self, id:str = "", health_point:int=0, max_health:int=0, attack:int=0, defense:int=0,
            move_point:int=0, max_move:int=0, move_regenerate:int=0, regenerate_mechanism:int=0
            ) -> None:
        self.id = id
        self.health_point = health_point
        self.max_health = max_health
        self.attack = attack
        self.defense = defense
        self.move_point = move_point
        self.max_move = max_move
        self.move_regenerate = move_regenerate
        self.regenerate_mechanism = regenerate_mechanism


def get_character(id: str) -> object:
    pass


# 定义队伍类
class Team:
    def __init__(self) -> None:         # 我也不知道怎么用先放在这里
        self.team: List[str, int] = ['']


# 定义boss类
class Boss:
    def __init__(
            self, health_point:int=0, max_health:int=0, attack:int=0, defense:int=0,
            skill_1:str="", skill_1_cd:int=0, skill_2:str="", skill_2_cd:int=0, skill_3:str="", skill_3_cd:int=0
            ) -> None:
        self.name:str = ""
        self.health_point = health_point
        self.max_health = max_health
        self.attack = attack
        self.defense = defense
        self.skill_1 = skill_1
        self.skill_1_cd = skill_1_cd
        self.skill_2 = skill_2
        self.skill_2_cd = skill_2_cd
        self.skill_3 = skill_3
        self.skill_3_cd = skill_3_cd
        self.status: List[int] = []


# 定义游戏类
class Game:
    def __init__(
            self, game_id:int, starter:str, starter_qq:int, game_type:int,
            deck:List[str]=[], skill_deck: List[str] =[],
            ) -> None:
        self.game_id = game_id              # 局次id作为每场对局的唯一识别码
        self.starter = starter              # 发起人和qq号
        self.starter_qq = starter_qq
        self.game_type = game_type          # 对局类型

        self.game_status: int = 0           # 游戏状态:0-准备阶段 1-进行中 2-已结束 3-暂停中 4-中途取消
        self.game_sequence: List[str] = []  # 出牌次序
        self.player_count: int = 0          # 玩家数量
        self.round: int = 0                 # 游戏轮次
        self.turn: int = 0                  # 玩家轮次

        self.players: Dict[str, Player] = []         # 玩家列表(名字 + 玩家实例)
        self.teams: List[Team] = []         # 队伍列表

        self.deck = deck                    # 摸牌堆
        self.discard: List[str] = []        # 出牌堆
        self.skill_deck = skill_deck        # 技能及已获取技能
        self.skill_fetched: List[str] = []
        self.character_fetched = List[str] = []     # 已使用的角色

        self.cancel_ensure: int = 1         # 确认取消对局


playing_games: Dict[int, Game] = {}         # 群号 + 游戏实例
game_temp: Dict[str, List[Game]] = {}       # 暂时存储对局初始状态和对局最终状态


def random_string(length:int=4):            # 随机字符串生成器 参数为字符串长度
    string="1234567890abcdefghijklmnopqrstuvwxyz1234567890"
    ret = ""
    for i in range(length):
        ret.join(random.choice(string))
    return ret


# 以下所有 gid 均表示 qq群号

def new_game(gid:int, starter:str, starter_qq:int, game_type:int=-1, length:int=4) -> str:
    if playing_games[gid]:
        return "已有对局准备着中"
    if type == -1:
        return "还没有指定对局类型哦"
    game_id = time.strftime("%y%m%d-", time.localtime()).join(random_string(length))        # 通过日期和随机十六进制数确定对局id
    playing_games[gid] = Game(game_id=game_id, game_type=game_type)                         # 将游戏实例加入游戏列表
    type_name = {"个人战", "团队战", "Boss战"}[game_type]
    return f"由 %{starter} 发起的 Strife & Strike %{type_name} 开始招募选手了！"


def save_game(id:str, is_complete:bool, is_canceled:bool=False):                            # 保存对局状态及对局过程日志
    pass


def cancel_game(gid:int, sender_qq:str) -> str:
    game_now = playing_games[gid]
    if not game_now:
        return "没有对局正在进行哦"
    if game_now.starter_qq != sender_qq:
        return f"只有对局的发起人 %{playing_games[gid].starter} 才能取消对局哦"
    if game_now.game_status == 0:
        playing_games.pop(gid)
        return "对局取消成功"
    elif game_now.game_status == 1:
        if game_now.cancel_ensure == 1:
            game_now.cancel_ensure -= 1
            return "请再次发送指令以取消对局"
        if game_now.cancel_ensure == 0:                                                     # 二次确认取消正在进行的对局
            game_now.game_status = 4
            game_temp[game_now.game_id][1] = game_now
            save_game(game_now.game_id, False, True)
            playing_games.pop(gid)
            return f"对局%{game_now.game_id}取消成功，存档和记录已保存"


def pause_game(gid:int, sender_qq:str) -> str:
    game_now = playing_games[gid]
    if not game_now:
        return "没有对局正在进行哦"
    if game_now.starter_qq != sender_qq:
        return f"只有对局的发起人 %{playing_games[gid].starter} 才能暂停对局哦"
    if game_now.game_status == 0:
        return "游戏还在准备阶段呢"
    game_now.game_status = 3
    game_temp[game_now.game_id][1] = game_now
    save_game(game_now.game_id, False)
    return f"对局%{game_now.game_id}暂停成功"


def join_game(gid:int, player_name:str):
    game_now = playing_games[gid]
    if not game_now:
        return "没有对局正在进行哦"
    if game_now.game_status == 1:
        return "对局已经开始了哦"
    game_now.players[player_name] = Player(order=game_now.player_count+1, name=player_name)
    game_now.player_count += 1