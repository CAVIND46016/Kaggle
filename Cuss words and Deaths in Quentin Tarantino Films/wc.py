"""
    The script builds a wordcloud using the Python WordCloud package.
"""
import sys

from wordcloud import WordCloud
import matplotlib.pyplot as plt

import pymysql

DATABASE = "tarantino"

def generate_wc(conn, cur):
    """
        Generates WordCloud from the word-frequency count queried from the database.
    """
    
    #CREATE OR REPLACE VIEW word_count AS(
    #SELECT word, COUNT(word) AS word_cnt
    #FROM tarantino
    #WHERE word <> ''
    #GROUP BY word
    #ORDER BY COUNT(word) DESC);
    query = "select word, word_cnt from word_count;"
    
    cur.execute(query)
    rows = cur.fetchall()
    
    word_freq = {}
    for row in rows:
        word_freq[row[0]] = int(row[1])
    
    cur.close()
    conn.close()
    
    word_cloud = WordCloud(max_font_size=40, collocations=False, \
                   background_color="white")
    word_cloud.generate_from_frequencies(frequencies=word_freq)
    plt.figure()
    plt.imshow(word_cloud, interpolation="bilinear")
    plt.axis("off")
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
    generate_wc(conn, cur)
    
if __name__ == "__main__":
    main()
    