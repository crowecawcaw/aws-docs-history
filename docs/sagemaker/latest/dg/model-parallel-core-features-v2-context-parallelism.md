# Context parallelism

_Context parallelism_ is a type of model parallelism
that partitions the model activations along the sequence dimension. Unlike other [sequence parallelism](https://arxiv.org/abs/2205.05198 "https://arxiv.org/abs/2205.05198") techniques,
which only partition the `LayerNorm` and `RMSNorm`, context
parallelism partitions the network inputs and all intermediate activations along the
sequence dimension.

SMP v2 integrates with [Transformer
Engine](https://docs.nvidia.com/deeplearning/transformer-engine/index.html "https://docs.nvidia.com/deeplearning/transformer-engine/index.html") for context parallelism and can be used in conjunction with PyTorch
FSDP and SMP [Tensor
parallelism](model-parallel-core-features-v2-tensor-parallelism.md "model-parallel-core-features-v2-tensor-parallelism.md"). You
can enable all three parallelisms simultaneously for model training. Context parallelism
is beneficial for training models with large activation sizes and long sequence lengths.
It accelerates the computation of attention scores and attention outputs, by allowing
each device to computes only a part of the scores and outputs along the sequence
dimension. While tensor parallelism also accelerates computation through partitioning
along the hidden dimension, the advantage of context parallelism is more substantial
since computational requirements increase quadratically with sequence dimension.

## Hugging Face Transformer models compatible with SMP context

parallelism

SMP v2 currently offers context parallelism support for the following Hugging Face
transformer models.

- GPT-NeoX
- Llama 2 and Llama 3
- [Mistral
  7B](https://huggingface.co/mistralai/Mistral-7B-v0.3 "https://huggingface.co/mistralai/Mistral-7B-v0.3")

## Configure context parallelism

Set an integer value to the `context_parallel_degree` parameter that
evenly divides the number of GPUs in your cluster. For example, if you have an 8-GPU
instance, use 2, 4, or 8 for `context_parallel_degree`. We recommend
starting with a small `context_parallel_degree` value and gradually
increasing it until the model fits in the GPU memory with the required input
sequence length.

The following code snippets show how to add the SMP initialization module
`torch.sagemaker.init()` to your training script and set up the SMP
configuration dictionary in JSON format for training job launcher while following
the two-step process introduced in [Use the SageMaker model parallelism
library v2](model-parallel-use-api-v2.md "model-parallel-use-api-v2.md"). You
don’t need to make any changes to your PyTorch model or [PyTorch FSDP](https://pytorch.org/docs/stable/fsdp.html#module-torch.distributed.fsdp "https://pytorch.org/docs/stable/fsdp.html#module-torch.distributed.fsdp") configuration. For more information about the
`context_parallel_degree` parameter, see [SMP v2 core
feature configuration parameters](distributed-model-parallel-v2-reference.md#distributed-model-parallel-v2-reference-init-config "distributed-model-parallel-v2-reference.md#distributed-model-parallel-v2-reference-init-config").

### In your training script

As part of [Step
1](model-parallel-use-api-v2.md#model-parallel-adapt-pytorch-script-v2 "model-parallel-use-api-v2.md#model-parallel-adapt-pytorch-script-v2"), initialize your script with `torch.sagemaker.init()` to
activate SMP v2 and wrap your model with the [torch.sagemaker.transform](distributed-model-parallel-v2-reference.md#model-parallel-v2-torch-sagemaker-reference-transform "distributed-model-parallel-v2-reference.md#model-parallel-v2-torch-sagemaker-reference-transform") API.

Starting from SMP v2.6.0, you can use the argument `cp_comm_type`
to determine which context parallelism implementation to use. The SMP library
currently supports two implementations: `p2p` and
`all_gather`. The `p2p` implementation uses
peer-to-peer send-receive calls for key-value accumulation during the attention
implementation and runs asynchronously, allowing overlaps with compute.
`all_gather` implementation, instead, uses the
`AllGather` collective operation and runs synchronously.

```
import torch.sagemaker as tsm
tsm.init()

from transformers import AutoModelForCausalLM
model = AutoModelForCausalLM.from_config(..)
model = tsm.transform(model, cp_comm_type="p2p")
```

### SMP configuration

As part of [Step
2](model-parallel-use-api-v2.md#model-parallel-launch-a-training-job-v2 "model-parallel-use-api-v2.md#model-parallel-launch-a-training-job-v2"), add the following parameter to the SMP configuration dictionary
for the SageMaker PyTorch estimator.

```
{
    ..., # other SMP config parameters
    "context_parallel_degree": 2
}
```
