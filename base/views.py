from django.shortcuts import render,redirect
from .models import Image, MoodBoard
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import HttpResponse
from io import BytesIO
from PIL import ImageGrab

def logoutUser(request):
    logout(request)
    return redirect('landing')

def loginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        try:
            user=User.objects.get(username=username)
        except:
            print("error")

        user=authenticate(request,username=username,password=password)

        if user is not None:
            login(request,user)
            return redirect('home',user)
        else:
            print('Username or password invalid')
    return render(request,'base/login.html')

@login_required
def home(request,user):
    username=User.objects.get(username__icontains=user)
    boards=MoodBoard.objects.filter(user=username)
    context={'boards':boards,'user':username}
    return render(request,'base\home.html',context)

@login_required
def create(request,user,t):
    userid=User.objects.get(username__icontains=user)
    if request.method=='POST':
        name=request.POST.get("name")
        desc=request.POST.get("description")
        images=request.FILES.getlist('images')
        if t=='t1' and len(images)!=12:
            print("Error")
        mood_board=MoodBoard.objects.create(user=userid,name=name,description=desc)
        for image in images:
            im=Image.objects.create(user=userid,image=image,mood_board=mood_board)
        return redirect('main',user,mood_board,t)
    else:
        return render(request,'base\createform.html')
    
def upload(request,user,pk,t):
    userid=User.objects.get(username__icontains=user)
    moodboard=MoodBoard.objects.get(name__icontains=pk)
    image=Image.objects.filter(Q(user=userid)&Q(mood_board=moodboard)).order_by('?')
    context={'images':image,'moodboard':moodboard,'user':userid,'template':t}
    if t =='t1':
        return render(request,'base\emp1.html',context)
    elif t =='t2':
        return render(request,'base\emp2.html',context)
    elif t =='t3':
        return render(request,'base\emp3.html',context)
    else:
        return render(request,'base\main.html',context)

def shuffle(request,user,pk,t):
    userid=User.objects.get(username__icontains=user)
    moodboard=MoodBoard.objects.get(name__icontains=pk)
    return redirect('main',userid,moodboard,t)

def capture_region(request):

    # Capture a screenshot of the region using Pillow
    img = ImageGrab.grab(bbox=(10,230,1850,1000))

    # Save the image to a BytesIO buffer
    buffer = BytesIO()
    img.save(buffer, format='PNG')
    buffer.seek(0)

    # Create a HttpResponse object with the image data
    response = HttpResponse(buffer, content_type='image/png')
    response['Content-Disposition'] = 'attachment; filename="mood_board.png"'

    return response
