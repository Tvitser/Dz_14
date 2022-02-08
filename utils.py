import sqlite3
def search_by_id(id):
    with sqlite3.connect("netflix.db") as connection:
        data={}
        cursor=connection.cursor()
        cursor.execute(f"""
        SELECT title, country, release_year, listed_in, description FROM netflix 
        WHERE show_id == 's{id}'
        ORDER BY 'release_year'
        LIMIT 1
        """)
        raw_data=cursor.fetchone()
        data["title"]=raw_data[0]
        data["country"]=raw_data[1]
        data["release_year"]=raw_data[2]
        data["genre"]=raw_data[3]
        data["description"]=raw_data[4]
        return data



def search_by_title(title):
    with sqlite3.connect("netflix.db") as connection:
        data={}
        cursor=connection.cursor()
        cursor.execute(f"""
        SELECT title, country, release_year, listed_in, description FROM netflix 
        WHERE title LIKE '%{title}%'
        ORDER BY release_year
        LIMIT 1
        """)
        raw_data=cursor.fetchone()
        data["title"]=raw_data[0]
        data["country"]=raw_data[1]
        data["release_year"]=raw_data[2]
        data["genre"]=raw_data[3]
        data["description"]=raw_data[4]
        return data

def search_by_year(year1, year2):
    with sqlite3.connect("netflix.db") as connection:
        data=[]
        cursor=connection.cursor()
        cursor.execute(f"""
        SELECT title, release_year FROM netflix 
        WHERE release_year BETWEEN year1 AND year2
        ORDER BY release_year
        LIMIT 100
        """)
        raw_data=cursor.fetchall()

        for i in range(len(raw_data)):
            data.append({"title":raw_data[i][0]})
            data[i]["release_year"]=raw_data[i][1]

        return data

def search_by_rating(rating):
    data = []
    if rating=="children":
        age_restrictions=('G', "Null")
    elif rating=="family":
        age_restrictions=('G', 'PG', 'PG-13')
    elif rating=="adult":
        age_restrictions=('R', 'NC-17')
    else:
        return data
    with sqlite3.connect("netflix.db") as connection:
        data=[]
        cursor=connection.cursor()
        cursor.execute(f"""
        SELECT title, rating, description FROM netflix 
        WHERE rating LIKE {age_restrictions}
        ORDER BY rating
        LIMIT 100
        """)
        raw_data=cursor.fetchall()

        for i in range(len(raw_data)):
            data.append({"title":raw_data[i][0]})
            data[i]["rating"]=raw_data[i][1]
            data[i]["description"] = raw_data[i][2]

        return data

def search_by_genre(genre):
    with sqlite3.connect("netflix.db") as connection:
        data=[]
        cursor=connection.cursor()
        cursor.execute(f"""
        SELECT title, description FROM netflix 
        WHERE listed_in LIKE '%{genre}%'
        ORDER BY title
        LIMIT 100
        """)
        raw_data=cursor.fetchall()
        for i in range(len(raw_data)):
            data.append({"title":raw_data[i][0]})
            data[i]["description"]=raw_data[i][1]

        return data

def search_by_actors(actor1, actor2):
    with sqlite3.connect("netflix.db") as connection:
        data=[]
        cursor=connection.cursor()
        cursor.execute(f"""
        SELECT * FROM netflix 
        WHERE [cast] LIKE '%{actor1}%' AND [cast] LIKE '%{actor2}%'
        ORDER BY title
        LIMIT 100
        """)
    return cursor.fetchall()

def search_by_year_genre_type(year, genre, type):
    with sqlite3.connect("netflix.db") as connection:
        data=[]
        cursor=connection.cursor()
        cursor.execute(f"""
        SELECT * FROM netflix 
        WHERE type is '{type}' AND release_year IS {year} AND listed_in LIKE '%{genre}%'
        ORDER BY title
        LIMIT 100
        """)
    return cursor.fetchall()
