# Django でテストを書く

## テストの実行方法

```
docker-compose run web python manage.py test
```

上記のテストを実行する為には startapp時に生成される tests.py を使うか、tests というパッケージを作り、その配下に test_xxx.py というモジュールを書く必要がある。

これらのモジュールにテストコードを書いておくと、上記のコマンドの実行時に自動テストが行われる。

```
django/sectionviewer/tests
├── __init__.py
├── test_department.py
├── test_filtercondition.py
└── test_store.py
```

python manage.py test を実行するとプロジェクト配下のテストがすべて実行されるが、以下のようにアプリケーションごとに実行することもできる。

```
docker-compose run web python manage.py test sectionviewer
```

他にも test コマンドの後ろに任意のラベルを与えることで、モジュール単位、クラス単位、メソッド単位で実行することもできる。


## DBの設定
DBに接続するテストを行う場合、test は test_appname というデータベースを作成し、そのデータベースを利用してテストを行う。
その為にデータベースには先述のデータベースを作成する為の権限が必要になる。
まずは既存の権限を確認する。
```
mysql> SHOW GRANTS FOR uriba_watch_user@'%' \g
+---------------------------------------------------------------------------+
| Grants for uriba_watch_user@%                                             |
+---------------------------------------------------------------------------+
| GRANT USAGE ON *.* TO 'uriba_watch_user'@'%'                              |
| GRANT ALL PRIVILEGES ON `uriba\_watch\_db`.* TO 'uriba_watch_user'@'%'    |
| GRANT ALL PRIVILEGES ON `test_uriba_watch_db`.* TO 'uriba_watch_user'@'%' |
+---------------------------------------------------------------------------+
4 rows in set (0.01 sec)
```

ここで該当のデータベースに対する権限がない場合は、以下のコマンドで権限を与える。

```
mysql> GRANT ALL PRIVILEGES ON test_uriba_watch_db.* TO 'uriba_watch_user'@'%';
```
また、fixture や マルチバイト文字を扱う為にDATABASESの設定にも修正を加える必要がある。
項目にTESTを追加し、その配下に CHARSET と COLLATION を追加する。

``` local_settings.py
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "",
        "USER": "",
        "PASSWORD": "",
        "HOST": "db",
        "PORT": "3306",
        "TEST": {
            "CHARSET": "utf8mb4",
            "COLLATION": "utf8mb4_general_ci",
        },
    }
}
```
