# form django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from service.models import *
from datetime import date
# from service.utils import send_email_to_client,send_email_with_attachment
from django.conf import settings
from django.core.mail import send_mail


# def send_mail(request):
#     subject="Medistr"
#     message="message vjay thal pati"
#     recipient_list=["rushiputthewad@gmail.com"]
#     # dh= Gallery.objects.all()
#     # print(dh.deliverypic.url)
#     file_path= f"{settings.BASE_DIR}/media/Aslan.jpg"
#     print(file_path)
#     send_email_with_attachment(subject,message,recipient_list,file_path)
#     return redirect()

def homePage(request):
    return render(request,"HomePage.html")
def cards(request):
    return render(request,"card_3.html")
# Authentication of user
def login_user(request):
    error = ""
    if request.method == 'POST':
        u = request.POST.get('email')
        p = request.POST.get('pass')
        user=authenticate(request,username=u,password=p)
        if user is not None:
            print(user)
            login(request,user)
            error="no"
        else:
            error="yes"
            # return redirect('donor_hom')
        
        # try:
        #     if user.is_staff:
        #         login(request, user)
        #         error="no"
        #     else:
        #         error="yes"
        # except:
        #     error="yes"
    return render(request,"login_user.html",locals())#done
def volunter_log(request):
    if request.method == 'POST':
        u = request.POST.get('email')
        p = request.POST.get('pass')
        user = authenticate(request,username=u,password=p)
        print(user)
        if user is not None:
            login(request, user)
            error="no"
            # try:
            #     user1 = Volunteer.objects.get(user=user)
            #     if user1.status != "pending":
                    
            #     else:
            #         error="not"
            # except:
            #     error="yes"
        else:
            error="yes"
    return render(request, "volunteer_login.html",locals())
#admin
def ngo_login(request):
    error=""
    if request.method == 'POST':
        u = request.POST['email']
        p = request.POST['password']
        user = authenticate(username=u, password=p)
        try:
            if user.is_staff:
                login(request, user)
                error="no"
            else:
                error="yes"
        except:
            error="yes"
    return render(request,"ngo_login.html",locals())

def donor_regiration(request):
    error= ""
    if request.method == "POST":
        fn = request.POST['first']
        ln = request.POST['last']
        uname = request.POST['Username']
        em = request.POST['Eamil']
        con = request.POST['contact']
        pwd = request.POST['pwd']
        Cpwd = request.POST['cpwd']
        img = request.FILES['pic']
        addr = request.POST['address']
        
        try:
            user= User.objects.create_user(first_name=fn,last_name=ln,username=uname,email=str(em),password=pwd)
            Donor.objects.create(user=user,contact=con,userpic=img, address=addr)
            print(user)
            error = "no"
        except:
            error = "yes"
            
    return render(request,"donor_reg.html",locals())

def navidation_bar(request):
    return render(request,"navigation_bars.html")

#Dashboard of Donor
def donor_home(request):
    if not request.user.is_authenticated:
        return redirect("login_user")
    return render(request,"Donor_home.html")

def Logout(request):
    logout(request)
    return redirect("home_page")

def add_services(request):
    if not request.user.is_authenticated:
        return redirect("login_user")
    return render(request,"add_service.html")

def donate_now(request):
    if not request.user.is_authenticated:
        return redirect("login_user")
    # user = request.user#--------------
    # {if request.method=="POST":
    #     data=request.POST
    #     print(data)
        
    #     medicinename=data.get('medicinename')
    #     medicinepic=request.FILES.get('donationpic')
    #     description=data.get('description')
    #     medic=data.get('medicinename')
    #     try:
            
    #         donationew.objects.create(medicine=medicinename,medicinepic=medicinepic,discrib=description)#Donation #donationpic=donationpic,
    #         print(medicinename,medicinepic,description)
    #         error="no"
            
    #     except:
    #         error="yes"}
    #Start
        
    # if request.method == "POST":
    #     medicinename=request.POST.get('medicinename')
    #     donationdate=request.POST.get('purchased_date')
    #     donationpic=request.FILES.get('donationpic')
    #     description=request.POST.get('description')
    #     print(medicinename)
    #     # try:
    #         # donor1 = User.objects.get(user=user)
    #     Donation(medicinename=medicinename,donationdate=donationdate,donationpic=donationpic,description=description)
    #     #donor=donor1,,status="pending"
    #     error = "yes"
        
    #     # except:
    #         # error = "yes"
            
    # return render(request,"donate_now_form.html",locals())
    
    user = request.user.id
    userpica = Donor.objects.get(user=user)
    file_url = userpica.userpic.url
    file_con = userpica.contact
    print(type(userpica.userpic),'Name:',userpica.userpic,'fil:',file_url,file_con)
    # donor = Donor.objects.get(user=user)#create
    # print(user,donor)----
    # donoerpic=Donor.objects.filter(id=userpic)
    # print(donoerpic)
    # print(userpic)
    if request.method=="POST":
        medicinename=request.POST['medicinename']
        #loss
        tab_count=request.POST['tabCount']
        # type_me=request.POST['type_medi']
        pu_date=request.POST['purchased_date']
        ex_date=request.POST['expiry_date']
        #-------
        donationpic=request.FILES['donationpic']#Medicine image
        collectionloc=request.POST['coll']
        detail=request.POST['description']
        
        
        try:
            xw= donationew.objects.create(medicine=medicinename,tablet_con=tab_count,pur_date=pu_date,ex_date=ex_date,medicinepic=donationpic,discrib=detail,collectionloc=collectionloc,
            name=request.user.first_name,last=request.user.last_name,email=request.user.email,donorpic=userpica.userpic,contact=file_con)#,contact=donoerpic.contact,userpic=donoerpic.userpic)#Donation #donationpic=donationpic,
            print(xw)
            error="no"
        except:
            error="yes"
        
    return render(request,"donate_now_form.html",locals())

