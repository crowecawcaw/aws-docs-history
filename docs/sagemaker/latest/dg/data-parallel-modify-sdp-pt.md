# Use the SMDDP library in your PyTorch training

script

Starting from the SageMaker AI distributed data parallelism (SMDDP) library v1.4.0, you can use
the library as a backend option for the [PyTorch distributed
package](https://pytorch.org/tutorials/beginner/dist_overview.html "https://pytorch.org/tutorials/beginner/dist_overview.html"). To use the SMDDP `AllReduce` and `AllGather`
collective operations, you only need to import the SMDDP library at the beginning of your
training script and set SMDDP as the the backend of PyTorch distributed modules during
process group initialization. With the single line of backend specification, you can keep
all the native PyTorch distributed modules and the entire training script unchanged. The
following code snippets show how to use the SMDDP library as the backend of PyTorch-based
distributed training packages: [PyTorch distributed data parallel (DDP)](https://pytorch.org/docs/stable/notes/ddp.html "https://pytorch.org/docs/stable/notes/ddp.html"), [PyTorch fully sharded data parallelism
(FSDP)](https://pytorch.org/docs/stable/fsdp.html "https://pytorch.org/docs/stable/fsdp.html"), [DeepSpeed](https://github.com/microsoft/DeepSpeed "https://github.com/microsoft/DeepSpeed"), and
[Megatron-DeepSpeed](https://github.com/microsoft/Megatron-DeepSpeed "https://github.com/microsoft/Megatron-DeepSpeed").

## For PyTorch DDP or FSDP

Initialize the process group as follows.

```
import torch.distributed as dist
import smdistributed.dataparallel.torch.torch_smddp

dist.init_process_group(backend="smddp")
```

###### Note

(For PyTorch DDP jobs only) The `smddp` backend currently does not
support creating subprocess groups with the `torch.distributed.new_group()`
API. You also cannot use the `smddp` backend concurrently with other process
group backends such as `NCCL` and `Gloo`.

## For DeepSpeed or

Megatron-DeepSpeed

Initialize the process group as follows.

```
import deepspeed
import smdistributed.dataparallel.torch.torch_smddp

deepspeed.init_distributed(dist_backend="smddp")
```

###### Note

To use SMDDP `AllGather` with the `mpirun`-based launchers
(`smdistributed` and `pytorchddp`) in [Launching distributed training jobs with SMDDP using the
SageMaker Python SDK](data-parallel-use-api.md "data-parallel-use-api.md"), you also need to set the following environment
variable in your training script.

```
export SMDATAPARALLEL_OPTIMIZE_SDP=true
```

For general guidance on writing a PyTorch FSDP training script, see [Advanced
Model Training with Fully Sharded Data Parallel (FSDP)](https://pytorch.org/tutorials/intermediate/FSDP_adavnced_tutorial.html "https://pytorch.org/tutorials/intermediate/FSDP_adavnced_tutorial.html") in the PyTorch
documentation.

For general guidance on writing a PyTorch DDP training script, see [Getting started with
distributed data parallel](https://pytorch.org/tutorials/intermediate/ddp_tutorial.html "https://pytorch.org/tutorials/intermediate/ddp_tutorial.html") in the PyTorch documentation.

After you have completed adapting your training script, proceed to [Launching distributed training jobs with SMDDP using the
SageMaker Python SDK](data-parallel-use-api.md "data-parallel-use-api.md").
