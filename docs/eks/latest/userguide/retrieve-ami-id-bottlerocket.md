

 **Help improve this page** 

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Retrieve recommended Bottlerocket AMI IDs
<a name="retrieve-ami-id-bottlerocket"></a>

When deploying nodes, you can specify an ID for a pre-built Amazon EKS optimized Amazon Machine Image (AMI). To retrieve an AMI ID that fits your desired configuration, query the AWS Systems Manager Parameter Store API. Using this API eliminates the need to manually look up Amazon EKS optimized AMI IDs. For more information, see [GetParameter](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_GetParameter.html). The [IAM principal](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html#iam-term-principal) that you use must have the `ssm:GetParameter` IAM permission to retrieve the Amazon EKS optimized AMI metadata.

You can retrieve the image ID of the latest recommended Amazon EKS optimized Bottlerocket AMI with the following AWS CLI command, which uses the sub-parameter `image_id`. Make the following modifications to the command as needed and then run the modified command:
+ Replace {{kubernetes-version}} with a supported [platform-version](https://docs.aws.amazon.com/eks/latest/userguide/platform-versions.html).
+ Replace {{-flavor}} with one of the following options.
  + Remove {{-flavor}} for variants without a GPU.
  + Use {{-nvidia}} for GPU-enabled variants.
  + Use {{-fips}} for FIPS-enabled variants.
+ Replace {{architecture}} with one of the following options.
  + Use {{x86\_64}} for `x86` based instances.
  + Use {{arm64}} for ARM instances.
+ Replace {{region-code}} with an [Amazon EKS supported AWS Region](https://docs.aws.amazon.com/general/latest/gr/eks.html) for which you want the AMI ID.

```
aws ssm get-parameter --name /aws/service/bottlerocket/aws-k8s-{{kubernetes-version-flavor}}/{{architecture}}/latest/image_id \
    --region {{region-code}} --query "Parameter.Value" --output text
```

Here’s an example command after placeholder replacements have been made.

```
aws ssm get-parameter --name /aws/service/bottlerocket/aws-k8s-{{1.31}}/{{x86_64}}/latest/image_id \
    --region {{us-west-2}} --query "Parameter.Value" --output text
```

An example output is as follows.

```
ami-{{1234567890abcdef0}}
```