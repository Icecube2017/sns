def get_func(func: str, *args) -> function:
    def wood_sword():
        pass

    funcs = {"木剑": wood_sword}
    return funcs[func]