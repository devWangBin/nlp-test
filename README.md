nlp-test
========

**Data:**

[https://github.com/xuanzebi/BERT-CH-NER/blob/master/tmp](https://github.com/xuanzebi/BERT-CH-NER/blob/master/tmp/dev.txt)

数据划分介绍：

训练集：17999行

验证集：684行

测试集：306行

题目1——中文NER：
================

命名实体识别（英语：Named Entity Recognition，简称NER）是指识别文本中具有特定意义的实体，主要包括人名、地名、机构名、专有名词等，以及时间、数量、货币、比例数值等文字。

**1. 模型：**

BERT-BiLSTM-CRF-NER：在BLSTM-CRF模型上用谷歌的BERT Fine-tuning来完成中文命名实体识别。

**2. 参考资料：**

[BLSTM-CRF模型git链接](https://github.com/macanv/BERT-BiLSTM-CRF-NER)

[BLSTM-CRF模型介绍博客](<https://blog.csdn.net/macanv/article/details/85684284>)

[bert模型项目git链接](https://github.com/google-research/bert)

**3. 步骤：**

(1). 首先对数据集进行预处理和格式调整使其符合模型的输入；

(2). 然后使用封装好的BERT-BiLSTM-CRF-NER 模型对处理后的数据进行训练；

(3). 调参得到最优模型；

(4). 测试模型结果。

**4. 原数据集统计信息：**

|        | 行数  | 平均长度（字数）  | 最大长度（字数） |
|--------|-------|-------------------|------------------|
| 验证集 | 684   | 50.42982456140351 | 236              |
| 测试集 | 306   | 53.75816993464052 | 556              |
| 训练集 | 17999 | 46.48280460025557 | 568              |

**5. 预处理后数据集统计信息：**

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

**6. 调参训练模型：**

由于是用自己个人PC跑的加上时间约束，所以没有进行充分地调参，未能使模型结果达到最优，而且为了加速训练，删除了较长的的句子。几次训练过程展示如下：

1.参数设置如下：模型输出见 ./NER/model01/

![image](https://github.com/devWangBin/nlp-test/blob/master/img/01.png)

训练集被遍历两遍，学习率0.001，2 epochs，batch size为64，一共训练了195个batch：

![image](https://github.com/devWangBin/nlp-test/blob/master/img/02.png)

最终准确率：86.20%，模型输出示例如下：第一列原句，第二列为标签，第三列为模型输出标签：

~~~
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
~~~

2.参数设置如下：模型输出见 ./NER/model02/

![image](https://github.com/devWangBin/nlp-test/blob/master/img/03.png)

训练集被遍历两遍，学习率0.0001，5 epochs，batch size为64，一共训练了487个batch：

![image](https://github.com/devWangBin/nlp-test/blob/master/img/04.png)

最终准确率：86.12%，模型输出示例如下：第一列原句，第二列为标签，第三列为模型输出标签：

~~~
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
~~~

**7. 潜在的问题：**

从输出的标注label也可以看出来，虽然从标注的准确率来看能达到85%以上，但由于训练不充分，参数没有调到较优的原因，所以模型对绝大部分字的标注都是“O”，也可能是因为原数据集的分布很不均匀而导致的。

**8. 如何提高/优化：**

1.  进一步调参优化，具体可以考虑增大LSTM网络层内部的隐藏层向量维度，即模型中LSTM_SIZE参数，或调整学习率、dropout rate等模型参数。

2.  针对标注的实体在数据中分布不均匀的情况，在该模型基础上增加attention机制，使模型重点关注句子中实体的识别建模，提高模型performance。


题目2——中文ERE：
================

实体抽取，也就是命名实体识别，包括实体的检测（find）和分类（classify）；关系抽取，是抽取如（实体1，实体2，关系）形的三元组（triple）。

**1. 模型方法：**

基于依存句法分析，实现文本的三元组抽取（实体和关系抽取）。不需要对数据集进行标注，先基于开源工具提取出命名实体，而后基于实体和依存句法分析，利用定义的中文依赖语义范式和其它工具来提取实体关系。

**2. 参考资料：**

[参考的开源项目，根据依存句法分析定义了中文的依赖语义范式DSNF(Dependency Semantic Normal Forms)](https://github.com/lemonhu/open-entity-relation-extraction)

[论文链接](https://dl.acm.org/doi/10.1145/3162077)

[pyltp](https://github.com/HIT-SCIR/pyltp)

**3. 步骤：**

1.  熟悉项目源代码，了解相关原理；

2.  安装各种所需的库与工具包，将数据预处理输入模型；

3.  微调代码得到要求的输出。

**4. 输入数据：**

使用上题数据集中的验证集部分(dev,txt)，一共684行。 eg:

*南斯拉夫队教练桑特拉奇说，赛前，我对我的队员说，伊朗队是个强队，没人信。*

*南斯拉夫队素质高、技术精，不要忘了，他们有许多优秀的球员在为各欧洲俱乐部踢球。*

**5. 模型输出结果：./ERE/triple_result.txt**

![image](https://github.com/devWangBin/nlp-test/blob/master/img/05.png)

eg: triple：(entity1 relation entity2)

triple: 布拉泽维奇 怕 牙买加人

triple: 英格兰队 英格兰队的 希勒

triple: 厄尔头球 扳平比分 克罗地亚队

triple: 厄尔头球 扳平比分 斯塔尼

triple: 厄尔头球 扳平比分 牙买加队


**6. 潜在的问题：**

1.  模型使用的是无标签数据，直接输出提取的关系，所以没有可以进行对比基线指标，无法直接对模型输出做出评价，后期可以考虑横向对比其它模型的输出结果；

2.  单从输出结果看，所抽取的实体关系三元组有一些少，六百多个句子只有约60组，可能存在提取不全面与充分的问题。

**7. 如何提高/优化：**

1.  从提高模型表现的角度，第一个方面是从模型本身出发，可以改进增删模型中的定义的中文依赖语义范式，论文中提出了七种，实际应用时可以结合实际问题的数据集分布特点进行改进，还可以尝试使用其它更优预训练的模型来进行实体识别和依存句法分析（不止于ltp）;

2.  第二个角度可以考虑借鉴boosting的思想，采用集成学习的方法集成多个模型，提升performance；
