# SageMaker model parallelism library v2

###### Note

Since the release of the SageMaker model parallelism (SMP) library v2.0.0 on December 19, 2023,
this documentation is renewed for the SMP library v2. For previous versions of the SMP
library, see [(Archived) SageMaker model parallelism library v1.x](model-parallel.md "model-parallel.md").

The Amazon SageMaker AI model parallelism library is a capability of SageMaker AI that enables high
performance and optimized large scale training on SageMaker AI accelerate compute instances. The
[Core features of the SageMaker model
parallelism library v2](model-parallel-core-features-v2.md "model-parallel-core-features-v2.md") include techniques and optimizations
to accelerate and simplify large model training, such as hybrid sharded data parallelism,
tensor parallelism, activation checkpointing, and activation offloading. You can use the SMP
library to accelerate the training and fine-tuning of large language models (LLMs), large
vision models (LVMs), and foundation models (FMs) with hundreds of billions of
parameters.

The SageMaker model parallelism library v2 (SMP v2) aligns the library’s APIs and methods with
open source PyTorch Fully Sharded Data Parallelism (FSDP), which gives you the benefit of
SMP performance optimizations with minimal code changes. With SMP v2, you can improve the
computational performance of training a state-of-the-art large model on SageMaker AI by bringing
your PyTorch FSDP training scripts to SageMaker AI.

You can use SMP v2 for the general [SageMaker Training](train-model.md "train-model.md") jobs
and distributed training workloads on [Amazon SageMaker HyperPod](sagemaker-hyperpod.md "sagemaker-hyperpod.md") clusters.

###### Topics

- [Model parallelism concepts](model-parallel-intro-v2.md "model-parallel-intro-v2.md")
- [Supported frameworks and
  AWS Regions](distributed-model-parallel-support-v2.md "distributed-model-parallel-support-v2.md")
- [Use the SageMaker model parallelism
  library v2](model-parallel-use-api-v2.md "model-parallel-use-api-v2.md")
- [Core features of the SageMaker model
  parallelism library v2](model-parallel-core-features-v2.md "model-parallel-core-features-v2.md")
- [Amazon SageMaker AI model parallelism library
  v2 examples](distributed-model-parallel-v2-examples.md "distributed-model-parallel-v2-examples.md")
- [SageMaker distributed model parallelism best
  practices](model-parallel-best-practices-v2.md "model-parallel-best-practices-v2.md")
- [The SageMaker model parallel
  library v2 reference](distributed-model-parallel-v2-reference.md "distributed-model-parallel-v2-reference.md")
- [Release notes for the SageMaker model parallelism
  library](model-parallel-release-notes.md "model-parallel-release-notes.md")
- [(Archived) SageMaker model parallelism library v1.x](model-parallel.md "model-parallel.md")
