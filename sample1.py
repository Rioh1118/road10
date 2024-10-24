"""
データを読み込んでそれをtrainとtestに分割し、ディレクトリ毎に保存する。
"""

from road_sign import DatasetHandler

data_handler = DatasetHandler(data_dir="./data/project18", train_dir="./data/train", test_dir="./data/test")

data_handler.convert_jfif_to_jpg_or_png()
data_handler.load_data()
data_handler.split_data()
data_handler.save_data()
