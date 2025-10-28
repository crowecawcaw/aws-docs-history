# General examples

## Deny access to AWS based on the requested

AWS Region

###### Topics

This SCP denies access to any operations outside of the specified Regions. Replace
`eu-central-1` and `eu-west-1` with the AWS Regions you want
to use. It provides exemptions for operations in approved global services. This example
also shows how to exempt requests made by either of two specified administrator roles.

###### Note

To use the Region deny SCP with AWS Control Tower, see [Deny access to AWS based on the requested AWS Region](../../../controltower/latest/controlreference/primary-region-deny-policy.md "../../../controltower/latest/controlreference/primary-region-deny-policy.md") in the _AWS Control Tower Controls Reference Guide_.

This policy uses the `Deny` effect to deny access to all requests for
operations that don't target one of the two approved regions (`eu-central-1`
and `eu-west-1`). The [NotAction](../../../IAM/latest/UserGuide/reference_policies_elements_notaction.md "../../../IAM/latest/UserGuide/reference_policies_elements_notaction.md")
element enables you to list services whose operations (or individual operations) are
exempted from this restriction. Because global services have endpoints that are
physically hosted by the `us-east-1` Region , they must be exempted in this
way. With an SCP structured this way, requests made to global services in the
`us-east-1` Region are allowed if the requested service is included in
the `NotAction` element. Any other requests to services in the
`us-east-1` Region are denied by this example policy.

###### Note

**_This example might not include all
of the latest global AWS services or operations._**
Replace the list of services and operations with the global services used by
accounts in your organization.

###### Tip

You can view the [service last accessed data in the IAM console](../../../IAM/latest/UserGuide/access_policies_access-advisor.md "../../../IAM/latest/UserGuide/access_policies_access-advisor.md") to determine what
global services your organization uses. The **Access Advisor**
tab on the details page for an IAM user, group, or role displays the AWS
services that have been used by that entity, sorted by most recent access.

###### Considerations

- AWS KMS and AWS Certificate Manager support Regional endpoints. However, if you want to
  use them with a global service such as Amazon CloudFront you must include them in the
  global service exclusion list in the following example SCP. A global service
  like Amazon CloudFront typically requires access to AWS KMS and ACM in the same
  region, which for a global service is the US East (N. Virginia) Region
  (`us-east-1`).
- By default, AWS STS is a global service and must be included in the global
  service exclusion list. However, you can enable AWS STS to use Region
  endpoints instead of a single global endpoint. If you do this, you can
  remove STS from the global service exemption list in the following example
  SCP. For more information see [Managing AWS STS in an AWS Region](../../../IAM/latest/UserGuide/id_credentials_temp_enable-regions.md "../../../IAM/latest/UserGuide/id_credentials_temp_enable-regions.md").

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "DenyAllOutsideEU",
            "Effect": "Deny",
            "NotAction": [
                "a4b:*",
                "acm:*",
                "aws-marketplace-management:*",
                "aws-marketplace:*",
                "aws-portal:*",
                "budgets:*",
                "ce:*",
                "chime:*",
                "cloudfront:*",
                "config:*",
                "cur:*",
                "directconnect:*",
                "ec2:DescribeRegions",
                "ec2:DescribeTransitGateways",
                "ec2:DescribeVpnGateways",
                "fms:*",
                "globalaccelerator:*",
                "health:*",
                "iam:*",
                "importexport:*",
                "kms:*",
                "mobileanalytics:*",
                "networkmanager:*",
                "organizations:*",
                "pricing:*",
                "route53:*",
                "route53domains:*",
                "route53-recovery-cluster:*",
                "route53-recovery-control-config:*",
                "route53-recovery-readiness:*",
                "s3:GetAccountPublic*",
                "s3:ListAllMyBuckets",
                "s3:ListMultiRegionAccessPoints",
                "s3:PutAccountPublic*",
                "shield:*",
                "sts:*",
                "support:*",
                "trustedadvisor:*",
                "waf-regional:*",
                "waf:*",
                "wafv2:*",
                "wellarchitected:*"
            ],
            "Resource": "*",
            "Condition": {
                "StringNotEquals": {
                    "aws:RequestedRegion": [
                        "eu-central-1",
                        "eu-west-1"
                    ]
                },
                "ArnNotLike": {
                    "aws:PrincipalARN": [
                        "arn:aws:iam::*:role/Role1AllowedToBypassThisSCP",
                        "arn:aws:iam::*:role/Role2AllowedToBypassThisSCP"
                    ]
                }
            }
        }
    ]
}
```

## Prevent IAM users and roles

from making certain changes

This SCP restricts IAM users and roles from making changes to the specified IAM
role that you created in all accounts in your organization.

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "DenyAccessToASpecificRole",
      "Effect": "Deny",
      "Action": [
        "iam:AttachRolePolicy",
        "iam:DeleteRole",
        "iam:DeleteRolePermissionsBoundary",
        "iam:DeleteRolePolicy",
        "iam:DetachRolePolicy",
        "iam:PutRolePermissionsBoundary",
        "iam:PutRolePolicy",
        "iam:UpdateAssumeRolePolicy",
        "iam:UpdateRole",
        "iam:UpdateRoleDescription"
      ],
      "Resource": [
        "arn:aws:iam::*:role/name-of-role-to-deny"
      ]
    }
  ]
}
```

