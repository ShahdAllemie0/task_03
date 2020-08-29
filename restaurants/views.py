from django.shortcuts import render

def welcome(request):
    return render(request, 'index.html', {'msg':'Hello World!'})

def restaurant_list(request):

    context = {
    "my_list":[
       {"restaurant_name" :"Piatto" ,"food_type":"Italian"},
       {"restaurant_name" :"Benihana" , "food_type":"Japanese" },
       {"restaurant_name" : "Nozomi", "food_type":"Japanese"}
       ]}
    return render(request, 'list.html', context)


def restaurant_detail(request):

    context = {
    "my_object":{"restaurant_name" :"Piatto" ,"food_type":"Italian"}

    }
    return render(request, 'detail.html', context)
