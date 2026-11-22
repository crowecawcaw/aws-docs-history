

# AWSAPIPortalServiceRolePolicy

**Description**: Allows APIPortal to manage associated AWS Resources on behalf of the customer

`AWSAPIPortalServiceRolePolicy` is an [AWS managed policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies).

## Using this policy
<a name="AWSAPIPortalServiceRolePolicy-how-to-use"></a>

This policy is attached to a service-linked role that allows the service to perform actions on your behalf. You cannot attach this policy to your users, groups, or roles.

## Policy details
<a name="AWSAPIPortalServiceRolePolicy-details"></a>
+ **Type**: Service-linked role policy 
+ **Creation time**: November 17, 2026, 23:37 UTC 
+ **Edited time:** November 19, 2026, 17:27 UTC
+ **ARN**: `arn:aws:iam::aws:policy/aws-service-role/AWSAPIPortalServiceRolePolicy`

## Policy version
<a name="AWSAPIPortalServiceRolePolicy-version"></a>

**Policy version:** v2 (default)

The policy's default version is the version that defines the permissions for the policy. When a user or role with the policy makes a request to access an AWS resource, AWS checks the default version of the policy to determine whether to allow the request. 

## JSON policy document
<a name="AWSAPIPortalServiceRolePolicy-json"></a>

```json
{
  "Version" : "2012-10-17",
  "Statement" : [
    {
      "Sid" : "APIPortalServiceRoleOrganizationsPermissions",
      "Effect" : "Allow",
      "Action" : [
        "organizations:DescribeAccount",
        "organizations:DescribeOrganization",
        "organizations:DescribeOrganizationalUnit",
        "organizations:ListAccounts",
        "organizations:ListChildren",
        "organizations:ListParents",
        "organizations:ListDelegatedAdministrators",
        "organizations:ListAWSServiceAccessForOrganization"
      ],
      "Resource" : "*"
    },
    {
      "Sid" : "APIPortalServiceRoleConfigPermissions",
      "Effect" : "Allow",
      "Action" : [
        "config:PutServiceLinkedConfigurationRecorder",
        "config:DescribeConfigurationRecorders",
        "config:DescribeConfigurationRecorderStatus",
        "config:DeleteServiceLinkedConfigurationRecorder",
        "config:AssociateResourceTypes",
        "config:DisassociateResourceTypes"
      ],
      "Resource" : [
        "arn:aws:config:*:*:configuration-recorder/*ConfigurationRecorderForAPIPortal*"
      ]
    },
    {
      "Sid" : "APIPortalServiceRoleConfigIamPermissions",
      "Effect" : "Allow",
      "Action" : [
        "iam:CreateServiceLinkedRole"
      ],
      "Resource" : "arn:aws:iam::*:role/aws-service-role/config.amazonaws.com/AWSServiceRoleForConfig",
      "Condition" : {
        "StringEquals" : {
          "iam:AWSServiceName" : "config.amazonaws.com"
        }
      }
    },
    {
      "Sid" : "APIPortalServiceRoleWafPermissions",
      "Effect" : "Allow",
      "Action" : [
        "wafv2:ListEvents"
      ],
      "Resource" : "*"
    }
  ]
}
```

## Learn more
<a name="AWSAPIPortalServiceRolePolicy-learn-more"></a>
+ [Understand versioning for IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-versioning.html)
+ [Get started with AWS managed policies and move toward least-privilege permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#bp-use-aws-defined-policies)