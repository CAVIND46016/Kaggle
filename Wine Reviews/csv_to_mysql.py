"""
    The script transfers data from csv file to MySQL database table.
"""
import sys
import csv
import pymysql


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
    file_name = "winemag-data_first150k.csv"
    
    with open(file_name, "r", encoding='utf8') as file:
        reader = csv.reader(file)
        for idx, line in enumerate(reader):
            if idx == 0:
                continue
            
            line[5] = int(float(line[5])) if line[5] != "" else None
                
            query = "INSERT INTO wine(srno, country, \
                    description, designation, points, price,\
                    province, region_1, region_2, variety, winery)\
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s,\
                    %s, %s);"
                        
            data = (int(line[0]), line[1], line[2], line[3], 
                    int(line[4]), line[5], line[6], line[7],
                    line[8], line[9], line[10])
            
            cur.execute(query, data)
    
    conn.commit()
    cur.close()
    conn.close()

if __name__ == "__main__":
    main()
    
