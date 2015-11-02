from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.123yq.com/read/27/27930/")
bsObj = BeautifulSoup(html)
filename = bsObj.find("title")
realname = filename.text
str="G:\\{0}.txt".format((realname.split(','))[0])
text0 = ""
text1 = ""
text2 = ""
Title0 = ""
Title1 = ""
Title2 = ""
i = 1
f=open(str,'a',encoding='utf-8')
for link in bsObj.find("div", {"id":"list"}).findAll("a"):
    if 'href' in link.attrs:
        #print(link.attrs['href'])
        html = urlopen(link.attrs['href'])
        bsObj1 = BeautifulSoup(html)
        text = bsObj1.find("div", {"class":"zhangjieTXT"})
        Title = bsObj1.find("h1")
        n = i%3
        if n == 0:
            text0 = text.text
            text0 = text0.replace("\xa0\xa0\xa0", "\n")
            text0 = text0.replace("ads_wz_2();", "")
            text0 = text0.replace("投推荐票上一章章节目录下一章加入书签返回书架章节错误/点此举报", "")
            text0 = text0.replace("ads_wz_3();", "")
            Title0 = Title.text
        elif n == 1:
            text1 = text.text
            text1 = text1.replace("\xa0\xa0\xa0", "\n")
            text1 = text1.replace("ads_wz_2();", "")
            text1 = text1.replace("投推荐票上一章章节目录下一章加入书签返回书架章节错误/点此举报", "")
            text1 = text1.replace("ads_wz_3();", "")
            Title1 = Title.text
        elif n ==2:
            text2 = text.text
            text2 = text2.replace("\xa0\xa0\xa0", "\n")
            text2 = text2.replace("ads_wz_2();", "")
            text2 = text2.replace("投推荐票上一章章节目录下一章加入书签返回书架章节错误/点此举报", "")
            text2 = text2.replace("ads_wz_3();", "")
            Title2 = Title.text
        if n == 0:
            f.write(Title0)
            f.write(text0)
            f.write(Title2)
            f.write(text2)
            f.write(Title1)
            f.write(text1)
            text0 = ""
            text1 = ""
            text2 = ""
            Title0 = ""
            Title1 = ""
            Title2 = ""
        i = i + 1
if len(text2) != 0:
    f.write(Title2)
    f.write(text2)
if len(text1) != 0:
    f.write(Title1)
    f.write(text1)

f.close