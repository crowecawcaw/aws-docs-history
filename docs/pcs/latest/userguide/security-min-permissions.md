# Minimum permissions for AWS PCS

This section describes the minimum IAM permissions required for an IAM identity (user, group, or role) to use the service.

###### Contents

- [Minimum permissions to use API actions](security-min-permissions.md#security-min-permissions_api "security-min-permissions.md#security-min-permissions_api")
- [Minimum permissions to use tags](security-min-permissions.md#security-min-permissions_tagging "security-min-permissions.md#security-min-permissions_tagging")
- [Minimum permissions to support logs](security-min-permissions.md#security-min-permissions_logging "security-min-permissions.md#security-min-permissions_logging")
- [Minimum permissions to use Capacity Blocks](security-min-permissions.md#security-min-permissions_capacity-blocks "security-min-permissions.md#security-min-permissions_capacity-blocks")
- [Minimum permissions for a service administrator](security-min-permissions.md#security-min-permissions_admin-policy "security-min-permissions.md#security-min-permissions_admin-policy")

## Minimum permissions to use API actions

| API action             | Minimum permissions                                                                                                                                                                                                                                                                                                                                                 | Additional permissions for the console                                                                   |
| ---------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| CreateCluster          | `<br>ec2:CreateNetworkInterface,<br>ec2:DescribeVpcs,<br>ec2:DescribeSubnets,<br>ec2:DescribeSecurityGroups,<br>ec2:GetSecurityGroupsForVpc,<br>iam:CreateServiceLinkedRole,<br>secretsmanager:CreateSecret,<br>secretsmanager:TagResource,<br>secretsmanager:RotateSecret,<br>pcs:CreateCluster<br>`                                                               |                                                                                                          |
| ListClusters           | `<br>pcs:ListClusters<br>`                                                                                                                                                                                                                                                                                                                                          |                                                                                                          |
| GetCluster             | `<br>pcs:GetCluster<br>`                                                                                                                                                                                                                                                                                                                                            | `<br>ec2:DescribeSubnets<br>`                                                                            |
| DeleteCluster          | `<br>pcs:DeleteCluster<br>`                                                                                                                                                                                                                                                                                                                                         |                                                                                                          |
| CreateComputeNodeGroup | `<br>ec2:DescribeVpcs,<br>ec2:DescribeSubnets,<br>ec2:DescribeSecurityGroups,<br>ec2:DescribeLaunchTemplates,<br>ec2:DescribeLaunchTemplateVersions,<br>ec2:DescribeInstanceTypes,<br>ec2:DescribeInstanceTypeOfferings,<br>ec2:RunInstances,<br>ec2:CreateFleet,<br>ec2:CreateTags,<br>iam:PassRole,<br>iam:GetInstanceProfile,<br>pcs:CreateComputeNodeGroup<br>` | `<br>iam:ListInstanceProfiles,<br>ec2:DescribeImages,<br>pcs:GetCluster<br>`                             |
| ListComputerNodeGroups | `<br>pcs:ListComputeNodeGroups<br>`                                                                                                                                                                                                                                                                                                                                 | `<br>pcs:GetCluster<br>`                                                                                 |
| GetComputeNodeGroup    | `<br>pcs:GetComputeNodeGroup<br>`                                                                                                                                                                                                                                                                                                                                   | `<br>ec2:DescribeSubnets<br>`                                                                            |
| UpdateComputeNodeGroup | `<br>ec2:DescribeVpcs,<br>ec2:DescribeSubnets,<br>ec2:DescribeSecurityGroups,<br>ec2:DescribeLaunchTemplates,<br>ec2:DescribeLaunchTemplateVersions,<br>ec2:DescribeInstanceTypes,<br>ec2:DescribeInstanceTypeOfferings,<br>ec2:RunInstances,<br>ec2:CreateFleet,<br>ec2:CreateTags,<br>iam:PassRole,<br>iam:GetInstanceProfile,<br>pcs:UpdateComputeNodeGroup<br>` | `<br>pcs:GetComputeNodeGroup,<br>iam:ListInstanceProfiles,<br>ec2:DescribeImages,<br>pcs:GetCluster<br>` |
| DeleteComputeNodeGroup | `<br>pcs:DeleteComputeNodeGroup<br>`                                                                                                                                                                                                                                                                                                                                |                                                                                                          |
| CreateQueue            | `<br>pcs:CreateQueue<br>`                                                                                                                                                                                                                                                                                                                                           | `<br>pcs:ListComputeNodeGroups,<br>pcs:GetCluster<br>`                                                   |
| ListQueues             | `<br>pcs:ListQueues<br>`                                                                                                                                                                                                                                                                                                                                            | `<br>pcs:GetCluster<br>`                                                                                 |
| GetQueue               | `<br>pcs:GetQueue<br>`                                                                                                                                                                                                                                                                                                                                              |                                                                                                          |
| UpdateQueue            | `<br>pcs:UpdateQueue<br>`                                                                                                                                                                                                                                                                                                                                           | `<br>pcs:ListComputeNodeGroups,<br>pcs:GetQueue<br>`                                                     |
| DeleteQueue            | `<br>pcs:DeleteQueue<br>`                                                                                                                                                                                                                                                                                                                                           |                                                                                                          |

## Minimum permissions to use tags

The following permissions are required to use tags with your resources in AWS PCS.

```
pcs:ListTagsForResource,
pcs:TagResource,
pcs:UntagResource
```

## Minimum permissions to support logs

AWS PCS sends log data to Amazon CloudWatch Logs (CloudWatch Logs). You must make sure that your identity has the minimum permissions to use CloudWatch Logs.
For more information, see [Overview
of managing access permissions to your CloudWatch Logs resources](../../../AmazonCloudWatch/latest/logs/iam-access-control-overview-cwl.md "../../../AmazonCloudWatch/latest/logs/iam-access-control-overview-cwl.md") in the _Amazon CloudWatch Logs User Guide_.

For information about permissions required for a service to send logs to CloudWatch Logs, see [Enabling logging from AWS services](../../../AmazonCloudWatch/latest/logs/AWS-logs-and-resource-policy.md#AWS-vended-logs-permissions-V2 "../../../AmazonCloudWatch/latest/logs/AWS-logs-and-resource-policy.md#AWS-vended-logs-permissions-V2") in the _Amazon CloudWatch Logs User Guide_.

## Minimum permissions to use Capacity Blocks

Amazon EC2 Capacity Blocks for ML is an Amazon EC2 purchasing option that enables you to pay in advance
to reserve GPU-based accelerated computing instances within a specific date and time range
to support short duration workloads. For more information, see [Using Amazon EC2 Capacity Blocks for ML with AWS PCS](capacity-blocks.md "capacity-blocks.md").

You choose to use Capacity Blocks when you create or update a compute node group. The IAM identity
you use to create or update the compute node group must have the following permission:

```
ec2:DescribeCapacityReservations
```

## Minimum permissions for a service administrator

The following IAM policy specifies the minimum permissions required for an IAM identity (user, group, or role) to configure and
manage the AWS PCS service.

###### Note

Users who don't configure and manage the service don't require these permissions. Users who only run jobs use secure shell (SSH) to connect to the cluster. AWS Identity and Access Management (IAM) doesn't handle authentication or authorization for SSH.

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "PCSAccess",
      "Effect": "Allow",
      "Action": [
        "pcs:*"
      ],
      "Resource": "*"
    },
    {
      "Sid": "EC2Access",
      "Effect": "Allow",
      "Action": [
        "ec2:CreateNetworkInterface",
        "ec2:DescribeImages",
        "ec2:GetSecurityGroupsForVpc",
        "ec2:DescribeSubnets",
        "ec2:DescribeSecurityGroups",
        "ec2:DescribeVpcs",
        "ec2:DescribeLaunchTemplates",
        "ec2:DescribeLaunchTemplateVersions",
        "ec2:DescribeInstanceTypes",
        "ec2:DescribeInstanceTypeOfferings",
        "ec2:RunInstances",
        "ec2:CreateFleet",
        "ec2:CreateTags",
        "ec2:DescribeCapacityReservations"
      ],
      "Resource": "*"
    },
    {
      "Sid": "IamInstanceProfile",
      "Effect": "Allow",
      "Action": [
        "iam:GetInstanceProfile"
      ],
      "Resource": "*"
    },
    {
      "Sid": "IamPassRole",
      "Effect": "Allow",
      "Action": [
        "iam:PassRole"
      ],
      "Resource": [
        "arn:aws:iam::*:role/*/AWSPCS*",
        "arn:aws:iam::*:role/AWSPCS*",
        "arn:aws:iam::*:role/aws-pcs/*",
        "arn:aws:iam::*:role/*/aws-pcs/*"
      ],
      "Condition": {
        "StringEquals": {
           "iam:PassedToService": [
             "ec2.amazonaws.com"
           ]
        }
      }
    },
    {
      "Sid": "SLRAccess",
      "Effect": "Allow",
      "Action": [
        "iam:CreateServiceLinkedRole"
      ],
      "Resource": [
        "arn:aws:iam::*:role/aws-service-role/pcs.amazonaws.com/AWSServiceRoleFor*",
        "arn:aws:iam::*:role/aws-service-role/spot.amazonaws.com/AWSServiceRoleFor*"
      ],
      "Condition": {
        "StringLike": {
          "iam:AWSServiceName": [
            "pcs.amazonaws.com",
            "spot.amazonaws.com"
          ]
        }
      }
    },
    {
      "Sid": "AccessKMSKey",
      "Effect": "Allow",
      "Action": [
        "kms:Decrypt",
        "kms:Encrypt",
        "kms:GenerateDataKey",
        "kms:CreateGrant",
        "kms:DescribeKey"
      ],
      "Resource": "*"
    },
    {
      "Sid": "SecretManagementAccess",
      "Effect": "Allow",
      "Action": [
        "secretsmanager:CreateSecret",
        "secretsmanager:TagResource",
        "secretsmanager:UpdateSecret",
        "secretsmanager:RotateSecret"
      ],
      "Resource": "*"
    },
    {
       "Sid": "ServiceLogsDelivery",
       "Effect": "Allow",
       "Action": [
         "pcs:AllowVendedLogDeliveryForResource",
         "logs:PutDeliverySource",
         "logs:PutDeliveryDestination",
         "logs:CreateDelivery"
       ],
       "Resource": "*"
    }
  ]
}
```
