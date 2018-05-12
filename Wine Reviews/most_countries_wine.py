"""
    Visualization 1: Countries with most entries of wine.
"""
import sys

import pymysql
import matplotlib.pyplot as plt
import numpy as np

DATABASE = "winemag"

def main():
    """
        Entry-point of the program
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
    x_axis, num = [], []
    
    # View definition:
    # CREATE OR REPLACE VIEW most_countries_wine AS(
    # SELECT country, COUNT(country) AS count_country
    # FROM wine
    # GROUP BY country
    # ORDER BY COUNT(country) DESC);
    
    query = "SELECT country, count_country FROM most_countries_wine;"
    
    cur.execute(query)
    rows = cur.fetchall()

    for row in rows:
        x_axis.append(row[0])
        num.append(row[1])
        
    cur.close()
    conn.close()

    plt.barh(x_axis, np.array(num))
    plt.ylabel("Country")
    plt.xlabel("Count of wine entries")
    plt.show()
    
if __name__ == "__main__":
    main()
    
