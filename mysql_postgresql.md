# MySQLとPostgreSQLコマンド比較表

機能 | MySQL | PostgreSQL
----|----|----
起動 | `$ mysql -p -h ホスト名 -P ポート番号 -u ユーザ名 DB名` | `$ psql -h ホスト名 -p ポート番号 -U ユーザ名 DB名`
データベース一覧 | show databases; | \l
データベース切替 | use DB名<br>\u DB名 | \c DB名
テーブル一覧 | show tables; | \d、\dt、\d+、\dt+
テーブル定義確認 | desc テーブル名; | \d テーブル名
テーブルCREATE文確認 | show create table テーブル名 | pg_dump DB名 -U ユーザ名 -s -t テーブル名
インデックス一覧 | SHOW INDEX FROM tbl_name; | \d table_name
行表示の切り替え | select * from t \G | \x<BR>select * from t;
SQLファイル実行 | \\. | \i
SQLダンプ | mysqldump | pg_dump
TSVダンプ | mysqldump -u USER --password=PASS DATABASE_NAME TABLE_NAME -T /tmp | ？？？
TSVインポート | LOAD DATA LOCAL INFILE '\$FILE_NAME' REPLACE INTO TABLE \$TABLE_NAME IGNORE 1 LINES; | copy table_name from '/absolute_path/to/data.tsv' ( delimiter '    ', format csv, header true ); **※1**
SQL時間計測 | デフォルトで表示される | \timing on
ログ出力開始 | \T log.txt | \o log.txt
ログ出力終了 | \t | \o
定義をコピーしてテーブル作成 | create table t2 like t1; | create table t2 (like t1);
実行計画 | SQLの先頭にEXPLAINをつける | SQLの先頭にEXPLAINをつける
接続先サーバ確認|\s | \conninfo
接続を確認 | show processlist; | select * from pg_stat_activity; |
連番ID | カラム名 int auto_increment | カラム名 serial
今日の日付 | curdate() | current_date
現在時刻 | now() | now()
ヘルプ | \h または \? | \?
設定ファイル | ~/.my.cnf | ~/.psqlrc
