## csvを読み込んでテンプレートに差し込む
- VLAN.csv（csvデータ）
- vlan2.txt（テンプレート、forループ）

データ中身や使い方次第で、便利なものができそう。


## pipからjinja2パッケージをインストール
pip3 install jinja2


## pythonプログラムを実行
python3 test_.py


## 参考にしたページ
https://stackoverflow.com/questions/66333367/for-loop-inside-jinja2-template-with-csv


## pythonプログラムを実行して output-2.txt にファイル出力
python3 test_.py > output-2.txt


## ファイルの書き出し
with open('sample.txt', 'w') as f:
    f.write(vlan_config)


## 環境
- パソコン: X230（Lenovo ThinkPad）
- OS: Linux Mint 20.3（Xfce）
- Python 3.8.10
