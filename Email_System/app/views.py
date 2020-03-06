"""
Definition of views.
"""
#coding:utf-8
#使用到的库
import copy
import uuid
import random
from datetime import datetime

from django.http import HttpRequest
from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponseRedirect
#下面是发邮件的
import smtplib
from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

#自己写的配置以及模型
from app.systemsettings import systemsettings
from app.models import user,friendlist,attachment,Mymail


def check_login(fun):  #自定义登录验证装饰器
    def warpper(request,*args,**kwargs):
            is_login = request.session.get('IS_LOGIN', False)
            if is_login:
                return fun(request,*args,**kwargs)
            else:
                next_url = request.get_full_path()
                request.session['next']= next_url
                return HttpResponseRedirect(f'/login?next={next_url}')
    return warpper
def check_Legality(id:str,acc:str):
    try:
        a = Mymail.objects.get(mid = id)
    except Mymail.DoesNotExist:
        return False
    if a.sender == acc or a.receiver == acc:
        return True
    return False

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Home',
            'year':datetime.now().year,
        }
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'关于开发者',
            'message':'联系网站工作人员',
            'year':datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'About',
            'message':'红衣邮箱系统',
            'year':datetime.now().year,
        }
    )

def login(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)

    if request.method == 'POST':
        acc = request.POST.get("user_email") + '@hongyi.com'
        psw = request.POST.get("password")
        tof = user.objects.filter(user_email = acc,password = psw)
        if len(tof)==1:
            request.session['IS_LOGIN'] = True
            next_url =request.session.get('next',None)
            request.session['user_email'] = acc
            request.session['user_name'] = tof[0].user_name
            if next_url:
                return HttpResponseRedirect(next_url)
            else:
                return render(
                   request,
                   'app/home_page.html',
                   {
                       'title':'登陆成功',
                       'year':datetime.now().year,
                   }
                )
        else:
            return render(
                request,
                'app/login.html',
                {
                    'errors':True,
                    'title':'log in',
                    'message':'Account or Password error!',
                    'year':datetime.now().year,
                }
            )
    return render(
        request,
        'app/login.html',
        {
            'title':'log in',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )

def logout(request):
    request.session.clear()
    return redirect('home')
def logon(request):
    message = copy.deepcopy(request.POST)
    if request.method == 'GET':
        return render(request,'app/logon.html',{'title':'log on','year':datetime.now().year,'obj':message})
    else:
        user_email = request.POST.get('user_email','')
        if user_email == '':
            message['user_email'] = ''
            return render(request,'app/logon.html',{'title':'log on','error':'1','message':message,'year':datetime.now().year,'obj':message})
        user_email += '@hongyi.com'
        accs = user.objects.values('user_email')
        for acc in accs:
            if user_email == acc['user_email']:
                message['user_email'] = ''
                return render(request,'app/logon.html',{'title':'log on','error':'1','message':message,'year':datetime.now().year,'obj':message})
        psd = request.POST.get('password','')
        psda = request.POST.get('password_again','')
        if len(psd) < 5 or psd != psda:
            message['password'] = message['password_again'] = ''
            return render(request,'app/logon.html',{'title':'log on','error':'2','message':message,'year':datetime.now().year})
        u = user()
        head = request.FILES.get('avatar')
        if head:
            u.user_head = head
        u.user_email = user_email
        nick_name = request.POST.get('nick_name','None')
        if nick_name == '':
            nick_name = 'None'
        u.user_name = nick_name
        u.password = psd
        u.last_login = datetime.now()
        u.user_sex = eval(request.POST.get('sex'))
        u.user_profile = request.POST.get('profile','')
        u.user_phonenum = request.POST.get('phonenum')
        u.save()
        request.session['IS_LOGIN'] = True
        request.session['user_email'] = user_email
        request.session['user_name'] = nick_name
        return render(request,'app/home_page.html',{'title':'注册成功','year':datetime.now().year})
@check_login
def home_page(request):
    return render(request,'app/home_page.html',
                  {
                      'title':'邮箱主页',
                      'massage':'主页',
                      'year':datetime.now().year
                  }
           )
@check_login
def writeletter(request):
    return render(request,'app/writeletter.html',
                  {
                      'title':'红衣邮箱-写信',
                      'massage':'写邮件',
                      'year':datetime.now().year,
                  }
        )
@check_login
def sendletter(request):
    send_mail = Mymail()
    send_mail.save()
    cou = int(request.POST.get('count','0'))
    if cou :
        letter = MIMEMultipart()
        letter.attach(MIMEText(request.POST.get('last'),'plain','utf-8'))
        for ifile in range(cou):
            app = attachment()
            temp = request.FILES.get(str(ifile))
            app.file = temp
            app.save()
            send_mail.files.add(app)
            f = MIMEText(temp.read(),'base64','utf-8')
            f['Content-Type'] = 'application/octet-stream'
            f.add_header('Content-Disposition','attachment',filename = temp.name)
            letter.attach(f)
    else:
        letter = MIMEText(request.POST.get('last'),'plain','utf-8')
    send_mail.content = request.POST.get('last')

    fr = request.session['user_email']
    send_mail.sender = fr
    letter['From'] = fr

    to = request.POST.get('first')
    send_mail.receiver = to
    letter['To'] = to

    letter['Subject'] = Header(request.POST.get('second'),'utf-8')
    send_mail.theme = request.POST.get('second')

    try:
        smtpobj = smtplib.SMTP()
        ss = systemsettings()
        smtpobj.connect(ss.EMAIL_HOST,ss.EMAIL_PORT)   
        smtpobj.login(ss.EMAIL_HOST_USER,ss.EMAIL_HOST_PASSWORD)
        smtpobj.sendmail(ss.EMAIL_HOST_USER,[to],letter.as_string())
    except Exception as e:
        send_mail.status = False
    send_mail.mid = ss.short_uuid(str(uuid.uuid3(uuid.NAMESPACE_DNS,fr + to + str(datetime.now()))).replace('-',''))
    print(ss.short_uuid('50e7bd6ce3b73f5c8c6647a785cec872'))
    send_mail.save()
    return render(request,'app/home_page.html',
                  {
                      'title':'发送成功',
                      'message':'邮件发送成功',
                      'year':datetime.now().year
                  }
        )
@check_login
def inbox(request):
    message = Mymail.objects.filter(receiver = request.session.get('user_email'),isdelete = False)
    for it in message:
        print(it.time)
    return render(request,'app/mailbox.html',
                  {
                      'title':'收件箱',
                      'year':datetime.now().year,
                      'boxtype':'发件人',
                      'message':message
                  }
                  )
@check_login
def sendbox(request):
    message = Mymail.objects.filter(sender = request.session.get('user_email'),isdelete = False)
    for it in message:
        print(it.time)
    return render(request,'app/mailbox.html',
                  {
                      'title':'收件箱',
                      'year':datetime.now().year,
                      'boxtype':'收件人',
                      'message':message
                  }
                  )
@check_login
def mail(request):
    if check_Legality(request.GET.get('mid'),request.session.get('user_email','')):
        mail = Mymail()
        mail = Mymail.objects.get(mid = request.GET.get('mid'))
        try:
            sender_name = user.objects.get(user_email = mail.sender).user_name
        except Exception as e:
            sender_name = ''
            pass
        try:
            receiver_name = user.objects.get(user_email = mail.receiver).user_name
        except Exception as e:
            receiver_name = ''
            pass
        if mail.sendstatus:
            status = '发送成功'
        else:
            status = '发送失败'
        if not mail.readstatus:
            mail.readstatus = True
            mail.save()

        att = []
        for f in mail.files.all():
            t = dict()
            t['name'] = f.file.name.replace('upload/','')
            t['size'] = format(f.file.size / 1024,'.2f')
            t['id'] = random.randint(0,10000)
            att.append(t)
        print(len(att))
        return render(
            request,
            'app/mail.html',
            {
                'title':mail.theme,
                'year':datetime.now().year,
                'mail':mail,
                'filelist':att,
                'attc':mail.files.count,
                'sendername':sender_name,
                'receivername':receiver_name,
                'status':status,
            }
        )
    else:
        return render(
            request,
            'app/index.html',
            {
                'title':'Home',
                'year':datetime.now().year,
            }
        )
@check_login
def addressbook(request):
    pass
@check_login
def settings(request):
    pass
