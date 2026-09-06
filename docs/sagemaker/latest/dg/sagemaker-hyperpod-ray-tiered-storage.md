

# Tiered checkpointing
<a name="sagemaker-hyperpod-ray-tiered-storage"></a>

HyperPod managed tiered checkpointing writes checkpoints to your cluster's CPU memory first and replicates them across nodes. It periodically persists them to durable storage such as Amazon S3. Because the fast tier is memory rather than object storage, you can checkpoint more often and lose less progress when a node fails. For how it works and how to configure it, see [HyperPod managed tiered checkpointing](managed-tier-checkpointing.md).

## Setup
<a name="sagemaker-hyperpod-ray-tiered-storage-setup"></a>

Set up managed tiered checkpointing on the cluster first. It is a cluster-level capability, and the setup is the same whatever framework you train with. For the steps, see [Set up managed tiered checkpointing](managed-tier-checkpointing-setup.md).

Then install the checkpointing package on the hosts that run your Ray workload.

```
pip install amzn-sagemaker-checkpointing
```

## Use it with Ray Train
<a name="sagemaker-hyperpod-ray-tiered-storage-use"></a>

Save checkpoints through `SageMakerTieredStorageWriter` instead of letting Ray upload them. Build a `SageMakerCheckpointConfig` inside your training function and pass the writer to `async_save`. Report the checkpoint asynchronously so training continues while the checkpoint uploads to Amazon S3.

This example uses [asynchronous checkpoint uploading](https://docs.ray.io/en/latest/train/user-guides/checkpoints.html#asynchronous-checkpoint-uploading) in the Ray documentation, which lets Ray Train kick off a background thread to wait for the upload to complete while training continues on the next step. The `save_checkpoint` function stages the checkpoint to tiered storage and reports it to Ray Train with `CheckpointUploadMode.ASYNC`. `ray.train.report` records the checkpoint with Ray Train so it can track the best checkpoints, enforce `num_to_keep`, and restore from the latest checkpoint on failure. For more information about Ray Train checkpointing, see [Saving and loading checkpoints](https://docs.ray.io/en/latest/train/user-guides/checkpoints.html) in the Ray documentation.

```
import os
import torch.distributed as dist
from torch.distributed.checkpoint import async_save, load

import ray
import ray.train
from ray.train import (
    Checkpoint, CheckpointConfig, CheckpointUploadMode,
    RunConfig, ScalingConfig, FailureConfig,
)
from ray.train.torch import TorchTrainer

from amzn_sagemaker_checkpointing.config.sagemaker_checkpoint_config import SageMakerCheckpointConfig
from amzn_sagemaker_checkpointing.checkpointing.filesystem.filesystem import (
    SageMakerTieredStorageWriter,
    SageMakerTieredStorageReader,
)

S3_PATH = "s3://my-bucket/checkpoints"
EXPERIMENT_NAME = "my-experiment"


def create_checkpoint_config():
    """Create a checkpoint config scoped to this training job."""
    return SageMakerCheckpointConfig(
        namespace=EXPERIMENT_NAME,
        world_size=dist.get_world_size(),
        s3_tier_base_path=S3_PATH,
    )


# Track the previous checkpoint future to avoid async_save deadlock.
# Only one async_save can be in flight at a time because background
# threads perform collectives that require all ranks to participate.
_prev_checkpoint_future = None


def save_checkpoint(model, optimizer, config, step, metrics):
    """Save a checkpoint asynchronously and report it to Ray Train."""
    global _prev_checkpoint_future

    # Wait for the previous checkpoint to finish before starting a new one.
    if _prev_checkpoint_future is not None:
        _prev_checkpoint_future.result()

    config.save_to_s3 = True
    writer = SageMakerTieredStorageWriter(checkpoint_config=config, step=step)
    state_dict = {
        "model": model.state_dict(),
        "optimizer": optimizer.state_dict(),
        "step": step,
    }

    future = async_save(state_dict=state_dict, storage_writer=writer)
    _prev_checkpoint_future = future

    def wait_for_upload(checkpoint, name):
        future.result()
        return checkpoint

    ray.train.report(
        metrics=metrics,
        checkpoint=Checkpoint(writer.s3_checkpoint_dir),
        checkpoint_upload_mode=CheckpointUploadMode.ASYNC,
        checkpoint_upload_fn=wait_for_upload,
        delete_local_checkpoint_after_upload=False,
    )


def load_checkpoint(model, optimizer, config):
    """Load the latest checkpoint if one exists. Returns the next step number."""
    reader = SageMakerTieredStorageReader(checkpoint_config=config)
    state_dict = {
        "model": model.state_dict(),
        "optimizer": optimizer.state_dict(),
        "step": 0,
    }
    try:
        load(state_dict, storage_reader=reader)
    except FileNotFoundError:
        # No checkpoint found, start from scratch.
        return 0

    model.load_state_dict(state_dict["model"])
    optimizer.load_state_dict(state_dict["optimizer"])
    return state_dict["step"] + 1


def train_func(config):
    device = ray.train.torch.get_device()
    model = build_model().to(device)
    optimizer = torch.optim.AdamW(model.parameters(), lr=1e-3)

    ckpt_config = create_checkpoint_config()
    start_step = load_checkpoint(model, optimizer, ckpt_config)

    for step in range(start_step, config["max_steps"]):
        loss = train_step(model, optimizer)

        if step % config["checkpoint_freq"] == 0:
            save_checkpoint(
                model, optimizer, ckpt_config, step,
                metrics={"loss": loss, "step": step},
            )


trainer = TorchTrainer(
    train_func,
    train_loop_config={"max_steps": 1000, "checkpoint_freq": 10},
    scaling_config=ScalingConfig(num_workers=4, use_gpu=True),
    run_config=RunConfig(
        name=EXPERIMENT_NAME,
        storage_path=S3_PATH,
        failure_config=FailureConfig(max_failures=3),
        checkpoint_config=CheckpointConfig(num_to_keep=3),
    ),
)
```

Key points:
+ **Async save with serialized writes.** Only one `async_save` can be in flight at a time. The background threads perform collective operations that require all ranks to participate. Calling `async_save` again before the previous one completes causes a deadlock. The `_prev_checkpoint_future` pattern ensures each save finishes before the next one starts, while still overlapping the upload with the next training step.
+ **delete\_local\_checkpoint\_after\_upload=False.** Set this to prevent Ray from deleting the checkpoint reported through `ray.train.report`. Because the reported checkpoint points to an S3 path managed by the tiered storage writer, deleting it would remove the checkpoint from S3.
+ **Resume from checkpoint.** `load_checkpoint` reads from tiered storage (cluster memory first, then Amazon S3). When a node is replaced and the job restarts via `FailureConfig`, recovery reads from the fast memory tier when available, avoiding a full Amazon S3 download.