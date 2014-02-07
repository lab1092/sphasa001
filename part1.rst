.. _label-part1:

10:20 -10:40,10:50-11:30 - ハンズオン

Part1.はじめてのSphinx
========================

今回はSphinxプロジェクトの基本を学んでもらいます。

この内容は http://dl.dropbox.com/u/3864210/sphasa001/part1.html で確認可能

Sphinxのインストール
------------------------

   .. note::
      
      2014.2現在の Python のバージョンは 3.3.3


最初に、お使いのPCにPythonがインストールされていることを確認してください。
コマンドラインから以下のように入力してください。

   ::

      python -V


出力結果の例はこちら。

   .. code-block :: bat
   
      C:\Users\manda>python -V
      Python 2.6.1


インストールされていなければPythonをインストールします(各OSに合わせたも
のをpython.org等から入手してください)。

   例: http://sphinx-users.jp/gettingstarted/install_windows.html

   .. tip::

      WindowsでPDF出力したい、という場合にはPILバイナリの絡みでPython 2.6
      かも…


Sphinx(1.0以上)をインストールします。インストールの方法についてはいくつ
かあります。

   * OSのパッケージマネージャを利用する方法
   * easy_install を利用する方法


   .. note:: setup_toolsのインストール

      こちらのページをよく読んで導入してください。

      http://pypi.python.org/pypi/setuptools

   .. note:: 環境によっては

      シンボリックリンクをを作成するなどが必要な様子。

      http://pocketstudio.jp/log3/2012/02/22/sphinx_handson_3/


Sphinxプロジェクトの作成
------------------------

では、任意の個所にプロジェクトのディレクトリ( :term:`ソースディレクトリ`
と呼ばれます)を作成します。

`sphinx-quickstart` コマンドを実行し、適宜内容を入力します。

   :: 

      mkdir myproject
      cd myproject
      sphinx-quickstart


   .. list-table:: 入力が必要な項目(他はEnterで)
      :widths: 40, 60
     

      * - Project name
        - <プロジェクト名>
      * - Author name(s)
        - <著者名>
      * - Project version
        - <"0.01"とでも>


入力が終わるとディレクトリといくつかのファイルが出来ているはずです。


はじめての"make html"
---------------------

`sphinx-quickstart` のあとは `make html` です。

コマンドラインから以下のように入力してください。

   ::

      make html

さて、コマンドラインにいろいろ表示されました。最後のほうに以下のような
メッセージが表示がされていれば成功です。

   ::

      build succeeded.
      
      Build finished. The HTML pages are in _build/html.

では、出力されたHTMLを見てみましょう。Webブラウザでファイルを開きます。

Windowsだと、プロジェクトディレクトリ上から以下のコマンドを実行すること
でブラウザを開いて表示することが可能です。

   ::

      start _build\html\index.html


   .. note::

      `make html` の出力するメッセージを注意深く観察してみましょう。

   .. note::

      `make html` をもう一度実行して、メッセージが変わるか確認してみま
      しょう。

どのような内容が表示されたでしょうか。

   .. note::

      エラーが出た場合にはメッセージの内容をよく確認してください。


演習問題:はじめてのreSTructured Text
------------------------------------

では、以下の演習問題を。先ほど作成したプロジェクトにファイルを追加し、
index.html の `.. toctree::` の行の下に対応するファイル名を記述した上で
`make html` しながら進めてみてください。

   .. toctree::
      :maxdepth: 1

      part1/lesson0
      part1/lesson1
      part1/lesson2
      part1/lesson3
      part1/lesson4
      part1/lesson5
      part1/lesson6



   .. note::

      `show source` でreSTructured Textで記述された元のファイルの内容を
      確認出来ます。

さて、上記は全て終わったでしょうか。上記が終わると一つプロジェクトが
出来上がっているはずです(内容的にはあまり大したことは無いですが)。
おめでとう。

   .. note::

      上記レッスンについて、どのような文書をターゲットにしているか、を記載しておきます。参考まで。

      * Lesson4まで修了: プレスリリースのような タイトルおよび本文のマークアップ
   
         * ex. http://www.businesswire.jp/portal/site/jp/home/ 

      * Lesson6まで修了: リリースノートとか
   
         * http://msdn.microsoft.com/ja-jp/ie/aa740486
         * http://kb2.adobe.com/jp/releasenotes/923/cpsid_92359.html


演習問題:Extra!!
------------------------------------

"ちょっと物足りない"という場合には以下もどぞー。

   .. toctree::
      :maxdepth: 1

      part1/lesson7
      part1/lesson8

   .. note::

      Lesson 7 および 8 は、HTMLの表示の拡張、です。