def merge_dicts(*args):
    res = {}
    for d in args:
        res.update(d)
    return res
