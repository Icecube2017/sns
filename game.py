import pickle
import time
import random

from pathlib import Path
from typing import List, Dict

from .assets import ALIAS, CHARACTER, PROPCARD, SKILL
from .classes import Player, Character, Team, Boss, Game


# 初始化游戏存档系统，记录已经进行/正在进行的游戏局次
game_history: List[int, Dict[int, List[str]]] = [0, {0: ["000000-0000"]}]       # [已经进行/正在进行/中途取消的游戏场数, 群号:[局次id]]

saves_path = Path(__file__).parent / "saves"                                    # 定义存档目录

try:                                                                            # 读取/新建游戏局次列表
    with open(saves_path / "saves.pkl", mode="rb") as _temp:
        game_history = pickle.load(_temp)
except FileNotFoundError:
    with open(saves_path / "saves.pkl", "wb") as _temp:
        pickle.dump(game_history, _temp)


# 群号 + 游戏实例
playing_games: Dict[int, Game] = {}
# 暂时存储对局初始状态和对局最终状态
game_temp: Dict[str, List[Game]] = {}
# 自带技能角色忽略技能抽取
SKILL_IGNORE = ["黯星", "恋慕", "卿别", "时雨", "敏博士", "赐弥"]


# 随机字符串生成器 参数为字符串长度
def random_string(length:int=4):
    string="1234567890abcdefghijklmnopqrstuvwxyz1234567890"
    ret = ""
    for i in range(length):
        ret.join(random.choice(string))
    return ret


# 以下所有"gid"均表示 qq群号
# 新建对局
def new_game(gid:int, starter:str, starter_qq:int, game_type:int=-1, length:int=4) -> str:
    if playing_games[gid]:
        return "已有对局准备中"
    if type == -1:
        return "还没有指定对局类型哦"
    game_id = time.strftime("%y%m%d-", time.localtime()).join(random_string(length))        # 通过日期和随机字符串确定对局id
    playing_games[gid] = Game(
            game_id=game_id, starter=starter, starter_qq= starter_qq, game_type=game_type,
            character_available=CHARACTER
            )                                                                               # 将游戏实例加入游戏列表
    playing_games[gid].skill_deck = SKILL
    type_name = {"个人战", "团队战", "Boss战"}[game_type]
    return f"由 %{starter} 发起的 Strife & Strike %{type_name} 开始招募选手了！"

# 保存对局状态及对局过程日志
def save_game(id:str, is_complete:bool, is_canceled:bool=False):
    pass

# 取消未开始的/正在进行的对局
def cancel_game(gid:int, sender_qq:str) -> str:
    game_now = playing_games[gid]
    if not game_now:                                                                        # 是否有对局在对局列表中
        return "没有对局正在进行哦"
    if game_now.starter_qq != sender_qq:                                                    # 比较命令发送者和发起者qq号 下同
        return f"只有对局的发起人 %{playing_games[gid].starter} 才能取消对局哦"
    if game_now.game_status == 0:                   # 对局未开始
        playing_games.pop(gid)
        return "对局取消成功"
    elif game_now.game_status == 1:                 # 对局进行中
        if game_now.cancel_ensure == 1:
            game_now.cancel_ensure -= 1
            return "请再次发送指令以取消对局"
        if game_now.cancel_ensure == 0:                                                     # 二次确认取消正在进行的对局
            game_now.game_status = 4
            game_temp[game_now.game_id][1] = game_now
            game_now.save(False, True)
            playing_games.pop(gid)
            return f"对局%{game_now.game_id}取消成功，存档和记录已保存"

# 暂停对局 将状态储存至本地
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

# 加入群内对局
def join_game(gid:int, player_name:str):
    game_now = playing_games[gid]
    if not game_now:
        return "没有对局正在进行哦"
    if game_now.game_status == 1:
        return "对局已经开始了哦"
    return game_now.add_player(player_name)

# 开始游戏
def start_game(gid:int, player_name: str):
    game_now = playing_games[gid]
    if not game_now:
        return "没有对局正在进行哦"
    ret = ""
    game_now.deck = PROPCARD
    random.shuffle(game_now.deck)
    game_now.game_sequence = [i for i in range(1, game_now.player_count+1)]
    random.shuffle(game_now.game_sequence)
