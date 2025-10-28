# Hybrid

sharded data parallelism

_Sharded data parallelism_ is a memory-saving
distributed training technique that splits the state of a model (model parameters,
gradients, and optimizer states) across devices. This helps you fit a larger model or
increase the batch size using the freed-up GPU memory. The SMP library offers a
capability of running sharded data parallelism with PyTorch Fully Sharded Data Parallel
(FSDP). PyTorch FSDP by default shards across the whole set of GPUs being used. In SMP
v2, the library offers this sharded data parallelism on top of PyTorch FSDP by extending
PyTorch hybrid sharding (`HYBRID_SHARD`), which is one of the [sharding strategies provided by PyTorch FSDP](https://pytorch.org/docs/stable/fsdp.html#torch.distributed.fsdp.ShardingStrategy "https://pytorch.org/docs/stable/fsdp.html#torch.distributed.fsdp.ShardingStrategy"): `FULL_SHARD`,
`SHARD_GRAD_OP`, `HYBRID_SHARD`,
`_HYBRID_SHARD_ZERO2`. Extending hybrid sharding in this manner helps
implement scale-aware-sharding as described in the blog [Near-linear scaling of gigantic-model training on AWS](https://www.amazon.science/blog/near-linear-scaling-of-gigantic-model-training-on-aws "https://www.amazon.science/blog/near-linear-scaling-of-gigantic-model-training-on-aws") for PyTorch
FSDP.

The SMP library makes it easy to use `HYBRID_SHARD` and
`_HYBRID_SHARD_ZERO2` across any configurable number of GPUs, extending
the native PyTorch FSDP that supports sharding across a single node
(`HYBRID_SHARD`) or all GPUs (`FULL_SHARD`). PyTorch FSDP
calls can stay as is, and you only need to add the `hybrid_shard_degree`
argument to the SMP configuration, as shown in the following code example. You don't
need to change the value of the `sharding_strategy` argument in the PyTorch
FSDP wrapper around your PyTorch model. You can pass
`ShardingStrategy.HYBRID_SHARD` as the value. Alternatively, the SMP
library overrides the strategy in the script and sets it to
`ShardingStrategy.HYBRID_SHARD` if you specify a value equal to or
greater than 2 to the `hybrid_shard_degree` parameter.

The following code snippets show how to add the SMP initialization module
`torch.sagemaker.init()` to your training script and set up the SMP
configuration dictionary in JSON format for training job launcher while following the
two-step process introduced in [Use the SageMaker model parallelism
library v2](model-parallel-use-api-v2.md "model-parallel-use-api-v2.md"). You don’t
need to make any changes to your PyTorch model or [PyTorch FSDP](https://pytorch.org/docs/stable/fsdp.html#module-torch.distributed.fsdp "https://pytorch.org/docs/stable/fsdp.html#module-torch.distributed.fsdp") configuration. For more information about the
`hybrid_shard_degree` parameter, see [SMP v2 core
feature configuration parameters](distributed-model-parallel-v2-reference.md#distributed-model-parallel-v2-reference-init-config "distributed-model-parallel-v2-reference.md#distributed-model-parallel-v2-reference-init-config").

**SMP configuration dictionary**

```
{ "hybrid_shard_degree": 16 }
```

**In training script**

```
**import torch.sagemaker as tsm
tsm.init()**

# Set up a PyTorch model
model = ...

# Wrap the PyTorch model using the PyTorch FSDP module
model = FSDP(
    model,
    ...
)

# Optimizer needs to be created after FSDP wrapper
optimizer = ...
```
