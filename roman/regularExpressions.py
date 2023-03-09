import re
"""
ローマ数字をチェックする

- ローマ数字の文字種は7つ
I = 1
V = 5
X = 10
L = 50
C = 100
D = 500
M = 1000

- 上記以外の数字は，上記を足すか引くかで表す
    - 0はなく，最大3999
- 並んだ数字の読み方
    - 左から右へと読む．ICのような並びはあり得ない
    - 足し算：並んだ文字を足し算として読む III = I+I+I = 3 VIII = 8 
    - 引き算：並んだ2つの数字を，後ろの文字から前の文字を引く，引き算で読む． IX = I-X = 9
- 並べ方の制限
    - 10の基数（I, X, C, M）の繰り返しは，3回まで． 
    - 5の文字(V, L, D)は，繰り返すことができない．
    - 繰り返しで表せない場合は，次の上位の文字からの引き算で表す． IV = 5 - 1 = 4, IX = 10 - 1 = 9
"""

# 1000の位 M = 1000, MM = 2000, MMM = 3000の3パターン  必ず先頭，1〜3回の繰り返し，ない場合もある
#  100の位 C = 100(-300も同様), CD = 400, D = 500, DC = 600(-800まで同様), CM = 900
#   10の位 X = 10(-30も同様), XL = 40, L = 50, LX = 60(-80まで同様), XC = 90
#    1の位 I = 1(-3も同様), IV = 4, V = 5, VI = 6(-8も同様), IX = 9

targets = [
#    "",
#    "M", "MM", "MMM",
#    "CM", "CD", "DC", "DCC", "DCCC", "CCC", "CC", "C",
#    "XC", "XL", "L", "LX", "LXX", "LXXX", "X"
#    "IX", "IV", "VI", "I", "II", "III",
    "MMXIV", "MMXL", "MMXLIX"
]

roman_arabic = {
    'M': 1000,
    'D':  500,
    'C':  100,
    'L':   50,
    'X':   10,
    'V':    5,
    'I':    1
}

pattern = re.compile(r'''
    ^
    (M{0,3})
    (CM|CD|D?C{0,3})
    (XC|XL|L?X{0,3})
    (IX|IV|V?I{0,3})
    $
''', re.VERBOSE)

for target in targets:
    serparetedNumber = pattern.search(target).groups()
    print(serparetedNumber)        
