# MacでのPostgreSQLの準備

## initdb する

```
%  initdb /usr/local/var/postgres -E utf8 --locale=C

The files belonging to this database system will be owned by user "iorionda".
This user must also own the server process.

The database cluster will be initialized with locale "C".
The default text search configuration will be set to "english".

Data page checksums are disabled.

# エラー出た
initdb: directory "/usr/local/var/postgres" exists but is not empty
If you want to create a new database system, either remove or empty
the directory "/usr/local/var/postgres" or run initdb
with an argument other than "/usr/local/var/postgres".
```

## エラーが出たのでディレクトリを確認する

```
% ls -al /usr/local/var/

total 0
drwxr-xr-x  12 iorionda  admin  408 12  1 14:24 .
drwxr-xr-x  17 root      wheel  578  2 22  2017 ..
drwxr-xr-x   3 iorionda  admin  102  8  9  2016 cache
drwxr-xr-x   3 iorionda  admin  102  8  9  2016 db
drwxr-xr-x   4 iorionda  admin  136 10  9  2016 homebrew
drwxr-xr-x   3 iorionda  admin  102  8 28 15:40 lib
drwxr-xr-x   5 iorionda  admin  170 12  1 14:25 log
drwxr-xr-x  25 iorionda  admin  850  9 21 17:29 mysql
drwxr-x---  27 iorionda  admin  918  2 10  2017 mysql.bak
drwx------  27 iorionda  admin  918 12  4 18:46 postgres
drwxr-xr-x   5 iorionda  admin  170 10 14  2016 rbenv
drwxr-xr-x   2 iorionda  admin   68  8  9  2016 run
```

メッセージ通り、既にpostgresディレクトリが存在しているので削除する。

```
% rm -rf /usr/local/var/postgres
% ls -al /usr/local/var

total 0
drwxr-xr-x  11 iorionda  admin  374 12  4 19:10 .
drwxr-xr-x  17 root      wheel  578  2 22  2017 ..
drwxr-xr-x   3 iorionda  admin  102  8  9  2016 cache
drwxr-xr-x   3 iorionda  admin  102  8  9  2016 db
drwxr-xr-x   4 iorionda  admin  136 10  9  2016 homebrew
drwxr-xr-x   3 iorionda  admin  102  8 28 15:40 lib
drwxr-xr-x   5 iorionda  admin  170 12  1 14:25 log
drwxr-xr-x  25 iorionda  admin  850  9 21 17:29 mysql
drwxr-x---  27 iorionda  admin  918  2 10  2017 mysql.bak
drwxr-xr-x   5 iorionda  admin  170 10 14  2016 rbenv
drwxr-xr-x   2 iorionda  admin   68  8  9  2016 run
```

削除されたのが確認できたので、もう一度`initdb`する。

```
% initdb /usr/local/var/postgres -E utf8 --locale=C

The files belonging to this database system will be owned by user "iorionda".
This user must also own the server process.

The database cluster will be initialized with locale "C".
The default text search configuration will be set to "english".

Data page checksums are disabled.

creating directory /usr/local/var/postgres ... ok
creating subdirectories ... ok
selecting default max_connections ... 100
selecting default shared_buffers ... 128MB
selecting dynamic shared memory implementation ... posix
creating configuration files ... ok
running bootstrap script ... ok
performing post-bootstrap initialization ... ok
syncing data to disk ... ok

WARNING: enabling "trust" authentication for local connections
You can change this by editing pg_hba.conf or using the option -A, or
--auth-local and --auth-host, the next time you run initdb.

Success. You can now start the database server using:

    pg_ctl -D /usr/local/var/postgres -l logfile start
```

WARNINGが出ているけれど、今回は開発環境のため無視しておく。

## brew services でpostgresの自動起動設定を行う

```
% brew services start postgresql
==> Successfully started `postgresql` (label: homebrew.mxcl.postgresql)

%brew services list
Name       Status  User     Plist
mysql      stopped
postgresql started iorionda /Users/iorionda/Library/LaunchAgents/homebrew.mxcl.postgresql.plist
rabbitmq   started iorionda /Users/iorionda/Library/LaunchAgents/homebrew.mxcl.rabbitmq.plist
redis      started iorionda /Users/iorionda/Library/LaunchAgents/homebrew.mxcl.redis.plist
```

## データベースの確認

今のデータベースの状況を確認する

```
% psql -l

List of databases
Name    |  Owner   | Encoding | Collate | Ctype |   Access privileges
-----------+----------+----------+---------+-------+-----------------------
postgres  | iorionda | UTF8     | C       | C     |
template0 | iorionda | UTF8     | C       | C     | =c/iorionda          +
|          |          |         |       | iorionda=CTc/iorionda
template1 | iorionda | UTF8     | C       | C     | =c/iorionda          +
|          |          |         |       | iorionda=CTc/iorionda
(3 rows)
```

## ユーザーの作成

Django向けにpostgresユーザーを作成する。
まずは現在のユーザー一覧を確認する。

```
% psql -q -c'select * from pg_user' postgres

usename  | usesysid | usecreatedb | usesuper | userepl | usebypassrls |  passwd  | valuntil | useconfig
----------+----------+-------------+----------+---------+--------------+----------+----------+-----------
iorionda |       10 | t           | t        | t       | t            | ******** |          |
(1 row)
```

続けてユーザーを作成する。

```
% createuser -P
 postgres

# 作成したユーザーが存在するか確認
% psql -q -c'select * from pg_user' postgres
usename  | usesysid | usecreatedb | usesuper | userepl | usebypassrls |  passwd  | valuntil | useconfig
----------+----------+-------------+----------+---------+--------------+----------+----------+-----------
iorionda |       10 | t           | t        | t       | t            | ******** |          |
postgres |    16384 | f           | f        | f       | f            | ******** |          |
(2 rows)

```

## 作成したユーザーがオーナーのdatabaseを作成する

postgresユーザーがオーナーのdatabaseを作成する。

```
% createdb -O postgres finreader
% psql -l
List of databases
Name    |  Owner   | Encoding | Collate | Ctype |   Access privileges
-----------+----------+----------+---------+-------+-----------------------
finreader | postgres | UTF8     | C       | C     |
postgres  | iorionda | UTF8     | C       | C     |
template0 | iorionda | UTF8     | C       | C     | =c/iorionda          +
|          |          |         |       | iorionda=CTc/iorionda
template1 | iorionda | UTF8     | C       | C     | =c/iorionda          +
|          |          |         |       | iorionda=CTc/iorionda
(4 rows)
```

以上でMacのPostgreSQLの準備は終了。

## Djangoのsettings.pyを編集する。

```
DATABASES = {
    'default': {
         'ENGINE': 'django.db.backends.postgresql_psycopg2',
         'NAME': 'DB_NAME',
         'USER': 'USER_NAME',
         'PASSWORD' : 'PASSWORD',
         'HOST' : '127.0.0.1',
         'PORT' : 5432,
     }
 }
 ```

 ## マイグレーションの実行

 ```
 % python manage.py migrate
 ```

 これでエラーが出なければ成功。
 
