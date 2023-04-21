## Приветствую, Вас.
### Сдаю домашнее задание по теме Event loop. Asyncio.
### Задачу до конца решить не смог. 
### Дело в том, что последняя группа id-шников возвращаемая с помощью chanked не записывается в БД. 
### В процессе подготовки данных функцией paste_to_db() возникает  ошибка KeyError. 
### Как будто бы функция main() передала в paste_to_db() пустой результат. Но это не так, данные в списке есть. 

Task exception was never retrieved
future: <Task finished name='Task-51' coro=<paste_to_db() done, defined at C:\script\py_homework_web\py_homeworks_asyncio\swapi_async.py:24> exception=KeyError('films')>
Traceback (most recent call last):
  File "C:\script\py_homework_web\py_homeworks_asyncio\swapi_async.py", line 29, in paste_to_db
    films = ' '.join(element['films'])
KeyError: 'films'