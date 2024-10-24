"""
データセットの読み込み
"""

from torchvision import datasets, transforms
from torch.utils.data import DataLoader

# 画像の前処理
transform = transforms.Compose([
    transforms.Resize((128, 128)),
    transforms.ToTensor(),
    transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))
])

train_dataset = datasets.ImageFolder(root='./data/project 18/train', transform=transform)
test_dataset = datasets.ImageFolder(root='./data/project 18/test', transform=transform)

#rでバッチ処理を行う
train_loader = DataLoader(train_dataset, batch_size=32, shuffle=True)
test_loader = DataLoader(test_dataset, batch_size=32, shuffle=False)

# クラス名を取得
class_names = train_dataset.classes
print(f"クラス名: {class_names}")



# データローダーからバッチを取得する例
for images, labels in train_loader:
    print(f"バッチ内の画像サイズ: {images.size()}")
    print(f"バッチ内のラベル: {labels}")
    break  # 最初のバッチのみ表示