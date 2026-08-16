# AWSSDMPServiceRolePolicy

**Description**: Allow SDMP to create and manage resources on behalf of the customer.

`AWSSDMPServiceRolePolicy` is an [AWS managed policy](../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies "../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies").

## Using this policy

This policy is attached to a service-linked role that allows the service to perform actions on
your behalf. You cannot attach this policy to your users, groups, or roles.

## Policy details

- **Type**: Service-linked role policy
- **Creation time**: July 24, 2026, 20:57 UTC
- **Edited time:** August 10, 2026, 22:27 UTC
- **ARN**:
  `arn:aws:iam::aws:policy/aws-service-role/AWSSDMPServiceRolePolicy`

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
      "Sid" : "ManageServiceLinkedChannel",
      "Effect" : "Allow",
      "Action" : [
        "cloudtrail:CreateServiceLinkedChannel",
        "cloudtrail:GetServiceLinkedChannel",
        "cloudtrail:UpdateServiceLinkedChannel",
        "cloudtrail:DeleteServiceLinkedChannel"
      ],
      "Resource" : "arn:aws:cloudtrail:*:*:channel/aws-service-channel/sdmp/*",
      "Condition" : {
        "StringEquals" : {
          "aws:ResourceAccount" : "${aws:PrincipalAccount}"
        }
      }
    },
    {
      "Sid" : "AllowListOperations",
      "Effect" : "Allow",
      "Action" : [
        "cloudtrail:ListServiceLinkedChannels",
        "iam:ListPolicies",
        "iam:ListPolicyTags",
        "iam:ListRoles",
        "account:ListRegions"
      ],
      "Resource" : "*"
    },
    {
      "Sid" : "CreateRoleWithConditions",
      "Effect" : "Allow",
      "Action" : [
        "iam:AttachRolePolicy",
        "iam:CreateRole",
        "iam:PutRolePolicy"
      ],
      "Resource" : "arn:aws:iam::*:role/SDMP-*",
      "Condition" : {
        "ArnEquals" : {
          "iam:PermissionsBoundary" : "arn:aws:iam::aws:policy/AWSDenyAll"
        },
        "StringEquals" : {
          "aws:ResourceAccount" : "${aws:PrincipalAccount}"
        },
        "StringLike" : {
          "aws:ResourceTag/CreatedBy" : "arn:aws:iam::*:role/SDMPServiceRole*"
        }
      }
    },
    {
      "Sid" : "AllowSDMPRoleTagging",
      "Effect" : "Allow",
      "Action" : "iam:TagRole",
      "Resource" : "arn:aws:iam::*:role/SDMP-*",
      "Condition" : {
        "ForAllValues:StringEquals" : {
          "aws:TagKeys" : [
            "CreatedBy"
          ]
        }
      }
    },
    {
      "Sid" : "AttachAWSDenyAll",
      "Effect" : "Allow",
      "Action" : "iam:AttachRolePolicy",
      "Resource" : "arn:aws:iam::*:role/SDMP-*",
      "Condition" : {
        "ArnEquals" : {
          "iam:PolicyARN" : "arn:aws:iam::aws:policy/AWSDenyAll"
        },
        "StringLike" : {
          "aws:ResourceTag/CreatedBy" : "arn:aws:iam::*:role/SDMPServiceRole*"
        },
        "StringEquals" : {
          "aws:ResourceAccount" : "${aws:PrincipalAccount}"
        }
      }
    },
    {
      "Sid" : "ReadSDMPRoles",
      "Effect" : "Allow",
      "Action" : [
        "iam:GetRole",
        "iam:GetRolePolicy",
        "iam:ListRoleTags",
        "iam:ListRolePolicies",
        "iam:ListAttachedRolePolicies"
      ],
      "Resource" : [
        "arn:aws:iam::*:role/SDMP-*",
        "arn:aws:iam::*:role/SDMPServiceRole*",
        "arn:aws:iam::*:role/aws-service-role/sdmp.amazonaws.com/AWSServiceRoleForSDMP"
      ]
    },
    {
      "Sid" : "ReadSDMPPolicies",
      "Effect" : "Allow",
      "Action" : [
        "iam:GetPolicy",
        "iam:GetPolicyVersion",
        "iam:ListPolicyVersions"
      ],
      "Resource" : [
        "arn:aws:iam::*:policy/SDMP*"
      ]
    },
    {
      "Sid" : "AllowSecurityServiceVerification",
      "Effect" : "Allow",
      "Action" : [
        "guardduty:ListDetectors",
        "guardduty:GetDetector",
        "macie2:GetMacieSession",
        "config:DescribeConfigurationRecorders",
        "config:DescribeConfigurationRecorderStatus",
        "securityhub:DescribeHub",
        "securityhub:ListFindingAggregators",
        "inspector2:BatchGetAccountStatus",
        "detective:ListGraphs",
        "cloudtrail:DescribeTrails",
        "cloudtrail:GetTrailStatus"
      ],
      "Resource" : "*"
    }
  ]
}
```

## Learn more

- [Understand versioning for IAM policies](../../../IAM/latest/UserGuide/access_policies_managed-versioning.md "../../../IAM/latest/UserGuide/access_policies_managed-versioning.md")
- [Get started with AWS managed policies and move toward least-privilege permissions](../../../IAM/latest/UserGuide/best-practices.md#bp-use-aws-defined-policies "../../../IAM/latest/UserGuide/best-practices.md#bp-use-aws-defined-policies")
