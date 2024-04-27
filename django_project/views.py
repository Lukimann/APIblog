from django.shortcuts import render
import requests


def index(request):
  r1 = requests.get('https://uselessfacts.jsph.pl/random.json?language=en')
  res1 = r1.json()
  fact = res1['text']

  r2 = requests.get('https://api.adviceslip.com/advice')
  res2 = r2.json()
  advice = res2['slip']

  r3 = requests.get('https://dog.ceo/api/breeds/image/random')
  res3 = r3.json()
  dog = res3['message']

  if request.method == 'POST':
    photo = request.POST['photo']
  else:
    photo = None

  return render(request, 'templates/index.html', {
      'fact': fact,
      'slip': advice,
      'dog': dog,
      'photo': photo
  })
