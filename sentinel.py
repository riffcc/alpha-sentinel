#!/usr/bin/python3
# Grab data from the Riff.CC Curator database and look for patterns

# Import needed modules
from __future__ import with_statement
import os, sys, yaml
import pymysql.cursors
import psycopg2

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

with connpg:
    with cursorpg.cursor() as cursor:
        # Read everything from Unit3D (traditional site)
        sql = "SELECT * FROM `releases`"
        cursorpg.execute(sql)
        result_set = cursorpg.fetchall()
        for row in result_set:
            print("TEST id "+ str(id))
