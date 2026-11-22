

# AWSAccountAccessManagerAdministrator

**Description**: Provides administrative access to AWS Account Access Manager, including managing applications and entitlements, and setting up the service across an organization (enabling service access and registering a delegated administrator). Includes the IAM Identity Center, Identity Store, AWS Organizations, and AWS KMS permissions required to administer the service.

`AWSAccountAccessManagerAdministrator` is an [AWS managed policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies).

## Using this policy
<a name="AWSAccountAccessManagerAdministrator-how-to-use"></a>

You can attach `AWSAccountAccessManagerAdministrator` to your users, groups, and roles.

## Policy details
<a name="AWSAccountAccessManagerAdministrator-details"></a>
+ **Type**: AWS managed policy 
+ **Creation time**: November 18, 2026, 21:37 UTC 
+ **Edited time:** November 18, 2026, 21:37 UTC
+ **ARN**: `arn:aws:iam::aws:policy/AWSAccountAccessManagerAdministrator`

## Policy version
<a name="AWSAccountAccessManagerAdministrator-version"></a>

**Policy version:** v1 (default)

The policy's default version is the version that defines the permissions for the policy. When a user or role with the policy makes a request to access an AWS resource, AWS checks the default version of the policy to determine whether to allow the request. 

## JSON policy document
<a name="AWSAccountAccessManagerAdministrator-json"></a>