def donation_history(request):
    if not request.user.is_authenticated:
        return redirect("login_user")
    user = request.user
    donor = Donor.objects.all()
    donation = donationew.objects.all()
    return render(request,"donor_history.html",locals())

# Admin (NGO)
def ngo_home(request):
    if not request.user.is_authenticated:
        return redirect("login_user")
    return render(request,"ngo_home.html")

def ngo_reg(request):
    error= ""
    if request.method == "POST":
        reg_no = request.POST.get('reg_no')
        ngo_name = request.POST.get('first')
        n_id = request.POST.get('last')
        em = request.POST.get('Eamil')
        con = request.POST.get('contact')
        pwd = request.POST.get('pwd')
        reg_date = request.POST.get('reg_date')
        img = request.FILES.get('pic')
        idpic = request.FILES.get('idpic')
        addr = request.POST.get('address')
        city = request.POST.get('city')
        state = request.POST.get('state')
        aboutme = request.POST.get('aboutme')
        try:
            user = User.objects.create_user(last_name=n_id,username=ngo_name,email=str(em),password=pwd)#(first_name=fn,last_name=ln,username=fn,password=pwd)
            e=Ngo.objects.create(user=user,reg_no=reg_no,reg_contact=con,reg_logo=img,reg_proof=idpic,address=addr,city=city,state=state,about_self=aboutme)
            print(e.reg_no,e.reg_contact,e.reg_logo,e.reg_proof,e.address,e.city,e.state,e.about_self)
            # print(e.user.first_name,e.user.last_name,e.reg_no,e.contact,e.ngo_id,e.reg_logo,e.reg_proof,e.address,e.city,e.state,e.about_self)
            error = "no"
            
        except:
            error = "yes"
            
    return render(request,"ngo_reg.html",locals())

def pending_donation(request):
    if not request.user.is_authenticated:
        return redirect("ngo_log")
    
    donation = donationew.objects.all()#resume-------------------------------------------------------------------
    return render(request,"pending_donation.html",locals())

def view_donation(request,pid):
    if not request.user.is_authenticated:
        return redirect("ngo_log")
    donation = donationew.objects.get(id=pid)
    if request.method=="POST":
        status=request.POST['status']
        adminremark=request.POST['adminremark']
        try:
            donation.adminremark = adminremark
            donation.status =status
            donation.updationdate=date.today()
            donation.save()
            error="no"
        except:
            error="yes"
    return render(request,"view_admin_donation.html",locals())

def accepted_donation(request):
    if not request.user.is_authenticated:
        return redirect("ngo_log")
    donation = donationew.objects.filter(status="accept")
    return render(request,"accepted_donation.html",locals())

def demo_donoy_base(request):
    return

def add_area(request):
    if not request.user.is_authenticated:
        return redirect("ngo_log")
    
    if request.method=="POST":
        areaname=request.POST['areaname']
        description=request.POST['description']
        try:
            DonationArea.objects.create(areaname=areaname,description=description)
            error="no"
        except:
            error="yes"
        
    return render(request,"add_area.html",locals())

def manage_area(request):
    if not request.user.is_authenticated:
        return redirect("ngo_log")
    area = DonationArea.objects.all()
    return render(request,"manage_area.html",locals())

def edit_area(request,pid):
    if not request.user.is_authenticated:
        return redirect("ngo_log")
    
    area = DonationArea.objects.get(id=pid)
    if request.method=="POST":
        areaname=request.POST['areaname']
        description=request.POST['description']
        area.areaname=areaname
        area.description=description
        try:
            area.save()
            error="no"
        except:
            error="yes"
        
    return render(request,"edit_area.html",locals())

