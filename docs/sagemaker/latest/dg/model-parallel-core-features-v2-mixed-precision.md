# Mixed precision

training

The SageMaker model parallelism (SMP) library v2 supports mixed precision training out of
the box by integrating with open source frameworks such as PyTorch FSDP and Transformer
Engine. To learn more, see the following topics.

###### Topics

- [Mixed precision training with FP8 on P5 instances using Transformer
  Engine](#model-parallel-core-features-v2-mixed-precision-fp8-training-on-p5 "#model-parallel-core-features-v2-mixed-precision-fp8-training-on-p5")
- [Mixed precision training with half-precision data types using PyTorch
  FSDP](#model-parallel-core-features-v2-mixed-precision-half-precision "#model-parallel-core-features-v2-mixed-precision-half-precision")

## Mixed precision training with FP8 on P5 instances using Transformer

Engine

Starting from the SageMaker model parallelism (SMP) library v2.2.0, the SMP library
integrates with [Transformer Engine](https://docs.nvidia.com/deeplearning/transformer-engine/index.html "https://docs.nvidia.com/deeplearning/transformer-engine/index.html") and supports [FP8 mixed precision training](https://docs.nvidia.com/deeplearning/transformer-engine/user-guide/examples/fp8_primer.html "https://docs.nvidia.com/deeplearning/transformer-engine/user-guide/examples/fp8_primer.html") out of the box, keeping compatibility with
[PyTorch FSDP `MixedPrecision`](https://pytorch.org/docs/stable/fsdp.html#torch.distributed.fsdp.MixedPrecision "https://pytorch.org/docs/stable/fsdp.html#torch.distributed.fsdp.MixedPrecision"). This means that you can use
both PyTorch FSDP for mixed precision training and Transformer Engine for FP8
training. For model layers not supported by Transformer Engine's FP8 training
feature, those layers fall back to PyTorch FSDP mixed precision.

###### Note

SMP v2 offers FP8 support for the following Hugging Face Transformer
models:

- GPT-NeoX (available in SMP v2.2.0 and later)
- Llama 2 (available in SMP v2.2.0 and later)
- Mixtral 8x7b and Mixtral 8x22b (available in SMP v2.5.0 and
  later)

###### Note

This FP8 training on the P5 feature is available in the following combination
of libraries of SageMaker and the PyTorch library:

- The SageMaker Python SDK v2.212.0 and later
- PyTorch v2.2.0 and later

_FP8_ (8-bit floating point precision) is a data
type that has emerged as another paradigm to accelerate deep learning training of
LLM models. With the release of NVIDIA H100 GPUs supporting FP8 data types, you can
benefit from the advantages from the performance improvements on P5 instances
equipped with the H100 GPUs, while accelerating distributed training with FP8 mixed
precision training.

The FP8 data type further branches down to E4M3 and E5M2 formats. _E4M3_ offers a better precision, has a limited dynamic
range, and is ideal for the forward pass in model training. _E5M2_ has a broader dynamic range, but reduced precision, and is
better suited for the backward pass, where precision is less critical and a wider
dynamic range becomes beneficial. Hence, we recommend that you use the [hybrid FP8 strategy recipe](https://docs.nvidia.com/deeplearning/transformer-engine/user-guide/examples/fp8_primer.html#FP8-recipe "https://docs.nvidia.com/deeplearning/transformer-engine/user-guide/examples/fp8_primer.html#FP8-recipe") to leverage these characteristics
effectively.

For half-precision data types (FP16 and BF16), global loss-scaling techniques such
as static loss-scaling or dynamic loss-scaling handle convergence issues that arise
from information loss due to rounding gradients in half-precision. However, the
dynamic range of FP8 is even narrower, and the global loss scaling techniques are
not sufficient. At this point, we need a finer-grained per-tensor scaling technique.
_Delayed scaling_ is a strategy that selects a
scaling factor based on the maximum absolute values observed in a number of tensors
form previous iterations. There's a trade-off in this strategy; it uses the full
performance benefits of FP8 computation but requires memory for keeping the maximum
value history of tensors. To learn more about the delayed scaling strategy in
general, see the paper [_FP8 Formats for Deep Learning_](https://arxiv.org/pdf/2209.05433.pdf "https://arxiv.org/pdf/2209.05433.pdf").

In practice, using FP8 is helpful in all training scenarios on P5 instances. We
strongly recommend enabling FP8 whenever possible for enhancing training
performance.

SMP v2 supports Transformer Engine out of the box. Therefore, when running FP8
training with SMP v2 on P5 instances of SageMaker AI (`ml.p5.48xlarge`), the only
thing you need to do is to import `torch.sagemaker` in your training
script and keep using the native Transformer Engine Python package. To learn more
about using Transformer Engine for FP8 training in general, see [Using FP8 with Transformer Engine](https://docs.nvidia.com/deeplearning/transformer-engine/user-guide/examples/fp8_primer.html "https://docs.nvidia.com/deeplearning/transformer-engine/user-guide/examples/fp8_primer.html") in the _NVIDIA Transformer
Engine documentation_. The following code snippet shows how the code
lines for importing the SMP library and setting up FP8 in your training script
should look.

```
import torch.sagemaker as tsm
import transformer_engine.pytorch as te
from transformer_engine.common.recipe import DelayedScaling, Format

# Initialize the SMP torch.sagemaker API.
**tsm.init()**

# Define a transformer model and wrap it with the torch.sagemaker.transform API.
from transformers import AutoModelForCausalLM
model = AutoModelForCausalLM.from_config(`ModelConfig`)
**model = tsm.transform(model)**

# Enable E4M3 during forward pass, E5M2 during backward pass.
fp8_format = Format.HYBRID

# Create an FP8 recipe.
fp8_recipe = DelayedScaling(fp8_format=fp8_format, amax_history_len=32, amax_compute_algo="max")

# Enable FP8 autocasting.
with te.fp8_autocast(enabled=True, fp8_recipe=fp8_recipe, fp8_group=tsm.state.world_process_group):
    out = model(inp)

loss = out.sum()
loss.backward()
```

To find a practical example of FP8 training with SMP v2 on P5 instances, see the
example notebook at [Accelerate SageMaker PyTorch FSDP Training of Llama-v2 (or GPT-NeoX) with FP8 on P5
instances](https://github.com/aws/amazon-sagemaker-examples/blob/main/training/distributed_training/pytorch/model_parallel_v2/llama_v2/smp-train-llama-fsdp-tp-fp8.ipynb "https://github.com/aws/amazon-sagemaker-examples/blob/main/training/distributed_training/pytorch/model_parallel_v2/llama_v2/smp-train-llama-fsdp-tp-fp8.ipynb").

## Mixed precision training with half-precision data types using PyTorch

FSDP

SMP v2 supports [PyTorch FSDP `MixedPrecision`](https://pytorch.org/docs/stable/fsdp.html#torch.distributed.fsdp.MixedPrecision "https://pytorch.org/docs/stable/fsdp.html#torch.distributed.fsdp.MixedPrecision") for training jobs on P4 and P5
instances. PyTorch FSDP provides various configurations for mixed precision for both
performance improvement and memory reduction.

###### Note

This mixed precision training with the PyTorch FSDP feature is available in
the following combination of libraries of SageMaker and the PyTorch library.

- SMP v2.0.0 and later
- the SageMaker Python SDK v2.200.0 and later
- PyTorch v2.0.1 and later

The standard way to configure a model for mixed precision is to create the model
in `float32`, and then allow FSDP to cast the parameters to
`float16` or `bfloat16` on the fly by passing a
`MixedPrecision` policy, as shown in the following code snippet. For
more information about options to change the `dtype` for parameters,
reduction, or buffers for mixed precision in PyTorch, see [PyTorch FSDP `MixedPrecision` API](https://pytorch.org/docs/stable/fsdp.html#torch.distributed.fsdp.MixedPrecision "https://pytorch.org/docs/stable/fsdp.html#torch.distributed.fsdp.MixedPrecision") in the _PyTorch
documentation_.

```
# Native PyTorch API
from torch.distributed.fsdp import MixedPrecision

dtype = torch.bfloat16
mixed_precision_policy = MixedPrecision(
    param_dtype=dtype, reduce_dtype=dtype, buffer_dtype=dtype
)

model = FSDP(
    model,
    ...,
    mixed_precision=mixed_precision_policy
)
```

Note that certain models (such as the Hugging Face Transformers Llama model)
expect buffers as `float32`. To use `float32`, replace
`torch.bfloat16` with `torch.float32` in the line defining
the `dtype` object.
