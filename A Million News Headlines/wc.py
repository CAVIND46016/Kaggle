"""
    The script builds a wordcloud using the Python WordCloud package.
"""
import sys
from collections import Counter

from wordcloud import WordCloud
import matplotlib.pyplot as plt

from util import connect_to_database_server

DATABASE = "ABCNews"

def generate_wc(conn, cur, n_g):
    """
        Generates WordCloud from the text queried from the database.
        n_g : 1, for single word, 2 for bigrams, 3 for trigrams, and so on.
    """
    query = "select headline_text from abcnews;"
    
    cur.execute(query)
    row = cur.fetchone()
    
    text = " "
    while row is not None:
        text += " " + " ".join([x.lower() for x in row])
        row = cur.fetchone()
    
    cur.close()
    conn.close()
      
    ngrams = lambda a, n: zip(*[a[i:] for i in range(n)])
    n_grams = Counter(ngrams(text.lower().split(), n_g)).most_common(50)
    
    dict_n_grams = {}
    for key, val in dict(n_grams).items():
        dict_n_grams[' '.join(key)] = val
    
    word_cloud = WordCloud(max_font_size=40, collocations=False, \
                   background_color="white", width=512, height=384)
    word_cloud.generate_from_frequencies(frequencies=dict_n_grams)
    plt.figure()
    plt.imshow(word_cloud, interpolation="bilinear")
    plt.axis("off")
    plt.show()

def main():
    """
    Entry-point for the function.
    """
    conn_obj = connect_to_database_server(DATABASE)
    
    if conn_obj == -1:
        print("Connection to PostgreSQL Database: {} failed.".format(DATABASE))
        sys.exit(0)
    else:
        conn = conn_obj[0]
        cur = conn_obj[1]
        
    n_g = 3 #2 for bigrams, 3 for trigrams and so on.
    generate_wc(conn, cur, n_g)
    
if __name__ == "__main__":
    main()
    
