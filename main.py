from utils import *
from utils import root
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import subprocess
# Interface for adguardvpn-cli.

# Selected server
servers = get_best()
server1 = servers[0][4:6]
server2 = servers[1][0:2]
server3 = servers[2][0:2]
server = server1

def conn():
    connect(server)
def dconn():
    if statusc == "connected":
        disconnect()
    else:
        print("VPN Is disconnected")
# Window settings
root.configure(bg="grey")
root.geometry("800x600")
root.title("AdGuard VPN")
root.resizable(False, False)

# TTK Style settings

style = ttk.Style()
style.theme_use("clam")
style.configure('CustoM.TButton', background='green', foreground='white')
style.configure('CustOM.TButton', backhround='grey', foreground="black")
style.map('CustoM.TButton', background=[('active', 'darkgreen')])
style.map('CustOM.TButton', backgorund=[('active', 'black')])
style.configure('CustoM.TLabel', background='grey', foreground='white')


# Elements
maintitle = ttk.Label(root, text="AdGuard VPN Cli GUI", font=(None, 30), style="CustoM.TLabel")
connectbutton = ttk.Button(root, text="Connect", width=15, command=conn, style="CustoM.TButton")
disconnectbutton = ttk.Button(root, text="Disconnect", width=15, command=dconn, style="CustOM.TButton")
selserv = ttk.Label(root, text=f"Selected server: {server}", style="CustoM.TLabel", font=(None, 15))

def selserv1():
    global server
    server = server1
    serv1.configure(style="CustoM.TButton")
    serv2.configure(style="CustOM.TButton")
    serv3.configure(style="CustOM.TButton")
    selserv.configure(text=f"Selected server: {server}")
    dconn()
    conn()

def selserv2():
    global server
    server = server2
    serv1.configure(style="CustOM.TButton")
    serv2.configure(style="CustoM.TButton")
    serv3.configure(style="CustOM.TButton")
    selserv.configure(text=f"Selected server: {server}")
    dconn()
    conn()

def selserv3():
    global server
    server = server3
    serv1.configure(style="CustOM.TButton")
    serv2.configure(style="CustOM.TButton")
    serv3.configure(style="CustoM.TButton")
    selserv.configure(text=f"Selected server: {server}")
    dconn()
    conn()

beserv = ttk.Label(root, text="Fastest servers:", style="CustoM.TLabel", font=(None, 20))
serv1 = ttk.Button(root, text=server1, width=15, style="CustoM.TButton", command=selserv1)
serv2 = ttk.Button(root, text=server2, width=15, style="CustOM.TButton", command=selserv2)
serv3 = ttk.Button(root, text=server3, width=15, style="CustOM.TButton", command=selserv3)

def showabout():
    messagebox.showinfo("About AdGuard VPN Cli GUI", "AdGuard VPN Cli GUI by pablo-chitaksa\nAdGuard VPN Cli GUI is NOT associated with AdGuard.\n\nv0.1")

aboutbtn = ttk.Button(root, text="About", style="CustOM.TButton", command=showabout)

# Packing elements
maintitle.pack(anchor="n")
connectbutton.pack(anchor="nw")
selserv.pack(anchor="nw")
disconnectbutton.pack(anchor="nw")
status.pack(anchor="nw")

beserv.pack(anchor="n")
serv1.pack(anchor="n")
serv2.pack(anchor="n")
serv3.pack(anchor="n")


aboutbtn.pack(side=RIGHT, anchor=SE, padx=10, pady=10)

# Main loop
root.mainloop()