.. _label-lesson0:

====================================
Lesson0:この演習について
====================================

さて皆さんの大好きな演習です。この時点で

   * Sphinxのインストール
   * プロジェクトの作成
   * はじめての `make html`

は済んでいるものと思われます。作成したSphinxプロジェクトに内容を追加して
いきましょう。

どのように進めていくのですか？
=====================================

演習ファイルの作成
------------------

lesson1～lessonX に移動すると、以下のような表示があります。以下の指示が
書かれている1行あるものは、この文が書かれたよりもり後の行の本文部分を
テキストエディタでコピーして、所定のファイルを作成して、ソースディレク
トリに保存してください。

   ::

      Webブラウザで表示させた状態で以降の行をテキストエディタにコピーの上、
      レイアウト等を再現するよう編集してください。

そのファイルに対して、reSTructured Text 形式でマークアップしていきます。


サンプル(テキストコピー後)
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Webブラウザからコピーする箇所を選択し、あらかじめ開いておいたテキスト
エディタにコピーします。Webブラウザ上で装飾された表示については装飾
無しのテキストとして貼り付けられます。

   ::

      reSTructured Text サンプル

      これはreSTructured Textです。

           インデントされた行はこう書きます、

         reSTructured Text はインデントが命です。

      サンプル終わり


マークアップ後サンプル
~~~~~~~~~~~~~~~~~~~~~~

上記をマークアップすると以下のようになります。

   ::

      reSTructured Text サンプル
      ==========================

      これはreSTructured Textです。

         インデントされた行はこう書きます、

         * reSTructured Text はインデントが命です。

      サンプル終わり


index.rstを編集して、make
-------------------------

たとえば、最初の演習が終わって"lesson1.rst"を作成出来たら、index.rstに
"lesson1"を加えます。

これを

   ::

      .. toctree::
         :maxdepth: 2

こうします。

   ::

      .. toctree::
         :maxdepth: 2
      
         lesson1

index.rstを作成し終えたら、"make html"してみます。

結果はどのようになったでしょううか。表示が演習で提示されたものと同じに
なったら次に進みます。


インデント、ディレクティブおよびロール
======================================

インデント、ディレクティブおよびロールについての説明については、

   * http://sphinx-users.jp/doc10/rest.html#rst-primer

に記載がありますのでそちらを確認してください。





演習
====

では、Lesson1からはじめてみましょう。

Lesson 1:

   :doc:`lesson1`

   .. tip::

      HTML表示の場合は次へ進むには、"Next Topc"のリンクをクリックして
      進めるといいですよ。


Lesson 2:

   :doc:`lesson2`


Lesson 3:

   :doc:`lesson3`

Lesson 4:

   :doc:`lesson4`

Lesson 5:

   :doc:`lesson5`

Lesson 6:

   :doc:`lesson6`


Intermediate
------------

さて、ここまでの演習で基本的なreSTructured Textの書き方はマスター出来
ましたね。

これまでに覚えたマークアップでおそらく以下のようなものを記述できるよう
になると思います。見出し、パラグラフ(インデント)、リンク等々…。

(文字の装飾は適当に解釈することにしますw)

   * `Internet Explorer 7 リリース ノート <http://msdn.microsoft.com/ja-jp/ie/aa740486>`_
   * `Flash Player 11.1 および AIR 3.1 ユーザーリリースノート <http://kb2.adobe.com/jp/releasenotes/923/cpsid_92359.html>`_



もちろん `reSTructured Text <http://docutils.sourceforge.net/rst.html>`_
のマークアップはもっと様々な種類がありますが、今回はこの辺で。

   さらに `reStructuredText Markup Specification <http://docutils.sourceforge.net/docs/ref/rst/restructuredtext.html>`_
   を参照するといいかもしれません。
