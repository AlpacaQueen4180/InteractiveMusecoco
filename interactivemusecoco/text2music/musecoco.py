import os
import subprocess

def generate(text_input):
    cwd = os.getcwd()
    os.chdir("/home/alpaca/musecoco_test/muzic/musecoco")
    subprocess.run(['python', 'pipeline.py', text_input])
    os.chdir(cwd)