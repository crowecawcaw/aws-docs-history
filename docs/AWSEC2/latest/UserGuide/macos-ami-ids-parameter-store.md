# Retrieve macOS AMI IDs using AWS Systems Manager Parameter Store API

You must specify an AMI when you launch an instance. An AMI is specific to an AWS Region,
operating system, and processor architecture. You can view all of the macOS AMIs in an
AWS Region and retrieve the latest macOS AMI by querying the AWS Systems Manager Parameter Store API.
Using these public parameters, you don't need to manually look up macOS AMI IDs. Public
parameters are available for both x86 and ARM64 macOS AMIs,
and can be integrated with your existing AWS CloudFormation templates.

###### Required permissions

To perform this action, the [IAM principal](../../../IAM/latest/UserGuide/id_roles.md#id_roles_terms-and-concepts "../../../IAM/latest/UserGuide/id_roles.md#id_roles_terms-and-concepts")
must have permissions to call the `ssm:GetParameter` API action.

###### To view a list of all macOS AMIs in the current AWS Region using the AWS CLI

Use the following [get-parameters-by-path](../../../cli/latest/reference/ssm/get-parameters-by-path.md "../../../cli/latest/reference/ssm/get-parameters-by-path.md") command to view a list of all macOS AMIs in the current
Region.

```
aws ssm get-parameters-by-path --path /aws/service/ec2-macos --recursive --query "Parameters[].Name"
```

###### To retrieve the AMI ID of the latest major macOS AMI using the AWS CLI

Use the following [get-parameter](../../../cli/latest/reference/ssm/get-parameter.md "../../../cli/latest/reference/ssm/get-parameter.md") command
with the sub-parameter `image_id`. In the following example, replace `sonoma` with a macOS supported major version, `x86_64_mac` with the processor, and `region-code`
with a supported AWS Region for which you want the latest macOS AMI ID.

```
aws ssm get-parameter --name /aws/service/ec2-macos/`sonoma`/`x86_64_mac`/latest/image_id --region `region-code`
```

For more information, see [Calling AMI public parameters for macOS](../../../systems-manager/latest/userguide/parameter-store-public-parameters-ami.md#public-parameters-ami-macos "../../../systems-manager/latest/userguide/parameter-store-public-parameters-ami.md#public-parameters-ami-macos") in the
_AWS Systems Manager User Guide_.
