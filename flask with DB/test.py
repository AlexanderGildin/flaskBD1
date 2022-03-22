from requests import get, post, delete, put

print(get('http://localhost:5000/api/news').json())
print(get('http://localhost:5000/api/news/1').json())
print(get('http://localhost:5000/api/news/999').json())
print(post('http://localhost:5000/api/news').json())

print(post('http://localhost:5000/api/news',
           json={'title': 'Заголовок'}).json())

print(post('http://localhost:5000/api/news',
           json={'title': 'Новость',
                 'content': 'ТОлько добавил',
                 'user_id': 2,
                 'is_private': False}).json())

print(post('http://localhost:5000/api/news',
           json={'title': 'Заголовок',
                 'content': 'Текст новости',
                 'user_id': 1,
                 'is_private': False}).json())

print(get('http://localhost:5000/api/news').json())
#print(delete('http://localhost:5000/api/news/999').json())
# новости с id = 999 нет в базе

#print(delete('http://localhost:5000/api/news/1').json())

print(put('http://localhost:5000/api/news/6',
           json={'title': 'Измененный заголовок',
                 'content': 'Исправленная новость'}).json())

print(get('http://localhost:5000/api/news').json())