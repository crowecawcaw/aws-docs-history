# Checkpointing using

SMP

The SageMaker model parallelism (SMP) library supports PyTorch APIs for checkpoints,
and provides APIs that help checkpoint properly while using the SMP library.

PyTorch FSDP (Fully Sharded Data Parallelism) supports three types of checkpoints:
full, sharded, and local, each serving different purposes. Full checkpoints are used
when exporting the model after training is completed, as generating a full checkpoint is
a computationally expensive process. Sharded checkpoints help save and load the state of a model sharded for each individual rank.
With sharded checkpoints,
you can resume training with different hardware configurations, such as a different
number of GPUs. However, loading sharded checkpoints can be slow due to the
communication involved among multiple devices. The SMP library provides local
checkpointing functionalities, which allow faster retrieval of the model's state without
additional communication overhead. Note that checkpoints created by FSDP require writing
to a shared network file system such as Amazon FSx.

## Async local checkpoints

When training machine learning models, there is no need for subsequent iterations
to wait for the checkpoint files to be saved to disk. With the release of SMP v2.5,
the library supports saving checkpoint files asynchronously. This means that the
subsequent training iteration can run simultaneously with the input and output (I/O)
operations for creating checkpoints, without being slowed down or held back by those
I/O operations. Also, the process of retrieving sharded model and optimizer
paramemeters in PyTorch can be time-consuming due to the additional collective
communication required to exchange distributed tensor metadata across ranks. Even
when using `StateDictType.LOCAL_STATE_DICT` to save local checkpoints for
each rank, PyTorch still invokes hooks that perform collective communication. To
mitigate this issue and reduce the time required for checkpoint retrieval, SMP
introduces `SMStateDictType.SM_LOCAL_STATE_DICT`, which allows for faster
retrieval of model and optimizer checkpoints by bypassing the collective
communication overhead.

###### Note

Maintaining consistency in the FSDP `SHARD_DEGREE` is a requirement
for utilizing the `SMStateDictType.SM_LOCAL_STATE_DICT`. Ensure that
the `SHARD_DEGREE` remains unchanged. While the number of model
replications can vary, the model shard degree needs to be identical to the
previous training setup when resuming from a checkpoint.

```
import os
import torch.distributed as dist
import torch.sagemaker as tsm
from torch.sagemaker import state
from torch.distributed.fsdp import FullyShardedDataParallel as FSDP
from torch.sagemaker.distributed.checkpoint.state_dict_saver import (
    async_save,
    maybe_finalize_async_calls,
)
from torch.sagemaker.distributed.checkpoint.state_dict_utils import (
    sm_state_dict_type,
    SMStateDictType,
)

global_rank = dist.get_rank()
save_dir = "/opt/ml/checkpoints"
sub_dir = f"tp{state.tp_rank}_ep{state.ep_rank}_fsdp{model.rank}"

# 1. Get replication ranks and group
current_replication_group = None
current_replication_ranks = None
for replication_ranks in state.ranker.get_rep_groups():
    rep_group = dist.new_group(replication_ranks)
    if global_rank in replication_ranks:
        current_replication_group = rep_group
        current_replication_ranks = replication_ranks

coordinator_rank = min(current_replication_ranks)

# 2. Wait for the previous checkpointing done
maybe_finalize_async_calls(
    blocking=True, process_group=current_replication_group
)

# 3. Get model local checkpoint
with sm_state_dict_type(model, SMStateDictType.SM_LOCAL_STATE_DICT):
    state_dict = {
       "model": model.state_dict(),
       "optimizer": optimizer.state_dict(),
        # Potentially add more customized state dicts.
    }

# 4. Save a local checkpoint
async_save(
    state_dict,
    checkpoint_id=os.path.join(save_dir, sub_dir),
    process_group=current_replication_group,
    coordinator_rank=coordinator_rank,
)
```

The following code snippet demonstrates how to load a checkpoint utilizing
`SMStateDictType.SM_LOCAL_STATE_DICT`.

