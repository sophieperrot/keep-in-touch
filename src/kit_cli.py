#!/usr/bin/env python3

import utils
import quick_capture
import contacts


def dashboard_cli():
    print("\n===== dashboard =====")
    print("----- quick actions -----")
    print(" (1) quick capture\n (2) add contact\n (3) add action item\n (4) add reminder\n (q) quit")
    print("----- dash widgets -----")
    print(" (u) upcoming\n (s) suggestions\n (t) summary stats")
    print("----- tabs -----")
    print(" (C) contacts\n (M) map\n (T) all stats")

    select = input("\nselect an option: ")
    while True:
        match select:
            case '1': 
                quick_capture.quick_capture_cli()
            case '2':
                contacts.add_contacts_cli()
            case '3':
                utils.coming_soon_cli()
            case '4':
                utils.coming_soon_cli()
            case 'q':
                utils.quit_cli()
            case 'u':
                utils.coming_soon_cli()
            case 's':
                utils.coming_soon_cli()
            case 't':
                utils.coming_soon_cli()
            case 'C':
                utils.coming_soon_cli()
            case 'M':
                utils.coming_soon_cli()
            case 'T':
                utils.coming_soon_cli()
            case _:
                select = input("not a valid option, try again: ")


if __name__ == "__main__":
    print("\nwelcome to the kit cli!")
    dashboard_cli()
