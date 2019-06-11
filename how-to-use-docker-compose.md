## Docker-composeの使い方
### 環境を立ち上げる
```
# foregroundで起動
$ docker-compose up

# backgroundで起動
$ docker-compose up -d
```

### 環境を停止する
```
# foregroudで起動していた時
# CTRL + C
# backgroundで起動していた時
$ docker-copmose stop
```

### 再起動
```
# foregroundで起動していた時
$ docker-compose up
# backgroundで起動していた時
$ docker-compose restart
```

### build or Dockerfileの変更を反映させる
```
# foregroundで起動
$ docker-copmose up --build
# backgroundで起動
$ docker-compose up --build -d
```

### 後片付け
```
# 停止＆削除（コンテナ・ネットワーク）
$ docker-compose down

# 停止＆削除（コンテナ・ネットワーク・イメージ）
$ docker-compose down --rmi all

# 停止＆削除（コンテナ・ネットワーク・ボリューム）
$ docker-compose down -v
```
