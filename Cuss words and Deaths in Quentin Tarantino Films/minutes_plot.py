"""
    The script builds a histogram using the matplotlib package.
"""
import sys

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

import pymysql

DATABASE = "tarantino"
MOVIE = "Kill Bill: Vol. 2"

#Legend color
COLOR_WORD = 'green'
COLOR_DEATH = 'red'

def get_mins(q_type, cur):
    """
        Get the minutes_in field value sorted given
        the type and the movie name.
    """
    query = "SELECT minutes_in\
            FROM tarantino\
            WHERE ttype = '{}'\
            AND movie = '{}'\
            ORDER BY minutes_in;".format(q_type, MOVIE)
    
    cur.execute(query)
    rows = cur.fetchall()
    
    mins = []
    for row in rows:
        mins.append(float(row[0]))
        
    return mins

def generate_plot(conn, cur):
    """
        Generates WordCloud from the word-frequency count queried from the database.
    """
    mins_word = get_mins("word", cur)
    mins_death = get_mins("death", cur)
    cur.close()
    conn.close()
    
    green_patch = mpatches.Patch(color=COLOR_WORD, label='Profane word')
    red_patch = mpatches.Patch(color=COLOR_DEATH, label='Death')
    
    plt.hist(mins_word, histtype='bar', color=COLOR_WORD)
    plt.hist(mins_death, histtype='bar', color=COLOR_DEATH)
    plt.legend(handles=[red_patch, green_patch])
    plt.title(MOVIE)
    plt.xticks(range(0, 181, 10))
    plt.yticks(range(0, 120, 10))
    plt.xlabel('Minutes')
    plt.ylabel('Count')
    plt.show()

def main():
    """
    Entry-point for the function.
    """
    try:
        conn = pymysql.connect(host='localhost', port=3306, \
                               user='root', passwd='mysql', \
                               db=DATABASE, charset='utf8')
    except pymysql.err.OperationalError as poe:
        print(poe.args[1])
        sys.exit(0)
    except pymysql.err.InternalError as pie:
        print(pie.args[1])
        sys.exit(0)
     
    cur = conn.cursor()
    generate_plot(conn, cur)
    
if __name__ == "__main__":
    main()
    