from .models import Category
 
 
def common(request):
    context = {
        "categories": Category.objects.all(),
    }
    return context
