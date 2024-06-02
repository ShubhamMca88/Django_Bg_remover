from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from PIL import Image
from rembg import remove
import io
import base64

def home(request):
    return render(request, 'main/home.html')

def about(request):
    return render(request, 'main/about.html')

def contact(request):
    return render(request, 'main/contact.html')

@csrf_exempt
def home(request):
    if request.method == 'POST':
        image_file = request.FILES['image']
        img = Image.open(image_file)
        output = remove(img)
        buffer = io.BytesIO()
        output.save(buffer, format="PNG")
        img_str = base64.b64encode(buffer.getvalue()).decode()
        return JsonResponse({'image': img_str})
    return render(request, 'main/home.html')