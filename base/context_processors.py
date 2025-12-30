from base.models import category

def extract_category(request):
    return {'categories':category.objects.all()}