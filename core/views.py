from django.shortcuts import render

from googletrans import Translator



def translate(request):
    if request.method == "POST":
        lang = request.POST.get("lang", None)
        txt = request.POST.get("txt", None)
        translator = Translator()
        tr = translator.translate(txt, dest=lang)
        context={
         "result":tr.text
        }
        return render(request, 'index.html',context)

    return render(request, 'index.html')