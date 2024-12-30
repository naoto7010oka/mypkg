# System Info LIstener

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
   mkdir -p ~/ros2_ws/src
   cd ~/ros2_ws/src
   git clone https://github.com/naoto7010oka/ros2.git

   ```	
## 使用方法

1. ROS2のワークスペースをビルド:
   ROS2のワークスペースにプロジェクトを追加しビルドします。
   ```bash	
   cd ~/ros2_ws
   colcon build
   ```
2. 環境をセットアップ:
   ```bash
   source /opt/ros/<distro>/setup.bash
   ```
3. ノードを実行:
   ```bash
   ros2 run system_info_node system_info
   ```
4. 出力例:
   ```bash
   [INFO] [1672599600.123456]: Current Time: 2024-12-30 12:00:00
   [INFO] [1672599600.123456]: Battery: 85% (Plugged in: True)
   ```
## テスト
   このプロジェクトには、github actionsを使用したテストワークフローが含まれています。
## テストの実行
   ローカル環境でテストを実行するには以下のコマンドを使用します
   ```bash
   pytest test_system_info_node.py
   ```
## GitHub Actions
　pushまたはpullリクエストが行われると、以下のことを自動的にテストします。
　- 現時刻のフォーマット
　- バッテリーの残量
## コードの説明
1. SystemInfoPublisher クラスは、ROS2のノードを拡張し、1秒ごとにシステム情報を収集します。:
2. __init__ メソッド:
   - ノードの名前を 'system_info_publisher' として初期化します。
create_publisher メソッドを使って、String 型のメッセージを system_info トピックに発行するパブリッシャーを作成します。
   - タイマーを設定し、1秒ごとに publish_info メソッドを呼び出します。
3. publish_info メソッド:
   - datetime モジュールを使用して現在時刻を取得し、フォーマットします。:
   - psutil.sensors_battery() を使用してバッテリーの残量と充電状況を取得します。バッテリー情報がない場合は適切に処理します。
   - 現在時刻とバッテリー情報を含むメッセージを作成し、publish メソッドを使ってトピックに発行します。
   - 発行した内容をログに出力します。
4. main関数
   - rclpy.init() でROS2を初期化し、ノードをスピンさせて実行します。:
   - キーボード割り込みが発生した場合、ノードを適切にシャットダウンします。:
## 著作権　ライセンス
 - このソフトウェアパッケージは３条項BSDライセンスのもと、再頒布および使用が許可されます。
 - © 2024 Naoto Oka
