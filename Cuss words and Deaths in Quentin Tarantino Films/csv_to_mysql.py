"""
    This script transfers data from csv to MySQL database.
"""
import sys
import csv
import pymysql

DATABASE = "tarantino"

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
    file_name = 'tarantino.csv'
        
    with open(file_name, "r", encoding='utf8') as file:
        reader = csv.reader(file)
        for idx, line in enumerate(reader):
            if idx == 0:
                continue
                
            query = "INSERT INTO tarantino(movie, ttype, \
                                    word, minutes_in) \
                                    VALUES (%s, %s, %s, %s);"
                         
            data = (line[0], line[1], line[2], float(line[3]))
            cur.execute(query, data)
    
    conn.commit()
    cur.close()
    conn.close()
    print("done")
    
if __name__ == "__main__":
    main()