## Prevent IAM users and roles

from making specified changes, with an exception for a specified admin role

This SCP builds on the previous example to make an exception for administrators. It
prevents IAM users and roles in affected accounts from making changes to a common
administrative IAM role created in all accounts in your organization
_except_ for administrators using a specified role.

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "DenyAccessWithException",
      "Effect": "Deny",
      "Action": [
        "iam:AttachRolePolicy",
        "iam:DeleteRole",
        "iam:DeleteRolePermissionsBoundary",
        "iam:DeleteRolePolicy",
        "iam:DetachRolePolicy",
        "iam:PutRolePermissionsBoundary",
        "iam:PutRolePolicy",
        "iam:UpdateAssumeRolePolicy",
        "iam:UpdateRole",
        "iam:UpdateRoleDescription"
      ],
      "Resource": [
        "arn:aws:iam::*:role/name-of-role-to-deny"
      ],
      "Condition": {
        "ArnNotLike": {
          "aws:PrincipalARN":"arn:aws:iam::*:role/name-of-admin-role-to-allow"
        }
      }
    }
  ]
}
```

## Require MFA to perform an API operation

Use an SCP like the following to require that multi-factor authentication (MFA) is
enabled before an IAM user or role can perform an action. In this example, the action
is to stop an Amazon EC2 instance.

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "DenyStopAndTerminateWhenMFAIsNotPresent",
      "Effect": "Deny",
      "Action": [
        "ec2:StopInstances",
        "ec2:TerminateInstances"
      ],
      "Resource": "*",
      "Condition": {"BoolIfExists": {"aws:MultiFactorAuthPresent": false}}
    }
  ]
}
```

## Block service access for the root user

The following policy restricts all access to the specified actions for the [root user](../../../IAM/latest/UserGuide/id_root-user.md "../../../IAM/latest/UserGuide/id_root-user.md") in a member account. If you
want to prevent your accounts from using root credentials in specific ways, add your own
actions to this policy.

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "RestrictEC2ForRoot",
      "Effect": "Deny",
      "Action": [
        "ec2:*"
      ],
      "Resource": [
        "*"
      ],
      "Condition": {
        "StringLike": {
          "aws:PrincipalArn": [
            "arn:aws:iam::*:root"
          ]
        }
      }
    }
  ]
}
```

## Prevent member accounts from leaving the

organization

The following policy blocks use of the `LeaveOrganization` API operation so
that administrators of member accounts can't remove their accounts from the
organization.

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Deny",
            "Action": [
                "organizations:LeaveOrganization"
            ],
            "Resource": "*"
        }
    ]
}
```
