## chapter1 python基础

## chapter2 控制流

## chapter3 函数

## chapter4 列表

## chapter5 字典和结构化数据

## chapter6 字符串操作

6.1.5

6.1.6 多行注释

    """  """

6.1.7 字符串下标和切片

    字符串像列表一样，使用下标和切片。可以将字符串看成是一个列表，字符串中的每个字符都是一个表项，有对应的下标

6.1.8 字符串的 in 和 not in 操作符

    像列表一样，in 和 not in 操作符也可以用于字符串。用 in 或 not in连接两个字符串得到的表达式，将求值为布尔值 True 或 False

### 6.2 有用的字符串 

6.2.1 upper()、lower()、isupper()、islower()

    upper()将字符串转变为大写
    lower()将字符串转变为小写
    注意：这些方法并没有改变字符串本身，而是返回一个新字符串

    isupper()判断字符串内容是否全部为大写，返回布尔值
    islower()判断字符串内容是否全部为小写，返回布尔值

6.2.2 isX 字符串方法

- isalpha(), 如果字符串只包含字母，并且非空，返回True
- islnum(), 如果字符串只包含字母和数字，并且非空，返回True
- isdecimal(), 如果字符串只包含数字字符，并且非空，返回True
- isspace(), 如果字符串只包含空格、制表符和换行，并且非空，返回True
- istitle(), 如果字符串仅包含以大写字母开头、后面都是小写字母的单词，返回True

6.2.3 字符串方法 startswith()和 endswith()

    检查字符串的开始或结束部分
    如果它们所调用的字符串以该方法传入的字符串开始或结束，返回True，否则返回False

6.2.4 字符串方法 join()和 split()

    join() 将一个字符串列表连接，成为一个单独的字符串
    注意，调用join()方法的字符串，被插入到列表参数中每个字符串的中间。
    例如，在','字符串上调用join(['cats','rats','bats'])，返回的字符串是'cats,rats,bats'
    ','.join(['cats','rats','bats'])

    split()对一个字符串调用，返回一个字符串列表。
    默认情况下，字符串按照各种空白字符分割，如空格、制表符或换行符。这些空白字符不包含在返回列表的字符串中。
    也可以向split()方法传入一个分割字符串，指定按照不同的字符串分割。

6.2.5 用rjust()、ljust()和center()方法对齐文本