{
  "attention_probs_dropout_prob": 0.0,  #乘法attention时，softmax后dropout概率
  "directionality": "bidi",
  "hidden_act": "gelu", #激活函数
  "hidden_dropout_prob": 0.0,  #隐藏层dropout概率
  "hidden_size": 768,  #隐藏单元数
  "embedding_size": 128,
  "initializer_range": 0.02, #初始化范围
  "intermediate_size": 3072 ,  #升维维度
  "max_position_embeddings": 512,   #一个大于seq_length的参数，用于生成position_embedding "num_attention_heads": 12, #每个隐藏层中的attention head数
  "num_attention_heads": 12,
  "num_hidden_layers": 12,  #隐藏层数

  "pooler_fc_size": 768,
  "pooler_num_attention_heads": 12,
  "pooler_num_fc_layers": 3,
  "pooler_size_per_head": 128,
  "pooler_type": "first_token_transform",
  "type_vocab_size": 2,  #segment_ids类别 [0,1]
  "vocab_size": 21128,  #词典中词数
   "ln_type":"postln"
}


* loss：训练集损失值
*
* accuracy:训练集准确率
*
* val_loss:测试集损失值
*
* val_accruacy:测试集准确率
*
*
* 以下5种情况可供参考：
*
* train loss 不断下降，test loss不断下降，说明网络仍在学习;（最好的）
*
* train loss 不断下降，test loss趋于不变，说明网络过拟合;（max pool或者正则化）
*
* train loss 趋于不变，test loss不断下降，说明数据集100%有问题;（检查dataset）
*
* train loss 趋于不变，test loss趋于不变，说明学习遇到瓶颈，需要减小学习率或批量数目;（减少学习率）
*
* train loss 不断上升，test loss不断上升，说明网络结构设计不当，训练超参数设置不当，数据集经过清洗等问题。（最不好的情况）