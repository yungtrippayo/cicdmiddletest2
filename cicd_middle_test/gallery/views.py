from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from datetime import timedelta
from .models import models

def gallery_view(request):
    one_month_ago = timezone.now() - timedelta(days=30)
    recent_images = models.objects.filter(created_at__gte=one_month_ago)
    return render(request, 'gallery.html', {'images': recent_images})

def image_detail(request, id):
    image = get_object_or_404(models, id=id)
    return render(request, 'image_detail.html', {'image': image})

