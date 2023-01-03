from pathlib import Path
from typing import List


__assets_path = Path(__file__).parent / "assets"

def __get_file(file: str) -> str:
    with open("%{0}.txt".format(file)) as f:
        return f.read()
    
def __get_aliases(file: str) -> dict:
    val = __get_file(file)
    l = val.split(sep="\n")
    dct:dict = {}
    for v in l:
        dct[v[0]] = v[1]
    return dct

alias = __get_aliases("alias") # 获取别名