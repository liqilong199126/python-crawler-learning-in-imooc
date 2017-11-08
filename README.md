# python-crawler-learning-in-imooc
慕课网 python crawler 学习总结

## 百度百科爬虫小项目

- 基于**Python 3.5.2**版本
- 使用IDE为**PyCharm**
- 引入第三方库为:**BeautifulSoup,re和urllib**(全部是在PyCharm中引入）

- 代码已加好注释，可帮助理解。

## 项目结构说明

- **baike_spider**文件夹为百度百科爬虫小项目

  - **spider_main.py**为入口文件，运行该文件即可

- **test**文件夹为测试第三方库**urllib**和**beautifulsoup4**的小例子


```
├── README.md
├── baike_spider
│   ├── __pycache__
│   │   ├── html_downloader.cpython-35.pyc
│   │   ├── html_outputer.cpython-35.pyc
│   │   ├── html_parser.cpython-35.pyc
│   │   └── url_manager.cpython-35.pyc
│   ├── html_downloader.py
│   ├── html_outputer.py
│   ├── html_parser.py
│   ├── output.html
│   ├── spider_main.py
│   └── url_manager.py
└── test
    ├── test_beautifulsoup4.py
    ├── test_urllib_01.py
    ├── test_urllib_02.py
    └── test_urllib_03.py
```


## 总结

修改以下代码，你就能抓取任何互联网网页！


```
root_url = "https://baike.baidu.com/item/Python/407313?fr=aladdin"

title_node = soup.find('dd', class_="lemmaWgt-lemmaTitle-title").find("h1")

summary_node = soup.find('div', class_="lemma-summary")
```


