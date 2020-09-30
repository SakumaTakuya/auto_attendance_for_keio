# auto_attendance_for_keio
自動でGoogleFormを提出するアプリです。
恐らく任意のGoogleFormに対応していますが、デフォルトでは慶應の勤退フォームを自動化する設定になっています。

ちなみにrequestsではなくwebbrowserを利用しているのは認証まわりが面倒だったためです。


## 実行
[pipenv](https://pipenv-ja.readthedocs.io/ja/translate-ja/)で管理しているので、以下よりpipenvを起動し、実行してください。

```sh
$ pipenv shell
$ python main.py -d path/to/data.csv

or

$ pipenv run python main.py -d path/to/data.csv
```

ヘルプの確認は`-h`オプションで行います。
```sh
$ python main.py -h
usage: main.py [-h] [-s SETTINGS] -d DATA [-o {viewform,formResponse}]

optional arguments:
  -h, --help            show this help message and exit
  -s SETTINGS, --settings SETTINGS
                        設定モジュール名
  -d DATA, --data DATA  実行データのパス(DATA_ROOTからの相対パス指定)
  -o {viewform,formResponse}, --op {viewform,formResponse}
                        実行命令(表示:viewform, 提出:formResponse)
```

## 設定
設定ファイルは`settings`ディレクトリにpythonファイルで設置してください。可能な設定項目は次の通りです。
実行時に`-s`オプションをつけてモジュール名を指定してください。

- `BASE_DIR`
  - `main.py`のファイルパスです。
- `FORM_URL`
  - 自動で提出するフォームURLです。**viewform**や**formResponse**を含まないことに注意してください。
- `OPERATION`
  - 実行命令です。次の二値から選択してください。
    - `"viewform"` : 入力された状態でブラウザを開きます。
    - `"formResponse"` : 入力後提出します。この命令を実行する前に`"viewform"`で内容を確認することをお勧めします。
- `DATA_ROOT`
  - 提出するデータが置かれているディレクトリのルートパスです。
- `DATA_FORMAT`
  - 読み込むデータの形式をここで定義します。
  - keyにはGoogleFormのentryを設定します。詳しくは[他のGoogleFormに対応する](#他のGoogleFormに対応する)を参照してください。
  - valueにはデフォルト値を入力できます。氏名など、全て統一したい項目がある場合はここに記入してください。

## データ
デフォルトでは`data`ディレクトリにcsv形式で設置します。以下、データ例です。
一行目は`DATA_FORMAT`のkeyに対応したヘッダをつけてください。データは欠損していても問題ありません。

```csv
1897951779,603641719,909280450
出勤打刻忘れ報告,2020-09-04,13:00
退勤打刻忘れ報告,2020-09-04,18:00
```

`data/sample.csv`にサンプルを設置しているので、以下のコマンドで結果を確かめることができます。

```sh
$ pipenv run python main.py -d sample.csv 
```


## 他のGoogleFormに対応する
他のGoogleFormに対応するためには上記の設定を変更してください。
GoogleFormの形式については以下を参照してください。

https://qiita.com/mkohei/items/b62700b46bb71bf0a9c3
