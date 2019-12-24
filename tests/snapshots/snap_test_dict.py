# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['test_deser 1'] = {
    'name': 'John',
    'phone': '555-112233'
}

snapshots['test_ser 1'] = {
    'contact': {
        'personal': {
            'name': 'Slash'
        },
        'phone': '555-334455'
    }
}

snapshots['test_quirky_object 1'] = {
    'name': 'John',
    'phone': '555-112233',
    'zip': 56000
}

snapshots['test_from_to_keys 1'] = {
    'name': 'John',
    'phone': '555-1111'
}

snapshots['test_from_to_keys 2'] = {
    'nameeee': 'John',
    'phoneeee': '555-1111'
}

snapshots['test_ser_with_default_values 1'] = {
    'name': 'Tel-Aviv',
    'zipcode': '6100000'
}

snapshots['test_deser_with_default_values 1'] = {
    'name': 'Tel-Aviv',
    'zipcode': '6100000'
}
