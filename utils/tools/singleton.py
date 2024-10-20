import functools


def singleton(cls):
    instance = None

    @functools.wraps(cls)
    def inner(*args):
        nonlocal instance
        if instance is None:
            instance = cls(*args)
        return instance
    return inner
