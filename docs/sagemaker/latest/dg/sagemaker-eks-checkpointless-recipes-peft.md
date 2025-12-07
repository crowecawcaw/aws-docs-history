# Amazon SageMaker HyperPod checkpointless PEFT-LoRA

The following sequence of steps is required to run checkpointless training recipes on HyperPod.

## Prerequisites

Before you start setting up your environment, make sure you have:

- [Enabled Amazon EKS support in Amazon SageMaker HyperPod](sagemaker-hyperpod-eks-prerequisites.md "sagemaker-hyperpod-eks-prerequisites.md")
- [Set up HyperPod training operator (v1.2+)](sagemaker-eks-operator.md "sagemaker-eks-operator.md")
- A shared storage location. It can be an Amazon FSx file system or NFS system that's accessible from the cluster nodes.
- Data in one of the following formats:
  - JSON
  - JSONGZ (Compressed JSON)
  - ARROW

- Pick a supported checkpointless training recipe for Llama 70B or GPT-OSS 120B from the [source](https://github.com/aws/sagemaker-hyperpod-recipes/tree/main/recipes_collection "https://github.com/aws/sagemaker-hyperpod-recipes/tree/main/recipes_collection").
- [Download the hugging face model weights](sagemaker-eks-checkpointless-release-notes.md "sagemaker-eks-checkpointless-release-notes.md") and covert to [Nemo supported format](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemo-2.0/features/hf-integration.html#importing-from-hugging-face "https://docs.nvidia.com/nemo-framework/user-guide/latest/nemo-2.0/features/hf-integration.html#importing-from-hugging-face").
- Setup your environment

## Kubernetes environment setup

To set up your Kubernetes environment, do the following:

1. Set up the virtual environment. Make sure you're using Python >= 3.10 and < 3.14.

```
python3 -m venv ${PWD}/venv
source venv/bin/activate
```

2. [Set up kubectl and eksctl](../../../eks/latest/userguide/install-kubectl.md "../../../eks/latest/userguide/install-kubectl.md")
3. [Install Helm](https://helm.sh/docs/intro/install/ "https://helm.sh/docs/intro/install/")
4. Connect to your Kubernetes cluster

```
aws eks update-kubeconfig --region "${CLUSTER_REGION}" --name "${CLUSTER_NAME}"
```

5. Install dependencies using one of the following methods:
   - SageMaker HyperPod recipes method:

   ```
   # install SageMaker HyperPod Recipes.
   git clone --recursive git@github.com:aws/sagemaker-hyperpod-recipes.git
   cd sagemaker-hyperpod-recipes
   pip3 install -r requirements.txt
   ```

   - kubectl with pre-defined job yaml method

   ```
   # install SageMaker HyperPod checkpointless training.
   git clone git@github.com:aws/sagemaker-hyperpod-checkpointless-training.git
   cd sagemaker-hyperpod-checkpointless-training
   ```

You can now launch the checkpointless training recipe using either the NeMo-style launcher or using kubectl.

## Launch the training job with the recipes launcher

Alternatively, you can use the SageMaker HyperPod recipes to submit your training job. Using the recipes involves updating k8s.yaml, config.yaml and running the launch script.

1. Update launcher_scripts/gpt_oss/run_checkpointless_gpt_oss_120b_lora.sh

your_contrainer: A Deep Learning container. To find the most recent release of the
checkpointless training container, see [checkpointless training release notes](sagemaker-eks-checkpointless-release-notes.md "sagemaker-eks-checkpointless-release-notes.md").

```
#!/bin/bash
SAGEMAKER_TRAINING_LAUNCHER_DIR=${SAGEMAKER_TRAINING_LAUNCHER_DIR:-"$(pwd)"}
TRAIN_DIR="${TRAIN_DIR}"
VAL_DIR="${VAL_DIR}"
EXP_DIR="${EXP_DIR}"
LOG_DIR="${LOG_DIR}"
CONTAINER_MOUNT="/data"
CONTAINER="${CONTAINER}"
MODEL_NAME_OR_PATH="${MODEL_NAME_OR_PATH}"

HYDRA_FULL_ERROR=1 python3 "${SAGEMAKER_TRAINING_LAUNCHER_DIR}/main.py" \
    recipes=fine-tuning/gpt_oss/checkpointless_gpt_oss_120b_lora \
    recipes.dataset.dataset_path="${TRAIN_DIR}" \
    recipes.exp_manager.exp_dir="${EXP_DIR}" \
    recipes.log_dir="${LOG_DIR}" \
    recipes.resume.restore_config.path="${MODEL_NAME_OR_PATH}" \
    base_results_dir="${SAGEMAKER_TRAINING_LAUNCHER_DIR}/results" \
    git.use_default=false \
    cluster=k8s \
    cluster_type=k8s \
    container="${CONTAINER}" \
    +cluster.hostNetwork=true \
    +cluster.persistent_volume_claims.0.claimName=fsx-claim \
    +cluster.persistent_volume_claims.0.mountPath="${CONTAINER_MOUNT}" \
    +recipes.dataset.val_dataset_path="${VAL_DIR}" \
    ++recipes.callbacks.3.test_fault_config.fault_prob_between_lock=1 \
```

2. Launch the training job

```
bash launcher_scripts/gpt_oss/run_checkpointless_gpt_oss_120b_lora.sh
```

After you've submitted the training job, you can use the following command to verify if you submitted it successfully.

```
kubectl get pods

NAME                             READY   STATUS             RESTARTS        AGE
gpt-oss-120b-worker-0             0/1    running               0            36s
```

If the STATUS is at PENDING or ContainerCreating, run the following command to get more details

```
kubectl describe pod <name of pod>
```

After the job STATUS changes to Running, you can examine the log by using the following command.

```
kubectl logs <name of pod>
```

The STATUS will turn to Completed when you run kubectl get pods

## Launch the training job with kubectl with pre-defined yaml

Another optional is to launch the training through kubectl with a pre-defined job yaml.

1. update the examples/gpt_oss/launch/peft_gpt_oss_120b_checkpointless_p5.yaml.yaml
   - image: A Deep Learning container. To find the most recent release of the checkpointless training container, see
     [checkpointless training release notes](sagemaker-eks-checkpointless-release-notes.md "sagemaker-eks-checkpointless-release-notes.md").
   - resume.restore_config.path=<path_to_pretrained_weights>: The path to downloaded pretrained model
     weights in Nemo format in
     [Prerequisites](sagemaker-eks-checkpointless-recipes-peft.md#sagemaker-eks-checkpointless-recipes-peft-prereqs "sagemaker-eks-checkpointless-recipes-peft.md#sagemaker-eks-checkpointless-recipes-peft-prereqs") step.
   - dataset.dataset_path=<path_to_dataset>: The path to the dataset that stored in the shared storage

2. Submit the job using kubectl with peft_gpt_oss_120b_checkpointless_p5.yaml.yaml

```
kubectl apply -f examples/gpt_oss/launch/peft_gpt_oss_120b_checkpointless_p5.yaml.yaml
```

After you've submitted the training job, you can use the following command to verify if you submitted it successfully.

```
kubectl get pods

NAME                                             READY   STATUS             RESTARTS        AGE
gpt-120b-lora-checkpointless-worker-0             0/1    running               0            36s
```

If the STATUS is at PENDING or ContainerCreating, run the following command to get more details

```
kubectl describe pod <name of pod>
```

After the job STATUS changes to Running, you can examine the log by using the following command.

```
kubectl logs <name of pod>
```

The STATUS will turn to Completed when you run kubectl get pods
