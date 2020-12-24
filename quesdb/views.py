from django.shortcuts import render, get_object_or_404,render_to_response
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from itertools import chain
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.db.models import Count
from django.db.models import Avg
from django.db.models import Sum,Avg,Min,Max

from .models import Squiz,Sanswer,Tanswer,Tquiz,Score,User
id_answer=-1
qno_squiz=""
qno_tquiz=""


def about(request):
    return render(request, 'quesdb/about.html', {'title': 'About'})

def home(request):
    return render(request, 'quesdb/home.html')
#操作失败页面
#
@login_required(login_url='login')
def failtofind(request):
    return render(request, 'quesdb/failtofind.html', {'title': 'Fail'})

#首页
#
@login_required(login_url='login')
def first(request):
    return render(request, "quesdb/first.html")

#看填空或选择
#
@login_required(login_url='login')
def newTorS(request):
    return render(request, "quesdb/newTorS.html")

#添加填空或选择
#
@login_required(login_url='login')
def addTorS(request):
    return render(request, "quesdb/addTorS.html")

#操作成功页面
#
@login_required(login_url='login')
def success(request):
    return render(request, 'quesdb/success.html', {'title': 'Success'})

#判断查询是否存在函数
def operationFail(dblist,targetkey):
    tem = [item for item in dblist]
    finding_list = []
    for eachitem in tem:
        finding_list.append(eachitem.pk)
    if targetkey not in finding_list:
        return False
    else:
        return True

#修改或删除选择题
@login_required(login_url='login')
def select(request):
    global qno_squiz
    s = Squiz.objects.filter(setter=request.user.pk)
    if request.method == 'GET':
        return render(request,"quesdb/select.html",locals())
    elif request.method == 'POST':
        qno_squiz = request.POST.get('squizno')
        del_squizno = request.POST.get("del_squizno")
        whichButton= request.POST.get("abc")
        if(whichButton=="1"):
            if operationFail(s,qno_squiz)==False:
                request.session['fail'] = "啊啊啊题目不存在~"
                return redirect('/failtofind/')
            else:
                Sanswer.objects.filter(qno=qno_squiz).delete()
                Score.objects.filter(setter=User.objects.get(id=request.user.pk)).update(score=0)
                return redirect('/updatedb/')
        elif(whichButton=="2"):
            if operationFail(s, del_squizno) == False:
                request.session['fail'] = "啊啊啊题目不存在~"
                return redirect('/failtofind/')
            else:
                Sanswer.objects.filter(qno=del_squizno).delete()
                Squiz.objects.get(squizno=del_squizno).delete()
                Score.objects.filter(setter=User.objects.get(id=request.user.pk)).update(score=0)
                request.session['success'] = "恭喜~删除成功啦！"
                return redirect('/success/')

#修改或删除填空题
#
@login_required(login_url='login')
def tiankong(request):
    global qno_tquiz
    t=Tquiz.objects.filter(setter=request.user.pk)
    if request.method == 'GET':
        return render(request,"quesdb/tiankong.html",locals())
    elif request.method == 'POST':
        qno_tquiz = request.POST.get('tquizno')
        del_tquizno = request.POST.get("del_tquizno")
        whichButton=request.POST.get("abc")
        if (whichButton=='1'):
            if operationFail(t, qno_tquiz) == False:
                request.session['fail'] = "啊啊啊题目不存在~"
                return redirect("/failtofind/")
            else:
                Tanswer.objects.filter(qno=qno_tquiz).delete()
                Score.objects.filter(setter=User.objects.get(id=request.user.pk)).update(score=0)
                return redirect('/tkupdatedb/')
        elif (whichButton=='2'):
            if operationFail(t, del_tquizno) == False:
                request.session['fail'] = "啊啊啊题目不存在~"
                return redirect("/failtofind/")
            else:
                Tanswer.objects.filter(qno=del_tquizno).delete()
                Tquiz.objects.get(tquizno=del_tquizno).delete()
                Score.objects.filter(setter=User.objects.get(id=request.user.pk)).update(score=0)
                request.session['success'] = "恭喜~删除成功啦！"
                return redirect("/success/")

