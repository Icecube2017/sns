# -*- coding:utf-8 -*-

import json

from pathlib import Path
from typing import List, Dict


__ASSETS_PATH = Path(__file__).parent / "assets"


def __get_file(file: str, suffix: str = "") -> str:
    if suffix:
        with open(__ASSETS_PATH / f"{file}.{suffix}", encoding="utf-8") as f:
            return f.read()
    else:
        with open(__ASSETS_PATH / f"{file}", encoding="utf-8") as f:
            return f.read()


# 以字典形式获取别名
def __get_aliases() -> dict:
    _val = __get_file("alias", "txt").split(sep="\n")
    _dct: dict = {}
    for v1 in _val:
        v2 = v1.split(sep=",")
        _dct[v2[0]] = v2[1]
    return _dct


ALIAS = __get_aliases()


# 以字典形式加载可用角色列表
def __get_character_list() -> dict:
    _characters: Dict[str, list] = {}

    _types: Dict[str, List[int]] = json.loads(
        __get_file("character_type", "json"))
    _regenerate_types: Dict[str, List[int]] = json.loads(
        __get_file("regenerate_type", "json"))
    _chs: Dict[str, List[str]] = json.loads(__get_file("character", "json"))
    for ch_id, chv in _chs.items():
        if ch_id != "角色": 
            _c_temp = _types[chv[0]]
            _c_temp.extend(_regenerate_types[chv[1]])
            _c_temp2 = [ch_id]
            _c_temp2.extend(_c_temp)
            _characters[ch_id] = _c_temp2
    return _characters


CHARACTER = __get_character_list()


# 加载牌堆
def get_propcard_list(deckname: str) -> list:
    _prop: List[str] = []
    _f = __get_file("propcard", "txt").split("\n")
    for _ in _f:
        _p = _.split(",")
        _prop.extend([_p[0]]*int(_p[1]))
    return _prop


# PROPCARD = __get_propcard_list()


# 加载技能卡堆
def __get_skill_list() -> Dict[str, int]:
    _val = __get_file("skill", "txt").split(sep="\n")
    _dct: dict = {}
    for v in _val:
        v2 = v.split(sep=",")
        _dct[v2[0]] = int(v2[1])
    return _dct


SKILL = __get_skill_list()


def __get_private_skill_list() -> Dict[str, int]:
    _val = __get_file("private_skill", "txt").split(sep="\n")
    _dct: dict = {}
    for v in _val:
        v2 = v.split(sep=",")
        _dct[v2[0]] = int(v2[1])
    return _dct


PRIVATE_SKILL = __get_private_skill_list()
