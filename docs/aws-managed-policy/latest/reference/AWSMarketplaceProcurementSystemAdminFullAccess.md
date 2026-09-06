

# AWSMarketplaceProcurementSystemAdminFullAccess
<a name="AWSMarketplaceProcurementSystemAdminFullAccess"></a>

**Description**: Provides full access to all administrative actions for an AWS Marketplace eProcurement integration.

`AWSMarketplaceProcurementSystemAdminFullAccess` is an [AWS managed policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies).

## Using this policy
<a name="AWSMarketplaceProcurementSystemAdminFullAccess-how-to-use"></a>

You can attach `AWSMarketplaceProcurementSystemAdminFullAccess` to your users, groups, and roles.

## Policy details
<a name="AWSMarketplaceProcurementSystemAdminFullAccess-details"></a>
+ **Type**: AWS managed policy 
+ **Creation time**: June 25, 2019, 13:07 UTC 
+ **Edited time:** April 21, 2026, 22:27 UTC
+ **ARN**: `arn:aws:iam::aws:policy/AWSMarketplaceProcurementSystemAdminFullAccess`

## Policy version
<a name="AWSMarketplaceProcurementSystemAdminFullAccess-version"></a>

**Policy version:** v2 (default)

The policy's default version is the version that defines the permissions for the policy. When a user or role with the policy makes a request to access an AWS resource, AWS checks the default version of the policy to determine whether to allow the request. 

## JSON policy document
<a name="AWSMarketplaceProcurementSystemAdminFullAccess-json"></a>

```
{
  "Version" : "2012-10-17",
  "Statement" : [
    {
      "Effect" : "Allow",
      "Action" : [
        "aws-marketplace:PutProcurementSystemConfiguration",
        "aws-marketplace:DescribeProcurementSystemConfiguration",
        "organizations:Describe*",
        "organizations:List*",
        "invoicing:CreateProcurementPortalPreference",
        "invoicing:GetProcurementPortalPreference",
        "invoicing:ListProcurementPortalPreferences"
      ],
      "Resource" : [
        "*"
      ]
    }
  ]
}
```

## Learn more
<a name="AWSMarketplaceProcurementSystemAdminFullAccess-learn-more"></a>
+ [Create a permission set using AWS managed policies in IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/howtocreatepermissionset.html) 
+ [Adding and removing IAM identity permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-attach-detach.html) 
+ [Understand versioning for IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-versioning.html)
+ [Get started with AWS managed policies and move toward least-privilege permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#bp-use-aws-defined-policies)