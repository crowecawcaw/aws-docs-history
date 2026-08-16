# AWSBedrockAgentCoreRuntimeInstancesServiceRolePolicy

**Description**: Allows Bedrock AgentCore Runtime Instances to manage compute resources on your behalf.

`AWSBedrockAgentCoreRuntimeInstancesServiceRolePolicy` is an [AWS managed policy](../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies "../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies").

## Using this policy

This policy is attached to a service-linked role that allows the service to perform actions on
your behalf. You cannot attach this policy to your users, groups, or roles.

## Policy details

- **Type**: Service-linked role policy
- **Creation time**: August 05, 2026, 09:57 UTC
- **Edited time:** August 05, 2026, 09:57 UTC
- **ARN**:
  `arn:aws:iam::aws:policy/aws-service-role/AWSBedrockAgentCoreRuntimeInstancesServiceRolePolicy`

## Policy version

**Policy version:** v1 (default)

The policy's default version is the version that defines the permissions for the policy. When a user or role with the policy makes a
request to access an AWS resource, AWS checks the default version of the policy to determine whether to allow the request.

## JSON policy document

```
{
  "Version" : "2012-10-17",
  "Statement" : [
    {
      "Sid" : "AllowDescribeResources",
      "Effect" : "Allow",
      "Action" : [
        "ec2:DescribeInstanceStatus",
        "ec2:DescribeInstances",
        "ec2:DescribeNetworkInterfaces",
        "ec2:DescribeVolumes",
        "ec2:DescribeLaunchTemplates",
        "ec2:DescribeLaunchTemplateVersions",
        "autoscaling:DescribeAutoScalingGroups"
      ],
      "Resource" : [
        "*"
      ]
    },
    {
      "Sid" : "AllowCleanupManagedLaunchTemplate",
      "Effect" : "Allow",
      "Action" : [
        "ec2:DeleteLaunchTemplate",
        "ec2:DeleteLaunchTemplateVersions"
      ],
      "Resource" : "arn:aws:ec2:*:*:launch-template/*",
      "Condition" : {
        "StringEquals" : {
          "ec2:ManagedResourceOperator" : "bedrock-agentcore.amazonaws.com"
        }
      }
    },
    {
      "Sid" : "AllowCleanupAutoScalingGroup",
      "Effect" : "Allow",
      "Action" : [
        "autoscaling:DeleteAutoScalingGroup",
        "autoscaling:CompleteLifecycleAction"
      ],
      "Resource" : "arn:aws:autoscaling:*:*:autoScalingGroup:*",
      "Condition" : {
        "Null" : {
          "aws:ResourceTag/bedrock-agentcore:capacity-provider-id" : "false"
        }
      }
    },
    {
      "Sid" : "AllowCleanupEventBridge",
      "Effect" : "Allow",
      "Action" : [
        "events:RemoveTargets",
        "events:DeleteRule"
      ],
      "Resource" : "arn:aws:events:*:*:rule/*",
      "Condition" : {
        "StringEquals" : {
          "events:ManagedBy" : "bedrock-agentcore.amazonaws.com"
        }
      }
    },
    {
      "Sid" : "AllowCleanupEBSVolumes",
      "Effect" : "Allow",
      "Action" : [
        "ec2:DeleteVolume"
      ],
      "Resource" : [
        "arn:aws:ec2:*:*:volume/*"
      ],
      "Condition" : {
        "StringEquals" : {
          "ec2:ManagedResourceOperator" : "bedrock-agentcore.amazonaws.com"
        }
      }
    },
    {
      "Sid" : "AllowDetachEBSVolumes",
      "Effect" : "Allow",
      "Action" : [
        "ec2:DetachVolume"
      ],
      "Resource" : [
        "arn:aws:ec2:*:*:volume/*",
        "arn:aws:ec2:*:*:instance/*"
      ],
      "Condition" : {
        "StringEquals" : {
          "ec2:ManagedResourceOperator" : "bedrock-agentcore.amazonaws.com"
        }
      }
    },
    {
      "Sid" : "AllowTerminateManagedInstances",
      "Effect" : "Allow",
      "Action" : [
        "ec2:TerminateInstances"
      ],
      "Resource" : [
        "arn:aws:ec2:*:*:instance/*"
      ],
      "Condition" : {
        "StringEquals" : {
          "ec2:ManagedResourceOperator" : "bedrock-agentcore.amazonaws.com"
        }
      }
    }
  ]
}
```

## Learn more

- [Understand versioning for IAM policies](../../../IAM/latest/UserGuide/access_policies_managed-versioning.md "../../../IAM/latest/UserGuide/access_policies_managed-versioning.md")
- [Get started with AWS managed policies and move toward least-privilege permissions](../../../IAM/latest/UserGuide/best-practices.md#bp-use-aws-defined-policies "../../../IAM/latest/UserGuide/best-practices.md#bp-use-aws-defined-policies")
