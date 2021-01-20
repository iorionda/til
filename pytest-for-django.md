# Django アプリの自動テスト

Django のテストには Python標準の `unittest.TestCase` を拡張したものが用意されているが、アサーションメソッドが多すぎるのと `fixture` の機能が乏しいので `pytest-django` をメインに利用してテストコードの作成を行っている。

pytest のメリットとしては

- pytest では単純なテストを書くのが簡単
- 複雑なテストをかくのも結構簡単
- pytest のテストコードは読みやすい
- テストを失敗させるには `assert` を使うだけでよい
- unittest や nose 用に書かれたテストも pytest で実行できる

が挙げられる。

## テストの実行方法

今回のプロジェクトの構成では docker-compose 上で Python が動いているので `docker-compose run` からテストを実行する。
テストコードを引数で指定することで、テストの件数を絞ってテストを行うことができる。
```
docker-compose run app pytest users/tests/test_views.py::test_ユーザー削除画面Viewが使われている

docker-compose run app pytest users/tests/test_views.py::test_ユーザー削除画面Viewが使われている
WARNING: Found orphan containers (uriba-watch_db_1) for this project. If you removed or renamed this service in your compose file, you can run this command with the --remove-orphans flag to clean it up.
Creating uriba-watch_app_run ... done
============================================================================================================================ test session starts =============================================================================================================================
platform linux -- Python 3.7.4, pytest-6.2.0, py-1.10.0, pluggy-0.13.1
django: settings: uriba_watch.settings (from ini)
rootdir: /opt/project, configfile: pytest.ini
plugins: freezegun-0.4.2, Faker-5.0.1, responses-0.4.0, django-4.1.0
collected 1 item

users/tests/test_views.py .                                                                                                                                                                                                                                            [100%]

============================================================================================================================== warnings summary ==============================================================================================================================
users/tests/test_views.py::test_ユーザー削除画面Viewが使われている
  /root/.local/share/virtualenvs/project-FOtWqnnI/lib/python3.7/site-packages/boto/plugin.py:40: DeprecationWarning: the imp module is deprecated in favour of importlib; see the module's documentation for alternative uses
    import imp

-- Docs: https://docs.pytest.org/en/stable/warnings.html
======================================================================================================================= 1 passed, 1 warning in 28.64s ========================================================================================================================

```

## 環境

- Python 3.7
- Django 2.2

## テスト用のパッケージ

- pytest-django = "*"
- pytest-freezegun = "*"
- pytest-responses = "*"
- faker = "*"

## pytest.ini の作成
pytest-django を使ってテストをする為に、設定ファイル `pytest.ini` を作成して、`DJANGO_SETTINGS_MODULE` を設定する。

```
❯ cat pytest.ini
[pytest]
DJANGO_SETTINGS_MODULE=uriba_watch.settings
```

## Factoryの作成

テストで使うデータの作成には2通りある。

- fixture
- factory

今回はデータの関連を `Arrange` のタイミングで作成した方がわかりやすいテストが書けるので factory で作成している。
factory は各アプリケーションディレクトリの `factory.py` または `factories` ディレクトリに定義している。

```
class CompanyModelFactory(DjangoModelFactory):
    class Meta:
        model = Company

    name = fake.company()
    email = fake.ascii_company_email()
    postal_code = fake.postcode()
    prefecture = fake.prefecture()
    municipality = fake.city()
    address = fake.address()
    telephone_number = fake.phone_number()
    created_at = datetime.now()
    updated_at = datetime.now()


class DepartmentModelFactory(DjangoModelFactory):
    class Meta:
        model = Department

    name = fake.company_category()
    company = SubFactory(CompanyModelFactory)
    created_at = datetime.now()
    updated_at = datetime.now()


class StoreModelFactory(DjangoModelFactory):
    class Meta:
        model = Store

    name = fake.town() + "店"
    postal_code = fake.postcode()
    address = fake.address()
    telephone_number = fake.phone_number()
    company = SubFactory(CompanyModelFactory)
    created_at = datetime.now()
    updated_at = datetime.now()
```

## Modelのテスト

`models.py` に対するテストコードとして `test_models.py` を作成する。
`sectionviewser` では `models.py` を複数ファイルに分割しているので、それに対応するようにファイルを分割してテストを作成している。
`tests` ディレクトリ配下に対応する `test_xxx.py` を作成している。

```
sectionviewer/tests
├── __init__.py
├── test_company.py
├── test_department.py
├── test_filtercondition.py
├── test_store.py
└── test_time_range.py
```

例のテストでは店舗に関連するメディアファイルの有無をテストしている。

```
class TestHasMediafileSet(object):
    @pytest.fixture
    def test_has_mediafile_set(self):
        company = CompanyModelFactory(id=1)
        store = StoreModelFactory(id=1, company=company)
        department = DepartmentModelFactory(company=company)
        camera = CameraModelFactory(company=company, store=store, department=department)
        MediafileModelFactory(
            id=1,
            company=company,
            store=store,
            department=department,
            camera=camera,
            created_at=datetime(2020, 12, 15, 1, 0, 0, tzinfo=timezone.utc),
            ext="jpg",
        )
        MediafileModelFactory(
            id=2,
            company=company,
            store=store,
            department=department,
            camera=camera,
            created_at=datetime(2020, 12, 15, 11, 0, 0, tzinfo=timezone.utc),
            ext="jpg",
        )

    @pytest.mark.django_db
    def test_メディアファイルがある場合(self, test_has_mediafile_set):
        store = Store.objects.get(id=1)

        expect_mediafile_set = store.has_mediafile_set()

        assert expect_mediafile_set is True

    @pytest.mark.django_db
    def test_メディアファイルがない場合(self):
        company = CompanyModelFactory(id=1)
        store = StoreModelFactory(name="神谷町店", company=company)
```

