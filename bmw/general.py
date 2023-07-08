from .models import Indra, Category, Copyright

def global_data(request):
    data={
        'indraData':Indra.objects.all(),
        'categoryData':Category.objects.all(),
        'copyrightData':Copyright.objects.all()
    }
    return data