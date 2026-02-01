• AWS Systems Manager Change Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see
[AWS Systems Manager Change Manager availability change](change-manager-availability-change.md "change-manager-availability-change.md").

 

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see
[Amazon CloudWatch Dashboard documentation](../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md "../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md").

# Reference: Amazon S3 buckets for patching

operations

In the course of performing various Patch Manager patching operations, AWS Systems Manager Agent
(SSM Agent) accesses certain Amazon Simple Storage Service (Amazon S3) buckets that are owned and maintained by
Amazon Web Services (AWS). These S3 buckets are publicly accessible, and by default, SSM Agent
connects to them using `HTTP` calls.

However, if you're using a virtual private cloud (VPC) endpoint in your Systems Manager operations,
you must provide explicit permission in an Amazon Elastic Compute Cloud (Amazon EC2) instance profile for Systems Manager, or
in a service role for non-EC2 machines in a [hybrid and multicloud](operating-systems-and-machine-types.md#supported-machine-types "operating-systems-and-machine-types.md#supported-machine-types") environment. Otherwise, your
resources can't access these public buckets.

This reference topic lists the patching-related buckets for each supported
AWS Region.

For information about specifying these S3 buckets in EC2 instance profiles, see [SSM Agent communications with
AWS managed S3 buckets](ssm-agent-technical-details.md#ssm-agent-minimum-s3-permissions "ssm-agent-technical-details.md#ssm-agent-minimum-s3-permissions").

For information about using VPC endpoints with Systems Manager, see [Improve the security of EC2 instances by using VPC
endpoints for Systems Manager](setup-create-vpc.md "setup-create-vpc.md").

###### Topics

- [Buckets containing SSM
  Command documents for patching operations (Linux and Windows Server)](#aws-patch-manager-buckets-linux-windows "#aws-patch-manager-buckets-linux-windows")
- [Buckets containing SSM Command
  documents for patching operations (macOS)](#aws-patch-manager-buckets-macos "#aws-patch-manager-buckets-macos")
- [Buckets containing AWS
  managed patch baseline snapshots](#aws-patch-manager-buckets-baseline-snapshots "#aws-patch-manager-buckets-baseline-snapshots")

## Buckets containing SSM

Command documents for patching operations (Linux and Windows Server)

Buckets with the format
`aws-patch-manager-`region`-`unique-suffix``
contain the following documents used by Patch Manager patching operations on the Linux and
Windows Server operating systems:

- `AWS-RunPatchBaseline`
- `AWS-RunPatchBaselineAssociation`
- `AWS-RunPatchBaselineWithHooks`
- `AWS-InstanceRebootWithHooks`
- `AWS-PatchAsgInstance`
- `AWS-PatchInstanceWithRollback`

| Region name               | Region code    | `aws-patch-manager-`region`-`suffix``<br>bucket |
| ------------------------- | -------------- | ----------------------------------------------- |
| US East (Ohio)            | us-east-2      | aws-patch-manager-us-east-2-552881074           |
| US East (N. Virginia)     | us-east-1      | aws-patch-manager-us-east-1-1970c647d           |
| US West (N. California)   | us-west-1      | aws-patch-manager-us-west-1-8badb4304           |
| US West (Oregon)          | us-west-2      | aws-patch-manager-us-west-2-34d7f99f8           |
| Africa (Cape Town)        | af-south-1     | aws-patch-manager-af-south-1-bdd5f65a9          |
| Asia Pacific (Hong Kong)  | ap-east-1      | aws-patch-manager-ap-east-1-632356271           |
| Asia Pacific (Hyderabad)  | ap-south-2     | aws-patch-manager-ap-south-2-32f4b4128          |
| Asia Pacific (Jakarta)    | ap-southeast-3 | aws-patch-manager-ap-southeast-3-aa48fc462      |
| Asia Pacific (Melbourne)  | ap-southeast-4 | aws-patch-manager-ap-southeast-4-01e2c40d3      |
| Asia Pacific (Mumbai)     | ap-south-1     | aws-patch-manager-ap-south-1-cb7c62ff9          |
| Asia Pacific (Osaka)      | ap-northeast-3 | aws-patch-manager-ap-northeast-3-67373598a      |
| Asia Pacific (Seoul)      | ap-northeast-2 | aws-patch-manager-ap-northeast-2-10467995c      |
| Asia Pacific (Singapore)  | ap-southeast-1 | aws-patch-manager-ap-southeast-1-7fdfd9ef7      |
| Asia Pacific (Sydney)     | ap-southeast-2 | aws-patch-manager-ap-southeast-2-17283a275      |
| Asia Pacific (Tokyo)      | ap-northeast-1 | aws-patch-manager-ap-northeast-1-4849fa78f      |
| Canada (Central)          | ca-central-1   | aws-patch-manager-ca-central-1-3148e69e3        |
| Canada West (Calgary)     | ca-west-1      | aws-patch-manager-ca-west-1-9e3a4b2f9           |
| Europe (Frankfurt)        | eu-central-1   | aws-patch-manager-eu-central-1-9163fdaaf        |
| Europe (Ireland)          | eu-west-1      | aws-patch-manager-eu-west-1-5522fb710           |
| Europe (London)           | eu-west-2      | aws-patch-manager-eu-west-2-902a2bc74           |
| Europe (Milan)            | eu-south-1     | aws-patch-manager-eu-south-1-c52f3f594          |
| Europe (Paris)            | eu-west-3      | aws-patch-manager-eu-west-3-29bf85721           |
| Europe (Spain)            | eu-south-2     | aws-patch-manager-eu-south-2-a4cf248b1          |
| Europe (Stockholm)        | eu-north-1     | aws-patch-manager-eu-north-1-795879e9b          |
| Europe (Zurich)           | eu-central-2   | aws-patch-manager-eu-central-2-184ce43c8        |
| Israel (Tel Aviv)         | il-central-1   | aws-patch-manager-il-central-1-e221cb57b        |
| Middle East (Bahrain)     | me-south-1     | aws-patch-manager-me-south-1-a53fc9dce          |
| Middle East (UAE)         | me-central-1   | aws-patch-manager-me-central-1-2932f2f80        |
| South America (São Paulo) | sa-east-1      | aws-patch-manager-sa-east-1-ddf4b6a09           |

## Buckets containing SSM Command

documents for patching operations (macOS)

Buckets with the format
`aws-patchmanager-macos-`region`-`unique-suffix``
contain the following documents used by Patch Manager patching operations on the macOS
operating system:

- `AWS-RunPatchBaseline`
- `AWS-RunPatchBaselineAssociation`
- `AWS-RunPatchBaselineWithHooks`
- `AWS-InstanceRebootWithHooks`
- `AWS-PatchAsgInstance`
- `AWS-PatchInstanceWithRollback`

| Region name               | Region code    | `aws-patchmanager-macos-`region`-`suffix``<br>bucket |
| ------------------------- | -------------- | ---------------------------------------------------- |
| US East (Ohio)            | us-east-2      | aws-patchmanager-macos-us-east-2-552881074           |
| US East (N. Virginia)     | us-east-1      | aws-patchmanager-macos-us-east-1-1970c647d           |
| US West (N. California)   | us-west-1      | aws-patchmanager-macos-us-west-1-8badb4304           |
| US West (Oregon)          | us-west-2      | aws-patchmanager-macos-us-west-2-34d7f99f8           |
| Africa (Cape Town)        | af-south-1     | aws-patchmanager-macos-af-south-1-bdd5f65a9          |
| Asia Pacific (Hong Kong)  | ap-east-1      | aws-patchmanager-macos-ap-east-1-632356271           |
| Asia Pacific (Hyderabad)  | ap-south-2     | aws-patchmanager-macos-ap-south-2-32f4b4128          |
| Asia Pacific (Jakarta)    | ap-southeast-3 | aws-patchmanager-macos-ap-southeast-3-aa48fc462      |
| Asia Pacific (Melbourne)  | ap-southeast-4 | aws-patchmanager-macos-ap-southeast-4-01e2c40d3      |
| Asia Pacific (Mumbai)     | ap-south-1     | aws-patchmanager-macos-ap-south-1-cb7c62ff9          |
| Asia Pacific (Osaka)      | ap-northeast-3 | aws-patchmanager-macos-ap-northeast-3-67373598a      |
| Asia Pacific (Seoul)      | ap-northeast-2 | aws-patchmanager-macos-ap-northeast-2-10467995c      |
| Asia Pacific (Singapore)  | ap-southeast-1 | aws-patchmanager-macos-ap-southeast-1-7fdfd9ef7      |
| Asia Pacific (Sydney)     | ap-southeast-2 | aws-patchmanager-macos-ap-southeast-2-17283a275      |
| Asia Pacific (Tokyo)      | ap-northeast-1 | aws-patchmanager-macos-ap-northeast-1-4849fa78f      |
| Canada (Central)          | ca-central-1   | aws-patchmanager-macos-ca-central-1-3148e69e3        |
| Canada West (Calgary)     | ca-west-1      | aws-patchmanager-macos-ca-west-1-9e3a4b2f9           |
| Europe (Frankfurt)        | eu-central-1   | aws-patchmanager-macos-eu-central-1-9163fdaaf        |
| Europe (Ireland)          | eu-west-1      | aws-patchmanager-macos-eu-west-1-5522fb710           |
| Europe (London)           | eu-west-2      | aws-patchmanager-macos-eu-west-2-902a2bc74           |
| Europe (Milan)            | eu-south-1     | aws-patchmanager-macos-eu-south-1-c52f3f594          |
| Europe (Paris)            | eu-west-3      | aws-patchmanager-macos-eu-west-3-29bf85721           |
| Europe (Spain)            | eu-south-2     | aws-patchmanager-macos-eu-south-2-a4cf248b1          |
| Europe (Stockholm)        | eu-north-1     | aws-patchmanager-macos-eu-north-1-795879e9b          |
| Europe (Zurich)           | eu-central-2   | aws-patchmanager-macos-eu-central-2-184ce43c8        |
| Israel (Tel Aviv)         | il-central-1   | aws-patchmanager-macos-il-central-1-e221cb57b        |
| Middle East (Bahrain)     | me-south-1     | aws-patchmanager-macos-me-south-1-a53fc9dce          |
| Middle East (UAE)         | me-central-1   | aws-patchmanager-macos-me-central-1-2932f2f80        |
| South America (São Paulo) | sa-east-1      | aws-patchmanager-macos-sa-east-1-ddf4b6a09           |

## Buckets containing AWS

managed patch baseline snapshots

Buckets with the format
`patch-baseline-snapshot-`region`` or
 `patch-baseline-snapshot-`region`-`unique-suffix``
contain AWS managed patch baseline snapshots. Access to this S3 bucket is required if
you use any of the following SSM documents:

- `AWS-RunPatchBaseline`
- `AWS-RunPatchBaselineAssociation`
- `AWS-RunPatchBaselineWithHooks`
- `AWS-ApplyPatchBaseline` (a legacy SSM Document)

| Region name               | Region code    | `patch-baseline-snapshot-*` bucket              |
| ------------------------- | -------------- | ----------------------------------------------- |
| US East (Ohio)            | us-east-2      | patch-baseline-snapshot-us-east-2               |
| US East (N. Virginia)     | us-east-1      | patch-baseline-snapshot-us-east-1               |
| US West (N. California)   | us-west-1      | patch-baseline-snapshot-us-west-1               |
| US West (Oregon)          | us-west-2      | patch-baseline-snapshot-us-west-2               |
| Africa (Cape Town)        | af-south-1     | patch-baseline-snapshot-af-south-1-tbxdb5b9     |
| Asia Pacific (Hong Kong)  | ap-east-1      | patch-baseline-snapshot-ap-east-1               |
| Asia Pacific (Hyderabad)  | ap-south-2     | patch-baseline-snapshot-ap-south-2-50209442     |
| Asia Pacific (Jakarta)    | ap-southeast-3 | patch-baseline-snapshot-ap-southeast-3-be0a3174 |
| Asia Pacific (Melbourne)  | ap-southeast-4 | patch-baseline-snapshot-ap-southeast-4-dc6f76ce |
| Asia Pacific (Mumbai)     | ap-south-1     | patch-baseline-snapshot-ap-south-1              |
| Asia Pacific (Osaka)      | ap-northeast-3 | patch-baseline-snapshot-ap-northeast-3          |
| Asia Pacific (Seoul)      | ap-northeast-2 | patch-baseline-snapshot-ap-northeast-2          |
| Asia Pacific (Singapore)  | ap-southeast-1 | patch-baseline-snapshot-ap-southeast-1          |
| Asia Pacific (Sydney)     | ap-southeast-2 | patch-baseline-snapshot-ap-southeast-2          |
| Asia Pacific (Tokyo)      | ap-northeast-1 | patch-baseline-snapshot-ap-northeast-1          |
| Canada (Central)          | ca-central-1   | patch-baseline-snapshot-ca-central-1            |
| Canada West (Calgary)     | ca-west-1      | patch-baseline-snapshot-ca-west-1               |
| Europe (Frankfurt)        | eu-central-1   | patch-baseline-snapshot-eu-central-1            |
| Europe (Ireland)          | eu-west-1      | patch-baseline-snapshot-eu-west-1               |
| Europe (London)           | eu-west-2      | patch-baseline-snapshot-eu-west-2               |
| Europe (Milan)            | eu-south-1     | patch-baseline-snapshot-eu-south-1              |
| Europe (Paris)            | eu-west-3      | patch-baseline-snapshot-eu-west-3               |
| Europe (Spain)            | eu-south-2     | patch-baseline-snapshot-eu-south-2-df2c9d70     |
| Europe (Stockholm)        | eu-north-1     | patch-baseline-snapshot-eu-north-1              |
| Europe (Zurich)           | eu-central-2   | patch-baseline-snapshot-eu-central-2            |
| Israel (Tel Aviv)         | il-central-1   | patch-baseline-snapshot-il-central-1            |
| Middle East (Bahrain)     | me-south-1     | patch-baseline-snapshot-me-south-1-uduvl7q8     |
| Middle East (UAE)         | me-central-1   | patch-baseline-snapshot-me-central-1            |
| South America (São Paulo) | sa-east-1      | patch-baseline-snapshot-sa-east-1               |