@pytest.fixture はテストの前処理(DBのセットアップやモックの作成など)を行う為の pytest の機能である。
fixture をうまく使うことでテストコードをクリーンに保つことができる。
テストケースの中で、その fixture を使用したい場合は、テストケースの引数に作成した fixture を指定するだけで利用できるようになる。

```
    # これが fixture
    @pytest.fixture
    def test_has_mediafile_set(self):
        company = CompanyModelFactory(id=1)
        store = StoreModelFactory(id=1, company=company)
        department = DepartmentModelFactory(company=company)
        camera = CameraModelFactory(company=company, store=store, department=department)
        MediafileModelFactory(
            id=1,
            company=company,
            store=store,
            department=department,
            camera=camera,
            created_at=datetime(2020, 12, 15, 1, 0, 0, tzinfo=timezone.utc),
            ext="jpg",
        )
        MediafileModelFactory(
            id=2,
            company=company,
            store=store,
            department=department,
            camera=camera,
            created_at=datetime(2020, 12, 15, 11, 0, 0, tzinfo=timezone.utc),
            ext="jpg",
        )
```

また pytest-django でテスト用のデータベースアクセスが必要になるテストケースの場合は `@pytest.mark.django_db` デコレータを指定する必要がある。

## URL のテスト

urls.py に対するテストコードとして `test_urls.py` を作成する。

テストでは

- URL が存在する場合に対応するクラスが呼ばれているか
- URL が存在しない場合に `Resolver404` 例外が発生するか

を確認している。

```
def test_存在しないURLの場合():
    with pytest.raises(Resolver404):
        resolve("/users/not-exist")


def test_ユーザー一覧ページ():
    found = resolve("/users/")

    assert found.func.__name__ == UserListView.__name__
```

pytest では例外を補足する場合には `with pytest.raises(例外):` で確認することができる。

## View のテスト

`views.py` に対応するテストコードとして `test_views.py` を作成する。

テストでは

- 正しいステータスコードか
- 期待しているテンプレートが使用されているか
- レスポンスに期待しているデータが含まれているか

を確認している。

```
@pytest.mark.django_db
def test_ユーザー一覧画面Viewが使われている(rf):
    company = CompanyModelFactory()
    user = User.objects.create(company=company, username="test_user_1", email=fake.safe_email())
    User.objects.create(company=company, username="test_user_2", email=fake.safe_email())
    User.objects.create(company=company, username="test_user_3", email=fake.safe_email())

    request = rf.get(reverse("users:user"))
    request.user = user

    response = UserListView.as_view()(request)

    assert "users/user_list.html" in response.template_name
    assert response.status_code == 200

    assert len(response.context_data["user_list"]) == 3
    assert set(list(response.context_data["user_list"])) == set(list(User.objects.filter(company_id=company.id)))
```

なお View へのリクエスト方法としては
 
- django.test.client
- django.test.RequestFactory

の二種類があるが今回は POSTリクエストの確認の為にRequestFactory を使ってテストコードを書いている。
TestClient なのか RequestFactory なのかは、テストケースの引数に何が渡されているかで判定されている。
`client` という引数が渡ってくる想定で書くと `TestClient` が渡ってくる。
`rf` という引数が渡ってくる想定で書くと `RequestFactory` が渡ってくる。

## Form のテスト

`forms.py` に対するテストコードとして `test_forms.py` を作成している。
通常は ModelForm は Model と紐付いている為、その部分のテストは不要だが、今回はモデルのテストが無い中で作成したのでバリデーションのテストも `test_forms.py` に記述している。

```
class TestIsValid(object):
    @pytest.fixture
    def test_data(self):
        company = CompanyModelFactory(id=1)
        UserModelFactory(id=1, company=company)

    @pytest.mark.django_db
    def test_is_valid(self, test_data):
        current_user = User.objects.get(id=1)

        data = {
            "username": fake.user_name(),
            "first_name": fake.first_name(),
            "last_name": fake.last_name(),
            "role": 2,
            "email": fake.safe_email(),
            "departments": Department.objects.all(),
            "stores": Store.objects.all(),
        }
        form = UserCreateForm(data=data, current_user=current_user)

        assert form.is_valid() is True

    @pytest.mark.django_db
    def test_ユーザーIDに記号がある(self, test_data):
        current_user = User.objects.get(id=1)

        data = {
            "username": "username!",
            "first_name": fake.first_name(),
            "last_name": fake.last_name(),
            "role": 2,
            "email": fake.safe_email(),
            "departments": Department.objects.all(),
            "stores": Store.objects.all(),
        }
        form = UserCreateForm(data=data, current_user=current_user)

        assert form.is_valid() is False

    @pytest.mark.django_db
    def test_usernameが150文字(self, test_data):
        current_user = User.objects.get(id=1)

        data = {
            "username": "a" * 150,
            "first_name": fake.first_name(),
            "last_name": fake.last_name(),
            "role": 2,
            "email": fake.safe_email(),
            "departments": Department.objects.all(),
            "stores": Store.objects.all(),
        }
        form = UserCreateForm(data=data, current_user=current_user)

        assert form.is_valid() is True

    @pytest.mark.django_db
    def test_usernameが151文字(self, test_data):
        current_user = User.objects.get(id=1)

        data = {
            "username": "a" * 151,
            "first_name": fake.first_name(),
            "last_name": fake.last_name(),
            "role": 2,
            "email": fake.safe_email(),
            "departments": Department.objects.all(),
            "stores": Store.objects.all(),
        }
        form = UserCreateForm(data=data, current_user=current_user)

        assert form.is_valid() is False
```