```
import os
import torch.sagemaker as tsm
from torch.sagemaker import state
from torch.sagemaker.distributed.checkpoint.state_dict_loader import load
from torch.sagemaker.distributed.checkpoint.state_dict_utils import (
    sm_state_dict_type,
    SMStateDictType,
    init_optim_state
)
from torch.sagemaker.distributed.checkpoint.filesystem import (
    DistributedFileSystemReader,
)

load_dir = "/opt/ml/checkpoints"
sub_dir = f"tp{state.tp_rank}_ep{state.ep_rank}_fsdp{model.rank}"
global_rank = dist.get_rank()
checkpoint_id = os.path.join(load_dir, sub_dir)
storage_reader = DistributedFileSystemReader(checkpoint_id)

# 1. Get replication ranks and group
current_replication_group = None
current_replication_ranks = None
for replication_ranks in state.ranker.get_rep_groups():
    rep_group = dist.new_group(replication_ranks)
    if global_rank in replication_ranks:
        current_replication_group = rep_group
        current_replication_ranks = replication_ranks

coordinator_rank = min(current_replication_ranks)

# 2. Create local state_dict
with sm_state_dict_type(model, SMStateDictType.SM_LOCAL_STATE_DICT):
    state_dict = {
        "model": model.state_dict(),
        # Potentially add more customized state dicts.
    }

    # Init optimizer state_dict states by setting zero grads and step.
    init_optim_state(optimizer, skip_empty_param=True)
    state_dict["optimizer"] = optimizer.state_dict()

# 3. Load a checkpoint
load(
    state_dict=state_dict,
    process_group=current_replication_group,
    coordinator_rank=coordinator_rank,
    storage_reader=storage_reader,
)
```

Storing checkpoints for large language models (LLMs) can be expensive as it often
requires creating a large filesystem volume. To reduce costs, you have the option to
save checkpoints directly to Amazon S3 without the need for additional filesystem
services such as Amazon FSx. You can leverage the previous example with the following
code snippet to save checkpoints to S3 by specifying an S3 URL as the destination.

```
key = os.path.join(checkpoint_dir, sub_dir)
checkpoint_id= f"`s3://{your_s3_bucket}/{key}`"
async_save(state_dict, checkpoint_id=checkpoint_id, **kw)
load(state_dict, checkpoint_id=checkpoint_id, **kw)
```

## Async sharded checkpoints

There may be situations where you need to continue training with different
hardware configurations, such as changing the number of GPUs. In these cases, your
training processes must load checkpoints while resharding, which means resuming
subsequent training with a different number of `SHARD_DEGREE`. In order
to address the scenario where you need to resume training with a different number of
`SHARD_DEGREE`, you must save your model checkpoints using the
sharded state dictionary type, which is represented by
`StateDictType.SHARDED_STATE_DICT`. Saving checkpoints in this format
allows you to properly handle the resharding process when continuing the training
with a modified hardware configuration. The provided code snippet illustrates how to
use the `tsm` API to asynchronously save sharded checkpoints, enabling a
more efficient and streamlined training process.

```
import os
import torch.sagemaker as tsm
from torch.sagemaker import state
from torch.distributed.fsdp import FullyShardedDataParallel as FSDP
from torch.distributed.fsdp import StateDictType
from torch.sagemaker.utils.process_group_utils import get_global_ranks
from torch.sagemaker.distributed.checkpoint.state_dict_saver import (
    async_save,
    maybe_finalize_async_calls,
)

save_dir = "/opt/ml/checkpoints"
sub_dir = f"tp{state.tp_rank}_ep{state.ep_rank}"
checkpoint_id = os.path.join(save_dir, sub_dir)

# To determine whether curreto take part in checkpointing.
global_rank = dist.get_rank()
action_rank = state.ranker.get_rep_rank(global_rank) == 0
process_group = model.process_group
coordinator_rank = min(get_global_ranks(process_group))

# 1. wait for the previous checkpointing done
maybe_finalize_async_calls(blocking=True, process_group=process_group)

# 2. retrieve model & optimizer sharded state_dict
with FSDP.state_dict_type(model, StateDictType.SHARDED_STATE_DICT):
    state_dict = {
        "model": model.state_dict(),
        "optimizer": FSDP.optim_state_dict(model, optimizer),
        # Potentially add more customized state dicts.
    }

# 3. save checkpoints asynchronously using async_save
if action_rank:
    async_save(
        state_dict,
        checkpoint_id=checkpoint_id,
        process_group=process_group,
        coordinator_rank=coordinator_rank,
    )
```

The process of loading shared checkpoints is similar to the previous section, but
it involves using the
`torch.sagemaker.distributed.checkpoint.filesystem.DistributedFileSystemReader`
and its `load` method. The `load` method of this class allows
you to load the shared checkpoint data, following a process analogous to the one
described earlier.

```
import os
from torch.distributed.fsdp import FullyShardedDataParallel as FSDP
from torch.distributed.fsdp import StateDictType
from torch.distributed.checkpoint.optimizer import load_sharded_optimizer_state_dict
from torch.sagemaker.distributed.checkpoint.state_dict_loader import load
from torch.sagemaker.utils.process_group_utils import get_global_ranks
from torch.sagemaker.distributed.checkpoint.filesystem import (
    DistributedFileSystemReader,
)

 load_dir = "/opt/ml/checkpoints"
