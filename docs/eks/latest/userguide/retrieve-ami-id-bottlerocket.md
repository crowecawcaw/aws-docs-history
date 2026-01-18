**Help improve this page**

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Retrieve recommended Bottlerocket AMI IDs

When deploying nodes, you can specify an ID for a pre-built Amazon EKS optimized Amazon Machine Image (AMI). To retrieve an AMI ID that fits your desired configuration, query the AWS Systems Manager Parameter Store API. Using this API eliminates the need to manually look up Amazon EKS optimized AMI IDs. For more information, see [GetParameter](../../../systems-manager/latest/APIReference/API_GetParameter.md "../../../systems-manager/latest/APIReference/API_GetParameter.md"). The [IAM principal](../../../IAM/latest/UserGuide/id_roles.md#iam-term-principal "../../../IAM/latest/UserGuide/id_roles.md#iam-term-principal") that you use must have the `ssm:GetParameter` IAM permission to retrieve the Amazon EKS optimized AMI metadata.

You can retrieve the image ID of the latest recommended Amazon EKS optimized Bottlerocket AMI with the following AWS CLI command, which uses the sub-parameter `image_id`. Make the following modifications to the command as needed and then run the modified command:

- Replace `kubernetes-version` with a supported [platform-version](platform-versions.md "platform-versions.md").
- Replace `-flavor` with one of the following options.
  - Remove `-flavor` for variants without a GPU.
  - Use `-nvidia` for GPU-enabled variants.
  - Use `-fips` for FIPS-enabled variants.

- Replace `architecture` with one of the following options.
  - Use `x86_64` for `x86` based instances.
  - Use `arm64` for ARM instances.

- Replace `region-code` with an [Amazon EKS supported AWS Region](../../../general/latest/gr/eks.md "../../../general/latest/gr/eks.md") for which you want the AMI ID.

```
 aws ssm get-parameter --name /aws/service/bottlerocket/aws-k8s-<replaceable>kubernetes-version-flavor</replaceable>/<replaceable>architecture</replaceable>/latest/image_id \
    --region <replaceable>region-code</replaceable> --query "Parameter.Value" --output text
```

Here’s an example command after placeholder replacements have been made.

```
 aws ssm get-parameter --name /aws/service/bottlerocket/aws-k8s-<replaceable>1.31</replaceable>/<replaceable>x86_64</replaceable>/latest/image_id \
    --region <replaceable>us-west-2</replaceable> --query "Parameter.Value" --output text
```

An example output is as follows.

```
 ami-<replaceable>1234567890abcdef0</replaceable>
```
