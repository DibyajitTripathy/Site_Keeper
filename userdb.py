import json
import getpass
import os
import sqlite3

def data_integrity():
    osuser = getpass.getuser()
    if os.name == 'nt':
        pat = os.path.join("C:", os.sep, "Users", osuser)
    elif sys.platform == 'darwin':
        pat = os.path.join("/","Users", osuser)
    else:
        pat = os.path.join("/", "home", osuser)
    sspath = os.path.join(pat,'ss.db')
    

    if not os.path.isfile(sspath):
        data=sqlite3.connect('ss.db')

data_integrity()
