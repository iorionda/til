# Rails の bundle install で mysql2 library not found for -lzstd のエラー

Apple silicon の Mac で Ruby on Rails の `bundle install` 実行時に mysql2 の gem で以下のエラーが発生した。

```
❯ bundle install
Fetching gem metadata from https://rubygems.org/............
Resolving dependencies...
Using rake 13.0.6
Using concurrent-ruby 1.1.9
Using nio4r 2.5.8
Using zeitwerk 2.4.2
Using builder 3.2.4
Using websocket-extensions 0.1.5
Using public_suffix 4.0.6
Using racc 1.5.2
Using bindex 0.8.1
Using msgpack 1.4.2
Using bundler 2.2.22
Using byebug 11.1.3
Using childprocess 3.0.0
Using ffi 1.15.3
Using method_source 1.0.0
Using thor 1.1.0
Using rack 2.2.3
Using graphql 1.12.15
Using rb-fsevent 0.11.0
Using rubyzip 2.3.2
Using tilt 2.0.10
Using semantic_range 3.0.0
Using spring 2.1.1
Using sqlite3 1.4.2
Using turbolinks-source 5.2.0
Using i18n 1.8.10
Using tzinfo 2.0.4
Using puma 5.4.0
Using nokogiri 1.12.3 (arm64-darwin)
Using websocket-driver 0.7.5
Using bootsnap 1.8.0
Using regexp_parser 2.1.1
Using rb-inotify 0.10.1
Using minitest 5.14.4
Using sassc 2.4.0
Using rack-test 1.1.0
Using sprockets 4.0.2
Using rack-mini-profiler 2.3.2
Using rack-proxy 0.7.0
Using selenium-webdriver 3.142.7
Using turbolinks 5.2.1
Using xpath 3.2.0
Using marcel 1.0.1
Using mini_mime 1.1.1
Using listen 3.7.0
Fetching mysql2 0.5.3
Using crass 1.0.6
Using addressable 2.8.0
Using activesupport 6.1.4.1
Using webdrivers 4.6.1
Using capybara 3.35.3
Using mail 2.7.1
Using loofah 2.12.0
Using rails-dom-testing 2.0.3
Using globalid 0.5.2
Using rails-html-sanitizer 1.4.2
Using activemodel 6.1.4.1
Using erubi 1.10.0
Using jbuilder 2.11.2
Using activejob 6.1.4.1
Using activerecord 6.1.4.1
Using actionview 6.1.4.1
Using actionpack 6.1.4.1
Using actioncable 6.1.4.1
Using activestorage 6.1.4.1
Using actionmailer 6.1.4.1
Using railties 6.1.4.1
Using sprockets-rails 3.2.2
Using actionmailbox 6.1.4.1
Using actiontext 6.1.4.1
Using graphiql-rails 1.8.0
Using sassc-rails 2.1.2
Using web-console 4.1.0
Using webpacker 5.4.2
Using rails 6.1.4.1
Using sass-rails 6.0.0
Installing mysql2 0.5.3 with native extensions
Gem::Ext::BuildError: ERROR: Failed to build gem native extension.

    current directory: /Users/iorionda/src/github.com/iorionda/til/graphql_rails/vendor/bundle/ruby/3.0.0/gems/mysql2-0.5.3/ext/mysql2
/Users/iorionda/.rbenv/versions/3.0.2/bin/ruby -I /Users/iorionda/.rbenv/versions/3.0.2/lib/ruby/3.0.0 -r
./siteconf20210827-69640-ew2un3.rb extconf.rb --with-cppflags\=-I/usr/local/opt/openssl@1.1/include
checking for rb_absint_size()... yes
checking for rb_absint_singlebit_p()... yes
checking for rb_wait_for_single_fd()... yes
-----
Using mysql_config at /opt/homebrew/bin/mysql_config
-----
checking for mysql.h... yes
checking for errmsg.h... yes
checking for SSL_MODE_DISABLED in mysql.h... yes
checking for SSL_MODE_PREFERRED in mysql.h... yes
checking for SSL_MODE_REQUIRED in mysql.h... yes
checking for SSL_MODE_VERIFY_CA in mysql.h... yes
checking for SSL_MODE_VERIFY_IDENTITY in mysql.h... yes
checking for MYSQL.net.vio in mysql.h... yes
checking for MYSQL.net.pvio in mysql.h... no
checking for MYSQL_ENABLE_CLEARTEXT_PLUGIN in mysql.h... yes
checking for SERVER_QUERY_NO_GOOD_INDEX_USED in mysql.h... yes
checking for SERVER_QUERY_NO_INDEX_USED in mysql.h... yes
checking for SERVER_QUERY_WAS_SLOW in mysql.h... yes
checking for MYSQL_OPTION_MULTI_STATEMENTS_ON in mysql.h... yes
checking for MYSQL_OPTION_MULTI_STATEMENTS_OFF in mysql.h... yes
checking for my_bool in mysql.h... no
-----
Don't know how to set rpath on your system, if MySQL libraries are not in path mysql2 may not load
-----
-----
Setting libpath to /opt/homebrew/Cellar/mysql/8.0.25_1/lib
-----
creating Makefile

current directory: /Users/iorionda/src/github.com/iorionda/til/graphql_rails/vendor/bundle/ruby/3.0.0/gems/mysql2-0.5.3/ext/mysql2
make DESTDIR\= clean

current directory: /Users/iorionda/src/github.com/iorionda/til/graphql_rails/vendor/bundle/ruby/3.0.0/gems/mysql2-0.5.3/ext/mysql2
make DESTDIR\=
compiling client.c
client.c:787:14: warning: incompatible function pointer types passing 'VALUE (void *)' (aka 'unsigned long (void *)') to parameter of
type 'VALUE (*)(VALUE)' (aka 'unsigned long (*)(unsigned long)') [-Wincompatible-function-pointer-types]
  rb_rescue2(do_send_query, (VALUE)&args, disconnect_and_raise, self, rb_eException, (VALUE)0);
             ^~~~~~~~~~~~~
/Users/iorionda/.rbenv/versions/3.0.2/include/ruby-3.0.0/ruby/internal/iterator.h:51:25: note: passing argument to parameter here
VALUE rb_rescue2(VALUE(*)(VALUE),VALUE,VALUE(*)(VALUE,VALUE),VALUE,...);
                        ^
client.c:795:16: warning: incompatible function pointer types passing 'VALUE (void *)' (aka 'unsigned long (void *)') to parameter of
type 'VALUE (*)(VALUE)' (aka 'unsigned long (*)(unsigned long)') [-Wincompatible-function-pointer-types]
    rb_rescue2(do_query, (VALUE)&async_args, disconnect_and_raise, self, rb_eException, (VALUE)0);
               ^~~~~~~~
/Users/iorionda/.rbenv/versions/3.0.2/include/ruby-3.0.0/ruby/internal/iterator.h:51:25: note: passing argument to parameter here
VALUE rb_rescue2(VALUE(*)(VALUE),VALUE,VALUE(*)(VALUE,VALUE),VALUE,...);
                        ^
2 warnings generated.
compiling infile.c
compiling mysql2_ext.c
compiling result.c
compiling statement.c
linking shared-object mysql2/mysql2.bundle
ld: library not found for -lzstd
clang: error: linker command failed with exit code 1 (use -v to see invocation)
make: *** [mysql2.bundle] Error 1

make failed, exit code 2

Gem files will remain installed in /Users/iorionda/src/github.com/iorionda/til/graphql_rails/vendor/bundle/ruby/3.0.0/gems/mysql2-0.5.3
for inspection.
Results logged to
/Users/iorionda/src/github.com/iorionda/til/graphql_rails/vendor/bundle/ruby/3.0.0/extensions/arm64-darwin-20/3.0.0/mysql2-0.5.3/gem_make.out

An error occurred while installing mysql2 (0.5.3), and Bundler cannot continue.
Make sure that `gem install mysql2 -v '0.5.3' --source 'https://rubygems.org/'` succeeds before bundling.

In Gemfile:
  mysql2
zsh: exit 5     bundle install
```

以下の手順でエラーが解消できた。

```
% bundle config --local build.mysql2 --with-ldflags=-L/opt/homebrew/lib --with-opt-dir=/opt/homebrew/opt/openssl
```

このコマンドを実行すると `.bundle/config` に以下のエントリーが追加される。

```
BUNDLE_BUILD__MYSQL2: "--with-ldflags=-L/opt/homebrew/lib --with-opt-dir=/opt/homebrew/opt/openssl"
```

ライブラリがインストールされていない場合は別途インストールする必要がある。

```
%brew install zstd
```
