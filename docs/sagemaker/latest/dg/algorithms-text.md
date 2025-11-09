# Built-in SageMaker AI Algorithms for Text Data

SageMaker AI provides algorithms that are tailored to the analysis of textual documents used
in natural language processing, document classification or summarization, topic modeling
or classification, and language transcription or translation.

- [BlazingText algorithm](blazingtext.md "blazingtext.md")—a highly
  optimized implementation of the Word2vec and text classification algorithms that
  scale to large datasets easily. It is useful for many downstream natural
  language processing (NLP) tasks.
- [Latent Dirichlet Allocation (LDA) Algorithm](lda.md "lda.md")—an algorithm suitable for
  determining topics in a set of documents. It is an _unsupervised algorithm_, which means that it doesn't use example
  data with answers during training.
- [Neural Topic Model (NTM) Algorithm](ntm.md "ntm.md")—another unsupervised
  technique for determining topics in a set of documents, using a neural network
  approach.
- [Object2Vec Algorithm](object2vec.md "object2vec.md")—a general-purpose neural embedding algorithm that can be used for recommendation systems, document classification, and sentence embeddings.
- [Sequence-to-Sequence Algorithm](seq-2-seq.md "seq-2-seq.md")—a supervised
  algorithm commonly used for neural machine translation.
- [Text Classification - TensorFlow](text-classification-tensorflow.md "text-classification-tensorflow.md")—a supervised
  algorithm that supports transfer learning with available pretrained models for text classification.

| Algorithm name                      | Channel name                                     | Training input mode | File type                                                     | Instance class                    | Parallelizable                                       |
| ----------------------------------- | ------------------------------------------------ | ------------------- | ------------------------------------------------------------- | --------------------------------- | ---------------------------------------------------- |
| BlazingText                         | train                                            | File or Pipe        | Text file (one sentence per line with space-separated tokens) | GPU (single instance only) or CPU | No                                                   |
| LDA                                 | train and (optionally) test                      | File or Pipe        | recordIO-protobuf or CSV                                      | CPU (single instance only)        | No                                                   |
| Neural Topic Model                  | train and (optionally) validation, test, or both | File or Pipe        | recordIO-protobuf or CSV                                      | GPU or CPU                        | Yes                                                  |
| Object2Vec                          | train and (optionally) validation, test, or both | File                | JSON Lines                                                    | GPU or CPU (single instance only) | No                                                   |
| Seq2Seq Modeling                    | train, validation, and vocab                     | File                | recordIO-protobuf                                             | GPU (single instance only)        | No                                                   |
| Text Classification<br>• TensorFlow | training and validation                          | File                | CSV                                                           | CPU or GPU                        | Yes (only across multiple GPUs on a single instance) |
