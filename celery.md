# Celery 3.1をDjangoで使う

CeleryはPythonで非同期処理をするためのTask Queue.
Celery 3.0 までは　Django で使う場合ひはdjango-celeryを使っていた。
Celery 3.1 からはdjango-celeryを使うべきではないとなった。

## 前準備
### celeryをインストールする
```
pip install celery
```

### Brokerを用意する

CeleryでstableあBrokerとしているのはRabbitMQとRedis.
Redisを使うとして、インストールしておく。
```
brew install redis
```

それだけではエラーが発生したので、pipでもインストールしておく。
```
ImportError: Missing redis library (pip install redis)

pip install redis
```

## 必要事項を設定する

以下、app という名前でアプリケーションを用意している前提で書く。

### settings.py

```
BROKER_URL = 'redis://localhost'
CELERY_RESULT_BACKEND = 'redis'
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_ACCEPT_CONTENT = ['json']
```

## celery.py

```
from __future__ import absolute_import

import os

from celery import Celery

from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

app = Celery('core')

app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
```

## tasks.py
```
from __future__ import absolute_import
from celery import shared_task
from celery.utils.log import get_task_logger


@shared_task
def test_celery(x, y):
    logger = get_task_logger(__name__)

    logger.info('func start ------------------->')
    logger.info('application: {0}'.format(__name__))
    logger.info('func end --------------------->')
    return x + y

```

## views.py
```
from django.shortcuts import render, HttpResponse
from .tasks import test_celery


def hello(request):
    result = test_celery.delay(3, 8)
    while not result.ready():
        print('spam')
    print(result.get())
    return HttpResponse(result.get())

```

## 動作確認する

```
$ python manage.py runserver  # サーバーを起動する
$ celery -A app worker -l info  # celery プロセスを起動する
```

## 公式ドキュメント
http://celery.readthedocs.io/en/latest/index.html
