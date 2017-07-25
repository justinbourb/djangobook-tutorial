from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template.loader import get_template
from django.shortcuts import render
import datetime
from mysite.forms import ContactForm
from django.core.mail import send_mail, get_connection

def hello(request):
    #url /hello
    return render(request, 'hello.html')

def my_homepage_view(request):
    #url 127.0.0.1:8000
    return render(request, 'homepage.html')

def current_datetime(request):
    #url /time
    #finds the time
    now = datetime.datetime.now()
    #uses parent template base.html and replaces content from child template current_datetimes.html
    return render(request, 'current_datetime.html', {'current_date': now})

def hours_ahead(request, offset):
    '''url /time/plus/##'''
    try:
        #checks if ## hour offset entered in url is an int or not
        offset = int(offset)
    except ValueError:
        raise Http404()
    #calculates the what the time will be in offset hours
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    #uses parent template base.html and replaces content from child template hours_ahead.html
    return render(request, 'hours_ahead.html', {'hour_offset': offset, 'next_time': dt})

def histowiz(request):
    #url /histowiz
    return render(request, 'histowiz.html')

def display_meta(request):
    '''in python 3.x request.meta.items() returns dict_items not dictionary,
    so it needs to be turned into a dictionary'''
    values = dict(request.META.items())
    html = []
    for k in sorted(values):
        html.append('<tr><td>%s</td><td>%s</td></tr>' % (k, values[k]))
    return HttpResponse('<table>%s</table>' % '\n'.join(html))

def contact(request):
    '''check to see if form is submitted with POST method else display blank
    form'''
    '''check that form contains valid data and sends email,
    redirects to contact/thanks/ page'''
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            con = get_connection('django.core.mail.backends.console.EmailBackend')
            send_mail(
                cd['subject'],
                cd['message'],
                cd.get('email', 'noreply@example.com'),
                ['siteowner@example.com'],
                connection=con
            )
            return HttpResponseRedirect('/contact/thanks/')
    else:
        form = ContactForm(
            initial={'subject': 'I love your site!'}
            )

    return render(request, 'contact_form.html', {'form': form})
            
