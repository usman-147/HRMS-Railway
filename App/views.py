from django.shortcuts import render, redirect
from .models import *

def index(request):
    return render(request, "index.html")

#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^Authority^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

def authority_register(request):
    success = ""
    if request.method == "POST":
        data = request.POST
        Authority.objects.create(
            name=data.get("name"),
            email=data.get("email"),
            company_name=data.get("company_name"),
            location=data.get("location"),
            password=data.get("password")
        )
        success = "Successfully Registered!"
    return render(request, "authority/register.html", {
        "success": success
     })

def authority_login(request):
    error = ""
    if request.method == "POST":
        email    = request.POST.get("email")
        password = request.POST.get("password")
        try:
            auth = Authority.objects.get(email=email)
            if auth.password == password:
                return redirect('/authority-display')
            else:
                error = "Invalid password"
        except Authority.DoesNotExist:
            error = "No account found with that email"
    return render(request, "authority/login.html", {"error": error})

def authority_display(request):
    m1 = HR.objects.all()
    m2 = Instructor.objects.all()
    context = {
        "m1" : m1,
        "m2" : m2,
    }
    return render(request, "authority/display.html", context)

def update_status(request):
    if request.method == "POST":
        data = request.POST
        state = data.get("state")
        case_id = data.get("search")

        m = Instructor.objects.get(id = case_id)
        m.status = state
        m.save()
        print(m.status)
        return redirect('/authority-display')
    return render(request, "authority/status.html")

def create_hr(request):
    success = ""
    if request.method == "POST":
        HRUser.objects.create(
            name=request.POST["name"],
            email=request.POST["email"],
            password=request.POST["password"]
        )
        success = "Successfully Created!"
    return render(request, "authority/create_hr.html", {
        "success": success
    })

#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^HR^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

def hr_login(request):
    error = ""
    if request.method == "POST":
        email    = request.POST.get("email")
        password = request.POST.get("password")
        try:
            hr = HRUser.objects.get(email=email)
            if hr.password == password:
                return redirect('hr-display')
            else:
                error = "Invalid password"
        except HRUser.DoesNotExist:
            error = "No HR account found with that email"
    return render(request, "hr/login.html", {"error": error})

def hr_display(request):
    m1 = HR.objects.all()
    m2 = Instructor.objects.all()
    context = {
        "m1" : m1,
        "m2" : m2,
    }
    return render(request, "hr/display.html", context)

def hr_insert(request):
    if request.method == "POST":
        data=request.POST
        print(data)
        joined_date = data.get("joined")
        dep_num = data.get("dep")
        ins_name = data.get("ins_name")
        ins_exe = data.get("ins_exe")
        ins_salary = data.get("ins_salary")
        m1 = HR(joined_data = joined_date, department = dep_num)
        m2 = Instructor(instructor_name = ins_name, experience = ins_exe, salary = ins_salary, status = "pending")
        m1.save()
        m2.save()
        return redirect('hr-display')
    return render(request, "hr/insert.html")

def search(request):
    if request.method == "POST":
        data = request.POST
        search = data.get("search")
        m1 = Instructor.objects.get(id = search)
        id = m1.id
        m2 = HR.objects.get(id = id)
        context = {
            "m1" : m1, 
            "m2" : m2,
        }
    return render(request, "hr/search.html", context)

def edit(request, id):
    if request.method == "POST":
        data=request.POST
        ins_name = data.get("ins_name")
        ins_exe = data.get("ins_exe")
        ins_salary = data.get("ins_salary")
        d_name = data.get("d_name")
        m1 = HR.objects.get(id = id)
        m2 = Instructor.objects.get(id = id)
        m1.department = d_name
        m1.save()
        m2.instructor_name = ins_name
        m2.experience = ins_exe
        m2.salary = ins_salary
        m2.save()
        return redirect("/hr-display")
    m1 = HR.objects.get(id = id)
    m2 = Instructor.objects.get(id = id)
    context = {
        "m1" : m1,
        "m2" : m2
    }
    return render(request, "hr/edit.html", context)

def delete_data(request, id):
    m1 = HR.objects.get(id = id)
    m2 = Instructor.objects.get(id = id)
    m1.delete()
    m2.delete()
    return redirect("/hr-display")

#^^^^^^^^^^^^^^^^^^^^^^^^^^^Future Iterations^^^^^^^^^^^^^^^^^^^^^^^^^^^^

def  faculty_insert(request):
    if request.method == "POST":
        data=request.POST
        print(data)
        d_name = data.get("d_name")
        d_no = data.get("d_no")
        act_name = data.get("act_name")
        act_duration = data.get("act_duration")
        bonus = data.get("bonus")
        m1 = Department(department_name = d_name, d_no = d_no)
        m2 = Activities(activity_name = act_name, activity_duration = act_duration)
        m3 = Capital(bonus = bonus)
        m1.save()
        m2.save()
        m3.save()
    return render(request, "future iterations/faculty_insert.html")

def faculty_edit(request, id):
    if request.method == "POST":
        data=request.POST
        print(data)
        d_name = data.get("d_name")
        d_no = data.get("d_no")
        act_name = data.get("act_name")
        act_duration = data.get("act_duration")
        bonus = data.get("bonus")
        m1 = Department.objects.get(id = id)
        m2 = Activities.objects.get(id = id)
        m3 = Capital.objects.get(id = id)
        m1.department_name = d_name
        m1.d_no = d_no
        m1.save()
        m2.activity_name = act_name
        m2.activity_duration = act_duration
        m2.save()
        m3.bonus = bonus
        m3.save()
        return redirect("/authority-display")
    m1 = Department.objects.get(id = id)
    m2 = Activities.objects.get(id = id)
    m3 = Capital.objects.get(id = id)
    context = {
        "m1" : m1,
        "m2" : m2,
        "m3" : m3
    }
    return render(request, "future iterations/faculty_edit.html", context)

def faculty_delete(request, id):
    m1 = Department.objects.get(id = id)
    m2 = Activities.objects.get(id = id)
    m3 = Capital.objects.get(id = id)
    m1.delete()
    m2.delete()
    m3.delete()
    return redirect("/authority-display")
