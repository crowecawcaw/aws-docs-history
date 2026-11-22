

# KiroVpcConnectionPolicy

**Description**: Provides Kiro access to read your Amazon VPC configuration and to create and manage the network interfaces that connect Kiro environments to your VPC.

`KiroVpcConnectionPolicy` is an [AWS managed policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies).

## Using this policy
<a name="KiroVpcConnectionPolicy-how-to-use"></a>

You can attach `KiroVpcConnectionPolicy` to your users, groups, and roles.

## Policy details
<a name="KiroVpcConnectionPolicy-details"></a>
+ **Type**: AWS managed policy 
+ **Creation time**: November 16, 2026, 23:27 UTC 
+ **Edited time:** November 16, 2026, 23:27 UTC
+ **ARN**: `arn:aws:iam::aws:policy/KiroVpcConnectionPolicy`

## Policy version
<a name="KiroVpcConnectionPolicy-version"></a>

**Policy version:** v1 (default)

The policy's default version is the version that defines the permissions for the policy. When a user or role with the policy makes a request to access an AWS resource, AWS checks the default version of the policy to determine whether to allow the request. 

## JSON policy document
<a name="KiroVpcConnectionPolicy-json"></a>

```json
{
  "Version" : "2012-10-17",
  "Statement" : [
    {
      "Sid" : "ReadVpcConfiguration",
      "Effect" : "Allow",
      "Action" : [
        "ec2:DescribeVpcs",
        "ec2:DescribeSubnets",
        "ec2:DescribeSecurityGroups",
        "ec2:DescribeNetworkInterfaces",
        "ec2:DescribeDhcpOptions"
      ],
      "Resource" : "*"
    },
    {
      "Sid" : "CreateKiroNetworkInterface",
      "Effect" : "Allow",
      "Action" : "ec2:CreateNetworkInterface",
      "Resource" : "arn:aws:ec2:*:*:network-interface/*",
      "Condition" : {
        "StringEquals" : {
          "aws:RequestTag/ManagedByKiro" : ""
        },
        "ForAllValues:StringEquals" : {
          "aws:TagKeys" : [
            "ManagedByKiro"
          ]
        }
      }
    },
    {
      "Sid" : "UseSubnetAndSecurityGroupForKiroNetworkInterface",
      "Effect" : "Allow",
      "Action" : "ec2:CreateNetworkInterface",
      "Resource" : [
        "arn:aws:ec2:*:*:subnet/*",
        "arn:aws:ec2:*:*:security-group/*"
      ]
    },
    {
      "Sid" : "TagKiroNetworkInterfaceOnCreate",
      "Effect" : "Allow",
      "Action" : "ec2:CreateTags",
      "Resource" : "arn:aws:ec2:*:*:network-interface/*",
      "Condition" : {
        "StringEquals" : {
          "ec2:CreateAction" : "CreateNetworkInterface",
          "aws:RequestTag/ManagedByKiro" : ""
        },
        "ForAllValues:StringEquals" : {
          "aws:TagKeys" : [
            "ManagedByKiro"
          ]
        }
      }
    },
    {
      "Sid" : "AllowAttachOfKiroNetworkInterface",
      "Effect" : "Allow",
      "Action" : "ec2:CreateNetworkInterfacePermission",
      "Resource" : "arn:aws:ec2:*:*:network-interface/*",
      "Condition" : {
        "StringEquals" : {
          "aws:ResourceTag/ManagedByKiro" : "",
          "ec2:Permission" : "INSTANCE-ATTACH"
        }
      }
    },
    {
      "Sid" : "DeleteKiroNetworkInterface",
      "Effect" : "Allow",
      "Action" : "ec2:DeleteNetworkInterface",
      "Resource" : "arn:aws:ec2:*:*:network-interface/*",
      "Condition" : {
        "StringEquals" : {
          "aws:ResourceTag/ManagedByKiro" : ""
        }
      }
    },
    {
      "Sid" : "ModifyKiroNetworkInterfaceAttribute",
      "Effect" : "Allow",
      "Action" : "ec2:ModifyNetworkInterfaceAttribute",
      "Resource" : "arn:aws:ec2:*:*:network-interface/*",
      "Condition" : {
        "StringEquals" : {
          "aws:ResourceTag/ManagedByKiro" : ""
        }
      }
    },
    {
      "Sid" : "ModifyNetworkInterfaceAttributeOnEnvironmentInstance",
      "Effect" : "Allow",
      "Action" : "ec2:ModifyNetworkInterfaceAttribute",
      "Resource" : "arn:aws:ec2:*:*:instance/*"
    }
  ]
}
```

## Learn more
<a name="KiroVpcConnectionPolicy-learn-more"></a>
+ [Create a permission set using AWS managed policies in IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/howtocreatepermissionset.html) 
+ [Adding and removing IAM identity permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-attach-detach.html) 
+ [Understand versioning for IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-versioning.html)
+ [Get started with AWS managed policies and move toward least-privilege permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#bp-use-aws-defined-policies)