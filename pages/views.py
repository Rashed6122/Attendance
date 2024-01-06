import os
from datetime import date
from django.http import HttpResponse
from .forms import ImageUploadForm ,ExportAttendanceForm
from .cv_codes.predict import recognize_faces
from django.shortcuts import render
import csv

def home(request):
    if request.method == "POST":
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_image = form.cleaned_data["image"]

            # Create a folder based on the current date
            today_folder = date.today().strftime("%Y-%m-%d")
            media_folder = "media"
            upload_folder_path = os.path.join(media_folder, today_folder)

            # Ensure the folder exists
            os.makedirs(upload_folder_path, exist_ok=True)

            # Save the uploaded image to the folder
            uploaded_image_path = os.path.join(upload_folder_path, uploaded_image.name)
            with open(uploaded_image_path, "wb") as destination:
                for chunk in uploaded_image.chunks():
                    destination.write(chunk)
            # Call your face recognition script with the image path
            output = recognize_faces(uploaded_image_path)
       
            return render(
                request,
                "pages/studentLst.html",
                {
                    "output": output,
                },
            )
    else:
        form = ImageUploadForm()

    return render(request, 'pages/home.html', {"form": form})



def course(request):
    return render(request, 'pages/course.html', {})

def download_csv(request):
    if request.method == "POST":
        # Assuming your CSV file is named "Attendance.csv" and is located in the same directory as views.py
        script_dir = os.path.dirname(os.path.abspath(__file__))
        csv_file_path = os.path.join(script_dir, "cv_codes/Attendance.csv")
        
        # Create the HttpResponse object with the appropriate CSV header.
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = f'attachment; filename="{os.path.basename(csv_file_path)}"'

        # Write the CSV file to the response.
        with open(csv_file_path, 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            for row in csv_reader:
                response.write(','.join(row) + '\n')

        return response
    else:
        form = ExportAttendanceForm()
        return render(
            request, "attendance/export_attendance.html", {"export_form": form}
        )