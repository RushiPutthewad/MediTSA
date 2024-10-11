"""
URL configuration for MediTSA project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from MediTSA import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.homePage, name="home_page"),
    path("cards_3/", views.cards, name="cards_3"),
    path("", views.send_mail, name="send_mail"),
    path("login_user/", views.login_user, name="login_user"),
    path("Volunteer/", views.volunter_log, name="volunter_log"),
    path("NGOs_login/", views.ngo_login, name="ngo_log"),
    path("Donor_Regitration/", views.donor_regiration, name="donor_regi"),
    path("navigation/", views.navidation_bar, name="nav_bar"),
    path("Donor_home/", views.donor_home, name="donor_hom"),
    path("Volunteer_home/", views.Volunteer_home, name="Volunteer_home"),#voulunteer home
    path("Logout/", views.Logout, name="logout"),
    path("add_services/", views.add_services, name="add_service"),
    path("donate_now/", views.donate_now, name="donate_now"),
    path("donor_history/", views.donation_history, name="donation_history"),
    #admin
    path("ngo_home/", views.ngo_home, name="ngo_home"),
    path("NGO_reg/", views.ngo_reg, name="ngo_reg"),
    path("pending_donation/", views.pending_donation, name="pending_donation"),
    path("view_donation_detail/<int:pid>/", views.view_donation, name="view_donation"),
    path("accepted_donation/", views.accepted_donation, name="accepted_donation"),
    path("demo_donoy_base/", views.demo_donoy_base, name="demo_donoy_base"),
    path("add_area/", views.add_area, name="add_area"),
    path("manage_area/", views.manage_area, name="manage_area"),
    path("edit_area/<int:pid>/", views.edit_area, name="edit_area"),
    path("delete_area/<int:pid>/", views.delete_area, name="delete_area"),
    path("manage_donor/", views.manage_donor, name="manage_donor"),
    path("view_donordetail/<int:pid>/", views.view_donordetail, name="view_donordetail"),
    path("delete_donor/<int:pid>/", views.delete_donor, name="delete_donor"),
    #Volunteer
    path("Volunteer_reg/", views.Volunteer_reg, name="Volunteer_reg"),
    path("new_volunteer/", views.new_volunteer, name="new_volunteer"),
    path("view_volunteerdetail/<int:pid>/", views.view_volunteerdetail, name="view_volunteerdetail"),
    path("accepted_volunteer/", views.accepted_volunteer, name="accepted_volunteer"),
    path("rejected_volunteer/", views.rejected_volunteer, name="rejected_volunteer"),
    path("all_volunteer/", views.all_volunteer, name="all_volunteer"),
    path("delete_volunteer/<int:pid>/", views.delete_volunteer, name="delete_volunteer"),
    path("accepted_donationdetail/<int:pid>/", views.accepted_donationdetail, name="accepted_donationdetail"),
    path("collection_reg/", views.collection_reg, name="collection_reg"),
    path("donationcollection_detail/<int:pid>/", views.donationcollection_detail, name="donationcollection_detail"),
    path("donationrec_volunteer/", views.donationrec_volunteer, name="donationrec_volunteer"),
    path("donationrec_detail/<int:pid>/", views.donationrec_detail, name="donationrec_detail"),
    path("donationnotrec_volunteer/", views.donationnotrec_volunteer, name="donationnotrec_volunteer"),
    path("donationdelivered_volunteer/", views.donationdelivered_volunteer, name="donationdelivered_volunteer"),
    path("profile_volunteer/", views.profile_volunteer, name="profile_volunteer"),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
