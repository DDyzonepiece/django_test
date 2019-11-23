from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.shortcuts import HttpResponse,HttpResponseRedirect
from .models import Question,Choice

from django.template import loader
from django.urls import reverse
from django.http import Http404


# Create your views here.
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))
    # output = ','.join([q.question_text for q in latest_question_list])
    # return HttpResponse(output)
    # return render(request,'polls/index.html',locals())

def detail(request, question_id):
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404('你访问的问卷不存在')
    question = get_object_or_404(Question, pk=question_id)

    return render(request, 'polls/detail.html',{'question':question})


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)

    #respone = '你正在查看问卷%s的调查结果'
    return render(request,'polls/results.html',locals())


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice=question.choice_set.get(id=request.POST.get('choice'))
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html',{'question':question,
                                                    'error_message':'你没有选择一个选项'})
    else:
        selected_choice.votes +=1
        selected_choice.save()
    return HttpResponseRedirect(reverse('polls:results',args=(question.id,)))
