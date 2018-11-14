from sys import argv
import pymysql
from bottle import *

@get('/')
def index():
    return template('index.tpl')

@route('/donyskra', method='POST')
def nyr():
    u = request.forms.get('user')
    p = request.forms.get('pass')
    n = request.forms.get('nafn')

    conn = pymysql.connect(host='tsuts.tskoli.is', port=3306, user='3004012790', passwd='mypassword', db='3004012790_vef2_v7')

    cur = conn.cursor()
    cur.execute("SELECT count(*) FROM 3004012790_vef2_v7.users where user=%s", (u))
    result = cur.fetchone()

    if result[0] == 0:
        cur.execute("INSERT INTO 3004012790_vef2_v7.users values(%s,%s,%s)", (u,p,n))
        conn.commit()
        cur.close()
        conn.close()
        return u, " hefur verið skráður <br><a href='/'>Heim</a>"
    else:
        return u, " er frátekið notandanafn, reyndu aftur <br><a href='/#ny'>Nýskrá</a>"

@route('/doinnskra', method='POST')
def innkra():
    u = request.forms.get('user')
    p = request.forms.get('pass')

    conn = pymysql.connect(host='tsuts.tskoli.is', port=3306, user='3004012790', passwd='mypassword', db='3004012790_vef2_v7')
    cur = conn.cursor()

    cur.execute("SELECT count(*) FROM 3004012790_vef2_v7.users where user=%s and pass=%s",(u,p))
    result = cur.fetchone()
    print(result)
    if result[0] == 1:

        cur.close()
        conn.close()
        return template('leyni', u=u)
    else:
        return template('ekkileyni')
@route('/members')
def member():
    conn = pymysql.connect(host='tsuts.tskoli.is', port=3306, user='3004012790', passwd='mypassword', db='3004012790_vef2_v7')
    c = conn.cursor()
    c.execute("SELECT nafn FROM 3004012790_vef2_v7.users")
    result = c.fetchall()
    c.close()
    output=template('members',rows=result)
    return output


@route("/static/<skra>")
def static_skrar(skra):
    return static_file(skra, root='./static')

######################################################
@error(404)
def villa(error):
    return "<h2 style='color:red'>Þessi síða finnst ekki</h2>"

try:
    run(host='0.0.0.0', port=os.environ.get('PORT'))
except:
    run(host='localhost', port=8080, reloader=True, debug=True)

