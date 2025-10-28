# Set up managed tiered checkpointing

This section contains setup process for managed tiered checkpointing for Amazon SageMaker HyperPod.
You’ll learn how to enable the capability on your cluster and implement checkpointing in your
training code.

###### Topics

- [Prerequisites](#managed-tier-checkpointing-setup-prerequisites "#managed-tier-checkpointing-setup-prerequisites")
- [Step 1: Enable
  managed tiered checkpointing for your cluster](#managed-tier-checkpointing-setup-step-enable-for-cluster "#managed-tier-checkpointing-setup-step-enable-for-cluster")
- [Step 2: Install the
  Python library in your training image](#managed-tier-checkpointing-setup-step-install-library "#managed-tier-checkpointing-setup-step-install-library")
- [Step 3: Save
  checkpoints in your training loop](#managed-tier-checkpointing-setup-step-save-checkpoint-in-loop "#managed-tier-checkpointing-setup-step-save-checkpoint-in-loop")
- [Step 4: Load
  checkpoints for recovery](#managed-tier-checkpointing-setup-step-load-checkpoint "#managed-tier-checkpointing-setup-step-load-checkpoint")
- [Validate your managed tiered
  checkpointing operations](#managed-tier-checkpointing-setup-validation "#managed-tier-checkpointing-setup-validation")

## Prerequisites

Before setting up managed tiered checkpointing, ensure you have:

- An Amazon EKS HyperPod cluster with sufficient CPU memory available for
  checkpoint allocation
- PyTorch training workloads and DCP jobs (both are supported)
- Appropriate IAM permissions for cluster management, including:
  - Amazon CloudWatch and Amazon S3 write permissions for the training pod to read/write
    checkpoints and push metrics
  - These permissions can be configured via [EKS OIDC
    setup](../../../eks/latest/userguide/iam-roles-for-service-accounts.md "../../../eks/latest/userguide/iam-roles-for-service-accounts.md")

## Step 1: Enable

managed tiered checkpointing for your cluster

###### Important

You must opt in to use managed tiered checkpointing.

Enable managed tiered checkpointing through the HyperPod APIs when creating or
updating your cluster. The service automatically installs the memory management system when
you specify the `TieredStorageConfig` parameter.

For new clusters, you can use [`create-cluster`](../../../cli/latest/reference/sagemaker/create-cluster.md "../../../cli/latest/reference/sagemaker/create-cluster.md") AWS CLI.

```
aws sagemaker create-cluster \
    --cluster-name `cluster-name` \
    --orchestrator "Eks={ClusterArn=`eks-cluster-arn`}" \
    --instance-groups '{
        "InstanceGroupName": "`instance-group-name`",
        "InstanceType": "`instance-type`",
        "InstanceCount": `instance-count`,
        "LifeCycleConfig": {
            "SourceS3Uri": "`s3-path-to-lifecycle-scripts`",
            "OnCreate": "`lifecycle-script-name`"
        },
        "ExecutionRole": "`instance-group-iam-role`",
        "ThreadsPerCore": `threads-per-core`,
        "InstanceStorageConfigs": [
            { "EbsVolumeConfig": {"VolumeSizeInGB": `volume-size`} }
        ]
    }' \
    --vpc-config '{
        "SecurityGroupIds": ["`security-group-ids`"],
        "Subnets": ["`subnets`"]
    }' \
    --tiered-storage-config '{
        "Mode": "Enable"
    }'
```

The `InstanceMemoryAllocationPercentage` parameter specifies the
`percentage` (int) of cluster memory to allocate
for checkpointing. The range is 20-100.

## Step 2: Install the

Python library in your training image

Install the [Amazon SageMaker
checkpointing library](https://pypi.org/project/amzn-sagemaker-checkpointing/ "https://pypi.org/project/amzn-sagemaker-checkpointing/") and its dependencies in your training image by adding it to
your Dockerfile:

```
# Add this line to your training image Dockerfile
RUN pip install amzn-sagemaker-checkpointing s3torchconnector tenacity torch boto3 s3torchconnector
```

## Step 3: Save

checkpoints in your training loop

In your training loop, you can asynchronously save checkpoints using PyTorch DCP. The
following is an example on how to do so.

```
import torch
import torch.distributed as dist
from torch.distributed.checkpoint import async_save, load
from amzn_sagemaker_checkpointing.checkpointing.filesystem.filesystem import (
    SageMakerTieredStorageWriter,
    SageMakerTieredStorageReader
)

# Initialize distributed training
dist.init_process_group(backend="nccl")

# Configure checkpointing
checkpoint_config = SageMakerCheckpointConfig(
    # Unique ID for your training job
    # Allowed characters in ID include: alphanumeric, hyphens, and underscores
    namespace=os.environ.get('TRAINING_JOB_NAME', f'job-{int(time.time())}'),

    # Number of distributed processes/available GPUs
    world_size=dist.get_world_size(),

    # S3 storage location, required for SageMakerTieredStorageReader for read fallbacks
    # Required for SageMakerTieredStorageWriter when save_to_s3 is True
    s3_tier_base_path="s3://my-bucket/checkpoints"
)

# Your model and optimizer
model = MyModel()
optimizer = torch.optim.AdamW(model.parameters())

# Training loop
future = None
in_memory_ckpt_freq = 10
s3_ckpt_freq = 50

for training_step in range(1000):
    # ... training code ...

    # Save checkpoint
    if (training_step % in_memory_ckpt_freq == 0 or
        training_step % s3_ckpt_freq == 0):
        # Create state dictionary
        state_dict = {
            "model": model.state_dict(),
            "optimizer": optimizer.state_dict(),
            "step": training_step,
            "epoch": epoch
        }

        # Create storage writer for current step
        checkpoint_config.save_to_s3 = training_step % s3_ckpt_freq == 0
        storage_writer = SageMakerTieredStorageWriter(
            checkpoint_config=checkpoint_config,
            step=training_step
        )

        # wait for previous checkpoint to get completed
        if future is not None:
            exc = future.exception()
            if exc:
                print(f"Failure in saving previous checkpoint:{str(exc)}")
                # Handle failures as required
            else:
                result = future.result()
                # Process results from save, if required

        # Async save checkpoint using PyTorch DCP
        future = async_save(state_dict=state_dict, storage_writer=storage_writer)

        # Continue training while checkpoint saves in background
```

## Step 4: Load

checkpoints for recovery

The following is an example on loading a checkpoint.

```
# Create state dictionary template
state_dict = {
    "model": model.state_dict(),
    "optimizer": optimizer.state_dict(),
    "step": 0,
    "epoch": 0
}

# Load latest checkpoint
storage_reader = SageMakerTieredStorageReader(checkpoint_config=checkpoint_config)
load(state_dict, storage_reader=storage_reader)

# Load specific checkpoint step
storage_reader = SageMakerTieredStorageReader(
    checkpoint_config=checkpoint_config,
    step=500 # Or don't pass step if you have to load the latest available step.
)
try:
    load(state_dict, storage_reader=storage_reader)
except BaseException as e:
    print(f"Checkpoint load failed: {str(e)}")
    # Add additional exception handling
```

## Validate your managed tiered

checkpointing operations

You can validate your managed tiered checkpointing operations with logs.

**Custom logging (optional)**

You can integrate checkpointing logs with other logs by passing a custom logger to the
library. For example, you can add a custom logger to your training code so that all logs
from the library are also collected in the training logger.

**Enhanced service logging (optional)**

For enhanced debugging and service visibility, you can mount the checkpointing log path
`/var/log/sagemaker_checkpointing` from within your pod to a path
`/var/logs/sagemaker_checkpointing` on your host. This ensures that
only library-specific logs are collected separately. This provides the service team with
enhanced visibility for debugging and support.
