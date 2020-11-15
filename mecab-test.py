#(C)Tsubasa Kato 2020/11/16
#Parts of code from: https://qiita.com/osyou84/items/c7864a5200238d8678aa
import sys
import MeCab
import html
#Make Mecab split words (wakati)
m = MeCab.Tagger ("-Owakati")
text = input(">>")
#sanitize input
text = html.escape(text)
#print the inputted words / text
print(m.parse(text))
