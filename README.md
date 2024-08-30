# ALT_PRACTICE

## プロジェクト概要

このプログラムは、再帰的な構造を持つカスタム式を評価するためのPythonスクリプトです。式は特定のフォーマットに従っており、再帰的な評価や繰り返し処理をサポートしています。

## 式のフォーマット

式のフォーマットは以下の通りです：

```
<{count}|{sub_expression}{value}>
```

- **count**: 繰り返し処理の回数（整数）
- **sub_expression**: 再帰的に評価するサブ式（オプション）
- **value**: 繰り返し処理される値（文字列）

## クラスと関数の説明

### クラス `Expression`

`Expression`クラスは、入力された式を評価するためのクラスです。

- **`__init__`**: 入力式の妥当性を確認し、`count`、`sub_expression`、`value`の各メンバ変数を初期化します。入力が無効な場合は`ValueError`をスローします。
- **`evaluate`**: 式を評価し、結果を文字列として返します。

### 関数 `execute`

`execute`関数は、入力式の妥当性を確認し、`Expression`クラスを使用して式を評価します。評価中に例外が発生した場合は、例外メッセージを文字列として返します。

### 関数 `demonstrate`

`demonstrate`関数は、サンプルの入力を使ってプログラムの動作を示すために使用されます。評価結果をコンソールに出力します。

## 使用方法

このプログラムを実行するには、Python 3.12.4が必要です。以下のコマンドを使用してプログラムを実行できます。

```bash
python main.py
```

プログラムを実行すると、いくつかのサンプル入力が評価され、結果がコンソールに出力されます。

## 実行例

以下はプログラムの実行例です：

```plaintext
----------
input:  <30|A>
result: AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
----------
input:  <30a|Aa>
result: [ValueError] Invalid input: <30a|Aa>
----------
input:  <3|<12|B>A>
result: BBABBABBA
```

## エラー処理

- 無効な形式の入力が提供された場合、プログラムは`[ValueError]`を含むエラーメッセージを返します。

## テスト方法

pytest下でテストが可能です
```bash
pytest
```
テスト結果は```.\tests\pytest.log```
テストベクトルは```.\tests\test_patterns.csv```をご覧ください。

## 依存関係

pip,condaどちらからでも環境構築可能です。
以下のファイルを活用ください

* conda:    ```alt_practice.yml```,
* pip:      ```requirements.txt```

