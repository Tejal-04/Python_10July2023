from fixtures.mydb import MyDB

def test_johns_id():
    db = MyDB()
    conn = db.connect('server')
    cur = conn.cursor()
    id = cur.execute('select id from employee_db where name = John')
    assert id == 123
def test_toms_id():
    db = MyDB()
    conn = db.connect('server')
    cur = conn.cursor()
    id = cur.execute('select id from employee_db where name = Tom')
    assert id == 789
    