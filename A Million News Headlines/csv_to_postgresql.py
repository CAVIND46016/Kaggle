"""
    The script transfers data from csv file to Postgresql database table.
"""
import sys
import csv
from datetime import datetime

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
    
    file_name = "abcnews-date-text.csv"

    with open(file_name, "r", encoding='utf8') as f_read:
        reader = csv.reader(f_read)
        for idx, line in enumerate(reader):
            if idx == 0:
                continue
                
            query = "INSERT INTO abcnews(publish_date, headline_text) VALUES (%s, %s);"         
            data = (datetime.strptime(line[0], "%Y%m%d").date(), line[1])
            cur.execute(query, data)
    
    conn.commit()
    cur.close()
    conn.close()
    
if __name__ == "__main__":
    main()
