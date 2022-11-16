from django.shortcuts import render, HttpResponse

recipes = [
  {
    'author': 'Henry',
    'title': 'Meatballs',
    'content': 'Combine ingredients, form into balls, brown, then place in oven.',
    'date_posted': 'Nov 15th, 2022'
  },
  {
    'author': 'Henry',
    'title': 'Chicken Cutlets',
    'content': 'Bread chicken, cook on each side for 8 min',
    'date_posted': 'Nov 10th, 2022'
  },
  {
    'author': 'Henry',
    'title': 'Sub',
    'content': 'Combine ingredients.',
    'date_posted': 'Nov 13th, 2022'
  }
]


# Create your views here.
def home(request):
    context = {
    'recipes': recipes
  }
    return render(request, "recipes/home.html", context)
    


def about(request):
    return HttpResponse ("<h1>This about my recipe app!</h1>")
