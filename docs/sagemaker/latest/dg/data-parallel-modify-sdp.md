# Distributed training with the SageMaker AI

distributed data parallelism library

The SageMaker AI distributed data parallelism (SMDDP) library is designed for ease of use and to
provide seamless integration with PyTorch.

When training a deep learning model with the SMDDP library on SageMaker AI, you can focus on writing
your training script and model training.

To get started, import the SMDDP library to use its collective operations optimized for
AWS. The following topics provide instructions on what to add to your training script
depending on which collective operation you want to optimize.

###### Topics

- [Adapting your training script
  to use the SMDDP collective operations](data-parallel-modify-sdp-select-framework.md "data-parallel-modify-sdp-select-framework.md")
- [Launching distributed training jobs with SMDDP using the
  SageMaker Python SDK](data-parallel-use-api.md "data-parallel-use-api.md")
