from django.shortcuts import render

# Create your views here.
def base_action(request) :
    context = {}
    if request.method == 'GET' :
        return render(request, 'blog/page.html', context)
