# Use the SMDDP library in your

PyTorch Lightning training script

If you want to bring your [PyTorch
Lightning](https://pytorch-lightning.readthedocs.io/en/latest/starter/introduction.html "https://pytorch-lightning.readthedocs.io/en/latest/starter/introduction.html") training script and run a distributed data parallel training job in
SageMaker AI, you can run the training job with minimal changes in your training script. The
necessary changes include the following: import the `smdistributed.dataparallel`
library’s PyTorch modules, set up the environment variables for PyTorch Lightning to accept
the SageMaker AI environment variables that are preset by the SageMaker training toolkit, and activate
the SMDDP library by setting the process group backend to `"smddp"`. To learn
more, walk through the following instructions that break down the steps with code
examples.

###### Note

The PyTorch Lightning support is available in the SageMaker AI data parallel library
v1.5.0 and later.

1. Import the `pytorch_lightning` library and the
   `smdistributed.dataparallel.torch` modules.

```
import lightning as pl
import smdistributed.dataparallel.torch.torch_smddp
```

2. Instantiate the [LightningEnvironment](https://pytorch-lightning.readthedocs.io/en/stable/api/pytorch_lightning.plugins.environments.LightningEnvironment.html "https://pytorch-lightning.readthedocs.io/en/stable/api/pytorch_lightning.plugins.environments.LightningEnvironment.html").

```
from lightning.fabric.plugins.environments.lightning import LightningEnvironment

env = LightningEnvironment()
env.world_size = lambda: int(os.environ["WORLD_SIZE"])
env.global_rank = lambda: int(os.environ["RANK"])
```

3. **For PyTorch DDP** – Create an object of
   the [DDPStrategy](https://lightning.ai/docs/pytorch/stable/api/lightning.pytorch.strategies.DDPStrategy.html "https://lightning.ai/docs/pytorch/stable/api/lightning.pytorch.strategies.DDPStrategy.html") class with `"smddp"` for
   `process_group_backend` and `"gpu"` for
   `accelerator`, and pass that to the [Trainer](https://pytorch-lightning.readthedocs.io/en/stable/common/trainer.html "https://pytorch-lightning.readthedocs.io/en/stable/common/trainer.html") class.

```
import lightning as pl
from lightning.pytorch.strategies import DDPStrategy

ddp = DDPStrategy(
    cluster_environment=env,
    process_group_backend="**smddp**",
    accelerator="gpu"
)

trainer = pl.Trainer(
    max_epochs=200,
    strategy=ddp,
    devices=num_gpus,
    num_nodes=num_nodes
)
```

**For PyTorch FSDP** – Create an object of
the [FSDPStrategy](https://lightning.ai/docs/pytorch/stable/api/lightning.pytorch.strategies.FSDPStrategy.html "https://lightning.ai/docs/pytorch/stable/api/lightning.pytorch.strategies.FSDPStrategy.html") class (with [wrapping policy](https://pytorch.org/docs/stable/fsdp.html "https://pytorch.org/docs/stable/fsdp.html") of choice)
with `"smddp"` for `process_group_backend` and
`"gpu"` for `accelerator`, and pass that to the [Trainer](https://pytorch-lightning.readthedocs.io/en/stable/common/trainer.html "https://pytorch-lightning.readthedocs.io/en/stable/common/trainer.html") class.

```
import lightning as pl
from lightning.pytorch.strategies import FSDPStrategy

from functools import partial
from torch.distributed.fsdp.wrap import size_based_auto_wrap_policy

policy = partial(
    size_based_auto_wrap_policy,
    min_num_params=10000
)

fsdp = FSDPStrategy(
    auto_wrap_policy=policy,
    process_group_backend="smddp",
    cluster_environment=env
)

trainer = pl.Trainer(
    max_epochs=200,
    strategy=fsdp,
    devices=num_gpus,
    num_nodes=num_nodes
)
```

After you have completed adapting your training script, proceed to [Launching distributed training jobs with SMDDP using the
SageMaker Python SDK](data-parallel-use-api.md "data-parallel-use-api.md").

###### Note

When you construct a SageMaker AI PyTorch estimator and submit a training job request in [Launching distributed training jobs with SMDDP using the
SageMaker Python SDK](data-parallel-use-api.md "data-parallel-use-api.md"), you need to provide `requirements.txt` to
install `pytorch-lightning` and `lightning-bolts` in the SageMaker AI
PyTorch training container.

```
# requirements.txt
pytorch-lightning
lightning-bolts
```

For more information about specifying the source directory to place the
`requirements.txt` file along with your training script and a job submission,
see [Using third-party libraries](https://sagemaker.readthedocs.io/en/stable/frameworks/pytorch/using_pytorch.html#id12 "https://sagemaker.readthedocs.io/en/stable/frameworks/pytorch/using_pytorch.html#id12") in the _Amazon SageMaker AI
Python SDK documentation_.
