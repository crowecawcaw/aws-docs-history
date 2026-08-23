# Automatic node recovery with Ray

HyperPod detects hardware and GPU faults on a node and recovers that node without
operator action. This runs at the infrastructure layer. Ray needs no configuration for it, and
your training code does not change.

## Setup

Set `NodeRecovery` to `Automatic` on the HyperPod
cluster. You apply this when you create or update the cluster, not from Ray. For more
information, see [NodeRecovery](../APIReference/API_CreateCluster.md#sagemaker-CreateCluster-request-NodeRecovery "../APIReference/API_CreateCluster.md#sagemaker-CreateCluster-request-NodeRecovery") in the _SageMaker AI API Reference_.

After node recovery is on for the cluster, it applies to every Ray workload that runs on
it.

## How it works with Ray

HyperPod recovers a faulty node by rebooting it or by replacing it. Ray treats
the node leaving and rejoining as ordinary worker loss. The head detects the lost workers
and reschedules the affected tasks and actors. Training continues as recovered nodes
rejoin the cluster.

For details of node recovery on a cluster orchestrated with Amazon EKS, see [Cluster resiliency features for SageMaker HyperPod cluster orchestrated with
Amazon EKS](sagemaker-hyperpod-eks-resiliency.md "sagemaker-hyperpod-eks-resiliency.md").

## Configure retries in Ray Train

Node recovery restores the node, but your training run must be told to retry. Ray Train
retries a run when a worker fails, up to `max_failures` on
`FailureConfig`. The default is 0, so a single node fault ends the run even
though HyperPod recovered the node.

Be liberal with retries. Hardware faults are routine at cluster scale, and a retry
resumes from your latest checkpoint rather than starting over. The following example uses
20, a deliberately high value.

```
from ray.train import FailureConfig, RunConfig, ScalingConfig
from ray.train.torch import TorchTrainer

trainer = TorchTrainer(
    train_loop_per_worker=train_func,
    scaling_config=ScalingConfig(num_workers=8, use_gpu=True),
    run_config=RunConfig(
        failure_config=FailureConfig(max_failures=20),
    ),
)
trainer.fit()
```

Set `max_failures=-1` to retry indefinitely. Retries only pay off if the run
checkpoints, so pair this with checkpointing. For more information, see [Tiered checkpointing](sagemaker-hyperpod-ray-tiered-storage.md "sagemaker-hyperpod-ray-tiered-storage.md").