sub_dir = f"tp{state.tp_rank}_ep{state.ep_rank}"
checkpoint_id = os.path.join(load_dir, sub_dir)
reader = DistributedFileSystemReader(checkpoint_id)

process_group = model.process_group
coordinator_rank = min(get_global_ranks(process_group))

with FSDP.state_dict_type(model, StateDictType.SHARDED_STATE_DICT):
   # 1. Load model and everything else except the optimizer.
   state_dict = {
        "model": model.state_dict()
        # Potentially more customized state dicts.
   }
   load(
        state_dict,
        storage_reader=reader,
        process_group=process_group,
        coordinator_rank=coordinator_rank,
   )
   model.load_state_dict(state_dict["model"])

   # 2. Load optimizer.
   optim_state = load_sharded_optimizer_state_dict(
        model_state_dict=state_dict["model"],
        optimizer_key="optimizer",
        storage_reader=reader,
        process_group=process_group,
    )
   flattened_optimizer_state = FSDP.optim_state_dict_to_load(
        optim_state["optimizer"], model, optimizer,
         group=model.process_group
   )
   optimizer.load_state_dict(flattened_optimizer_state)
```

## Full model

checkpoints

At the end of training, you can save a full checkpoint that combines all shards of
a model into a single model checkpoint file. The SMP library fully supports the
PyTorch full model checkpoints API, so you don't need to make any changes.

Note that if you use the SMP [Tensor
parallelism](model-parallel-core-features-v2-tensor-parallelism.md "model-parallel-core-features-v2-tensor-parallelism.md"), the SMP library
transforms the model. When checkpointing the full model in this case, the SMP
library translates the model back to the Hugging Face Transformers checkpoint format
by default.

In cases where you train with the SMP tensor parallelism and turn off the SMP
translation process, you can use the `translate_on_save` argument of the
PyTorch `FullStateDictConfig` API to switch the SMP auto-translation on
or off as needed. For example, if you are focusing on training a model, you don’t
need to add the translation process which adds overhead. In that case, we recommend
you to set `translate_on_save=False`. Also, if you plan to keep using the
SMP translation of the model for further training in future, you can switch it off
to save the SMP translation of the model for later use. Translating the model back
to the Hugging Face Transformers model checkpoint format is needed when you wrap up
the training of your model and use that for inference.

```
from torch.distributed.fsdp import FullyShardedDataParallel as FSDP
from torch.distributed.fsdp import FullStateDictConfig
**import torch.sagemaker as tsm**

# Save checkpoints.
with FSDP.state_dict_type(
    model,
    StateDictType.FULL_STATE_DICT,
    FullStateDictConfig(
        rank0_only=True, offload_to_cpu=True,
        **# Default value is to translate back to Hugging Face Transformers format,
 # when saving full checkpoints for models trained with SMP tensor parallelism.
 # translate\_on\_save=True**
    ),
):
    state_dict = model.state_dict()
    if dist.get_rank() == 0:
        logger.info("Processed state dict to save. Starting write to disk now.")
        os.makedirs(`save_dir`, exist_ok=True)
        # This name is needed for HF from_pretrained API to work.
        torch.save(state_dict, os.path.join(`save_dir`, "pytorch_model.bin"))
        hf_model_config.save_pretrained(`save_dir`)
    dist.barrier()
```

Note that the option `FullStateDictConfig(rank0_only=True,
 offload_to_cpu=True)` is to gather the model on the CPU of the 0th rank
device to save memory when training large models.

To load the model back for inference, you do so as shown in the following code
example. Note that the class `AutoModelForCausalLM` might change to other
factor builder classes in Hugging Face Transformers, such as
`AutoModelForSeq2SeqLM`, depending on your model. For more
information, see [Hugging Face Transformers documentation](https://huggingface.co/docs/transformers/v4.36.1/en/model_doc/auto#natural-language-processing "https://huggingface.co/docs/transformers/v4.36.1/en/model_doc/auto#natural-language-processing").

```
from transformers import AutoModelForCausalLM
model = AutoModelForCausalLM.from_pretrained(`save_dir`)
```
