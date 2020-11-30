---
layout: docs
header: true
title: Training Models with NLU
permalink: /docs/en/training
key: docs-developers
modify_date: "2020-05-08"
---

<div class="main-docs" markdown="1">

<div class="h3-box" markdown="1">

You can fit load a trainable NLU pipeline via nlu.load('train.<model>') you can 

# NER Training
[NER training demo](https://colab.research.google.com/drive/1_GwhdXULq45GZkw3157fAOx4Wqo-fmFV?usp=sharing)        
You can train your own custom NER model with an [CoNLL 20003 IOB](https://www.aclweb.org/anthology/W03-0419.pdf) formatted dataset.      
By default *Glove 100d Token Embeddings* are used as features for the classifier.

```python
train_path = '/content/eng.train'
fitted_pipe = nlu.load('train.ner').fit(dataset_path=train_path)
```

If a NLU reference to a Token Embeddings model is added before the train reference, that Token Embedding will be used when training the NER model.

```python
# Train on BERT embeddigns
train_path = '/content/eng.train'
fitted_pipe = nlu.load('bert train.ner').fit(dataset_path=train_path)
```

# Multi Class Text Classifier Training
[Multi Class Text Classifier Training Demo](https://colab.research.google.com/drive/12FA2TVvvRWw4pRhxDnK32WAzl9dbF6Qw?usp=sharing)         
To train the Multi Class text classifier model, you must pass a dataframe with a 'text' column and a 'y' column for the label.
By default *Universal Sentence Encoder Embeddings (USE)* are used as sentence embeddings. 

```python
fitted_pipe = nlu.load('train.classifier').fit(train_df)
preds = fitted_pipe.predict(train_df)
```

If you add a nlu sentence embeddings reference, before the train reference, NLU will use that Sentence embeddings instead of the default USE.

```python
#Train on BERT sentence emebddings
fitted_pipe = nlu.load('embed_sentence.bert train.classifier').fit(train_df)
preds = fitted_pipe.predict(train_df)
```


# Sentiment Classifier Training
[Sentiment Classification Training Demo](https://colab.research.google.com/drive/1f-EORjO3IpvwRAktuL4EvZPqPr2IZ_g8?usp=sharing)         

To train the Binary Sentiment classifier model, you must pass a dataframe with a 'text' column and a 'y' column for the label.

By default *Universal Sentence Encoder Embeddings (USE)* are used as sentence embeddings. 

```python
fitted_pipe = nlu.load('train.sentiment').fit(train_df)
preds = fitted_pipe.predict(train_df)
```

If you add a nlu sentence embeddings reference, before the train reference, NLU will use that Sentence embeddings instead of the default USE.

```python
#Train on BERT sentence emebddings
fitted_pipe = nlu.load('embed_sentence.bert train.classifier').fit(train_df)
preds = fitted_pipe.predict(train_df)
```



## Saving a NLU pipelien to disk

```python
train_path = '/content/eng.train'
fitted_pipe = nlu.load('train.ner').fit(dataset_path=train_path)
stored_model_path = './models/classifier_dl_trained' 
fitted_pipe.save(stored_model_path)

```

## Loading a NLU pipeline from disk

```python
train_path = '/content/eng.train'
fitted_pipe = nlu.load('train.ner').fit(dataset_path=train_path)
stored_model_path = './models/classifier_dl_trained' 
fitted_pipe.save(stored_model_path)
hdd_pipe = nlu.load(path=stored_model_path)
```



## Loading a NLU pipeline as pyspark.ml.PipelineModel
```python
import pyspark
# load the NLU pipeline as pyspark pipeline
pyspark_pipe = pyspark.ml.PipelineModel.load(stored_model_path)
# Generate spark Df and transform it with the pyspark Pipeline
s_df = spark.createDataFrame(df)
pyspark_pipe.transform(s_df).show()
```


</div></div>