# psql が Library not loaded になってしまう

## TL;DR
`psql`がエラーになってしまった。
Homebrewで使用している`readline`のバージョンをスイッチすればOK


```
$ psql -v
dyld: Library not loaded: /usr/local/opt/readline/lib/libreadline.7.dylib
  Referenced from: /usr/local/bin/psql
  Reason: image not found
fish: 'psql' terminated by signal SIGABRT (Abort)
```

```
$ brew switch readline 7.0.3_1
Cleaning /usr/local/Cellar/readline/6.3.8
Cleaning /usr/local/Cellar/readline/7.0.3_1
Cleaning /usr/local/Cellar/readline/7.0.5
Cleaning /usr/local/Cellar/readline/8.0.0
```

# 初期状態のRDSに接続する
```
psql -h voice-karte-dbinstance.csazskpv51sn.ap-northeast-1.rds.amazonaws.com -U <username> postgres
```

usernameとpasswordはterraform.tfvarsに書いてある。

## userを作成する
```
CREATE USER voice_karte_user WITH PASSWORD 'FeBiMUWWaQPr';
```

## databaseを作成する
```
CREATE DATABASE voice_karte_app;
