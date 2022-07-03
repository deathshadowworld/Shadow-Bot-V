from os import truncate
from sqlite3.dbapi2 import IntegrityError, ProgrammingError
import discord
import datetime
import sqlite3
import random
import testmap
import threading

userDB = sqlite3.connect('test.db')




class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))
        

    async def on_message(self, message):
        content = str(message.content)
        channel = message.channel
        author = message.author
        numberID = author.id
        strID = str(numberID)
        try:
            if (content == 'register user'):
                userDB.execute("INSERT INTO USER(ID) VALUES ("+strID+")")
                userDB.commit()
                await channel.send ('User registered into the database.')

            if (strID == '259999538666930177'):
                if (content == 'view user'):
                    cursor = userDB.execute("SELECT ID, NAME, STATUS FROM USER")
                    for row in cursor:
                        name = row[1] or 'None'
                        status = row[2] or 'None'
                        data = '`ID = '+str(row[0])+'` **|** `Name = '+name+'` **|** `Status = '+status+'`'
                        await channel.send (data)
                if (content == 'view character'):
                    cursor = userDB.execute("SELECT ID, NAME, CLASS, PLAYERID FROM CHARACTER")
                    for row in cursor:
                        id = row[0] or 'None'
                        name = row[1] or 'None'
                        Class = row[2] or 'None'
                        playerID = row[3] or 'None'
                        data = '`ID = '+str(id)+'` **|** `Name = '+name+'` **|** `Class = '+Class+'` **|** `Player = '+str(playerID)+'`'
                        await channel.send (data)
                if (content.startswith('update user ')):
                    content = content.replace('update data ','')
                    if (content.startswith('name')):
                        content = content.replace('name ','')
                        userDB.execute("UPDATE USER SET NAME = '"+content+"' WHERE ID = "+strID)
                        userDB.commit()
                        await channel.send ('Name `'+content+'` updated into your profile.')
                    if (content.startswith('status')):
                        content = content.replace('status ','')
                        userDB.execute("UPDATE USER SET STATUS = '"+content+"' WHERE ID = "+strID)
                        userDB.commit()
                        await channel.send ('Status `'+content+'` updated into your profile.')


            if (content == 'view profile'):
                cursor = userDB.execute("SELECT NAME,STATUS FROM USER WHERE ID = "+strID)
                for row in cursor:
                    name = row[0]
                    status = row[1]
                #await channel.send (embed = buildEmbed(prAuthor='Shadow Bot IV', prFooter=strID,prTitle=name, prDesc=status, prThumbnail=author.avatar_url))
                await channel.send (embed = buildProfile(prEmbed(prID = strID, prAuthor='Shadow Bot IV', prFooter=strID, prTitle=name, prDesc=status, prThumbnail=author.avatar_url)))
            
            global state
            global new
            if new is None:
                new = newUser(strID)

            if (content.startswith('update character ')):
                content = content.replace('update character ','')
                if (content.startswith('image')):
                    content = content.replace('image','')
                    content = content.replace(' ','')
                    userDB.execute("UPDATE CHARACTER SET IMAGE = '"+content+"' WHERE PLAYERID = "+strID)
                    userDB.commit()
                    await channel.send ('Image `'+content+'` updated into your profile.')

            if (content == 'register character' and state.getState() == 0):
                if checkPlayer(strID):
                    await channel.send ('You already have a character')
                    return
                else:
                    state.changeState(1)
                    state.changeLock(strID)
                    await channel.send ('Please enter your character name.')                 
            if (state.getState() == 1 and strID == state.getLock() and content != 'register character'):
                new.name = content
                await channel.send ('Please pick your class using the numbers.')
                await channel.send ('''```css
[1]   Warrior - Adept in hand-to-hand combat
[2]   Archer  - Adept in ranged attacks
[3]   Caster  - Adept in damaging spells
[4]   Healer  - Adept in healing and support spells```''')
                state.changeState(2)
                fresh = True
            
            if (state.getState() == 2 and strID == state.getLock() and content.isdigit()):
                new.charClass = content
                state.changeState(0)
                new.charInit()
                await channel.send ('Your character is registered. Please head to your profile.')

            if (state.getState() == 2 and strID == state.getLock() and not content.isdigit() and fresh is False):
                await channel.send ('Class not found. Please try again.')
                fresh = False

        except ProgrammingError:
            await channel.send ("Database error.")
        except IntegrityError:
            await channel.send ("You are already registered.")
        except IndexError:
            await channel.send ("The value you're looking for isn't available.")