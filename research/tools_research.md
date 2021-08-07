# BERT
- BERT是2018年10月由Google AI研究院提出的一种预训练模型。可以用来做语义分析。网上很多关于BERT的资料是有关如何进行语义分析训练的，这是超算干的活，我们需要的仅仅是一个能够使用训练完成的数据集进行语义分析的工具。google提供了一些训练完成的数据集，包括中英文。
## 一些可能可以用的东西
- 搜了圈下来，这两个比较合适
- https://github.com/Brokenwind/BertSimilarity  利用Bert计算句子相似度。语义相似度计算。文本相似度计算。
- https://github.com/shangan23/similar-sentences Similar sentence Prediction with more accurate results with your dataset on top of pertained 
## 使用BERT的机制
- BERT训练出来的数据集，依靠文本的分词结果作为输入，需要对文字进行编码。网上很多使用教程仅仅到编码这一步就结束了。
- 尝试了一份教程，可以在本机做文字预测，就是把一份文本遮蔽一个字后猜测那个字是什么。试过了，可以用。 https://blog.csdn.net/Xiao_CangTian/article/details/108272159?utm_medium=distribute.pc_relevant.none-task-blog-2%7Edefault%7EBlogCommendFromMachineLearnPai2%7Edefault-10.base&depth_1-utm_source=distribute.pc_relevant.none-task-blog-2%7Edefault%7EBlogCommendFromMachineLearnPai2%7Edefault-10.base    
    要注意的是加载model，from_pretrained()最好改成本地路径的，而不是训练集名称，自动搜索会搜不到。
model
# 备用选项
- https://github.com/chatopera/Synonyms 中文近义词 可以简单使用。试过了，可以用。