from django.shortcuts import render

from lembretes.models import Lembretes

def pagina_inicial(request):
    lembretes = Lembretes.objects.all()
    context = {'lembretes' : lembretes}
    return render(request, "lembretes/pagina_inicial.html", context)