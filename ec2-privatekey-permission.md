# EC2にSSHで接続しようとしたら、秘密鍵のパーミッションでエラーが発生する


```
ssh -i <pem file>  ec2-user@<EC2 public DNS>
```

```
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@         WARNING: UNPROTECTED PRIVATE KEY FILE!          @
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
Permissions 0644 for '/privatekey.pem' are too open.
It is required that your private key files are NOT accessible by others.
This private key will be ignored.
Load key "/Users/iorionda/.ssh/g_alert_check_apparel.pem": bad permissions
Permission denied (publickey,gssapi-keyex,gssapi-with-mic).
```

パーミッションが開きすぎているから、もっとセキュアにしろと言われる。
なので`600`に変更する。

```
chmod 600 <pem file>
```

これで EC2にSSH接続することができる



