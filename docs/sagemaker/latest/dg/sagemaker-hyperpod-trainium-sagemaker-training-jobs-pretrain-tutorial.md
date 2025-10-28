# Trainium SageMaker training jobs pre-training tutorial

This tutorial guides you through the process of setting up and running a pre-training
job using SageMaker training jobs with AWS Trainium instances.

- Set up your environment
- Launch a training job
  Before you begin, make sure you have the following prerequisites.

###### Prerequisites

Before you start setting up your environment, make sure you have:

- Amazon FSx file system or S3 bucket where you can load the data and output the
  training artifacts.
- Request a Service Quota for the `ml.trn1.32xlarge` instance on
  Amazon SageMaker AI. To request a service quota increase, do the following:

###### To request a service quota increase for ml.trn1.32xlarge

instance

    1. Navigate to the AWS Service Quotas console.
    2. Choose AWS services.
    3. Select JupyterLab.
    4. Specify one instance for `ml.trn1.32xlarge`.

- Create an AWS Identity and Access Management (IAM) role with the
  `AmazonSageMakerFullAccess` and
  `AmazonEC2FullAccess` managed policies. These policies
  provide Amazon SageMaker AI with permissions to run the examples.
- Data in one of the following formats:
  - JSON
  - JSONGZ (Compressed JSON)
  - ARROW

- (Optional) If you need the pre-trained weights from HuggingFace or if
  you're training a Llama 3.2 model, you must get the HuggingFace token before
  you start training. For more information about getting the token, see [User access
  tokens](https://huggingface.co/docs/hub/en/security-tokens "https://huggingface.co/docs/hub/en/security-tokens").

## Set up your environment for Trainium SageMaker training jobs

Before you run a SageMaker training job, use the `aws configure` command to
configure your AWS credentials and preferred region . As an alternative, you can
also provide your credentials through environment variables such as the
`AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`, and
`AWS_SESSION_TOKEN`. For more information, see [SageMaker AI Python
SDK](https://github.com/aws/sagemaker-python-sdk "https://github.com/aws/sagemaker-python-sdk").

We strongly recommend using a SageMaker AI Jupyter notebook in SageMaker AI JupyterLab to launch
a SageMaker training job. For more information, see [SageMaker JupyterLab](studio-updated-jl.md "studio-updated-jl.md").

- (Optional) If you are using Jupyter notebook in Amazon SageMaker Studio, you can
  skip running the following command. Make sure to use a version >= python
  3.9

```
# set up a virtual environment
python3 -m venv ${PWD}/venv
source venv/bin/activate
# install dependencies after git clone.

git clone --recursive git@github.com:aws/sagemaker-hyperpod-recipes.git
cd sagemaker-hyperpod-recipes
pip3 install -r requirements.txt

```

- Install SageMaker AI Python SDK

```
pip3 install --upgrade sagemaker
```

- - If you are running a llama 3.2 multi-modal training job, the
    `transformers` version must be `4.45.2` or
    greater.
    - Append `transformers==4.45.2` to
      `requirements.txt` in source_dir only when
      you're using the SageMaker AI Python SDK.
    - If you are using HyperPod recipes to launch using
      `sm_jobs` as the cluster type, you don't have
      to specify the transformers version.

  - `Container`: The Neuron container is set automatically
    by SageMaker AI Python SDK.

## Launch the training job with a Jupyter Notebook

You can use the following Python code to run a SageMaker training job using your
recipe. It leverages the PyTorch estimator from the [SageMaker AI Python SDK](https://sagemaker.readthedocs.io/en/stable/ "https://sagemaker.readthedocs.io/en/stable/") to
submit the recipe. The following example launches the llama3-8b recipe as a SageMaker AI
Training Job.

- `compiler_cache_url`: Cache to be used to save the compiled
  artifacts, such as an Amazon S3 artifact.

```
import os
import sagemaker,boto3
from sagemaker.debugger import TensorBoardOutputConfig

from sagemaker.pytorch import PyTorch

sagemaker_session = sagemaker.Session()
role = sagemaker.get_execution_role()

recipe_overrides = {
    "run": {
        "results_dir": "/opt/ml/model",
    },
    "exp_manager": {
        "explicit_log_dir": "/opt/ml/output/tensorboard",
    },
    "data": {
        "train_dir": "/opt/ml/input/data/train",
    },
    "model": {
        "model_config": "/opt/ml/input/data/train/config.json",
    },
    "compiler_cache_url": "`<compiler_cache_url>`"
}

tensorboard_output_config = TensorBoardOutputConfig(
    s3_output_path=os.path.join(output, 'tensorboard'),
    container_local_output_path=overrides["exp_manager"]["explicit_log_dir"]
)

estimator = PyTorch(
    output_path=output_path,
    base_job_name=f"llama-trn",
    role=role,
    instance_type="ml.trn1.32xlarge",
    sagemaker_session=sagemaker_session,
    training_recipe="training/llama/hf_llama3_70b_seq8k_trn1x16_pretrain",
    recipe_overrides=recipe_overrides,
)

estimator.fit(inputs={"train": "your-inputs"}, wait=True)

```

The preceding code creates a PyTorch estimator object with the training recipe and
then fits the model using the `fit()` method. Use the
`training_recipe` parameter to specify the recipe you want to use for
training.

## Launch the training job with the recipes launcher

- Update `./recipes_collection/cluster/sm_jobs.yaml`
  - compiler_cache_url: The URL used to save the artifacts. It can be
    an Amazon S3 URL.

```
sm_jobs_config:
  output_path: `<s3_output_path>`
  wait: True
  tensorboard_config:
    output_path: `<s3_output_path>`
    container_logs_path: /opt/ml/output/tensorboard  # Path to logs on the container
  wait: True  # Whether to wait for training job to finish
  inputs:  # Inputs to call fit with. Set either s3 or file_system, not both.
    s3:  # Dictionary of channel names and s3 URIs. For GPUs, use channels for train and validation.
      train: `<s3_train_data_path>`
      val: null
  additional_estimator_kwargs:  # All other additional args to pass to estimator. Must be int, float or string.
    max_run: 180000
    image_uri: `<your_image_uri>`
    enable_remote_debug: True
    py_version: py39
  recipe_overrides:
    model:
      exp_manager:
        exp_dir: `<exp_dir>`
      data:
        train_dir: /opt/ml/input/data/train
        val_dir: /opt/ml/input/data/val

```

- Update `./recipes_collection/config.yaml`

```
defaults:
  - _self_
  - cluster: sm_jobs
  - recipes: training/llama/hf_llama3_8b_seq8k_trn1x4_pretrain
cluster_type: sm_jobs # bcm, bcp, k8s or sm_jobs. If bcm, k8s or sm_jobs, it must match - cluster above.

instance_type: ml.trn1.32xlarge
base_results_dir: ~/sm_job/hf_llama3_8B # Location to store the results, checkpoints and logs.
```

- Launch the job with `main.py`

```
python3 main.py --config-path recipes_collection --config-name config
```

For more information about configuring SageMaker training jobs, see [SageMaker
training jobs pre-training tutorial (GPU)](sagemaker-hyperpod-gpu-sagemaker-training-jobs-pretrain-tutorial.md "sagemaker-hyperpod-gpu-sagemaker-training-jobs-pretrain-tutorial.md").
