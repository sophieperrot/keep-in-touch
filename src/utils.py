#!/usr/bin/env python3

import sys
import kit_cli


def quit_cli():
    print("\nthank you for using kit, your updates have been saved locally\n")
    sys.exit()


def coming_soon_cli():
    print("\n * coming soon... (redirecting you to dashboard)")
    kit_cli.dashboard_cli()


def not_implementable_cli():
    select = input(" * not implementable in this demo, d to return to dash or q to quit: ")
    while True:
        match select:
            case 'd':
                kit_cli.dashboard_cli()
            case 'q':
                quit_cli()
            case _:
                select = input("not a valid option, try again: ")