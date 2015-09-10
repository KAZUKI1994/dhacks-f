# dhack-f
This is the f team. 
Our team name is *"Hickeys"*.
私たちは、「ヒッキーズ」です。DIT主催の同志社大学生限定ハッカソンDHACKS用のGitHub

#仕様詳細
##バイト情報データベースフィールド
| label            | var        | field         | input[type] | detail                   |
|------------------|------------|---------------|-------------|--------------------------|
| タイトル         | title      | CharField     | text        | 学内バイト募集タイトル   |
| カテゴリー       | category   | CharField     | text        | choices                  |
| 募集者           | publisher  | CharField     | text        |                          |
| 募集者電話       | pub_phone  | IntegerField  | tel         |                          |
| 募集者メール     | pub_mail   | EmailField    | email       |                          |
| 募集内容         | content    | TextField     | textarea    | 500文字以内              |
| 募集条件         | condition  | CharField     | text        | 例：男性1年など          |
| 募集校地         | canvas     | CharField     | checkbox    | 今出川or京田辺           |
| 場所             | location   | CharField     | text        | 校舎・教室               |
| 勤務期間         | work_period | CharField     | text        | バイトで実際働いてもらいたい期間 |
| 締め切り         | dead_line  | DateField     | date        | 募集締め切り期間         |
| 対応可能時間     | can_time   | DateField     | radio       | choices                  |
| 報酬             | pay        | CharField  | number      | 図書券とか時給とか       |
| アイキャッチ画像 | top_image  | FilePathField | radio       |                          |
##ユーザー登録
登録者は、「バイト募集者」「バイト情報掲載者」両方。  
###バイト募集者の対応
バイト募集者の普段いる校地やほしい給料などに合わせて一覧できる情報や流れてくるメールマガジンが変わるように設定したい。

###バイト情報掲載者の対応
バイト掲載者の場合、ログインしていたり登録済みの画面状態では入力フォームがすでに入力されている状態に設定したい。  
ifでユーザー情報を確認しログインされている状態であれば、すでに入力しておくというロジック  
また、一度掲載した後も変更があった際に変更できる管理画面が必要

##管理用
###変数
- "new_archieve_list": 募集終了期間がもっとも近いものからリストアップした10のバイトリスト

###カテゴリー
- 被験者バイト
- 生協バイト
- 赤ジャン
- 授業補助
- イベント

