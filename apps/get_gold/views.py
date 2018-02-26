from django.shortcuts import render, HttpResponse, redirect
import random

def index(request):
    if 'number' not in request.session: # if there isnt a session make session if there is a session leave it alone
        request.session['number'] = 0
    if 'activities' not in request.session: # if there isnt a session make session if there is a session leave it alone
        request.session['activities'] = []
        
    return render(request, "get_gold/index.html")

def farm(request):
    earned = random.randint(10, 20)
    request.session['number'] += earned

    farm_gold = {'gold':earned, 'location': 'farm'}

    temp = request.session['activities']
    temp.append(farm_gold)
    request.session['activities'] = temp

    return redirect('/')

def cave(request):
    earned = random.randint(5, 10)
    request.session['number'] = request.session['number'] + earned

    cave_gold = {'gold':earned, 'location': 'cave'}

    temp = request.session['activities']
    temp.append(cave_gold)
    request.session['activities'] = temp

    return redirect('/')

def house(request):
    earned = random.randint(2, 5)
    request.session['number'] = request.session['number'] + earned

    house_gold = {'gold':earned, 'location': 'house'}

    temp = request.session['activities']
    temp.append(house_gold)
    request.session['activities'] = temp

    return redirect('/')

def casino(request):
    earned = random.randint(-50, 50)
    request.session['number'] = request.session['number'] + earned

    casino_gold = {'gold':earned, 'location': 'casino'}

    temp = request.session['activities']
    temp.append(casino_gold)
    request.session['activities'] = temp           

    return redirect('/')