#更新选择题
#
@login_required(login_url='login')
def updatedb(request):
    global qno_squiz
    s_squiz=Squiz.objects.get(squizno=qno_squiz)
    if request.method == 'GET':
        return render(request,'quesdb/updatedb.html', locals())
    elif request.method == 'POST':
        scontent = request.POST.get('scontent')
        setter = request.user.pk
        a = request.POST.get('a')
        b = request.POST.get('b')
        c = request.POST.get('c')
        d = request.POST.get('d')
        e = request.POST.get('e')
        if(scontent=="" or((a=="")or(b=="")or(c=="")or(d=="")or(e==""))):
            request.session['fail'] = "题目没改完哟~"
            return redirect("/failtofind/")
        else:
            squiz_setter = User.objects.get(id=request.user.pk)
            Squiz.objects.filter(squizno=qno_squiz).update(scontent=scontent, a=a, b=b, c=c, d=d, e=e)
            request.session['success'] = "恭喜~修改题目成功啦！"
            return redirect("/success/")

#更新填空题
#
@login_required(login_url='login')
def tkupdatedb(request):
    global qno_tquiz
    t_tquiz=Tquiz.objects.get(tquizno=qno_tquiz)
    if request.method == 'GET':
        return render(request,'quesdb/tkupdatedb.html', locals())
    elif request.method == 'POST':
        tquizcontent = request.POST.get('tquizcontent')
        if(tquizcontent==""):
            request.session['fail'] = "题目没改完哟~"
            return redirect("/failtofind/")
        else:
            setter = request.user.pk
            tquiz_setter = User.objects.get(id=request.user.pk)
            Tquiz.objects.filter(tquizno=qno_tquiz).update(tquizcontent=tquizcontent)
            request.session['success'] = "恭喜~修改题目成功啦！"
            return redirect("/success/")

#查找答题的题目
#
@login_required(login_url='login')
def searchfortest(request):
    global id_answer
    context = {
        'submit_type': '查询',
        'url': '/searchfortest/'
    }
    if request.method == 'GET':
        return render(request, template_name='quesdb/searchfortest.html', context=context)
    elif request.method == 'POST':
        id_answer = request.POST.get("id")
        if id_answer=="" or int(id_answer)<=0:
            request.session['fail'] = "不好意思~Spring没有这样的用户哟!"
            return redirect("/failtofind/")
        id_answer = int(request.POST.get("id"))
        s = Squiz.objects.filter(setter=id_answer)
        t = Tquiz.objects.filter(setter=id_answer)
        tem1 = [item for item in s]
        tem2 = [item for item in t]
        tem = tem1 + tem2
        finding_list = []
        for eachitem in tem:
            finding_list.append(eachitem.setter_id)
        if id_answer not in finding_list:
            request.session['fail'] = "啊啊啊TA还没出题~"
            return redirect("/failtofind/")
        else:
            return redirect('/answer/')

#添加选择题
#使用聚集函数
@login_required(login_url='login')
def add(request):
    if request.method=='GET':
        context={
        'submit_type':'添加',
        'url':'/add/'
        }
        return render(request, template_name='quesdb/add.html', context=context)

    elif request.method=='POST':
        scontent=request.POST.get('scontent')
        setter=request.user.pk
        print(setter)
        a = request.POST.get('a')
        b = request.POST.get('b')
        c = request.POST.get('c')
        d = request.POST.get('d')
        e = request.POST.get('e')
        if (scontent == "" or ((a == "") or (b == "") or (c == "") or (d == "") or (e == ""))):
            request.session['fail'] = "题目没添加完哟~"
            return redirect("/failtofind/")
        else:
            current_num=Squiz.objects.filter().count()
            if current_num==0:
                squizno="S1"
            else:
                squizno_number_list=list(Squiz.objects.order_by('-squizno').first().squizno)
                squizno_number=int(squizno_number_list[1])+1
                squizno="S"+str(squizno_number)
            squiz_setter=User.objects.get(id=request.user.pk)
            s=Squiz(squizno=squizno,setter=squiz_setter,scontent=scontent,a=a,b=b,c=c,d=d,e=e)
            s.save()
            request.session['success']="恭喜~添加题目成功啦"
            return redirect("/success/")