def delete_area(request,pid):
    area = DonationArea.objects.get(id=pid).delete()
    return redirect('manage_area')

def manage_donor(request):
    if not request.user.is_authenticated:
        return redirect("ngo_log")
    donor = Donor.objects.all()
    return render(request,"manage_donor.html",locals()) 

def view_donordetail(request,pid):
    if not request.user.is_authenticated:
        return redirect("ngo_log")
    donor = Donor.objects.get(id=pid)
    return render(request,"view_donordetail.html",locals())

def delete_donor(request,pid):
    User.objects.get(id=pid).delete()
    return redirect('manage_donor')

#Volunterr
def Volunteer_reg(request):
    error= ""
    if request.method == "POST":
        uname = request.POST['Username']
        fn = request.POST.get('first')
        ln = request.POST.get('last')
        em = request.POST.get('Eamil')
        con = request.POST.get('contact')
        pwd = request.POST.get('pwd')
        # Cpwd = request.POST.get('cpwd')
        img = request.FILES.get('pic')
        idpic = request.FILES.get('idpic')
        addr = request.POST.get('address')
        aboutme = request.POST.get('aboutme')
        try:
            user = User.objects.create_user(first_name=fn,last_name=ln,username=uname,email=str(em),password=pwd)#(first_name=fn,last_name=ln,username=fn,password=pwd)
            Volunteer.objects.create(user=user,contact=con,userpic=img, idpic=idpic,address=addr,aboutme=aboutme,status="pending")
            error = "no"
            
        except:
            error = "yes"
            
    return render(request,"Volunteer_reg.html",locals())

def Volunteer_home(request):
    if not request.user.is_authenticated:
        return redirect("volunter_log")
    return render(request,"volunteer_home.html",locals())

def new_volunteer(request):
    if not request.user.is_authenticated:
        return redirect("ngo_log")
    volunteer = Volunteer.objects.filter(status="pending")
    return render(request,"new_volunteer.html",locals())

def view_volunteerdetail(request,pid):
    if not request.user.is_authenticated:
        return redirect("ngo_log")
    volunteer = Volunteer.objects.get(id=pid)
    if request.method=="POST":
        status=request.POST['status']
        adminremark=request.POST['adminremark']
        try:
            volunteer.adminremark = adminremark
            volunteer.status =status
            volunteer.updationdate=date.today()
            volunteer.save()
            error="no"
        except:
            error="yes"
    return render(request,"view_volunteerdetail.html",locals())

def accepted_volunteer(request):
    if not request.user.is_authenticated:
        return redirect("ngo_log")
    volunteer = Volunteer.objects.filter(status="accept")
    return render(request,"accepted_volunteer.html",locals())

def rejected_volunteer(request):
    if not request.user.is_authenticated:
        return redirect("ngo_log")
    volunteer = Volunteer.objects.filter(status="reject")
    return render(request,"rejected_volunteer.html",locals())

def all_volunteer(request):
    if not request.user.is_authenticated:
        return redirect("ngo_log")
    volunteer = Volunteer.objects.all()
    return render(request,"all_volunteer.html",locals())

def delete_volunteer(request,pid):
    User.objects.get(id=pid).delete()
    return redirect('all_volunteer')

def accepted_donationdetail(request,pid):
    if not request.user.is_authenticated:
        return redirect("ngo_log")
    donation = donationew.objects.get(id=pid)
    donationarea = DonationArea.objects.all()
    volunteer = Volunteer.objects.all()
    # user = request.donation.id
    
    if request.method=="POST":
        donationareaid =request.POST['donationareaid']
        Volunteerid =request.POST['Volunteerid']
        # print('Id: ',donationareaid,Volunteerid)
        da= DonationArea.objects.get(id=donationareaid)
        va= Volunteer.objects.get(id=Volunteerid)
        donation, created = donationew.objects.get_or_create(id=pid)
        # donationew.objects.create(area=da.areaname,vol_member=va.user.username)
        donation.area=da.areaname
        donation.vol_member=str(va.user.username+' '+va.user.email)
        print('area: ',donation.area,'volunteer:',donation.vol_member)
        try:
            # print('namev: ',da,va,va.user.first_name,va.user.last_name,va.user.username)
            # print('area:',da.areaname)
            # donation.area = da
            # donation.vol_member = va  #Glich
            donation.donationarea = da
            donation.volunteer = va
            # print('file: ',donation.area,donation.vol_member,donation.donationarea,donation.volunteer)
            donation.status = "Volunteer Allocated"
            donation.updationdate=date.today()
            donation.save()
            # donationew.objects.create(area=donation.donationarea,vol_member=donation.volunteer)
            error="no"
            
        except:
            error="yes"
    return render(request,"accepted_donationdetail.html",locals())

