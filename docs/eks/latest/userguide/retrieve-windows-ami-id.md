**Help improve this page**

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Retrieve recommended Microsoft Windows AMI IDs

When deploying nodes, you can specify an ID for a pre-built Amazon EKS optimized Amazon Machine Image (AMI). To retrieve an AMI ID that fits your desired configuration, query the AWS Systems Manager Parameter Store API. Using this API eliminates the need to manually look up Amazon EKS optimized AMI IDs. For more information, see [GetParameter](../../../systems-manager/latest/APIReference/API_GetParameter.md "../../../systems-manager/latest/APIReference/API_GetParameter.md"). The [IAM principal](../../../IAM/latest/UserGuide/id_roles.md#iam-term-principal "../../../IAM/latest/UserGuide/id_roles.md#iam-term-principal") that you use must have the `ssm:GetParameter` IAM permission to retrieve the Amazon EKS optimized AMI metadata.

You can retrieve the image ID of the latest recommended Amazon EKS optimized Windows AMI with the following command, which uses the sub-parameter `image_id`. Make the following modifications to the command as needed and then run the modified command:

- Replace `release` with one of the following options.
  - Use `2022` for Windows Server 2022.
  - Use `2019` for Windows Server 2019.

- Replace `installation-option` with one of the following options. For more information, see [What is the Server Core installation option in Windows Server](https://learn.microsoft.com/en-us/windows-server/administration/server-core/what-is-server-core "https://learn.microsoft.com/en-us/windows-server/administration/server-core/what-is-server-core").
  - Use `Core` for a minimal installation with a smaller attack surface.
  - Use `Full` to include the Windows desktop experience.

- Replace `kubernetes-version` with a supported [platform-version](platform-versions.md "platform-versions.md").
- Replace `region-code` with an [Amazon EKS supported AWS Region](../../../general/latest/gr/eks.md "../../../general/latest/gr/eks.md") for which you want the AMI ID.

```
 aws ssm get-parameter --name /aws/service/ami-windows-latest/Windows_Server-<replaceable>release</replaceable>-English-<replaceable>installation-option</replaceable>-EKS_Optimized-<replaceable>kubernetes-version</replaceable>/image_id \
    --region <replaceable>region-code</replaceable> --query "Parameter.Value" --output text
```

Here’s an example command after placeholder replacements have been made.

```
 aws ssm get-parameter --name /aws/service/ami-windows-latest/Windows_Server-<replaceable>2022</replaceable>-English-<replaceable>Core</replaceable>-EKS_Optimized-<replaceable>k8s-n-2</replaceable>/image_id \
    --region <replaceable>us-west-2</replaceable> --query "Parameter.Value" --output text
```

An example output is as follows.

```
 ami-<replaceable>1234567890abcdef0</replaceable>
```
