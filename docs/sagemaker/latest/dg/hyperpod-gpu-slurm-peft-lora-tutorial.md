# HyperPod Slurm cluster

PEFT-Lora tutorial (GPU)

The following tutorial sets up Slurm environment and starts a parameter-efficient
fine-tuning (PEFT) job on a Llama 8 billion parameter model.

###### Prerequisites

Before you start setting up your environment, make sure you have:

- Set up HyperPod GPU Slurm cluster
  - Your HyperPod Slurm cluster must have Nvidia Enroot and
    Pyxis enabled (these are enabled by default).

- A shared storage location. It can be an Amazon FSx file system or NFS system
  that's accessible from the cluster nodes.
- Data in one of the following formats:
  - JSON
  - JSONGZ (Compressed JSON)
  - ARROW

- (Optional) If you need the pre-trained weights from HuggingFace or if
  you're training a Llama 3.2 model, you must get the HuggingFace token before
  you start training. For more information about getting the token, see [User access
  tokens](https://huggingface.co/docs/hub/en/security-tokens "https://huggingface.co/docs/hub/en/security-tokens").

## Set up the HyperPod GPU Slurm environment

To initiate a training job on a Slurm cluster, do the following:

- SSH into the head node of your Slurm cluster.
- After you log in, set up the virtual environment. Make sure you're using
  Python 3.9 or greater.

```
#set up a virtual environment
python3 -m venv ${PWD}/venv
source venv/bin/activate

```

- Clone the SageMaker HyperPod recipes and SageMaker HyperPod adapter repositories to a
  shared storage location. The shared storage location can be an Amazon FSx file
  system or NFS system that's accessible from the cluster nodes.

```
git clone https://github.com/aws/sagemaker-hyperpod-training-adapter-for-nemo.git
git clone --recursive https://github.com/aws/sagemaker-hyperpod-recipes.git
cd sagemaker-hyperpod-recipes
pip3 install -r requirements.txt

```

- Create a squash file using Enroot. To find the most recent release of the
  SMP container, see [Release notes for the SageMaker model parallelism
  library](model-parallel-release-notes.md "model-parallel-release-notes.md"). For more information
  about using the Enroot file, see [Build AWS-optimized Nemo-Launcher image](https://github.com/aws-samples/awsome-distributed-training/tree/main/3.test_cases/2.nemo-launcher#2-build-aws-optimized-nemo-launcher-image "https://github.com/aws-samples/awsome-distributed-training/tree/main/3.test_cases/2.nemo-launcher#2-build-aws-optimized-nemo-launcher-image").

```
REGION="`<region>`"
IMAGE="658645717510.dkr.ecr.${REGION}.amazonaws.com/smdistributed-modelparallel:2.4.1-gpu-py311-cu121"
aws ecr get-login-password --region ${REGION} | docker login --username AWS --password-stdin 658645717510.dkr.ecr.${REGION}.amazonaws.com
enroot import -o $PWD/smdistributed-modelparallel.sqsh dockerd://${IMAGE}
mv $PWD/smdistributed-modelparallel.sqsh "/fsx/`<any-path-in-the-shared-filesystem>`"

```

- To use the Enroot squash file to start training, use the following example
  to modify the `recipes_collection/config.yaml` file.

```
container: /fsx/path/to/your/smdistributed-modelparallel.sqsh

```

## Launch the

training job

To launch a PEFT job for the Llama 8 billion parameter model with a sequence
length of 8192 on a single Slurm compute node, set the launch script,
`launcher_scripts/llama/run_hf_llama3_8b_seq8k_gpu_lora.sh`, to the
following:

- `IMAGE`: The container from the environment setup
  section.
- `HF_MODEL_NAME_OR_PATH`: Define the name or the path of the
  pre-trained weights in the hf_model_name_or_path parameter of the
  recipe.
- (Optional) You can provide the HuggingFace token if you need pre-trained
  weights from HuggingFace by setting the following key-value pair:

```
recipes.model.hf_access_token=${`HF_ACCESS_TOKEN`}
```

```
#!/bin/bash
IMAGE="${YOUR_IMAGE}"
SAGEMAKER_TRAINING_LAUNCHER_DIR="${SAGEMAKER_TRAINING_LAUNCHER_DIR:-${PWD}}"

TRAIN_DIR="${YOUR_TRAIN_DIR}" # Location of training dataset
VAL_DIR="${YOUR_VAL_DIR}" # Location of validation dataset

# experiment output directory
EXP_DIR="${`YOUR_EXP_DIR`}"
HF_ACCESS_TOKEN="${`YOUR_HF_TOKEN`}"
HF_MODEL_NAME_OR_PATH="${`YOUR_HF_MODEL_NAME_OR_PATH`}"

# Add hf_model_name_or_path and turn off synthetic_data
HYDRA_FULL_ERROR=1 python3 ${SAGEMAKER_TRAINING_LAUNCHER_DIR}/main.py \
    recipes=fine-tuning/llama/hf_llama3_8b_seq8k_gpu_lora \
    base_results_dir=${SAGEMAKER_TRAINING_LAUNCHER_DIR}/results \
    recipes.run.name="hf_llama3_lora" \
    recipes.exp_manager.exp_dir="$EXP_DIR" \
    recipes.model.data.train_dir="$TRAIN_DIR" \
    recipes.model.data.val_dir="$VAL_DIR" \
    recipes.model.hf_model_name_or_path="$HF_MODEL_NAME_OR_PATH" \
    container="${IMAGE}" \
    +cluster.container_mounts.0="/fsx:/fsx" \
    recipes.model.hf_access_token="${HF_ACCESS_TOKEN}"

```

After you've configured all the required parameters in the preceding script, you
can initiate the training job by running it.

```
bash launcher_scripts/llama/run_hf_llama3_8b_seq8k_gpu_lora.sh
```

For more information about the Slurm cluster configuration, see [Running a training job on HyperPod Slurm](cluster-specific-configurations-run-training-job-hyperpod-slurm.md "cluster-specific-configurations-run-training-job-hyperpod-slurm.md").
