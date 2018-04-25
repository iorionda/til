# AWSにdeployした手順

## EC2インスタンスの作成

## yumアップデート
```
% sudo yum update -y
```

## nginx の設定
```
% yum install nginx
% chkconfig --add nginx
% chkconfig nginx on
% chkconfig | grep nginx
```

Amazon Linuxでは/etc/nginx/nginx.confに設定ファイルがある

```
/etc/nginx/nginx.conf
〜中略〜

http {
   〜中略〜

   upstream app_server {
       server 127.0.0.1:8000 fail_timeout=0;
    }

   server {
        #以下4行はコメントアウト
        #listen       80 default_server;
        #listen       [::]:80 default_server;
        #server_name  localhost;
        #root         /usr/share/nginx/html;

       # 以下3行を追加
        listen    80;
        server_name     IPアドレス or ドメイン;
        client_max_body_size    4G;

       # Load configuration files for the default server block.
        include /etc/nginx/default.d/*.conf;

       location / {
            # 以下4行を追加
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
            proxy_set_header Host $http_host;
            proxy_redirect off;
            proxy_pass   http://app_server;
        }

   〜以下略〜
```

### nginxを再起動する
```
% service nginx restart
```

## git のインストール
```
% yum install git
```

### 鍵の設定
```
% ssh-keygen -t rsa
% cat ~/.ssh/id_rsa.pub
```

公開鍵をgithubに設定する

リポジトリを`git clone`する

## pythonのインストール
```
% yum list | grep python36
% yum install python36-devel python36-libs python36-setuptools
```

### 依存するライブラリのインストール
```
% yum install gcc gcc-c++ zlib-devel bzip2 bzip2-devel readline readline-devel openssl openssl-devel -y
% yum install postgresql
```

## mecabのインストール
```
% sudo rpm -ivh http://packages.groonga.org/centos/groonga-release-1.1.0-1.noarch.rpm
% yum -y install mecab mecab-ipadic mecab-devel
```

## pipのインストール
```
% /usr/bin/easy_install-3.6 pip
% pip3 install --upgrade -r finreader/requirements.txt
```

## redisのインストール
```
% sudo yum --enablerepo=epel install redis
% redis-server
```

## 起動確認
```
% gunicorn finreader.wsgi --bind=0.0.0.0:8000
```

## RDSの作成
インバウンドの設定
- PostgreSQL TCP 5432 0.0.0.0/0

### postgresユーザーになる
```
% sudo su - postgres
```

#### DBを作成する
```
$ createdb -O postgres finreader
```

#### migrateする
```
$ python3 manage.py migrate
```

### gunicornを起動して確認する
```
% gunicorn finreader.wsgi --bind=0.0.0.0:8000
```
http://(パブリックDNS)で確認できたら成功。

## daemon化する
```
% gunicorn finreader.wsgi --bind=0.0.0.0:8000 -D
% celery -A finreader worker -B -l info -D
```
