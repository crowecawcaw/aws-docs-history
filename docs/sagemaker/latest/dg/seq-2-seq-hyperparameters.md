

# Sequence-to-Sequence Hyperparameters
<a name="seq-2-seq-hyperparameters"></a>

The following table lists the hyperparameters that you can set when training with the Amazon SageMaker AI Sequence-to-Sequence (seq2seq) algorithm.


| Parameter Name | Description | 
| --- | --- | 
| batch\_size | Mini batch size for gradient descent.<br />**Optional**<br />Valid values: positive integer<br />Default value: 64 | 
| beam\_size | Length of the beam for beam search. Used during training for computing `bleu` and used during inference.<br />**Optional**<br />Valid values: positive integer<br />Default value: 5 | 
| bleu\_sample\_size | Number of instances to pick from validation dataset to decode and compute `bleu` score during training. Set to -1 to use full validation set (if `bleu` is chosen as `optimized_metric`).<br />**Optional**<br />Valid values: integer<br />Default value: 0 | 
| bucket\_width | Returns (source,target) buckets up to (`max_seq_len_source`, `max_seq_len_target`). The longer side of the data uses steps of `bucket_width` while the shorter side uses steps scaled down by the average target/source length ratio. If one sided reaches its maximum length before the other, width of extra buckets on that side is fixed to that side of `max_len`.<br />**Optional**<br />Valid values: positive integer<br />Default value: 10 | 
| bucketing\_enabled | Set to `false` to disable bucketing, unroll to maximum length.<br />**Optional**<br />Valid values: `true` or `false`<br />Default value: `true` | 
| checkpoint\_frequency\_num\_batches | Checkpoint and evaluate every x batches. This checkpointing hyperparameter is passed to the SageMaker AI's seq2seq algorithm for early stopping and retrieving the best model. The algorithm's checkpointing runs locally in the algorithm's training container and is not compatible with SageMaker AI checkpointing. The algorithm temporarily saves checkpoints to a local path and stores the best model artifact to the model output path in S3 after the training job has stopped.<br />**Optional**<br />Valid values: positive integer<br />Default value: 1000 | 
| checkpoint\_threshold | Maximum number of checkpoints model is allowed to not improve in `optimized_metric` on validation dataset before training is stopped. This checkpointing hyperparameter is passed to the SageMaker AI's seq2seq algorithm for early stopping and retrieving the best model. The algorithm's checkpointing runs locally in the algorithm's training container and is not compatible with SageMaker AI checkpointing. The algorithm temporarily saves checkpoints to a local path and stores the best model artifact to the model output path in S3 after the training job has stopped.<br />**Optional**<br />Valid values: positive integer<br />Default value: 3 | 
| clip\_gradient | Clip absolute gradient values greater than this. Set to negative to disable.<br />**Optional**<br />Valid values: float<br />Default value: 1 | 
| cnn\_activation\_type | The `cnn` activation type to be used.<br />**Optional**<br />Valid values: String. One of `glu`, `relu`, `softrelu`, `sigmoid`, or `tanh`.<br />Default value: `glu` | 
| cnn\_hidden\_dropout | Dropout probability for dropout between convolutional layers.<br />**Optional**<br />Valid values: Float. Range in [0,1].<br />Default value: 0 | 
| cnn\_kernel\_width\_decoder | Kernel width for the `cnn` decoder.<br />**Optional**<br />Valid values: positive integer<br />Default value: 5 | 
| cnn\_kernel\_width\_encoder | Kernel width for the `cnn` encoder.<br />**Optional**<br />Valid values: positive integer<br />Default value: 3 | 
| cnn\_num\_hidden | Number of `cnn` hidden units for encoder and decoder.<br />**Optional**<br />Valid values: positive integer<br />Default value: 512 | 
| decoder\_type | Decoder type.<br />**Optional**<br />Valid values: String. Either `rnn` or `cnn`.<br />Default value: *rnn* | 
| embed\_dropout\_source | Dropout probability for source side embeddings.<br />**Optional**<br />Valid values: Float. Range in [0,1].<br />Default value: 0 | 
| embed\_dropout\_target | Dropout probability for target side embeddings.<br />**Optional**<br />Valid values: Float. Range in [0,1].<br />Default value: 0 | 
| encoder\_type | Encoder type. The `rnn` architecture is based on attention mechanism by Bahdanau et al. and *cnn* architecture is based on Gehring et al.<br />**Optional**<br />Valid values: String. Either `rnn` or `cnn`.<br />Default value: `rnn` | 
| fixed\_rate\_lr\_half\_life | Half life for learning rate in terms of number of checkpoints for `fixed_rate_`\* schedulers.<br />**Optional**<br />Valid values: positive integer<br />Default value: 10 | 
| learning\_rate | Initial learning rate.<br />**Optional**<br />Valid values: float<br />Default value: 0.0003 | 
| loss\_type | Loss function for training.<br />**Optional**<br />Valid values: String. `cross-entropy`<br />Default value: `cross-entropy` | 
| lr\_scheduler\_type | Learning rate scheduler type. `plateau_reduce` means reduce the learning rate whenever `optimized_metric` on `validation_accuracy` plateaus. `inv_t` is inverse time decay. `learning_rate`/(1\+`decay_rate`\*t)<br />**Optional**<br />Valid values: String. One of `plateau_reduce`, `fixed_rate_inv_t`, or `fixed_rate_inv_sqrt_t`.<br />Default value: `plateau_reduce` | 
| max\_num\_batches | Maximum number of updates/batches to process. -1 for infinite.<br />**Optional**<br />Valid values: integer<br />Default value: -1 | 
| max\_num\_epochs | Maximum number of epochs to pass through training data before fitting is stopped. Training continues until this number of epochs even if validation accuracy is not improving if this parameter is passed. Ignored if not passed.<br />**Optional**<br />Valid values: Positive integer and less than or equal to max\_num\_epochs.<br />Default value: none | 
| max\_seq\_len\_source | Maximum length for the source sequence length. Sequences longer than this length are truncated to this length.<br />**Optional**<br />Valid values: positive integer<br />Default value: 100 | 
| max\_seq\_len\_target | Maximum length for the target sequence length. Sequences longer than this length are truncated to this length.<br />**Optional**<br />Valid values: positive integer<br />Default value: 100 | 
| min\_num\_epochs | Minimum number of epochs the training must run before it is stopped via `early_stopping` conditions.<br />**Optional**<br />Valid values: positive integer<br />Default value: 0 | 
| momentum | Momentum constant used for `sgd`. Don't pass this parameter if you are using `adam` or `rmsprop`.<br />**Optional**<br />Valid values: float<br />Default value: none | 
| num\_embed\_source | Embedding size for source tokens.<br />**Optional**<br />Valid values: positive integer<br />Default value: 512 | 
| num\_embed\_target | Embedding size for target tokens.<br />**Optional**<br />Valid values: positive integer<br />Default value: 512 | 
| num\_layers\_decoder | Number of layers for Decoder *rnn* or *cnn*.<br />**Optional**<br />Valid values: positive integer<br />Default value: 1 | 
| num\_layers\_encoder | Number of layers for Encoder `rnn` or `cnn`.<br />**Optional**<br />Valid values: positive integer<br />Default value: 1 | 
| optimized\_metric | Metrics to optimize with early stopping.<br />**Optional**<br />Valid values: String. One of `perplexity`, `accuracy`, or `bleu`.<br />Default value: `perplexity` | 
| optimizer\_type | Optimizer to choose from.<br />**Optional**<br />Valid values: String. One of `adam`, `sgd`, or `rmsprop`.<br />Default value: `adam` | 
| plateau\_reduce\_lr\_factor | Factor to multiply learning rate with (for `plateau_reduce`).<br />**Optional**<br />Valid values: float<br />Default value: 0.5 | 
| plateau\_reduce\_lr\_threshold | For `plateau_reduce` scheduler, multiply learning rate with reduce factor if `optimized_metric` didn't improve for this many checkpoints.<br />**Optional**<br />Valid values: positive integer<br />Default value: 3 | 
| rnn\_attention\_in\_upper\_layers | Pass the attention to upper layers of *rnn*, like Google NMT paper. Only applicable if more than one layer is used.<br />**Optional**<br />Valid values: boolean (`true` or `false`)<br />Default value: `true` | 
| rnn\_attention\_num\_hidden | Number of hidden units for attention layers. defaults to `rnn_num_hidden`.<br />**Optional**<br />Valid values: positive integer<br />Default value: `rnn_num_hidden` | 
| rnn\_attention\_type | Attention model for encoders. `mlp` refers to concat and bilinear refers to general from the Luong et al. paper.<br />**Optional**<br />Valid values: String. One of `dot`, `fixed`, `mlp`, or `bilinear`.<br />Default value: `mlp` | 
| rnn\_cell\_type | Specific type of `rnn` architecture.<br />**Optional**<br />Valid values: String. Either `lstm` or `gru`.<br />Default value: `lstm` | 
| rnn\_decoder\_state\_init | How to initialize `rnn` decoder states from encoders.<br />**Optional**<br />Valid values: String. One of `last`, `avg`, or `zero`.<br />Default value: `last` | 
| rnn\_first\_residual\_layer | First *rnn* layer to have a residual connection, only applicable if number of layers in encoder or decoder is more than 1.<br />**Optional**<br />Valid values: positive integer<br />Default value: 2 | 
| rnn\_num\_hidden | The number of *rnn* hidden units for encoder and decoder. This must be a multiple of 2 because the algorithm uses bi-directional Long Term Short Term Memory (LSTM) by default.<br />**Optional**<br />Valid values: positive even integer<br />Default value: 1024 | 
| rnn\_residual\_connections | Add residual connection to stacked *rnn*. Number of layers should be more than 1.<br />**Optional**<br />Valid values: boolean (`true` or `false`)<br />Default value: `false` | 
| rnn\_decoder\_hidden\_dropout | Dropout probability for hidden state that combines the context with the *rnn* hidden state in the decoder.<br />**Optional**<br />Valid values: Float. Range in [0,1].<br />Default value: 0 | 
| training\_metric | Metrics to track on training on validation data.<br />**Optional**<br />Valid values: String. Either `perplexity` or `accuracy`.<br />Default value: `perplexity` | 
| weight\_decay | Weight decay constant.<br />**Optional**<br />Valid values: float<br />Default value: 0 | 
| weight\_init\_scale | Weight initialization scale (for `uniform` and `xavier` initialization). <br />**Optional**<br />Valid values: float<br />Default value: 2.34 | 
| weight\_init\_type | Type of weight initialization. <br />**Optional**<br />Valid values: String. Either `uniform` or `xavier`.<br />Default value: `xavier` | 
| xavier\_factor\_type | Xavier factor type.<br />**Optional**<br />Valid values: String. One of `in`, `out`, or `avg`.<br />Default value: `in` | 