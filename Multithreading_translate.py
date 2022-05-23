"""
 -*- coding: utf-8 -*-
 author： Hao Hu
 @date   2022/5/23 9:24 PM
"""
###if you don not care MONEY,use this script
#  多线程翻译
from translate import Translator

translator = Translator(to_lang="zh")
from tqdm import tqdm
import paramiko
from concurrent.futures import ThreadPoolExecutor


def analyse_txt():
    with open('./question.txt', 'r') as fp:
        contents = fp.readlines()
    en_list = []
    for sample in contents:
        tmp_sentence = sample[:-1]
        en_list.append(tmp_sentence)
    return en_list


def translate_english_to_chinese(tmp_sentence):
    """将英文翻译成中文"""
    en_zh_list = []
    translation = translator.translate(tmp_sentence)
    en_zh_list.append("{} *** {}".format(tmp_sentence, translation))

    return en_zh_list


if __name__ == '__main__':
    en_list = analyse_txt()
    executor = ThreadPoolExecutor(max_workers=20)
    en_zh_list = [executor.submit(translate_english_to_chinese, (tmp_sentence)) for tmp_sentence in en_list]
    end_list = []
    for sample in en_zh_list:
        end_list.append("{}\n".format(sample.result()[0]))

    with open('./en_zh_question.txt', 'w') as f:
        f.writelines(end_list)

