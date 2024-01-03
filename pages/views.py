from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import requests
import base64
import cv2
import numpy as np
from PIL import Image
from io import BytesIO

from django.http import HttpResponse
from django.shortcuts import redirect
from .forms import ImageForm
# import numpy as np
# import face_recognition
import os
# from datetime import datetime
# import pickle
def home(request):
    return render(request, 'pages/home.html', {})
def course(request):
    return render(request, 'pages/course.html', {})
#@csrf_exempt
#def studentLst(request):
    
def image_view(request):
 
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
 
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = ImageForm()  
    return render(request, 'hotel_image_form.html', {'form': form})
 
 
def success(request):
    return HttpResponse('successfully uploaded')