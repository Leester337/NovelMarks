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
    scenario_fp = open(scenario_filepath)
    scenario = json.load()
    scenario_fp.close()
except Exception as e:
    print("Error when loading scenario JSON: ", str(e))
    sys.exit(1)

prog_manager = Manager(scenario, "scenario_chkpnt.json")


# While manager keeps returning success actions, keep going
manager_state = prog_manager.state
while manager_state == manager.ManagerState.RUNNING:
    manager_state = prog_manager.process_user_action()

print("Bye!")

