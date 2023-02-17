from django.shortcuts import render

# Create your views here.
def index_page(request):
    return render(request, 'index.html')

def first_help_page(request):
    return render(request, 'direction_study/first_help.html')

def occupational_page(request):
    return render(request, 'direction_study/occupational_safety.html')

def professions_page(request):
    return render(request, 'direction_study/professions.html')

def teachers_page(request):
    return render(request, 'direction_study/teachers.html')

def second_page(request):
    return render(request, 'second.html')

def forthypointforty_page(request):
    return render(request, '404.html')

def news_page(request):
    return render(request, 'news/news_main.html')

def news_new_site_obr_page(request):
    return render(request, 'news/news_new_site_obr.html')

def medic_and_student_page(request):
    return render(request, 'news/medic_and_student.html')

def greep_page(request):
    return render(request, 'news/greep.html')

def hygienic_page(request):
    return render(request, 'news/hygienic.html')

def prevention_page(request):
    return render(request, 'news/prevention.html')

def virus_page(request):
    return render(request, 'news/virus.html')

def contacts_main_page(request):
    return render(request, 'contacts/main_contacts.html')

def faq_page(request):
    return render(request, 'contacts/faq.html')

def appeals_page(request):
    return render(request, 'contacts/appeals.html')

def comments_page(request):
    return render(request, 'contacts/comments.html')

def deal_page(request):
    return render(request, 'contacts/deal.html')

def attestation_page(request):
    return render(request, 'teachers_page/attestation.html')

def cabinet_page(request):
    return render(request, 'teachers_page/cabinet.html')

def application_page(request):
    return render(request, 'application/application.html')

def antiterrorist_page(request):
    return render(request, 'information/antiterrorist.html')

def independet_page(request):
    return render(request, 'information/independet.html')

def corruption_page(request):
    return render(request, 'information/corruption.html')

def photo_page(request):
    return render(request, 'media_pages/photo.html')

def video_page(request):
    return render(request, 'media_pages/video.html')

def quests_page(request):
    return render(request, 'media_pages/quests.html')

def main_info_page(request):
    return render(request, 'information_base/main_information.html')

def structur_page(request):
    return render(request, 'information_base/structur.html')

def document_page(request):
    return render(request, 'information_base/documents.html')

def education_page(request):
    return render(request, 'information_base/education.html')

def education_standart_page(request):
    return render(request, 'information_base/standart_education.html')

def cast_page(request):
    return render(request, 'information_base/management.html')

def security_page(request):
    return render(request, 'information_base/techical-obespejenia.html')

def scholarship_page(request):
    return render(request, 'information_base/stipend.html')

def paid_services_page(request):
    return render(request, 'information_base/education_uslugi.html')

def financially_page(request):
    return render(request, 'information_base/economic.html')

def vacant_page(request):
    return render(request, 'information_base/vacancies.html')

def accessible_page(request):
    return render(request, 'information_base/available_sredi.html')

def organ_page(request):
    return render(request,
                  'information_base/control.html')

def cooperation_page(request):
    return render(request, 'information_base/collab.html')

def distant_page(request):
    return render(request, 'information_base/distant.html')

def map_page(request):
    return render(request, 'map.html')