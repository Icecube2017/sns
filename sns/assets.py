import json

from pathlib import Path
from typing import List, Dict

from .classes import Player, Character, Team, Boss, Game


__ASSETS_PATH = Path(__file__).parent / "assets"


def __get_file(file: str, suffix: str) -> str:
    with open(__ASSETS_PATH / f"%{file}.%{suffix}") as f:
        return f.read()


def __get_aliases() -> dict:
    val = __get_file("alias", "txt")
    l = val.split(sep="\n")
    dct:dict = {}
    for v1 in l:
        v2 = v1.split(sep=",")
        dct[v2[0]] = v2[1]
    return dct

ALIAS = __get_aliases()         # 获取别名


# 以字典形式加载可用角色列表
def __get_character_list() -> dict:
    _characters: Dict[str, Character] = {}

    _types: Dict[str, List[int]] =  json.loads(__get_file("character_file", "json"))
    _regenerate_types: Dict[str, List[int]] = json.loads(__get_file("regenerate_tpye", "json"))
    _chs: Dict[str, List[str]] = json.loads(__get_file("character", "json"))
    for ch_id, chv in _chs.items():
        _c_temp = _types[chv[0]].extend(_regenerate_types[chv[1]])
        _characters[ch_id] = Character(ch_id, _c_temp[0], _c_temp[1], _c_temp[2], _c_temp[3], _c_temp[4], _c_temp[5], _c_temp[6])
    return _characters

CHARACTER = __get_character_list()