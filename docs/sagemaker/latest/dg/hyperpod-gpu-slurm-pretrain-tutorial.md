# HyperPod Slurm cluster

pre-training tutorial (GPU)

The following tutorial sets up Slurm environment and starts a training job on a Llama
8 billion parameter model.

###### Prerequisites

Before you start setting up your environment to run the recipe, make sure you
have:

- Set up a HyperPod GPU Slurm cluster.
  - Your HyperPod Slurm cluster must have Nvidia Enroot and
    Pyxis enabled (these are enabled by default).

- A shared storage location. It can be an Amazon FSx file system or an NFS system
  that's accessible from the cluster nodes.
- Data in one of the following formats:
  - JSON
  - JSONGZ (Compressed JSON)
  - ARROW

- (Optional) You must get a HuggingFace token if you're using the model
  weights from HuggingFace for pre-training or fine-tuning. For more
  information about getting the token, see [User access
  tokens](https://huggingface.co/docs/hub/en/security-tokens "https://huggingface.co/docs/hub/en/security-tokens").

## HyperPod GPU Slurm

environment setup

To initiate a training job on a HyperPod GPU Slurm cluster, do the
following:

1. SSH into the head node of your Slurm cluster.
2. After you log in, set up the virtual environment. Make sure you're using
   Python 3.9 or greater.

```
#set up a virtual environment
python3 -m venv ${PWD}/venv
source venv/bin/activate

```

3. Clone the SageMaker HyperPod recipes and SageMaker HyperPod adapter repositories to a
   shared storage location.

```
git clone https://github.com/aws/sagemaker-hyperpod-training-adapter-for-nemo.git
git clone --recursive https://github.com/aws/sagemaker-hyperpod-recipes.git
cd sagemaker-hyperpod-recipes
pip3 install -r requirements.txt

```

4. Create a squash file using Enroot. To find the most recent release of the
   SMP container, see [Release notes for the SageMaker model parallelism
   library](model-parallel-release-notes.md "model-parallel-release-notes.md"). To gain a deeper
   understanding of how to use the Enroot file, see [Build AWS-optimized Nemo-Launcher image](https://github.com/aws-samples/awsome-distributed-training/tree/main/3.test_cases/2.nemo-launcher#2-build-aws-optimized-nemo-launcher-image "https://github.com/aws-samples/awsome-distributed-training/tree/main/3.test_cases/2.nemo-launcher#2-build-aws-optimized-nemo-launcher-image").

```
REGION="`<region>`"
IMAGE="658645717510.dkr.ecr.${`REGION`}.amazonaws.com/smdistributed-modelparallel:2.4.1-gpu-py311-cu121"
aws ecr get-login-password --region ${`REGION`} | docker login --username AWS --password-stdin 658645717510.dkr.ecr.${`REGION`}.amazonaws.com
enroot import -o $PWD/smdistributed-modelparallel.sqsh dockerd://${IMAGE}
mv $PWD/smdistributed-modelparallel.sqsh "/fsx/`<any-path-in-the-shared-filesystem>`"

```

5. To use the Enroot squash file to start training, use the following example
   to modify the `recipes_collection/config.yaml` file.

```
container: /fsx/path/to/your/smdistributed-modelparallel.sqsh

```

## Launch the training

job

After you install the dependencies, start a training job from the
`sagemaker-hyperpod-recipes/launcher_scripts` directory. You get the
dependencies by cloning the [SageMaker HyperPod recipes
repository](https://github.com/aws/sagemaker-hyperpod-recipes "https://github.com/aws/sagemaker-hyperpod-recipes"):

First, pick your training recipe from Github, the model name is specified as part
of the recipe. We use the
`launcher_scripts/llama/run_hf_llama3_8b_seq16k_gpu_p5x16_pretrain.sh`
script to launch a Llama 8b with sequence length 8192 pre-training recipe,
`llama/hf_llama3_8b_seq16k_gpu_p5x16_pretrain`, in the following
example.

- `IMAGE`: The container from the environment setup
  section.
- (Optional) You can provide the HuggingFace token if you need pre-trained
  weights from HuggingFace by setting the following key-value pair:

```
recipes.model.hf_access_token=`<your_hf_token>`
```

```
#!/bin/bash
IMAGE="${YOUR_IMAGE}"
SAGEMAKER_TRAINING_LAUNCHER_DIR="${SAGEMAKER_TRAINING_LAUNCHER_DIR:-${PWD}}"

TRAIN_DIR="${YOUR_TRAIN_DIR}" # Location of training dataset
VAL_DIR="${YOUR_VAL_DIR}" # Location of validation dataset

# experiment ouput directory
EXP_DIR="${YOUR_EXP_DIR}"

HYDRA_FULL_ERROR=1 python3 "${SAGEMAKER_TRAINING_LAUNCHER_DIR}/main.py" \
  recipes=training/llama/hf_llama3_8b_seq16k_gpu_p5x16_pretrain \
  base_results_dir="${SAGEMAKER_TRAINING_LAUNCHER_DIR}/results" \
  recipes.run.name="hf_llama3_8b" \
  recipes.exp_manager.exp_dir="$EXP_DIR" \
  recipes.model.data.train_dir="$TRAIN_DIR" \
  recipes.model.data.val_dir="$VAL_DIR" \
  container="${IMAGE}" \
  +cluster.container_mounts.0="/fsx:/fsx"

```

After you've configured all the required parameters in the launcher script, you
can run the script using the following command.

```
bash launcher_scripts/llama/run_hf_llama3_8b_seq16k_gpu_p5x16_pretrain.sh
```

For more information about the Slurm cluster configuration, see [Running a training job on HyperPod Slurm](cluster-specific-configurations-run-training-job-hyperpod-slurm.md "cluster-specific-configurations-run-training-job-hyperpod-slurm.md").
