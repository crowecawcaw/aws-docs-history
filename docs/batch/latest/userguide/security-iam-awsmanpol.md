# AWS managed policies for AWS Batch

You can use AWS managed policies for simpler identity access management for your team and provisioned AWS
resources. AWS managed policies cover a variety of common use cases, are available by default in your AWS account,
and are maintained and updated on your behalf. You can't change the permissions in AWS managed policies. If you
require greater flexibility, you can alternatively choose to create IAM customer managed policies. This way, you can
provide your team provisioned resources with only the exact permissions they need.

For more information about AWS managed policies, see [AWS managed policies](../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies "../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies")
in the _IAM User Guide_.

AWS services maintain and update AWS managed policies on your behalf. Periodically, AWS services add
additional permissions to an AWS managed policy. AWS managed policies are most likely updated when a new feature
launch or operation becomes available. These updates automatically affect all identities (users, groups, and roles)
where the policy is attached. However, they don't remove permissions or break your existing permissions.

Additionally, AWS supports managed policies for job functions that span multiple services. For example, the
`ReadOnlyAccess` AWS managed policy provides read-only access to all AWS services and resources. When
a service launches a new feature, AWS adds read-only permissions for new operations and resources. For a list and
descriptions of job function policies, see [AWS managed policies for job functions](../../../IAM/latest/UserGuide/access_policies_job-functions.md "../../../IAM/latest/UserGuide/access_policies_job-functions.md") in the
_IAM User Guide_.

## AWS managed policy:

**BatchServiceRolePolicy**

The **BatchServiceRolePolicy** managed IAM policy is used by the [AWSServiceRoleForBatch](using-service-linked-roles.md "using-service-linked-roles.md")
service-linked role. This allows AWS Batch to perform actions on your behalf. You can't attach
this policy to your IAM entities. For more information, see [Using service-linked roles for
AWS Batch](using-service-linked-roles.md "using-service-linked-roles.md").

This policy allows AWS Batch to complete the following actions on specific resources:

- `autoscaling` – Allows AWS Batch to create and manage Amazon EC2 Auto Scaling resources.
  AWS Batch creates and manages Amazon EC2 Auto Scaling groups for most compute environments.
- `ec2` – Allows AWS Batch to control the lifecycle of Amazon EC2 instances as well
  as create and manage launch templates and tags. AWS Batch creates and manages EC2 Spot Fleet
  requests for some EC2 Spot compute environments.
- `ecs` - Allows AWS Batch to create and managed Amazon ECS clusters, task
  definitions and tasks for job execution.
- `eks` - Allows AWS Batch to describe the Amazon EKS cluster resource for
  validations.
- `iam` - Allows AWS Batch to validate and pass roles provided by owner to
  Amazon EC2, Amazon EC2 Auto Scaling and Amazon ECS.
- `logs` – Allows AWS Batch to create and manage log groups and log streams for
  AWS Batch jobs.

To view the JSON for the policy, see [BatchServiceRolePolicy](../../../aws-managed-policy/latest/reference/BatchServiceRolePolicy.md "../../../aws-managed-policy/latest/reference/BatchServiceRolePolicy.md") in the [_AWS managed policies Reference
Guide_](../../../aws-managed-policy/latest/reference/about-managed-policy-reference.md "../../../aws-managed-policy/latest/reference/about-managed-policy-reference.md").

## AWS managed policy:

**AWSBatchServiceRolePolicyForSageMaker**

[AWSServiceRoleForAWSBatchWithSagemaker](using-service-linked-roles-batch-sagemaker.md "using-service-linked-roles-batch-sagemaker.md") allows AWS Batch to perform actions on your behalf. You can't attach
this policy to your IAM entities. For more information, see [Using service-linked roles for
AWS Batch](using-service-linked-roles.md "using-service-linked-roles.md").

This policy allows AWS Batch to complete the following actions on specific resources:

- `sagemaker` – Allows AWS Batch to manage SageMaker AI training jobs and other SageMaker AI
  resources.
- `iam:PassRole` – Allows AWS Batch to pass customer-defined execution roles to SageMaker AI for job execution. The resource constraint allows passing roles to SageMaker AI services.

