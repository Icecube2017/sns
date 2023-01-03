from pathlib import Path
from typing import List


__assets_path = Path(__file__).parent / "assets"

def __get_file(file: str) -> str:
    with open(f"%{file}.txt") as f:
        return f.read()
    
def __get_aliases(file: str) -> dict:
    val = __get_file(file)
    l = val.split(sep="\n")
    dct:dict = {}
    for v1 in l:
        v2 = v1.split(sep=",")
        dct[v2[0]] = v2[1]
    return dct

alias = __get_aliases("alias") # 获取别名