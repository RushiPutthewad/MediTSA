from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.
class Donor(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    contact = models.CharField(max_length=15,null=True)
    address = models.CharField(max_length=300,null=True)
    userpic = models.FileField(null=True)
    regdate = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.user.username

class Volunteer(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    contact = models.CharField(max_length=15,null=True)
    address = models.CharField(max_length=300,null=True)
    userpic = models.FileField(null=True) 
    idpic = models.FileField(null=True)
    aboutme = models.CharField(max_length=300,null=True)
    status = models.CharField(max_length=20,null=True)
    regdate = models.DateTimeField(auto_now_add=True)
    adminremark = models.CharField(max_length=300,null=True)
    updationdate = models.DateField(null=True)
    def __str__(self):
        return self.user.username

class Ngo(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    ngo_name=models.CharField(max_length=150,null=True)
    ngo_id=models.CharField(max_length=20,null=True)#Reg.date #last-front
    reg_no=models.CharField(max_length=20,null=True)
    reg_contact=models.CharField(max_length=15,null=True)
    reg_logo=models.FileField(null=True)
    reg_proof=models.FileField(null=True)
    address=models.CharField(max_length=300,null=True)
    city=models.CharField(max_length=20,null=True)
    state=models.CharField(max_length=20,null=True)
    about_self=models.CharField(max_length=400,null=True)
    def __str__(self):
        return self.user.username
    

# for volunteer area adrress to delivery
class DonationArea(models.Model):
    areaname = models.CharField(max_length=100,null=True)
    description = models.CharField(max_length=300,null=True)
    creationdate = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.areaname
    
class donationew(models.Model):
    # name,last,contact,email,donor pic
    
    medicine = models.CharField(max_length=100,default='now')
    tablet_con=models.CharField(max_length=6)
    medi_type=models.CharField(max_length=13,default='Syrub')
    pur_date=models.DateField(null=True)
    ex_date=models.DateField(null=True)
    discrib = models.TextField()
    medicinepic = models.FileField(null=True)
    collectionloc = models.CharField(max_length=300,null=True)
    status = models.CharField(max_length=50,null=True,default="Pending")
    adminremark = models.CharField(max_length=300,null=True)
    volunteerreamrk = models.CharField(max_length=300,null=True)
    donationdate = models.DateTimeField(auto_now_add=True)
    updationdate = models.DateField(null=True)
    name=models.CharField(max_length=20)
    last=models.CharField(max_length=20)
    contact=models.CharField(max_length=15)
    email=models.CharField(max_length=60)
    donorpic=models.FileField(null=True)
    area=models.CharField(max_length=100,null=True)
    vol_member=models.CharField(max_length=60) #----------
    deliverypic = models.FileField(null=True)
    deliverydate = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.medicine
    class Meta:
        db_table = "donationew"
    
# class Donation(models.Model):
#     medicinename = models.CharField(max_length=100,null=True)
#     donationpic = models.FileField(null=True)
#     collectionloc = models.CharField(max_length=300,null=True)
#     description = models.TextField()
#     status = models.CharField(max_length=50,null=True,default="Pending")
#     donationdate = models.DateTimeField(auto_now_add=True)            
#     adminremark = models.CharField(max_length=300,null=True)
#     volunteerreamrk = models.CharField(max_length=300,null=True)
#     updationdate = models.DateField(null=True)
#     donor = models.ForeignKey(Donor,on_delete=models.CASCADE)
#     volunteer = models.ForeignKey(Volunteer,on_delete=models.CASCADE)
#     donationarea = models.ForeignKey(DonationArea,on_delete=models.CASCADE)
#     donationew = models.ForeignKey(donationew,on_delete=models.CASCADE)

#     def __str__(self):
#         return self.medicinename
#     class Meta:
#         db_table="donation"

# confirmation of delivery of medicine by volunteers proof pic image/ self of delivery
class Gallery(models.Model):
    donation_g = models.ForeignKey(donationew,on_delete=models.CASCADE)
    deliverypic = models.FileField(null=True)
    creationdate = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.donation_g.medicine
# @receiver(post_save,sender=donationew)
# def create_or_update_Donation(sender,instance,created,**kwargs):
#     if created:
#         Donation.objects.update_or_create(medicinename=sender.medicine,donationpic=sender.medicinepic)#,defaults={'medicinename':instance.medicine,'donationpic':instance.medicinepic})