# DATASET LOADER

# 1.　概要
このリポジトリは下記のディレクトリ構造を前提にして、それをtrainとtestに分け、
torchvisionモジュールのdataloaderで取ってこれる形式に直すプログラムです。
そのクラスについて定義しているファイルはroad_sign.pyで、使い方の例をsample1,sample2で
示しています。

``` kotlin
data / project18 /
|   ├── class1Name/
│       ├── img1.jpg
│       ├── img2.jpg
│       └── ...
    ├── class2Name/
│       └── img1.jpg
└── ...

```

# 2 .使い方
2.1. 前提条件
このプロジェクトを実行するためには、以下のライブラリが必要です。

- Python 3.x
- PyTorch
- torchvision
- scikit-learn
- PIL (Python Imaging Library)

road_signモジュールをインポートするか、
road_sign.pyをコピペして、sample1, sample2を参考にして使ってください。
sample1は、基本的にはtrainとtestに分けて保存するだけです。
``` bash
data/
├── train/
│   ├── class1/
│   │   ├── img1.jpg
│   │   ├── img2.jpg
│   │   └── ...
│   ├── class2/
│   └── ...
└── test/
    ├── class1/
    └── class2/
```