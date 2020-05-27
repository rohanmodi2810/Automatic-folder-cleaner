import os

def create_dir(name):
    if os.path.exists(name) == False:
        os.makedirs(name)

files = os.listdir()
files.remove('main.py')
# print(files)

create_dir('docs')
create_dir('audio')
create_dir('video')
create_dir('images')
create_dir('others')

docs_ext = ['.txt', '.pdf', '.docx', '.pptx', '.xlsx']
audio_ext = ['.m4a', '.mp3']
video_ext = ['.mov', '.mp4']
image_ext = ['.png', '.jpg', '.jpeg']

docs = []
audio = []
video = []
images = []
others = []

for file in files:
    if os.path.splitext(file)[1].lower() in docs_ext:
        docs.append(file)
    elif os.path.splitext(file)[1].lower() in audio_ext:
        audio.append(file)
    elif os.path.splitext(file)[1].lower() in video_ext:
        video.append(file)
    elif os.path.splitext(file)[1].lower() in image_ext:
        images.append(file)
    elif os.path.isfile(file):
        others.append(file)

# print(docs)
# print(audio)
# print(video)
# print(images)
# print(others)

for doc in docs:
    os.rename(doc, f"docs/{doc}")

for aud in audio:
    os.rename(aud, f"audio/{aud}")

for vid in video:
    os.rename(vid, f"video/{vid}")

for img in images:
    os.rename(img, f"images/{img}")

for oth in others:
    os.rename(oth, f"others/{oth}")






