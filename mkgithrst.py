# -*- coding: utf-8 -*-
#
# git logとるよ
#
import os
import sys

# Git実行パス
gitdir = r'"C:\Program Files\Git\bin\git.exe"'

fo = open('git_history.rst','w')

wl = u"""==============
Git history
==============

Git履歴。

git.exe log
==============

.. code-block:: none

"""

fo.write(wl)


lines= os.popen(gitdir+ ' log' ,"r")
sys.stdout.flush()

# MAX?
c_max = 10

c = 0

while 1:
    line = lines.readline()

    if not line:
        break
    
    if 'commit' in line > 0:
        
        if c >= c_max:
            break
        c = c + 1

#    wl = line + "\n"
#    fo.write(wl)
    print  >>fo,'   '+unicode(line, 'utf-8').rstrip()


print >>fo,""
print >>fo,u"現在、最新の" , c_max , u"件を表示中。" 

fo.close()   
