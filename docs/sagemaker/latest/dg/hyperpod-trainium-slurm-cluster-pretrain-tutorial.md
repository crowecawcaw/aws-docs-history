# Trainium Slurm

cluster pre-training tutorial

The following tutorial sets up a Trainium environment on a Slurm cluster and starts a
training job on a Llama 8 billion parameter model.

###### Prerequisites

Before you start setting up your environment, make sure you have:

- Set up a SageMaker HyperPod Trainium Slurm cluster.
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

## Set up the Trainium environment on the Slurm Cluster

To initiate a training job on a Slurm cluster, do the following:

- SSH into the head node of your Slurm cluster.
- After you log in, set up the Neuron environment. For information about
  setting up Neuron, see [Neuron setup steps](https://awsdocs-neuron.readthedocs-hosted.com/en/latest/libraries/nxd-training/tutorials/hf_llama3_8B_SFT.html#setting-up-the-environment "https://awsdocs-neuron.readthedocs-hosted.com/en/latest/libraries/nxd-training/tutorials/hf_llama3_8B_SFT.html#setting-up-the-environment"). We recommend relying on the Deep learning
  AMI's that come pre-installed with Neuron's drivers, such as [Ubuntu 20 with DLAMI Pytorch](https://awsdocs-neuron.readthedocs-hosted.com/en/latest/general/setup/neuron-setup/pytorch/neuronx/ubuntu/torch-neuronx-ubuntu20-pytorch-dlami.html#setup-torch-neuronx-ubuntu20-dlami-pytorch "https://awsdocs-neuron.readthedocs-hosted.com/en/latest/general/setup/neuron-setup/pytorch/neuronx/ubuntu/torch-neuronx-ubuntu20-pytorch-dlami.html#setup-torch-neuronx-ubuntu20-dlami-pytorch").
- Clone the SageMaker HyperPod recipes repository to a shared storage location in
  the cluster. The shared storage location can be an Amazon FSx file system or NFS
  system that's accessible from the cluster nodes.

```
git clone --recursive https://github.com/aws/sagemaker-hyperpod-recipes.git
cd sagemaker-hyperpod-recipes
pip3 install -r requirements.txt

```

- Go through the following tutorial: [HuggingFace Llama3-8B Pretraining](https://awsdocs-neuron.readthedocs-hosted.com/en/latest/libraries/nxd-training/tutorials/hf_llama3_8B_pretraining.html# "https://awsdocs-neuron.readthedocs-hosted.com/en/latest/libraries/nxd-training/tutorials/hf_llama3_8B_pretraining.html#")
- Prepare a model configuration. The model configurations available in the
  Neuron repo. For the model configuration used the in this tutorial, see
  [llama3 8b model config](https://github.com/aws-neuron/neuronx-distributed/blob/main/examples/training/llama/tp_zero1_llama_hf_pretrain/8B_config_llama3/config.json "https://github.com/aws-neuron/neuronx-distributed/blob/main/examples/training/llama/tp_zero1_llama_hf_pretrain/8B_config_llama3/config.json")

## Launch the training job in Trainium

To launch a training job in Trainium, specify a cluster configuration and a Neuron
recipe. For example, to launch a llama3 8b pre-training job in Trainium, set the
launch script,
`launcher_scripts/llama/run_hf_llama3_8b_seq8k_trn1x4_pretrain.sh`,
to the following:

- `MODEL_CONFIG`: The model config from the environment setup
  section
- (Optional) You can provide the HuggingFace token if you need pre-trained
  weights from HuggingFace by setting the following key-value pair:

```
recipes.model.hf_access_token=`<your_hf_token>`
```

```
#!/bin/bash

#Users should set up their cluster type in /recipes_collection/config.yaml

SAGEMAKER_TRAINING_LAUNCHER_DIR=${SAGEMAKER_TRAINING_LAUNCHER_DIR:-"$(pwd)"}

COMPILE=0
TRAIN_DIR="${TRAIN_DIR}" # Location of training dataset
MODEL_CONFIG="${MODEL_CONFIG}" # Location of config.json for the model

HYDRA_FULL_ERROR=1 python3 "${SAGEMAKER_TRAINING_LAUNCHER_DIR}/main.py" \
    base_results_dir="${SAGEMAKER_TRAINING_LAUNCHER_DIR}/results" \
    instance_type="trn1.32xlarge" \
    recipes.run.compile="$COMPILE" \
    recipes.run.name="hf-llama3-8b" \
    recipes.trainer.num_nodes=4 \
    recipes=training/llama/hf_llama3_8b_seq8k_trn1x4_pretrain \
    recipes.data.train_dir="$TRAIN_DIR" \
    recipes.model.model_config="$MODEL_CONFIG"

```

To launch the training job, run the following command:

```
bash launcher_scripts/llama/run_hf_llama3_8b_seq8k_trn1x4_pretrain.sh
```

For more information about the Slurm cluster configuration, see [Running a training job on HyperPod Slurm](cluster-specific-configurations-run-training-job-hyperpod-slurm.md "cluster-specific-configurations-run-training-job-hyperpod-slurm.md").
