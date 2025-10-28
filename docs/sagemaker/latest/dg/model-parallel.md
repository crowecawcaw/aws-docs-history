# (Archived) SageMaker model parallelism library v1.x

###### Important

As of December 19, 2023, the SageMaker model parallelism (SMP) library v2 is released.
In favor of the SMP library v2, the SMP v1 capabilites are no longer supported in future
releases. The following section and topics are archived and specific to using the SMP
library v1. For information about using the SMP library v2, see [SageMaker model parallelism library v2](model-parallel-v2.md "model-parallel-v2.md").

Use Amazon SageMaker AI's model parallel library to train large deep learning (DL) models that are
difficult to train due to GPU memory limitations. The library automatically and efficiently
splits a model across multiple GPUs and instances. Using the library, you can achieve a
target prediction accuracy faster by efficiently training larger DL models with billions or
trillions of parameters.

You can use the library to automatically partition your own TensorFlow and PyTorch models
across multiple GPUs and multiple nodes with minimal code changes. You can access the
library's API through the SageMaker Python SDK.

Use the following sections to learn more about model parallelism and the SageMaker model
parallel library. This library's API documentation is located at [Distributed Training APIs](https://sagemaker.readthedocs.io/en/v2.199.0/api/training/smd_model_parallel.html "https://sagemaker.readthedocs.io/en/v2.199.0/api/training/smd_model_parallel.html") in the _SageMaker Python SDK v2.199.0
documentation_.

###### Topics

- [Introduction to Model Parallelism](model-parallel-intro.md "model-parallel-intro.md")
- [Supported Frameworks and
  AWS Regions](distributed-model-parallel-support.md "distributed-model-parallel-support.md")
- [Core Features of the SageMaker Model Parallelism
  Library](model-parallel-core-features.md "model-parallel-core-features.md")
- [Run a SageMaker Distributed Training Job with Model
  Parallelism](model-parallel-use-api.md "model-parallel-use-api.md")
- [Checkpointing and Fine-Tuning a Model
  with Model Parallelism](distributed-model-parallel-checkpointing-and-finetuning.md "distributed-model-parallel-checkpointing-and-finetuning.md")
- [Amazon SageMaker AI model parallelism library
  v1 examples](distributed-model-parallel-examples.md "distributed-model-parallel-examples.md")
- [SageMaker Distributed Model Parallelism Best
  Practices](model-parallel-best-practices.md "model-parallel-best-practices.md")
- [The SageMaker Distributed Model
  Parallelism Library Configuration Tips and Pitfalls](model-parallel-customize-tips-pitfalls.md "model-parallel-customize-tips-pitfalls.md")
- [Model Parallel
  Troubleshooting](distributed-troubleshooting-model-parallel.md "distributed-troubleshooting-model-parallel.md")
