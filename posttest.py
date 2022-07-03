import psycopg2,os

def run():
    DATABASE_URL = os.environ.get('postgresql-encircled-78418')

    con = psycopg2.connect(
    host=DATABASE_URL,
    user="postgres",
    password="postgres")

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