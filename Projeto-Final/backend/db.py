import duckdb

DB_PATH = "data/movies.duckdb"

def get_connection():
    """
    Retorna uma conexão ao banco de dados DuckDB.
    """
    return duckdb.connect(database=DB_PATH, read_only=False)

def initialize_database():
    """
    Inicializa o banco de dados e importa os CSVs.
    """
    conn = get_connection()
    conn.execute("""
        CREATE TABLE IF NOT EXISTS movies AS SELECT * FROM 'data/movies.csv';
        CREATE TABLE IF NOT EXISTS ratings AS SELECT * FROM 'data/ratings.csv';
        CREATE TABLE IF NOT EXISTS genome_scores AS SELECT * FROM 'data/genome-scores.csv';
        CREATE TABLE IF NOT EXISTS genome_tags AS SELECT * FROM 'data/genome-tags.csv';
        CREATE TABLE IF NOT EXISTS links AS SELECT * FROM 'data/links.csv';
    """)
    conn.close()
