import psycopg2,os
'postgresql-encircled-78418'
def run():
    DATABASE_URL = os.environ.get('DATABASE_URL')


    con = psycopg2.connect(DATABASE_URL)
    cur = con.cursor()

    cur.execute('''CREATE TABLE PLAYER(
        ID          INT             NOT NULL,
        NAME        VARCHAR,
        STATUS      VARCHAR,
        PRIMARY KEY (ID)
    );
    ''')
    cur.execute('''CREATE TABLE CHARACTER(
    0   ID          INT             NOT NULL,
    1   NAME        VARCAR          NOT NULL,
    2   CLASS       VARCHAR         NOT NULL,
    3   LEVEL       INT             NOT NULL,
    4   EXP         INT             NOT NULL,
    5   VITALITY    INT             NOT NULL,
    6   STRENGTH    INT             NOT NULL,
    7   AGILITY     INT             NOT NULL,
    8   INTELLECT   INT             NOT NULL,
    9   WISDOM      INT             NOT NULL,
    10  CHARM       INT             NOT NULL,
    11  PLAYERID    INT             NOT NULL,
    12  IMAGE       TEXT,
    13  COINS       INT,
    14  BACKSTORY   VARCHAR,
        PRIMARY KEY (ID),
        FOREIGN KEY (PLAYERID) REFERENCES PLAYER(ID)
        );
    ''')

    '''
    vit cross in heart red
    vig bicep orange
    agi run green
    eru book blue
    jud mind awareness yellow
    cha mini hearts purple
    '''
    cur.execute('''CREATE TABLE INVENTORY(
        ID          INT             NOT NULL,
        NAME        CHAR(64)        NOT NULL,
        SLOT        CHAR(32)        NOT NULL,  
        EFFECT      CHAR(256)       NOT NULL,
        TEXT        CHAR(512)       NOT NULL,
        CHARACTER   INT             NOT NULL,
        PRIMARY KEY (ID),
        FOREIGN KEY (CHARACTER) REFERENCES CHARACTER(ID)
    );
    ''')
    cur.execute('''CREATE TABLE EQUIPPED(
        ITEM        INT             NOT NULL,
        CHARACTER   INT             NOT NULL,
        FOREIGN KEY (CHARACTER) REFERENCES CHARACTER(ID),
        FOREIGN KEY (ITEM) REFERENCES INVENTORY(ID)
    );
    ''')
    



    con.commit()
    cur.close()