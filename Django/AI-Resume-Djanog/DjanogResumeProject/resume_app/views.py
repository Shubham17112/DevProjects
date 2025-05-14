from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.forms import UserCreationForm  
from resume_app.forms import CustomForm
import json,re
# Create your views here.
from google import genai
import requests
def index(request):
    form = CustomForm()
    if request.method == 'POST':
        form = CustomForm(request.POST)
        if form.is_valid():
            name=form.cleaned_data['name']
            email=form.cleaned_data['email']
            mobile=form.cleaned_data['mobile']
            address=form.cleaned_data['address']
            exeperice_1=form.cleaned_data['exeperice_1']
            exeperice_2=form.cleaned_data['exeperice_2']
            Job_Description = form.cleaned_data['Job_Description']
            Project_Info = form.cleaned_data['Project_Info']
            
            data = {
                'name':name,
                'email':email,
                'mobile':mobile,
                'address':address,
                'exeperice_1':exeperice_1,
                'exeperice_2':exeperice_2,
                'Job_Description':Job_Description,
                'Project_Info':Project_Info
                
            }
            request.session['data'] = data
            
            # print(request.session['data'])
            skillCreator(request)
            
    return render(request,'Home/index.html',{'a':form})

try:
    def jobSummary(request):
        print('job summary hit')
        data = request.session.get('data')
        Job_Description = data['Job_Description'] 
        print('this si job description',Job_Description)
        client = genai.Client(api_key="AIzaSyBwzyss_nF_oi_oqXkhs0toD4WcHu-uw3M")

        try:
            response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=f"  The following is a job description for a {Job_Description}.please create a 2 line  summary for candidate resume. and please make text inside in the string without any extra text"
        
        )
        except Exception as e:
            print(e)
        print('response has been set')
        res = response.text
        
        
        
        HttpResponse('hello')
except Exception as e:
    print(e)


def skillCreator(request):
        data = request.session.get('data')
        Job_Description = data['Job_Description'] 
        print('this si job description',Job_Description)
        client = genai.Client(api_key="AIzaSyBwzyss_nF_oi_oqXkhs0toD4WcHu-uw3M")

        try:
            response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=f"  The following is a job description for a {Job_Description}.please create a skills into json formate note only top 4 skill requried "
        
        )

        except Exception as e:
            print(e)
        
        res = response.text

        print('response has been set')
        res = re.sub(r'```json|```','',res).strip()

        print(res)
        res = json.loads(res)
        print(res)
        
        HttpResponse('hello')
        
def projectcreation(request):
    data = request.session.get('data')
    Project_Info = data['Project_Info']
    client = genai.Client(api_key="AIzaSyBwzyss_nF_oi_oqXkhs0toD4WcHu-uw3M")

    try:
        response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=f"The following is a job description for a {Project_Info}.please create a skills into json formate note only top 4 skill requried "
        
        )

    except Exception as e:
        print(e)
    

def resumeCreation(request):
    data = request.session.get('data')
    
    pass