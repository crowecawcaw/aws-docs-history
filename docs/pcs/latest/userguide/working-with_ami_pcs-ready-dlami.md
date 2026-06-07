# Using PCS-ready DLAMI with AWS PCS

AWS PCS-ready DLAMI Base GPU AMI (Ubuntu 24.04) is an AWS-maintained Amazon Machine Image
for running AI/ML and HPC workloads on AWS PCS. It provides a production-ready foundation
so you can deploy clusters in minutes instead of building and validating custom AMIs.

## What's included

PCS-ready DLAMI is built on the
[Deep Learning
Base GPU AMI (Ubuntu 24.04)](../../../dlami/latest/devguide/overview-base.md "../../../dlami/latest/devguide/overview-base.md") and adds the following AWS PCS components:

- **PCS Agent** – The AWS PCS cluster management agent
- **Slurm for AWS PCS** – Multiple supported Slurm versions are
  pre-installed. The correct version is activated automatically during instance launch based on
  your cluster's configuration.
- **EFS utilities** – For mounting Amazon EFS file systems

The source DLAMI provides the operating system (Ubuntu 24.04), NVIDIA GPU drivers, CUDA toolkit,
EFA drivers, Lustre client, and other foundational infrastructure. For details on these components,
see the [Deep
Learning AMI release notes](../../../dlami/latest/devguide/appendix-ami-release-notes.md "../../../dlami/latest/devguide/appendix-ami-release-notes.md").

PCS-ready DLAMI is available for both x86_64 and arm64 architectures.

###### Note

PCS-ready DLAMI does not include application software such as AI/ML frameworks
(PyTorch, TensorFlow, JAX), compilers, or math libraries. You can add your application
layer on shared file systems or by building a custom AMI on top of PCS-ready DLAMI.

Each AMI's _Description_ field summarizes its content, including
the source DLAMI it is based on, the PCS Agent version, supported Slurm versions, and EFS
utilities version. You can view this field in the Amazon EC2 console or by using the
`describe-images` API. The following is an example of a Description field
value:

```
PCS-Ready DLAMI based on Deep Learning Base OSS Nvidia Driver GPU AMI (Ubuntu 24.04) 20260522. PCS Agent: 1.4.0-1. Slurm: 24.11.7-1, 25.05.7-1, 25.11.2-1. EFS Utils: 2.4.2
```

## Find the current PCS-ready DLAMI

AWS Management Console

###### To find PCS-ready DLAMI in the console

1. Open the AWS PCS console and navigate to create or edit a compute node group.
2. In the AMI selection section, select **PCS-ready AMIs**.
3. A dropdown appears showing available PCS-ready DLAMIs filtered by your selected
   instance type architecture.
4. Choose **AWS PCS-ready DLAMI Base AMI (Ubuntu 24.04)**. The dropdown
   displays the AMI ID and full AMI name below for reference.

AWS CLI
You can retrieve the latest PCS-ready DLAMI AMI ID using Amazon EC2 Systems Manager Parameter Store.
Replace `region-code` with your AWS Region.

- x86_64

```
aws ssm get-parameter --region `region-code` \
  --name /aws/service/pcs/ami/dlami-base-ubuntu2404/x86_64/latest/ami-id \
  --query "Parameter.Value" --output text
```

- arm64

```
aws ssm get-parameter --region `region-code` \
  --name /aws/service/pcs/ami/dlami-base-ubuntu2404/arm64/latest/ami-id \
  --query "Parameter.Value" --output text
```

Alternatively, you can search for PCS-ready DLAMI by name pattern:

- x86_64

```
aws ec2 describe-images --region `region-code` --owners amazon \
  --filters 'Name=name,Values=aws-pcs-ready-dlami-base-ubuntu2404-x86_64-*' \
            'Name=state,Values=available' \
  --query 'sort_by(Images, &CreationDate)[-1].[Name,ImageId]' --output text
```

- arm64

```
aws ec2 describe-images --region `region-code` --owners amazon \
  --filters 'Name=name,Values=aws-pcs-ready-dlami-base-ubuntu2404-arm64-*' \
            'Name=state,Values=available' \
  --query 'sort_by(Images, &CreationDate)[-1].[Name,ImageId]' --output text
```

Use the AMI ID when you create or update a compute node group.

## Use with Infrastructure as Code

The SSM parameter path provides a stable reference that always resolves to the latest
AMI ID. You can use this in CloudFormation templates to automatically pick up new versions on
redeployment:

```
AmiId: '{{resolve:ssm:/aws/service/pcs/ami/dlami-base-ubuntu2404/x86_64/latest/ami-id}}'
```

## Update to a new version

AWS releases updated PCS-ready DLAMI versions when the source Deep Learning Base GPU AMI
is updated or when PCS components (PCS Agent or Slurm for PCS) are updated. To update your
cluster, retrieve the latest AMI ID using the SSM parameter or name search described above,
then update each compute node group to reference the new AMI ID.
