import pytest
import sqlite3

@pytest.fixture
def database():
    # creates in memory database
    conn = sqlite3.connect('memory:')
    yield conn
    # cleanup connection
    conn.close()

