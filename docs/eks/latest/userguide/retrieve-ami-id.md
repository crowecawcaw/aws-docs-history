**Help improve this page**

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Retrieve recommended Amazon Linux AMI IDs

When deploying nodes, you can specify an ID for a pre-built Amazon EKS optimized Amazon Machine Image (AMI). To retrieve an AMI ID that fits your desired configuration, query the AWS Systems Manager Parameter Store API. Using this API eliminates the need to manually look up Amazon EKS optimized AMI IDs. For more information, see [GetParameter](../../../systems-manager/latest/APIReference/API_GetParameter.md "../../../systems-manager/latest/APIReference/API_GetParameter.md"). The [IAM principal](../../../IAM/latest/UserGuide/id_roles.md#iam-term-principal "../../../IAM/latest/UserGuide/id_roles.md#iam-term-principal") that you use must have the `ssm:GetParameter` IAM permission to retrieve the Amazon EKS optimized AMI metadata.

You can retrieve the image ID of the latest recommended Amazon EKS optimized Amazon Linux AMI with the following command, which uses the sub-parameter `image_id`. Make the following modifications to the command as needed and then run the modified command:

- Replace `<kubernetes-version>` with an [Amazon EKS supported version](kubernetes-versions.md "kubernetes-versions.md").
- Replace `ami-type` with one of the following options. For information about the types of Amazon EC2 instances, see [Amazon EC2 instance types](../../../AWSEC2/latest/UserGuide/instance-types.md "../../../AWSEC2/latest/UserGuide/instance-types.md").
  - Use `amazon-linux-2023/x86_64/standard` for Amazon Linux 2023 (AL2023) `x86` based instances.
  - Use `amazon-linux-2023/arm64/standard` for AL2023 ARM instances, such as [AWS Graviton](https://aws.amazon.com/ec2/graviton/ "https://aws.amazon.com/ec2/graviton/") based instances.
  - Use `amazon-linux-2023/x86_64/nvidia` for the latest approved AL2023 NVIDIA `x86` based instances.
  - Use `amazon-linux-2023/arm64/nvidia` for the latest approved AL2023 NVIDIA `arm64` based instances.
  - Use `amazon-linux-2023/x86_64/neuron` for the latest AL2023 [AWS Neuron](https://aws.amazon.com/machine-learning/neuron/ "https://aws.amazon.com/machine-learning/neuron/") instances.
  - Use `amazon-linux-2` for Amazon Linux 2 (AL2) `x86` based instances.
  - Use `amazon-linux-2-arm64` for AL2 ARM instances, such as [AWS Graviton](https://aws.amazon.com/ec2/graviton/ "https://aws.amazon.com/ec2/graviton/") based instances.
  - Use `amazon-linux-2-gpu` for AL2 [hardware accelerated](../../../AWSEC2/latest/UserGuide/accelerated-computing-instances.md "../../../AWSEC2/latest/UserGuide/accelerated-computing-instances.md")
    `x86` based instances for NVIDIA GPU, [Inferentia](https://aws.amazon.com/machine-learning/inferentia/ "https://aws.amazon.com/machine-learning/inferentia/"), and [Trainium](https://aws.amazon.com/machine-learning/trainium/ "https://aws.amazon.com/machine-learning/trainium/") based workloads.

- Replace `<region-code>` with an [Amazon EKS supported AWS Region](../../../general/latest/gr/eks.md "../../../general/latest/gr/eks.md") for which you want the AMI ID.

```
aws ssm get-parameter --name /aws/service/eks/optimized-ami/<kubernetes-version>/<ami-type>/recommended/image_id \
    --region <region-code> --query "Parameter.Value" --output text
```

Here’s an example command after placeholder replacements have been made.

```
aws ssm get-parameter --name /aws/service/eks/optimized-ami/`1.31`/`amazon-linux-2023`/`x86_64/standard`/recommended/image_id \
    --region `us-west-2` --query "Parameter.Value" --output text
```

An example output is as follows.

```
ami-`1234567890abcdef0`

```
