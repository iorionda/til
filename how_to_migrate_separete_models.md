# Django の models.py を分割した場合に migration する方法

## 構成

```
├── news
│   ├── models
│   │   ├── __init__.py
│   │   ├── category.py
│   │   ├── comments.py
│   │   ├── news.py
│   │   └── stocks.py
```

models 以下のファイルをロードする為に `__init__.py` を実装する必要がある。

```
from news.models.news import *
from news.models.category import *
from news.models.comments import *
from news.models.stocks import *
```
