#!/usr/bin/env python3
"""Entry point for the crafting automater"""
import sys
from json_editor import json_reader
from process import Process
from time import sleep

def args_checker():
    accepted_args = ["foodbuff", "potbuff"]
    args = sys.argv[1:]
    all_ok = 0
    for arg in args:
        if arg in accepted_args:
            all_ok += 1
    if all_ok != len(args):
        print("Incorrect argument(s). Choose from this list:\n{}\n".format(accepted_args))
        quit()
    return args

if __name__ == "__main__":
    json_data = json_reader()
    ffxiv = Process(json_data["process_name"])

    args = args_checker()

    foodbuff = 0
    food_time = None
    food_limiter = 0

    potbuff = 0
    pot_time = None
    pot_limiter = 0

    if "foodbuff" in args:
        print("Adding foodbuffer to crafting automation...")
        food_time = input("What is your current food buff time?\n")
        foodbuff = 1
    if "potbuff" in args:
        print("Adding potbuffer to crafting automation...")
        pot_time = input("What is your current pot buff time?\n")
        potbuff = 1

    # Regular auto-craft
    print("Starting crafting automation...")
    print("TO QUIT: PRESS CTRL+C\n")
    while True:
        if foodbuff == 1:
            if food_limiter >= food_time:
                food_limiter = 0
                food_time = 1770 # Default 30 min pot buff minus 30 seconds
        if potbuff == 1:
            if pot_limiter >= pot_time:
                pot_limiter = 0
                pot_time = 870 # Default 15 min pot buff minus 30 seconds

        print("  -> Pressing + Selecting 'Synthesis'")
        for zero_counter in range(25):
            ffxiv.press_key("{VK_NUMPAD0}")
        sleep(5)
        food_limiter += 7
        pot_limiter += 7

        ffxiv.press_key(json_data["k1"])
        print("  -> Pressing Macro 1")
        print("    -> Waiting {} seconds.".format(json_data["m1"]))
        sleep(json_data["m1"])
        food_limiter += json_data["m1"]
        pot_limiter += json_data["m1"]

        ffxiv.press_key(json_data["k2"])
        print("  -> Pressing Macro 2")
        print("    -> Waiting {} seconds.".format(json_data["m2"]))
        sleep(json_data["m2"])
        food_limiter += json_data["m2"]
        pot_limiter += json_data["m2"]

        sleep(3)
        food_limiter += 3
        pot_limiter += 3