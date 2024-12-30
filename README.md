# System Info Publisher

このプロジェクトは、ROS2を使用してシステム情報（現在時刻とバッテリー情報）をトピックに発行するノードを実装しています。1秒ごとに情報を収集し、`system_info` トピックにメッセージを送信します。

## 必要条件

- Python 3.x
- ROS2 (Foxy, Galactic, Humble など)
- `psutil` ライブラリ

## インストール

1. **ROS2をインストール**: [ROS2の公式サイト](https://docs.ros.org/en/foxy/Installation.html)からインストール手順に従ってください。

2. **依存関係のインストール**:
   ```bash
   pip install psutil
	```
## プロジェクトのクローン
   ```bash
	git clone git@github.com:naoto7010oka/mypkg.git
	cd ros2	
## 使用方法
1. ROS2のワークスペースをビルド:
	ROS2のワークスペースにプロジェクトを追加しビルドします。
	```bash	
	colcon build
2. 環境をセットアップ:
	```bash
	source /opt/ros/<distro>/setup.bash
3. ノードを実行:
	```bash
	python3 system_info_node.py
	```
## コードの説明
1. SystemInfoPublisher クラスは、ROS2のノードを拡張し、1秒ごとにシステム情報を収集します。:
2. 現在時刻とバッテリーの状態を取得し、system_info トピックにメッセージを発行します。:

