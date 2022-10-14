from django.shortcuts import render
from ast import Return
from re import I
from urllib import request
import sklearn
import joblib



# Create your views here.
def home(request):
    return render(request,'index.html')


def result(request):
    list=[]
    list.append(request.GET['Follicle1'])
    list.append(request.GET['Follicle2'])
    if request.GET["Skin darkening(Y/N)"]=='yes':
        list.append(1)
    else:
        list.append(0)

    if request.GET["Hair growth(Y/N)"]=='yes':
        list.append(1)
    else:
        list.append(0)


    if request.GET["Weight gain(Y/N)"]=='yes':
        list.append(1)
    else:
        list.append(0)


    if request.GET["Cycle(R/I)"]=='regular':
        list.append(1)
    else:
        list.append(0)


    model_pcos=joblib.load('pcos_model.sav')
    ans=model_pcos.predict([list])
    if ans == 1:
        ans1='Yes'
    elif ans==0:
        ans1='No'



    return render(request,'result.html',{'ans1':ans1})