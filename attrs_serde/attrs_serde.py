from cytoolz.curried import get_in, merge, update_in, reduce, pipe, map, filter
from attr import attrib, attrs, fields, asdict


def serde(cls):
    from_fields = list(
        map(lambda a: (a, get_in(["from"], a.metadata, [a.name])), fields(cls))
    )

    to_fields = pipe(
        fields(cls),
        map(lambda a: (a, get_in(["to"], a.metadata))),
        filter(lambda f: f[1]),
        list,
    )

    def from_dict(d):
        return cls(
            **dict(
                map(lambda f: (f[0].name, get_in(f[1], d, f[0].default)), from_fields)
            )
        )

    def to_dict(self):
        d = asdict(self)
        return reduce(
            lambda acc, f: update_in(acc, f[1], lambda _: d[f[0].name]), to_fields, {}
        )

    cls.from_dict = staticmethod(from_dict)
    cls.to_dict = to_dict
    return cls
