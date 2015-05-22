# coding: utf-8

##Caesar暗号を生成/解読するスクリプト用のアルファベットリストの場合は冗長##
#alphabetList = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

##ASCIIコードを使用してアルファベットを生成する方法がスマート
#小文字が97から123までのxrange 大文字が65から91までのxrange
#alphabetTable = [chr(i) for i in range(ord('A'), ord('Z')+1)]
#alphabetTable = [chr(i) for i in xrange(97,123)]
alphabetTable = [chr(i) for i in xrange(65,91)]
print alphabetTable
