.. _label-part1:

10:00 -10:40 - 第一部:ハンズオン

Part1.はじめてのSphinx
========================

今回はSphinxプロジェクトの基本を学んでもらいます。


Sphinxのインストール
------------------------

最初に、お使いのPCにPythonがインストールされていることを確認してください。
コマンドラインから以下のように入力してください。

   ::

      python -V

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


Sphinxプロジェクトの作成
------------------------

では、任意の個所にプロジェクトのディレクトリを作成します。
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

では、出力されたHTMLを見てみましょう。
コマンドラインから以下のように入力してください。またはブラウザで直接ファ
イルを開きます。

Windowsだとこんな感じ。

   ::

      start _build\html\index.html

FireFoxがインストールされ、コマンドラインから起動可能であれば以下のよ
うなコマンドを入力することでブラウザを開くことが出来ます

   .. note::

      `make html` の出力するメッセージを注意深く観察してみましょう。

   .. note::

      `make html` をもう一度実行して、メッセージが変わるか確認してみま
      しょう。

   ::

      firefox _build/html/index.html &

どのような内容が表示されたでしょうか。


はじめてのreSTructured Text
---------------------------
