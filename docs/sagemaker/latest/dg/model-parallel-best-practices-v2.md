

# SageMaker distributed model parallelism best practices
<a name="model-parallel-best-practices-v2"></a>

Use the following guidelines when you run a distributed training job with the SageMaker model parallel library v2 (SMP v2).

## Setting up the right configuration for distributed training
<a name="model-parallel-best-practices-configuration-v2"></a>

To estimate and find the best starting point to apply distributed training techniques that SMP v2 provides, review the following list. Each list item discusses the advantage of using the [Core features of the SageMaker model parallelism library v2](model-parallel-core-features-v2.md) along with potential tradeoffs. 

### Configuration tips
<a name="model-parallel-best-practices-v2-config-tips"></a>

This section provides guidelines on how to decide on the best model configurations for optimal throughput with global batch size requirements.

First, we recommend the following setups regardless of the size of your model.

1. Use the most powerful instance type that you can use.

1. Turn on [mixed precision](model-parallel-core-features-v2-mixed-precision.md) all the time, as it provides substantial benefits for performance and memory reduction. We recommend you to use `bfloat16` as it's more precise than `float16`.

1. Turn on the [SageMaker distributed data parallelism library](data-parallel.md) (instead of using NCCL) whenever it’s applicable, as shown in [Compatibility with the SMDDP library optimized for AWS infrastructure](model-parallel-core-features-v2-smddp-allgather.md). One exception is for tensor-parallelism-only use cases (`hybrid_shard_degree = 1` and `tensor_paralle_degree > 1`).

1. If your model has more than about 60 billion parameters, we recommend using [Delayed parameter initialization](model-parallel-core-features-v2-delayed-param-init.md). You can also use delayed parameter initialization to speed up the initialization for any model.

1. We recommend you to enable [Activation checkpointing](model-parallel-core-features-v2-pytorch-activation-checkpointing.md). 

Depending on the size of you model, we recommend that you start with the following guidance.

1. Use sharded data parallelism.

   1. Depending on the batch size you intend to fit in the GPU memory, choose the appropriate sharded data parallel degree. Normally, you should start with the lowest degree to fit your model in the GPU memory while minimizing overhead from network communication. If you see a warning that cache flushes are happening, we recommend that you increase the sharding degree. 

   1. Determine `world_size` based on the maximum local batch size and required global batch size, if any.

   1. You can experiment with activation offloading. Depending on scenarios, it can address your memory needs without having to increase the sharding degree, which means less communication. 

1. Use sharded data parallelism of PyTorch FSDP and tensor parallelism of SMP v2 simultaneously, as introduced in [Tensor parallelism](model-parallel-core-features-v2-tensor-parallelism.md).

   1. When training on large clusters, with FSDP alone the global batch size can become too large, causing convergence issues for the model. Typically, most research work keeps the batch size under 4 million tokens. In this case, you can resolve the problem by composing PyTorch FSDP with tensor parallelism of SMP v2 to reduce the batch size.

      For example, if you have 256 nodes and sequence length 4096, even a batch size of 1 per GPU leads to global batch size of 8M tokens. However, when you use tensor parallelism with degree 2 and batch size of 1 per tensor parallel group, this becomes 1/2 batch size per GPU, which translates to 4 million tokens.

   1. When training with long context lengths such as 8k, 16k activation memory can become very high. FSDP doesn't shard activations, and activations can cause GPUs to go out of memory. In such scenarios, you can train efficiently by composing PyTorch FSDP with tensor parallelism of SMP v2.

### Reference configurations
<a name="model-parallel-best-practices-configuration-reference-v2"></a>

The SageMaker model parallelism training team provides the following reference points based on experiments with the Llama 2 model transformed to the SMP transformer model using [`torch.sagemaker.transform`](distributed-model-parallel-v2-reference.md#model-parallel-v2-torch-sagemaker-reference-transform), and trained on `ml.p4d.24xlarge` instance(s) with sequence length 4096 and mixed precision (FP16 or BF16).



- **Llama 2**
  - **Model size (the number of model parameters):** 7B / **The number of instances:** 1 / **Sharded data parallel degree:** 8 / **Tensor parallel degree:** 1 / **Activation checkpointing:** TRUE / **Activation offloading:** FALSE / **Batch size:** 4
  - **Model size (the number of model parameters):** 70B / **The number of instances:** 32 / **Sharded data parallel degree:** 256 / **Tensor parallel degree:** 1 / **Activation checkpointing:** TRUE / **Activation offloading:** FALSE / **Batch size:** 2
  - **Model size (the number of model parameters):** 175B / **The number of instances:** 64 / **Sharded data parallel degree:** 128 / **Tensor parallel degree:** 4 / **Activation checkpointing:** TRUE / **Activation offloading:** TRUE / **Batch size:** 6



You can extrapolate from the preceding configurations to estimate GPU memory usage for your model configuration. For example, if you increase the sequence length for a 10-billion-parameter model or increase the size of the model to 20 billion, you might want to lower batch size first. If the model still doesn’t fit, try increasing the degree of tensor parallelism.

## Monitoring and logging a training job using the SageMaker AI console and Amazon CloudWatch
<a name="model-parallel-best-practices-monitoring-v2"></a>

To monitor system-level metrics such as CPU memory utilization, GPU memory utilization, and GPU utilization, use visualization provided through the [SageMaker AI console](https://console.aws.amazon.com/sagemaker/).

1. In the left navigation pane, choose **Training**.

1. Choose **Training jobs**.

1. In the main pane, choose the training job name for which you want to see more details.

1. Browse the main pane and find the **Monitor** section to see the automated visualization.

1. To see training job logs, choose **View logs** in the **Monitor** section. You can access the distributed training job logs of the training job in CloudWatch. If you launched multi-node distributed training, you should see multiple log streams with tags in the format of **algo-n-1234567890**. The **algo-1** log stream tracks training logs from the main (0th) node.

For more information, see [Amazon CloudWatch Metrics for Monitoring and Analyzing Training Jobs](training-metrics.md).

## Permissions
<a name="model-parallel-best-practices-permissions-v2"></a>

To run a SageMaker training job with model parallelism, make sure you have the right permissions in your IAM role, such as the following:
+ To use [FSx for Lustre](https://aws.amazon.com/fsx/), add [`AmazonFSxFullAccess`](https://console.aws.amazon.com/iam/home#/policies/arn%3Aaws%3Aiam%3A%3Aaws%3Apolicy%2FAmazonFSxFullAccess).
+ To use Amazon S3 as a data channel, add [`AmazonS3FullAccess`](https://console.aws.amazon.com/iam/home#/policies/arn%3Aaws%3Aiam%3A%3Aaws%3Apolicy%2FAmazonS3FullAccess).
+ To use Docker, build your own container, and push it to Amazon ECR, add [`AmazonEC2ContainerRegistryFullAccess`](https://console.aws.amazon.com/iam/home#/policies/arn%3Aaws%3Aiam%3A%3Aaws%3Apolicy%2FAmazonEC2ContainerRegistryFullAccess).
+ To have a full access to use the entire suite of SageMaker AI features, add [`AmazonSageMakerFullAccess`](https://console.aws.amazon.com/iam/home#/policies/iam/home#/policies/arn%3Aaws%3Aiam%3A%3Aaws%3Apolicy%2FAmazonSageMakerFullAccess). 