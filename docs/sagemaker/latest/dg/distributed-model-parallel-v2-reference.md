# The SageMaker model parallel

library v2 reference

The following are references for the SageMaker model parallel library v2 (SMP v2).

###### Topics

- [SMP v2 core
  feature configuration parameters](#distributed-model-parallel-v2-reference-init-config "#distributed-model-parallel-v2-reference-init-config")
- [Reference for the SMP v2
  torch.sagemaker package](#model-parallel-v2-torch-sagemaker-reference "#model-parallel-v2-torch-sagemaker-reference")
- [Upgrade from SMP v1 to SMP v2](#model-parallel-v2-upgrade-from-v1 "#model-parallel-v2-upgrade-from-v1")

## SMP v2 core

feature configuration parameters

The following is a complete list of parameters to activate and configure the [Core features of the SageMaker model
parallelism library v2](model-parallel-core-features-v2.md "model-parallel-core-features-v2.md"). These must be written in JSON format
and passed to the PyTorch estimator in the SageMaker Python SDK or saved as a JSON file for
SageMaker HyperPod.

```
{
    "hybrid_shard_degree": `Integer`,
    "sm_activation_offloading": `Boolean`,
    "activation_loading_horizon": `Integer`,
    "fsdp_cache_flush_warnings": `Boolean`,
    "allow_empty_shards": `Boolean`,
    "tensor_parallel_degree": `Integer`,
    "context_parallel_degree": `Integer`,
    "expert_parallel_degree": `Integer`,
    "random_seed": `Integer`
}
```

- `hybrid_shard_degree` (Integer) – Specifies a sharded
  parallelism degree. The value must be an integer between `0` and
  `world_size`. The default value is `0`.
  - If set to `0`, it falls back to the native PyTorch
    implementation and API in the script when
    `tensor_parallel_degree` is 1. Otherwise, it computes the
    largest possible `hybrid_shard_degree` based on
    `tensor_parallel_degree` and `world_size`.
    When falling back to the native PyTorch FSDP use cases, if
    `FULL_SHARD` is the strategy you use, it shards across
    the whole cluster of GPUs. If `HYBRID_SHARD` or
    `_HYBRID_SHARD_ZERO2` was the strategy, it is equivalent
    to `hybrid_shard_degree` of 8. When tensor parallelism is
    enabled, it shards based on the revised
    `hybrid_shard_degree`.
  - If set to `1`, it falls back to the native PyTorch
    implementation and API for `NO_SHARD` in the script when
    `tensor_parallel_degree` is 1. Otherwise, it's equivalent
    to `NO_SHARD` within any given tensor parallel groups.
  - If set to an integer between 2 and `world_size`, sharding
    happens across the specified number of GPUs. If you don't set up
    `sharding_strategy` in the FSDP script, it gets
    overridden to `HYBRID_SHARD`. If you set
    `_HYBRID_SHARD_ZERO2`, the `sharding_strategy`
    you specify is used.

- `sm_activation_offloading` (Boolean) – Specifies whether to enable
  the SMP activation offloading implementation. If `False`, offloading
  uses the native PyTorch implementation. If `True`, it uses the SMP
  activation offloading implementation. You also need to use the PyTorch activation
  offload wrapper
  (`torch.distributed.algorithms._checkpoint.checkpoint_wrapper.offload_wrapper`)
  in your script. To learn more, see [Activation
  offloading](model-parallel-core-features-v2-pytorch-activation-offloading.md "model-parallel-core-features-v2-pytorch-activation-offloading.md").
  The default value is `True`.
- `activation_loading_horizon` (Integer) – An integer specifying the
  activation offloading horizon type for FSDP. This is the maximum number of
  checkpointed or offloaded layers whose inputs can be in the GPU memory
  simultaneously. To learn more, see [Activation
  offloading](model-parallel-core-features-v2-pytorch-activation-offloading.md "model-parallel-core-features-v2-pytorch-activation-offloading.md").
  The input value must be a positive integer. The default value is
  `2`.
- `fsdp_cache_flush_warnings` (Boolean) – Detects and warns if cache
  flushes happen in the PyTorch memory manager, because they can degrade
  computational performance. The default value is `True`.
- `allow_empty_shards` (Boolean) – Whether to allow empty shards when sharding
  tensors if tensor is not divisible. This is an experimental fix for crash during
  checkpointing in certain scenarios. Disabling this falls back to the original
  PyTorch behavior. The default value is `False`.
- `tensor_parallel_degree` (Integer) – Specifies a tensor
  parallelism degree. The value must be between `1` and
  `world_size`. The default value is `1`. Note that
  passing a value greater than 1 does not enable context parallelism
  automatically; you also need to use the [torch.sagemaker.transform](#model-parallel-v2-torch-sagemaker-reference-transform "#model-parallel-v2-torch-sagemaker-reference-transform") API to
  wrap the model in your training script. To learn more, see [Tensor
  parallelism](model-parallel-core-features-v2-tensor-parallelism.md "model-parallel-core-features-v2-tensor-parallelism.md").
- `context_parallel_degree` (Integer) – Specifies the context
  parallelism degree. The value must be between `1` and
  `world_size` , and must be `<=
hybrid_shard_degree`. The default value is `1`. Note that
  passing a value greater than 1 does not enable context parallelism
  automatically; you also need to use the [torch.sagemaker.transform](#model-parallel-v2-torch-sagemaker-reference-transform "#model-parallel-v2-torch-sagemaker-reference-transform") API to
  wrap the model in your training script. To learn more, see [Context parallelism](model-parallel-core-features-v2-context-parallelism.md "model-parallel-core-features-v2-context-parallelism.md").
- `expert_parallel_degree` (Integer) – Specifies a expert
  parallelism degree. The value must be between 1 and `world_size`. The
  default value is `1`. Note that passing a value greater than 1 does
  not enable context parallelism automatically; you also need to use the [torch.sagemaker.transform](#model-parallel-v2-torch-sagemaker-reference-transform "#model-parallel-v2-torch-sagemaker-reference-transform") API to
  wrap the model in your training script. To learn more, see [Expert
  parallelism](model-parallel-core-features-v2-expert-parallelism.md "model-parallel-core-features-v2-expert-parallelism.md").
- `random_seed` (Integer) – A seed number for the random
  operations in distributed modules by SMP tensor parallelism or expert
  parallelism. This seed is added to tensor-parallel or expert-parallel ranks to
  set the actual seed for each rank. It is unique for each tensor-parallel and
  expert-parallel rank. SMP v2 makes sure that the random number generated across
  tensor-parallel and expert-parallel ranks matches the non-tensor-parallelism and
  non-expert-parallelism cases respectively.

## Reference for the SMP v2

`torch.sagemaker` package

This section is a reference for the `torch.sagemaker` package provided by
SMP v2.

###### Topics

- [torch.sagemaker.delayed_param.DelayedParamIniter](#model-parallel-v2-torch-sagemaker-reference-delayed-param-init "#model-parallel-v2-torch-sagemaker-reference-delayed-param-init")
- [torch.sagemaker.distributed.checkpoint.state_dict_saver.async_save](#model-parallel-v2-torch-sagemaker-reference-checkpoint-async-save "#model-parallel-v2-torch-sagemaker-reference-checkpoint-async-save")
- [torch.sagemaker.distributed.checkpoint.state_dict_saver.maybe_finalize_async_calls](#model-parallel-v2-torch-sagemaker-reference-checkpoint-state-dict-saver "#model-parallel-v2-torch-sagemaker-reference-checkpoint-state-dict-saver")
- [torch.sagemaker.distributed.checkpoint.state_dict_saver.save](#model-parallel-v2-torch-sagemaker-reference-checkpoint-save "#model-parallel-v2-torch-sagemaker-reference-checkpoint-save")
- [torch.sagemaker.distributed.checkpoint.state_dict_loader.load](#model-parallel-v2-torch-sagemaker-reference-checkpoint-load "#model-parallel-v2-torch-sagemaker-reference-checkpoint-load")
- [torch.sagemaker.moe.moe_config.MoEConfig](#model-parallel-v2-torch-sagemaker-reference-moe "#model-parallel-v2-torch-sagemaker-reference-moe")
- [torch.sagemaker.nn.attn.FlashSelfAttention](#model-parallel-v2-torch-sagemaker-reference-flashselfattention "#model-parallel-v2-torch-sagemaker-reference-flashselfattention")
- [torch.sagemaker.nn.attn.FlashGroupedQueryAttention](#model-parallel-v2-torch-sagemaker-reference-flashGroupedQueryAttn "#model-parallel-v2-torch-sagemaker-reference-flashGroupedQueryAttn")
- [torch.sagemaker.nn.huggingface.llama_flashattn.LlamaFlashAttention](#model-parallel-v2-torch-sagemaker-reference-llamaFlashAttn "#model-parallel-v2-torch-sagemaker-reference-llamaFlashAttn")
- [torch.sagemaker.transform](#model-parallel-v2-torch-sagemaker-reference-transform "#model-parallel-v2-torch-sagemaker-reference-transform")
- [torch.sagemaker util functions and properties](#model-parallel-v2-torch-sagemaker-reference-utils "#model-parallel-v2-torch-sagemaker-reference-utils")

### `torch.sagemaker.delayed_param.DelayedParamIniter`

An API for applying [Delayed parameter
initialization](model-parallel-core-features-v2-delayed-param-init.md "model-parallel-core-features-v2-delayed-param-init.md") to a PyTorch
model.

```
class torch.sagemaker.delayed_param.DelayedParamIniter(
    model: nn.Module,
    init_method_using_config : Callable = None,
    verbose: bool = False,
)
```

**Parameters**

- `model` (`nn.Module`) – A PyTorch model to wrap and
  apply the delayed parameter initialization functionality of SMP v2.
- `init_method_using_config` (Callable) – If you use the
  tensor parallel implementation of SMP v2 or supported [Hugging Face Transformer models compatible with the SMP tensor
  parallelism](model-parallel-core-features-v2-tensor-parallelism.md#model-parallel-core-features-v2-tensor-parallelism-supported-models "model-parallel-core-features-v2-tensor-parallelism.md#model-parallel-core-features-v2-tensor-parallelism-supported-models"), keep this parameter at the default value, which is `None`. By
  default, the `DelayedParamIniter` API finds out how to initialize
  the given model correctly. For any other models, you need to create a custom
  parameter initialization function and add it to your script. The following
  code snippet is the default `init_method_using_config` function
  that SMP v2 implemented for the [Hugging Face Transformer models compatible with the SMP tensor
  parallelism](model-parallel-core-features-v2-tensor-parallelism.md#model-parallel-core-features-v2-tensor-parallelism-supported-models "model-parallel-core-features-v2-tensor-parallelism.md#model-parallel-core-features-v2-tensor-parallelism-supported-models"). Use the following code snippet as a reference for creating your own
  initialization configuration function, adding it to your script, and passing
  it to the `init_method_using_config` parameter of the SMP
  `DelayedParamIniter` API.

```
from torch.sagemaker.utils.module_utils import empty_module_params, move_buffers_to_device

# Define a custom init config function.
def `custom_init_method_using_config`(module):
    d = torch.cuda.current_device()
    empty_module_params(module, device=d)
    if isinstance(module, (nn.Linear, Conv1D)):
        module.weight.data.normal_(mean=0.0, std=config.initializer_range)
        if module.bias is not None:
            module.bias.data.zero_()
    elif isinstance(module, nn.Embedding):
        module.weight.data.normal_(mean=0.0, std=config.initializer_range)
        if module.padding_idx is not None:
            module.weight.data[module.padding_idx].zero_()
    elif isinstance(module, nn.LayerNorm):
        module.weight.data.fill_(1.0)
        module.bias.data.zero_()
    elif isinstance(module, LlamaRMSNorm):
        module.weight.data.fill_(1.0)
    move_buffers_to_device(module, device=d)

delayed_initer = DelayedParamIniter(model, init_method_using_config=`custom_init_method_using_config`)
```

For more information about the `torch.sagemaker.module_util`
functions in the preceding code snippet, see [torch.sagemaker util functions and properties](#model-parallel-v2-torch-sagemaker-reference-utils "#model-parallel-v2-torch-sagemaker-reference-utils").

- `verbose` (Boolean) – Whether to enable more detailed logging
  during initialization and validation. The default value is
  `False`.

**Methods**

- `get_param_init_fn()` – Returns the parameter initialization
  function that you can pass to the `param_init_fn` argument of the
  PyTorch FSDP wrapper class.
- `get_post_param_init_fn()` – Returns the parameter
  initialization function that you can pass to the
  `post_param_init_fn` argument of the PyTorch FSDP wrapper
  class. This is needed when you have tied weights in the model. The model
  must implement the method `tie_weights`. For more information,
  see the **Notes on tied weight** in [Delayed parameter
  initialization](model-parallel-core-features-v2-delayed-param-init.md "model-parallel-core-features-v2-delayed-param-init.md").
- `count_num_params` (`module: nn.Module, *args:
Tuple[nn.Parameter]`) – Tracks how many parameters are being
  initialized by the parameter initialization function. This helps implement
  the following `validate_params_and_buffers_inited` method. You
  usually don’t need to call this function explicitly, because the
  `validate_params_and_buffers_inited` method implicitly calls
  this method in the backend.
- `validate_params_and_buffers_inited` (`enabled:
bool=True`) – This is a context manager that helps validate that
  the number of parameters initialized matches the total number of parameters
  in the model. It also validates that all parameters and buffers are now on
  GPU devices instead of meta devices. It raises `AssertionErrors`
  if these conditions are not met. This context manager is only optional and
  you're not required to use this context manager to initialize
  parameters.

### `torch.sagemaker.distributed.checkpoint.state_dict_saver.async_save`

Entry API for asynchronous save. Use this method to save a `state_dict`
asynchronously to a specified `checkpoint_id`.

```
def async_save(
    state_dict: STATE_DICT_TYPE,
    *,
    checkpoint_id: Union[str, os.PathLike, None] = None,
    storage_writer: Optional[StorageWriter] = None,
    planner: Optional[SavePlanner] = None,
    process_group: Optional[dist.ProcessGroup] = None,
    coordinator_rank: int = 0,
    queue : AsyncCallsQueue = None,
    sharded_strategy: Union[SaveShardedStrategy, Tuple[str, int], None] = None,
    wait_error_handling: bool = True,
    force_check_all_plans: bool = True,
    s3_region: Optional[str] = None,
    s3client_config: Optional[S3ClientConfig] = None
) -> None:
```

**Parameters**

- `state_dict` (dict) - Required. The state dict to save.
- `checkpoint_id` (str) - Required. The storage path to save
  checkpoints to.
- `storage_writer` (StorageWriter) - Optional. An instance of
  [`StorageWriter`](https://pytorch.org/docs/stable/distributed.checkpoint.html#torch.distributed.checkpoint.StorageWriter "https://pytorch.org/docs/stable/distributed.checkpoint.html#torch.distributed.checkpoint.StorageWriter") in PyTorch to perform write
  operations. If this is not specificed, the default configuration of [`StorageWriter`](https://pytorch.org/docs/stable/distributed.checkpoint.html#torch.distributed.checkpoint.StorageWriter "https://pytorch.org/docs/stable/distributed.checkpoint.html#torch.distributed.checkpoint.StorageWriter") is used.
- `planner` (SavePlanner) - Optional. An instance of [`SavePlanner`](https://pytorch.org/docs/stable/distributed.checkpoint.html#torch.distributed.checkpoint.SavePlanner "https://pytorch.org/docs/stable/distributed.checkpoint.html#torch.distributed.checkpoint.SavePlanner") in PyTorch. If this is not
  specificed, the default configuration of [`SavePlanner`](https://pytorch.org/docs/stable/distributed.checkpoint.html#torch.distributed.checkpoint.SavePlanner "https://pytorch.org/docs/stable/distributed.checkpoint.html#torch.distributed.checkpoint.SavePlanner") is used.
- `process_group` (ProcessGroup) - Optional. The process group to
  work on. If `None`, the default (global) process group is
  used.
- `coordinator_rank` (int) - Optional. The rank of the
  coordinator when performing collective communication operators such as
  `AllReduce`.
- `queue` (AsyncRequestQueue) - Optional. The async scheduler to
  use. By default, it takes the global parameter
  `DEFAULT_ASYNC_REQUEST_QUEUE`.
- `sharded_strategy` (PyTorchDistSaveShardedStrategy) - Optional.
  The sharded strategy to use for saving checkpoints. If this is is not
  specified,
  `torch.sagemaker.distributed.checkpoint.state_dict_saver.PyTorchDistSaveShardedStrategy`
  is used by default.
- `wait_error_handling` (bool) - Optional. A flag specifying
  whether to wait for all ranks to finish error handling. The default value is
  `True`.
- `force_check_all_plans` (bool) - Optional. A flag that
  determines whether to forcibly synchronize plans across ranks, even in the
  case of a cache hit. The default value is `True`.
- `s3_region` (str) - Optional. The region where the S3 bucket is
  located. If not specified, the region is inferred from the
  `checkpoint_id`.
- `s3client_config` (S3ClientConfig) - Optional. The dataclass
  exposing configurable parameters for the S3 client. If not provided, the
  default configuration of [S3ClientConfig](https://github.com/awslabs/s3-connector-for-pytorch/blob/main/s3torchconnector/src/s3torchconnector/_s3client/s3client_config.py#L7 "https://github.com/awslabs/s3-connector-for-pytorch/blob/main/s3torchconnector/src/s3torchconnector/_s3client/s3client_config.py#L7") is used. The `part_size` parameter is
  set to 64MB by default.

### `torch.sagemaker.distributed.checkpoint.state_dict_saver.maybe_finalize_async_calls`

This function allows a training process to monitor multiple asynchronous requests
to be done.

```
def maybe_finalize_async_calls(
    blocking=True,
    process_group=None
) -> List[int]:
```

**Parameters**

- `blocking` (bool) - Optional. If `True`, it will
  wait until all active requests are completed. Otherwise, it finalizes only
  the asynchronous requests that have already finished. The default value is
  `True`.
- `process_group` (ProcessGroup) - Optional. The process group to
  operate on. If set to `None`, the default (global) process group
  is utilized.

**Returns**

- A list containing the indices of asynchronous calls are successfully
  finalized.

### `torch.sagemaker.distributed.checkpoint.state_dict_saver.save`

Use this method to save a `state_dict` synchronously to a specified
`checkpoint_id`.

```
def save(
    state_dict: STATE_DICT_TYPE,
    *,
    checkpoint_id: Union[str, os.PathLike, None] = None,
    storage_writer: Optional[StorageWriter] = None,
    planner: Optional[SavePlanner] = None,
    process_group: Optional[dist.ProcessGroup] = None,
    coordinator_rank: int = 0,
    wait_error_handling: bool = True,
    force_check_all_plans: bool = True,
    s3_region: Optional[str] = None,
    s3client_config: Optional[S3ClientConfig] = None
) -> None:
```

**Parameters**

- `state_dict` (dict) - Required. The state dict to save.
- `checkpoint_id` (str) - Required. The storage path to save
  checkpoints to.
- `storage_writer` (StorageWriter) - Optional. An instance of
  [`StorageWriter`](https://pytorch.org/docs/stable/distributed.checkpoint.html#torch.distributed.checkpoint.StorageWriter "https://pytorch.org/docs/stable/distributed.checkpoint.html#torch.distributed.checkpoint.StorageWriter") in PyTorch to perform write
  operations. If this is not specificed, the default configuration of [`StorageWriter`](https://pytorch.org/docs/stable/distributed.checkpoint.html#torch.distributed.checkpoint.StorageWriter "https://pytorch.org/docs/stable/distributed.checkpoint.html#torch.distributed.checkpoint.StorageWriter") is used.
- `planner` (SavePlanner) - Optional. An instance of [`SavePlanner`](https://pytorch.org/docs/stable/distributed.checkpoint.html#torch.distributed.checkpoint.SavePlanner "https://pytorch.org/docs/stable/distributed.checkpoint.html#torch.distributed.checkpoint.SavePlanner") in PyTorch. If this is not
  specificed, the default configuration of [`SavePlanner`](https://pytorch.org/docs/stable/distributed.checkpoint.html#torch.distributed.checkpoint.SavePlanner "https://pytorch.org/docs/stable/distributed.checkpoint.html#torch.distributed.checkpoint.SavePlanner") is used.
- `process_group` (ProcessGroup) - Optional. The process group to
  work on. If `None`, the default (global) process group is
  used.
- `coordinator_rank` (int) - Optional. The rank of the
  coordinator when performing collective communication operators such as
  `AllReduce`.
- `wait_error_handling` (bool) - Optional. A flag specifying
  whether to wait for all ranks to finish error handling. The default value is
  `True`.
- `force_check_all_plans` (bool) - Optional. A flag that
  determines whether to forcibly synchronize plans across ranks, even in the
  case of a cache hit. The default value is `True`.
- `s3_region` (str) - Optional. The region where the S3 bucket is
  located. If not specified, the region is inferred from the
  `checkpoint_id`.
- `s3client_config` (S3ClientConfig) - Optional. The dataclass
  exposing configurable parameters for the S3 client. If not provided, the
  default configuration of [S3ClientConfig](https://github.com/awslabs/s3-connector-for-pytorch/blob/main/s3torchconnector/src/s3torchconnector/_s3client/s3client_config.py#L7 "https://github.com/awslabs/s3-connector-for-pytorch/blob/main/s3torchconnector/src/s3torchconnector/_s3client/s3client_config.py#L7") is used. The `part_size` parameter is
  set to 64MB by default.

### `torch.sagemaker.distributed.checkpoint.state_dict_loader.load`

Load the state dictionary of a distributed model (`state_dict`).

```
def load(
    state_dict: Dict[str, Any],
    *,
    checkpoint_id: Union[str, os.PathLike, None] = None,
    storage_reader: Optional[StorageReader] = None,
    planner: Optional[LoadPlanner] = None,
    process_group: Optional[dist.ProcessGroup] = None,
    check_keys_matched: bool = True,
    coordinator_rank: int = 0,
    s3_region: Optional[str] = None,
    s3client_config: Optional[S3ClientConfig] = None
) -> None:
```

**Parameters**

- `state_dict` (dict) - Required. The `state_dict` to
  load.
- `checkpoint_id` (str) - Required. The ID of a checkpoint. The
  meaning of the `checkpoint_id` depends on the storage. It can be
  a path to a folder or to a file. It can also be a key if the storage is a
  key-value store.
- `storage_reader` (StorageReader) - Optional. An instance of
  [`StorageReader`](https://pytorch.org/docs/stable/distributed.checkpoint.html#torch.distributed.checkpoint.StorageReader "https://pytorch.org/docs/stable/distributed.checkpoint.html#torch.distributed.checkpoint.StorageReader") in PyTorch to perform read
  operations. If not specified, distributed checkpointing will automatically
  infer the reader based on the `checkpoint_id`. If
  `checkpoint_id` is also `None`, an exception error
  is raised.
- `planner` (StorageReader) - Optional. An instance of [`LoadPlanner`](https://pytorch.org/docs/stable/distributed.checkpoint.html#torch.distributed.checkpoint.LoadPlanner "https://pytorch.org/docs/stable/distributed.checkpoint.html#torch.distributed.checkpoint.LoadPlanner") in PyTorch. If not specificed, the
  default configuration of [`LoadPlanner`](https://pytorch.org/docs/stable/distributed.checkpoint.html#torch.distributed.checkpoint.LoadPlanner "https://pytorch.org/docs/stable/distributed.checkpoint.html#torch.distributed.checkpoint.LoadPlanner") is used.
- `check_keys_matched` (bool) - Optional. If enabled, checks
  whether the `state_dict` keys of all ranks are matched using
  `AllGather`.
- `s3_region` (str) - Optional. The region where the S3 bucket is
  located. If not specified, the region is inferred from the
  `checkpoint_id`.
- `s3client_config` (S3ClientConfig) - Optional. The dataclass
  exposing configurable parameters for the S3 client. If not provided, the
  default configuration of [S3ClientConfig](https://github.com/awslabs/s3-connector-for-pytorch/blob/main/s3torchconnector/src/s3torchconnector/_s3client/s3client_config.py#L7 "https://github.com/awslabs/s3-connector-for-pytorch/blob/main/s3torchconnector/src/s3torchconnector/_s3client/s3client_config.py#L7") is used. The `part_size` parameter is
  set to 64MB by default.

### `torch.sagemaker.moe.moe_config.MoEConfig`

A configuration class for setting up the SMP-implementation of Mixture-of-Experts
(MoE). You can specify MoE configuration values through this class and pass it to
the [`torch.sagemaker.transform`](distributed-model-parallel-v2-reference.md#model-parallel-v2-torch-sagemaker-reference-transform "distributed-model-parallel-v2-reference.md#model-parallel-v2-torch-sagemaker-reference-transform") API call. To learn more
about the usage of this class for training MoE models, see [Expert
parallelism](model-parallel-core-features-v2-expert-parallelism.md "model-parallel-core-features-v2-expert-parallelism.md").

```
class torch.sagemaker.moe.moe_config.MoEConfig(
    smp_moe=True,
    random_seed=12345,
    moe_load_balancing="sinkhorn",
    global_token_shuffle=False,
    moe_all_to_all_dispatcher=True,
    moe_aux_loss_coeff=0.001,
    moe_z_loss_coeff=0.001
)
```

**Parameters**

- `smp_moe` (Boolean) - Whether to use the SMP-implementation of
  MoE. The default value is `True`.
- `random_seed` (Integer) - A seed number for the random
  operations in expert-parallel distributed modules. This seed is added to the
  expert parallel rank to set the actual seed for each rank. It is unique for
  each expert parallel rank. The default value is `12345`.
- `moe_load_balancing` (String) - Specify the load balancing type
  of the MoE router. Valid options are `aux_loss`,
  `sinkhorn`, `balanced`, and `none`. The
  default value is `sinkhorn`.
- `global_token_shuffle` (Boolean) - Whether to shuffle tokens
  across EP ranks within the same EP group. The default value is
  `False`.
- `moe_all_to_all_dispatcher` (Boolean) - Whether to use
  all-to-all dispatcher for the communications in MoE. The default value is
  `True`.
- `moe_aux_loss_coeff` (Float) - A coefficient for auxiliary load
  balancing loss. The default value is `0.001`.
- `moe_z_loss_coeff` (Float) - Coefficient for z-loss. The
  default value is `0.001`.

### `torch.sagemaker.nn.attn.FlashSelfAttention`

An API for using [FlashAttention](model-parallel-core-features-v2-flashattention.md "model-parallel-core-features-v2-flashattention.md")
with SMP v2.

```
class torch.sagemaker.nn.attn.FlashSelfAttention(
   attention_dropout_prob: float = 0.0,
   scale: Optional[float] = None,
   triton_flash_attention: bool = False,
   use_alibi: bool = False,
)
```

**Parameters**

- `attention_dropout_prob` (float) – The dropout probability to
  apply to attention. The default value is `0.0`.
- `scale` (float) – If passed, this scale factor is
  applied for softmax. If set to `None` (which is also the default
  value), the scale factor is `1 / sqrt(attention_head_size)`. The
  default value is `None`.
- `triton_flash_attention` (bool) – If passed, Triton
  implementation of flash attention is used. This is necessary to supports
  Attention with Linear Biases (ALiBi) (see the following
  `use_alibi` parameter). This version of the kernel doesn’t
  support dropout. The default value is `False`.
- `use_alibi` (bool) – If passed, it enables Attention with
  Linear Biases (ALiBi) using the mask provided. When using ALiBi, it needs an
  attention mask prepared as follows. The default value is
  `False`.

```
def generate_alibi_attn_mask(attention_mask, batch_size, seq_length,
    num_attention_heads, alibi_bias_max=8):
    device, dtype = attention_mask.device, attention_mask.dtype
    alibi_attention_mask = torch.zeros(
        1, num_attention_heads, 1, seq_length, dtype=dtype, device=device
    )

    alibi_bias = torch.arange(1 - seq_length, 1, dtype=dtype, device=device).view(
        1, 1, 1, seq_length
    )
    m = torch.arange(1, num_attention_heads + 1, dtype=dtype, device=device)
    m.mul_(alibi_bias_max / num_attention_heads)
    alibi_bias = alibi_bias * (1.0 / (2 ** m.view(1, num_attention_heads, 1, 1)))

    alibi_attention_mask.add_(alibi_bias)
    alibi_attention_mask = alibi_attention_mask[..., :seq_length, :seq_length]
    if attention_mask is not None and attention_mask.bool().any():
        alibi_attention_mask.masked_fill(
            attention_mask.bool().view(batch_size, 1, 1, seq_length), float("-inf")
        )

    return alibi_attention_mask
```

**Methods**

- `forward(self, qkv, attn_mask=None, causal=False, cast_dtype=None,
layout="b h s d")` – A regular PyTorch module function. When a
  `module(x)` is called, SMP runs this function
  automatically.
  - `qkv` – `torch.Tensor` of the following
    form: `(batch_size x seqlen x (3 x num_heads) x
head_size)` or `(batch_size, (3 x num_heads) x seqlen
x head_size)`, a tuple of `torch.Tensors` each
    of which might be of shape `(batch_size x seqlen x num_heads x
head_size)`, or `(batch_size x num_heads x seqlen x
head_size)`. An appropriate layout arg must be passed
    based on the shape.
  - `attn_mask` – `torch.Tensor` of the
    following form `(batch_size x 1 x 1 x seqlen)`. To enable
    this attention mask parameter, it requires
    `triton_flash_attention=True` and `use_alibi=True`.
    To learn how to generate an attention mask using this method, see
    the code examples at [FlashAttention](model-parallel-core-features-v2-flashattention.md "model-parallel-core-features-v2-flashattention.md"). The
    default value is `None`.
  - `causal` – When set to `False`, which
    is the default value of the argument, no mask is applied. When set
    to `True`, the `forward` method uses the
    standard lower triangular mask. The default value is
    `False`.
  - `cast_dtype` – When set to a particular
    `dtype`, it casts the `qkv` tensors to
    that `dtype` before `attn`. This is useful for
    implementations such as the Hugging Face Transformer GPT-NeoX model,
    which has `q` and `k` with `fp32`
    after rotary embeddings. If set to `None`, no cast is
    applied. The default value is `None`.
  - `layout` (string) – Available values are `b h s
d` or `b s h d`. This should be set to the
    layout of `qkv` tensors passed, so appropriate
    transformations can be applied for `attn`. The default
    value is `b h s d`.

**Returns**

A single `torch.Tensor` with shape `(batch_size x num_heads x
 seq_len x head_size)`.

### `torch.sagemaker.nn.attn.FlashGroupedQueryAttention`

An API for using `FlashGroupedQueryAttention` with SMP v2. To learn
more about the usage of this API, see [Use
FlashAttention kernels for grouped-query attention](model-parallel-core-features-v2-flashattention.md#model-parallel-core-features-v2-flashattention-grouped-query "model-parallel-core-features-v2-flashattention.md#model-parallel-core-features-v2-flashattention-grouped-query").

```
class torch.sagemaker.nn.attn.FlashGroupedQueryAttention(
    attention_dropout_prob: float = 0.0,
    scale: Optional[float] = None,
)
```

**Parameters**

- `attention_dropout_prob` (float) – The dropout probability to
  apply to attention. The default value is `0.0`.
- `scale` (float) – If passed, this scale factor is
  applied for softmax. If set to `None`,
  `1 / sqrt(attention_head_size)` is used as the scale factor.
  The default value is `None`.

**Methods**

- `forward(self, q, kv, causal=False, cast_dtype=None, layout="b s h
d")` – A regular PyTorch module function. When a
  `module(x)` is called, SMP runs this function
  automatically.
  - `q` – `torch.Tensor` of the following form
    `(batch_size x seqlen x num_heads x head_size)` or
    `(batch_size x num_heads x seqlen x head_size)`.
    Appropriate layout arg must be passed based on the shape.
  - `kv` – `torch.Tensor` of the following form
    `(batch_size x seqlen x (2 x num_heads) x head_size)`
    or `(batch_size, (2 x num_heads) x seqlen x head_size)`,
    or a tuple of two `torch.Tensor`s, each of which might be
    of shape `(batch_size x seqlen x num_heads x head_size)`
    or `(batch_size x num_heads x seqlen x head_size)`.
    Appropriate `layout` argument must also be passed based
    on the shape.
  - `causal` – When set to `False`, which
    is the default value of the argument, no mask is applied. When set
    to `True`, the `forward` method uses the
    standard lower triangular mask. The default value is
    `False`.
  - `cast_dtype` – When set to a particular dtype, it casts
    the `qkv` tensors to that dtype before `attn`.
    This is useful for implementations such as Hugging Face Transformers
    GPT-NeoX, which has `q,k` with `fp32` after
    rotary embeddings. If set to `None`, no cast is applied.
    The default value is `None`.
  - layout (string) – Available values are `"b h s d"` or
    `"b s h d"`. This should be set to the layout of
    `qkv` tensors passed, so appropriate transformations
    can be applied for `attn`. The default value is `"b
h s d"`.

**Returns**

Returns a single `torch.Tensor (batch_size x num_heads x seq_len x
 head_size)` that represents the output of attention computation.

### `torch.sagemaker.nn.huggingface.llama_flashattn.LlamaFlashAttention`

An API that supports FlashAttention for the Llama model. This API uses the [torch.sagemaker.nn.attn.FlashGroupedQueryAttention](#model-parallel-v2-torch-sagemaker-reference-flashGroupedQueryAttn "#model-parallel-v2-torch-sagemaker-reference-flashGroupedQueryAttn")
API at low level. To learn how to use this, see [Use
FlashAttention kernels for grouped-query attention](model-parallel-core-features-v2-flashattention.md#model-parallel-core-features-v2-flashattention-grouped-query "model-parallel-core-features-v2-flashattention.md#model-parallel-core-features-v2-flashattention-grouped-query").

```
class torch.sagemaker.nn.huggingface.llama_flashattn.LlamaFlashAttention(
    config: LlamaConfig
)
```

**Parameters**

- `config` – A FlashAttention configuration for the Llama
  model.

**Methods**

- `forward(self, hidden_states, attention_mask, position_ids,
past_key_value, output_attentions, use_cache)`
  - `hidden_states` (`torch.Tensor`) –
    Hidden states of a tensor in form of `(batch_size x seq_len x
num_heads x head_size)`.
  - `attention_mask` (`torch.LongTensor`) – Mask
    to avoid performing attention on padding token indices in form of
    `(batch_size x seqlen)`. The default value is
    `None`.
  - `position_ids` (`torch.LongTensor`) –
    When not being `None`, it is in form of `(batch_size
x seqlen)`, indicating the indices of positions of each
    input sequence token in the position embeddings. The default value
    is `None`.
  - `past_key_value` (Cache) – Pre-computed hidden-states
    (key and values in the self-attention blocks and in the
    cross-attention blocks). The default value is `None`.
  - `output_attentions` (bool) – Indicates whether to
    return the attentions tensors of all attention layers. The default
    value is `False`.
  - `use_cache` (bool) – Indicates whether to return
    `past_key_values` key value states. The default value
    is `False`.

**Returns**

Returns a single `torch.Tensor (batch_size x num_heads x seq_len x
 head_size)` that represents the output of attention computation.

### `torch.sagemaker.transform`

SMP v2 provides this `torch.sagemaker.transform()` API for transforming
Hugging Face Transformer models to SMP model implementations and enabling the SMP
tensor parallelism.

```
torch.sagemaker.transform(
    model: nn.Module,
    device: Optional[torch.device] = None,
    dtype: Optional[torch.dtype] = None,
    config: Optional[Dict] = None,
    load_state_dict_from_rank0: bool = False,
    cp_comm_type: str = "p2p"
)
```

SMP v2 maintains transformation policies for the [Hugging Face Transformer models compatible with the SMP tensor
parallelism](model-parallel-core-features-v2-tensor-parallelism.md#model-parallel-core-features-v2-tensor-parallelism-supported-models "model-parallel-core-features-v2-tensor-parallelism.md#model-parallel-core-features-v2-tensor-parallelism-supported-models")
by converting the configuration of the Hugging Face Transformer models to the SMP
transformer configuration.

**Parameters**

- `model` (`torch.nn.Module`) – A model from
  [Hugging Face Transformer models compatible with the SMP tensor
  parallelism](model-parallel-core-features-v2-tensor-parallelism.md#model-parallel-core-features-v2-tensor-parallelism-supported-models "model-parallel-core-features-v2-tensor-parallelism.md#model-parallel-core-features-v2-tensor-parallelism-supported-models") to transform and apply the tensor parallelism feature of the SMP
  library.
- `device` (`torch.device`) – If passed, a new
  model is created on this device. If the original module has any parameter on
  meta device (see [Delayed parameter
  initialization](model-parallel-core-features-v2-delayed-param-init.md "model-parallel-core-features-v2-delayed-param-init.md")), then
  the transformed module will also be created on meta device, ignoring the
  argument passed here. The default value is `None`.
- `dtype` (`torch.dtype`) – If passed, sets
  this as the dtype context manager for the creation of the model and creates
  a model with this dtype. This is typically unnecessary, as we want to create
  the model with `fp32` when using `MixedPrecision`, and
  `fp32` is the default dtype in PyTorch. The default value is
  `None`.
- `config` (dict) – This is a dictionary for configuring
  the SMP transformer. The default value is `None`.
- `load_state_dict_from_rank0` (Boolean) – By default,
  this module creates a new instance of the model with new weights. When this
  argument is set to `True`, SMP tries to load the state dictionary
  of the original PyTorch model from the 0th rank into transformed model for
  the tensor parallel group that the 0th rank is part of. When this is set to
  `True`, rank 0 can’t have any parameters on meta device. Only
  the first tensor parallel group populates the weights from the 0th rank
  after this transform call. You need to set `sync_module_states`
  to `True` in the FSDP wrapper to get these weights from the first
  tensor parallel group to all other processes. With this activated, the SMP
  library loads the state dictionary from the original model. The SMP library
  takes the `state_dict` of the model before transform, converts it
  to match the structure of the transformed model, shards it for each tensor
  parallel rank, communicates this state from the 0th rank to other ranks in
  the tensor parallel group that the 0th rank is part of, and loads it. The
  default value is `False`.
- `cp_comm_type` (str) – Determines the context parallelism implementation and
  is only applicable when the `context_parallel_degree` is greater
  than 1. Available values for this parameter are `p2p` and
  `all_gather`. The `p2p` implementation utilizes
  peer-to-peer send-receive calls for key-and-value (KV) tensor accumulation
  during the attention computation, running asynchronously and allowing
  communication to overlap with computation. On the other hand, the
  `all_gather` implementation employs the
  `AllGather` communication collective operation for KV tensor
  accumulation. The default value is `"p2p"`.

**Returns**

Returns a transformed model that you can wrap with PyTorch FSDP. When
`load_state_dict_from_rank0` is set to `True`, the tensor
parallel group that involves rank 0 has weights loaded from the original state
dictionary on rank 0. When using [Delayed parameter
initialization](model-parallel-core-features-v2-delayed-param-init.md "model-parallel-core-features-v2-delayed-param-init.md") on the original
model, only these ranks have the actual tensors on CPUs for the parameters and
buffers of the transformed model. The rest of the ranks continue to have the
parameters and buffers on the meta device to save memory.

### `torch.sagemaker` util functions and properties

###### torch.sagemaker util functions

- `torch.sagemaker.init(config: Optional[Union[str, Dict[str, Any]]] =
None) -> None` – Initializes the PyTorch training job with
  SMP.
- `torch.sagemaker.is_initialized() -> bool` – Checks
  whether the training job is initialized with SMP. When falling back to the
  native PyTorch while the job is initialized with SMP,
  some of the properties are not relevant and become
  `None`, as indicated in the following **Properties** list.
- `torch.sagemaker.utils.module_utils.empty_module_params(module:
nn.Module, device: Optional[torch.device] = None, recurse: bool = False)
-> nn.Module` – Creates empty parameters on the given
  `device` if any, and it can be recursive for all nested
  modules if specified.
- `torch.sagemaker.utils.module_utils.move_buffers_to_device(module:
nn.Module, device: torch.device, recurse: bool = False) ->
nn.Module` – Moves module buffers to the given
  `device`, and it can be recursive for all nested modules if
  specified.

###### Properties

`torch.sagemaker.state` holds multiple useful properties after the
initialization of SMP with `torch.sagemaker.init`.

- `torch.sagemaker.state.hybrid_shard_degree` (int) – The sharded
  data parallelism degree, a copy from user input in the SMP configuration
  passed to `torch.sagemaker.init()`. To learn more, see [Use the SageMaker model parallelism
  library v2](model-parallel-use-api-v2.md "model-parallel-use-api-v2.md").
- `torch.sagemaker.state.rank` (int) – The global rank for the
  device, in the range of `[0, world_size)`.
- `torch.sagemaker.state.rep_rank_process_group`
  (`torch.distributed.ProcessGroup`) – The process group
  including all devices with the same replication rank. Note the subtle but
  fundamental difference with
  `torch.sagemaker.state.tp_process_group`. When falling back
  to native PyTorch, it returns `None`.
- `torch.sagemaker.state.tensor_parallel_degree` (int) – The
  tensor parallelism degree, a copy from user input in the SMP configuration
  passed to `torch.sagemaker.init()`. To learn more, see [Use the SageMaker model parallelism
  library v2](model-parallel-use-api-v2.md "model-parallel-use-api-v2.md").
- `torch.sagemaker.state.tp_size` (int) – An alias to
  `torch.sagemaker.state.tensor_parallel_degree`.
- `torch.sagemaker.state.tp_rank` (int) – The tensor parallelism
  rank for the device in the range of `[0, tp_size)`, determined by
  the tensor parallelism degree and the ranking mechanism.
- `torch.sagemaker.state.tp_process_group`
  (`torch.distributed.ProcessGroup`) – The tensor parallel
  process group including all devices with the same rank in other dimensions
  (for example, sharded data parallelism and replication) but unique tensor
  parallel ranks. When falling back to native PyTorch, it returns
  `None`.
- `torch.sagemaker.state.world_size` (int) – The total number of
  devices used in training.

## Upgrade from SMP v1 to SMP v2

To move from SMP v1 to SMP v2, you must make script changes to remove the SMP v1 APIs
and apply the SMP v2 APIs. Instead of starting from your SMP v1 script, we recommend you
start from a PyTorch FSDP script, and follow the instructions at [Use the SageMaker model parallelism
library v2](model-parallel-use-api-v2.md "model-parallel-use-api-v2.md").

To bring SMP v1 _models_ to SMP v2, in SMP v1 you
must collect the full model state dictionary and apply the translation functions on the
model state dictionary to convert it into the Hugging Face Transformers model checkpoint
format. Then in SMP v2, as discussed in [Checkpointing using
SMP](model-parallel-core-features-v2-checkpoints.md "model-parallel-core-features-v2-checkpoints.md"), you can load the Hugging
Face Transformers model checkpoints, and then continue with using the PyTorch checkpoint
APIs with SMP v2. To use SMP with your PyTorch FSDP model, make sure that you move to
SMP v2 and make changes to your training script to use PyTorch FSDP and other latest
features.

```
import smdistributed.modelparallel.torch as smp

# Create model
model = ...
model = smp.DistributedModel(model)

# Run training
...

# Save v1 full checkpoint
if smp.rdp_rank() == 0:
    model_dict = model.state_dict(gather_to_rank0=True) # save the full model
    # Get the corresponding translation function in smp v1 and translate
    if model_type == "gpt_neox":
        from smdistributed.modelparallel.torch.nn.huggingface.gptneox import translate_state_dict_to_hf_gptneox
        translated_state_dict = translate_state_dict_to_hf_gptneox(state_dict, max_seq_len=None)

    # Save the checkpoint
    checkpoint_path = "checkpoint.pt"
    if smp.rank() == 0:
        smp.save(
            {"model_state_dict": translated_state_dict},
            checkpoint_path,
            partial=False,
        )
```

To find available translation functions in SMP v1, see [Support for
Hugging Face Transformer Models](model-parallel-extended-features-pytorch-hugging-face.md "model-parallel-extended-features-pytorch-hugging-face.md").

For instruction on model checkpoints saving and loading in SMP v2, see [Checkpointing using
SMP](model-parallel-core-features-v2-checkpoints.md "model-parallel-core-features-v2-checkpoints.md").
