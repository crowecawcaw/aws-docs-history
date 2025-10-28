# Expert

parallelism

A _Mixture of Experts_ (MoE) model is a type of
transformer model that employs a _sparse_ approach, making it lighter
for training compared to training traditional dense models. In this MoE neural network
architecture, only a subset of the model's components called
_experts_ are utilized for each input. This approach offers
several advantages, including more efficient training and faster inference, even with a
larger model size. In other words, with the same compute budget for training a full
dense model, you can fit a larger model or dataset when using MoE.

An MoE model consists of multiple _experts_, each
consisting of a neural network, typically a feed-forward network (FFN). A gate network
called _router_ determines which tokens are sent to
which expert. These experts specialize in processing specific aspects of the input data,
enabling the model to train faster, reduce compute cost, while achieving the same
performance quality as its counterpart dense model. To learn more about Mixture of
Experts in general, refer to the blog [Applying Mixture of Experts in LLM Architectures](https://developer.nvidia.com/blog/applying-mixture-of-experts-in-llm-architectures/ "https://developer.nvidia.com/blog/applying-mixture-of-experts-in-llm-architectures/") in the _NVIDIA developer website_.

_Expert parallelism_ is a type of parallelism that
handles splitting experts of an MoE model across GPU devices.

SMP v2 integrates with [NVIDIA
Megatron](https://github.com/NVIDIA/Megatron-LM "https://github.com/NVIDIA/Megatron-LM") for implementing expert parallelism to support training MoE models,
and runs on top of PyTorch FSDP APIs. You keep using your PyTorch FSDP training code as
is and activate SMP expert parallelism for training MoE models.

## Hugging Face Transformer models compatible with SMP expert parallelism

SMP v2 currently offers expert parallelism support for the following Hugging Face
transformer models.

- [Mixtral](https://huggingface.co/docs/transformers/en/model_doc/mixtral "https://huggingface.co/docs/transformers/en/model_doc/mixtral")

## Configure expert parallelism

For `expert_parallel_degree`, you select a value for the degree of
expert parallelism. The value must evenly divide the number of GPUs in your cluster.
For example, to shard your model while using an instance with 8 GPUs, choose 2, 4,
or 8. We recommend that you start with a small number, and gradually increase it
until the model fits in the GPU memory.

The following code snippets show how to add the SMP initialization module
`torch.sagemaker.init()` to your training script and set up the SMP
configuration dictionary in JSON format for training job launcher while following
the two-step process introduced in [Use the SageMaker model parallelism
library v2](model-parallel-use-api-v2.md "model-parallel-use-api-v2.md"). You
don’t need to make any changes to your PyTorch model or [PyTorch FSDP](https://pytorch.org/docs/stable/fsdp.html#module-torch.distributed.fsdp "https://pytorch.org/docs/stable/fsdp.html#module-torch.distributed.fsdp") configuration. For more information about the
`expert_parallel_degree` parameter, see [SMP v2 core
feature configuration parameters](distributed-model-parallel-v2-reference.md#distributed-model-parallel-v2-reference-init-config "distributed-model-parallel-v2-reference.md#distributed-model-parallel-v2-reference-init-config").

###### Note

You can use expert parallelism with [Hybrid
sharded data parallelism](model-parallel-core-features-v2-sharded-data-parallelism.md "model-parallel-core-features-v2-sharded-data-parallelism.md"). Note
that expert parallelism is currently not compatible with tensor
parallelism.

###### Note

This expert parallelism training feature is available in the following
combination of libraries of SageMaker and the PyTorch library:

- SMP v2.3.0 and later
- The SageMaker Python SDK v2.214.4 and later
- PyTorch v2.2.0 and later

### In your training script

As part of [Step
1](model-parallel-use-api-v2.md#model-parallel-adapt-pytorch-script-v2 "model-parallel-use-api-v2.md#model-parallel-adapt-pytorch-script-v2"), initialize your script with `torch.sagemaker.init()` to
activate SMP v2 and wrap your model with the [torch.sagemaker.transform](distributed-model-parallel-v2-reference.md#model-parallel-v2-torch-sagemaker-reference-transform "distributed-model-parallel-v2-reference.md#model-parallel-v2-torch-sagemaker-reference-transform") API,
adding the `config` parameter to the API to activate MoE. The
following code snippet shows how to activate SMP MoE for the generic model class
`AutoModelForCausalLM` pulling an MoE transformer model
configuration using the `from_config` method for training from
scratch, or the `from_pretrained` method for fine-tuning. To learn
more about the SMP `MoEConfig` class, see [torch.sagemaker.moe.moe_config.MoEConfig](distributed-model-parallel-v2-reference.md#model-parallel-v2-torch-sagemaker-reference-moe "distributed-model-parallel-v2-reference.md#model-parallel-v2-torch-sagemaker-reference-moe").

```
# Import the torch.sagemaker.transform API and initialize.
**import torch.sagemaker as tsm
tsm.init()**

# Import transformers AutoModelForCausalLM class.
from transformers import AutoModelForCausalLM

# Import the SMP-implementation of MoE configuration class.
**from torch.sagemaker.moe.moe\_config import MoEConfig**

# Define a transformer model with an MoE model configuration
model = AutoModelForCausalLM.from_config(`MoEModelConfig`)

# Wrap it by torch.sagemaker.transform with the SMP MoE configuration.
**model = tsm.transform**(
    model,
    **config=MoEConfig(
 smp\_moe=`True`,
 random\_seed=`12345`,
 moe\_load\_balancing="`sinkhorn`",
 global\_token\_shuffle=`False`,
 moe\_all\_to\_all\_dispatcher=`True`,
 moe\_aux\_loss\_coeff=`0.001`,
 moe\_z\_loss\_coeff=`0.001`
 )**
)
```

### SMP configuration

As part of [Step
2](model-parallel-use-api-v2.md#model-parallel-launch-a-training-job-v2 "model-parallel-use-api-v2.md#model-parallel-launch-a-training-job-v2"), add the following parameter to the SMP configuration dictionary
for the SageMaker PyTorch estimator.

```
{
    ..., # other SMP config parameters
    "expert_parallel_degree": `8`
}
```
