from .models import Tag

def tags(request):
  return {'tags': Tag.objects.all()}