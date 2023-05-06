from django.shortcuts import render
from urllib import request
from django.http import HttpResponse
# import nltk 
# nltk.download('punkt')
# from nltk.tokenize import word_tokenize
# import numpy as np
# Create your views here.
# def paraphrase(request):
#     if request.method == 'POST':
#         org_sentence = request.POST.get('original_sentence', '')
#         tokenized_sentence = nltk.word_tokenize(original_sentence)
#         replacement_words = get_replacement_words(tokenized_sentence)
#         paraphrased_sentence = replace_words(tokenized_sentence, replacement_words)
#         return render(request, 'paraphrase.html', {'original_sentence': original_sentence,
#                                                    'paraphrased_sentence': paraphrased_sentence})
#     else:
#         return render(request, 'paraphrase.html')       
# tokenized_sentence = 'He is a good boy'
# x = tokenized_sentence.split()
# print(x)
# def get_replacement_words(tokenized_sentence):
#     replacement_words = word_tokenize(tokenized_sentence)
#     return replacement_words

    
import openai

def renderTemplate(request):
    return render(request, 'index.html')
# openai api key = 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
# openai api key 1 = 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
def  rephrase(request):
    if request.method == 'POST':
        # prompt = request.POST['prompt']
        # message = request.data['prompt']
        message = request.POST['prompt']
        openai.api_key = "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"
        prompt = f"Paraphrase this and give two results -{message}"
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            temperature=0.5,
            max_tokens=1024,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
        response_text = response.choices[0].text.strip()
        data = {
            'response_text' : response_text,
        }
        # print(response_text)
        # return HttpResponse(response_text)
        return render(request, 'index.html', context = data) 
    return HttpResponse('Enter a valid text!!')
        # {response_text : response_text})

# def create(response_text):
#     return HttpResponse(response_text, render('index.html'))