#添加填空题
#使用聚集函数
@login_required(login_url='login')
def tkadd(request):
    if request.method=='GET':
        context={
        'url':'/tkadd/'
        }
        return render(request, template_name='quesdb/tkadd.html', context=context)

    elif request.method=='POST':
        tquizcontent=request.POST.get('tquizcontent')
        setter=request.user.pk
        if (tquizcontent == ""):
            request.session['fail'] = "题目没添加完哟~"
            return redirect("/failtofind/")
        else:
            if Tquiz.objects.filter().count()==0:
                tquizno="T1"
            else:
                tquizno_number_list = list(Tquiz.objects.order_by('-tquizno').first().tquizno)
                tquizno_number = int(tquizno_number_list[1]) + 1
                tquizno = "T" + str(tquizno_number)
            tquiz_setter = User.objects.get(id=request.user.pk)
            t = Tquiz(tquizno=tquizno, setter=tquiz_setter, tquizcontent=tquizcontent)
            t.save()
            request.session['success']="恭喜~添加题目成功啦！"
            return redirect("/success/")

#回答题目
#使用聚集函数
@login_required(login_url='login')
def answer(request):
    global id_answer
    s = Squiz.objects.filter(setter=id_answer)
    t = Tquiz.objects.filter(setter=id_answer)
    num_select=s.count()
    if request.method=='GET':
        return render(request,'quesdb/answer.html', locals())
    elif request.method=='POST':
        #选择题答案
        check_box_list = request.POST.getlist("check_box_list")
        select_answer = []
        for each in check_box_list:
            select_answer.append(each)
        # 填空题答案
        tem_answer = request.POST.getlist("tsolution")
        answer_respondent = User.objects.get(id=request.user.pk)

        if len(check_box_list)!=num_select or ("" in tem_answer):
            request.session['fail'] = "题目没答完哦~"
            return redirect("/failtofind/")
        else:
            detect_score=Score.objects.filter(setter=User.objects.get(id=id_answer),respondent=User.objects.get(id=request.user.pk))
            if detect_score.exists()==False:
                res_setter=Score(respondent=User.objects.get(id=request.user.pk),setter=User.objects.get(id=id_answer),score=0)
                res_setter.save()
            else:
                Score.objects.filter(respondent=User.objects.get(id=request.user.pk),setter=User.objects.get(id=id_answer)).update(score=0)
            tem_answer = request.POST.getlist("tsolution")#填空题答案
            answer_respondent = User.objects.get(id=request.user.pk)

            i = 0
            for each in s:
                answer_qno=Squiz.objects.get(squizno=each.squizno)
                detect_squiz = Sanswer.objects.filter(qno=answer_qno,respondent=id_answer)
                if detect_squiz.exists() == False:
                    new_answer=Sanswer(ssolution=select_answer[i],qno=answer_qno,respondent=answer_respondent)
                    new_answer.save()
                else:
                    Sanswer.objects.filter(qno=answer_qno,respondent=id_answer).update(ssolution=select_answer[i])
                i=i+1

            i = 0
            for each in t:
                answer_qno = Tquiz.objects.get(tquizno=each.tquizno)
                detect_tquiz = Tanswer.objects.filter(qno=answer_qno, respondent=id_answer)
                if detect_tquiz.exists() == False:
                    new_answer = Tanswer(tsolution=tem_answer[i], qno=answer_qno, respondent=answer_respondent)
                    new_answer.save()
                else:
                    Tanswer.objects.filter(qno=answer_qno, respondent=id_answer).update(tsolution=tem_answer[i])
                i = i + 1
            request.session['success']="恭喜~回答成功啦！"
            return redirect("/success/")

