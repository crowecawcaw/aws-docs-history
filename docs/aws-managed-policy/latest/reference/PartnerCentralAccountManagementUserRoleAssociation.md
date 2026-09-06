

# PartnerCentralAccountManagementUserRoleAssociation
<a name="PartnerCentralAccountManagementUserRoleAssociation"></a>

**Description**: Provides access to associate and dissociate partner central users with IAM roles

`PartnerCentralAccountManagementUserRoleAssociation` is an [AWS managed policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies).

## Using this policy
<a name="PartnerCentralAccountManagementUserRoleAssociation-how-to-use"></a>

You can attach `PartnerCentralAccountManagementUserRoleAssociation` to your users, groups, and roles.

## Policy details
<a name="PartnerCentralAccountManagementUserRoleAssociation-details"></a>
+ **Type**: AWS managed policy 
+ **Creation time**: November 10, 2023, 02:03 UTC 
+ **Edited time:** November 10, 2023, 02:03 UTC
+ **ARN**: `arn:aws:iam::aws:policy/PartnerCentralAccountManagementUserRoleAssociation`

## Policy version
<a name="PartnerCentralAccountManagementUserRoleAssociation-version"></a>

**Policy version:** v1 (default)

The policy's default version is the version that defines the permissions for the policy. When a user or role with the policy makes a request to access an AWS resource, AWS checks the default version of the policy to determine whether to allow the request. 

## JSON policy document
<a name="PartnerCentralAccountManagementUserRoleAssociation-json"></a>

```
{
  "Version" : "2012-10-17",
  "Statement" : [
    {
      "Sid" : "PassPartnerCentralRole",
      "Effect" : "Allow",
      "Action" : [
        "iam:PassRole"
      ],
      "Resource" : "arn:aws:iam::*:role/PartnerCentralRoleFor*",
      "Condition" : {
        "StringEquals" : {
          "iam:PassedToService" : "partnercentral-account-management.amazonaws.com"
        }
      }
    },
    {
      "Sid" : "PartnerUserRoleAssociation",
      "Effect" : "Allow",
      "Action" : [
        "iam:ListRoles",
        "partnercentral-account-management:AssociatePartnerUser",
        "partnercentral-account-management:DisassociatePartnerUser"
      ],
      "Resource" : "*"
    }
  ]
}
```

## Learn more
<a name="PartnerCentralAccountManagementUserRoleAssociation-learn-more"></a>
+ [Create a permission set using AWS managed policies in IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/howtocreatepermissionset.html) 
+ [Adding and removing IAM identity permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-attach-detach.html) 
+ [Understand versioning for IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-versioning.html)
+ [Get started with AWS managed policies and move toward least-privilege permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#bp-use-aws-defined-policies)