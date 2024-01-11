from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.db import IntegrityError
from assemblyai import AssemblyAIError
import assemblyai as aai


def index(request):

    return render(request , 'index.html')



def register(request):
    if request.method == "POST":
        fname = request.POST.get("fname")
        lname = request.POST.get("lname")
        email = request.POST.get("email")
        username = request.POST.get("username")
        password = request.POST.get("password")

        try:

            new_user = User.objects.create_user(username, email, password)
            # new_user = UserCreationForm(request.POST)
            new_user.first_name = fname
            new_user.last_name = lname

            new_user.save()
            return redirect("login")
            # Redirect or perform other actions for successful registration
        except IntegrityError:
            # Handle the case when a user with the same username already exists
            error_message = (
                "Username already exists. Please choose a different username."
            )
            return render(
                request,
                "register.html",
                {"error_message": error_message},
            )

    else:
        return render(
            request, "register.html"
        )  # Render the registration form for GET requests


def transcribe(request):

    if request.method == 'POST':

        uploaded_file = request.FILES.get('file')
        print(uploaded_file)
        result = {}

        if uploaded_file:
            print("file uploaded")
            # Save the file to the media directory
            with open(f'media/{uploaded_file.name}', 'wb') as destination:
                
                for chunk in uploaded_file.chunks():
                    
                    destination.write(chunk)

            try:
                print(uploaded_file.name)
                aai.settings.api_key = "c2321eb4b5c247ceaf452bf334e536a6"
                # Transcribe the saved file using AssemblyAI
                transcriber = aai.Transcriber()
                transcript = transcriber.transcribe(f"media/{uploaded_file.name}")
                
                context = {'message': 'File transcribed successfully', 'transcription': transcript.text}
                return JsonResponse({'message': 'File transcribed successfully', 'transcription': transcript.text})

            except AssemblyAIError as e:
                print("in catch")
                # Handle any exceptions that might occur during transcription
                context = {'error': f"Transcription error: {e}"}
        else:
            context = {'error': 'No file provided for transcription'}

        return JsonResponse({'message': context})
    
    else:
        return render(request, 'transcribe.html')
    