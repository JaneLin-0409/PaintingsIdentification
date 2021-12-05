import MySQLdb
from django.shortcuts import render, redirect


# Create your views here.
# 学生信息列表处理函数
def index(request):
    conn = MySQLdb.connect(host="localhost", user="root", passwd="1234", db="fairy", charset='utf8')
    with conn.cursor(cursorclass=MySQLdb.cursors.DictCursor) as cursor:
        cursor.execute("SELECT id, student_no, student_name FROM sims_student")
        students = cursor.fetchall()
    return render(request, 'student/index.html', {'students': students})


# 学生信息新增处理函数
def add(request):
    if request.method == 'GET':
        return render(request, 'student/add.html')
    else:
        diary = request.POST.get('student_no', '')
        time = request.POST.get('student_name', '')
        conn = MySQLdb.connect(host="localhost", user="root", passwd="1234", db="fairy", charset='utf8')
        with conn.cursor(cursorclass=MySQLdb.cursors.DictCursor) as cursor:
            cursor.execute("INSERT INTO fairy_page (diary,time ) "
                           "values (%s, %s)", [diary, time])
            conn.commit()
        return redirect('../')


# 学生信息修改处理函数
def edit(request):
    if request.method == 'GET':
        id = request.GET.get("id")
        conn = MySQLdb.connect(host="localhost", user="root", passwd="1234", db="fairy", charset='utf8')
        with conn.cursor(cursorclass=MySQLdb.cursors.DictCursor) as cursor:
            cursor.execute("SELECT id, diary, time FROM fairy_page where id =%s", [id])
            page = cursor.fetchone()
        return render(request, 'student/edit.html', {'student': page})
    else:
        id = request.POST.get("id")
        diary = request.POST.get('student_no', '')
        time = request.POST.get('student_name', '')
        conn = MySQLdb.connect(host="localhost", user="root", passwd="1234", db="fairy", charset='utf8')
        with conn.cursor(cursorclass=MySQLdb.cursors.DictCursor) as cursor:
            cursor.execute("UPDATE sims_student set diary=%s,time=%s where id =%s",
                           [diary, time, id])
            conn.commit()
        return redirect('../')


# 学生信息删除处理函数
def delete(request):
    id = request.GET.get("id")
    conn = MySQLdb.connect(host="localhost", user="root", passwd="123456", db="sms", charset='utf8')
    with conn.cursor(cursorclass=MySQLdb.cursors.DictCursor) as cursor:
        cursor.execute("DELETE FROM fairy_page WHERE id =%s", [id])
        conn.commit()
    return redirect('../')
