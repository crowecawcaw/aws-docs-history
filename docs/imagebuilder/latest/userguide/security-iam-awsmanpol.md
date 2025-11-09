# Use AWS managed policies for EC2 Image Builder

An AWS managed policy is a standalone policy that is created and administered by AWS. AWS managed policies are designed
to provide permissions for many common use cases so that you can start assigning permissions to users, groups, and roles.

Keep in mind that AWS managed policies might not grant least-privilege permissions for your specific use cases because
they're available for all AWS customers to use. We recommend that you reduce permissions further by defining
[customer managed policies](../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#customer-managed-policies "../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#customer-managed-policies") that are specific to your use cases.

You cannot change the permissions defined in AWS managed policies. If AWS updates the permissions defined in an AWS
managed policy, the update affects all principal identities (users, groups, and roles) that the policy is attached to. AWS is
most likely to update an AWS managed policy when a new AWS service is launched or new API operations become available for
existing services.

For more information, see [AWS managed policies](../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies "../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies") in the
_IAM User Guide_.

## AWSImageBuilderFullAccess policy

The **AWSImageBuilderFullAccess** policy grants full
access to Image Builder resources for the role it's attached to, allowing the role to list,
describe, create, update, and delete Image Builder resources. The policy also
grants targeted permissions to related AWS services that are needed, for example,
to verify resources, or to display current resources for the account in the AWS Management Console.

### Permissions details

This policy includes the following permissions:

- **Image Builder** – Administrative access
  is granted, so that the role can list, describe, create, update, and
  delete Image Builder resources.
- **Amazon EC2** – Access is granted for
  Amazon EC2 Describe actions that are needed to verify resource existence
  or get lists of resources belonging to the account.
- **IAM** – Access is granted to
  get and use instance profiles whose name contains "imagebuilder",
  to verify the existence of the Image Builder service-linked role via the
  `iam:GetRole` API action, and to create the Image Builder service-linked role.
- **License Manager** – Access is granted to
  list license configurations or licenses for a resource.
- **Amazon S3** – Access is granted to list buckets
  belonging to the account, and also Image Builder buckets with "imagebuilder" in their
  names.
- **Amazon SNS** – Write permissions are
  granted to Amazon SNS to verify topic ownership for topics containing "imagebuilder".

To view the permissions for this policy, see [AWSImageBuilderFullAccess](../../../aws-managed-policy/latest/reference/AWSImageBuilderFullAccess.md "../../../aws-managed-policy/latest/reference/AWSImageBuilderFullAccess.md") in the _AWS
Managed Policy Reference_.

## AWSImageBuilderReadOnlyAccess policy

The **AWSImageBuilderReadOnlyAccess** policy provides
read-only access to all Image Builder resources. Permissions are granted to verify that the
Image Builder service-linked role exists via the `iam:GetRole` API action.

### Permissions details

This policy includes the following permissions:

- **Image Builder** – Access is granted for
  read-only access to Image Builder resources.
- **IAM** – Access is granted to
  verify the existence of the Image Builder service-linked role via the `iam:GetRole`
  API action.

To view the permissions for this policy, see [AWSImageBuilderReadOnlyAccess](../../../aws-managed-policy/latest/reference/AWSImageBuilderReadOnlyAccess.md "../../../aws-managed-policy/latest/reference/AWSImageBuilderReadOnlyAccess.md") in the _AWS
Managed Policy Reference_.

## AWSServiceRoleForImageBuilder policy

The **AWSServiceRoleForImageBuilder** policy allows Image Builder to
call AWS services on your behalf.

### Permissions details

This policy is attached to the Image Builder service-linked role when the role is created
through Systems Manager. For more information about the Image Builder service-linked role, see
[Use IAM service-linked roles for
Image Builder](image-builder-service-linked-role.md "image-builder-service-linked-role.md").

The policy includes the following permissions:

- **CloudWatch Logs** – Access is granted to
  create and upload CloudWatch Logs to any log group whose name starts with
  `/aws/imagebuilder/`.
- **Amazon EC2** – Access is granted for Image Builder to
  create, take snapshots of and register images (AMIs) that it creates and launch
  EC2 instances in your account. Image Builder uses related snapshots,
  volumes, network interfaces, subnets, security groups, license configuration and
  key pairs as required, as long as the image, instance, and volumes that are being
  created or used are tagged with `CreatedBy: EC2 Image Builder` or
  `CreatedBy: EC2 Fast Launch`.

Image Builder can get information about Amazon EC2 images, instance attributes, instance
status, the instance types that are available to your account, launch templates,
subnets, hosts, and tags on your Amazon EC2 resources.

Image Builder can update image settings to enable or disable faster launching of Windows
instances in your account, where the image is tagged with
`CreatedBy: EC2 Image Builder`.

Additionally, Image Builder can start, stop, and terminate instances that are running
in your account, share Amazon EBS snapshots, create and update images and launch templates,
de-register existing images, add tags, and replicate images across accounts
that you have granted permissions to via the **Ec2ImageBuilderCrossAccountDistributionAccess** policy. Image Builder
tagging is required for all of these actions, as described
previously.

- **Amazon ECR** – Access is granted for Image Builder to
  create a repository if needed for container image vulnerability scans, and tag the
  resources it creates to limit the scope of its operations. Access is also granted
  for Image Builder to delete the container images that it created for the scans after it
  takes snapshots of the vulnerabilities.
- **EventBridge** – Access is granted for Image Builder to
  create and manage EventBridge rules.
- **IAM** – Access is granted for Image Builder to
  pass any role in your account to Amazon EC2, and to VM Import/Export.
- **Amazon Inspector** – Access is granted for Image Builder to
  determine when Amazon Inspector completes build instance scans, and to collect findings for
  images that are configured to allow it.
- **AWS KMS** – Access is granted for Amazon EBS to
  encrypt, decrypt, or re-encrypt Amazon EBS volumes. This is crucial to ensure that
  encrypted volumes work when Image Builder builds an image.
- **License Manager** – Access is granted for Image Builder to
  update License Manager specifications via `license-manager:UpdateLicenseSpecificationsForResource`.
- **Amazon SNS** – Write permissions are
  granted for any Amazon SNS topic in your account.
- **Systems Manager** – Access is granted for Image Builder to
  list Systems Manager commands and their invocations, inventory entries , describe instance
  information and automation execution statuses, describe hosts for instance placement support,
  and get command invocation details. Image Builder can also send automation signals, and
  stop automation executions for any resource in your account.

Image Builder is able to issue run command invocations to any instance that is tagged
`"CreatedBy": "EC2 Image Builder"` for the following script files:
`AWS-RunPowerShellScript`, `AWS-RunShellScript`,
or `AWSEC2-RunSysprep`. Image Builder is able to start an Systems Manager automation
execution in your account for automation documents where the name starts with
`ImageBuilder`.

Image Builder is also able to create or delete State Manager associations for any instance
in your account, as long as the association document is
`AWS-GatherSoftwareInventory`, and to create the Systems Manager service-linked
role in your account.

Image Builder is able to read public Parameter Store Parameters, and read and update private
Parameters prefixed with `/imagebuilder/` so that it can update the Parameter
value with the output AMI IDs that Image Builder creates from a new build.

- **AWS STS** – Access is granted for Image Builder to
  assume roles named **EC2ImageBuilderDistributionCrossAccountRole**
  from your account to any account where the Trust policy on the role permits it. This
  is used for cross-account image distribution.

To view the permissions for this policy, see [AWSServiceRoleForImageBuilder](../../../aws-managed-policy/latest/reference/AWSServiceRoleForImageBuilder.md "../../../aws-managed-policy/latest/reference/AWSServiceRoleForImageBuilder.md") in the _AWS
Managed Policy Reference_.

## Ec2ImageBuilderCrossAccountDistributionAccess policy

The **Ec2ImageBuilderCrossAccountDistributionAccess**
policy grants permissions for Image Builder to distribute images across accounts in target Regions.
Additionally, Image Builder can describe, copy, and apply tags to any Amazon EC2 image in the account.
The policy also grants the ability to modify AMI permissions via the
`ec2:ModifyImageAttribute` API action.

### Permissions details

This policy includes the following permissions:

- **Amazon EC2** – Access is granted for
  Amazon EC2 to describe, copy, and modify attributes for an image, and to create
  tags for any Amazon EC2 images in the account.

To view the permissions for this policy, see [Ec2ImageBuilderCrossAccountDistributionAccess](../../../aws-managed-policy/latest/reference/Ec2ImageBuilderCrossAccountDistributionAccess.md "../../../aws-managed-policy/latest/reference/Ec2ImageBuilderCrossAccountDistributionAccess.md") in the _AWS
Managed Policy Reference_.

## EC2ImageBuilderLifecycleExecutionPolicy policy

The **EC2ImageBuilderLifecycleExecutionPolicy**
policy grants permissions for Image Builder to perform actions such as deprecate, disable, or delete Image Builder
image resources and their underlying resources (AMIs, snapshots) to support automated rules for
image lifecycle management tasks.

### Permissions details

This policy includes the following permissions:

- **Amazon EC2** – Access is granted for Amazon EC2
  to perform the following actions for Amazon Machine Images (AMIs) in the account
  that are tagged with `CreatedBy: EC2 Image Builder`.
  - Enable and disable an AMI.
  - Enable and disable image deprecation.
  - Describe and deregister an AMI.
  - Describe and modify AMI image attributes.
  - Delete volume snapshots that are associated with the AMI.
  - Retrieve tags for a resource.
  - Add or remove tags from an AMI for deprecation.

- **Amazon ECR** – Access is granted for
  Amazon ECR to perform the following batch actions on ECR repositories with
  the `LifecycleExecutionAccess: EC2 Image Builder` tag. Batch actions
  support automated container image lifecycle rules.

      + `ecr:BatchGetImage`
      + `ecr:BatchDeleteImage`

  Access is granted at the repository level for ECR repositories that are tagged
  with `LifecycleExecutionAccess: EC2 Image Builder`.

- **AWS Resource groups** – Access is granted for
  Image Builder to get resources based on tags.
- **EC2 Image Builder** – Access is granted for
  Image Builder to delete Image Builder image resources.

To view the permissions for this policy, see [EC2ImageBuilderLifecycleExecutionPolicy](../../../aws-managed-policy/latest/reference/EC2ImageBuilderLifecycleExecutionPolicy.md "../../../aws-managed-policy/latest/reference/EC2ImageBuilderLifecycleExecutionPolicy.md") in the _AWS
Managed Policy Reference_.

## EC2InstanceProfileForImageBuilder policy

The **EC2InstanceProfileForImageBuilder** policy grants
the minimum permissions required for an EC2 instance to work with Image Builder. This does not
include permissions required to use the Systems Manager Agent.

### Permissions details

This policy includes the following permissions:

- **CloudWatch Logs** – Access is granted to
  create and upload CloudWatch Logs to any log group whose name starts with
  `/aws/imagebuilder/`.
- **Amazon EC2** – Access is granted to
  describe volumes and snapshots, to create snapshots of volume or
  snapshot resources that Image Builder created, and to create tags for Image Builder resources.
- **Image Builder** – Access is granted to
  get any Image Builder or AWS Marketplace component.
- **AWS KMS** – Access is granted to
  decrypt an Image Builder component, if it was encrypted via AWS KMS.
- **Amazon S3** – Access is granted to
  get objects stored in an Amazon S3 bucket whose name starts with
  `ec2imagebuilder-`, or resources that have an
  ISO file extension.

To view the permissions for this policy, see [EC2InstanceProfileForImageBuilder](../../../aws-managed-policy/latest/reference/EC2InstanceProfileForImageBuilder.md "../../../aws-managed-policy/latest/reference/EC2InstanceProfileForImageBuilder.md") in the _AWS
Managed Policy Reference_.

## EC2InstanceProfileForImageBuilderECRContainerBuilds policy

The **EC2InstanceProfileForImageBuilderECRContainerBuilds**
policy grants the minimum permissions required for an EC2 instance when working with Image Builder
to build Docker images and then register and store the images in an Amazon ECR container repository.
This does not include permissions required to use the Systems Manager Agent.

### Permissions details

This policy includes the following permissions:

- **CloudWatch Logs** – Access is granted to
  create and upload CloudWatch Logs to any log group whose name starts with
  `/aws/imagebuilder/`.
- **Amazon ECR** – Access is granted for
  Amazon ECR to get, register, and store a container image, and to get an
  authorization token.
- **Image Builder** – Access is granted to
  get an Image Builder component or container recipe.
- **AWS KMS** – Access is granted to
  decrypt an Image Builder component or container recipe, if it was encrypted via AWS KMS.
- **Amazon S3** – Access is granted to
  get objects stored in an Amazon S3 bucket whose name starts with
  `ec2imagebuilder-`.

To view the permissions for this policy, see [EC2InstanceProfileForImageBuilderECRContainerBuilds](../../../aws-managed-policy/latest/reference/EC2InstanceProfileForImageBuilderECRContainerBuilds.md "../../../aws-managed-policy/latest/reference/EC2InstanceProfileForImageBuilderECRContainerBuilds.md") in the _AWS
Managed Policy Reference_.

## Image Builder updates to AWS managed

policies

This section provides information about updates to AWS managed policies for Image Builder
since this service began tracking these changes. For automatic alerts about changes to
this page, subscribe to the RSS feed on the Image Builder [document
history](doc-history.md "doc-history.md") page.

| Change                                                                                                                                                                       | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | Date               |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------ |
| [AWSServiceRoleForImageBuilder](#sec-iam-manpol-AWSServiceRoleForImageBuilder "#sec-iam-manpol-AWSServiceRoleForImageBuilder") –<br>Update to an existing policy             | Image Builder made the following changes to the service role to support the use of<br>AWS Systems Manager (SSM) Parameter Store Parameters in recipes and during image<br>distribution.<br>• Added ssm:GetParameter to allow Image Builder to read public SSM Parameters<br>and private SSM Parameters prefixed with `/imagebuilder/` so that<br>they can be used in recipes.<br>• Added ssm:PutParameter to allow Image Builder to update private SSM Parameters<br>prefixed with `/imagebuilder/` with the output AMI IDs that<br>Image Builder creates from a new build.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | July 23, 2025      |
| [EC2InstanceProfileForImageBuilder](#sec-iam-manpol-EC2InstanceProfileForImageBuilder "#sec-iam-manpol-EC2InstanceProfileForImageBuilder") –<br>Update to an existing policy | Image Builder made the following changes to the instance profile policy to support<br>more file extensions for ISO file downloads.<br>• Added two file extensions to the `s3:GetObject` action<br>resource list: `"arn:aws:s3:::*/*.iso"` and<br>`"arn:aws:s3:::*/*.Iso"`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | May 19, 2025       |
| [AWSServiceRoleForImageBuilder](#sec-iam-manpol-AWSServiceRoleForImageBuilder "#sec-iam-manpol-AWSServiceRoleForImageBuilder") –<br>Update to an existing policy             | Image Builder made the following changes to the service role to support the import<br>of Microsoft client OS ISO files as the base image.<br>• Added ec2:RegisterImage to allow Image Builder to create a snapshot and<br>create and register an AMI whose baseline operating system was imported<br>from verified ISO disk files.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | December 30, 2024  |
| [EC2InstanceProfileForImageBuilder](#sec-iam-manpol-EC2InstanceProfileForImageBuilder "#sec-iam-manpol-EC2InstanceProfileForImageBuilder") –<br>Update to an existing policy | Image Builder made the following changes to the instance profile policy to support<br>image creation from disk image files.<br>• Added the following ec2 actions: DescribeVolumes and<br>DescribeSnapshots on all resources to retrieve details. Also added the<br>following actions for resources that were created by Image Builder:<br>CreateSnapshot for volume and snapshot resources, and CreateTags. Added<br>s3:GetObject for resources with an "ISO" file extension.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | December 30, 2024  |
| [EC2InstanceProfileForImageBuilder](#sec-iam-manpol-EC2InstanceProfileForImageBuilder "#sec-iam-manpol-EC2InstanceProfileForImageBuilder") –<br>Updated policy               | Image Builder updated the `EC2InstanceProfileForImageBuilder` policy<br>to allow Image Builder to get AWS Marketplace components.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | December 2, 2024   |
| [EC2ImageBuilderLifecycleExecutionPolicy](#sec-iam-manpol-EC2ImageBuilderLifecycleExecutionPolicy "#sec-iam-manpol-EC2ImageBuilderLifecycleExecutionPolicy") –<br>New policy | Image Builder added the new `EC2ImageBuilderLifecycleExecutionPolicy` policy<br>that contains permissions for image lifecycle management.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | November 17, 2023  |
| [AWSServiceRoleForImageBuilder](#sec-iam-manpol-AWSServiceRoleForImageBuilder "#sec-iam-manpol-AWSServiceRoleForImageBuilder") –<br>Update to an existing policy             | Image Builder made the following changes to the service role to provide instance placement support.<br>• Added ec2:DescribeHosts enables Image Builder to poll the hostId to determine when it's<br>in a valid state to launch an instance.<br>• Added ssm:GetCommandInvocation, API action to improve the method that Image Builder uses<br>to get details of the command invocation.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | October 19, 2023   |
| [AWSServiceRoleForImageBuilder](#sec-iam-manpol-AWSServiceRoleForImageBuilder "#sec-iam-manpol-AWSServiceRoleForImageBuilder") –<br>Update to an existing policy             | Image Builder made the following changes to the service role to provide instance placement support.<br>• Added ec2:DescribeHosts enable Image Builder to poll the hostId to determine when it's<br>in a valid state to launch an instance.<br>• Added ssm:GetCommandInvocation, API action to improve the method that Image Builder uses<br>to get details of the command invocation.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | September 28, 2023 |
| [AWSServiceRoleForImageBuilder](#sec-iam-manpol-AWSServiceRoleForImageBuilder "#sec-iam-manpol-AWSServiceRoleForImageBuilder") –<br>Update to an existing policy             | Image Builder made the following changes to the service role to allow Image Builder workflows to<br>collect vulnerability findings for both AMI and ECR container image builds. The<br>new permissions support the CVE detection and reporting feature.<br>• Added inspector2:ListCoverage and inspector2:ListFindings to allow Image Builder to determine<br>when Amazon Inspector completes test instance scans, and to collect findings for images that are<br>configured to allow it.<br>• Added ecr:CreateRepository, with a requirement for Image Builder to tag the repository with<br>`CreatedBy: EC2 Image Builder` (tag-on-create). Also added ecr:TagResource<br>(required for tag-on-create) with the same CreatedBy tag constraint, and an additional<br>constraint that requires the repository name to start with `image-builder-*`.<br>The name constraint prevents the escalation of privileges and prevents changes to<br>repositories that Image Builder didn't create.<br>• Added ecr:BatchDeleteImage for ECR repositories tagged with `CreatedBy:<br>EC2 Image Builder`. This permission requires the repository name to start with<br>`image-builder-*`.<br>• Added event permissions for Image Builder to create and manage Amazon EventBridge managed rules that<br>include `ImageBuilder-*` in the name. | March 30, 2023     |
| [AWSServiceRoleForImageBuilder](#sec-iam-manpol-AWSServiceRoleForImageBuilder "#sec-iam-manpol-AWSServiceRoleForImageBuilder") –<br>Update to an existing policy             | Image Builder made the following changes to the service role:<br>• Added License Manager licenses as a resource for the ec2:RunInstance call to allow customers to<br>use base image AMIs that are associated with a license configuration.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | March 22, 2022     |
| [AWSServiceRoleForImageBuilder](#sec-iam-manpol-AWSServiceRoleForImageBuilder "#sec-iam-manpol-AWSServiceRoleForImageBuilder") –<br>Update to an existing policy             | Image Builder made the following changes to the service role:<br>• Added permissions for EC2 EnableFastLaunch API action, to enable and disable faster<br>launching for Windows instances.<br>• Tightened scope more for ec2:CreateTags action and resource tag conditions.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | February 21, 2022  |
| [AWSServiceRoleForImageBuilder](#sec-iam-manpol-AWSServiceRoleForImageBuilder "#sec-iam-manpol-AWSServiceRoleForImageBuilder") –<br>Update to an existing policy             | Image Builder made the following changes to the service role:<br>• Added permissions to call the VMIE service to import a VM and create a base AMI from it.<br>• Tightened scope for ec2:CreateTags action and resource tag conditions.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | November 20, 2021  |
| [AWSServiceRoleForImageBuilder](#sec-iam-manpol-AWSServiceRoleForImageBuilder "#sec-iam-manpol-AWSServiceRoleForImageBuilder") –<br>Update to an existing policy             | Image Builder added new permissions to fix issues where more than one<br>inventory association causes the image build to get stuck.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | August 11, 2021    |
| [AWSImageBuilderFullAccess](#sec-iam-manpol-AWSImageBuilderFullAccess "#sec-iam-manpol-AWSImageBuilderFullAccess") –<br>Update to an existing policy                         | Image Builder made the following changes to the full access role:<br>• Added permissions to allow `ec2:DescribeInstanceTypeOffereings`.<br>• Added permissions to call `ec2:DescribeInstanceTypeOffereings` to enable the Image Builder<br>console to accurately reflect the instance types that are available in the account.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | April 13, 2021     |
| Image Builder started tracking changes                                                                                                                                       | Image Builder started tracking changes for its AWS managed policies.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | April 02, 2021     |
