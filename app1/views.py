from django.shortcuts import render

# Create your views here.
def index_page(request):
    return render(request, 'index.html')

def first_help_page(request):
    return render(request, 'Направления обучения/first_help.html')

def occupational_page(request):
    return render(request, 'Направления обучения/occupational_safety.html')

def professions_page(request):
    return render(request, 'Направления обучения/professions.html')

def teachers_page(request):
    return render(request, 'Направления обучения/teachers.html')

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
    return render(request, 'Педагогам/attestation.html')

def cabinet_page(request):
    return render(request, 'Педагогам/cabinet.html')

def application_page(request):
    return render(request, 'application/application.html')

def antiterrorist_page(request):
    return render(request, 'information/antiterrorist.html')

def independet_page(request):
    return render(request, 'information/independet.html')

def corruption_page(request):
    return render(request, 'information/corruption.html')

def photo_page(request):
    return render(request, 'Медиа/photo.html')

def video_page(request):
    return render(request, 'Медиа/video.html')

def quests_page(request):
    return render(request, 'Медиа/quests.html')

def main_info_page(request):
    return render(request, 'Сведения об образовательной организации/основные_сведения.html')

def structur_page(request):
    return render(request, 'Сведения об образовательной организации/Структура и органы управления образовательной организацией.html')

def document_page(request):
    return render(request, 'Сведения об образовательной организации/документы.html')

def education_page(request):
    return render(request, 'Сведения об образовательной организации/Образование.html')

def education_standart_page(request):
    return render(request, 'Сведения об образовательной организации/Образовательные стандарты.html')

def cast_page(request):
    return render(request, 'Сведения об образовательной организации/Руководство.html')

def security_page(request):
    return render(request, 'Сведения об образовательной организации/Материально-техническое обеспечение.html')

def scholarship_page(request):
    return render(request, 'Сведения об образовательной организации/Стипендии и меры поддержки обучающихся.html')

def paid_services_page(request):
    return render(request, 'Сведения об образовательной организации/Платные образовательные услуги.html')

def financially_page(request):
    return render(request, 'Сведения об образовательной организации/Финансово-хозяйственная деятельность.html')

def vacant_page(request):
    return render(request, 'Сведения об образовательной организации/Вакантные места для приема (перевода) обучающихся.html')

def accessible_page(request):
    return render(request, 'Сведения об образовательной организации/Доступные среды.html')

def organ_page(request):
    return render(request, 'Сведения об образовательной организации/Предписания органов, осуществляющих государственный контроль (надзор).html')

def cooperation_page(request):
    return render(request, 'Сведения об образовательной организации/Международное сотрудничество.html')

def distant_page(request):
    return render(request, 'Сведения об образовательной организации/Дистанционное обучение.html')

def map_page(request):
    return render(request, 'map.html')