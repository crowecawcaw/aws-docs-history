# Amazon SageMaker HyperPod Essential Commands

Guide

Amazon SageMaker HyperPod provides extensive command-line functionality for managing
training workflows. This guide covers essential commands for common operations, from
connecting to your cluster to monitoring job progress.

###### Prerequisites

Before using these commands, ensure you have completed the following setup:

- SageMaker HyperPod cluster with RIG created (typically in us-east-1)
- Output Amazon S3 bucket created for training artifacts
- IAM roles configured with appropriate permissions
- Training data uploaded in correct JSONL format
- FSx for Lustre sync completed (verify in cluster logs on first job)

###### Topics

- [Installing Recipe CLI](#nova-hp-essential-commands-guide-install "#nova-hp-essential-commands-guide-install")
- [Connecting to your
  cluster](#nova-hp-essential-commands-guide-connect "#nova-hp-essential-commands-guide-connect")
- [Starting a training job](#nova-hp-essential-commands-guide-start-job "#nova-hp-essential-commands-guide-start-job")
- [Checking job status](#nova-hp-essential-commands-guide-status "#nova-hp-essential-commands-guide-status")
- [Monitoring job logs](#nova-hp-essential-commands-guide-logs "#nova-hp-essential-commands-guide-logs")
- [Listing active jobs](#nova-hp-essential-commands-guide-list-jobs "#nova-hp-essential-commands-guide-list-jobs")
- [Canceling a job](#nova-hp-essential-commands-guide-cancel-job "#nova-hp-essential-commands-guide-cancel-job")
- [Running an evaluation
  job](#nova-hp-essential-commands-guide-evaluation "#nova-hp-essential-commands-guide-evaluation")
- [Common issues](#nova-hp-essential-commands-guide-troubleshooting "#nova-hp-essential-commands-guide-troubleshooting")

## Installing Recipe CLI

Navigate to the root of your recipe repository before running the installation
command.

###### Use the Hyperpodrecipes repository if using Non Forge customization techniques,

for Forge based customization refer to the forge specific recipe repository.

Run the following commands to install the SageMaker HyperPod CLI:

###### Note

Make sure you aren’t in an active conda / anaconda / miniconda environment or another virtual environment

If you are, please exit the environment using:

- `conda deactivate` for conda / anaconda / miniconda environments
- `deactivate` for python virtual environments

If you are using a Non Forge customization technique, download the
sagemaker-hyperpod-recipes as shown below:

```

git clone -b release_v2 https://github.com/aws/sagemaker-hyperpod-cli.git
cd sagemaker-hyperpod-cli
pip install -e .
cd ..
root_dir=$(pwd)
export PYTHONPATH=${root_dir}/sagemaker-hyperpod-cli/src/hyperpod_cli/sagemaker_hyperpod_recipes/launcher/nemo/nemo_framework_launcher/launcher_scripts:$PYTHONPATH
curl -fsSL -o get_helm.sh https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3
chmod 700 get_helm.sh
./get_helm.sh
rm -f ./get_helm.sh


```

If you are a **Forge Subscriber,** you should be
downloading the recipes using below mentioned process.

```
mkdir NovaForgeHyperpodCLI
cd NovaForgeHyperpodCLI
aws s3 cp s3://nova-forge-c7363-206080352451-us-east-1/v1/ ./ --recursive
pip install -e .

curl -fsSL -o get_helm.sh https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3
chmod 700 get_helm.sh
./get_helm.sh
rm -f ./get_helm.sh
```

###### Tip

To use a [new virtual
environment](https://docs.python.org/3/library/venv.html "https://docs.python.org/3/library/venv.html") before running `pip install -e .`, run:

- `python -m venv nova_forge`
- `source nova_forge/bin/activate`
- Your command line will now display (nova_forge) at the beginning of your prompt
- This ensures there are no competing dependencies when using the CLI

**Purpose**: Why do we do `pip install -e .`
?

This command installs the SageMaker HyperPod CLI in editable mode, allowing you to use
updated recipes without reinstalling each time. It also enables you to add new recipes that
the CLI can automatically pick up.

## Connecting to your

cluster

Connect the SageMaker HyperPod CLI to your cluster before running any jobs:

```
export AWS_REGION=us-east-1 &&  SageMaker HyperPod  connect-cluster --cluster-name <your-cluster-name> --region us-east-1
```

###### Important

This command creates a context file (`/tmp/hyperpod_context.json`) that
subsequent commands require. If you see an error about this file not found, re-run the
connect command.

**Pro tip**: You can further configure your cluster to
always use the `kubeflow` namespace by adding the `--namespace
 kubeflow` argument to your command as follows:

```
export AWS_REGION=us-east-1 && \
hyperpod connect-cluster \
--cluster-name <your-cluster-name> \
--region us-east-1 \
--namespace kubeflow
```

This saves you the effort of adding the `-n kubeflow` in every command when
interacting with your jobs.

## Starting a training job

###### Note

If running PPO/RFT jobs, ensure you add label selector settings to
`src/hyperpod_cli/sagemaker_hyperpod_recipes/recipes_collection/cluster/k8s.yaml`
so that all pods are schedule on the same node.

```
label_selector:
  required:
    sagemaker.amazonaws.com/instance-group-name:
      - <rig_group>
```

Launch a training job using a recipe with optional parameter overrides:

```
hyperpod start-job -n kubeflow \
--recipe fine-tuning/nova/nova_1_0/nova_micro/SFT/nova_micro_1_0_p5_p4d_gpu_lora_sft \
--override-parameters '{
"instance_type": "ml.p5.48xlarge",
    "container": "708977205387.dkr.ecr.us-east-1.amazonaws.com/nova-fine-tune-repo:SM-HP-SFT-latest"
  }'
```

**Expected output**:

```
Final command: python3 <path_to_your_installation>/NovaForgeHyperpodCLI/src/hyperpod_cli/sagemaker_hyperpod_recipes/main.py recipes=fine-tuning/nova/nova_micro_p5_gpu_sft cluster_type=k8s cluster=k8s base_results_dir=/local/home/<username>/results cluster.pullPolicy="IfNotPresent" cluster.restartPolicy="OnFailure" cluster.namespace="kubeflow" container="708977205387.dkr.ecr.us-east-1.amazonaws.com/nova-fine-tune-repo:HP-SFT-DATAMIX-latest"

Prepared output directory at /local/home/<username>/results/<job-name>/k8s_templates
Found credentials in shared credentials file: ~/.aws/credentials
Helm script created at /local/home/<username>/results/<job-name>/<job-name>_launch.sh
Running Helm script: /local/home/<username>/results/<job-name>/<job-name>_launch.sh

NAME: <job-name>
LAST DEPLOYED: Mon Sep 15 20:56:50 2025
NAMESPACE: kubeflow
STATUS: deployed
REVISION: 1
TEST SUITE: None
Launcher successfully generated: <path_to_your_installation>/NovaForgeHyperpodCLI/src/hyperpod_cli/sagemaker_hyperpod_recipes/launcher/nova/k8s_templates/SFT

{
 "Console URL": "https://us-east-1.console.aws.amazon.com/sagemaker/home?region=us-east-1#/cluster-management/<your-cluster-name>"
}
```

## Checking job status

Monitor your running jobs using kubectl:

```
kubectl get pods -o wide -w -n kubeflow | (head -n1 ; grep <your-job-name>)
```

###### Understanding pod statuses

The following table explains common pod statuses:

| Status                              | Description                                                                                     |
| ----------------------------------- | ----------------------------------------------------------------------------------------------- |
| `Pending`                           | Pod accepted but not yet scheduled onto a node, or waiting for container<br>images to be pulled |
| `Running`                           | Pod bound to a node with at least one container running or<br>starting                          |
| `Succeeded`                         | All containers completed successfully and won't restart                                         |
| `Failed`                            | All containers terminated with at least one ending in failure                                   |
| `Unknown`                           | Pod state cannot be determined (usually due to node communication<br>issues)                    |
| `CrashLoopBackOff`                  | Container repeatedly failing; Kubernetes backing off from restart<br>attempts                   |
| `ImagePullBackOff` / `ErrImagePull` | Unable to pull container image from registry                                                    |
| `OOMKilled`                         | Container terminated for exceeding memory limits                                                |
| `Completed`                         | Job or Pod finished successfully (batch job completion)                                         |

###### Tip

Use the `-w` flag to watch pod status updates in real-time. Press
`Ctrl+C` to stop watching.

## Monitoring job logs

You can view your logs one of three ways:

###### Using CloudWatch

Your logs are available in your AWS account that contains the Hyperpodcluster under
CloudWatch. To view them in your browser, navigate to the CloudWatch homepage in your account and
search for your cluster name. For example, if your cluster were called
`my-hyperpod-rig` the log group would have the prefix:

- **Log group**:
  `/aws/sagemaker/Clusters/my-hyperpod-rig/{UUID}`
- Once you're in the log group, you can find your specific log using the node instance
  ID such as - `hyperpod-i-00b3d8a1bf25714e4`.
  - `i-00b3d8a1bf25714e4` here represents the Hyperpodfriendly machine
    name where your training job is running. Recall how in the previous command
    `kubectl get pods -o wide -w -n kubeflow | (head -n1 ; grep
my-cpt-run)` output we captured a column called **NODE**.
  - The "master" node run was in this case running on
    hyperpod-`i-00b3d8a1bf25714e4` and thus we'll use that string to select
    the log group to view. Select the one that says
    `SagemakerHyperPodTrainingJob/rig-group/[NODE]`

###### Using CloudWatch Insights

If you have your job name handy and don't wish to go through all the steps above, you
can simply query all logs under
`/aws/sagemaker/Clusters/my-hyperpod-rig/{UUID}` to find the individual
log.

CPT:

```
fields @timestamp, @message, @logStream, @log
| filter @message like /(?i)Starting CPT Job/
| sort @timestamp desc
| limit 100
```

For job completion replace `Starting CPT Job` with `CPT Job
 completed`

Then you can click through the results and pick the one that says "Epoch 0" since that
will be your master node.

###### Using the AWSAWS CLI

You may choose to tail your logs using the AWS CLI. Before doing so, please check
your aws cli version using `aws --version`. It is also recommended to use this
utility script that helps in live log tracking in your terminal

**for V1**:

```
aws logs get-log-events \
--log-group-name /aws/sagemaker/YourLogGroupName \
--log-stream-name YourLogStream \
--start-from-head | jq -r '.events[].message'
```

**for V2**:

```
aws logs tail /aws/sagemaker/YourLogGroupName \
 --log-stream-name YourLogStream \
--since 10m \
--follow
```

## Listing active jobs

View all jobs running in your cluster:

```
hyperpod list-jobs -n kubeflow
```

**Example output**:

```
{
  "jobs": [
    {
      "Name": "test-run-nhgza",
      "Namespace": "kubeflow",
      "CreationTime": "2025-10-29T16:50:57Z",
      "State": "Running"
    }
  ]
}
```

## Canceling a job

Stop a running job at any time:

```
hyperpod cancel-job --job-name <job-name> -n kubeflow
```

###### Finding your job name

**Option 1: From your recipe**

The job name is specified in your recipe's `run` block:

```
run:
  name: "my-test-run"                        # This is your job name
  model_type: "amazon.nova-micro-v1:0:128k"
  ...
```

**Option 2: From list-jobs command**

Use `hyperpod list-jobs -n kubeflow` and copy the `Name` field
from the output.

## Running an evaluation

job

Evaluate a trained model or base model using an evaluation recipe.

###### Prerequisites

Before running evaluation jobs, ensure you have:

- Checkpoint Amazon S3 URI from your training job's `manifest.json` file (for
  trained models)
- Evaluation dataset uploaded to Amazon S3 in the correct format
- Output Amazon S3 path for evaluation results

###### Command

Run the following command to start an evaluation job:

```
hyperpod start-job -n kubeflow \
  --recipe evaluation/nova/nova_2_0/nova_lite/nova_lite_2_0_p5_48xl_gpu_bring_your_own_dataset_eval \
  --override-parameters '{
    "instance_type": "p5.48xlarge",
    "container": "708977205387.dkr.ecr.us-east-1.amazonaws.com/nova-evaluation-repo:SM-HP-Eval-latest",
    "recipes.run.name": "<your-eval-job-name>",
    "recipes.run.model_name_or_path": "<checkpoint-s3-uri>",
    "recipes.run.output_s3_path": "s3://<your-bucket>/eval-results/",
    "recipes.run.data_s3_path": "s3://<your-bucket>/eval-data.jsonl"
  }'
```

**Parameter descriptions**:

- `recipes.run.name`: Unique name for your evaluation job
- `recipes.run.model_name_or_path`: Amazon S3 URI from
  `manifest.json` or base model path (e.g.,
  `nova-micro/prod`)
- `recipes.run.output_s3_path`: Amazon S3 location for evaluation results
- `recipes.run.data_s3_path`: Amazon S3 location of your evaluation
  dataset

**Tips**:

- **Model-specific recipes**: Each model size (micro,
  lite, pro) has its own evaluation recipe
- **Base model evaluation**: Use base model paths (e.g.,
  `nova-micro/prod`) instead of checkpoint URIs to evaluate base
  models

###### Evaluation data format

**Input format (JSONL)**:

```
{
  "metadata": "{key:4, category:'apple'}",
  "system": "arithmetic-patterns, please answer the following with no other words: ",
  "query": "What is the next number in this series? 1, 2, 4, 8, 16, ?",
  "response": "32"
}
```

**Output format**:

```
{
  "prompt": "[{'role': 'system', 'content': 'arithmetic-patterns, please answer the following with no other words: '}, {'role': 'user', 'content': 'What is the next number in this series? 1, 2, 4, 8, 16, ?'}]",
  "inference": "['32']",
  "gold": "32",
  "metadata": "{key:4, category:'apple'}"
}
```

**Field descriptions**:

- `prompt`: Formatted input sent to the model
- `inference`: Model's generated response
- `gold`: Expected correct answer from input dataset
- `metadata`: Optional metadata passed through from input

## Common issues

- `ModuleNotFoundError: No module named 'nemo_launcher'`, you might've to
  add `nemo_launcher` to your python path based on where
  `hyperpod_cli` is installed. Sample command:

```
export PYTHONPATH=<path_to_hyperpod_cli>/sagemaker-hyperpod-cli/src/hyperpod_cli/sagemaker_hyperpod_recipes/launcher/nemo/nemo_framework_launcher/launcher_scripts:$PYTHONPATH
```

- `FileNotFoundError: [Errno 2] No such file or directory:
'/tmp/hyperpod_current_context.json'` indicates you missed running the hyperpod
  connect cluster command.
- If you don't see your job scheduled, double check if the output of your
  SageMaker HyperPod CLI has this section with job names and other metadata. If not,
  re-install helm chart by running:

```
curl -fsSL -o get_helm.sh https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3
chmod 700 get_helm.sh
./get_helm.sh
rm -f ./get_helm.sh
```
