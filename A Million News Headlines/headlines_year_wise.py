"""
    Visualization 1: Year vs Headline count
"""
import sys

import matplotlib.pyplot as plt
import numpy as np

from util import connect_to_database_server

DATABASE = "ABCNews"

def main():
    """
        Entry-point of the program
    """
    conn_obj = connect_to_database_server(DATABASE)
    
    if conn_obj == -1:
        print("Connection to PostgreSQL Database: {} failed.".format(DATABASE))
        sys.exit(0)
    else:
        conn = conn_obj[0]
        cur = conn_obj[1]

    x, num = [], []
    
    # View definition:
    # CREATE OR REPLACE VIEW headlines_year_wise AS(
    # SELECT EXTRACT(YEAR FROM publish_date) AS Year, COUNT(headline_text) AS num_of_headlines
    # FROM abcnews
    # GROUP BY Year
    # ORDER BY Year);
    
    query = "SELECT year, num_of_headlines FROM headlines_year_wise;"
    
    cur.execute(query)
    rows = cur.fetchall()

    for row in rows:
        x.append(row[0])
        num.append(row[1])
        
    cur.close()
    conn.close()

    plt.barh(x, np.array(num))
    plt.yticks(range(2003, 2018))
    plt.xticks(range(0, 100000, 10000))
    plt.ylabel("Year")
    plt.xlabel("No. of headlines")
    plt.show()
    
if __name__ == "__main__":
    main()
    