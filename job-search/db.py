"""Database functions"""

sql_schema = '''
CREATE TABLE IF NOT EXISTS logs (
    time TIMESTAMP,
    level VARCHAR(16),
    MESSAGE TEXT
);

CREATE INDEX IF NOT EXISTS logs_time ON logs(time);
CREATE INDEX IF NOT EXISTS logs_level ON logs(level);
'''

def create_schema(conn):
    """create logs schema in database"""
    cur = conn.cursor()
    try:
        cur.executescript(sql_schema)
        conn.commit()
    except Exception:
        conn.rollback()
        raise