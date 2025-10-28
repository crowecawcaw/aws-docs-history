# SageMaker

training jobs pre-training tutorial (GPU)

This tutorial guides you through the process of setting up and running a pre-training
job using SageMaker training jobs with GPU instances.

- Set up your environment
- Launch a training job using SageMaker HyperPod recipes
  Before you begin, make sure you have following prerequisites.

###### Prerequisites

Before you start setting up your environment, make sure you have:

- Amazon FSx file system or an Amazon S3 bucket where you can load the data and output
  the training artifacts.
- Requested a Service Quota for 1x ml.p4d.24xlarge and 1x ml.p5.48xlarge on
  Amazon SageMaker AI. To request a service quota increase, do the following:
  1.  On the AWS Service Quotas console, navigate to AWS
      services,
  2.  Choose **Amazon SageMaker AI**.
  3.  Choose one ml.p4d.24xlarge and one ml.p5.48xlarge instance.

- Create an AWS Identity and Access Management(IAM) role with the following managed policies to
  give SageMaker AI permissions to run the examples.
  - AmazonSageMakerFullAccess
  - AmazonEC2FullAccess

- Data in one of the following formats:
  - JSON
  - JSONGZ (Compressed JSON)
  - ARROW

- (Optional) You must get a HuggingFace token if you're using the model
  weights from HuggingFace for pre-training or fine-tuning. For more
  information about getting the token, see [User access
  tokens](https://huggingface.co/docs/hub/en/security-tokens "https://huggingface.co/docs/hub/en/security-tokens").

## GPU SageMaker training jobs environment setup

Before you run a SageMaker training job, configure your AWS credentials and preferred
region by running the `aws configure` command. As an alternative to the
configure command, you can provide your credentials through environment variables
such as `AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`, and
`AWS_SESSION_TOKEN.` For more information, see [SageMaker AI Python
SDK](https://github.com/aws/sagemaker-python-sdk "https://github.com/aws/sagemaker-python-sdk").

We strongly recommend using a SageMaker AI Jupyter notebook in SageMaker AI JupyterLab to launch
a SageMaker training job. For more information, see [SageMaker JupyterLab](studio-updated-jl.md "studio-updated-jl.md").

- (Optional) Set up the virtual environment and dependencies. If you are
  using a Jupyter notebook in Amazon SageMaker Studio, you can skip this step. Make
  sure you're using Python 3.9 or greater.

```
# set up a virtual environment
python3 -m venv ${PWD}/venv
source venv/bin/activate
# install dependencies after git clone.

git clone --recursive git@github.com:aws/sagemaker-hyperpod-recipes.git
cd sagemaker-hyperpod-recipes
pip3 install -r requirements.txt
# Set the aws region.

aws configure set `<your_region>`

```

- Install SageMaker AI Python SDK

```
pip3 install --upgrade sagemaker
```

- `Container`: The GPU container is set automatically by the SageMaker AI
  Python SDK. You can also provide your own container.

###### Note

If you're running a Llama 3.2 multi-modal training job, the
`transformers` version must be `4.45.2` or
greater.

Append `transformers==4.45.2` to `requirements.txt`
in `source_dir` only when you're using the SageMaker AI Python SDK. For
example, append it if you're using it in a notebook in SageMaker AI
JupyterLab.

If you are using HyperPod recipes to launch using cluster type
`sm_jobs`, this will be done automatically.

## Launch the training job using a Jupyter Notebook

You can use the following Python code to run a SageMaker training job with your recipe.
It leverages the PyTorch estimator from the [SageMaker AI Python SDK](https://sagemaker.readthedocs.io/en/stable/ "https://sagemaker.readthedocs.io/en/stable/") to
submit the recipe. The following example launches the llama3-8b recipe on the SageMaker AI
Training platform.

```
import os
import sagemaker,boto3
from sagemaker.debugger import TensorBoardOutputConfig

from sagemaker.pytorch import PyTorch

sagemaker_session = sagemaker.Session()
role = sagemaker.get_execution_role()

bucket = sagemaker_session.default_bucket()
output = os.path.join(f"s3://{bucket}", "output")
output_path = "`<s3-URI>`"

overrides = {
    "run": {
        "results_dir": "/opt/ml/model",
    },
    "exp_manager": {
        "exp_dir": "",
        "explicit_log_dir": "/opt/ml/output/tensorboard",
        "checkpoint_dir": "/opt/ml/checkpoints",
    },
    "model": {
        "data": {
            "train_dir": "/opt/ml/input/data/train",
            "val_dir": "/opt/ml/input/data/val",
        },
    },
}

tensorboard_output_config = TensorBoardOutputConfig(
    s3_output_path=os.path.join(output, 'tensorboard'),
    container_local_output_path=overrides["exp_manager"]["explicit_log_dir"]
)

estimator = PyTorch(
    output_path=output_path,
    base_job_name=f"llama-recipe",
    role=role,
    instance_type="ml.p5.48xlarge",
    training_recipe="training/llama/hf_llama3_8b_seq8k_gpu_p5x16_pretrain",
    recipe_overrides=recipe_overrides,
    sagemaker_session=sagemaker_session,
    tensorboard_output_config=tensorboard_output_config,
)

estimator.fit(inputs={"train": "s3 or fsx input", "val": "s3 or fsx input"}, wait=True)

```

The preceding code creates a PyTorch estimator object with the training recipe and
then fits the model using the `fit()` method. Use the training_recipe
parameter to specify the recipe you want to use for training.

###### Note

If you're running a Llama 3.2 multi-modal training job, the transformers
version must be 4.45.2 or greater.

Append `transformers==4.45.2` to `requirements.txt` in
`source_dir` only when you're using SageMaker AI Python SDK directly. For
example, you must append the version to the text file when you're using a Jupyter
notebook.

When you deploy the endpoint for a SageMaker training job, you must specify the image
URI that you're using. If don't provide the image URI, the estimator uses the
training image as the image for the deployment. The training images that
SageMaker HyperPod provides don't contain the dependencies required for inference and
deployment. The following is an example of how an inference image can be used for
deployment:

```
from sagemaker import image_uris
container=image_uris.retrieve(framework='pytorch',region='us-west-2',version='2.0',py_version='py310',image_scope='inference', instance_type='ml.p4d.24xlarge')
predictor = estimator.deploy(initial_instance_count=1,instance_type='ml.p4d.24xlarge',image_uri=container)

```

###### Note

Running the preceding code on Sagemaker notebook instance might need more than
the default 5GB of storage that SageMaker AI JupyterLab provides. If you run into space
not available issues, create a new notebook instance where you use a different
notebook instance and increase the storage of the notebook.

## Launch the training job with the recipes launcher

Update the `./recipes_collection/cluster/sm_jobs.yaml` file to look
like the following:

```
sm_jobs_config:
  output_path: `<s3_output_path>`
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
    enable_remote_debug: True
  recipe_overrides:
    exp_manager:
      explicit_log_dir: /opt/ml/output/tensorboard
    data:
      train_dir: /opt/ml/input/data/train
    model:
      model_config: /opt/ml/input/data/train/config.json
    compiler_cache_url: "`<compiler_cache_url>`"

```

Update `./recipes_collection/config.yaml` to specify
`sm_jobs` in the `cluster` and
`cluster_type`.

```
defaults:
  - _self_
  - cluster: sm_jobs  # set to `slurm`, `k8s` or `sm_jobs`, depending on the desired cluster
  - recipes: training/llama/hf_llama3_8b_seq8k_trn1x4_pretrain
cluster_type: sm_jobs  # bcm, bcp, k8s or sm_jobs. If bcm, k8s or sm_jobs, it must match - cluster above.

```

Launch the job with the following command

```
python3 main.py --config-path recipes_collection --config-name config
```

For more information about configuring SageMaker training jobs, see Run a training job
on SageMaker training jobs.
