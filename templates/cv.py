from pywebio import start_server
from pywebio.input import *
from pywebio.output import *
from pywebio.session import *
from pywebio.pin import *
def App():
    put_html('<center><h3>الملف التعريفي للطالب</h3></center>').style('background-color:#130B60; color:gold; padding:5px;')
    put_html('<p>تطبيق ويب لتصدير السير الذاتية للطلاب المؤهلين للدراسة لدينا</p>').style('text-align:center;')
    put_html('<center><img src="https://pngimg.com/uploads/student/student_PNG136.png" width="300px"></center>')
    data = input_group(
        'املأ الحقول التالية للطالب المؤهل :',
        [
            input('اسم الطالب ' , name='student'),
            input('عنوان الطالب', name='country'),
            input('البريد الالكتروني', name='email'),
            input('رقم الهاتف', name='phone',type=NUMBER),
            radio('مؤهلات الطالب' , options=['word','excel','powerpoint'], name='certi'),
            checkbox('اتقان اللغات' , options=['Arabic','English','France'],inline=True, name='lang'),
        ],)
    imgs =file_upload(
        'تحميل صورة شخصية' ,
        accept='image/*',
        multiple=True)
    for img in imgs:
        global rr
        rr = img['content']
    put_text('Student CV :')
    put_table([
        ['Profile','NAME' , 'Address' ,'Phone', 'Email' , 'Certificate' , 'Langauge'],
        [put_image(rr).style('width:50px;') ,data['student'] ,data['phone'], data['country'],data['email'],data['certi'], data['lang']]])
start_server(App, port=3345 , debug=True)