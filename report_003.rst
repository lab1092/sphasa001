.. _label-report_003:

================================================
Sphinx朝会＠神戸 開催しましたよ #sphinxjp
================================================

開催後レポートです。参加された皆さんありがとうございました!!

http://blog.livedoor.jp/lab1092/archives/51761621.html


昨日、日曜日10：00から、Sphinx朝会＠神戸を開催しました。

http://atnd.org/events/25549


ご参加いただいた皆さん、ありがとうございました。

説明および演習に使った資料:
----------------------------

今回、説明資料は以下のものを使用しました。

    Sphinx朝会2012年3月にようこそ!!


自己紹介タイム：
----------------

それぞれ自己紹介していただきました。いろいろと他のコミュニティで活躍されている方が多くて「すげー」とかおもってしまったり。


キーワードとしては以下のようなものが出てたような。

   * PyConJP
   * PHPカンファレンス関西
   * 神戸ITフェスティバル
   * Android神戸
   * WordBench神戸
   * LibreOffice
   * OSC東京/OSC愛媛
   * blender

アンケート(3つ)：


今回自身も含めて9名の参加でした。3つほどアンケート取りました。

   * Python使ってますか? - 3名
   * 業務でドキュメント書いてますか - 6名
   * 勉強会等で発表されてますか - 8名

ほうほう。


Sphinxを使う最初の一歩:

ほとんどの方がSphinxの環境をインストールされていたようなので、ひとまず "make html"を行うまでを実演しました。

    説明資料 - http://dl.dropbox.com/u/3864210/sphasa001/part1.html#part1-sphinx


インストールの話題で出ていましたが、それぞれPythonやSphinxのインストール時に一筋縄ではいかなかったという意見があったようです(勉強会内では詳しく聞けませんでした)


あと、自分の環境には"make"コマンドが無いということだけ強調しておきました。開発をされる方は「XCodeのインストールはまず最初に行いますよねー」ということのようなので、「ﾃﾞｽﾖﾈｰ」とか言っておきましたｗ


こういうのを用意しとけば「makeが無くても安心」。

   :: 

      sphinx-build -b html -d _build/doctree . _build/html


演習:
-----

演習については前々回、前回と同じ資料を参照して行っていただきました。

まあ、演習の前からだったんですけど、ネットの接続が(WiMAX使用)不調で、ちょっと時間を取るはめに。

    説明資料 - http://dl.dropbox.com/u/3864210/sphasa001/part1.html#restructured-text

演習時間、とは言ってましたが、「おやつを食べたり」「イベントの紹介だったりしてたような気がしたり。

(これはUst流せないよねぇとか思いつつ)


演習はまずすべてこなせないということで、「おうち帰ってやりましょうね」的な。


S6テーマの紹介&雑談：
----------------------

今回はreSTを書いて"make html"すると、プレゼン資料が作れてしまう、S6テーマについて少しだけ触れました。

    Sphinxのテーマとして提供されてますよ。( http://pypi.python.org/pypi から入手してね)
    ローカルでうまく表示されないときは一行Webサーバを実行させてそちらにアクセスするといいよ

また、実際に作ったS6テーマの資料などを表示させてみたり。

.. raw:: html

   <div align="center"><iframe width="540" height="480" src="http://dl.dropbox.com/u/3864210/sphasa001/03kobe_pre/index.html" frameborder="1" allowfullscreen></iframe></div>

http://dl.dropbox.com/u/3864210/sphasa001/03kobe_pre/index.html


ちなみに、例の動画は友P( @tomo_ ) 制作。

.. raw:: html

   <iframe width="560" height="315" src="http://www.youtube.com/embed/Z8cUMsQFHp4" frameborder="0" allowfullscreen></iframe>



スライド中の最後の動画を全部流して「Sphinxと何のつながりがっ!?」というツッコミがあったり(→実はblender python APIのドキュメントはSphinxだし、BlenderはAddon用にPythonのエンジンを搭載している、ということで)

他に テーマの話やblockdiagの話などもありましたが、「簡単に触れた」程度にとどまりました。


どんどん脱線していくので面白かったと言えば面白かったんですが、ひとつ大事なものをわすれてまして。実は一部不完全ながらSymfony2のドキュメントをビルドするデモンストレーションをする時間が無くなっちゃいました。てへ。


ということで(?)、「楽しい」時間は過ごせたように思います。


そのあと(行ける方の)みランチ、という感じでした。


今回思ったこと:
----------------

 ｢マルチプラットホーム」対応のツールの説明はそれぞれの環境を多少知っていないと話をしにくい。あと、インストールにまつわるいろいろも「話として知っている」以上でないと。｢Windowsのみ対応」とかだとある程度決め打ちで話を進められるんですけどね。


あと、今回はものすごくいいタイミングで質問をもらったり、補足説明いただいたりと、参加しているみなさんに助けられました。改めてありがとうございます。


次回予定は未定：
-----------------

次は…。具体的な場所と日程はまだですが、「大阪」、「土曜」という要望が出てるらしいです。いい会場ご存知でしたらお知らせいただけるとありがたいです。


次回はテーマの変更やカスタマイズ、Sphinx拡張についての話題で行ければと思います。


あと、この「Sphinx朝会」については「ドキュメンテーションツール、Sphinxを愛でる」のが目的です。というところで。

.. raw:: html

   <embed type="application/x-shockwave-flash" src="https://picasaweb.google.com/s/c/bin/slideshow.swf" width="288" height="192" flashvars="host=picasaweb.google.com&amp;hl=ja&amp;feat=flashalbum&amp;RGB=0x000000&amp;feed=https%3A%2F%2Fpicasaweb.google.com%2Fdata%2Ffeed%2Fapi%2Fuser%2F111078457452695101816%2Falbumid%2F5715919913756109009%3Falt%3Drss%26kind%3Dphoto%26hl%3Dja" pluginspage="http://www.macromedia.com/go/getflashplayer"></embed>


Togetterでまとめられているようです。

    http://togetter.com/li/267615

