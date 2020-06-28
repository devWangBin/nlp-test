nlp-test
========

Yu Zaishi intern Test submission.

For detail:

<https://github.com/ybdesire/yuzaishi_candidate_exam/blob/master/exam_nlp_intern.md>

**Data:**

[https://github.com/xuanzebi/BERT-CH-NER/blob/master/tmp](https://github.com/xuanzebi/BERT-CH-NER/blob/master/tmp/dev.txt)

数据划分介绍：

训练集：17999行

验证集：684行

测试集：306行

题目1——中文NER：
================

命名实体识别（英语：Named Entity
Recognition，简称NER）是指识别文本中具有特定意义的实体，主要包括人名、地名、机构名、专有名词等，以及时间、数量、货币、比例数值等文字。

**1.  模型：**

BERT-BiLSTM-CRF-NER：在BLSTM-CRF模型上用谷歌的BERT
Fine-tuning来完成中文命名实体识别。

 **2. 参考资料：**

[BLSTM-CRF模型git链接](<https://github.com/macanv/BERT-BiLSTM-CRF-NER>)

[BLSTM-CRF模型介绍博客](<https://blog.csdn.net/macanv/article/details/85684284>
)

[bert模型项目git链接](<https://github.com/google-research/bert>)

**3.  步骤：**

(1).  首先对数据集进行预处理和格式调整使其符合模型的输入；

(2).  然后使用封装好的BERT-BiLSTM-CRF-NER 模型对处理后的数据进行训练；

(3).  调参得到最优模型；

(4).  测试模型结果。

**4.  原数据集统计信息：**

|        | 行数  | 平均长度（字数）  | 最大长度（字数） |
|--------|-------|-------------------|------------------|
| 验证集 | 684   | 50.42982456140351 | 236              |
| 测试集 | 306   | 53.75816993464052 | 556              |
| 训练集 | 17999 | 46.48280460025557 | 568              |

**5.  预处理后数据集统计信息：**

**删除大于字数128的句子：**

|        | 行数  | 平均长度（字数）   | 最大长度（字数） |
|--------|-------|--------------------|------------------|
| 验证集 | 668   | 47.82335329341317  | 128              |
| 测试集 | 298   | 49.355704697986575 | 128              |
| 训练集 | 17745 | 44.57897999436461  | 128              |

**删除大于字数32的句子：**

|        | 行数 | 平均长度（字数）   | 最大长度（字数） |
|--------|------|--------------------|------------------|
| 验证集 | 211  | 24.161137440758292 | 32               |
| 测试集 | 91   | 23.912087912087912 | 32               |
| 训练集 | 6244 | 23.887251761691225 | 32               |

**6.  调参训练模型：**

由于是用自己个人PC跑的加上时间约束，所以没有进行充分地调参，未能使模型结果达到最优，而且为了加速训练，删除了较长的的句子。

几次训练过程展示如下：

1.  参数设置如下：模型输出见 ./NER/model01/

![image](https://github.com/devWangBin/nlp-test/blob/master/media/662898347e6dd24088c339cfdcf380cd.png)
训练集被遍历两遍，学习率0.001，2 epochs，batch size为64，一共训练了195个batch：

![image](https://github.com/devWangBin/nlp-test/blob/master/media/0be8538d7981c2646d081f2eac33c1bd.png)
最终准确率：86.20%，模型输出示例如下：第一列原句，第二列为标签，第三列为模型输出标签：
```
神 B-ORG O
州 I-ORG O
数 I-ORG O
码 I-ORG O
今 O O
天 O O
开 O O
启 O O
了 O O
闭 O O
幕 O O
仪 O O
式 O O
。 O O
```
2、参数设置如下：模型输出见 ./NER/model02/

![image](https://github.com/devWangBin/nlp-test/blob/master/media/ddf38eaa9a70eef66ef36148c52b2be3.png)
训练集被遍历两遍，学习率0.0001，5 epochs，batch size为64，一共训练了487个batch：

![image](https://github.com/devWangBin/nlp-test/blob/master/media/6677585197dc5b22c22cfee882c8b53c.png)
最终准确率：86.12%，模型输出示例如下：第一列原句，第二列为标签，第三列为模型输出标签：
```
全 O O
市 O O
有 O O
1 O O
． O O
8 O O
万 O O
农 O O
户 O O
被 O O
评 O O
为 O O
“ O O
少 O O
生 O O
快 O O
富 O O
标 O O
兵 O O
户 O O
” O O
。 O O
```
题目2——中文ERE：
================

实体抽取，也就是命名实体识别，包括实体的检测（find）和分类（classify）；关系抽取，是抽取如（实体1，实体2，关系）形的三元组（triple）。

**1.  模型方法：**

基于依存句法分析，实现文本的三元组抽取（实体和关系抽取）。不需要对数据集进行标注，先基于开源工具提取出命名实体，而后基于实体和依存句法分析，利用定义的中文依赖语义范式和其它工具来提取实体关系。

**2.  参考资料：**

[参考的开源项目，根据依存句法分析定义了中文的依赖语义范式DSNF(Dependency
Semantic Normal
Forms)](<https://github.com/lemonhu/open-entity-relation-extraction>)

[论文链接](<https://dl.acm.org/doi/10.1145/3162077>)

[pyltp](<https://github.com/HIT-SCIR/pyltp>)

**3.  步骤：**

(1) 熟悉项目源代码，了解相关原理；

(2) 安装各种所需的库与工具包，将数据预处理输入模型；

(3) 微调代码得到要求的输出。

**4.  输入数据：**

使用上题数据集中的验证集部分(dev,txt)，一共684行。
eg:

*南斯拉夫队教练桑特拉奇说，赛前，我对我的队员说，伊朗队是个强队，没人信。*

*南斯拉夫队素质高、技术精，不要忘了，他们有许多优秀的球员在为各欧洲俱乐部踢球。*

**5.  模型输出结果：./ERE/triple_result.txt**

![image](https://github.com/devWangBin/nlp-test/blob/master/media/efb3564b466fa95fc96911e8a38753bd.png)
eg:
triple：(entity1 relation entity2)

triple: 布拉泽维奇 怕 牙买加人

triple: 英格兰队 英格兰队的 希勒

triple: 厄尔头球 扳平比分 克罗地亚队

triple: 厄尔头球 扳平比分 斯塔尼

triple: 厄尔头球 扳平比分 牙买加队
