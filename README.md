# 起名助手

- 简体、繁体、拼音
- 百度记录数
- 互动百科记录数
- PCbaby 打分
- 名字常见性分析
- 建立字典索引

## How to use

### quick start

用法: `./qm.py --test`

```
+------+--------+--------+----------------+--------------+----------+-------+------+---------------+-------------------------------------------------------+
| 序号 | 简体   | 繁体   | 读音           | ID           | 百度     | 百科  | 打分 | 分析          | 释义                                                  |
+------+--------+--------+----------------+--------------+----------+-------+------+---------------+-------------------------------------------------------+
| 0    | 孙中山 | 孫中山 | sūn zhōng shān | sunzhongshan | 17800000 | 19071 | 51   | 0.004 大众名  | 山〈名〉 (象形。甲骨文和金文字形,象山峰并立的形状。山 |
| 1    | 戴笠   | 戴笠   | dài lì         | daili        | 11200000 | 1576  | 70   | 0.0 稀有名    | 笠〈名〉 (形声。从竹,立声。本义笠帽,用竹箬或棕皮等编  |
| 2    | 杨利伟 | 楊利偉 | yáng lì wěi    | yangliwei    | 5550000  | 841   | 69   | 0.0093 大众名 | 伟  (形声。从人,韦声。本义高大;壮美) 同本义           |
| 3    | 曹植   | 曹植   | cáo zhí        | caozhi       | 13700000 | 9808  | 83   | 0.0001 普通名 | 植  (形声。从木,直声。本义关闭门户用的直木) 同        |
| 4    | 李小龙 | 李小龍 | lǐ xiǎo lóng   | lixiaolong   | 12900000 | 4016  | 61   | 0.0091 大众名 | 龙  (象形。甲骨文,象龙形。本义古代传说中一种有鳞有须  |
+------+--------+--------+----------------+--------------+----------+-------+------+---------------+-------------------------------------------------------+
```

### 分析名字

用法: `./qm.py --names=何正,陈道明`

```
+------+--------+--------+---------------+-------------+----------+-------+------+---------------+-----------------------------------------------------+
| 序号 | 简体   | 繁体   | 读音          | ID          | 百度     | 百科  | 打分 | 分析          | 释义                                                |
+------+--------+--------+---------------+-------------+----------+-------+------+---------------+-----------------------------------------------------+
| 0    | 何正   | 何正   | hé zhèng      | hezheng     | 49400    | 57073 | 99   | 0.0012 大众名 | 正  农历一年的第一个月  正,岁之首月,夏以建寅月      |
| 1    | 陈道明 | 陳道明 | chén dào míng | chendaoming | 11400000 | 1546  | 62   | 0.0143 大众名 | 明  (会意。甲骨文以日、月”发光表示明亮。小篆从月囧, |
+------+--------+--------+---------------+-------------+----------+-------+------+---------------+-----------------------------------------------------+
```

### 查询字典

用法: `./qm.py --word=正`

```
正

 农历一年的第一个月

 正,岁之首月,夏以建寅月为正,殷以建丑月为正,周以建子月为正。--《集韵·清韵》

 箭靶的中心

 终日射候,不出正兮。--《诗·齐风·猗嗟》

 引申为目标

 刑(形)名已立,声号已建,则无所逃迹若正匿。--《马王堆汉墓帛书》

 正

 通征”

 征税

 正其货贿。--《周礼·地官·司门》。郑注正,读为征。”

 唯加田无国正。--《周礼·夏官·司勋》

 谨正盐筴。--《管子·海王》。李哲明云正,税也,正、征古字通用。”

 出兵,征讨

 正zhèng

...
```

### 常见名字

用法: `./qm.py --topk=8`

```
1. 华: 24021
2. 明: 17226
3. 平: 16515
4. 林: 14037
5. 军: 13232
6. 英: 13061
7. 文: 12879
8. 芳: 11177
```

## Data source

- 百度搜索
- 互动百科
- PCbaby
- 字典[data/word.json](https://github.com/pwxcoo/chinese-xinhua)
- 姓名语料库[data/chinese_names_corpus.txt](https://github.com/wainshine/Chinese-Names-Corpus)

## Thirdparty

- 简体-繁体转换 opencc
- 汉语拼音 pinyin
