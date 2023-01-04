from typing import List, Dict


# 定义角色类
class Character:
    def __init__(
            self, id:str = "", max_hp:int=0, attack:int=0, defense:int=0,
            max_move:int=0, move_regenerate:int=0, regenerate_type:int=0, regenerate_turns:int=1
            ) -> None:
        self.id = id
        self.hp = max_hp
        self.max_health = max_hp
        self.attack = attack
        self.defense = defense
        self.move_point:int = 0
        self.max_move = max_move
        self.move_regenerate = move_regenerate
        self.regenerate_type = regenerate_type
        self.regenerate_turns = regenerate_turns


# 定义玩家类
class Player:
    def __init__(
            self, id: int=0, name:str="", character:str="", card_count: int=0,
            skill_1:str="", skill_1_cd:int=0, skill_2:str="", skill_2_cd:int=0, skill_3:str="", skill_3_cd:int=0
            ) -> None:              # 初始化玩家数据
        self.id = id          # 玩家编号
        self.name = name            # 玩家昵称
        self.team: int = 0

        self.character: Character = Character()     # 传入角色数据

        self.skill_1 = skill_1
        self.skill_1_cd = skill_1_cd
        self.skill_2 = skill_2
        self.skill_2_cd = skill_2_cd
        self.skill_3 = skill_3
        self.skill_3_cd = skill_3_cd

        self.status: List[int] = []     # 初始化玩家状态
        self.card_count = card_count    # 玩家手牌数量
        self.card: List[str] = ['']     # 初始化玩家手牌

    def regenerate(self, round: int) -> str:   # 行动点回复方法
        if round == 0:
            pass
        if round % self.character.regenerate_turns == 0:
            _move_temp = self.character.move_point
            self.character.move_point += self.character.move_regenerate
            if self.character.move_point > self.character.max_move:
                self.character.move_point = self.character.max_move
            return f"行动点已回复 %{_move_temp} -> %{self.character.move_point}"

    def _has_card(self, card: str) -> bool:             # 判断玩家是否持有手牌
        return True if card in self.card else False
    
    def set_character(self, character: Character):      # 设置玩家角色
        self.character = character
        return f"%{self.name} 选择了角色 %{character.id}"


# 定义队伍类
class Team:
    def __init__(self, *players) -> None:
        self.team_member: List[str] = list(players)      # 队伍成员


# 定义boss类
class Boss:
    def __init__(
            self, max_hp:int=0, attack:int=0, defense:int=0,
            skill_1:str="", skill_1_cd:int=0, skill_2:str="", skill_2_cd:int=0, skill_3:str="", skill_3_cd:int=0
            ) -> None:
        self.name:str = ""
        self.health_point = max_hp
        self.max_health = max_hp
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
            deck:List[str]=[], skill_deck: List[str] =[], character_available: Dict[str, Character] = {}
            ) -> None:
        self.game_id = game_id              # 局次id作为每场对局的唯一识别码
        self.starter = starter              # 发起人和qq号
        self.starter_qq = starter_qq
        self.game_type = game_type          # 对局类型:0-个人战 1-团队战 2-Boss战

        self.game_status: int = 0           # 游戏状态:0-准备阶段 1-进行中 2-已结束 3-暂停中 4-中途取消
        self.game_sequence: List[str] = []  # 出牌次序
        self.player_count: int = 0          # 玩家数量
        self.round: int = 0                 # 游戏轮次
        self.turn: int = 0                  # 玩家轮次

        self.players: Dict[str, Player] = []                # 玩家列表(名字 + 玩家实例)
        self.team_count:int = 0             # 队伍数量
        self.teams: Dict[int, Team] = {}    # 队伍id和队伍列表

        self.deck = deck                    # 摸牌堆
        self.discard: List[str] = []        # 出牌堆
        self.skill_deck = skill_deck        # 技能及已获取技能
        self.skill_banned: List[str] = []
        self.character_available = character_available      # 可用角色
        self.character_banned = List[str] = []              # 已使用的角色

        self.cancel_ensure: int = 1         # 确认取消对局

    def add_player(self, player_name: str):
        self.players[player_name] = Player(id=self.player_count+1, name=player_name)
        self.player_count += 1
        return f"%{player_name} 加入了对局 %{self.game_id}\n目前已有 %{self.player_count} 名玩家"
    
    def move_player(self, player_name: str):
        if self.game_status != 0:           # 判断对局是否在准备状态
            return "你现在不能退出哦"
        try:                                # 确认玩家是否在对局中 否则不执行
            _player = self.players[player_name]
        except KeyError:
            return "你还没加入对局哦"
        _id = _player.id
        for name, player in self.players.items():   # 更改其余玩家的编号
            if player.id > _id:
                player.id -= 1
        self.player_count -= 1                      # 对局玩家总数
        if self.game_type == 1:                     # 团队战模式中移出团队
            ret = self.quit_team(player_name)
        self.players.pop(player_name)               # 将玩家移出对局
    
    def set_character(self, player_name: str, character: str):
        try:
            _player = self.players[player_name]
        except KeyError:
            return "你还没加入对局哦"
        if not character in self.character_available:
            return "该角色不存在哦"
        if character in self.character_banned:
            return "该角色已被占用/禁用"
        if _player.character.id:                        # 玩家已选择角色时
            self.character_banned.append(character)     # 禁用玩家当前角色 撤销禁用玩家选择的上一个角色
            _ = self.unban_character(_player.character.id)
            return _player.set_character(self.character_available[character]) + _
        else:
            self.character_banned.append(character)
            return _player.set_character(self.character_available[character])

    def ban_character(self, character: str):
        self.character_banned.append(character)
        return f"已禁用角色 %{character}"
    
    def unban_character(self, character: str):
        self.character_banned.remove(character)
        return f"%{character} 目前可用"
    
    def save(self, is_complete: bool, is_canceled: bool=False):
        pass

    def quit_team(self, player_name: str):
        try:                                # 确认玩家是否在对局中 否则不执行
            _player = self.players[player_name]
        except KeyError:
            return "你还没加入对局哦"
        if not _player.team:
            return "你还没加入任何队伍哦"
        _id = _player.team
        self.teams[_id].team_member.remove(player_name)
        ret = f"%{player_name} 已退出队伍 %{id}"
        if len(self.teams[_id].team_member) == 0:
            for id, team in self.teams.items():
                if id > _id:
                    id -= 1
            self.teams.pop(_id)
            self.team_count -= 1
            ret += f"\n队伍 %{_id} 人数为0 已清除"
        return ret


    def set_team(self, player_name: str, team_id: int=0, to_player: str=""):
        try:
            _player = self.players[player_name]
        except KeyError:
            return "你还没加入对局哦"
        if self.game_type != 1:
            return "当前对局不是团队战哦"
        if not team_id and not to_player:
            return "请选择目标队伍/玩家"
        elif team_id and not to_player:
            try:
                self.teams[team_id].team_member.append(player_name)
                _player.team = team_id
            except KeyError:
                return f"队伍 %{team_id} 不存在"
        elif to_player and not team_id:
            try:
                _player2 = self.players[to_player]
            except KeyError:
                return f"玩家不存在"
            if _player2.team:
                team_id = _player2.team
                self.teams[team_id].team_member.append(player_name)
                return f"已加入 %{to_player}  所在的队伍 %{team_id}"
            else:
                team_id = self.team_count + 1
                self.team_count += 1
                self.teams[team_id] = Team(player_name, to_player)
                _player.team = team_id
                _player2.team = team_id
                return f"%{player_name} 与 %{to_player} 已创建队伍 %{team_id}"
