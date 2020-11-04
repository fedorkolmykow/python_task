def flatten_rec_lazy(d: dict, prefix: str = ""):
    for k, v in d.items():
        if isinstance(v, dict):
            prefix += str(k) + '.'
            yield from flatten_rec_lazy(v, prefix)
        else:
            yield prefix + str(k), v


def flatten(d: dict) -> dict:
    return dict(flatten_rec_lazy(d))


di = {
    "a": 5,
    "b": 6,
    "c": {
        "f": 9,
        "g": {
            "m": 17,
            "n": 3
        }
    }
}
print(flatten(di))
