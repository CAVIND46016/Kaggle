"""
    Pie charts for visualizing count of 'cuss words' 
    and 'death occurrences' grouped by movie name.
"""
import sys

import pymysql
import matplotlib.pyplot as plt

DATABASE = "tarantino"
_TYPE = 'word'

def main():
    """
        Entry-point of the function.
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
    
    # CREATE VIEW count_movie_type AS(
    # select movie, ttype, count(*)as cnt
    # from tarantino
    # group by movie, ttype)
    query = "select * from count_movie_type where ttype = '{}' order by cnt desc;".format(_TYPE)
    cur.execute(query)
    rows = cur.fetchall()
    cur.close()
    conn.close()
    
    labels, cnt = [], []
    for row in rows:
        labels.append(row[0])
        cnt.append(row[2])

    plt.pie(cnt, labels=labels, autopct='%1.1f%%')
    plt.axis('equal')
    plt.show()
    
if __name__ == "__main__":
    main()
    