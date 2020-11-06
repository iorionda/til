# コーディングスタイルのフォーマットに利用しているツール

## black
Python のコードを自動でフォーマットしてくれるツール

### black の特徴
black は制限が強く、自由に設定ができないのが特徴。
開発プロジェクトごとの違いや開発者の好みを反映することはほぼできない

- PEP8に自動で従ってほしい
- PEP8で触れられてない以上のルールを設定したい
- どこで改行するか議論したくない
  - \ で改行するか
  - () で改行するか
  - () のどこで改行するのか
- シングルクォートを使うのか、ダブルクォートを使うのかで議論したくない
- 「プロジェクトごとに色々設定」できないほうが楽で良い

### how to install

```
$ pip install black
```

### how to use

```
$ black <target>
```

### 設定
基本的には設定できる項目があまりないが、文字の幅や無視するパスを指定することが出来る
プロジェクト配下に pyproject.toml をおいて設定を適用することが出来る

```
[tool.black]
line-length = 119
target-version = ['py37']
include = '\.pyi?$'
exclude = '''

(
  /(
      \.eggs         # exclude a few common directories in the
    | \.git          # root of the project
    | \.hg
    | \.mypy_cache
    | \.tox
    | \.venv
    | _build
    | buck-out
    | build
    | dist
  )/
  | foo.py           # also separately exclude a file named foo.py in
                     # the root of the project
)
'''
```

また、後述の isort や black と共存することもできる

```
[flake8]
max-line-length = 119
ignore = E203,W503,W504

[tool.isort]
include_trailing_comma = true
line_length = 119
multi_line_output = 3
```

## isort
PEP8 では import に関して以下の記述がある

> Imports should be grouped in the following order:

> importは次の順序でグループ化する必要があります。

> Standard library imports.（標準ライブラリ）
> Related third party imports.（サードパーティ関連）
> Local application/library specific imports.（ローカルアプリケーション/ライブラリ固有）
> You should put a blank line between each group of imports.

> importの各グループの間に空白行を挿入する必要があります。

しかし、パッケージの順番をおぼえるのは大変

そこで、適切な順番に並び替えてくれるライブラリを使う

### how to install

```
$ pip install isort
```

### how to use

```
$ isort <target>
```

#### 実行前

```
from django.contrib import admin
from .models import Contract
from sectionviewer.models import Company, Camera
from related_admin import RelatedFieldAdmin
from related_admin import getter_for_related_field
import requests
from django.conf import settings
import logging
import datetime
```

#### 実行後

```
import datetime
import logging

import requests
from related_admin import RelatedFieldAdmin, getter_for_related_field

from django.conf import settings
from django.contrib import admin
from sectionviewer.models import Camera, Company

from .models import Contract
```

## flake8
広範囲をカバーしてくれる Python のコードチェックツール

具体的には下記コードチェックのラッパーツール
自動的に修正してくれるわけではない

- PyFlakes（pyflakes : コードのエラーチェック）
- pycodestyle（pycodestyle : PEP8に準拠しているかチェック）
- Ned Batchelder’s McCabe script（mccabe : 循環的複雑度のチェック）

### how to install

```
$ pip install flake8
```

### how to use

```
$ flake8 <target>
```

#### 出力結果

```
❯ flake8 source /Users/iorionda/src/github.com/randd-nxw/uriba-watch/django/contract/admin.py
source:0:1: E902 FileNotFoundError: [Errno 2] No such file or directory: 'source'
/Users/iorionda/src/github.com/randd-nxw/uriba-watch/django/contract/admin.py:14:1: E302 expected 2 blank lines, found 1
/Users/iorionda/src/github.com/randd-nxw/uriba-watch/django/contract/admin.py:16:120: E501 line too long (136 > 119 characters)
/Users/iorionda/src/github.com/randd-nxw/uriba-watch/django/contract/admin.py:30:23: E261 at least two spaces before inline comment
/Users/iorionda/src/github.com/randd-nxw/uriba-watch/django/contract/admin.py:40:120: E501 line too long (137 > 119 characters)
/Users/iorionda/src/github.com/randd-nxw/uriba-watch/django/contract/admin.py:42:120: E501 line too long (157 > 119 characters)
/Users/iorionda/src/github.com/randd-nxw/uriba-watch/django/contract/admin.py:52:14: E261 at least two spaces before inline comment
/Users/iorionda/src/github.com/randd-nxw/uriba-watch/django/contract/admin.py:60:120: E501 line too long (174 > 119 characters)
/Users/iorionda/src/github.com/randd-nxw/uriba-watch/django/contract/admin.py:74:120: E501 line too long (153 > 119 characters)
/Users/iorionda/src/github.com/randd-nxw/uriba-watch/django/contract/admin.py:84:1: E305 expected 2 blank lines after class or function definition, found 1
/Users/iorionda/src/github.com/randd-nxw/uriba-watch/django/contract/admin.py:86:1: E302 expected 2 blank lines, found 1
/Users/iorionda/src/github.com/randd-nxw/uriba-watch/django/contract/admin.py:117:1: E302 expected 2 blank lines, found 1
/Users/iorionda/src/github.com/randd-nxw/uriba-watch/django/contract/admin.py:132:1: E305 expected 2 blank lines after class or function definition, found 1
```

