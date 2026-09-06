

 **Help improve this page** 

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Retrieve recommended Amazon Linux AMI IDs
<a name="retrieve-ami-id"></a>

When deploying nodes, you can specify an ID for a pre-built Amazon EKS optimized Amazon Machine Image (AMI). To retrieve an AMI ID that fits your desired configuration, query the AWS Systems Manager Parameter Store API. Using this API eliminates the need to manually look up Amazon EKS optimized AMI IDs. For more information, see [GetParameter](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_GetParameter.html). The [IAM principal](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html#iam-term-principal) that you use must have the `ssm:GetParameter` IAM permission to retrieve the Amazon EKS optimized AMI metadata.

You can retrieve the image ID of the latest recommended Amazon EKS optimized Amazon Linux AMI with the following command, which uses the sub-parameter `image_id`. Make the following modifications to the command as needed and then run the modified command:
+ Replace `<kubernetes-version>` with an [Amazon EKS supported version](https://docs.aws.amazon.com/eks/latest/userguide/kubernetes-versions.html).
+ Replace {{ami-type}} with one of the following options. For information about the types of Amazon EC2 instances, see [Amazon EC2 instance types](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-types.html).
  + Use {{amazon-linux-2023/x86\_64/standard}} for Amazon Linux 2023 (AL2023) `x86` based instances.
  + Use {{amazon-linux-2023/arm64/standard}} for AL2023 ARM instances, such as [AWS Graviton](https://aws.amazon.com/ec2/graviton/) based instances.
  + Use {{amazon-linux-2023/x86\_64/nvidia}} for the latest approved AL2023 NVIDIA `x86` based instances.
  + Use {{amazon-linux-2023/arm64/nvidia}} for the latest approved AL2023 NVIDIA `arm64` based instances.
  + Use {{amazon-linux-2023/x86\_64/neuron}} for the latest AL2023 [AWS Neuron](https://aws.amazon.com/machine-learning/neuron/) instances.
+ Replace `<region-code>` with an [Amazon EKS supported AWS Region](https://docs.aws.amazon.com/general/latest/gr/eks.html) for which you want the AMI ID.

```
aws ssm get-parameter --name /aws/service/eks/optimized-ami/<kubernetes-version>/<ami-type>/recommended/image_id \
    --region <region-code> --query "Parameter.Value" --output text
```

Here’s an example command after placeholder replacements have been made.

```
aws ssm get-parameter --name /aws/service/eks/optimized-ami/{{1.31}}/{{amazon-linux-2023}}/{{x86_64/standard}}/recommended/image_id \
    --region {{us-west-2}} --query "Parameter.Value" --output text
```

An example output is as follows.

```
ami-{{1234567890abcdef0}}
```