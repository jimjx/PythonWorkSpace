# coding=gbk
import shutil
import zipfile
import random
# shutil ģ�鷽������
# copy() �����ļ�
rst = shutil.copy("F:\PythonWorkSpace\pest.txt","F:\PythonWorkSpace\jim\pest1.txt")
print(rst)
# copyfile()
shutil.copy("F:\PythonWorkSpace\pest.txt","F:\PythonWorkSpace\jim\pest1.txt")

# help(shutil.make_archive)
# ��õ�һ������guidang.my�Ĺ鵵�ļ�
ma = shutil.make_archive("F:\PythonWorkSpace\guidang","zip","F:\PythonWorkSpace\jim")
print(ma)

# zipfile������
zf = zipfile.ZipFile("F:\PythonWorkSpace\yasuo.zip")

# ��ȡzip�ĵ���ָ���ļ�����Ϣ,����һ��zipfile.ZipInfo����,�����ļ�����ϸ��Ϣ
print(zf.getinfo("pest1.txt"))

# ZipFile.namelist()
# ��ȡzip�ĵ��������ļ��������б�
nl = zf.namelist()
print(nl)

# ZipFile.extractall([path[,members[,pwd]]])
# ��ѹzip�ĵ��е������ļ�����ǰĿ¼������members��Ĭ��ֵΪzip�ĵ��������ļ������б�
rst = zf.extractall("F:\PythonWorkSpace")

# random����������һ��0-1�����С��
print(random.random())
# random(a,b),����a��b֮���һ���������,����ұ�
print(random.randint(1,100))
# choice() ������������е�ĳ��ֵ
l = [str(i)+"haha" for i in range(10)]
print(l)
rss = random.choice(l)
print(rss)

# shuffle() ����ԭ����,������һ��None
l1 = [i for i in range(10)]
print(l1)
l2 = random.shuffle(l1)
print(l1)
print(l2)
