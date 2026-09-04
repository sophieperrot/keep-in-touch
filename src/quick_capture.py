#!/usr/bin/env python3

import os
from datetime import datetime

import kit_cli
import utils


def quick_capture_cli():
    print("\n===== quick capture =====")
    print(" (1) scribble\n (2) ramble\n (d) dashboard\n (q) quit")
    select = input("select an option: ")
    while True:
        match select:
            case '1':
                scribble_cli()
            case '2':
                ramble_cli()
            case 'd':
                kit_cli.dashboard_cli()
            case 'q':
                kit_cli.quit_cli()
            case _:
                select = input("not a valid option, try again: ")


def ramble_cli():
    print("\n===== ramble =====")
    print(" - this is where you would be able record a voice note, saved locally")
    utils.not_implementable_cli()


SCRIBBLES_DIR = os.path.join(os.getcwd(), "scribbles/")

def scribble_cli():
    print("\n===== scribble =====")
    print(" (1) new scribble\n (2) view scribbles\n (r) return \n (d) dashboard\n (q) quit")
    select = input("select an option: ")
    while True:
        match select:
            case '1':
                new_scribble()
            case '2':
                view_scribbles()
            case 'r':
                quick_capture_cli()
            case 'd':
                kit_cli.dashboard_cli()
            case 'q':
                kit_cli.quit_cli()
            case _:
                select = input("not a valid option, try again: ")


def new_scribble():
    scribble_id = datetime.strftime(datetime.now(), "%Y-%m-%d-%H-%M")
    scribble_filepath = os.path.join(SCRIBBLES_DIR, scribble_id)
    scribble_contents = []

    print("\n===== new scribble =====")
    print("scribble away! (enter twice to save) \n")
    while True:
        try:
            line = input()
            scribble_contents.append(line)
            if line == "" and scribble_contents[-1] == "":
                scribble_contents[-1] == "_EOF"
                break
        except KeyboardInterrupt:
            break

    try:
        with open(scribble_filepath, 'w') as scribble_file:
            for line in scribble_contents:
                scribble_file.write(line) if line != "_EOF" else print("(scribble saved)")
        print("(scribble saved)")
    except Exception as e:
        print(f"exception ocurred ({e})")

    scribble_cli()


def view_scribbles():
    scribbles = os.listdir(SCRIBBLES_DIR)

    print("\n===== view scribble =====")
    for idx, scribble in enumerate(scribbles):
        print(f" {idx}. {scribble}")

    select = input("select a scribble to view (r to return): ")
    while True:
        if select == 'r':
            scribble_cli()
        elif select.isnumeric() and int(select) < len(scribbles):
            print(os.path.join(SCRIBBLES_DIR, scribbles[int(select)]))
            break
        else:
            select = input("input not valid, try again: ")

    view_scribbles()