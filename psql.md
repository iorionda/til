# psql を起動しようとしたら readline でエラーが出た

```
% psql -l
dyld: Library not loaded: /usr/local/opt/readline/lib/libreadline.7.dylib
 Referenced from: /usr/local/bin/psql
 Reason: image not found
fish: 'psql -l' terminated by signal SIGABRT (Abort)
```

readline.7.dylib がないとエラーを吐いた。
本当にないのか確認してみる。

```
% ls /usr/local/opt/readline/lib/libreadline.7.dylib
ls: /usr/local/opt/readline/lib/libreadline.7.dylib: No such file or directory
```
なかった。
なので、brewで現在6.3.8を使っているのを7系に変更する。

```
% brew switch readline 7.0.3_1
Cleaning /usr/local/Cellar/readline/6.3.8
Cleaning /usr/local/Cellar/readline/7.0.3_1
Opt link created for /usr/local/Cellar/readline/7.0.3_1

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

動いた。
