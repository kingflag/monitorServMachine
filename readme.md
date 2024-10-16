## config DB
```python
DATABASES = {
    'default':
    {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'table',
        'HOST': 'ip',
        'PORT': 3306,
        'USER': 'username',
        'PASSWORD': 'pwd',
    }
}
```

## add models



```bash
py manage.py makemigrations backend
```
the response in bash (id don't have this response,pls remove dir`[__pycache__]`)
```
Migrations for 'backend':
  backend\migrations\0001_initial.py
    - Create model Machine
```

```bash
py manage.py migrate
```