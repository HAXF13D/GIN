import sqlite3
import pandas as pd
import os

def init_file_bd():
    con = sqlite3.connect('datebase.db')
    cur = con.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS file(
                                         filename TEXT,
                                         category TEXT,
                                         username TEXT
                                         )''')
    con.commit()
    con.close()


def add_to_datebase(filename, category, username):
    con = sqlite3.connect("datebase.db")
    cur = con.cursor()
    cur.execute("SELECT filename FROM file WHERE filename = ?", (filename,))
    cur.execute("INSERT INTO file VALUES (?, ?, ?)", (filename, category, username))
    con.commit()
    con.close()

def get_all_files():
    result = []
    try:
        con = sqlite3.connect("datebase.db")
        cur = con.cursor()
        cur.execute("SELECT filename FROM file")
        result = cur.fetchall()
        con.commit()
        con.close()
    except Exception as e:
        print(e)
    temp = []
    for s in result:
        temp.append(s[0])
    result = temp
    return result[-1]

def get_all_columns():
    result = get_all_files()
    return get_columns(result)


def category_files(category):
    con = sqlite3.connect("datebase.db")
    cur = con.cursor()
    cur.execute("SELECT filename FROM file WHERE category = ?", (category,))
    status = cur.fetchall()
    con.commit()
    con.close()
    temp = []
    for s in status:
        temp.append(s[0])
    status = temp
    return status


def user_files(username):
    con = sqlite3.connect("datebase.db")
    cur = con.cursor()
    cur.execute("SELECT filename FROM file WHERE username = ?", (username,))
    status = cur.fetchall()
    con.commit()
    con.close()
    temp = []
    for s in status:
        temp.append(s[0])
    status = temp
    return status


def file_ext(filename):
    return filename.split('.')[-1]



def get_columns(filename):
    try:
        file = "VTB_data/files/" + filename
        print(file)
        ext = file_ext(file)
        print(file)
        p = os.path.abspath(file)
        print(p)
        df = None
        if ext == 'csv':
            df = pd.read_csv(file)
        if ext == 'xlsx':
            df = pd.read_excel(file)
        return df.columns.values
    except Exception as e:
        print(e)
