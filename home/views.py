from django.shortcuts import render
import random
import csv


def random_quote(request):
    with open('Motivational_Quotes_Database.csv') as quotefile:
        content = csv.reader(quotefile, delimiter=';')
        choice = random.choice(list(content))
        context = {'text': choice[0], 'author': choice[1]}
    return render(request, 'home.html', context)
