"""
 -*- coding: utf-8 -*-
 author： Hao Hu
 @date   2022/5/23 9:30 PM
"""
# totally free
from baidu_translate import TranslateClient
from time import sleep
from tqdm import tqdm
def analyse_txt():
    with open('./question.txt','r') as fp:
        contents = fp.readlines()
    en_list = []
    for sample in contents:
        tmp_sentence = sample[:-1]
        en_list.append(tmp_sentence)
    return en_list

def test():
    client = TranslateClient()
    print(client.auto2auto('你好, 这是个测试').text)
    print(client.zh2en('你好, 这是个测试').text)
    print(client.en2zh('Hello').text)


def translate_by_baidu(en_list):
    client = TranslateClient()
    en_zh_list = []
    for sample in tqdm(en_list):
        try:
            zh_sentence = client.en2zh(sample).text
            en_zh_list.append("{} *** {}\n".format(sample, zh_sentence))
            print(sample)
            print('***')
            print(zh_sentence)
            sleep(1.2)
        except:
            pass
    return en_zh_list

if __name__ == '__main__':
    
    en_list = analyse_txt()
    #test()
    en_zh_list = translate_by_baidu(en_list)
    with open('./en_zh_question.txt', 'w') as f:
        f.writelines(en_zh_list)
    
