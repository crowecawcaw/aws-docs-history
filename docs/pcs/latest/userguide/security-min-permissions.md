

# Minimum permissions for AWS PCS
<a name="security-min-permissions"></a>

This section describes the minimum IAM permissions required for an IAM identity (user, group, or role) to use the service.

**Contents**
+ [Minimum permissions to use API actions](#security-min-permissions_api)
+ [Minimum permissions to use tags](#security-min-permissions_tagging)
+ [Minimum permissions to support logs](#security-min-permissions_logging)
+ [Minimum permissions to use Capacity Blocks](#security-min-permissions_capacity-blocks)
+ [Minimum permissions for a service administrator](#security-min-permissions_admin-policy)

## Minimum permissions to use API actions
<a name="security-min-permissions_api"></a>


| API action | Minimum permissions | Additional permissions for the console | 
| --- | --- | --- | 
| CreateCluster |  <pre>ec2:CreateNetworkInterface,<br />ec2:DescribeVpcs,<br />ec2:DescribeSubnets,<br />ec2:DescribeSecurityGroups, <br />ec2:GetSecurityGroupsForVpc, <br />iam:CreateServiceLinkedRole,<br />secretsmanager:CreateSecret,<br />secretsmanager:TagResource,<br />secretsmanager:RotateSecret,<br />pcs:CreateCluster</pre>  |  | 
| ListClusters |  <pre>pcs:ListClusters</pre>  |  | 
| GetCluster |  <pre>pcs:GetCluster</pre>  |  <pre>ec2:DescribeSubnets</pre>  | 
| DeleteCluster |  <pre>pcs:DeleteCluster</pre>  |  | 
| CreateComputeNodeGroup |  <pre>ec2:DescribeVpcs,<br />ec2:DescribeSubnets,<br />ec2:DescribeSecurityGroups,<br />ec2:DescribeLaunchTemplates,<br />ec2:DescribeLaunchTemplateVersions,<br />ec2:DescribeInstanceTypes,<br />ec2:DescribeInstanceTypeOfferings,<br />ec2:RunInstances,<br />ec2:CreateFleet,<br />ec2:CreateTags,<br />iam:PassRole,<br />iam:GetInstanceProfile,<br />pcs:CreateComputeNodeGroup</pre>  |  <pre>iam:ListInstanceProfiles,<br />ec2:DescribeImages,<br />pcs:GetCluster</pre>  | 
| ListComputerNodeGroups |  <pre>pcs:ListComputeNodeGroups</pre>  |  <pre>pcs:GetCluster</pre>  | 
| GetComputeNodeGroup |  <pre>pcs:GetComputeNodeGroup</pre>  |  <pre>ec2:DescribeSubnets</pre>  | 
| UpdateComputeNodeGroup |  <pre>ec2:DescribeVpcs,<br />ec2:DescribeSubnets,<br />ec2:DescribeSecurityGroups,<br />ec2:DescribeLaunchTemplates,<br />ec2:DescribeLaunchTemplateVersions,<br />ec2:DescribeInstanceTypes,<br />ec2:DescribeInstanceTypeOfferings,<br />ec2:RunInstances,<br />ec2:CreateFleet,<br />ec2:CreateTags,<br />iam:PassRole,<br />iam:GetInstanceProfile,<br />pcs:UpdateComputeNodeGroup</pre>  |  <pre>pcs:GetComputeNodeGroup,<br />iam:ListInstanceProfiles,<br />ec2:DescribeImages,<br />pcs:GetCluster</pre>  | 
| DeleteComputeNodeGroup |  <pre>pcs:DeleteComputeNodeGroup</pre>  |  | 
| CreateQueue |  <pre>pcs:CreateQueue</pre>  |  <pre>pcs:ListComputeNodeGroups,<br />pcs:GetCluster</pre>  | 
| ListQueues |  <pre>pcs:ListQueues</pre>  |  <pre>pcs:GetCluster</pre>  | 
| GetQueue |  <pre>pcs:GetQueue</pre>  |  | 
| UpdateQueue |  <pre>pcs:UpdateQueue</pre>  |  <pre>pcs:ListComputeNodeGroups,<br />pcs:GetQueue</pre>  | 
| DeleteQueue |  <pre>pcs:DeleteQueue</pre>  |  | 

## Minimum permissions to use tags
<a name="security-min-permissions_tagging"></a>

 The following permissions are required to use tags with your resources in AWS PCS. 

```
pcs:ListTagsForResource,
pcs:TagResource,
pcs:UntagResource
```

## Minimum permissions to support logs
<a name="security-min-permissions_logging"></a>

AWS PCS sends log data to Amazon CloudWatch Logs (CloudWatch Logs). You must make sure that your identity has the minimum permissions to use CloudWatch Logs. For more information, see [Overview of managing access permissions to your CloudWatch Logs resources](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/iam-access-control-overview-cwl.html) in the *Amazon CloudWatch Logs User Guide*.

For information about permissions required for a service to send logs to CloudWatch Logs, see [Enabling logging from AWS services](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/AWS-logs-and-resource-policy.html#AWS-vended-logs-permissions-V2) in the *Amazon CloudWatch Logs User Guide*.

## Minimum permissions to use Capacity Blocks
<a name="security-min-permissions_capacity-blocks"></a>

Amazon EC2 Capacity Blocks for ML is an Amazon EC2 purchasing option that enables you to pay in advance to reserve GPU-based accelerated computing instances within a specific date and time range to support short duration workloads. For more information, see [Using Amazon EC2 Capacity Blocks for ML with AWS PCS](capacity-blocks.md).

You choose to use Capacity Blocks when you create or update a compute node group. The IAM identity you use to create or update the compute node group must have the following permissions:

```
ec2:DescribeCapacityReservations,
ec2:DescribeCapacityBlocks,
ec2:DescribeCapacityBlockStatus
```

## Minimum permissions for a service administrator
<a name="security-min-permissions_admin-policy"></a>

The following IAM policy specifies the minimum permissions required for an IAM identity (user, group, or role) to configure and manage the AWS PCS service.

**Note**  
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
        "ec2:DescribeCapacityReservations",
        "ec2:DescribeCapacityBlocks",
        "ec2:DescribeCapacityBlockStatus"
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