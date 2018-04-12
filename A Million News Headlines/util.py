

def connect_to_database_server(dbname):
    import psycopg2
    # PostGresSQL Params
    HOST = "localhost"
    USER = "postgres"
    PASSWORD = "postcavingres"
    
    try:
        conn = psycopg2.connect(host = HOST, database = dbname, user = USER, password = PASSWORD);
        cur = conn.cursor() 
        return [conn, cur]
    except:
        return -1; # Connection failure
    
