

# BlazingText Hyperparameters
<a name="blazingtext_hyperparameters"></a>

When you start a training job with a `CreateTrainingJob` request, you specify a training algorithm. You can also specify algorithm-specific hyperparameters as string-to-string maps. The hyperparameters for the BlazingText algorithm depend on which mode you use: Word2Vec (unsupervised) and Text Classification (supervised).

## Word2Vec Hyperparameters
<a name="blazingtext_hyperparameters_word2vec"></a>

The following table lists the hyperparameters for the BlazingText Word2Vec training algorithm provided by Amazon SageMaker AI.


| Parameter Name | Description | 
| --- | --- | 
| mode | The Word2vec architecture used for training.<br />**Required**<br />Valid values: `batch_skipgram`, `skipgram`, or `cbow` | 
| batch\_size | The size of each batch when `mode` is set to `batch_skipgram`. Set to a number between 10 and 20.<br />**Optional**<br />Valid values: Positive integer<br />Default value: 11 | 
| buckets | The number of hash buckets to use for subwords.<br />**Optional**<br />Valid values: positive integer<br />Default value: 2000000 | 
| epochs | The number of complete passes through the training data.<br />**Optional**<br />Valid values: Positive integer<br />Default value: 5 | 
| evaluation | Whether the trained model is evaluated using the [WordSimilarity-353 Test](http://www.gabrilovich.com/resources/data/wordsim353/wordsim353.html).<br />**Optional**<br />Valid values: (Boolean) `True` or `False`<br />Default value: `True` | 
| learning\_rate | The step size used for parameter updates.<br />**Optional**<br />Valid values: Positive float<br />Default value: 0.05 | 
| min\_char | The minimum number of characters to use for subwords/character n-grams.<br />**Optional**<br />Valid values: positive integer<br />Default value: 3 | 
| min\_count | Words that appear less than `min_count` times are discarded.<br />**Optional**<br />Valid values: Non-negative integer<br />Default value: 5 | 
| max\_char | The maximum number of characters to use for subwords/character n-grams<br />**Optional**<br />Valid values: positive integer<br />Default value: 6 | 
| negative\_samples | The number of negative samples for the negative sample sharing strategy.<br />**Optional**<br />Valid values: Positive integer<br />Default value: 5 | 
| sampling\_threshold | The threshold for the occurrence of words. Words that appear with higher frequency in the training data are randomly down-sampled.<br />**Optional**<br />Valid values: Positive fraction. The recommended range is (0, 1e-3]<br />Default value: 0.0001 | 
| subwords | Whether to learn subword embeddings on not.<br />**Optional**<br />Valid values: (Boolean) `True` or `False`<br />Default value: `False` | 
| vector\_dim | The dimension of the word vectors that the algorithm learns.<br />**Optional**<br />Valid values: Positive integer<br />Default value: 100 | 
| window\_size | The size of the context window. The context window is the number of words surrounding the target word used for training.<br />**Optional**<br />Valid values: Positive integer<br />Default value: 5 | 

## Text Classification Hyperparameters
<a name="blazingtext_hyperparameters_text_class"></a>

The following table lists the hyperparameters for the Text Classification training algorithm provided by Amazon SageMaker AI.

**Note**  
Although some of the parameters are common between the Text Classification and Word2Vec modes, they might have different meanings depending on the context.


| Parameter Name | Description | 
| --- | --- | 
| mode | The training mode.<br />**Required**<br />Valid values: `supervised` | 
| buckets | The number of hash buckets to use for word n-grams.<br />**Optional**<br />Valid values: Positive integer<br />Default value: 2000000 | 
| early\_stopping | Whether to stop training if validation accuracy doesn't improve after a `patience` number of epochs. Note that a validation channel is required if early stopping is used.<br />**Optional**<br />Valid values: (Boolean) `True` or `False`<br />Default value: `False` | 
| epochs | The maximum number of complete passes through the training data.<br />**Optional**<br />Valid values: Positive integer<br />Default value: 5 | 
| learning\_rate | The step size used for parameter updates.<br />**Optional**<br />Valid values: Positive float<br />Default value: 0.05 | 
| min\_count | Words that appear less than `min_count` times are discarded.<br />**Optional**<br />Valid values: Non-negative integer<br />Default value: 5 | 
| min\_epochs | The minimum number of epochs to train before early stopping logic is invoked.<br />**Optional**<br />Valid values: Positive integer<br />Default value: 5 | 
| patience | The number of epochs to wait before applying early stopping when no progress is made on the validation set. Used only when `early_stopping` is `True`.<br />**Optional**<br />Valid values: Positive integer<br />Default value: 4 | 
| vector\_dim | The dimension of the embedding layer.<br />**Optional**<br />Valid values: Positive integer<br />Default value: 100 | 
| word\_ngrams | The number of word n-gram features to use.<br />**Optional**<br />Valid values: Positive integer<br />Default value: 2 | 