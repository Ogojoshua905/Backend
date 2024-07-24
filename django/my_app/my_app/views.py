from django.http import HttpResponse


def home(request):
    return HttpResponse("<body style='background-color: black; color: white;'><h1 style='color: red; text-align: center; padding: 15px 32px; text-decoration: underline;'>My Data to You</h1><br><h2>Name: <span style='color: red;'>Byte</span><span style='color: purple;'>Prowler</span></h2><br> <h2>Occupation: <span style='color:pink;'>Code Bomber</span></h2></body>") 