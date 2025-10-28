# Core Features of the SageMaker Model Parallelism

Library

Amazon SageMaker AI's model parallelism library offers distribution strategies and memory-saving
techniques, such as sharded data parallelism, tensor parallelism, model partitioning by
layers for pipeline scheduling, and checkpointing. The model parallelism strategies and
techniques help distribute large models across multiple devices while optimizing training
speed and memory consumption. The library also provides Python helper functions, context
managers, and wrapper functions to adapt your training script for automated or manual
partitioning of your model.

When you implement model parallelism to your training job, you keep the same two-step
workflow shown in the [Run a
SageMaker Distributed Training Job with Model Parallelism](model-parallel-use-api.md "model-parallel-use-api.md") section. For adapting
your training script, you'll add zero or few additional code lines to your training script.
For launching a training job of the adapted training script, you'll need to set the
distribution configuration parameters to activate the memory-saving features or to pass
values for the degree of parallelism.

To get started with examples, see the following Jupyter notebooks that demonstrate how to
use the SageMaker model parallelism library.

- [PyTorch example notebooks](https://github.com/aws/amazon-sagemaker-examples/tree/main/training/distributed_training/pytorch/model_parallel "https://github.com/aws/amazon-sagemaker-examples/tree/main/training/distributed_training/pytorch/model_parallel")
- [TensorFlow example notebooks](https://github.com/aws/amazon-sagemaker-examples/tree/main/training/distributed_training/tensorflow/model_parallel/mnist "https://github.com/aws/amazon-sagemaker-examples/tree/main/training/distributed_training/tensorflow/model_parallel/mnist")
  To dive deep into the core features of the library, see the following topics.

###### Note

The SageMaker distributed training libraries are available through the AWS deep learning
containers for PyTorch, Hugging Face, and TensorFlow within the SageMaker Training platform. To
utilize the features of the distributed training libraries, we recommend that you use
the SageMaker Python SDK. You can also manually configure in JSON request syntax if you use
SageMaker APIs through SDK for Python (Boto3) or AWS Command Line Interface. Throughout the documentation, instructions and
examples focus on how to use the distributed training libraries with the SageMaker Python
SDK.

###### Important

The SageMaker model parallelism library supports all the core features for PyTorch, and
supports pipeline parallelism for TensorFlow.

###### Topics

- [Sharded Data Parallelism](model-parallel-extended-features-pytorch-sharded-data-parallelism.md "model-parallel-extended-features-pytorch-sharded-data-parallelism.md")
- [Pipelining a Model](model-parallel-core-features-pipieline-parallelism.md "model-parallel-core-features-pipieline-parallelism.md")
- [Tensor
  Parallelism](model-parallel-extended-features-pytorch-tensor-parallelism.md "model-parallel-extended-features-pytorch-tensor-parallelism.md")
- [Optimizer State Sharding](model-parallel-extended-features-pytorch-optimizer-state-sharding.md "model-parallel-extended-features-pytorch-optimizer-state-sharding.md")
- [Activation Checkpointing](model-parallel-extended-features-pytorch-activation-checkpointing.md "model-parallel-extended-features-pytorch-activation-checkpointing.md")
- [Activation Offloading](model-parallel-extended-features-pytorch-activation-offloading.md "model-parallel-extended-features-pytorch-activation-offloading.md")
- [FP16 Training with Model
  Parallelism](model-parallel-extended-features-pytorch-fp16.md "model-parallel-extended-features-pytorch-fp16.md")
- [Support for
  FlashAttention](model-parallel-attention-head-size-for-flash-attention.md "model-parallel-attention-head-size-for-flash-attention.md")
