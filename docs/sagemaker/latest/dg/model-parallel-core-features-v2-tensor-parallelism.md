# Tensor

parallelism

_Tensor parallelism_ is a type of model parallelism
in which specific model weights, gradients, and optimizer states are split across
devices. In contrast to pipeline parallelism, which keeps individual weights intact but
partitions the _set_ of weights, gradients, or
optimizer across devices, tensor parallelism shards _individual_ weights. This typically involves distributed computation of
specific operations, modules, or layers of the model.

Tensor parallelism is required in cases in which a single parameter consumes most of
the GPU memory (such as large embedding tables with a large vocabulary size or a large
softmax layer with a large number of classes). In this case, treating this large tensor
or operation as an atomic unit is inefficient and impedes balance of the memory
load.

SMP v2 integrates with [Transformer
Engine](https://docs.nvidia.com/deeplearning/transformer-engine/index.html "https://docs.nvidia.com/deeplearning/transformer-engine/index.html") for the implementation for tensor parallelism, and runs on top of
PyTorch FSDP APIs. You can enable PyTorch FSDP and SMP tensor parallelism
simultaneously, and determine the best model parallelism for best performance.

In practice, tensor parallelism is especially helpful in the following
scenarios.

- When training with long context lengths as that leads to high activation
  memory with FSDP alone.
- When training with really large clusters on which the global batch size
  exceeds desired limits.

## Hugging Face Transformer models compatible with the SMP tensor

parallelism

SMP v2 currently offers tensor parallelism support for the following Hugging Face
transformer models.

- GPT-NeoX
- Llama 2
- Llama 3
- [Mistral
  7B](https://huggingface.co/mistralai/Mistral-7B-v0.3 "https://huggingface.co/mistralai/Mistral-7B-v0.3")
- [Mixtral
  8x7B](https://huggingface.co/mistralai/Mixtral-8x7B-v0.1 "https://huggingface.co/mistralai/Mixtral-8x7B-v0.1")
- [Mixtral
  8x22B](https://huggingface.co/mistralai/Mixtral-8x22B-v0.1 "https://huggingface.co/mistralai/Mixtral-8x22B-v0.1")

For reference configuration for applying tensor parallelism on these models, see
[Configuration tips](model-parallel-best-practices-v2.md#model-parallel-best-practices-v2-config-tips "model-parallel-best-practices-v2.md#model-parallel-best-practices-v2-config-tips").

## Configure tensor parallelism

For `tensor_parallel_degree`, you select a value for the degree of
tensor parallelism. The value must evenly divide the number of GPUs in your cluster.
For example, to shard your model while using an instance with 8 GPUs, choose 2, 4,
or 8. We recommend that you start with a small number, and gradually increase it
until the model fits in the GPU memory.

The following code snippets show how to add the SMP initialization module
`torch.sagemaker.init()` to your training script and set up the SMP
configuration dictionary in JSON format for training job launcher while following
the two-step process introduced in [Use the SageMaker model parallelism
library v2](model-parallel-use-api-v2.md "model-parallel-use-api-v2.md"). You
don’t need to make any changes to your PyTorch model or [PyTorch FSDP](https://pytorch.org/docs/stable/fsdp.html#module-torch.distributed.fsdp "https://pytorch.org/docs/stable/fsdp.html#module-torch.distributed.fsdp") configuration. For more information about the
`tensor_parallel_degree` and `random_seed` parameters, see
[SMP v2 core
feature configuration parameters](distributed-model-parallel-v2-reference.md#distributed-model-parallel-v2-reference-init-config "distributed-model-parallel-v2-reference.md#distributed-model-parallel-v2-reference-init-config").

**SMP configuration**

```
{
    "tensor_parallel_degree": 8,
    "random_seed": 0
}
```

**In your training script**

Initialize with `torch.sagemaker.init()` to activate SMP v2 and wrap
your model with the [torch.sagemaker.transform](distributed-model-parallel-v2-reference.md#model-parallel-v2-torch-sagemaker-reference-transform "distributed-model-parallel-v2-reference.md#model-parallel-v2-torch-sagemaker-reference-transform") API.

```
**import torch.sagemaker as tsm
tsm.init()**

from transformers import AutoModelForCausalLM
model = AutoModelForCausalLM.from_config(..)
**model = tsm.transform(model)**
```

## Saving and loading Hugging Face Transformer checkpoints

After the SMP library transforms a model, it changes the state dictionary
(`state_dict`) of the model. This means that the model becomes
incompatible with the original Hugging Face Transformer checkpointing
functionalities. To handle this, the SMP library provides APIs to save checkpoints
from a transformed model in Hugging Face Transformer representation, and the
`torch.sagemaker.transform` API to load a Hugging Face Transformer
model checkpoint for fine-tuning.

For more information about saving checkpoints while using the tensor parallelism
feature of SMP v2, see [Checkpointing using
SMP](model-parallel-core-features-v2-checkpoints.md "model-parallel-core-features-v2-checkpoints.md").

For more information about fine-tuning a model applying the tensor parallelism
feature of SMP v2, see [Fine-tuning](model-parallel-core-features-v2-fine-tuning.md "model-parallel-core-features-v2-fine-tuning.md").
