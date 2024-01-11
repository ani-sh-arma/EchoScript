from django.conf import settings
aai = settings.KEY

aai.settings.api_key = "c2321eb4b5c247ceaf452bf334e536a6"

transcriber = aai.Transcriber()

# transcript = transcriber.transcribe("D:/Educational/personal/Django/EchoScript/static/assemblyAItest.mp3")
transcript = transcriber.transcribe("media/assemblyAItest.mp3")

print(transcript.text)