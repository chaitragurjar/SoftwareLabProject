from django.shortcuts import render,redirect
import os
import subprocess
from .form import ImageForm
from .models import Image

# Create your views here.
def index(request):
    if request.method == "POST":
        form=ImageForm(data=request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
            obj=form.instance
            filename=obj.Upload_File.name
            filepath=obj.Upload_File.path
            #print("spleeter separate -o output/ "+filepath)
            #print("filename="+obj.Upload_File.name)
            status = 1
            status = os.system('spleeter separate -o media/output/ '+filepath)
            #print("/output/"+filename+"/vocals.wav")
            obj.Upload_File.name=filename.split('.')[0]
            return render(request,"index.html",{"obj":obj})
    else:
        form=ImageForm()
    img=Image.objects.all()
    
    return render(request,"index.html",{"img":img,"form":form})