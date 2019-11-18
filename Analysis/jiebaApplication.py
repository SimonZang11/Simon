import jieba
import pandas as pd
import json

dict_address = r'D:\py_code\Analysis\mydict.txt'
address = r'C:\Users\Wellempc07\Desktop\result.xls'
jieba.load_userdict(dict_address)
excel_file = pd.read_excel(address)
row1 = excel_file.loc[0]  # 第一行数据
tip = row1.values[4]  # 收费小贴士
item = row1.values[5]  # 收费项目
check = row1.values[9]  # 查体
dia = row1.values[11]  # 诊断
stopwords = ["'", ",", "（", "）", "[", "]", " ", "，", "。", "、"]


def segment(text):
    seg_list = jieba.cut(text, cut_all=False)
    final = ''
    for seg in seg_list:
        if seg not in stopwords:
            final += seg
    final = jieba.lcut(final, cut_all=False)
    return final


def trans(data):
    # if isinstance(data, list):
    #     if data[1] == "'":
    #         data = data.replace("'", '"')
    #     result = json.dumps(data)
    #     return result
    if data[1] == "'":
        data = data.replace("'", '"')
    result = json.loads(data)
    return result
