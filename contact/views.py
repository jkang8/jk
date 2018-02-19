from django.shortcuts import render
from contact.models import FormPage


# Create your views here.
def contact(request):
    page = FormPage.objects.get(slug='contact')
    return render(request, 'contact/form_page.html', {
        'page': page
        # 'search_query': search_query,
        # 'search_results': search_results,
    })
