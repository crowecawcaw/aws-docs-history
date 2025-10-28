# Release notes for the SageMaker model parallelism

library

See the following release notes to track the latest updates for the SageMaker model parallelism
(SMP) library. If you have further questions about the SMP library, contact the SMP service
team at `sm-model-parallel-feedback@amazon.com`.

## The SageMaker model parallelism

library v2.8.0

_Date: April 01, 2025_

### SMP library

updates

**Bug fixes**

- SMP gradient norm clipping now supports activation offloading.

### SMP Docker and

Enroot containers

The SMP library team distributes Docker containers in replacement of the SageMaker
PyTorch framework containers. If you use the PyTorch estimator class in the SageMaker
Python SDK and specify distribution configuration to use SMP v2, SageMaker AI automatically
picks up the SMP Docker containers. To use this release of SMP v2, upgrade your SageMaker
Python SDK to `v2.243.0` or later.

**Currency updates**

- Added support for PyTorch v2.5.1
- Upgraded CUDA support to v12.4
- Upgraded NCCL support to v2.23.4
- Upgraded SMDDP library to 2.6.0

**Container details**

- SMP Docker container for PyTorch v2.5.1 with CUDA v12.4

```
658645717510.dkr.ecr.`<us-west-2>`.amazonaws.com/smdistributed-modelparallel:2.5.1-gpu-py311-cu124
```

- SMP Enroot container for PyTorch v2.5.1 with CUDA v12.4

```
https://sagemaker-distributed-model-parallel.s3.`<us-west-2>`.amazonaws.com/enroot/2.5.1-gpu-py311-cu124.sqsh
```

- Pre-installed packages
  - The SMP library v2.8.0
  - The SMDDP library v2.6.0
  - CUDNN v9.4.0
  - FlashAttention v2.5.8
  - TransformerEngine v1.10
  - Megatron v0.8.0
  - Hugging Face Transformers v4.44.2
  - Hugging Face Datasets library v2.19.0
  - EFA v1.36.0
  - NCCL v2.23.4
  - AWS-OFI-NCCL v1.13.2

### SMP Conda

channel

The following S3 bucket is the public Conda channel of the SMP library hosted by
the SMP service team. If you want to install the SMP v2 library in an environment
such as SageMaker HyperPod clusters, use this Conda channel to properly install the SMP
library.

- `https://sagemaker-distributed-model-parallel.s3.us-west-2.amazonaws.com/smp-v2/`