To view the JSON for the policy, see [AWSBatchServiceRolePolicyForSageMaker](../../../aws-managed-policy/latest/reference/AWSBatchServiceRolePolicyForSageMaker.md "../../../aws-managed-policy/latest/reference/AWSBatchServiceRolePolicyForSageMaker.md") in the [_AWS managed policies Reference
Guide_](../../../aws-managed-policy/latest/reference/about-managed-policy-reference.md "../../../aws-managed-policy/latest/reference/about-managed-policy-reference.md").

## AWS managed policy:

**AWSBatchServiceRole** policy

The role permissions policy named **AWSBatchServiceRole** allows AWS Batch
to complete the following actions on specific resources:

The **AWSBatchServiceRole** managed IAM policy is often used by a role
named **AWSBatchServiceRole** and includes the following permissions.
Following the standard security advice of granting least privilege, the
**AWSBatchServiceRole** managed policy can be used as a guide. If any of
the permissions that are granted in the managed policy aren't needed for your use case, create
a custom policy and add only the permissions that you require. This AWS Batch managed policy and
role can be used with most compute environment types, but service-linked role usage is
preferred for a less error prone, better scoped and improved managed experience.

- `autoscaling` – Allows AWS Batch to create and manage Amazon EC2 Auto Scaling resources.
  AWS Batch creates and manages Amazon EC2 Auto Scaling groups for most compute environments.
- `ec2` – Allows AWS Batch to manage the lifecycle of Amazon EC2 instances as well
  as create and manage launch templates and tags. AWS Batch creates and manages EC2 Spot Fleet
  requests for some EC2 Spot compute environments.
- `ecs` - Allows AWS Batch to create and managed Amazon ECS clusters, task
  definitions and tasks for job execution.
- `iam` - Allows AWS Batch to validate and pass roles provided by owner to
  Amazon EC2, Amazon EC2 Auto Scaling and Amazon ECS.
- `logs` – Allows AWS Batch to create and manage log groups and log streams for
  AWS Batch jobs.

To view the JSON for the policy, see [AWSBatchServiceRole](../../../aws-managed-policy/latest/reference/AWSBatchServiceRole.md "../../../aws-managed-policy/latest/reference/AWSBatchServiceRole.md") in the [_AWS managed policies Reference
Guide_](../../../aws-managed-policy/latest/reference/about-managed-policy-reference.md "../../../aws-managed-policy/latest/reference/about-managed-policy-reference.md").

## AWS managed policy:

**AWSBatchFullAccess**

The **AWSBatchFullAccess** policy grants AWS Batch actions full access to AWS Batch resources. It
also grants describe and list action access for Amazon EC2, Amazon ECS, Amazon EKS, CloudWatch, and IAM services. This is so that IAM
identities, either users or roles, can view AWS Batch managed resources that were created on their behalf. Last, this
policy also allows for selected IAM roles to be passed to those services.

You can attach **AWSBatchFullAccess** to your IAM entities. AWS Batch also attaches this
policy to a service role that allows AWS Batch to perform actions on your behalf.

To view the JSON for the policy, see [AWSBatchFullAccess](../../../aws-managed-policy/latest/reference/AWSBatchFullAccess.md "../../../aws-managed-policy/latest/reference/AWSBatchFullAccess.md") in the [_AWS managed policies Reference
Guide_](../../../aws-managed-policy/latest/reference/about-managed-policy-reference.md "../../../aws-managed-policy/latest/reference/about-managed-policy-reference.md").

## AWS Batch updates to AWS managed

policies

View details about updates to AWS managed policies for AWS Batch since this service began tracking these
changes. For automatic alerts about changes to this page, subscribe to the RSS feed on the AWS Batch Document history
page.