```json
{
  "Version" : "2012-10-17",
  "Statement" : [
    {
      "Sid" : "AccountAccessManagerApplicationPermissions",
      "Effect" : "Allow",
      "Action" : [
        "account-access:CreateApplication",
        "account-access:ListApplications"
      ],
      "Resource" : "*"
    },
    {
      "Sid" : "AccountAccessManagerApplicationResourcePermissions",
      "Effect" : "Allow",
      "Action" : [
        "account-access:DeleteApplication",
        "account-access:GetApplication"
      ],
      "Resource" : "arn:aws:account-access:*:*:application/*"
    },
    {
      "Sid" : "AccountAccessManagerEntitlementPermissions",
      "Effect" : "Allow",
      "Action" : [
        "account-access:CreateEntitlement",
        "account-access:DeleteEntitlement",
        "account-access:GetEntitlement",
        "account-access:ListEntitlements"
      ],
      "Resource" : "arn:aws:account-access:*:*:application/*"
    },
    {
      "Sid" : "AccountAccessManagerTagPermissions",
      "Effect" : "Allow",
      "Action" : [
        "account-access:ListTagsForResource",
        "account-access:TagResource",
        "account-access:UntagResource"
      ],
      "Resource" : "arn:aws:account-access:*:*:application/*"
    },
    {
      "Sid" : "IdentityCenterReadPermissions",
      "Effect" : "Allow",
      "Action" : [
        "sso:DescribeApplication",
        "sso:DescribeInstance"
      ],
      "Resource" : [
        "arn:aws:sso:::instance/*",
        "arn:aws:sso::*:application/*/*"
      ]
    },
    {
      "Sid" : "IdentityCenterListPermissions",
      "Effect" : "Allow",
      "Action" : [
        "sso:DescribeRegion",
        "sso:ListApplications",
        "sso:ListInstances"
      ],
      "Resource" : "*"
    },
    {
      "Sid" : "IdentityCenterCreateApplicationViaService",
      "Effect" : "Allow",
      "Action" : "sso:CreateApplication",
      "Resource" : "*",
      "Condition" : {
        "Bool" : {
          "aws:ViaAWSService" : "true"
        }
      }
    },
    {
      "Sid" : "IdentityCenterApplicationManagementViaService",
      "Effect" : "Allow",
      "Action" : [
        "sso:DeleteApplication",
        "sso:PutApplicationAccessScope",
        "sso:PutApplicationAssignmentConfiguration",
        "sso:PutApplicationAuthenticationMethod",
        "sso:PutApplicationGrant"
      ],
      "Resource" : "arn:aws:sso::*:application/*/*",
      "Condition" : {
        "Bool" : {
          "aws:ViaAWSService" : "true"
        }
      }
    },
    {
      "Sid" : "IdentityStoreDescribePermissions",
      "Effect" : "Allow",
      "Action" : [
        "identitystore:DescribeGroup",
        "identitystore:DescribeUser"
      ],
      "Resource" : [
        "arn:aws:identitystore::*:identitystore/*",
        "arn:aws:identitystore:::user/*",
        "arn:aws:identitystore:::group/*"
      ]
    },
    {
      "Sid" : "IdentityStoreListPermissions",
      "Effect" : "Allow",
      "Action" : [
        "identitystore:ListGroupMemberships",
        "identitystore:ListGroups",
        "identitystore:ListUsers"
      ],
      "Resource" : "*"
    },
    {
      "Sid" : "IdentityStoreDirectoryConsolePermissions",
      "Effect" : "Allow",
      "Action" : [
        "sso-directory:DescribeGroup",
        "sso-directory:DescribeGroups",
        "sso-directory:DescribeUser",
        "sso-directory:DescribeUsers",
        "sso-directory:ListGroupsForUser",
        "sso-directory:ListMembersInGroup",
        "sso-directory:SearchGroups",
        "sso-directory:SearchUsers"
      ],
      "Resource" : "*"
    },
    {
      "Sid" : "OrganizationsAccountReadPermissions",
      "Effect" : "Allow",
      "Action" : [
        "organizations:DescribeAccount",
        "organizations:ListDelegatedServicesForAccount"
      ],
      "Resource" : "arn:aws:organizations::*:account/o-*/*"
    },
    {
      "Sid" : "OrganizationsPermissions",
      "Effect" : "Allow",
      "Action" : [
        "organizations:DescribeOrganization",
        "organizations:ListAccounts",
        "organizations:ListAWSServiceAccessForOrganization",
        "organizations:ListDelegatedAdministrators",
        "organizations:ListRoots"
      ],
      "Resource" : "*"
    },
    {
      "Sid" : "OrganizationsParentReadPermissions",
      "Effect" : "Allow",
      "Action" : [
        "organizations:ListAccountsForParent",
        "organizations:ListOrganizationalUnitsForParent"
      ],
      "Resource" : [
        "arn:aws:organizations::*:root/o-*/r-*",
        "arn:aws:organizations::*:ou/o-*/ou-*"
      ]
    },
    {
      "Sid" : "AccountAccessManagerManageDelegatedAdministratorPermissions",
      "Effect" : "Allow",
      "Action" : [
        "organizations:DeregisterDelegatedAdministrator",
        "organizations:RegisterDelegatedAdministrator"
      ],
      "Resource" : "arn:aws:organizations::*:account/o-*/*",
      "Condition" : {
        "StringEquals" : {
          "organizations:ServicePrincipal" : "account-access.amazonaws.com"
        }
      }
    },
    {
      "Sid" : "AccountAccessManagerEnableServiceAccessPermissions",
      "Effect" : "Allow",
      "Action" : [
        "organizations:DisableAWSServiceAccess",
        "organizations:EnableAWSServiceAccess"
      ],
      "Resource" : "*",
      "Condition" : {
        "StringEquals" : {
          "organizations:ServicePrincipal" : "account-access.amazonaws.com"
        }
      }
    },
    {
      "Sid" : "KMSDecryptViaIdentityCenter",
      "Effect" : "Allow",
      "Action" : "kms:Decrypt",
      "Resource" : "arn:aws:kms:*:*:key/*",
      "Condition" : {
        "StringLike" : {
          "kms:ViaService" : "sso.*.amazonaws.com",
          "kms:EncryptionContext:aws:sso:instance-arn" : "arn:aws:sso:::instance/*"
        }
      }
    },
    {
      "Sid" : "KMSDecryptViaIdentityStore",
      "Effect" : "Allow",
      "Action" : "kms:Decrypt",
      "Resource" : "arn:aws:kms:*:*:key/*",
      "Condition" : {
        "StringLike" : {
          "kms:ViaService" : "identitystore.*.amazonaws.com",
          "kms:EncryptionContext:aws:identitystore:identitystore-arn" : "arn:aws:identitystore::*:identitystore/*"
        }
      }
    },
    {
      "Sid" : "CreateServiceLinkedRolePermissions",
      "Effect" : "Allow",
      "Action" : "iam:CreateServiceLinkedRole",
      "Resource" : "arn:aws:iam::*:role/aws-service-role/account-access.amazonaws.com/AWSServiceRoleForAccountAccessManager",
      "Condition" : {
        "StringEquals" : {
          "iam:AWSServiceName" : "account-access.amazonaws.com"
        }
      }
    }
  ]
}
```

## Learn more
<a name="AWSAccountAccessManagerAdministrator-learn-more"></a>
+ [Create a permission set using AWS managed policies in IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/howtocreatepermissionset.html) 
+ [Adding and removing IAM identity permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-attach-detach.html) 
+ [Understand versioning for IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-versioning.html)
+ [Get started with AWS managed policies and move toward least-privilege permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#bp-use-aws-defined-policies)