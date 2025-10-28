# Setting up multiple controller

nodes for a SageMaker HyperPod Slurm cluster

This topic explains how to configure multiple controller (head) nodes in a
SageMaker HyperPod Slurm cluster using lifecycle scripts. Before you start, review the
prerequisites listed in [Prerequisites for using
SageMaker HyperPod](sagemaker-hyperpod-prerequisites.md "sagemaker-hyperpod-prerequisites.md") and
familiarize yourself with the lifecycle scripts in [Customizing SageMaker HyperPod
clusters using lifecycle scripts](sagemaker-hyperpod-lifecycle-best-practices-slurm.md "sagemaker-hyperpod-lifecycle-best-practices-slurm.md"). The instructions in this
topic use AWS CLI commands in Amazon Linux environment. Note that the environment variables used
in these commands are available in the current session unless explicitly
preserved.

###### To set up multiple controller (head) nodes for a SageMaker HyperPod Slurm

cluster, follow these steps.

- [Provisioning resources using
  AWS CloudFormation stacks](sagemaker-hyperpod-multihead-slurm-cfn.md "sagemaker-hyperpod-multihead-slurm-cfn.md")
- [Creating and attaching an
  IAM policy](sagemaker-hyperpod-multihead-slurm-iam.md "sagemaker-hyperpod-multihead-slurm-iam.md")
- [Preparing and uploading
  lifecycle scripts](sagemaker-hyperpod-multihead-slurm-scripts.md "sagemaker-hyperpod-multihead-slurm-scripts.md")
- [Creating a SageMaker HyperPod
  cluster](sagemaker-hyperpod-multihead-slurm-create.md "sagemaker-hyperpod-multihead-slurm-create.md")
- [Considering important
  notes](sagemaker-hyperpod-multihead-slurm-notes.md "sagemaker-hyperpod-multihead-slurm-notes.md")
- [Reviewing environment
  variables reference](sagemaker-hyperpod-multihead-slurm-variables-reference.md "sagemaker-hyperpod-multihead-slurm-variables-reference.md")
