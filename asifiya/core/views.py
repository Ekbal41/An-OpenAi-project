from django.shortcuts import render, redirect


from django.http import HttpResponse
import os
import openai
import array
from django.utils.datastructures import MultiValueDictKeyError


# Create your views here.

def oneai(request):
    #openai.api_key = os.getenv("OPENAI_API_KEY")
    openai.api_key = "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"

    
    try:
        data = request.GET['fulltextarea']
    except MultiValueDictKeyError:
        data = False

    welcome =  "welcome me to Asif.com"
    response = openai.Completion.create(
         model="text-davinci-002",
         prompt= data if data else welcome,
         temperature=0.7,
         max_tokens=256,
         top_p=1,
         frequency_penalty=0,
        presence_penalty=0
        )
    answer = response['choices'][0]['text']

    context = {
        'answer' : answer,
        'data' : data
       
    }

   
    return render(request, 'oneai.html', context)


