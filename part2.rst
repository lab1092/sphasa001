.. _label-part2:

====================================
Sphinxその他もろもろ
====================================

Tips
====

make-html.bat
-------------

Windowsユーザーはバッチファイル書くといいよ。

ドキュメントディレクトリに以下の行を書いてあげると ``make html`` のあとにブラウザ開いてくれます。

::

   call .\make.bat html

   .\_build\html\index.html


Macユーザーで XTools インストールしていない人は ``make html`` できないので、 make-html.sh でも書いておけばいいよ。

:: 
   
   sphinx-build -b html -d _build/doctree . _build/html

.. note::

   ``make clean`` も同様に.bat / .sh 書いておくといいよ。

::

   call .\make.bat clean


::

   rm -rf _build/html/*



S6形式のプレゼンテーション資料
-------------------------------

こういうやつです。

   http://dl.dropbox.com/u/3864210/sphasa001/03kobe_pre/index.html

これをローカル環境で開くと、Webブラウザのセキュリティ設定によっては正しく表示されないことがあります。

解消するには、ブラウザの設定を変更するか、Python入っている環境であれば「一行webサーバ」を立てます。
( http://mojix.org/2009/03/05/python_one_line_fileserver )

::

   python -m SimpleHTTPServer 8080 


拡張など
========


CSS見栄えの変更
---------------

テーマを変えることも可能です。

ad hocな変更であれば、テーマで使っている CSS ファイルを _static にコピペして編集します。

.. note::

   .jsも _static にコピペすると…


blockdiagなど
-------------

http://pypi.python.org/pypi に行って、 ``blockdiag`` で検索してみてください。



rst2pdf
-------------

なにげにハードル高いです。Windows であれば Python 2.6x + Sphinx + PIL 1.1.6 + ReportLab 2.5 の組み合わせがいいかも。

DocUtils 0.8ではエラーが出るので対処が必要になる模様

   * sphinx make pdf でエラーになる件 - うまい棒blog
      * http://d.hatena.ne.jp/hogem/20120113/1326463395

rst2odf
-------------

rst2odf でOpenOffice.orgで採用されている .odt 形式を作成(変換可能)です。

   * reSTからPDFにする(JODConverter経由で)
      * http://blog.livedoor.jp/lab1092/archives/51727259.html

make htmlhelp
--------------

``make htmlhelp`` を実行して、.chmファイルを作成したときについて

   * http://blog.livedoor.jp/lab1092/archives/51735420.html

pandoc
-------

いろいろなマークアップを変換出来る *pandoc*

http://johnmacfarlane.net/pandoc/

   * UTF-8 を前提に処理しているっぽいので事前に適宜文字コード変換すること
   * 相互変換出来ないマークアップありますので方向に破棄をつけてください。
   * HTML -> reST は結構微妙
   



