![](media/cover.png)

# attrs-serde

A serialization addon for [attrs](https://attrs.org).


```py
person_dict = {"contact": {"personal": {"name": "John"}, "phone": "555-112233"}}

name_path = ["contact", "personal", "name"]
phone_path = ["contact", "phone"]

@serde
@attrs
class Person(object):
    name = attrib(metadata={"to": name_path, "from": name_path})
    phone = attrib(metadata={"to": phone_path, "from": phone_path})

>>> p = Person.from_dict(person_dict)
Person(name=John phone=555-112233)

>>> p.to_dict
{"contact": {"personal": {"name": "John"}, "phone": "555-112233"}}
```


## Quick Start

Install using pip/pipenv/etc. (we recommend [poetry](https://github.com/sdispater/poetry) for sane dependency management):

```
$ poetry add attrs-serde
```

Decorate with `serde` for automatic `to_dict` and `from_dict`. Provide paths in `metadata`:

1. `from` - path to fetch field value from
2. `to` - path to serialize value into (creates nested dictionaries as needed)

Example:

```py
from attrs_serde import serde
from attr import attrs, attrib
@serde
@attrs
class Person(object):
    name = attrib(metadata={"to": name_path, "from": name_path})
    phone = attrib(metadata={"to": phone_path, "from": phone_path})
```

Custom `from` and `to` keys (in case you or a different extension use those):

```py
from attrs_serde import serde
from attr import attrs, attrib
@serde(from_key="get", to_key="set")
@attrs
class Person(object):
    name = attrib(metadata={"get": name_path, "set": name_path})
    phone = attrib(metadata={"get": phone_path, "set": phone_path})
```

## Performance

`attrs-serde` works with `cytoolz` (mostly C implementation) and so presents very low overhead over what `attrs` already does.


Against manual object construction:

```
------------------------------------------------------------------------------------- benchmark 'deserialization': 2 tests ------------------------------------------------------------------------------------
Name (time in ns)              Min                    Max                  Mean                StdDev                Median                 IQR            Outliers  OPS (Kops/s)            Rounds  Iterations
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
test_deser_baseline       583.2500 (1.0)       5,037.3500 (1.0)        641.4743 (1.0)        161.4237 (1.0)        603.8500 (1.0)       33.7500 (1.0)     2315;3276    1,558.9089 (1.0)       77828          20
test_deser_serde        1,976.0000 (3.39)     88,504.0000 (17.57)    2,226.3774 (3.47)     1,195.7336 (7.41)     2,127.0000 (3.52)     110.0000 (3.26)     484;1576      449.1601 (0.29)      86806           1
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
```

Serialization against attr's `asdict`:

```
-------------------------------------------------------------------------- benchmark 'serialization': 2 tests --------------------------------------------------------------------------
Name (time in us)        Min                 Max              Mean            StdDev            Median               IQR            Outliers  OPS (Kops/s)            Rounds  Iterations
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
test_ser_baseline     2.6600 (1.0)      130.4550 (1.33)     2.9098 (1.0)      1.3230 (1.0)      2.7940 (1.0)      0.1320 (1.0)       302;882      343.6625 (1.0)       46642           1
test_ser_serde        5.0390 (1.89)      98.4540 (1.0)      5.6411 (1.94)     2.2398 (1.69)     5.4465 (1.95)     0.2890 (2.19)      491;912      177.2706 (0.52)      32936           1
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
```

### Thanks:

To all [Contributors](https://github.com/jondot/attrs-serde/graphs/contributors) - you make this happen, thanks!

# Copyright

Copyright (c) 2018 [@jondot](http://twitter.com/jondot). See [LICENSE](LICENSE.txt) for further details.