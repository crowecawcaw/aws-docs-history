# Trainium Kubernetes cluster pre-training tutorial

You can use one of the following methods to start a training job in a Trainium
Kubernetes cluster.

- (Recommended) [HyperPod command-line tool](https://github.com/aws/sagemaker-hyperpod-cli "https://github.com/aws/sagemaker-hyperpod-cli")
- The NeMo style launcher

###### Prerequisites

Before you start setting up your environment, make sure you have:

- Set up a HyperPod Trainium Kubernetes cluster
- A shared storage location that can be an Amazon FSx file system or NFS system
  that's accessible from the cluster nodes.
- Data in one of the following formats:
  - JSON
  - JSONGZ (Compressed JSON)
  - ARROW

- (Optional) You must get a HuggingFace token if you're using the model
  weights from HuggingFace for pre-training or fine-tuning. For more
  information about getting the token, see [User access
  tokens](https://huggingface.co/docs/hub/en/security-tokens "https://huggingface.co/docs/hub/en/security-tokens").

## Set up your Trainium Kubernetes environment

To set up the Trainium Kubernetes environment, do the following:

1. Complete the steps in the following tutorial: [HuggingFace Llama3-8B Pretraining](https://awsdocs-neuron.readthedocs-hosted.com/en/latest/libraries/nxd-training/tutorials/hf_llama3_8B_pretraining.html#download-the-dataset "https://awsdocs-neuron.readthedocs-hosted.com/en/latest/libraries/nxd-training/tutorials/hf_llama3_8B_pretraining.html#download-the-dataset") starting from
   **Download the dataset**.
2. Prepare a model configuration. They're available in the Neuron repo. For
   this tutorial, you can use the llama3 8b model config.
3. Virtual environment setup. Make sure you're using Python 3.9 or
   greater.

```
python3 -m venv ${PWD}/venv
source venv/bin/activate

```

4. Install the dependencies
   - (Recommended) Use the following HyperPod command-line
     tool

   ```
   # install HyperPod command line tools
   git clone https://github.com/aws/sagemaker-hyperpod-cli
   cd sagemaker-hyperpod-cli
   pip3 install .

   ```

   - If you're using SageMaker HyperPod recipes, specify the following

   ```
   # install SageMaker HyperPod Recipes.
   git clone --recursive git@github.com:aws/sagemaker-hyperpod-recipes.git
   cd sagemaker-hyperpod-recipes
   pip3 install -r requirements.txt

   ```

5. [Set up kubectl and
   eksctl](../../../eks/latest/userguide/install-kubectl.md "../../../eks/latest/userguide/install-kubectl.md")
6. [Install
   Helm](https://helm.sh/docs/intro/install/ "https://helm.sh/docs/intro/install/")
7. Connect to your Kubernetes cluster

```
aws eks update-kubeconfig --region "${CLUSTER_REGION}" --name "${CLUSTER_NAME}"
hyperpod connect-cluster --cluster-name "${CLUSTER_NAME}" [--region "${CLUSTER_REGION}"] [--namespace <namespace>]

```

8. Container: The [Neuron container](https://github.com/aws-neuron/deep-learning-containers?tab=readme-ov-file#pytorch-training-neuronx "https://github.com/aws-neuron/deep-learning-containers?tab=readme-ov-file#pytorch-training-neuronx")

## Launch the

training job with the SageMaker HyperPod CLI

We recommend using the SageMaker HyperPod command-line interface (CLI) tool to submit
your training job with your configurations. The following example submits a training
job for the `hf_llama3_8b_seq8k_trn1x4_pretrain` Trainium model.

- `your_neuron_container`: The [Neuron container](https://github.com/aws-neuron/deep-learning-containers?tab=readme-ov-file#pytorch-training-neuronx "https://github.com/aws-neuron/deep-learning-containers?tab=readme-ov-file#pytorch-training-neuronx").
- `your_model_config`: The model configuration from the
  environment setup section
- (Optional) You can provide the HuggingFace token if you need pre-trained
  weights from HuggingFace by setting the following key-value pair:

```
"recipes.model.hf_access_token": "`<your_hf_token>`"
```

```

hyperpod start-job --recipe training/llama/hf_llama3_8b_seq8k_trn1x4_pretrain \
--persistent-volume-claims fsx-claim:data \
--override-parameters \
'{
 "cluster": "k8s",
 "cluster_type": "k8s",
 "container": "`<your_neuron_contrainer>`",
 "recipes.run.name": "hf-llama3",
 "recipes.run.compile": 0,
 "recipes.model.model_config": "`<your_model_config>`",
 "instance_type": "trn1.32xlarge",
 "recipes.data.train_dir": "`<your_train_data_dir>`"
}'
```

After you've submitted a training job, you can use the following command to verify
if you submitted it successfully.

```
kubectl get pods
NAME                              READY   STATUS             RESTARTS        AGE
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

The `STATUS` will turn to `Completed` when you run
`kubectl get pods`.

## Launch the

training job with the recipes launcher

Alternatively, use SageMaker HyperPod recipes to submit your training job. To submit the
training job using a recipe, update `k8s.yaml` and
`config.yaml`. Run the bash script for the model to launch it.

- In `k8s.yaml`, update persistent_volume_claims to mount the
  Amazon FSx claim to the /data directory in the compute nodes

```
persistent_volume_claims:
  - claimName: fsx-claim
    mountPath: data
```

- Update
  launcher_scripts/llama/run_hf_llama3_8b_seq8k_trn1x4_pretrain.sh

      + `your_neuron_contrainer`: The container from the
       environment setup section
      + `your_model_config`: The model config from the
       environment setup section

  (Optional) You can provide the HuggingFace token if you need pre-trained
  weights from HuggingFace by setting the following key-value pair:

```
recipes.model.hf_access_token=`<your_hf_token>`
```

```
 #!/bin/bash
#Users should set up their cluster type in /recipes_collection/config.yaml
IMAGE="`<your_neuron_contrainer>`"
MODEL_CONFIG="`<your_model_config>`"
SAGEMAKER_TRAINING_LAUNCHER_DIR=${SAGEMAKER_TRAINING_LAUNCHER_DIR:-"$(pwd)"}
TRAIN_DIR="`<your_training_data_dir>`" # Location of training dataset
VAL_DIR="`<your_val_data_dir>`" # Location of talidation dataset

HYDRA_FULL_ERROR=1 python3 "${SAGEMAKER_TRAINING_LAUNCHER_DIR}/main.py" \
  recipes=training/llama/hf_llama3_8b_seq8k_trn1x4_pretrain \
  base_results_dir="${SAGEMAKER_TRAINING_LAUNCHER_DIR}/results" \
  recipes.run.name="hf-llama3-8b" \
  instance_type=trn1.32xlarge \
  recipes.model.model_config="$MODEL_CONFIG" \
  cluster=k8s \
  cluster_type=k8s \
  container="${IMAGE}" \
  recipes.data.train_dir=$TRAIN_DIR \
  recipes.data.val_dir=$VAL_DIR

```

- Launch the job

```
bash launcher_scripts/llama/run_hf_llama3_8b_seq8k_trn1x4_pretrain.sh
```

After you've submitted a training job, you can use the following command to verify
if you submitted it successfully.

```
kubectl get pods
NAME                             READY   STATUS             RESTARTS        AGE
hf-llama3-<your-alias>-worker-0   0/1     running         0               36s

```

If the `STATUS` is at `PENDING` or
`ContainerCreating`, run the following command to get more
details.

```
kubectl describe pod `name_of_pod`
```

After the job STATUS changes to Running, you can examine the log by using the
following command.

```
kubectl logs `name_of_pod`
```

The `STATUS` will turn to `Completed` when you run
`kubectl get pods`.

For more information about the k8s cluster configuration, see [Trainium Kubernetes cluster pre-training tutorial](sagemaker-hyperpod-trainium-kubernetes-cluster-pretrain-tutorial.md "sagemaker-hyperpod-trainium-kubernetes-cluster-pretrain-tutorial.md").