修正箇所をわかりやすくする為に `--show-source` を argument に指定すると良い

```
/Users/iorionda/.venv/bin/flake8 --show-source /Users/iorionda/src/github.com/randd-nxw/uriba-watch/django/contract/admin.py
/Users/iorionda/src/github.com/randd-nxw/uriba-watch/django/contract/admin.py:14:1: E302 expected 2 blank lines, found 1
class ContractAdmin(RelatedFieldAdmin):
^
/Users/iorionda/src/github.com/randd-nxw/uriba-watch/django/contract/admin.py:16:120: E501 line too long (136 > 119 characters)
    list_display = ('contract_uuid', 'camera', 'company', 'camera__store', 'camera__department', 'camera__name', 'camera__camera_type',)
                                                                                                                       ^
/Users/iorionda/src/github.com/randd-nxw/uriba-watch/django/contract/admin.py:30:23: E261 at least two spaces before inline comment
        if not change: # 新規作成
                      ^
/Users/iorionda/src/github.com/randd-nxw/uriba-watch/django/contract/admin.py:40:120: E501 line too long (137 > 119 characters)
                response_post = requests.post(device_contract_create_url, json=contract_data, timeout=settings.REQUEST_TERMINATE_TIMEOUT)
                                                                                                                       ^
/Users/iorionda/src/github.com/randd-nxw/uriba-watch/django/contract/admin.py:42:120: E501 line too long (157 > 119 characters)
                response_get = requests.get(device_contract_get_url, params={'serial': obj.camera.serial_number}, timeout=settings.REQUEST_TERMINATE_TIMEOUT)
                                                                                                                       ^
/Users/iorionda/src/github.com/randd-nxw/uriba-watch/django/contract/admin.py:52:14: E261 at least two spaces before inline comment
        else: # 既存レコードの更新
             ^
/Users/iorionda/src/github.com/randd-nxw/uriba-watch/django/contract/admin.py:60:120: E501 line too long (174 > 119 characters)
                response_post = requests.post(device_contract_set_url, json=contract_data, params={'deviceid': obj.contract_uuid}, timeout=settings.REQUEST_TERMINATE_TIMEOUT)
                                                                                                                       ^
/Users/iorionda/src/github.com/randd-nxw/uriba-watch/django/contract/admin.py:74:120: E501 line too long (153 > 119 characters)
            response_post = requests.post(device_contract_delete_url, params={'deviceid': obj.contract_uuid}, timeout=settings.REQUEST_TERMINATE_TIMEOUT)
                                                                                                                       ^
/Users/iorionda/src/github.com/randd-nxw/uriba-watch/django/contract/admin.py:84:1: E305 expected 2 blank lines after class or function definition, found 1
admin.site.register(Contract, ContractAdmin)
^
/Users/iorionda/src/github.com/randd-nxw/uriba-watch/django/contract/admin.py:86:1: E302 expected 2 blank lines, found 1
class ContractInline(admin.TabularInline):
^
/Users/iorionda/src/github.com/randd-nxw/uriba-watch/django/contract/admin.py:117:1: E302 expected 2 blank lines, found 1
class CompanyAdmin(admin.ModelAdmin):
^
/Users/iorionda/src/github.com/randd-nxw/uriba-watch/django/contract/admin.py:132:1: E305 expected 2 blank lines after class or function definition, found 1
admin.site.register(Company, CompanyAdmin)
^

Process finished with exit code 1
```
