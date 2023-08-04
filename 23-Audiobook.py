import PyPDF2

pdfReader = PyPDF2.PdfFileReader(open('file.pdf', 'rb'))
import pyttsx3

speaker = pyttsx3.init()

for page_num in range(pdfReader.numPages):
    text = pdfReader.getPage(page_num).extractText()
    speaker.say(text)
    speaker.runAndWait()
speaker.stop()

pyttsx3.engine.save_to_file(text, 'audio.mp3')
pyttsx3.engine.runAndWait()
