.. _label-lesson7:

===================================================
Lesson7: RAWディレクティブによるYoutube動画埋め込み
===================================================

   :保存ファイル名: lesson7.rst
   :必要な操作: ファイルの作成、編集

Webブラウザで表示させた状態で以降の行をテキストエディタにコピーの上、
レイアウト等を再現するよう編集してください。
(必要な画像はブラウザ上で右クリックの上保存して適宜配置してください)

   .. note::
      
      http://d.hatena.ne.jp/tk0miya/20111206 にて、sphinxcontrib.youtube
      という Sphinx 拡張でも実現が可能だとの記述があります。

   .. tip::

      youtube動画の埋め込みコードは[共有]>[埋め込みコード]から。


Google Chrome: Hatsune Miku (初音ミク) 
======================================

``raw`` ディレクティブを使うと、もっと凝ったことができる半面、
出力先メディアに依存する度合いが高くなってしまうので注意。

  * 元URL: http://www.youtube.com/watch?v=MGt25mv4-2Q

.. raw:: html

   <iframe width="560" height="315" src="http://www.youtube.com/embed/MGt25mv4-2Q" frameborder="0" allowfullscreen></iframe>


