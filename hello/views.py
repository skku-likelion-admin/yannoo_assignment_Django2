from django.shortcuts import render

# Create your views here.


def home (request) :
    return render(request, 'home.html')

def judgement (request) :
    first_score = (request.GET["first_question"]=="Gucci")
    second_score = (request.GET["sq"]=="wooyoungmi")
    score = first_score + second_score
    return render(request, "judgement.html",{"first_score" : first_score, "second_score" : second_score, "score" : score})