#!/usr/bin/python3
# Grab data from the Riff.CC Curator database and look for patterns

# Import needed modules
from __future__ import with_statement
import os, sys, yaml
import psycopg2
from pynput import keyboard

def on_press(key):
    try:
        print('alphanumeric key {0} pressed'.format(
            key.char))
    except AttributeError:
        print('special key {0} pressed'.format(
            key))

def on_release(key):
    print('{0} released'.format(
        key))
    if key == keyboard.Key.esc:
        # Stop listener
        return False

# Dynamically load in our magic config files
configname = os.path.expanduser('~/.rcc-tools.yml')
config = yaml.safe_load(open(configname))

# Check if the config is empty
if config is None:
    print("Failed to load configuration.")
    sys.exit(1338)

# Get our Riff.CC credentials and load them in
curator_user = config["curator_user"]
curator_pass = config["curator_pass"]
curator_host = config["curator_host"]

# Connect to the Curator database
connpg = psycopg2.connect(host=curator_host,
                          database="collection",
                          user=curator_user,
                          password=curator_pass)

# create a cursor
cursorpg = connpg.cursor()

with connpg.cursor() as cursor:
    # Read everything from Unit3D (traditional site)
    sql = "SELECT id, name, description FROM releases"
    cursorpg.execute(sql)
    result_set = cursorpg.fetchall()
    for row in result_set:
        release_id = row[0]
        name = row[1]
        # print("Release ID: " + str(release_id) + " (Name: " + name + ")")
        if " " not in name:
            print("Found issue - " + str(release_id) + " may have an invalid name")
            # Collect events until released
            with keyboard.Listener(
                    on_press=on_press,
                    on_release=on_release) as listener:
                        print("how do I do stuff here? :)")
                listener.join()