def collection_reg(request):
    if not request.user.is_authenticated:
        return redirect("Volunteer_home")
    user = request.user
    volunteer = Volunteer.objects.filter(user=user)
    donation = donationew.objects.filter(status="Volunteer Allocated")#volunteer=volunteer
    return render(request,"collection_reg.html",locals())

def donationcollection_detail(request,pid):
    if not request.user.is_authenticated:
        return redirect("ngo_log")
    donation = donationew.objects.get(id=pid)
    # user = request.user.id
    # userpica = Donor.objects.get(user=user)
    donationarea = DonationArea.objects.all()
    volunteer = Volunteer.objects.all()#-----------------------------
    # file_url = userpica.userpic.url
    # file_area = userpica.areaname
    # da= DonationArea.objects.get(id=pid)
    # va= Volunteer.objects.get(id=Volunteerid)
    error=""
    if request.method=="POST":
        status =request.POST['status']
        volunte =request.POST['volunteerremark']
        donation, created = donationew.objects.get_or_create(id=pid)
        try:
            donation.volunteerreamrk=volunte
            donation.status = status
            donation.updationdate=date.today()
            donation.save()
            error="no"
        except:
            error="yes"
    return render(request,"donationcollection_detail.html",locals())

def donationrec_volunteer(request):
    if not request.user.is_authenticated:
        return redirect("Volunteer_home")
    user = request.user
    volunteer = Volunteer.objects.filter(user=user)
    #donation = Donation.objects.filter(status="Donation Received")#volunteer=volunteer,
    donation = donationew.objects.filter(status='Donation Received')#volunteer=volunteer,
    return render(request,"donationrec_volunteer.html",locals())

def donationrec_detail(request,pid):
    if not request.user.is_authenticated:
        return redirect("ngo_log")
    donation = donationew.objects.get(id=pid)
    
    error=""
    if request.method=="POST":
        status =request.POST['status']
        deliverypic =request.FILES['deliverypic']
        
        try:
            donation.status = status
            donation.deliverydate=date.today()
            donation.save()
            obj, created = donationew.objects.get_or_create(medicine=donation.medicine,updationdate=donation.updationdate)#deliverypic=deliverypic,deliverydate=donation.deliverydate)
            obj.deliverypic=deliverypic
            obj.save()
            # send_mail('MediTSA',status,'settings.EMAIL_HOST_USER',['rushiputthewad@gmail.com'],
            #       fail_silently=False)
            error="no"
        except:
            error="yes"
    return render(request,"donationrec_detail.html",locals())

def donationnotrec_volunteer(request):#Edit--------------------
    if not request.user.is_authenticated:
        return redirect("Volunteer_home")
    user = request.user
    volunteer = Volunteer.objects.filter(user=user)
    #donation = Donation.objects.filter(volunteer=volunteer,status="Donation Not Received")
    donation = donationew.objects.filter(status="Donation Not Received")
    return render(request,"donationnotrec_volunteer.html",locals())

def donationdelivered_volunteer(request):
    if not request.user.is_authenticated:
        return redirect("volunter_log")
    # user = request.user
    # volunteer = Volunteer.objects.get(user=user)
    # donation = Donation.objects.filter(volunteer=volunteer,status="Donation Delivered Successfully")
    # volunteer = Volunteer.objects.filter(user=user)
    donation = donationew.objects.filter(status="Donation Delivered Successfully")#-----------------Donoaion----------------------------
    return render(request,"donationdelivered_volunteer.html",locals())

def profile_volunteer(request):
    if not request.user.is_authenticated:
        return redirect("volunter_log")
    error= ""
    user = request.user
    #volunteer = Volunteer.objects.get(user=user)
    if request.method == "POST":
        fn = request.POST['first']
        ln = request.POST['last']
        em = request.POST['Eamil']
        con = request.POST['contact']
        pwd = request.POST['pwd']
        Cpwd = request.POST['cpwd']
        img = request.FILES['pic']
        idpic = request.FILES['idpic']
        addr = request.POST['address']
        aboutme = request.POST['aboutme']
        
        try:
            user= User.objects.create_user(first_name=fn,last_name=ln,username=em,password=pwd)
            Volunteer.objects.create(user=user,contact=con,userpic=img, idpic=idpic,address=addr,aboutme=aboutme,status="pending")
            error = "no"
            
        except:
            error = "yes"
            
    return render(request,"profile_volunteer.html",locals())

