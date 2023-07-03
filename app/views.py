from django.shortcuts import render, redirect 
from django.http import HttpResponse, JsonResponse
from .models import *
from django.db.models.functions import ExtractMonth , ExtractYear
from django.db.models import Count
import json
# Create your views here.
def home(request):
    articles = Article.objects.order_by("created_date")
    articles_by_year_month = articles.annotate(month = ExtractMonth("created_date"), year = ExtractYear("created_date"))
    print(articles_by_year_month)
    return render(request, "app/home.html")
def article(request):
    ## 생성
    if request.method == "POST":
        print("POST")
        response = json.loads(request.body)
        article = Article.objects.create(
            title = response.get("title"),
            writer =  response.get("writer"),
            summary =  response.get("summary"),
            content =  response.get("content"),
            conclusion =  response.get("conclusion") 
        )
        for concept_name, concept_detail in enumerate(request.POST.getlist("concept")):
            concept = Concept(name = concept_name, detail = concept_detail)
            article.concepts.add(concept)
        article.save()
        return HttpResponse(200)
    else:
        return HttpResponse(400)
    ## 읽기
    if request.method == "GET":
        return HttpResponse(200)
    ## 삭제
    if request.method == "DELETE":
        return HttpResponse(200)
    ## 수정
    if request.method == "PATCH":
        return HttpResponse(200)
    
