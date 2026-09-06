

 **Help improve this page** 

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Retrieve recommended Microsoft Windows AMI IDs
<a name="retrieve-windows-ami-id"></a>

When deploying nodes, you can specify an ID for a pre-built Amazon EKS optimized Amazon Machine Image (AMI). To retrieve an AMI ID that fits your desired configuration, query the AWS Systems Manager Parameter Store API. Using this API eliminates the need to manually look up Amazon EKS optimized AMI IDs. For more information, see [GetParameter](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_GetParameter.html). The [IAM principal](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html#iam-term-principal) that you use must have the `ssm:GetParameter` IAM permission to retrieve the Amazon EKS optimized AMI metadata.

You can retrieve the image ID of the latest recommended Amazon EKS optimized Windows AMI with the following command, which uses the sub-parameter `image_id`. Make the following modifications to the command as needed and then run the modified command:
+ Replace {{release}} with one of the following options.
  + Use {{2025}} for Windows Server 2025.
  + Use {{2022}} for Windows Server 2022.
  + Use {{2019}} for Windows Server 2019.
+ Replace {{installation-option}} with one of the following options. For more information, see [What is the Server Core installation option in Windows Server](https://learn.microsoft.com/en-us/windows-server/administration/server-core/what-is-server-core).
  + Use {{Core}} for a minimal installation with a smaller attack surface.
  + Use {{Full}} to include the Windows desktop experience.
+ Replace {{kubernetes-version}} with a supported [platform-version](https://docs.aws.amazon.com/eks/latest/userguide/platform-versions.html).
+ Replace {{region-code}} with an [Amazon EKS supported AWS Region](https://docs.aws.amazon.com/general/latest/gr/eks.html) for which you want the AMI ID.

```
aws ssm get-parameter --name /aws/service/ami-windows-latest/Windows_Server-{{release}}-English-{{installation-option}}-EKS_Optimized-{{kubernetes-version}}/image_id \
    --region {{region-code}} --query "Parameter.Value" --output text
```

Here’s an example command after placeholder replacements have been made.

```
aws ssm get-parameter --name /aws/service/ami-windows-latest/Windows_Server-{{2022}}-English-{{Core}}-EKS_Optimized-{{k8s-n-2}}/image_id \
    --region {{us-west-2}} --query "Parameter.Value" --output text
```

An example output is as follows.

```
ami-{{1234567890abcdef0}}
```