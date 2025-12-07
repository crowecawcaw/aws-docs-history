# Release notes

See the following release notes to track the latest updates for the SageMaker HyperPod checkpointless training.

**The SageMaker HyperPod checkpointless training v1.0.0**

Date: Dec 03, 2025

**SageMaker HyperPod checkpointless training Features**

- **Collective Communication Initialization Improvements**: Offers novel initialization methods, Rootless and TCPStoreless for NCCL and Gloo.
- **Memory-mapped (MMAP)** Dataloader: Caches (persist) prefetched batches so that they are available even when a fault causes a restart of the training job.
- **Checkpointless**: Enables faster recovery from cluster training faults in large-scale distributed training environments by making framework-level optimizations
- **Built on Nvidia Nemo and PyTorch Lightning**: Leverages these powerful frameworks for efficient and flexible model training

      + [Nividia NeMo](https://github.com/NVIDIA-NeMo/NeMo "https://github.com/NVIDIA-NeMo/NeMo")
      + [PyTorch Lightning](https://lightning.ai/docs/pytorch/stable/ "https://lightning.ai/docs/pytorch/stable/")

  **SageMaker HyperPod Checkpointless training Docker container**

Checkpointless training on HyperPod is built on top of the [NVIDIA NeMo framework](https://docs.nvidia.com/nemo-framework/user-guide/latest/overview.html "https://docs.nvidia.com/nemo-framework/user-guide/latest/overview.html"). HyperPod checkpointless training aims to recover faster from cluster training faults in large-scale distributed training environments by making framework-level optimizations that will be delivered on a base container containing the base image with NCCL and PyTorch optimizations.

**Availability**

Currently images are only available in:

```
eu-north-1
ap-south-1
us-east-2
eu-west-1
eu-central-1
sa-east-1
us-east-1
eu-west-2
ap-northeast-1
us-west-2
us-west-1
ap-southeast-1
ap-southeast-2
```

but not available in the following 3 opt-in Regions:

```
ap-southeast-3
ap-southeast-4
eu-south-2
```

**Container details**

Checkpointless training Docker container for PyTorch v2.6.0 with CUDA v12.9

```
963403601044.dkr.ecr.eu-north-1.amazonaws.com/hyperpod-checkpointless-training:v1.0.0
423350936952.dkr.ecr.ap-south-1.amazonaws.com/hyperpod-checkpointless-training:v1.0.0
556809692997.dkr.ecr.us-east-2.amazonaws.com/hyperpod-checkpointless-training:v1.0.0
942446708630.dkr.ecr.eu-west-1.amazonaws.com/hyperpod-checkpointless-training:v1.0.0
391061375763.dkr.ecr.eu-central-1.amazonaws.com/hyperpod-checkpointless-training:v1.0.0
311136344257.dkr.ecr.sa-east-1.amazonaws.com/hyperpod-checkpointless-training:v1.0.0
327873000638.dkr.ecr.us-east-1.amazonaws.com/hyperpod-checkpointless-training:v1.0.0
016839105697.dkr.ecr.eu-west-2.amazonaws.com/hyperpod-checkpointless-training:v1.0.0
356859066553.dkr.ecr.ap-northeast-1.amazonaws.com/hyperpod-checkpointless-training:v1.0.0
920498770698.dkr.ecr.us-west-2.amazonaws.com/hyperpod-checkpointless-training:v1.0.0
827510180725.dkr.ecr.us-west-1.amazonaws.com/hyperpod-checkpointless-training:v1.0.0
885852567298.dkr.ecr.ap-southeast-1.amazonaws.com/hyperpod-checkpointless-training:v1.0.0
304708117039.dkr.ecr.ap-southeast-2.amazonaws.com/hyperpod-checkpointless-training:v1.0.0
```

**Pre-installed packages**

```
PyTorch: v2.6.0
CUDA: v12.9
NCCL: v2.27.5
EFA: v1.43.0
AWS-OFI-NCCL v1.16.0
Libfabric version 2.1
Megatron v0.15.0
Nemo v2.6.0rc0
```
