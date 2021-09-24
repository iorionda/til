# 【Python】 ロギングをスッキリ使う

## `print()` は使わない

Pythonでシステム開発をする時に print 文でのデバッグには問題点がある。
ひとつは **表示される文字列がログ出力なのか、コマンドラインツールが本当にユーザーに提示したい情報なのかわからない** ことが挙げられる。
実際に標準出力で欲しい情報を出力することに `print()` で書き出すのは間違いではない。
ログは動作の過程で何かが発生した時のプログラムが動作したかを追跡する為に使うものだ。
なので **ログ出力** の為に `print()` ベースのアプローチはやめよう。

## logging も使わない

1. `from logging import getLogger` を使う。
2. `Logger` インスタンスを使う。
3. 環境設定ファイル(json/YAML)でロギングの設定を行う。
4. 簡易的に設定する場合は環境設定ファイルではなく `basicConfig()` を使う

## Python の `basicConfig()` の基本設定

``` python
from logging import critical
from logging import DEBUG
from logging import INFO
from logging import debug
from logging import error
from logging import info
from logging import warning
from logging import exception
from logging import basicConfig, getLogger

logger: Any = getLogger(__name__)
basicConfig(
    level=DEBUG, format="{asctime} [{levelname:.4}] {name}: {message}", style="{"
)
```

## handler を使った基本設定

```python
from logging import DEBUG, Formatter, StreamHandler, basicConfig, getLogger

logger: Any = getLogger(__name__)
logger.propagate = False
logger.setLevel(DEBUG)
handler = StreamHandler()
handler.setFormatter(Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
handler.setLevel(DEBUG)
logger.addHandler(handler)
```

## 関連情報

- [Python Logging Best Practices](https://pieces.openpolitics.com/2012/04/python-logging-best-practices/)
- [ライブラリのためのロギングの設定](https://docs.python.org/ja/3/howto/logging.html#configuring-logging-for-a-library)
- [Good logging practice in Python](https://fangpenlin.com/posts/2012/08/26/good-logging-practice-in-python/)
- [Pythonのloggingをスッキリ使いこなす](https://own-search-and-study.xyz/2019/10/20/python-logging-clear/)
