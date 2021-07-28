from django.shortcuts import render

# Create your views here.
def welcome(request):
    message="hello siva good evening"
    employees=[{"name":"siva","age":28,"sal":3000},
         {"name":"rama","age":29,"sal":2000},
         {"name":"krishna","age":30,"sal":4000}
         ]
    num=12
    words="hello madam python is a high level language".split()
    return render(request,'sample.html',
                  {'msg':message,'emp':employees,'number':num,
                   'words':words})

