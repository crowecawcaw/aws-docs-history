# Kubernetes

cluster pre-training tutorial (GPU)

There are two ways to launch a training job in a GPU Kubernetes cluster:

- (Recommended) [HyperPod command-line tool](https://github.com/aws/sagemaker-hyperpod-cli "https://github.com/aws/sagemaker-hyperpod-cli")
- The NeMo style launcher

###### Prerequisites

Before you start setting up your environment, make sure you have:

- A HyperPod GPU Kubernetes cluster is setup properly.
- A shared storage location. It can be an Amazon FSx file system or NFS system
  that's accessible from the cluster nodes.
- Data in one of the following formats:
  - JSON
  - JSONGZ (Compressed JSON)
  - ARROW

- (Optional) You must get a HuggingFace token if you're using the model
  weights from HuggingFace for pre-training or fine-tuning. For more
  information about getting the token, see [User access
  tokens](https://huggingface.co/docs/hub/en/security-tokens "https://huggingface.co/docs/hub/en/security-tokens").

## GPU Kubernetes

environment setup

To set up a GPU Kubernetes environment, do the following:

- Set up the virtual environment. Make sure you're using Python 3.9 or
  greater.

```
python3 -m venv ${PWD}/venv
source venv/bin/activate

```

- Install dependencies using one of the following methods:
  - (Recommended): [HyperPod command-line tool](https://github.com/aws/sagemaker-hyperpod-cli "https://github.com/aws/sagemaker-hyperpod-cli") method:

  ```
  # install HyperPod command line tools
  git clone https://github.com/aws/sagemaker-hyperpod-cli
  cd sagemaker-hyperpod-cli
  pip3 install .

  ```

  - SageMaker HyperPod recipes method:

  ```
  # install SageMaker HyperPod Recipes.
  git clone --recursive git@github.com:aws/sagemaker-hyperpod-recipes.git
  cd sagemaker-hyperpod-recipes
  pip3 install -r requirements.txt

  ```

- [Set up kubectl and
  eksctl](../../../eks/latest/userguide/install-kubectl.md "../../../eks/latest/userguide/install-kubectl.md")
- [Install
  Helm](https://helm.sh/docs/intro/install/ "https://helm.sh/docs/intro/install/")
- Connect to your Kubernetes cluster

```
aws eks update-kubeconfig --region "`CLUSTER_REGION`" --name "`CLUSTER_NAME`"
hyperpod connect-cluster --cluster-name "`CLUSTER_NAME`" [--region "`CLUSTER_REGION`"] [--namespace <namespace>]

```

## Launch

the training job with the SageMaker HyperPod CLI

We recommend using the SageMaker HyperPod command-line interface (CLI) tool to submit
your training job with your configurations. The following example submits a training
job for the `hf_llama3_8b_seq16k_gpu_p5x16_pretrain` model.

- `your_training_container`: A Deep Learning container. To find
  the most recent release of the SMP container, see [Release notes for the SageMaker model parallelism
  library](model-parallel-release-notes.md "model-parallel-release-notes.md").
- (Optional) You can provide the HuggingFace token if you need pre-trained
  weights from HuggingFace by setting the following key-value pair:

```
"recipes.model.hf_access_token": "`<your_hf_token>`"
```

```
hyperpod start-job --recipe training/llama/hf_llama3_8b_seq16k_gpu_p5x16_pretrain \
--persistent-volume-claims fsx-claim:data \
--override-parameters \
'{
"recipes.run.name": "hf-llama3-8b",
"recipes.exp_manager.exp_dir": "/data/`<your_exp_dir>`",
"container": "658645717510.dkr.ecr.`<region>`.amazonaws.com/smdistributed-modelparallel:2.4.1-gpu-py311-cu121",
"recipes.model.data.train_dir": "`<your_train_data_dir>`",
"recipes.model.data.val_dir": "`<your_val_data_dir>`",
"cluster": "k8s",
"cluster_type": "k8s"
}'

```

After you've submitted a training job, you can use the following command to verify
if you submitted it successfully.

```
kubectl get pods
NAME                             READY   STATUS             RESTARTS        AGE
hf-llama3-<your-alias>-worker-0   0/1     running         0               36s

```

If the `STATUS` is `PENDING` or
`ContainerCreating`, run the following command to get more
details.

```
kubectl describe pod `name_of_pod`
```

After the job `STATUS` changes to `Running`, you can examine
the log by using the following command.

```
kubectl logs `name_of_pod`
```

The `STATUS` becomes `Completed` when you run `kubectl
 get pods`.

## Launch the training job with the recipes launcher

Alternatively, you can use the SageMaker HyperPod recipes to submit your training job.
Using the recipes involves updating `k8s.yaml`, `config.yaml`,
and running the launch script.

- In `k8s.yaml`, update `persistent_volume_claims`. It
  mounts the Amazon FSx claim to the `/data` directory of each computing
  pod

```
persistent_volume_claims:
  - claimName: fsx-claim
    mountPath: data
```

- In `config.yaml`, update `repo_url_or_path` under
  `git`.

```
git:
  repo_url_or_path: `<training_adapter_repo>`
  branch: null
  commit: null
  entry_script: null
  token: null
```

- Update
  `launcher_scripts/llama/run_hf_llama3_8b_seq16k_gpu_p5x16_pretrain.sh`
  - `your_contrainer`: A Deep Learning container. To find
    the most recent release of the SMP container, see [Release notes for the SageMaker model parallelism
    library](model-parallel-release-notes.md "model-parallel-release-notes.md").
  - (Optional) You can provide the HuggingFace token if you need
    pre-trained weights from HuggingFace by setting the following
    key-value pair:

  ```
  recipes.model.hf_access_token=`<your_hf_token>`
  ```

```
#!/bin/bash
#Users should setup their cluster type in /recipes_collection/config.yaml
REGION="`<region>`"
IMAGE="658645717510.dkr.ecr.${REGION}.amazonaws.com/smdistributed-modelparallel:2.4.1-gpu-py311-cu121"
SAGEMAKER_TRAINING_LAUNCHER_DIR=${SAGEMAKER_TRAINING_LAUNCHER_DIR:-"$(pwd)"}
EXP_DIR="`<your_exp_dir>`" # Location to save experiment info including logging, checkpoints, ect
TRAIN_DIR="`<your_training_data_dir>`" # Location of training dataset
VAL_DIR="`<your_val_data_dir>`" # Location of talidation dataset

HYDRA_FULL_ERROR=1 python3 "${SAGEMAKER_TRAINING_LAUNCHER_DIR}/main.py" \
    recipes=training/llama/hf_llama3_8b_seq8k_gpu_p5x16_pretrain \
    base_results_dir="${SAGEMAKER_TRAINING_LAUNCHER_DIR}/results" \
    recipes.run.name="hf-llama3" \
    recipes.exp_manager.exp_dir="$EXP_DIR" \
    cluster=k8s \
    cluster_type=k8s \
    container="${IMAGE}" \
    recipes.model.data.train_dir=$TRAIN_DIR \
    recipes.model.data.val_dir=$VAL_DIR

```

- Launch the training job

```
bash launcher_scripts/llama/run_hf_llama3_8b_seq16k_gpu_p5x16_pretrain.sh
```

After you've submitted the training job, you can use the following command to
verify if you submitted it successfully.

```
kubectl get pods
```

```
NAME READY   STATUS             RESTARTS        AGE
hf-llama3-<your-alias>-worker-0   0/1     running         0               36s

```

If the `STATUS` is `PENDING` or
`ContainerCreating`, run the following command to get more
details.

```
kubectl describe pod `<name-of-pod>`
```

After the job `STATUS` changes to `Running`, you can examine
the log by using the following command.

```
kubectl logs `name_of_pod`
```

The `STATUS` will turn to `Completed` when you run
`kubectl get pods`.

For more information about the k8s cluster configuration, see [Running a training job on HyperPod k8s](cluster-specific-configurations-run-training-job-hyperpod-k8s.md "cluster-specific-configurations-run-training-job-hyperpod-k8s.md").