For more information about Conda channels in general, see [Channels](https://docs.conda.io/projects/conda/en/latest/user-guide/concepts/channels.html "https://docs.conda.io/projects/conda/en/latest/user-guide/concepts/channels.html") in the _Conda documentation_.

## The SageMaker model parallelism

library v2.7.0

_Date: December 04, 2024_

### SMP library

updates

**New features**

- Added support for [SageMaker HyperPod recipes](sagemaker-hyperpod-recipes.md "sagemaker-hyperpod-recipes.md").

### SMP Docker and

Enroot containers

The SMP library team distributes Docker and Enroot containers in replacement of
the SageMaker PyTorch framework containers. If you use the PyTorch estimator class in the
SageMaker Python SDK and specify distribution configuration to use SMP v2, SageMaker
automatically picks up the SMP Docker containers. To use this release of SMP v2,
upgrade your SageMaker Python SDK to `v2.237.0` or later.

**Container details**

- SMP Docker container for PyTorch v2.4.1 with CUDA v12.1

```
658645717510.dkr.ecr.`<us-west-2>`.smdistributed-modelparallel:2.4.1-gpu-py311-cu121
```

- SMP Enroot container for PyTorch v2.4.1 with CUDA v12.1

```
https://sagemaker-distributed-model-parallel.s3.`<us-west-2>`.amazonaws.com/enroot/2.4.1-gpu-py311-cu121.sqsh
```

- Pre-installed packages
  - The SMP library v2.7.0
  - The SMDDP library v2.5.0
  - CUDNN v9.4.0
  - FlashAttention v2.5.8
  - TransformerEngine v1.10
  - Megatron v0.8.0
  - Hugging Face Transformers v4.44.2
  - Hugging Face Datasets library v2.19.0
  - EFA v1.32.0
  - NCCL v2.21.5

### SMP Conda

channel

The following S3 bucket is the public Conda channel of the SMP library hosted by
the SMP service team. If you want to install the SMP v2 library in a Conda
environment such as SageMaker HyperPod clusters, use this Conda channel to properly
install the SMP library.

- `https://sagemaker-distributed-model-parallel.s3.us-west-2.amazonaws.com/smp-v2/`

For more information about Conda channels in general, see [Channels](https://docs.conda.io/projects/conda/en/latest/user-guide/concepts/channels.html "https://docs.conda.io/projects/conda/en/latest/user-guide/concepts/channels.html") in the _Conda documentation_.

## The SageMaker model parallelism

library v2.6.1

_Date: October 31, 2024_

### SMP library

updates

**Bug fixes**

- Fixed an `ImportError` issue that occurred when using older
  training scripts with SMP v2.6.0. This fixes the backward incompatibility
  with SMP v2.6.0.
- Added a `DeprecationWarning` for
  `torch.sagemaker.distributed.fsdp.checkpoint`. This module
  will be deprecated and removed in SMP v2.7.0. If you're currently using
  `torch.sagemaker.distributed.fsdp.checkpoint` in your code,
  you should plan to update your scripts before the release of SMP v2.7.0 to
  avoid issues in the future.
- Fixed a backward compatibility issue identified in SMP v2.6.0. This issue
  was related to the deprecation of the `USE_PG_WITH_UTIL`
  checkpoint method in SMP v2.6.0, which broke backward compatibility with
  previous versions of training scripts. To resolve this issue, re-run your
  PyTorch training jobs to pick up the latest SMP container packaged with SMP
  v2.6.1.

### SMP Docker

container

The SMP library team distributes Docker containers in replacement of the SageMaker
PyTorch framework containers. If you use the PyTorch estimator class in the SageMaker
Python SDK and specify distribution configuration to use SMP v2, SageMaker AI automatically
picks up the SMP Docker containers.

**Container details**

- SMP Docker container for PyTorch v2.4.1 with CUDA v12.1

```
658645717510.dkr.ecr.`<us-west-2>`.amazonaws.com/smdistributed-modelparallel:2.4.1-gpu-py311-cu121
```

- Pre-installed packages
  - The SMP library v2.6.1
  - The SMDDP library v2.5.0
  - CUDNN v9.4.0
  - FlashAttention v2.5.8
  - TransformerEngine v1.10
  - Megatron v0.8.0
  - Hugging Face Transformers v4.44.2
  - Hugging Face Datasets library v2.19.0
  - EFA v1.32.0
  - NCCL v2.21.5

### SMP Conda

channel

The following S3 bucket is the public Conda channel of the SMP library hosted by
the SMP service team. If you want to install the SMP v2 library in an environment of
highly customizable compute resources such as SageMaker HyperPod clusters, use this Conda
channel to properly install the SMP library.

- `https://sagemaker-distributed-model-parallel.s3.us-west-2.amazonaws.com/smp-v2/`

For more information about Conda channels in general, see [Channels](https://docs.conda.io/projects/conda/en/latest/user-guide/concepts/channels.html "https://docs.conda.io/projects/conda/en/latest/user-guide/concepts/channels.html") in the _Conda documentation_.

## The SageMaker model parallelism

library v2.6.0

_Date: October 17, 2024_

### SMP library

updates

**New features**

- Added support for the following LLM model configurations. You can start
  using [Context parallelism](model-parallel-core-features-v2-context-parallelism.md "model-parallel-core-features-v2-context-parallelism.md")
  and [Tensor
  parallelism](model-parallel-core-features-v2-tensor-parallelism.md "model-parallel-core-features-v2-tensor-parallelism.md").
  - [Llama3.1 8B](https://huggingface.co/meta-llama/Llama-3.1-8B "https://huggingface.co/meta-llama/Llama-3.1-8B")
  - [Llama3.1 70B](https://huggingface.co/meta-llama/Llama-3.1-70B "https://huggingface.co/meta-llama/Llama-3.1-70B")
  - [Mistral 7B](https://huggingface.co/mistralai/Mistral-7B-v0.3 "https://huggingface.co/mistralai/Mistral-7B-v0.3")

- Added [Tensor
  parallelism](model-parallel-core-features-v2-tensor-parallelism.md "model-parallel-core-features-v2-tensor-parallelism.md")
  support for the following Mixtral model configurations.
  - [Mixtral 8x7B](https://huggingface.co/mistralai/Mixtral-8x7B-v0.1 "https://huggingface.co/mistralai/Mixtral-8x7B-v0.1")
  - [Mixtral 8x22B](https://huggingface.co/mistralai/Mixtral-8x22B-v0.1 "https://huggingface.co/mistralai/Mixtral-8x22B-v0.1")

- Added support for an AllGather-based context parallelism implementation
  that utilizes the AllGather communication collective to obtain the full
  sequence of key-and-value tensors. Available implementations are
  `p2p` and `all_gather`. The `p2p`
  implementation utilizes peer-to-peer send-receive calls for key-and-value
  (KV) tensor accumulation during the attention computation, running
  asynchronously and allowing communication to overlap with computation. On
  the other hand, the `all_gather` implementation employs the
  `AllGather` communication collective operation for KV tensor
  accumulation. To learn how to apply these context parallelism
  implementation, see [Context parallelism](model-parallel-core-features-v2-context-parallelism.md "model-parallel-core-features-v2-context-parallelism.md").
- Added support for tuning the Rotary Position Embedding (RoPE) theta
  value.

**Bug fixes**

- Fixed a bug where Rotary Position Embedding (RoPE) isn’t properly
  initialized during pre-training when delayed parameter is enabled.

**Known issues**

- Transformer Engine does not currently support context parallelism or FP8
  with sliding window attention enabled. Thus, the SMP version of Mistral
  transformers don’t support context parallelism or FP8 training when sliding
  window configuration is set to a non-null value.

### SMP Docker

container

The SMP library team distributes Docker containers in replacement of the SageMaker
PyTorch framework containers. If you use the PyTorch estimator class in the SageMaker
Python SDK and specify distribution configuration to use SMP v2, SageMaker AI automatically
picks up the SMP Docker containers.

**Currency updates**

- Upgraded PyTorch to v2.4.1
- Upgraded Megatron to v0.8.0
- Upgraded the TransformerEngine library to v1.10
- Upgraded Transformers to v4.44.2
- Upgraded cuDNN to v9.4.0.58

**Container details**

- SMP Docker container for PyTorch v2.4.1 with CUDA v12.1

```
658645717510.dkr.ecr.`<us-west-2>`.amazonaws.com/smdistributed-modelparallel:2.4.1-gpu-py311-cu121
```

- Pre-installed packages
  - The SMP library v2.6.0
  - The SMDDP library v2.5.0
  - CUDNN v9.4.0
  - FlashAttention v2.5.8
  - TransformerEngine v1.10
  - Megatron v0.8.0
  - Hugging Face Transformers v4.44.2
  - Hugging Face Datasets library v2.19.0
  - EFA v1.32.0
  - NCCL v2.21.5

### SMP Conda

channel

The following S3 bucket is the public Conda channel of the SMP library hosted by
the SMP service team. If you want to install the SMP v2 library in an environment of
highly customizable compute resources such as SageMaker HyperPod clusters, use this Conda
channel to properly install the SMP library.

- `https://sagemaker-distributed-model-parallel.s3.us-west-2.amazonaws.com/smp-v2/`

For more information about Conda channels in general, see [Channels](https://docs.conda.io/projects/conda/en/latest/user-guide/concepts/channels.html "https://docs.conda.io/projects/conda/en/latest/user-guide/concepts/channels.html") in the _Conda documentation_.

## The SageMaker model parallelism

library v2.5.0

_Date: August 28, 2024_

### SMP library

updates

**New features**

- Added support for mixed-precision training using FP8 data format on P5
  instances for the Mixtral model.
  - Supported Mixtral configurations are 8x7B and 8x22B. To learn
    more, see [Mixed precision training with FP8 on P5 instances using Transformer
    Engine](model-parallel-core-features-v2-mixed-precision.md#model-parallel-core-features-v2-mixed-precision-fp8-training-on-p5 "model-parallel-core-features-v2-mixed-precision.md#model-parallel-core-features-v2-mixed-precision-fp8-training-on-p5").

- Added support for [Context parallelism](model-parallel-core-features-v2-context-parallelism.md "model-parallel-core-features-v2-context-parallelism.md") for the
  following model configurations.
  - Llama-v2: 7B and 70B
  - Llama-v3: 8B and 70B
  - GPT-NeoX: 20B

- Added support for saving checkpoints asynchronously. To learn more, see
  [Checkpointing using
  SMP](model-parallel-core-features-v2-checkpoints.md "model-parallel-core-features-v2-checkpoints.md").
  - Support for saving checkpoints to S3 directly without using Amazon EBS
    or file servers.

**Bug fixes**

- Resolved an issue that caused unexpectedly high initial loss during Llama
  fine-tuning when loading a pre-trained model checkpoint and utilizing tensor
  parallelism.

**Notes**

- To use activation checkpointing for Mixtral with FP8 mixed precision, you
  will need to checkpoint the attention and expert layers separately. For an
  example of setting it up properly, see the [example training script](https://github.com/aws/amazon-sagemaker-examples/blob/main/training/distributed_training/pytorch/model_parallel_v2/shared-scripts/train_utils.py "https://github.com/aws/amazon-sagemaker-examples/blob/main/training/distributed_training/pytorch/model_parallel_v2/shared-scripts/train_utils.py") in the _Amazon SageMaker AI Examples
  repository_.

**Known issues**

- The balanced load balancing type in the MoE configuration ([torch.sagemaker.moe.moe_config.MoEConfig](distributed-model-parallel-v2-reference.md#model-parallel-v2-torch-sagemaker-reference-moe "distributed-model-parallel-v2-reference.md#model-parallel-v2-torch-sagemaker-reference-moe")) is
  currently incompatible with activation checkpointing.
- With context parallelism, GPT-NeoX shows performance regression in both
  pre-training and fine-tuning.
- For GPT-NeoX on P4 instances, directly loading weights from a delayed
  parameter initialized transformed model into a Hugging Face transformer
  model leads to a loss mismatch on the first step.

### SMP Docker

container

The SMP library team distributes Docker containers in replacement of the SageMaker
PyTorch framework containers. If you use the PyTorch estimator class in the SageMaker
Python SDK and specify distribution configuration to use SMP v2, SageMaker AI automatically
picks up the SMP Docker containers. To use this release of SMP v2, upgrade your SageMaker
Python SDK to v2.224.0 or later.

**Currency updates**

- Upgraded the FlashAttention library to v2.5.8
- Upgraded the Transformer Engine library to v1.8
  - If you want to install Transformer Engine in a Conda environment,
    you need to build from the source and cherry-pick the specific
    upstream fixes ([744624d](https://github.com/NVIDIA/TransformerEngine/commit/744624d004f4514ffbaa90ac83e214311c86c607 "https://github.com/NVIDIA/TransformerEngine/commit/744624d004f4514ffbaa90ac83e214311c86c607"), [27c6342](https://github.com/NVIDIA/TransformerEngine/commit/27c6342ea8ad88034bf04b587dd13cb6088d2474 "https://github.com/NVIDIA/TransformerEngine/commit/27c6342ea8ad88034bf04b587dd13cb6088d2474"), [7669bf3](https://github.com/NVIDIA/TransformerEngine/commit/7669bf3da68074517b134cd6acebd04b221fd545 "https://github.com/NVIDIA/TransformerEngine/commit/7669bf3da68074517b134cd6acebd04b221fd545")).

**Container details**

- SMP Docker container for PyTorch v2.3.1 with CUDA v12.1

```
658645717510.dkr.ecr.`<region>`.amazonaws.com/smdistributed-modelparallel:2.3.1-gpu-py311-cu121
```

For a complete list of supported regions, see [AWS Regions](distributed-data-parallel-support.md#distributed-data-parallel-availablity-zone "distributed-data-parallel-support.md#distributed-data-parallel-availablity-zone").

- Pre-installed packages
  - The SMP library v2.5.0
  - The SMDDP library v2.3.0
  - CUDNN v8.9.7.29
  - FlashAttention v2.5.8
  - TransformerEngine v1.8
  - Megatron v0.7.0
  - Hugging Face Transformers v4.40.1
  - Hugging Face Datasets library v2.19.0
  - EFA v1.32.0
  - NCCL v2.21.5

### SMP Conda

channel

The following S3 bucket is the public Conda channel of the SMP library hosted by
the SMP service team. If you want to install the SMP v2 library in an environment of
highly customizable compute resources such as SageMaker HyperPod clusters, use this Conda
channel to properly install the SMP library.

- `https://sagemaker-distributed-model-parallel.s3.us-west-2.amazonaws.com/smp-v2/`

For more information about Conda channels in general, see [Channels](https://docs.conda.io/projects/conda/en/latest/user-guide/concepts/channels.html "https://docs.conda.io/projects/conda/en/latest/user-guide/concepts/channels.html") in the _Conda documentation_.

## The SageMaker model parallelism

library v2.4.0

_Date: June 20, 2024_

### SMP library

updates

**Bug fixes**

- Fixed a bug that causes incorrect logit shapes when labels are not passed
  in the forward pass while using the SMP Transformer.

**Currency updates**

- Added support for PyTorch v2.3.1.
- Added support for Python v3.11.
- Added support for the Hugging Face Transformers library v4.40.1.

**Deprecations**

- Discontinued support for Python v3.10.
- Discontinued support for the Hugging Face Transformers library versions
  before v4.40.1.

**Other changes**

- Included a patch to toggle saving de-duplicated tensors on different
  ranks. To learn more, see the [discussion
  thread](https://github.com/pytorch/pytorch/pull/126569 "https://github.com/pytorch/pytorch/pull/126569")in the PyTorch GitHub repository.

**Known issues**

- There is a known issue that the loss might spike and then resume at a
  higher loss value while fine-tuning Llama-3 70B with tensor
  parallelism.

### SMP Docker

container

The SMP library team distributes Docker containers in replacement of the SageMaker
PyTorch framework containers. If you use the PyTorch estimator class in the SageMaker
Python SDK and specify distribution configuration to use SMP v2, SageMaker AI automatically
picks up the SMP Docker containers. To use this release of SMP v2, upgrade your SageMaker
Python SDK to v2.224.0 or later.

**Currency updates**

- Upgraded the SMDDP library to v2.3.0.
- Upgraded the NCCL library to v2.21.5.
- Upgraded the EFA software to v1.32.0.

**Deprecations**

- Discontinued the installation of the [Torch Distributed
  Experimental (torchdistX) library](https://pytorch.org/torchdistx/latest/index.html "https://pytorch.org/torchdistx/latest/index.html").

**Container details**

- SMP Docker container for PyTorch v2.3.1 with CUDA v12.1

```
658645717510.dkr.ecr.`us-west-2`.amazonaws.com/smdistributed-modelparallel:2.3.1-gpu-py311-cu121
```

- Pre-installed packages
  - The SMP library v2.4.0
  - The SMDDP library v2.3.0
  - CUDNN v8.9.7.29
  - FlashAttention v2.3.3
  - TransformerEngine v1.2.1
  - Hugging Face Transformers v4.40.1
  - Hugging Face Datasets library v2.19.0
  - EFA v1.32.0
  - NCCL v2.21.5

### SMP Conda

channel

The following S3 bucket is the public Conda channel of the SMP library hosted by
the SMP service team. If you want to install the SMP v2 library in an environment of
highly customizable compute resources such as SageMaker HyperPod clusters, use this Conda
channel to properly install the SMP library.

- `https://sagemaker-distributed-model-parallel.s3.us-west-2.amazonaws.com/smp-v2/`

For more information about Conda channels in general, see [Channels](https://docs.conda.io/projects/conda/en/latest/user-guide/concepts/channels.html "https://docs.conda.io/projects/conda/en/latest/user-guide/concepts/channels.html") in the _Conda documentation_.

## The SageMaker model parallelism

library v2.3.1

_Date: May 9, 2024_

**Bug fixes**

- Fixed an `ImportError` issue when using
  `moe_load_balancing=balanced` in [torch.sagemaker.moe.moe_config.MoEConfig](distributed-model-parallel-v2-reference.md#model-parallel-v2-torch-sagemaker-reference-moe "distributed-model-parallel-v2-reference.md#model-parallel-v2-torch-sagemaker-reference-moe") for expert
  parallelism.
- Fixed a fine-tuning issue where the [torch.sagemaker.transform](distributed-model-parallel-v2-reference.md#model-parallel-v2-torch-sagemaker-reference-transform "distributed-model-parallel-v2-reference.md#model-parallel-v2-torch-sagemaker-reference-transform") call
  raised `KeyError` when `load_state_dict_from_rank0` is
  enabled.
- Fixed an out-of-memory (OOM) error raised when loading large Mixture of
  Experts (MoE) models, such as Mixtral 8x22B, for fine-tuning.

**SMP Docker container**

The SMP library team distributes Docker containers in replacement of the SageMaker PyTorch
framework containers. This release incorporates the aforementioned bug fixes into the
following SMP Docker image.

- SMP Docker container for PyTorch v2.2.0 with CUDA v12.1

```
658645717510.dkr.ecr.`us-west-2`.amazonaws.com/smdistributed-modelparallel:2.2.0-gpu-py310-cu121
```

## The SageMaker model parallelism

library v2.3.0

_Date: April 11, 2024_

**New features**

- Added a new core feature, _expert parallelism_, to support
  Mixture of Experts transformer models. To learn more, see [Expert
  parallelism](model-parallel-core-features-v2-expert-parallelism.md "model-parallel-core-features-v2-expert-parallelism.md").

**SMP Docker container**

The SMP library team distributes Docker containers in replacement of the SageMaker PyTorch
framework containers. If you use the PyTorch estimator class in the SageMaker Python SDK and
specify distribution configuration to use SMP v2, SageMaker automatically picks up the SMP
Docker containers. To use this release of SMP v2, upgrade your SageMaker Python SDK to
v2.214.4 or later.

- SMP Docker container for PyTorch v2.2.0 with CUDA v12.1

```
658645717510.dkr.ecr.`us-west-2`.amazonaws.com/smdistributed-modelparallel:2.2.0-gpu-py310-cu121
```

    + Pre-installed packages in this Docker container




    	- The SMDDP library v2.2.0
    	- CUDNN v8.9.5.29
    	- FlashAttention v2.3.3
    	- TransformerEngine v1.2.1
    	- Hugging Face Transformers v4.37.1
    	- Hugging Face Datasets library v2.16.1
    	- Megatron-core 0.5.0
    	- EFA v1.30.0
    	- NCCL v2.19.4

## The SageMaker model parallelism

library v2.2.0

_Date: March 7, 2024_

**New Features**

- Added support for [FP8 training](model-parallel-core-features-v2-mixed-precision.md#model-parallel-core-features-v2-mixed-precision-fp8-training-on-p5 "model-parallel-core-features-v2-mixed-precision.md#model-parallel-core-features-v2-mixed-precision-fp8-training-on-p5") of the following Hugging Face transformer models on P5
  instances with Transformer Engine integration:
  - GPT-NeoX
  - Llama 2

**Bug Fixes**

- Fixed a bug where tensors were not guaranteed to be contiguous before the
  `AllGather` collective call during tensor parallelism
  training.

**Currency Updates**

- Added support for PyTorch v2.2.0.
- Upgraded the SMDDP library to v2.2.0.
- Upgraded the FlashAttention library to v2.3.3.
- Upgraded the NCCL library to v2.19.4.

**Deprecation**

- Discontinued support for Transformer Engine versions before v1.2.0.

**Known issues**

- The SMP [Activation
  offloading](model-parallel-core-features-v2-pytorch-activation-offloading.md "model-parallel-core-features-v2-pytorch-activation-offloading.md")
  feature currently does not work. Use the native PyTorch activation offloading
  instead.

**Other changes**

- Included a patch to fix the performance regression discussed in the issue
  thread at [https://github.com/pytorch/pytorch/issues/117748](https://github.com/pytorch/pytorch/issues/117748 "https://github.com/pytorch/pytorch/issues/117748") in the PyTorch
  GitHub repository.

**SMP Docker container**

The SMP library team distributes Docker containers in replacement of the SageMaker PyTorch
framework containers. If you use the PyTorch estimator class in the SageMaker Python SDK and
specify distribution configuration to use SMP v2, SageMaker AI automatically picks up the SMP
Docker containers. To use this release of SMP v2, upgrade your SageMaker Python SDK to
v2.212.0 or later.

- SMP Docker container for PyTorch v2.2.0 with CUDA v12.1

```
658645717510.dkr.ecr.`us-west-2`.amazonaws.com/smdistributed-modelparallel:2.2.0-gpu-py310-cu121
```

    + Available for P4d, P4de, and P5 instances
    + Pre-installed packages in this Docker container




    	- The SMDDP library v2.2.0
    	- CUDNN v8.9.5.29
    	- FlashAttention v2.3.3
    	- TransformerEngine v1.2.1
    	- Hugging Face Transformers v4.37.1
    	- Hugging Face Datasets library v2.16.1
    	- EFA v1.30.0
    	- NCCL v2.19.4

## The SageMaker model parallelism

library v2.1.0

_Date: February 6, 2024_

**Currency Updates**

- Added support for PyTorch v2.1.2.

**Deprecation**

- Discontinued support for Hugging Face Transformers v4.31.0.

**Known issues**

- An issue is discovered that fine-tuning of the Hugging Face Llama 2 model with
  `attn_implementation=flash_attention_2` and FSDP causes the model
  to diverge. For reference, see the [issue
  ticket](https://github.com/huggingface/transformers/issues/28826 "https://github.com/huggingface/transformers/issues/28826") in the _Hugging Face Transformers
  GitHub repository_. To avoid the divergence issue, use
  `attn_implementation=sdpa`. Alternatively, use the SMP
  transformer model implementation by setting up
  `use_smp_implementation=True`.

**SMP Docker container**

The SMP library team distributes Docker containers in replacement of the SageMaker PyTorch
framework containers. If you use the PyTorch estimator class in the SageMaker Python SDK and
specify distribution configuration to use SMP v2, SageMaker automatically picks up the SMP
Docker containers. To use this release of SMP v2, upgrade your SageMaker Python SDK to
v2.207.0 or later.

- SMP Docker container for PyTorch v2.1.2 with CUDA v12.1

```
658645717510.dkr.ecr.`us-west-2`.amazonaws.com/smdistributed-modelparallel:2.1.2-gpu-py310-cu121
```

    + Available for P4d, P4de, and P5 instances
    + Pre-installed packages in this Docker container




    	- The SMDDP library v2.1.0
    	- CUDNN v8.9.5.29
    	- FlashAttention v2.3.3
    	- TransformerEngine v1.2.1
    	- Hugging Face Transformers v4.37.1
    	- Hugging Face Datasets library v2.16.1
    	- EFA v1.30.0

**SMP Conda channel**

The following S3 bucket is a public Conda channel hosted by the SMP service team. If
you want to install the SMP v2 library in an environment of highly customizable compute
resources such as SageMaker HyperPod clusters, use this Conda channel to properly install the
SMP library.

- `https://sagemaker-distributed-model-parallel.s3.us-west-2.amazonaws.com/smp-v2/`

For more information about Conda channels in general, see [Channels](https://docs.conda.io/projects/conda/en/latest/user-guide/concepts/channels.html "https://docs.conda.io/projects/conda/en/latest/user-guide/concepts/channels.html") in the _Conda documentation_.

## The SageMaker model parallelism

library v2.0.0

_Date: December 19, 2023_

**New features**

Released the SageMaker model parallelism (SMP) library v2.0.0 with the following new
offerings.

- A new `torch.sagemaker` package, entirely revamped from the
  previous `smdistributed.modelparallel.torch` package in SMP v1.x.
- Support for PyTorch 2.0.1.
- Support for PyTorch FSDP.
- Tensor parallelism implementation by integrating with the [Transformer Engine](https://docs.nvidia.com/deeplearning/transformer-engine/index.html "https://docs.nvidia.com/deeplearning/transformer-engine/index.html") library.
- Support for both [SageMaker Training](train-model.md "train-model.md") and [SageMaker HyperPod](sagemaker-hyperpod.md "sagemaker-hyperpod.md").

**Breaking changes**

- SMP v2 revamped the APIs entirely and provides the
  `torch.sagemaker` package. Mostly, you only need to initialize
  with the `torch.sagemaker.init()` module and pass model parallel
  configuration parameters. With this new package, you can significantly simplify
  code modifications in your training script. To learn more about adapting your
  training script to use SMP v2, see [Use the SageMaker model parallelism
  library v2](model-parallel-use-api-v2.md "model-parallel-use-api-v2.md").
- If you've used SMP v1 for training Hugging Face Transformer models and want to
  reuse the models in SMP v2, see [Upgrade from SMP v1 to SMP v2](distributed-model-parallel-v2-reference.md#model-parallel-v2-upgrade-from-v1 "distributed-model-parallel-v2-reference.md#model-parallel-v2-upgrade-from-v1").
- For PyTorch FSDP training, you should use SMP v2.

**Known issues**

- Activation checkpointing currently only works with the following wrapping
  policies with FSDP.
  - `auto_wrap_policy =
functools.partial(transformer_auto_wrap_policy, ...)`

- To use [Activation
  offloading](model-parallel-core-features-v2-pytorch-activation-offloading.md "model-parallel-core-features-v2-pytorch-activation-offloading.md"),
  FSDP activation checkpointing type must be [REENTRANT](https://pytorch.org/docs/stable/checkpoint.html "https://pytorch.org/docs/stable/checkpoint.html").
- When running with tensor parallel enabled with the sharded data parallel
  degree set to `1`, you must use `backend = nccl`. The
  `smddp` backend option is not supported in this scenario.
- [Transformer Engine](https://docs.nvidia.com/deeplearning/transformer-engine/index.html "https://docs.nvidia.com/deeplearning/transformer-engine/index.html") is required to use PyTorch with the SMP library
  even when not using tensor parallelism.

**Other changes**

- Starting from this release, the documentation for the SageMaker model parallelism
  library is fully available in this _Amazon SageMaker AI Developer
  Guide_. In favor of this complete developer guide for SMP v2 in the
  _Amazon SageMaker AI Developer Guide_, the [additional reference for SMP v1.x](https://sagemaker.readthedocs.io/en/stable/api/training/distributed.html#the-sagemaker-distributed-model-parallel-library "https://sagemaker.readthedocs.io/en/stable/api/training/distributed.html#the-sagemaker-distributed-model-parallel-library") in the _SageMaker Python SDK
  documentation_ is deprecated. If you still need the documentation
  for SMP v1.x, the developer guide for SMP v1.x is available at [(Archived) SageMaker model parallelism library v1.x](model-parallel.md "model-parallel.md"), and the SMP Python library v1.x reference is
  available in the [SageMaker Python SDK v2.199.0 documentation](https://sagemaker.readthedocs.io/en/v2.199.0/api/training/smd_model_parallel_release_notes/smd_model_parallel_change_log.html "https://sagemaker.readthedocs.io/en/v2.199.0/api/training/smd_model_parallel_release_notes/smd_model_parallel_change_log.html").

**Deprecations**

- Discontinued support for TensorFlow.
- There is no pipeline parallelism support in SMP v2.
- There is no support for the DeepSpeed library in favor of native PyTorch
  FSDP.

**SMP Docker container**

The SMP library team distributes Docker containers in replacement of the SageMaker PyTorch
framework containers. If you use the PyTorch estimator class in the SageMaker Python SDK and
specify distribution configuration to use SMP v2, SageMaker AI automatically picks up the SMP
Docker containers. To use this release of SMP v2, upgrade your SageMaker Python SDK to
v2.207.0 or later.

- SMP Docker container for PyTorch v2.0.1 with CUDA v12.1

```
658645717510.dkr.ecr.`us-west-2`.amazonaws.com/smdistributed-modelparallel:2.0.1-gpu-py310-cu121
```
