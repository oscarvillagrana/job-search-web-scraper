import db

def test_create_schema(database):
    db.create_schema(database)
    cur = database.cursor()
    # makes sure the table exists
    cur.execute('SELECT * FROM logs')
    # do 2nd time without error
    db.create_schema(database)