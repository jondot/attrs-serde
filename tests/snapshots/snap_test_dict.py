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
