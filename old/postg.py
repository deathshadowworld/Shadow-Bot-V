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


def findUser(user):
    con = createConn()
    cur = con.cursor()
    try:
        cur.execute("SELECT name,id,status FROM player WHERE id = "+str(user.id)+";")
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

def findChar(user):
    con = createConn()
    cur = con.cursor()
    try:
        cur.execute("SELECT * FROM character WHERE playerid = "+str(user.id)+";")
        charInfo = cur.fetchone()
        charInfo = {
            'name':charInfo[1],
            'class':str(charInfo[2]),
            'level':charInfo[3],
            'exp':charInfo[4],
            'image':charInfo[12],
        }
    except:
        pass
    cur.close()
    con.close()
    return charInfo

def viewPlayerTable():
    con = createConn()
    cur = con.cursor()
    cur.execute("TABLE player")
    queried = cur.fetchall()
    players = []
    for x in queried:
        players.append(x)
    cur.close()
    return players

def viewCharTable():
    con = createConn()
    cur = con.cursor()
    cur.execute("TABLE character")
    queried = cur.fetchall()
    characters = []
    for x in queried:
        characters.append(x)
    cur.close()
    return characters

def viewInvTable():
    con = createConn()
    cur = con.cursor()
    cur.execute("TABLE character")
    queried = cur.fetchall()
    inventory = []
    for x in queried:
        inventory.append(x)
    cur.close()
    return inventory

def viewEquippedTable():
    con = createConn()
    cur = con.cursor()
    cur.execute("SELECT id,name,class,level,playerid FROM character;")
    queried = cur.fetchall()
    equipped = []
    for x in queried:
        equipped.append(x)
    cur.close()
    return equipped







#######           SET SECTION           #######

def registerUser(user):
    con = createConn()
    cur = con.cursor()
    try:
        cur.execute("INSERT INTO player(id,name,status) VALUES ("+str(user.id)+",\'"+user.name+"\','0');")    
    except:
        cur.close()
        con.close()
        return False
    con.commit()
    cur.close()
    con.close()
    return True

def registerChar(obj):
    name = obj.name
    option = obj.chosen
    uid = obj.uid
    con = createConn()
    cur = con.cursor()
    num = viewCharTable()
    x = findStats(option)
    
    if num == None:
        num = 0
    else:  
        for i in num:
            if i[11] ==  uid:
                return None
        num = len(num)
      
    try:
        #print(num,name,option,x[0],x[1],x[2],x[3],x[4],x[5],uid)
        cur.execute('''INSERT INTO character(
            id,name,class,level,exp,vitality,strength,dexterity,intellect,wisdom,charm,playerid,coins) 
        VALUES ({0},'{1}','{2}',0,0,{3},{4},{5},{6},{7},{8},{9},0);'''.format(num,name,option,x[0],x[1],x[2],x[3],x[4],x[5],uid))

    except:
        cur.close()
        con.close()
        return False
    
    con.commit()
    cur.close()
    con.close()
    return True
    
def updateImg(url,user):
    chars = viewCharTable()
    if chars == None:
        return None
    else:  
        for i in chars:
            if i[11] ==  user.id:
                con = createConn()
                cur = con.cursor()
                try:
                    cur.execute("UPDATE character SET image='"+url+"' WHERE playerid="+str(user.id)+";")
                except:
                    con.commit()
                    cur.close()
                    con.close()
                    return False

                con.commit()
                cur.close()
                con.close()
                return True

def deleteChar(user):
    con = createConn()
    cur = con.cursor()
    try:
        cur.execute("DELETE FROM character WHERE playerid="+str(user.id)+";")
    except:
        con.commit()
        cur.close()
        con.close()
        return False

    con.commit()
    cur.close()
    con.close()
    return True

















def resetAll():
    con = createConn()
    cur = con.cursor()
    cur.execute("DELETE FROM equipped;")
    cur.execute("DELETE FROM inventory;")
    cur.execute("DELETE FROM character;")
    cur.execute("DELETE FROM player;")
    con.commit()
    cur.close()
    con.close()
    return

def fix():
    con = createConn()
    cur = con.cursor()
    #cur.execute("ALTER TABLE PLAYER ALTER COLUMN ID TYPE BIGINT;")
    #cur.execute("ALTER TABLE player ADD COLUMN name VARCHAR, ADD COLUMN status VARCHAR;")
    cur.execute("ALTER TABLE character ALTER COLUMN name TYPE VARCHAR;")
    cur.execute("ALTER TABLE character ALTER COLUMN class TYPE VARCHAR;")
    #cur.execute('ALTER TABLE character RENAME COLUMN vigor TO strength;')

    con.commit()
    cur.close()
    con.close()
    return

def findStats(query):
    if query == 'Healer':
        return [1,0,0,1,3,1]
    if query == 'Archer':
        return [0,1,3,0,1,1]
    if query == 'Warrior':
        return [2,4,0,0,0,0]
    if query == 'Caster':
        return [0,0,0,4,2,0]