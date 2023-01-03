from pathlib import Path
from typing import List

from .assets import alias


# 定义玩家类
class Player:
    def __init__(self, order: int = 0,
            name: str = "",
            character: str = "",
            card_count: int = 0,
            skill_1: str = "",
            skill_1_cd: int = 0,
            skill_2: str = "",
            skill_2_cd: int = 0,
            skill_3: str = "",
            skill_3_cd: int = 0) -> None:     # 初始化玩家数据
        self.order = order
        self.name = name
        self.character: object = get_character(character)
        self.card_count = card_count
        self.skill_1 = skill_1
        self.skill_1_cd = skill_1_cd
        self.skill_2 = skill_2
        self.skill_2_cd = skill_2_cd
        self.skill_3 = skill_3
        self.skill_3_cd = skill_3_cd
        self.status: List[int] = []
        self.card: List[str] = ['']     # 初始化玩家手牌


# 定义角色类
class Character:
    def __init__(self, id: str = "",
            health_point: int = 0,
            max_health: int = 0,
            attack: int = 0,
            defense: int = 0,
            move_point: int = 0,
            max_move: int = 0,
            move_regenerate: int = 0,
            regenerate_mechanism: int = 0) -> None:
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
    def __init__(self) -> None:
        self.team: List[str, int] = ['']


# 定义boss类
class Boss:
    def __init__(self) -> None:
        self.data: List[str, int] = ['', 0, 0, 0, 0, '', 0, '', 0, '', 0]


# 定义游戏类
class Game:
    def __init__(self) -> None:
        self.game_sequence: List[str] = []
        self.player_count: int = 0
        self.round: int = 0
        self.turn: int = 0
        self.gametype: int = 0
        self.teams: List[Team] = []


games: List[Game] = []
