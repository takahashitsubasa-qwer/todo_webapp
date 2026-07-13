良い選択だと思います。ToDoアプリはシンプルですが、**Webアプリ開発で必要な技術が一通り詰まっています。**

## 完成イメージ

**Streamlit（画面）**

```
-----------------------------
📝 ToDoアプリ
-----------------------------

タイトル
[________________]

優先度
(高・中・低)

[追加]

-----------------------------

□ FastAPIを勉強する
優先度：高

[完了] [編集] [削除]

-----------------------------

☑ Python課題
優先度：中

[未完了] [編集] [削除]
```

---

## 最初はリストで管理

```python
todos = [
    {
        "id": 1,
        "title": "FastAPIを勉強",
        "priority": "高",
        "done": False
    }
]
```

FastAPIではこのリストを操作します。

---

## API一覧

| メソッド   | URL                | 内容       |
| ------ | ------------------ | -------- |
| GET    | `/todos`           | 一覧取得     |
| POST   | `/todos`           | 新規追加     |
| PUT    | `/todos/{id}`      | 編集       |
| DELETE | `/todos/{id}`      | 削除       |
| PATCH  | `/todos/{id}/done` | 完了・未完了切替 |

この5つが実装できれば、CRUDの基本はほぼ身につきます。


---

## 開発する順番

### ① FastAPIだけ作る

まずはAPIを完成させます。

```
GET
POST
PUT
DELETE
PATCH
```

PostmanやSwagger UIで動作確認します。

---

### ② Streamlitを作る

APIを呼び出して

* 一覧表示
* 追加
* 編集
* 削除

ができるようにします。

---

### ③ 検索機能

```
FastAPI
↓

GET /todos?keyword=python
```

タイトル検索を実装します。

---

### ④ 優先度

```
高
中
低
```

並び替えもできるとさらに実践的です。

---

### ⑤ MySQLへ変更

リスト

↓

```python
todos = [...]
```

を

```
MySQL
```

へ置き換えるだけです。

テーブルはこんな感じになります。

| id | title   | priority | done  |
| -- | ------- | -------- | ----- |
| 1  | FastAPI | 高        | False |

FastAPI側のAPIはほとんど変更せず、データの保存先だけを変更するイメージです。

---

## このアプリで学べること

* FastAPIのCRUD
* Pydanticによるデータ検証
* HTTPメソッド（GET・POST・PUT・DELETE・PATCH）
* StreamlitからAPIを呼び出す方法
* JSONのやり取り
* MySQLへの移行
* （発展）SQLAlchemyなどのORM

---

このToDoアプリを最後まで作れるようになると、次に「家計簿」「在庫管理」「学習管理」なども同じ構成で作れるようになるので、Webアプリ開発の基礎力がかなり身につきます。



https://docs.streamlit.io/develop/api-reference/layout/st.bottom