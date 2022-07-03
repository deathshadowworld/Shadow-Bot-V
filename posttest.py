import psycopg2,os
'postgresql-encircled-78418'
def run():
    DATABASE_URL = os.environ.get('DATABASE_URL')
    data = []
    strurl = DATABASE_URL.replace('postgres://','')
    temp1 = strurl.split(':')
    data.append(temp1[0])
    temp2 = temp1[1].split("@")
    data.append(temp2[0])
    data.append(temp2[1])
    temp3 = temp1[2].split("/")
    data.append(temp3[0])
    data.append(temp3[1])

    con = psycopg2.connect(
        host=data[2],
        database=data[4],
        user=data[0],
        password=[1],
        port=data[3],
    )
    cur = con.cursor()


    cur.execute('CREATE DATABASE shadowVgame;')
    cur.execute('''CREATE TABLE PLAYER(
        ID          INT             NOT NULL,

    );
    ''')
    cur.execute('''CREATE TABLE CHARACTER(
        ID          INT             NOT NULL,
        NAME        CHAR(32)        NOT NULL,
        CLASS       CHAR(16)        NOT NULL,
        LEVEL       INT             NOT NULL,
        EXP         INT             NOT NULL,
        VITALITY    INT             NOT NULL,
        VIGOR       INT             NOT NULL,
        AGILITY     INT             NOT NULL,
        ERUDITION   INT             NOT NULL,
        JUDGMENT    INT             NOT NULL,
        CHARM       INT             NOT NULL,
        PLAYERID    INT             NOT NULL,
        IMAGE       TEXT,
        PRIMARY KEY (ID),
        FOREIGN KEY (PLAYERID) REFERENCES PLAYER(ID),
        );
    ''')
    cur.execute('''CREATE TABLE EQUIPPED(
        ITEM        INT             NOT NULL,
        CHARACTER   INT             NOT NULL,
        FOREIGN KEY (CHARACTER) REFERENCES CHARACTER(ID),
        FOREIGN KEY (ITEM) REFERENCES INVENTORY(ID),
    );
    ''')
    cur.execute('''CREATE TABLE INVENTORY(
        ID          INT             NOT NULL,
        NAME        CHAR(64)        NOT NULL,
        SLOT        CHAR(32)        NOT NULL,  
        EFFECT      CHAR(256)       NOT NULL,
        TEXT        CHAR(512)       NOT NULL,
        CHARACTER   INT             NOT NULL,
        PRIMARY KEY (ID),
        FOREIGN KEY (CHARACTER) REFERENCES CHARACTER(ID),
    );
    ''')




    cur.close()