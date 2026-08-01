import os
import subprocess
from tkinter import *
from tkinter import ttk

root = Tk()
statusc = "disconnected"
status = ttk.Label(root, text=f"Status: {statusc}", style="CustoM.TLabel", font=(None, 12))
def updstat(stat):
    global statusc

    statusc = stat
    status.configure(text=f"Status: {stat}")

def check_stat():
    global statusc
    print("Checking connection status...")
    result = subprocess.run(["adguardvpn-cli", "status"], capture_output=True, text=True)
    if "VPN is disconnected" in result.stdout:
        statusc = "disconnected"
        status.configure(text=f"Status: {statusc}")
    else:
        statusc = "connected"
        status.configure(text=f"Status: {statusc}")


# Utilities

check_stat()

# Connect function
def connect(server):

    my_env = os.environ.copy()

    try:
        result = subprocess.run(
                ["adguardvpn-cli", "connect", "-l", f"{server}"],
                env=my_env
        )
        print("Connection successful!")
        print(result.stdout)
        updstat("connected")
    except subprocess.CalledProcessError as e:
        print("ERROR!")
        print("STDOUT: ", result.stdout)
        print("STDERR: ", result.stderr)
        updstat("error")

# Disconnect function
def disconnect():

    my_env = os.environ.copy()

    try:
        result = subprocess.run(
                ["adguardvpn-cli", "disconnect"],
                env=my_env,
                capture_output=True,
                text=True,
                check=True
        )
        print("Disconnection successful!")
        print(result.stdout)
        updstat("disconnected")
    except subprocess.CalledProcessError as e:
        print("ERROR!")
        print("STDOUT: ", result.stdout)
        print("STDERR: ", result.stderr)
        updstat("error")

def get_best() -> tuple:
    serv1_index = 1
    serv2_index = 2
    serv3_index = 3
    current_index = 0
    final_output = ["1", "2", "3"]
    my_env = os.environ.copy()

    print("Getting best servers...")

    process = subprocess.Popen(["adguardvpn-cli", "list-locations"], stdout=subprocess.PIPE, text=True, env=my_env)

    for line in process.stdout:
        if current_index == serv1_index:
            target1_line = line.strip()
            final_output[0] = target1_line
        if current_index == serv2_index:
            target2_line = line.strip()
            final_output[1] = target2_line
        if current_index == serv3_index:
            target3_line = line.strip()
            final_output[2] = target3_line
            process.terminate()
            break
        current_index += 1
    process.wait()
    # print(target1_line + target2_line + target3_line)
    return final_output