| Change                                                                                                                                                                                                                                                | Description                                                                                                                                                                                                                                                                                                               | Date             |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------- |
| \***_[AWSBatchServiceRolePolicyForSageMaker](using-service-linked-roles-batch-sagemaker.md "using-service-linked-roles-batch-sagemaker.md")_**<br>• policy<br>added                                                                                   | Added new AWS managed policy for the \*_AWSBatchServiceRolePolicyForSageMaker_<br>• service-linked role that allows<br>AWS Batch to manage SageMaker AI on your behalf.                                                                                                                                                   | July 31, 2025    |
| \***_[BatchServiceRolePolicy](#security-iam-awsmanpol-BatchServiceRolePolicy "#security-iam-awsmanpol-BatchServiceRolePolicy")_**<br>• policy updated                                                                                                 | Updated to add support for describing Spot Fleet request history and Amazon EC2 Auto Scaling<br>activities.                                                                                                                                                                                                               | December 5, 2023 |
| \***_[AWSBatchServiceRole](#security-iam-awsmanpol-AWSBatchServiceRolePolicy "#security-iam-awsmanpol-AWSBatchServiceRolePolicy")_**<br>• policy added                                                                                                | Updated to add statement IDs, grant AWS Batch permissions to `ec2:DescribeSpotFleetRequestHistory`<br>and `autoscaling:DescribeScalingActivities`.                                                                                                                                                                        | December 5, 2023 |
| \*_[BatchServiceRolePolicy](#security-iam-awsmanpol-BatchServiceRolePolicy "#security-iam-awsmanpol-BatchServiceRolePolicy")_<br>• policy updated                                                                                                     | Updated to add support for describing Amazon EKS clusters.                                                                                                                                                                                                                                                                | October 20, 2022 |
| **[AWSBatchFullAccess](#security-iam-awsmanpol-BatchFullAccess "#security-iam-awsmanpol-BatchFullAccess")**<br>policy updated                                                                                                                         | Updated to add support for listing and describing Amazon EKS clusters.                                                                                                                                                                                                                                                    | October 20, 2022 |
| \*_[BatchServiceRolePolicy](#security-iam-awsmanpol-BatchServiceRolePolicy "#security-iam-awsmanpol-BatchServiceRolePolicy")_<br>• policy updated                                                                                                     | Updated to add support for Amazon EC2 Capacity Reservation groups that are managed by AWS Resource Groups. For more<br>information, see [Work with<br>Capacity Reservation groups](../../../AWSEC2/latest/UserGuide/create-cr-group.md "../../../AWSEC2/latest/UserGuide/create-cr-group.md") in _Amazon EC2 User Guide_. | May 18, 2022     |
| **[BatchServiceRolePolicy](#security-iam-awsmanpol-BatchServiceRolePolicy "#security-iam-awsmanpol-BatchServiceRolePolicy")\*<br>• and **[AWSBatchServiceRole](using-service-linked-roles.md "using-service-linked-roles.md")\*<br>• policies updated | Updated to add support for describing the status of AWS Batch managed instances in Amazon EC2 so that unhealthy<br>instances are replaced.                                                                                                                                                                                | December 6, 2021 |
| \*_[BatchServiceRolePolicy](#security-iam-awsmanpol-BatchServiceRolePolicy "#security-iam-awsmanpol-BatchServiceRolePolicy")_<br>• policy updated                                                                                                     | Updated to add support for placement group, capacity reservation, elastic GPU, and Elastic Inference resources in<br>Amazon EC2.                                                                                                                                                                                          | March 26, 2021   |
| \*_[BatchServiceRolePolicy](#security-iam-awsmanpol-BatchServiceRolePolicy "#security-iam-awsmanpol-BatchServiceRolePolicy")_<br>• policy added                                                                                                       | With the **BatchServiceRolePolicy\*<br>• managed policy for the<br>**AWSServiceRoleForBatch\*<br>• service-linked role, you can use a service-linked role managed by<br>AWS Batch. With this policy, you don't need to maintain your own role for use in your compute environments.                                       | March 10, 2021   |
| \*_[AWSBatchFullAccess](#security-iam-awsmanpol-BatchFullAccess "#security-iam-awsmanpol-BatchFullAccess")_<br>• add<br>permission to add service-linked role                                                                                         | Add IAM permissions to allow the \*_AWSServiceRoleForBatch_<br>• service-linked role to be<br>added to the account.                                                                                                                                                                                                       | March 10, 2021   |
| AWS Batch started tracking changes                                                                                                                                                                                                                    | AWS Batch started tracking changes for its AWS managed policies.                                                                                                                                                                                                                                                          | March 10, 2021   |
