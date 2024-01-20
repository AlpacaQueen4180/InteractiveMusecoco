from django.shortcuts import render
from django.http import HttpResponse

import mimetypes
import os
import concurrent.futures

from . import musecoco

executor = concurrent.futures.ThreadPoolExecutor(1)

def print_input(request):
    user_input = ""
    
    if request.method == 'POST':
        user_input = request.POST.get('user_input', '')
        print(f"User typed: {user_input}")

    return user_input

def play_sample(request):
    # Assuming 'sample.mp3' is in the 'static/music/' folder
    audio_file_path = 'static/music/abc.mp3'
    return audio_file_path

def index(request):

    if request.method == 'POST':
        user_input = request.POST.get('user_input', '') 
        try:
            executor.submit(musecoco.generate, user_input)
        except:
            user_input = "An error occured"
    else:
        user_input = ''

    print(f"{user_input=}")
    # user_input = print_input(request)
    audio_file_path = play_sample(request)

    context = {'user_input': user_input, 'audio_file_path': audio_file_path}
    return render(request, 'index.html', context)

def download_midi(request):
    # Specify the file path on the server
    file_path = "/home/alpaca/musecoco_test/muzic/musecoco/2-attribute2music_model/generation/0505/linear_mask-1billion-attribute2music/infer_pipeline/topk15-t1.0-ngram0/0/midi/1.mid"

    # Open the file and create an HttpResponse object
    with open(file_path, "rb") as file:
        response = HttpResponse(
            file.read(), content_type=mimetypes.guess_type(file_path)[0]
        )
        # Set the Content-Disposition header to prompt the user for download
        response[
            "Content-Disposition"
        ] = f'attachment; filename="{os.path.basename(file_path)}"'
        return response