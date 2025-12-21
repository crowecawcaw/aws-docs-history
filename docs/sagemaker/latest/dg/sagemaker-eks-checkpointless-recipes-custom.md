# Tutorials - Amazon SageMaker HyperPod Checkpointless Pretraining or Finetuning Custom Models

The following sequence of steps is required to run checkpointless training with your custom model on HyperPod.

## Prerequisites

Before you start setting up your environment, make sure you have:

- [Enabled Amazon EKS support in Amazon SageMaker HyperPod](sagemaker-hyperpod-eks-prerequisites.md "sagemaker-hyperpod-eks-prerequisites.md")
- [Set up HyperPod training operator (v1.2+)](sagemaker-eks-operator.md "sagemaker-eks-operator.md")
- A shared storage location. It can be an Amazon FSx file system or NFS system that's accessible from the cluster nodes.
- Data in one of the following formats:
  - JSON
  - JSONGZ (Compressed JSON)
  - ARROW

- [Download the hugging face model weights](sagemaker-eks-checkpointless-release-notes.md "sagemaker-eks-checkpointless-release-notes.md") and covert to [Nemo supported format](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemo-2.0/features/hf-integration.html#importing-from-hugging-face "https://docs.nvidia.com/nemo-framework/user-guide/latest/nemo-2.0/features/hf-integration.html#importing-from-hugging-face").
- Setup your environment

## Kubernetes environment setup

To set up your Kubernetes environment, do the following:

1. Set up the virtual environment. Make sure you're using Python greater than or equal to 3.10 and lower than 3.14.

```
python3 -m venv ${PWD}/venv
source venv/bin/activate
```

2. [Set up kubectl and eksctl](../../../eks/latest/userguide/install-kubectl.md "../../../eks/latest/userguide/install-kubectl.md")
3. Connect to your Kubernetes cluster

```
aws eks update-kubeconfig --region "${CLUSTER_REGION}" --name "${CLUSTER_NAME}"
```

4. Install dependencies

```
# install SageMaker HyperPod checkpointless training.
git clone git@github.com:aws/sagemaker-hyperpod-checkpointless-training.git
cd sagemaker-hyperpod-checkpointless-training
```

## Checkpointless training modification instructions

To incrementally adopt checkpointless training for custom models, follow the integration guide (here we use Llama 3 70b pretraining as an example), which involves:

- Fast communicator creation
- Memory-mapped dataloader (MMAP)
- In-process & Checkpointless recovery

### Component 1: Fast communicator creation

This is to optimize time to establish connections between the workers. There is no code changes needed and only requires setting env variables

```
  # Enable Rootless features
  export HPCT_USE_ROOTLESS=1 && \
  sysctl -w net.ipv4.ip_local_port_range="20000 65535" && \

  hyperpodrun --nproc_per_node=8 \
              ...
              --inprocess-restart \
              ...
```

The full change can be found in the
[llama3 70 pretrain launch job config](https://github.com/aws/sagemaker-hyperpod-checkpointless-training/blob/main/examples/llama3/launch/pretrain_llama3_70b_checkpointless_p5.yaml "https://github.com/aws/sagemaker-hyperpod-checkpointless-training/blob/main/examples/llama3/launch/pretrain_llama3_70b_checkpointless_p5.yaml").

### Component 2: Memory-mapped dataloader (MMAP)

MMAP caches to store pre-fetched data samples & enable immediate training start without needing to wait for data preprocessing.
It requires minimal code changes to adopt by wrapping existing dataloader.

```
data_module = MMAPDataModule(
  data_module=base_data_module,
  mmap_config=CacheResumeMMAPConfig(cache_dir=…)
)
```

### Components 3 and 4: In-process and checkpointless recovery

This enables failure recovery without restart training processes or loading from checkpoints. Additional code changes needed
(strategy & training config update, wrap existing main)

```
@HPWrapper(
  health_check=CudaHealthCheck(),
  hp_api_factory=HPAgentK8sAPIFactory(),
  abort_timeout=60.0,
...)
def run_main(
  cfg,
  caller: Optional[HPCallWrapper] = None):
...


CheckpointlessMegatronStrategy(
  **self.cfg.strategy,
  ddp=self.ddp,
)
```

The full change can be found in the [llama3 70 pretrain entry script](https://github.com/aws/sagemaker-hyperpod-checkpointless-training/blob/main/examples/llama3/llama3_70b_pretrain_checkpointless.py "https://github.com/aws/sagemaker-hyperpod-checkpointless-training/blob/main/examples/llama3/llama3_70b_pretrain_checkpointless.py") and the corresponding training config change can be
found in the [llama3 70b training config](https://github.com/aws/sagemaker-hyperpod-checkpointless-training/blob/main/examples/llama3/config/llama3_70b_peft_checkpointless.yaml "https://github.com/aws/sagemaker-hyperpod-checkpointless-training/blob/main/examples/llama3/config/llama3_70b_peft_checkpointless.yaml").

### Launch training

You can now launch the checkpointless training using kubectl.

```
kubectl apply -f your_job_config.yaml
```
