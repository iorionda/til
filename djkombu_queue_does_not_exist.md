# relation "djkombu_queue" does not exist

## Celeryの設定中に`djkombu_queue`が存在しないというエラーが発生した

```
[2017-12-12 15:21:58,334: ERROR/MainProcess] Unrecoverable error: ProgrammingError('relation "djkombu_queue" does not exist\nLINE 1: ..."djkombu_queue"."id", "djkombu_queue"."name" FROM "djkombu_q...\n                                                             ^\n',)
Traceback (most recent call last):
```

## 解決方法

settings.pyに以下を追加

```
INSTALLED_APPS = [
  ...
  'kombu.transport.django',
  ...
]
```

コンソールからsyncdbを実行する

```
% python manage.py migrate --run-syncdb
```
