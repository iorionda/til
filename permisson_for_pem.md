# EC2にアクセスしようとした時に Permisson denied(Publickey)になってしまった時

## 問題
- ssh接続の時に以下のエラーが出る

```
% ssh -i ~/.ssh/xxx.pem  ec2-user@xxxx

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@         WARNING: UNPROTECTED PRIVATE KEY FILE!          @
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
Permissions 0644 for '/Users/xxx/.ssh/xxx.pem' are too open.
It is required that your private key files are NOT accessible by others.
This private key will be ignored.
Load key "/Users/xxx/.ssh/xxx.pem": bad permissions
Permission denied (publickey).
```

## 原因
- .pemファイルのアクセス権限の問題


## 解決

```
% chmod 600 ~/.ssh/xxx.pem
```