#给答题者打分
#多表连接
@login_required(login_url='login')
def givescore(request):
    global id_answer
    s_result=Score.objects.filter(setter=User.objects.get(id=request.user.pk))
    if request.method == 'GET':
        return render(request,'quesdb/givescore.html', locals())
    elif request.method == 'POST':
        id_answer=request.POST.get("responder")
        if id_answer=="" or int(id_answer)<=0:
            request.session['fail'] = "不好意思~Spring没有这样的用户哟!"
            return redirect("/failtofind/")
        id_answer = int(request.POST.get("responder"))
        tem = [item for item in s_result]
        finding_list = []
        for eachitem in tem:
            finding_list.append(eachitem.respondent_id)
        if id_answer not in finding_list:
            request.session['fail'] = "啊啊啊~TA没有回答你的题哟！"
            return redirect("/failtofind/")
        else:
            return redirect('/makejudge/')

#
@login_required(login_url='login')
def makejudge(request):
    global id_answer
    s_squiz=Squiz.objects.filter(setter=request.user.pk).all()
    s_sanswer=Sanswer.objects.filter(respondent=id_answer).filter(qno__setter=request.user.pk).all()
    t_tanswer = Tanswer.objects.filter(respondent=id_answer).filter(qno__setter=request.user.pk).all()
    t_tquiz = Tquiz.objects.filter(setter=request.user.pk).all()
    if request.method == 'GET':
        return render(request,'quesdb/makejudge.html', locals())
    elif request.method == 'POST':
        score=request.POST.get("score")
        print(score)
        if score=="" or int(score)<=0:
            request.session['fail'] = "啊啊啊~不能这样评分哟！"
            return redirect('/failtofind/')
        Score.objects.filter(setter=User.objects.get(id=request.user.pk),respondent=User.objects.get(id=id_answer)).update(score=int(score))
        request.session['success'] = "恭喜~评分成功啦！"
        return redirect('/success/')

#查看他人的分数
#
@login_required(login_url='login')
def otherscore(request):
    s_score=Score.objects.filter(setter=User.objects.get(id=request.user.pk)).values("respondent__username","score","respondent")
    avg_score=Score.objects.all().values("respondent").annotate(Avg("score"))
    s_score = s_score.exclude(score=0)
    return render(request,"quesdb/otherscore.html",locals())

class avg_show:
    def __init__(self, nickname, score):
        self.nickname = nickname
        self.score = score
#查看自己的得分
#
@login_required(login_url='login')
def myscore(request):
    avg_score = Score.objects.all().values("respondent").annotate(avgs=Avg("score")).order_by("-avgs").values(
        "respondent__username", "avgs")
    show_avg = []
    temp_avg = avg_show((avg_score[0])["respondent__username"], (avg_score[0])["avgs"])
    show_avg.append(temp_avg)
    temp_avg = avg_show(avg_score[1]["respondent__username"], avg_score[1]['avgs'])
    show_avg.append(temp_avg)
    s_score = Score.objects.filter(respondent=User.objects.get(id=request.user.pk)).values("setter__username", "score")
    s_score = s_score.exclude(score=0)
    return render(request,"quesdb/myscore.html",locals())

@login_required(login_url='login')
def excellentscore(request):
    avg_score = Score.objects.all().exclude(score=0).values("respondent").annotate(avgs=Avg("score")).order_by("-avgs").values("respondent__username", "avgs")
    show_avg = []
    temp_avg = avg_show((avg_score[0])["respondent__username"], avg_score[0]["avgs"])
    show_avg.append(temp_avg)
    temp_avg = avg_show(avg_score[1]["respondent__username"], avg_score[1]['avgs'])
    show_avg.append(temp_avg)
    temp_avg = avg_show((avg_score[2])["respondent__username"], avg_score[2]["avgs"])
    show_avg.append(temp_avg)
    return render(request,"quesdb/excellentscore.html",locals())



