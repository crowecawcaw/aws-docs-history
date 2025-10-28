# AWS managed policies for Amazon GameLift Servers

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

## AWS managed policy:

GameLiftContainerFleetPolicy

You can attach `GameLiftContainerFleetPolicy` to your IAM roles.

The policy grants permissions for compute actions in an Amazon GameLift Servers container fleet. A
container fleet is a set of hosting resources that Amazon GameLift Servers manages for you. Amazon GameLift Servers needs
permissions to connect to the Amazon GameLift Servers service and other AWS services on your behalf.

When creating a container fleet with Amazon GameLift Servers, provide an IAM service role with the
GameLiftContainerFleetPolicy managed policy attached. For instructions on creating the service role, see [Set up an IAM service role for Amazon GameLift Servers](setting-up-role.md "setting-up-role.md").

For more information, see [GameLiftContainerFleetPolicy](../../../aws-managed-policy/latest/reference/GameLiftContainerFleetPolicy.md "../../../aws-managed-policy/latest/reference/GameLiftContainerFleetPolicy.md").

**Permissions details**

This policy includes the following permissions.

- `cloudwatch` – Allows Amazon GameLift Servers to write game session logs to an
  Amazon CloudWatch Events log stream in your AWS account.
- `cloudwatch` – Allows Amazon GameLift Servers to create an CloudWatch log group to
  organize game session data in the log stream.
- `s3` – Allows Amazon GameLift Servers to write game session logs to an Amazon Simple Storage Service
  bucket in your AWS account.
- `s3` – Allows Amazon GameLift Servers to retrieve the AWS Region where a
  specified Amazon S3 bucket resides, using the API action
  `s3:GetBucketLocation`.
- `gamelift` – Allows Amazon GameLift Servers to retrieve an authentication token
  that allows a hosted game server to communicate with the Amazon GameLift Servers service through your
  AWS account.

## Amazon GameLift Servers updates to AWS managed

policies

View details about updates to AWS managed policies for Amazon GameLift Servers since this service
began tracking these changes. For automatic alerts about changes to this page, subscribe to
the RSS feed on the Amazon GameLift Servers Release notes page.

| Change                                                                                                                                                   | Description                                                                                                                      | Date              |
| -------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- | ----------------- |
| [GameLiftContainerFleetPolicy](#security-iam-awsmanpol-GameLiftContainerFleetPolicy "#security-iam-awsmanpol-GameLiftContainerFleetPolicy") – Change     | Amazon GameLift Servers added new permissions to retrieve the AWS Region of an Amazon S3 bucket.                                 | February 5, 2024  |
| [GameLiftContainerFleetPolicy](#security-iam-awsmanpol-GameLiftContainerFleetPolicy "#security-iam-awsmanpol-GameLiftContainerFleetPolicy") – New policy | Amazon GameLift Servers added new permissions to enable game server containers to run on Amazon GameLift Servers managed fleets. | November 12, 2024 |
| Amazon GameLift Servers started tracking changes                                                                                                         | Amazon GameLift Servers started tracking changes for its AWS managed policies.                                                   | November 12, 2024 |
