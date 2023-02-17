"""djangoProject_UCPK URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import include

from django.conf import settings
from django.conf.urls.static import static

import app1.views
from app1.views import index_page, second_page, first_help_page, occupational_page, teachers_page, professions_page,\
    forthypointforty_page, news_page, news_new_site_obr_page, medic_and_student_page, greep_page, hygienic_page, \
    prevention_page, virus_page, contacts_main_page, faq_page, appeals_page, comments_page, deal_page, cabinet_page,\
    attestation_page, application_page, independet_page, antiterrorist_page, corruption_page, photo_page, video_page, \
    quests_page, main_info_page, structur_page, document_page, education_page, education_standart_page, cast_page, \
    security_page, scholarship_page, paid_services_page, financially_page, vacant_page, accessible_page, organ_page,\
    cooperation_page, distant_page, map_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index_page),
    path('second/', second_page),
    path('first_help/', first_help_page),
    path('occupational_safety/', occupational_page),
    path('teachers/', teachers_page),
    path('professions/', professions_page),
    path('404/', forthypointforty_page),
    path('news/', news_page),
    path('news/news_new_site_obr/', news_new_site_obr_page),
    path('news/medic_and_student/', medic_and_student_page),
    path('news/greep/', greep_page),
    path('news/hygienic/', hygienic_page),
    path('news/prevention/', prevention_page),
    path('news/virus/', virus_page),
    path('contacts/', contacts_main_page),
    path('contacts/faq/', faq_page),
    path('contacts/appeals/', appeals_page),
    path('contacts/comments/', comments_page),
    path('contacts/appeals/deal', deal_page),
    path('attestation/', attestation_page),
    path('cabinet/', cabinet_page),
    path('application/', application_page),
    path('independet/', independet_page),
    path('antiterrorist/', antiterrorist_page),
    path('corruption/', corruption_page),
    path('photo/', photo_page),
    path('video/', video_page),
    path('quests/', quests_page),
    path('main_info/', main_info_page),
    path('structur/', structur_page),
    path('document/', document_page),
    path('education/', education_page),
    path('education_standart/', education_standart_page),
    path('cast/', cast_page),
    path('security/', security_page),
    path('scholarship/', scholarship_page),
    path('paid_services/', paid_services_page),
    path('financially/', financially_page),
    path('vacant/', vacant_page),
    path('accessible/', accessible_page),
    path('organ/', organ_page),
    path('cooperation/', cooperation_page),
    path('distant/', distant_page),
    path('map/', map_page),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)