# BlazingText Hyperparameters

When you start a training job with a `CreateTrainingJob` request, you
specify a training algorithm. You can also specify algorithm-specific hyperparameters as
string-to-string maps. The hyperparameters for the BlazingText algorithm depend on which
mode you use: Word2Vec (unsupervised) and Text Classification (supervised).

## Word2Vec

Hyperparameters

The following table lists the hyperparameters for the BlazingText Word2Vec
training algorithm provided by Amazon SageMaker AI.

| Parameter Name       | Description                                                                                                                                                                                                                                                                                                       |
| -------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `mode`               | The Word2vec architecture used for training.<br>**Required**<br>Valid values: `batch_skipgram`,<br>`skipgram`, or `cbow`                                                                                                                                                                                          |
| `batch_size`         | The size of each batch when `mode` is set to<br>`batch_skipgram`. Set to a number between 10 and<br>20.<br>**Optional**<br>Valid values: Positive integer<br>Default value: 11                                                                                                                                    |
| `buckets`            | The number of hash buckets to use for subwords.<br>**Optional**<br>Valid values: positive integer<br>Default value: 2000000                                                                                                                                                                                       |
| `epochs`             | The number of complete passes through the training<br>data.<br>**Optional**<br>Valid values: Positive integer<br>Default value: 5                                                                                                                                                                                 |
| `evaluation`         | Whether the trained model is evaluated using the [WordSimilarity-353 Test](http://www.gabrilovich.com/resources/data/wordsim353/wordsim353.html "http://www.gabrilovich.com/resources/data/wordsim353/wordsim353.html").<br>**Optional**<br>Valid values: (Boolean) `True` or<br>`False`<br>Default value: `True` |
| `learning_rate`      | The step size used for parameter updates.<br>**Optional**<br>Valid values: Positive float<br>Default value: 0.05                                                                                                                                                                                                  |
| `min_char`           | The minimum number of characters to use for subwords/character<br>n-grams.<br>**Optional**<br>Valid values: positive integer<br>Default value: 3                                                                                                                                                                  |
| `min_count`          | Words that appear less than `min_count` times are<br>discarded.<br>**Optional**<br>Valid values: Non-negative integer<br>Default value: 5                                                                                                                                                                         |
| `max_char`           | The maximum number of characters to use for subwords/character<br>n-grams<br>**Optional**<br>Valid values: positive integer<br>Default value: 6                                                                                                                                                                   |
| `negative_samples`   | The number of negative samples for the<br>negative<br>sample sharing strategy.<br>**Optional**<br>Valid values: Positive integer<br>Default value: 5                                                                                                                                                              |
| `sampling_threshold` | The threshold for the occurrence of words. Words that appear<br>with higher frequency in the training data are randomly<br>down-sampled.<br>**Optional**<br>Valid values: Positive fraction. The recommended range is (0,<br>1e-3]<br>Default value: 0.0001                                                       |
| `subwords`           | Whether to learn subword embeddings on not.<br>**Optional**<br>Valid values: (Boolean) `True` or<br>`False`<br>Default value: `False`                                                                                                                                                                             |
| `vector_dim`         | The dimension of the word vectors that the algorithm<br>learns.<br>**Optional**<br>Valid values: Positive integer<br>Default value: 100                                                                                                                                                                           |
| `window_size`        | The size of the context window. The context window is the<br>number of words surrounding the target word used for<br>training.<br>**Optional**<br>Valid values: Positive integer<br>Default value: 5                                                                                                              |

## Text Classification

Hyperparameters

The following table lists the hyperparameters for the Text Classification training
algorithm provided by Amazon SageMaker AI.

###### Note

Although some of the parameters are common between the Text Classification and
Word2Vec modes, they might have different meanings depending on the
context.

| Parameter Name   | Description                                                                                                                                                                                                                                                                   |
| ---------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `mode`           | The training mode.<br>**Required**<br>Valid values: `supervised`                                                                                                                                                                                                              |
| `buckets`        | The number of hash buckets to use for word n-grams.<br>**Optional**<br>Valid values: Positive integer<br>Default value: 2000000                                                                                                                                               |
| `early_stopping` | Whether to stop training if validation accuracy doesn't<br>improve after a `patience` number of epochs. Note<br>that a validation channel is required if early stopping is<br>used.<br>**Optional**<br>Valid values: (Boolean) `True` or<br>`False`<br>Default value: `False` |
| `epochs`         | The<br>maximum<br>number of complete passes through the training data.<br>**Optional**<br>Valid values: Positive integer<br>Default value: 5                                                                                                                                  |
| `learning_rate`  | The step size used for parameter updates.<br>**Optional**<br>Valid values: Positive float<br>Default value: 0.05                                                                                                                                                              |
| `min_count`      | Words that appear less than `min_count` times are<br>discarded.<br>**Optional**<br>Valid values: Non-negative integer<br>Default value: 5                                                                                                                                     |
| `min_epochs`     | The minimum number of epochs to train before early stopping<br>logic is invoked.<br>**Optional**<br>Valid values: Positive integer<br>Default value: 5                                                                                                                        |
| `patience`       | The number of epochs to wait before applying early stopping<br>when no progress is made on the validation set. Used only when<br>`early_stopping` is `True`.<br>**Optional**<br>Valid values: Positive integer<br>Default value: 4                                            |
| `vector_dim`     | The dimension of the embedding layer.<br>**Optional**<br>Valid values: Positive integer<br>Default value: 100                                                                                                                                                                 |
| `word_ngrams`    | The number of word n-gram features to use.<br>**Optional**<br>Valid values: Positive integer<br>Default value: 2                                                                                                                                                              |
