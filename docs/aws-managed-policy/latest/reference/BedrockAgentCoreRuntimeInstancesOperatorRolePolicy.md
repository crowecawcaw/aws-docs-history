# BedrockAgentCoreRuntimeInstancesOperatorRolePolicy

**Description**: Provides access to create and manage compute and associated resources for Bedrock AgentCore Runtime Instances

`BedrockAgentCoreRuntimeInstancesOperatorRolePolicy` is an [AWS managed policy](../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies "../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies").

## Using this policy

You can attach `BedrockAgentCoreRuntimeInstancesOperatorRolePolicy` to your users, groups, and roles.

## Policy details

- **Type**: AWS managed policy
- **Creation time**: August 05, 2026, 11:27 UTC
- **Edited time:** August 06, 2026, 10:12 UTC
- **ARN**:
  `arn:aws:iam::aws:policy/BedrockAgentCoreRuntimeInstancesOperatorRolePolicy`

## Policy version

**Policy version:** v2 (default)

The policy's default version is the version that defines the permissions for the policy. When a user or role with the policy makes a
request to access an AWS resource, AWS checks the default version of the policy to determine whether to allow the request.

## JSON policy document

```
{
  "Version" : "2012-10-17",
  "Statement" : [
    {
      "Sid" : "DescribeComputeResources",
      "Effect" : "Allow",
      "Action" : [
        "ec2:DescribeAvailabilityZones",
        "ec2:DescribeCapacityReservations",
        "ec2:DescribeInstances",
        "ec2:DescribeInstanceStatus",
        "ec2:DescribeInstanceTypeOfferings",
        "ec2:DescribeInstanceTypes",
        "ec2:DescribeSecurityGroups",
        "ec2:DescribeSubnets",
        "ec2:DescribeVolumes",
        "ec2:DescribeLaunchTemplateVersions",
        "ec2:DescribeNetworkInterfaces",
        "autoscaling:DescribeAutoScalingInstances",
        "autoscaling:DescribeAutoScalingGroups"
      ],
      "Resource" : "*"
    },
    {
      "Sid" : "DescribeEventBridgeRule",
      "Effect" : "Allow",
      "Action" : [
        "events:DescribeRule"
      ],
      "Resource" : "arn:*:events:*:*:rule/agentcore-lifecycle-events-*"
    },
    {
      "Sid" : "CreateVolumeForManagedInstances",
      "Effect" : "Allow",
      "Action" : [
        "ec2:CreateVolume"
      ],
      "Resource" : [
        "arn:aws:ec2:*:*:volume/*"
      ],
      "Condition" : {
        "Null" : {
          "aws:RequestTag/bedrock-agentcore:capacity-provider-id" : "false"
        }
      }
    },
    {
      "Sid" : "AttachVolumeForManagedInstances",
      "Effect" : "Allow",
      "Action" : [
        "ec2:AttachVolume"
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
      "Sid" : "CreateLaunchTemplateForManagedInstances",
      "Effect" : "Allow",
      "Action" : [
        "ec2:CreateLaunchTemplate"
      ],
      "Resource" : [
        "arn:aws:ec2:*:*:launch-template/*"
      ],
      "Condition" : {
        "Null" : {
          "aws:RequestTag/bedrock-agentcore:capacity-provider-id" : "false"
        }
      }
    },
    {
      "Sid" : "ModifyLaunchTemplateForManagedInstances",
      "Effect" : "Allow",
      "Action" : [
        "ec2:CreateLaunchTemplateVersion",
        "ec2:ModifyLaunchTemplate"
      ],
      "Resource" : [
        "arn:aws:ec2:*:*:launch-template/*"
      ],
      "Condition" : {
        "StringEquals" : {
          "ec2:ManagedResourceOperator" : "bedrock-agentcore.amazonaws.com"
        }
      }
    },
    {
      "Sid" : "CreateAutoScalingForManagedInstances",
      "Effect" : "Allow",
      "Action" : [
        "autoscaling:CreateAutoScalingGroup"
      ],
      "Resource" : "arn:*:autoscaling:*:*:autoScalingGroup:*:autoScalingGroupName/agentcore-managed-instances-*",
      "Condition" : {
        "Null" : {
          "aws:RequestTag/bedrock-agentcore:capacity-provider-id" : "false"
        }
      }
    },
    {
      "Sid" : "UpdateAndLaunchAutoScaling",
      "Effect" : "Allow",
      "Action" : [
        "autoscaling:UpdateAutoScalingGroup",
        "autoscaling:PutLifecycleHook",
        "autoscaling:CompleteLifecycleAction",
        "autoscaling:LaunchInstances"
      ],
      "Resource" : "arn:*:autoscaling:*:*:autoScalingGroup:*:autoScalingGroupName/agentcore-managed-instances-*",
      "Condition" : {
        "Null" : {
          "aws:ResourceTag/bedrock-agentcore:capacity-provider-id" : "false"
        }
      }
    },
    {
      "Sid" : "NetworkingAccessForManagedInstances",
      "Effect" : "Allow",
      "Action" : [
        "ec2:RunInstances",
        "ec2:CreateNetworkInterface",
        "ec2:CreateFleet"
      ],
      "Resource" : [
        "arn:aws:ec2:*:*:subnet/*",
        "arn:aws:ec2:*:*:security-group/*"
      ]
    },
    {
      "Sid" : "AmazonAMIsAccessForManagedInstances",
      "Effect" : "Allow",
      "Action" : [
        "ec2:RunInstances",
        "ec2:CreateFleet"
      ],
      "Resource" : [
        "arn:aws:ec2:*:*:image/*"
      ],
      "Condition" : {
        "StringEquals" : {
          "ec2:Owner" : "amazon"
        }
      }
    },
    {
      "Sid" : "CreateFleetAccess",
      "Effect" : "Allow",
      "Action" : [
        "ec2:CreateFleet"
      ],
      "Resource" : [
        "arn:aws:ec2:*:*:fleet/*"
      ]
    },
    {
      "Sid" : "LaunchWithManagedLaunchTemplate",
      "Effect" : "Allow",
      "Action" : [
        "ec2:CreateFleet",
        "ec2:RunInstances"
      ],
      "Resource" : [
        "arn:aws:ec2:*:*:launch-template/*"
      ],
      "Condition" : {
        "Null" : {
          "aws:ResourceTag/bedrock-agentcore:capacity-provider-id" : "false"
        }
      }
    },
    {
      "Sid" : "ProvisionEC2InstancesForManagedInstances",
      "Effect" : "Allow",
      "Action" : [
        "ec2:CreateFleet",
        "ec2:RunInstances"
      ],
      "Resource" : [
        "arn:aws:ec2:*:*:instance/*",
        "arn:aws:ec2:*:*:network-interface/*",
        "arn:aws:ec2:*:*:volume/*"
      ],
      "Condition" : {
        "Null" : {
          "aws:RequestTag/bedrock-agentcore:capacity-provider-id" : "false"
        }
      }
    },
    {
      "Sid" : "TagOnCreateManagedResources",
      "Effect" : "Allow",
      "Action" : [
        "ec2:CreateTags"
      ],
      "Resource" : [
        "arn:aws:ec2:*:*:fleet/*",
        "arn:aws:ec2:*:*:instance/*",
        "arn:aws:ec2:*:*:network-interface/*",
        "arn:aws:ec2:*:*:volume/*",
        "arn:aws:ec2:*:*:launch-template/*"
      ],
      "Condition" : {
        "StringEquals" : {
          "ec2:CreateAction" : [
            "CreateFleet",
            "CreateLaunchTemplate",
            "RunInstances",
            "CreateVolume",
            "CreateNetworkInterface"
          ]
        }
      }
    },
    {
      "Sid" : "TagAfterCreateManagedResources",
      "Effect" : "Allow",
      "Action" : [
        "ec2:CreateTags"
      ],
      "Resource" : [
        "arn:aws:ec2:*:*:fleet/*",
        "arn:aws:ec2:*:*:instance/*",
        "arn:aws:ec2:*:*:network-interface/*",
        "arn:aws:ec2:*:*:volume/*",
        "arn:aws:ec2:*:*:launch-template/*"
      ],
      "Condition" : {
        "StringEquals" : {
          "ec2:ManagedResourceOperator" : "bedrock-agentcore.amazonaws.com"
        },
        "ForAllValues:StringLike" : {
          "aws:TagKeys" : "bedrock-agentcore:*"
        }
      }
    },
    {
      "Sid" : "AttachNetworkInterfaceToManagedInstance",
      "Effect" : "Allow",
      "Action" : [
        "ec2:AttachNetworkInterface"
      ],
      "Resource" : [
        "arn:aws:ec2:*:*:instance/*",
        "arn:aws:ec2:*:*:network-interface/*"
      ],
      "Condition" : {
        "StringEquals" : {
          "ec2:ManagedResourceOperator" : "bedrock-agentcore.amazonaws.com"
        }
      }
    },
    {
      "Sid" : "EventBridgeAccessForManagedRule",
      "Effect" : "Allow",
      "Action" : [
        "events:PutRule",
        "events:PutTargets",
        "events:RemoveTargets"
      ],
      "Resource" : "arn:*:events:*:*:rule/agentcore-lifecycle-events-*",
      "Condition" : {
        "StringEquals" : {
          "events:ManagedBy" : "bedrock-agentcore.amazonaws.com"
        }
      }
    },
    {
      "Sid" : "ServiceLinkedRoleAccessForAutoScaling",
      "Effect" : "Allow",
      "Action" : [
        "iam:CreateServiceLinkedRole"
      ],
      "Resource" : [
        "arn:aws:iam::*:role/aws-service-role/autoscaling.amazonaws.com/AWSServiceRoleForAutoScaling"
      ]
    },
    {
      "Sid" : "PassRoleToManagedInstances",
      "Effect" : "Allow",
      "Action" : [
        "iam:PassRole"
      ],
      "Resource" : [
        "arn:aws:iam::*:role/AmazonBedrockAgentCoreCapacityProviderDefaultInstanceRole*",
        "arn:aws:iam::*:role/service-role/AmazonBedrockAgentCoreCapacityProviderDefaultInstanceRole*"
      ],
      "Condition" : {
        "StringLike" : {
          "iam:PassedToService" : "ec2.*"
        }
      }
    }
  ]
}
```

## Learn more

- [Create a permission set using AWS managed policies in IAM Identity Center](../../../singlesignon/latest/userguide/howtocreatepermissionset.md "../../../singlesignon/latest/userguide/howtocreatepermissionset.md")
- [Adding and removing IAM identity permissions](../../../IAM/latest/UserGuide/access_policies_manage-attach-detach.md "../../../IAM/latest/UserGuide/access_policies_manage-attach-detach.md")
- [Understand versioning for IAM policies](../../../IAM/latest/UserGuide/access_policies_managed-versioning.md "../../../IAM/latest/UserGuide/access_policies_managed-versioning.md")
- [Get started with AWS managed policies and move toward least-privilege permissions](../../../IAM/latest/UserGuide/best-practices.md#bp-use-aws-defined-policies "../../../IAM/latest/UserGuide/best-practices.md#bp-use-aws-defined-policies")
