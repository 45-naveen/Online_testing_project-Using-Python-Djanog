from django.shortcuts import render
from django.http import HttpResponse;
from django.template import loader
def testpaper(request):
    que = "Who Developed Python Language ?"
    a="Dennis Ritchie"
    b="Ken Thompson"
    c="Guido Van Rossum"
    d="Bjarne Stroustrup"
    context = {
        'que':que,
        'options':[a,b,c,d]
    }
    template = loader.get_template('testpaper.html')
    res=template.render(context,request)
    return HttpResponse(res)


def examresult(request):
    s="<h1>This is result of BCA</h1>"
    return HttpResponse(s)


