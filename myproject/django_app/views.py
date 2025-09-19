from django.shortcuts import render,redirect
from django.http import HttpResponse
# from .models import Patient
from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import login


# Create your views here.

def greet(request):
    return HttpResponse("Hello, learn Python")


#-------------------------------------------------------------------------------------------------------------
def hello(request):
    person_data={  #this type python dictionary
    'person':[{     #list type dictionary
     "name":"Shamila",
     "place":"Kannur",
     "details":False
    },
    {
     "name":"Adhila",
     "place":"Malapuram",
     "age":22,
     "details":True
    },
    {
     "name":"Hadhiya",
     "place":"Palakad",
     "age":18,
     "details":True
    },
    {
     "name":"Shanif",
     "place":"Mannarkad",
     "age":25,
     "details":True
    },
    { 
     "name":"Haniya",
     "place":"Thaliparamb",
     "age":24,
     "details":True
    },
    ]}
    
    return render(request,'first.html',person_data)



#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def patient_list(request):
    patients_data={
    'list':[{
    'name':'Rahul',
    'age':20,
    'disease':'fever'
    },
    {
    'name':'Radhu',
    'age':18,
    'disease':'head pain'
    },
    {
    'name':'Raniya',
    'age':19,
    'disease':'leg pain'
    },
    {
    'name':'Shamila',
    'age':21,
    'disease':'Stomach pain'
    },
    {
    'name':'Wafa',
    'age':20,
    'disease':'fever'
    },
    ]} # pyright: ignore[reportInvalidTypeForm]
    return render(request,'patients.html', patients_data)

def doctor_list(request):
    doctors_data={
    'data':[{
    'name':'Dr.Anub',
    'specialization':'Cardiologist',
    'time':'1pm to 4pm'
    },
    {
    'name':'Dr.Sahul',
    'specialization':'ENT',
    'time':'10am to 1pm'
    },
    {
    'name':'Dr.Rashid',
    'specialization':'General OP',
    'time':'10am to 12:30'
    },
    ]}
    return render(request,'doctors.html', doctors_data)
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------
# def list_patients(request):
#     patients = Patient.objects.all()
#     return render(request, 'hospital.html', {"patients": patients})

# def add_patient(request):
#     if request.method == "POST":
#         name = request.POST.get("name")
#         age = request.POST.get("age")
#         disease=request.POST.get("disease")
#         if name:
#             Patient.objects.create(name=name,age=age,disease=disease)
#     return redirect("list_patients")
# def delete_patient(request, id):
#     patient = get_object_or_404(Patient, id=id)
#     if request.method == "POST":
#         patient.delete()
#     return redirect("list_patients")
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            return render(request, "login.html", {"error": "Invalid username or password"})
    return render(request, "login.html")

def logout_view(request):
    logout(request)
    return redirect("login")

@login_required
def home(request):
    return render(request, "login.html")