#!/usr/bin/env python3

import os
from tinydb import TinyDB

GROUPS_DB_PATH = os.path.join(os.getcwd(), "groups.json")
groups_db = TinyDB(GROUPS_DB_PATH)

def list_groups():
    pass