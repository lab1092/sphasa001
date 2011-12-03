# base_po2tsv.py 
# 
# usage:
#  1. copy this file and ahoy2-20110823.po on same directory.
#  2. python po2tsv.py
#
# copy following 2 lines C:\Python26\Lib\site-packages\sitecustomize.py
#  
#  import sys
#  sys.setdefaultencoding("utf-8")
#

infilename = "ahoy2-20110823.po"
outfilename = "index.rst"

linetags = ( "msgid","msgstr" )

flg=0

key = u""
note = u""
buf = []

fi = open(infilename)
foo = open(outfilename,"w")

print >> foo , "Welcome to podiff's documentation!"
print >> foo , "=================================="
print >> foo , ""
print >> foo , "Contents:"
print >> foo , ""
print >> foo , ".. toctree::"
print >> foo , "   :maxdepth: 1"
print >> foo , ""

def filerst(msg,cnt):

    outfilename = str(cnt).zfill(6) + ".rst"


    fo = open(outfilename,"w")

    print >> fo, "==========================="
    print >> fo, str(cnt) + "‚©‚ç["
    print >> fo, "==========================="
    print >> fo, ""
    print >> fo, ""
    print >> fo, msg
   
    fo.close()

    print >> foo , "   " + str(cnt).zfill(6)

#----------------

def writetorst(podict,tags,key,mcnt):

    buf = []

    
    buf.append(str(mcnt))
    buf.append('-------------')
    buf.append('')

    if podict.has_key(key):
       buf.append( '.. _L'+ str(podict[key]).zfill(6) +'-label:\n')
    else:
       buf.append('')
    

    
    for tag in tags:
        if podict.has_key(tag):
            buf.append('   ::\n')
            
            flg = 0
            for line in podict[tag]:
                if line.strip() == "":
                    flg = 1
                if line.startswith('Last-Translator:'):
                    buf.append('      Last-Translator:')
                else:
                    buf.append('      ' + line)
            if flg== 1:
                buf.append('      [Empty]')
            buf.append('')
        else:
            buf.append('')

    msg = '\n' + '\n'.join(buf) + '\n'

    return msg

#---------------

lnum = 1        # linenumber
mcnt = 1        # message count (= pootleid???)
podict = {}
curtag = ""
flg =0

pagelen = 1000
pagecnt = 0

c = 1

msg = ""

for line in fi:


    if line.strip() == '':
        
        if podict.has_key('lnum'):
            msg = msg + writetorst(podict,('msgid','msgstr'),'lnum',mcnt)
            mcnt = mcnt + 1
        
        podict = {}
        curtag = ''
    else:
        flg =0
        for tag in linetags:
            if line.startswith(tag+' '):
               if tag == 'msgid':
                  podict['lnum'] = lnum
               s = line[len(tag):].strip().strip('\x22')
               podict[tag] = [s]
               curtag = tag
               flg =1
               break
        
        if curtag != '' and flg == 0:
            s = line.strip().strip('\x22')
            podict[curtag].append(s)
    

    
    if (mcnt % pagelen ) == 0 and msg != "":
        filerst(msg,pagecnt)
        pagecnt = pagecnt +pagelen
        msg = ""

    lnum = lnum +1

if podict.has_key('lnum'):
    msg = msg + writetorst(podict,('msgid','msgstr'),'lnum',mcnt)

if mcnt > pagecnt :
    filerst(msg,pagecnt)
    print pagecnt

print >> foo , ""
print >> foo , "Indices and tables"
print >> foo , "=================="
print >> foo , ""
print >> foo , "* :ref:`genindex`"
print >> foo , "* :ref:`search`"
