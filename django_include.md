# Djangoのincludeの仕様変更のメモ

エラーになったのは以下のような場合

```
urlpatterns = [
  url(r'^admin/', admin.site.urls),
  url(r'foo/', include('foo.urls', namespace='foo')),
]
```

URLのルーティングをする場合にincludeを使うが、仕様が変わっていて以下のようなエラーがでた。

```
django.core.exceptions.ImproperlyConfigured: Specifying a namespace in include() without providing an app_name is not supported. Set the app_name attribute in the included module, or pass a 2-tuple containing the list of patterns and app_name instead.
```

上記の該当箇所を以下のようにincludeの引数にタプルオブジェクトを渡すことで正常に動くようになった。

* namespaceは使わない。
* タプルオブジェクトの2つ目の要素に従来のnamespaceに相当するものを設定する。

```
urlpatterns = [
  url(r'^admin/', admin.site.urls),
  url(r'foo/', include(('foo.urls', 'foo'),)),
]
```
