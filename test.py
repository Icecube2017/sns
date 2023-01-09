from .game import *

class Log(object):
    def __init__(self, level: str) -> None:
        self.level = f"[{level.upper}]"

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            print(func(*args, **kwargs))
            return
        return wrapper