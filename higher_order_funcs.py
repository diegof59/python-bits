# higher_order_funcs.py

DATA = [
  {
    'name': 'Diego',
    'age': 25,
    'org': 'Univalle',
    'position': 'Student',
    'language': 'python'
  },
  {
    'name': 'Sebastian',
    'age': 25,
    'org': 'Holberton',
    'position': 'Student',
    'language': 'java'
  },
  {
    'name': 'Johan',
    'age': 28,
    'org': 'Univalle',
    'position': 'Student',
    'language': 'javascript'
  },
  {
    'name': 'Luisana',
    'age': 33,
    'organization': 'Globant',
    'position': 'UX Designer',
    'language': 'javascript',
  },
  {
    'name': 'Héctor',
    'age': 19,
    'organization': 'Platzi',
    'position': 'Associate',
    'language': 'ruby',
  },
  {
    'name': 'Gabriel',
    'age': 20,
    'organization': 'Platzi',
    'position': 'Associate',
    'language': 'javascript',
  },
  {
    'name': 'Isabella',
    'age': 30,
    'organization': 'Platzi',
    'position': 'QA Manager',
    'language': 'java',
  },
  {
    'name': 'Karo',
    'age': 23,
    'organization': 'Everis',
    'position': 'Backend Developer',
    'language': 'python',
  },
  {
    'name': 'Ariel',
    'age': 32,
    'organization': 'Rappi',
    'position': 'Support',
    'language': '',
  },
  {
    'name': 'Juan',
    'age': 17,
    'organization': '',
    'position': 'Student',
    'language': 'go',
  },
  {
    'name': 'Pablo',
    'age': 32,
    'organization': 'Master',
    'position': 'Human Resources Manager',
    'language': 'python',
  },
  {
    'name': 'Lorena',
    'age': 56,
    'organization': 'Python Organization',
    'position': 'Language Maker',
    'language': 'python',
  }
]

from functools import reduce

adults = filter(lambda worker: worker['age'] > 18, DATA)
python_programmers = filter(lambda worker: worker['language'] == 'python', DATA)
python_programmers = map(lambda worker: worker['name'], python_programmers)

is_old = list(map(lambda worker: {**worker, "old": worker['age'] > 70}, DATA))

ages_sum = reduce(
  lambda prev_worker_age, worker: prev_worker_age + worker['age'],
  DATA,
  0
)

age_avg = ages_sum / len(DATA)