# AWS managed policies for AWS Fault Injection Service

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

## AWS managed policy: AmazonFISServiceRolePolicy

This policy is attached to the service-linked role named **AWSServiceRoleForFIS**
to allow AWS FIS to manage monitoring and resource selection for experiments. For more information, see [Use service-linked roles for AWS Fault Injection Service](using-service-linked-roles.md "using-service-linked-roles.md").

## AWS managed policy: AWSFaultInjectionSimulatorEC2Access

Use this policy in an experiment role to grant AWS FIS permission to run experiments that
use the [AWS FIS actions for Amazon EC2](fis-actions-reference.md#ec2-actions-reference "fis-actions-reference.md#ec2-actions-reference"). For more
information, see [IAM roles for AWS FIS experiments](getting-started-iam-service-role.md "getting-started-iam-service-role.md").

To view the permissions for this policy, see [AWSFaultInjectionSimulatorEC2Access](../../../aws-managed-policy/latest/reference/AWSFaultInjectionSimulatorEC2Access.md "../../../aws-managed-policy/latest/reference/AWSFaultInjectionSimulatorEC2Access.md") in the _AWS Managed Policy Reference_.

## AWS managed policy: AWSFaultInjectionSimulatorECSAccess

Use this policy in an experiment role to grant AWS FIS permission to run experiments that
use the [AWS FIS actions for Amazon ECS](fis-actions-reference.md#ecs-actions-reference "fis-actions-reference.md#ecs-actions-reference"). For more
information, see [IAM roles for AWS FIS experiments](getting-started-iam-service-role.md "getting-started-iam-service-role.md").

To view the permissions for this policy, see [AWSFaultInjectionSimulatorECSAccess](../../../aws-managed-policy/latest/reference/AWSFaultInjectionSimulatorECSAccess.md "../../../aws-managed-policy/latest/reference/AWSFaultInjectionSimulatorECSAccess.md") in the _AWS Managed Policy Reference_.

## AWS managed policy: AWSFaultInjectionSimulatorEKSAccess

Use this policy in an experiment role to grant AWS FIS permission to run experiments that
use the [AWS FIS actions for Amazon EKS](fis-actions-reference.md#eks-actions-reference "fis-actions-reference.md#eks-actions-reference"). For more
information, see [IAM roles for AWS FIS experiments](getting-started-iam-service-role.md "getting-started-iam-service-role.md").

To view the permissions for this policy, see [AWSFaultInjectionSimulatorEKSAccess](../../../aws-managed-policy/latest/reference/AWSFaultInjectionSimulatorEKSAccess.md "../../../aws-managed-policy/latest/reference/AWSFaultInjectionSimulatorEKSAccess.md") in the _AWS Managed Policy Reference_.

## AWS managed policy: AWSFaultInjectionSimulatorNetworkAccess

Use this policy in an experiment role to grant AWS FIS permission to run experiments that
use the [AWS FIS networking actions](fis-actions-reference.md#network-actions-reference "fis-actions-reference.md#network-actions-reference"). For more
information, see [IAM roles for AWS FIS experiments](getting-started-iam-service-role.md "getting-started-iam-service-role.md").

To view the permissions for this policy, see [AWSFaultInjectionSimulatorNetworkAccess](../../../aws-managed-policy/latest/reference/AWSFaultInjectionSimulatorNetworkAccess.md "../../../aws-managed-policy/latest/reference/AWSFaultInjectionSimulatorNetworkAccess.md") in the _AWS Managed Policy Reference_.

## AWS managed policy: AWSFaultInjectionSimulatorRDSAccess

Use this policy in an experiment role to grant AWS FIS permission to run experiments that
use the [AWS FIS actions for Amazon RDS](fis-actions-reference.md#rds-actions-reference "fis-actions-reference.md#rds-actions-reference"). For more
information, see [IAM roles for AWS FIS experiments](getting-started-iam-service-role.md "getting-started-iam-service-role.md").

To view the permissions for this policy, see [AWSFaultInjectionSimulatorRDSAccess](../../../aws-managed-policy/latest/reference/AWSFaultInjectionSimulatorRDSAccess.md "../../../aws-managed-policy/latest/reference/AWSFaultInjectionSimulatorRDSAccess.md") in the _AWS Managed Policy Reference_.

## AWS managed policy: AWSFaultInjectionSimulatorSSMAccess

Use this policy in an experiment role to grant AWS FIS permission to run experiments that
use the [AWS FIS actions for Systems Manager](fis-actions-reference.md#ssm-actions-reference "fis-actions-reference.md#ssm-actions-reference"). For more
information, see [IAM roles for AWS FIS experiments](getting-started-iam-service-role.md "getting-started-iam-service-role.md").

To view the permissions for this policy, see [AWSFaultInjectionSimulatorSSMAccess](../../../aws-managed-policy/latest/reference/AWSFaultInjectionSimulatorSSMAccess.md "../../../aws-managed-policy/latest/reference/AWSFaultInjectionSimulatorSSMAccess.md") in the _AWS Managed Policy Reference_.

## AWS FIS updates to AWS managed policies

View details about updates to AWS managed policies for AWS FIS since this service
began tracking these changes.

| Change                                                                                                                                                               | Description                                                                                                                                                                                                  | Date              |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------- |
| [AWSFaultInjectionSimulatorECSAccess](#AWSFaultInjectionSimulatorECSAccess "#AWSFaultInjectionSimulatorECSAccess") – Update to an existing policy                    | Added permissions to allow AWS FIS to resolve ECS targets.                                                                                                                                                   | January 25, 2024  |
| [AWSFaultInjectionSimulatorNetworkAccess](#AWSFaultInjectionSimulatorNetworkAccess "#AWSFaultInjectionSimulatorNetworkAccess") – Update to an existing policy        | Added permissions to allow AWS FIS to run experiments using the **aws:network:route-table-disrupt-cross-region-connectivity** and **aws:network:transit-gateway-disrupt-cross-region-connectivity** actions. | January 25, 2024  |
| [AWSFaultInjectionSimulatorEC2Access](#AWSFaultInjectionSimulatorEC2Access "#AWSFaultInjectionSimulatorEC2Access") – Update to an existing policy                    | Added permissions to allow AWS FIS to resolve EC2 instances.                                                                                                                                                 | November 13, 2023 |
| [AWSFaultInjectionSimulatorEKSAccess](#AWSFaultInjectionSimulatorEKSAccess "#AWSFaultInjectionSimulatorEKSAccess") – Update to an existing policy                    | Added permissions to allow AWS FIS to resolve EKS targets.                                                                                                                                                   | November 13, 2023 |
| [AWSFaultInjectionSimulatorRDSAccess](#AWSFaultInjectionSimulatorRDSAccess "#AWSFaultInjectionSimulatorRDSAccess") – Update to an existing policy                    | Added permissions to allow AWS FIS to resolve RDS targets.                                                                                                                                                   | November 13, 2023 |
| [AWSFaultInjectionSimulatorEC2Access](#AWSFaultInjectionSimulatorEC2Access "#AWSFaultInjectionSimulatorEC2Access") – Update to an existing policy                    | Added permissions to allow AWS FIS to run SSM documents on EC2 instances and to terminate EC2 instances.                                                                                                     | June 2, 2023      |
| [AWSFaultInjectionSimulatorSSMAccess](#AWSFaultInjectionSimulatorSSMAccess "#AWSFaultInjectionSimulatorSSMAccess") – Update to an existing policy                    | Added permissions to allow AWS FIS to run SSM documents on EC2 instances.                                                                                                                                    | June 2, 2023      |
| [AWSFaultInjectionSimulatorECSAccess](#AWSFaultInjectionSimulatorECSAccess "#AWSFaultInjectionSimulatorECSAccess") – Update to an existing policy                    | Added permissions to allow AWS FIS to run experiments using the new **aws:ecs:task** actions.                                                                                                                | June 1, 2023      |
| [AWSFaultInjectionSimulatorEKSAccess](#AWSFaultInjectionSimulatorEKSAccess "#AWSFaultInjectionSimulatorEKSAccess") – Update to an existing policy                    | Added permissions to allow AWS FIS to run experiments using the new **aws:eks:pod** actions.                                                                                                                 | June 1, 2023      |
| [AWSFaultInjectionSimulatorEC2Access](#AWSFaultInjectionSimulatorEC2Access "#AWSFaultInjectionSimulatorEC2Access") – New policy                                      | Added a policy to allow AWS FIS to run an experiment that uses AWS FIS actions for Amazon EC2.                                                                                                               | October 26, 2022  |
| [AWSFaultInjectionSimulatorECSAccess](#AWSFaultInjectionSimulatorECSAccess "#AWSFaultInjectionSimulatorECSAccess") – New policy                                      | Added a policy to allow AWS FIS to run an experiment that uses AWS FIS actions for Amazon ECS.                                                                                                               | October 26, 2022  |
| [AWSFaultInjectionSimulatorEKSAccess](#AWSFaultInjectionSimulatorEKSAccess "#AWSFaultInjectionSimulatorEKSAccess") – New policy                                      | Added a policy to allow AWS FIS to run an experiment that uses AWS FIS actions for Amazon EKS.                                                                                                               | October 26, 2022  |
| [AWSFaultInjectionSimulatorNetworkAccess](#AWSFaultInjectionSimulatorNetworkAccess "#AWSFaultInjectionSimulatorNetworkAccess") – New policy                          | Added a policy to allow AWS FIS to run an experiment that uses AWS FIS networking actions.                                                                                                                   | October 26, 2022  |
| [AWSFaultInjectionSimulatorRDSAccess](#AWSFaultInjectionSimulatorRDSAccess "#AWSFaultInjectionSimulatorRDSAccess") – New policy                                      | Added a policy to allow AWS FIS to run an experiment that uses AWS FIS actions for Amazon RDS.                                                                                                               | October 26, 2022  |
| [AWSFaultInjectionSimulatorSSMAccess](#AWSFaultInjectionSimulatorSSMAccess "#AWSFaultInjectionSimulatorSSMAccess") – New policy                                      | Added a policy to allow AWS FIS to run an experiment that uses AWS FIS actions for Systems Manager.                                                                                                          | October 26, 2022  |
| [AmazonFISServiceRolePolicy](#security-iam-awsmanpol-AmazonFISServiceRolePolicy "#security-iam-awsmanpol-AmazonFISServiceRolePolicy") – Update to an existing policy | Added permissions to allow AWS FIS to describe subnets.                                                                                                                                                      | October 26, 2022  |
| [AmazonFISServiceRolePolicy](#security-iam-awsmanpol-AmazonFISServiceRolePolicy "#security-iam-awsmanpol-AmazonFISServiceRolePolicy") – Update to an existing policy | Added permissions to allow AWS FIS to describe EKS clusters.                                                                                                                                                 | July 7, 2022      |
| [AmazonFISServiceRolePolicy](#security-iam-awsmanpol-AmazonFISServiceRolePolicy "#security-iam-awsmanpol-AmazonFISServiceRolePolicy") – Update to an existing policy | Added permissions to allow AWS FIS to list and describe the tasks in your clusters.                                                                                                                          | February 7, 2022  |
| [AmazonFISServiceRolePolicy](#security-iam-awsmanpol-AmazonFISServiceRolePolicy "#security-iam-awsmanpol-AmazonFISServiceRolePolicy") – Update to an existing policy | Removed the `events:ManagedBy` condition for the `events:DescribeRule` action.                                                                                                                               | January 6, 2022   |
| [AmazonFISServiceRolePolicy](#security-iam-awsmanpol-AmazonFISServiceRolePolicy "#security-iam-awsmanpol-AmazonFISServiceRolePolicy") – Update to an existing policy | Added permissions to allow AWS FIS to retrieve history for the CloudWatch alarms used in stop conditions.                                                                                                    | June 30, 2021     |
| AWS FIS started tracking changes                                                                                                                                     | AWS FIS started tracking changes to its AWS managed policies                                                                                                                                                 | March 1, 2021     |
