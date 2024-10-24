import os
import shutil
from sklearn.model_selection import train_test_split
from PIL import Image

class DatasetHandler:
    def __init__(self, data_dir, train_dir, test_dir, test_size=0.2):
        """
        データセットのハンドリングを行うクラス

        Parameters:
        :param data_dir: 全ての画像が保存されているディレクトリ
        :param train_dir: 分割後の訓練データの保存先ディレクトリ
        :param test_dir: 分割後のテストデータの保存先ディレクトリ
        :param test_size: 訓練データとテストデータの分割比率
        """
        self.data_dir = data_dir
        self.train_dir = train_dir
        self.test_dir = test_dir
        self.test_size = test_size

    def load_data(self):
        """データディレクトリから画像パスとクラスラベルを取得"""
        self.data = []
        self.labels = []
        for class_name in os.listdir(self.data_dir):
            class_path = os.path.join(self.data_dir,class_name)
            if os.path.isdir(class_path):
                for img_name in os.listdir(class_path):
                    img_path = os.path.join(class_path, img_name)
                    if os.path.isfile(img_path):
                        self.data.append(img_path)
                        self.labels.append(class_name)
        print(f"合計{len(self.data)}枚の画像を読み込みました。")

    def split_data(self):
        """データを訓練データとテストデータに分割する"""
        self.train_data, self.test_data, self.train_labels, self.test_labels = train_test_split(
            self.data, self.labels, test_size=self.test_size, stratify=self.labels, random_state = 42
        )
        print(f"訓練データ: {len(self.train_data)}枚, テストデータ: {len(self.test_data)}枚に分割しました。")

    def _save_split_data(self, data, labels, target_dir):
        """分割されたデータを保存する内部関数"""
        if not os.path.exists(target_dir):
            os.makedirs(target_dir)

            for img_path, label in zip(data, labels):
                label_dir = os.path.join(target_dir, label)
                if not os.path.exists(target_dir):
                    os.makedirs(target_dir)

                for img_path, label in zip(data, labels):
                    label_dir = os.path.join(target_dir, label)
                    if not os.path.exists(label_dir):
                        os.makedirs(label_dir)
                    shutil.copy(img_path, os.path.join(label_dir, os.path.basename(img_path)))

    def save_data(self):
        """訓練データとテストデータを指定ディレクトリに保存する"""
        self._save_split_data(self.train_data, self.train_labels, self.train_dir)
        self._save_split_data(self.test_data, self.test_labels, self.test_dir)
        print(f"データを {self.train_dir} と {self.test_dir} に保存しました。")

    def preprocess(self, size=(128, 128)):
        """前処理を行う(option)"""
        for img_path in self.data:
            img = Image.open(img_path)
            img = img.resize(size)
            img.save(img_path)
        print(f"すべての画像を{size}にリサイズしました。")