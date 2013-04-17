#!/usr/bin/python

import sys

sys.path.append('../Model')

import node
import argparse
import pickle

_NODE_NAME_KEY = "name"
_NODE_DATE_KEY = "date"
_NODE_CLICKCOUNT_KEY = "click_count"
_NODE_TYPE_KEY = "type"
_NODE_TYPE_BOOKMARK = "bookmark"
_NODE_TYPE_FOLDER = "folder"
_NODE_URL_KEY = "url"
_NODE_CHILDREN_KEY = "children"
            
def serialize(root, filename):
    """Serializes a tree of bookmark objects to file

    Keyword Args:
    root -- root of bookmark object tree
    filename -- filename to write to
    """
    fp = open(filename, 'w')
    pickle.dump(root, fp)
    fp.close()
    
def deserialize(filename):
    """Deserializes the contents of a file into a bookmark object tree

    Keyword Args:
    filename -- name of file to deserialize

    Returns:
    Root of deserialized bookmark object tree
    """
    fp = open(filename, 'r')
    return pickle.load(fp)
    fp.close()


# Display scenario-creating CLI if user runs specifically this script
if __name__ == "__main__":
    root = node.Folder('root')
    current_node = root
    filename = None
    running = True
    unsaved_changes = False

    # REPL to navigate and build scenario
    while running:
        user_input = raw_input(">> ")
        input_words = user_input.split()
        len_input = len(input_words)

        if len_input <= 0:
            continue

        command = input_words[0].lower()
        # list this node, its parent, and its children
        if command == "ls":
            if current_node.parent is None:
                print("   NONE")
            else:
                print("  " + current_node.parent.name)
            print("  --> " + current_node.name)
            if isinstance(current_node, node.Folder):
                for child in current_node.children:
                    fold_str = "  "
                    if isinstance(child, node.Folder):
                        fold_str = "+ "
                    print("      " + fold_str + child.name)

        # Display detailed information about the node
        elif command == "info":
            if isinstance(current_node, node.Folder):
                print("  FOLDER '" + current_node.name + "'")
            elif isinstance(current_node, node.Bookmark):
                print("  BOOKMARK '" + current_node.name + "'")
                print("    Url:         " + current_node.url)
            print("    Depth:       " + str(current_node.depth))
            print("    Created:     " + str(current_node.date))
            print("    Click Count: " + str(current_node.clickCount))

        # Displays help info
        elif command == "help":
            if len_input == 1:
                print("  Commands:")
                print("    ls    : displays information about the surrounding nodes")
                print("    cd    : changes nodes")
                print("    info  : displays detailed info about the current node")
                print("    save  : saves the tree to file")
                print("    name  : displays the current tree filename being used")
                print("    bkmk  : adds a bookmark child to the current folder")
                print("    fold  : adds a folder child to the current folder")
                print("    del   : deletes the current directory and its children")
                print("    quit  : quit the scenario manager")
            elif len_input > 1:
                help_topic = input_words[1].lower()
                if help_topic == "ls":
                    print("  ls")
                    print("    The current node is designated by an arrow -->")
                    print("    Folder children are marked with a +")
                elif help_topic == "cd":
                    print("  cd ../<child name>") 
                    print("    Changes to the parent directory if .. is given")
                    print("    Changes to the named child directory otherwise")
                elif help_topic == "save":
                    print("  save [filename]")
                    print("    If no filename is given, uses the last-used filename (viewable with 'name' command)")
                    print("    Otherwise, write the existing scenario to file")
                elif help_topic == "load":
                    print("  load <filename>")
                    print("    Loads the given file into the workspace, overwriting the current workspace contents")
                else:
                    print("  No help available")


        # Displays the scenario's current filename
        elif command == "name":
            if filename is None:
                print("  No filename given yet")
            else:
                print("  " + filename)
        # if the user loaded the file, save it back there
        # if the user provides a filename, save it there
        elif command == "save":
            if len_input == 1:
                if filename is None:
                    print("  No working filename; please specify one")
                else:
                    try:
                        serialize(root, filename)
                    except IOError as e:
                        print("  Unable to write to file: " + str(e))
                        continue
                    print("  Saved '" + filename + "' successfully")
                    unsaved_changes = False
            else:
                desired_filename = input_words[1]
                try:
                    serialize(root, desired_filename)
                except IOError as e:
                    print("  Unable to write the given filename: " + str(e))
                    continue
                filename = desired_filename
                print("  Saved '" + desired_filename + "' successfully")
                unsaved_changes = False

        # Loads the given file
        elif command == "load":
            if len_input < 2:
                print("  Specify filename to load from")
                continue
            # Warn before squashing changes
            if unsaved_changes:
                decision = raw_input("  Overwrite unsaved changes? (Y/n): ")
                if decision.lower() != "y":
                    continue

            target_filename = input_words[1]
            try:
                new_root = deserialize(target_filename)
            except IOError as e:
                print("  Unable to load the file: " + str(e))
                continue
            root = new_root
            current_node = new_root
            filename = target_filename
            unsaved_changes = False
            print("  Loaded '" + target_filename + "' successfully")

        # move to the child with the specified name, or to the node's parent if it has one
        elif command == "cd":
            if len_input == 1:
                print("  Specify number of node to change to, or .. to go to parent")
                continue
            target_node_name = input_words[1]

            # Try to change to parent
            if target_node_name == "..":
                if current_node.parent is None:
                    print("  Current node has no parent")
                else:
                    current_node = current_node.parent
                continue

            # Try to change to children
            if not isinstance(current_node, node.Folder):
                print("  Current node is not a folder")
            else:
                target = None
                for child in current_node.children:
                    if target_node_name.lower() == child.name.lower():
                        target = child
                        break
                if target is None:
                    print("  No such child exists")
                else:
                    current_node = target

        # adds a bookmark child with the given information
        elif command == "bkmk":
            if not isinstance(current_node, node.Folder):
                print("  Current node is not a folder")
                continue

            if len_input < 3:
                print("  Specify name and URL of bookmark to add")
            name = input_words[1]
            url = input_words[2]
            bookmark = node.Bookmark(name, url)
            current_node.add_child(bookmark)
            unsaved_changes = True

        # adds an empty folder child with the given information
        elif command == "fold":
            if not isinstance(current_node, node.Folder):
                print("  Current node is not a folder")
                continue

            if len_input < 2:
                print("  Specify name of folder to add")
            name = input_words[1]
            folder = node.Folder(name)
            current_node.add_child(folder)
            unsaved_changes = True

        # if the node has a parent,
        # deletes the current node and all nodes under and changes to the parent
        elif command == "del":
            if current_node.parent is None:
                print("  Cannot delete root")
                continue
            decision = raw_input("  Really delete? (Y/n): ")
            if decision.lower() != "y":
                continue
            temp = current_node
            current_node = current_node.parent
            temp.parent = None
            current_node.children = [child for child in current_node.children if child != temp]
            unsaved_changes = True

        # quit the program
        elif command == "quit":
            running = False
        else:
            print("  Unrecognized command. Try 'help'")




    

