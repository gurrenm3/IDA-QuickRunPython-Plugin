import os
import idaapi
import traceback


def run_script_from_file():
    # Get the directory of the currently executing script
    current_script = __file__
    script_directory = os.path.dirname(current_script)

    # Create a file path for the script name file in the same directory
    script_name_file = os.path.join(script_directory, "quick_run_python_config.txt")

    # Check if the script name file exists; if not, create it
    if not os.path.exists(script_name_file):
        print("quick_run_python_config.txt doesn't exist, creating it now...")
        with open(script_name_file, "w") as f:
            f.write("")

    # Try to read the name of the script to run from the file
    try:
        with open(script_name_file, "r") as f:
            script_to_run = f.read().strip()
            if not script_to_run:
                print("quick_run_python_config.txt did not contain a valid path to a script to run.")
            else:
                script_to_run_path = os.path.join(script_directory, script_to_run)

                # Check if the script to run exists
                if os.path.isfile(script_to_run_path):
                    with open(script_to_run_path, "r") as script_file:
                        script_code = script_file.read()
                        if not script_code.strip():
                            print("The specified script file is empty.")
                        else:
                            exec(script_code)
                else:
                    print(f"Script '{script_to_run}' not found in the script directory.")
    except Exception as e:
        print(f"Error reading or executing the script")
        traceback.print_exc()



class MyPlugin(idaapi.plugin_t):
    flags = 0
    comment = "Quickly execute the python script located in the config file."
    help = "Plugin help text"
    wanted_name = "Quick Run Python"
    wanted_hotkey = "Alt-R"

    def init(self):
        # print("MyPlugin initialized")
        return idaapi.PLUGIN_OK

    def run(self, arg):
        run_script_from_file()

    def term(self):
        return

def PLUGIN_ENTRY():
    return MyPlugin()