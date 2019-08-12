import os
import getpass
import sqlite3
import time

# this function writes data to the db
def write(user,masterkey,site,username,password):
	c.execute("INSERT INTO data VALUES(?,?,?,?,?)", (user,masterkey,site,username,password))
	conn.commit()
def read(user,masterkey,site):
	# ans = c.execute('SELECT * FROM data where user = ? AND masterkey = ? AND site = ?', (user,masterkey,site))
	for row in c.execute('SELECT * FROM data'):
		print(row)

def delete(user,masterkey,site):
	c.execute('DELETE FROM data WHERE user = ? AND masterkey = ? AND site = ?', (user,masterkey,site))
	conn.commit()
def update(user,masterkey,site,username,password):
	c.execute('DELETE FROM data WHERE user = ? AND masterkey = ? AND site = ?', (user,masterkey,site))
	c.execute("INSERT INTO data VALUES(?,?,?,?)", (user,masterkey,site,username,password))	
	conn.commit()


if __name__ == '__main__':

	osuser = getpass.getuser()
	if os.name == 'nt':
		pat = os.path.join("C:", os.sep, "Users", osuser)
	elif sys.platform == 'darwin':
		pat = os.path.join("/","Users", osuser)
	else:
		pat = os.path.join("/", "home", osuser)
	sspath = os.path.join(pat,'dj.db')
	

	if os.path.isfile(sspath):
		conn = sqlite3.connect(sspath)
		c=conn.cursor()
 
	else:
		conn = sqlite3.connect(sspath)
		c=conn.cursor() 		
		c.execute('''CREATE TABLE data(user text,masterkey text,site text,username text,password text)''')

	write('dibyajit','qwerty','www.facebook.com','dj','gdjh')
	write('dibyajit','qwerty','www.google.com','akjshd','asjhgasjh')
	read('dibyajit','qwerty','www.google.com')
	