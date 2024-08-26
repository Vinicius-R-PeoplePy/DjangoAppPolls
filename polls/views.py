from django.db.models import F 
from django.urls import reverse 
from django.shortcuts import HttpResponse, HttpResponseRedirect
#from django.template import loader
from .models import Choice, Question
from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.views import generic

class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        """Return the last five publised questions."""
        return Question.objects.order_by("-pub_date")[:5]
    
class DetailView(generic.DetailView):
    model = Question 
    template_name = "polls/detail.html"

class ResultsView(generic.DetailView):
    model = Question 
    template_name = "polls/results.html"

def vote(request, question_id):
    model = Question 
    template_name = "polls/results.html"






















'''def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    #output = ", ".join([q.question_text for q in latest_question_list])
    #return HttpResponse("Hello, world. You're at the polls index.")
    #return HttpResponse(output)
    #template = loader.get_template("polls/index.html")
    context = { 
        "latest_question_list": latest_question_list,
    }
    #return HttpResponse(template.render(context, request))
    return render(request, "polls/index.html", context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/detail.html", {"question": question})'''

'''try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, "polls/details.html", {"question": question})'''
   #return HttpResponse("You're looking at question %s." % question_id)
   
'''
   Why do we use a helper function get_object_or_404() instead of automatically catching the ObjectDoesNotExist exceptions at a higher level, or having the model API raise Http404 instead of ObjectDoesNotExist?
   Because that would couple the model layer to the view layer. One of the foremost design goals of Django is to maintain loose coupling. Some controlled coupling is introduced in the django.shortcuts module.

   There’s also a get_list_or_404() function, which works just as get_object_or_404() – except using filter() instead of get(). It raises Http404 if the list is empty.
'''

def results(request, question_id):
    #response = "You're looking at the results of question %s."
    question = get_object_or_404(Question, pk=question_id)
    #return HttpResponse(response % question_id)
    return render(request, "polls/results.html", {"question": question})

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form. 
        return render(
            request,
            "polls/detail.html",
            {
                "question": question,
                "error_message": "You didn't select a choice.",
            },
        )
    else:
        selected_choice.votes = F("votes") + 1 
        selected_choice.save()
        # Always return an HttpResponseRedirect after succesfully dealing
        # with POST data. This prevents data from being posted twice if 
        # a user hits the Back button. 
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))


