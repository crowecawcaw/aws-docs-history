

# AWSMarketplaceSubsidiaryAuthorizationServiceRolePolicy
<a name="AWSMarketplaceSubsidiaryAuthorizationServiceRolePolicy"></a>

**Description**: Enables AWS Marketplace to share Subsidiary Authorization entities across AWS accounts on the customer's behalf using AWS Resource Access Manager.

`AWSMarketplaceSubsidiaryAuthorizationServiceRolePolicy` is an [AWS managed policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies).

## Using this policy
<a name="AWSMarketplaceSubsidiaryAuthorizationServiceRolePolicy-how-to-use"></a>

You can attach `AWSMarketplaceSubsidiaryAuthorizationServiceRolePolicy` to your users, groups, and roles.

## Policy details
<a name="AWSMarketplaceSubsidiaryAuthorizationServiceRolePolicy-details"></a>
+ **Type**: Service role policy 
+ **Creation time**: October 26, 2026, 17:27 UTC 
+ **Edited time:** October 26, 2026, 17:27 UTC
+ **ARN**: `arn:aws:iam::aws:policy/service-role/AWSMarketplaceSubsidiaryAuthorizationServiceRolePolicy`

## Policy version
<a name="AWSMarketplaceSubsidiaryAuthorizationServiceRolePolicy-version"></a>

**Policy version:** v1 (default)

The policy's default version is the version that defines the permissions for the policy. When a user or role with the policy makes a request to access an AWS resource, AWS checks the default version of the policy to determine whether to allow the request. 

## JSON policy document
<a name="AWSMarketplaceSubsidiaryAuthorizationServiceRolePolicy-json"></a>

```
{
  "Version" : "2012-10-17",
  "Statement" : [
    {
      "Sid" : "AllowSubsidiaryAuthorizationShareActionsRAMCreate",
      "Effect" : "Allow",
      "Action" : [
        "ram:CreateResourceShare"
      ],
      "Resource" : [
        "arn:aws:ram:*:*:*"
      ],
      "Condition" : {
        "StringEquals" : {
          "ram:RequestedResourceType" : "aws-marketplace:Entity"
        },
        "ArnLike" : {
          "ram:ResourceArn" : [
            "arn:aws:aws-marketplace:*:*:*/SubsidiaryAuthorization/*"
          ]
        },
        "Null" : {
          "ram:Principal" : "true"
        }
      }
    },
    {
      "Sid" : "AllowSubsidiaryAuthorizationShareActionsRAMAssociate",
      "Effect" : "Allow",
      "Action" : [
        "ram:AssociateResourceShare"
      ],
      "Resource" : [
        "arn:aws:ram:*:*:*"
      ],
      "Condition" : {
        "Null" : {
          "ram:Principal" : "false"
        },
        "StringEquals" : {
          "ram:ResourceShareName" : "AWSMarketplaceSubsidiaryAuthorization"
        }
      }
    },
    {
      "Sid" : "AllowSubsidiaryAuthorizationShareActionsRAMAcceptDelete",
      "Effect" : "Allow",
      "Action" : [
        "ram:AcceptResourceShareInvitation",
        "ram:DeleteResourceShare"
      ],
      "Resource" : [
        "arn:aws:ram:*:*:*"
      ],
      "Condition" : {
        "StringEquals" : {
          "ram:ResourceShareName" : "AWSMarketplaceSubsidiaryAuthorization"
        }
      }
    },
    {
      "Sid" : "AllowSubsidiaryAuthorizationShareActionsRAMGet",
      "Effect" : "Allow",
      "Action" : [
        "ram:GetResourceShareInvitations",
        "ram:GetResourceShareAssociations"
      ],
      "Resource" : [
        "arn:aws:ram:*:*:*"
      ]
    },
    {
      "Sid" : "AllowSubsidiaryAuthorizationShareActionsMarketplace",
      "Effect" : "Allow",
      "Action" : [
        "aws-marketplace:PutResourcePolicy",
        "aws-marketplace:GetResourcePolicy",
        "aws-marketplace:DeleteResourcePolicy"
      ],
      "Resource" : [
        "arn:aws:aws-marketplace:*:*:*/SubsidiaryAuthorization/*"
      ],
      "Condition" : {
        "ForAnyValue:StringEquals" : {
          "aws:CalledVia" : [
            "ram.amazonaws.com"
          ]
        }
      }
    },
    {
      "Sid" : "AllowSubsidiaryAuthorizationShareActionsMarketplaceDescribe",
      "Effect" : "Allow",
      "Action" : [
        "aws-marketplace:DescribeEntity"
      ],
      "Resource" : [
        "arn:aws:aws-marketplace:*:*:*/SubsidiaryAuthorization/*"
      ]
    }
  ]
}
```

## Learn more
<a name="AWSMarketplaceSubsidiaryAuthorizationServiceRolePolicy-learn-more"></a>
+ [Create a permission set using AWS managed policies in IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/howtocreatepermissionset.html) 
+ [Adding and removing IAM identity permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-attach-detach.html) 
+ [Understand versioning for IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-versioning.html)
+ [Get started with AWS managed policies and move toward least-privilege permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#bp-use-aws-defined-policies)