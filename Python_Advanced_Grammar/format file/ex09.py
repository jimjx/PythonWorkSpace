# 导入相关包
import re

# 查找数字
# r表示字符串不转义 \d表示一个数字 +表示前面的内容至少出现一次
p = re.compile(r'\d+')
# 在字符串"one12twothree23423565four78"中进行查找,按照规则p制定的正则进行查找
# 参数3,26表示在字符串中查找的范围
m = p.match("one12twothree23423565four78", 3, 26)
m1 = p.match("45612a34abc")
# 返回结果是None表示没有找到,否则返回match对象
print(m)
# 找到的结果进行分组,而且只有一组
print(m[0])
# 可以查看匹配到的字符串从哪个位置开始的 m.start(0) 闭区间
print(m.start(0))
# 还可以查看匹配到的字符串从哪个位置结束的 m.end(0) 开区间
print(m.end(0))
print(m1)
# 上述代码说明的问题
# 1. match可以输入参数表示起始位置
# 2. 查找到的结果只包含一个,表示第一次进行匹配成功的内容
# 例如上面的m 从位置3开始找,虽然是要找完整个字符串到26位置,但是由于在3,4两个位置找到了数字(贪婪),就直接放弃查找了,直接返回结果
