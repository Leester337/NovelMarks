import sys
import os.path
import manager
import json

# argument sanity check
if len(sys.argv) != 2:
    print("usage: ", argv[0], " <path to scenario file>")
    sys.exit(1)
scenario_filepath = argv[1]

# open file and load into an object
if not os.path.exists(scenario_filepath):
    print("Invalid scenario file")
    sys.exit(1)
try:
    scenario = json.load(open(scenario_filepath))
except Exception as e:
    print("Error when opening scenario JSON: ", str(e))
    sys.exit(1)

manager = Manager(scenario, "scenario_chkpnt.json")

# 
