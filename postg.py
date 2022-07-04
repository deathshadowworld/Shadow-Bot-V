import psycopg2,os
from dotenv import load_dotenv

def createConn():
    load_dotenv()
    DATABASE_URL = os.environ.get('DATABASE_URL')
    con = psycopg2.connect(DATABASE_URL)
    return con

# 1. Create connection
# 2. Create cursor
# 3. Try to execute normally 
# 4. Catch if cursor is already open
# 4a Commit
# 5. Close cursor
# 6. Close connection



#######           GET SECTION           #######


def viewUser(user):
    con = createConn()
    cur = con.cursor()
    try:
        cur.execute("SELECT NAME,ID,STATUS FROM PLAYER WHERE ID = "+str(user.id)+";")
        userInfo = cur.fetchone()
        userInfo = {
            'name':userInfo[0],
            'id':str(userInfo[1]),
            'status':userInfo[2],
        }
    except:
        pass
    cur.close()
    con.close()
    
    return userInfo

def viewUsers():
    con = createConn()
    cur = con.cursor()
    cur.execute("TABLE PLAYER")
    userInfo = cur.fetchall()
    usersInfo = []
    for x in userInfo:
        usersInfo.append(x)
    cur.close()
    return usersInfo



#######           SET SECTION           #######

def registerUser(user):
    con = createConn()
    cur = con.cursor()
    try:
        cur.execute("INSERT INTO PLAYER(ID,NAME,STATUS) VALUES ("+str(user.id)+",\'"+user.name+"\',\'"+user.status+"\');")    
        print("register success")
    except:
        cur.close()
        con.close()
        print("register failed success")
        return False
    con.commit()
    cur.close()
    con.close()
    return True

def resetAll():
    con = createConn()
    cur = con.cursor()
    cur.execute("DELETE FROM player;")
    cur.execute("DELETE FROM character;")
    cur.execute("DELETE FROM inventory;")
    cur.execute("DELETE FROM equipped;")
    con.commit()
    cur.close()
    con.close()
    return

def fix():
    con = createConn()
    cur = con.cursor()
    #cur.execute("ALTER TABLE PLAYER ALTER COLUMN ID TYPE BIGINT;")
    #cur.execute("ALTER TABLE player ADD COLUMN name VARCHAR, ADD COLUMN status VARCHAR;")
    con.commit()
    cur.close()
    con.close()
    return