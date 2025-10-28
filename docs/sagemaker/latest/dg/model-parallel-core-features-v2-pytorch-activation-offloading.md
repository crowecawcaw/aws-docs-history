# Activation

offloading

###### Important

In SMP v2.2.0, the activation offloading functionality of the SMP library doesn't
work. Use the native PyTorch activation offloading instead.

Typically, the forward pass computes activations at each layer and keeps them in GPU
memory until the backward pass for the corresponding layer finishes. Offloading these
tensors to CPU memory after forward pass and fetching them back to GPU when they are
needed can save substantial GPU memory usage. PyTorch supports offloading activations,
but the implementation causes GPUs to be idle while activations are fetched back from
CPU during backward pass. This causes a major performance degradation when using
activation offloading.

SMP v2 improves this activation offloading. It pre-fetches activations ahead of time
before the activations are needed for the GPU to start backward pass on those
activations. The pre-fetching feature helps training progresses be run more efficiently
without idle GPUs. This results in offering benefits from lower memory usage without a
performance degradation.

You can keep the native PyTorch modules for offloading activations in your training
script. The following is an example structure of applying the SMP activation offloading
feature in your script. Note that activation offloading is applicable _only_ when used together with [Activation checkpointing](model-parallel-core-features-v2-pytorch-activation-checkpointing.md "model-parallel-core-features-v2-pytorch-activation-checkpointing.md"). To
learn more about the native PyTorch checkpoint tools for activation offloading,
see:

- [checkpoint_wrapper.py](https://github.com/pytorch/pytorch/blob/v2.0.1/torch/distributed/algorithms/_checkpoint/checkpoint_wrapper.py#L171 "https://github.com/pytorch/pytorch/blob/v2.0.1/torch/distributed/algorithms/_checkpoint/checkpoint_wrapper.py#L171") in the _PyTorch GitHub
  repository_
- [Activation Checkpointing](https://pytorch.org/blog/scaling-multimodal-foundation-models-in-torchmultimodal-with-pytorch-distributed/#activation-checkpointing "https://pytorch.org/blog/scaling-multimodal-foundation-models-in-torchmultimodal-with-pytorch-distributed/#activation-checkpointing") in the PyTorch blog _Scaling Multi-modal Foundation Models in TorchMultimodal with
  PyTorch Distributed_.
  You can apply the SMP activation offloading feature on [PyTorch activation checkpointing](https://pytorch.org/blog/scaling-multimodal-foundation-models-in-torchmultimodal-with-pytorch-distributed/#activation-checkpointing "https://pytorch.org/blog/scaling-multimodal-foundation-models-in-torchmultimodal-with-pytorch-distributed/#activation-checkpointing"). This is done by adding the
  `sm_activation_offloading` and `activation_loading_horizon`
  parameters to the SMP configuration dictionary during [Step 2: Launch a training
  job](model-parallel-use-api-v2.md#model-parallel-launch-a-training-job-v2 "model-parallel-use-api-v2.md#model-parallel-launch-a-training-job-v2").

The following code snippets show how to add the SMP initialization module
`torch.sagemaker.init()` to your training script and set up the SMP
configuration dictionary in JSON format for training job launcher while following the
two-step process introduced in [Use the SageMaker model parallelism
library v2](model-parallel-use-api-v2.md "model-parallel-use-api-v2.md"). You don’t
need to make any changes to your PyTorch model or [PyTorch FSDP](https://pytorch.org/docs/stable/fsdp.html#module-torch.distributed.fsdp "https://pytorch.org/docs/stable/fsdp.html#module-torch.distributed.fsdp") configuration. For more information about the
`sm_activation_offloading` and `activation_loading_horizon`
parameters, see [SMP v2 core
feature configuration parameters](distributed-model-parallel-v2-reference.md#distributed-model-parallel-v2-reference-init-config "distributed-model-parallel-v2-reference.md#distributed-model-parallel-v2-reference-init-config").

**SMP configuration**

```
{
    "activation_loading_horizon": 2,
    "sm_activation_offloading": True
}
```

**In training script**

###### Note

While activating the SMP activation offloading feature, make sure that you also
use the PyTorch `offload_wrapper` function and apply it to the root
module. The SMP activation offloading feature uses the root module to determine when
forward pass is done to start pre-fetching.

```
**import torch.sagemaker as tsm
tsm.init()**

# Native PyTorch module for activation offloading
from torch.distributed.algorithms._checkpoint.checkpoint_wrapper import (
    apply_activation_checkpointing,
    offload_wrapper,
)

model = FSDP(...)

# Activation offloading requires activation checkpointing.
apply_activation_checkpointing(
    model,
    check_fn=`checkpoint_transformer_layers_policy`,
)

**model = offload\_wrapper(model)**
```
