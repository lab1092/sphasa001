.. _label-lesson8:

===================================================
Lesson8: クラスとアドホックなデザインの変更
===================================================

   :保存ファイル名: lesson8.rst
   :必要な操作: rstファイルの作成、編集


Webブラウザで表示させた状態で以降の行をテキストエディタにコピーの上、
レイアウト等を再現するよう編集してください。
(必要な画像などはブラウザ上で右クリックの上保存して適宜配置してください)

   * 今回のコピー対象は「"はんこ"を押すところを作ってみよう」から。

今回の演習は以下のファイルにを使用します。右クリックでファイルに保存
し、プロジェクトディレクトリの、 ``\_static`` フォルダにコピーします。

   * `default.css <../_static/default.css>`_

次に以下の追加コードを default.css も追加します。

追加コード::

   table.custom-right {
       margin-left:auto;
   }
   
   table.custom-right th {
       font-weight: bold;
       border: 1px solid #000;
   }
   
   table.custom-right tbody td {
       border: 1px solid #000;
   }
   
   
   table.stamp-table-right {
       margin-left:auto;
   }
   
   table.stamp-table-right th {
       font-size: 0.6em;
       font-weight: bold;
       text-align: center;
       border: 1px solid #000;
       width: 80px;
   }
   
   table.stamp-table-right tbody td {
       border: 1px solid #000;
       height: 80px;
       width: 80px;
   }
   
   table.stamp-table-center {
       margin-left:auto;
       margin-right:auto;
   }
   
   table.stamp-table-center th {
       font-size: 0.6em;
       font-weight: bold;
       text-align: center;
       border: 1px solid #000;
       width: 80px;
   }
   
   table.stamp-table-center tbody td {
       border: 1px solid #000;
       height: 80px;
       width: 80px;
   }

上記を追加出来たら保存し、 ``make clean`` を実行し、 ``make clean``
でHTMLを作成します。



"はんこ"を押すところを作ってみよう
====================================

これまで学習したマークアップのうち、テーブルなど、独自にクラス
を設定出来るものがあります。

::

   .. table:: 
      :class: stamp-table-center
   
      +--------+---------+
      | 検収印 | 確認印  |
      +========+=========+
      |        |         |
      +--------+---------+


.. table:: 
   :class: stamp-table-right

   +-----------+-----------+-----------+-----------+-----------+
   | 回覧                                                      |
   +-----------+-----------+-----------+-----------+-----------+
   | 部長印    | 副部長印  | 係長印    | 主任印    | 本人印    |
   +===========+===========+===========+===========+===========+
   |           |           |           |           |           |
   +-----------+-----------+-----------+-----------+-----------+



.. table:: 
   :class: stamp-table-center

   +--------+---------+
   | 検収印 | 確認印  |
   +========+=========+
   |        |         |
   +--------+---------+


