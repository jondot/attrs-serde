from toolz import pipe
from attrs_serde import serde
from attr import attrs, attrib

person_dict = {"contact": {"personal": {"name": "John"}, "phone": "555-112233"}}

name_path = ["contact", "personal", "name"]
phone_path = ["contact", "phone"]


@serde
@attrs
class Person(object):
    name = attrib(metadata={"to": name_path, "from": name_path})
    phone = attrib(metadata={"to": phone_path, "from": phone_path})


@serde
@attrs
class Contact(object):
    name = attrib(metadata={"to": name_path, "from": name_path})
    phone = attrib(metadata={"to": phone_path, "from": phone_path})
    zip_code = attrib(default=56000, metadata={"to": phone_path})
    address = attrib()


def test_deser(snapshot):
    p = Person.from_dict(person_dict)
    snapshot.assert_match({"name": p.name, "phone": p.phone})


def test_ser(snapshot):
    snapshot.assert_match(Person(name="Slash", phone="555-334455").to_dict())


def test_quirky_object(snapshot):
    c = Contact.from_dict(person_dict)
    snapshot.assert_match({"name": c.name, "phone": c.phone, "zip": c.zip_code})


def test_irrelevant_object(snapshot):
    c = Contact.from_dict({"irrelevant": True})
