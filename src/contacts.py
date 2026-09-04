#!/usr/bin/env python3

from tinydb import TinyDB, Query
import os

import utils
import kit_cli


CONTACTS_DB_PATH = os.path.join(os.getcwd(), "network.json")
contacts_db = TinyDB(CONTACTS_DB_PATH)


def contacts_cli():
    print("\n===== contacts =====")
    print(" (1) add contacts\n (2) view contacts\n (3) edit contacts\n (d) dashboard\n (q) quit")
    select = input("select an option: ")
    while True:
        match select:
            case '1':
                add_contacts_cli()
            case '2':
                view_contacts_cli()
            case '3':
                edit_contacts_cli()
            case 'd':
                kit_cli.dashboard_cli()
            case 'q':
                utils.quit_cli()
            case _:
                select = input("not a valid option, try again: ")


def add_contacts_cli():
    utils.coming_soon_cli()


def add_contact(contact_info):
    # TODO: implement some try/except and other validation stuff
    contacts_db.insert(contact_info)

add_contact({"personal-info": {"name": "Jane Doe", "alias": "Jane", "age-category": "18-22"}, 
             "affiliations": {
                "education": ["spgs", "Cambs"],
                "interests": ["EEE", "quidditch"],
                "organisations": ["MM", "DA"],
                "locations": {
                    "bases": ["hogwarts"], 
                    "frequent-locations": ["London", "Scotland"],
                    "last-location": {"location": "beaubatons", "last-confirmed": "2026-9-4"}}}
             })

def view_contacts_cli():
    utils.coming_soon_cli()
    entries = get_contacts()
    contacts_list_view(entries)


def edit_contacts_cli():
    utils.coming_soon_cli()
    entries = get_contacts()
    contacts_list_view(entries)


def contacts_list_view(entries):
    utils.coming_soon_cli()


def get_contacts(filters: dict = None, sort=None):
    Person = Query()
    if filters is not None:    
        entries = contacts_db.search(Person.fragment(filters))
    else:
        entries = contacts_db.all()
    if sort is not None:
        pass
    else:
        return entries


def contacts_graph_view():
    print("\n===== contacts graph view =====")
    print(" - as the name suggests, similar to Obsidian's graph view")
    utils.not_implementable_cli()


def contacts_map_view():
    print("\n===== contacts map view =====")
    print(" - as the name suggests, visually view where contacts are based or travelling (configured, not real-time)")
    utils.not_implementable_cli()