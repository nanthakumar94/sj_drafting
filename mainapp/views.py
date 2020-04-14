from django.http import JsonResponse
from django.core import serializers
from django.shortcuts import render, redirect
from mainapp.forms import ContactForm
# Create your views here.
from django.core.mail import EmailMessage
from django.template.loader import get_template
from django.contrib import messages


def index(request):
    context = {"home_page": "active"}
    return render(request, 'index.html', context)


def build_services(request):
    return render(request, 'services/build_constrction_services.html')


def family_services(request):
    return render(request, 'services/family-modeling_services.html')


def autocad_services(request):
    return render(request, 'services/autocad-drafting_services.html')


def solidworks(request):
    return render(request, 'services/solidworks-modeling_services.html')


def bim_services(request):
    return render(request, 'revit-building-construction-and-family-modeling_services.html')


def contact_us(request):

    return render(request, 'contact_us/contact_us.html')


def about_us(request):
    return render(request, 'about_us.html')


def microstation(request):
    return render(request, 'microstation.html')


def creo(request):
    return render(request, 'creo_modeling_services.html')


def inventor(request):
    return render(request, 'inventor_modeling_services.html')


def tekla(request):
    return render(request, 'tekla_services.html')


def request_for_quote(request):
    return render(request, 'request_for_quote.html')


def emailView(request):
    form_class = ContactForm

    # new logic!
    if request.is_ajax and request.method == 'POST':
        form = form_class(data=request.POST)

        if form.is_valid():
            first_name = request.POST.get('first_name', '')
            last_name = request.POST.get('last_name', '')
            company_name = request.POST.get('company_name', '')
            email = request.POST.get('email', '')
            phone = request.POST.get('phone', '')
            project = request.POST.get(
                'project'
                , '')

            # Email the profile with the
            # contact information
            template = get_template('contact_template.txt')
        context = {
            'first_name': first_name,
            'last_name': last_name,
            'company_name': company_name,
            'email': email,
            'phone': phone,
            'project': project,
        }
        content = template.render(context)

        email = EmailMessage(
            "New contact form submission",
            content,
            "Your website" + '',
            ['nantha.k1994@gmail.com'],
            headers={'Reply-To': email}
        )
        res = email.send()
        if res == 1:
            messages.success(request, "Your email send successfully")
        return redirect('index')

    return render(request, 'index.html', {'form': form_class})

