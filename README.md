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