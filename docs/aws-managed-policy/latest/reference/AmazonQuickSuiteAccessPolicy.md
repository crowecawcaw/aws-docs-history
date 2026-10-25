

# AmazonQuickSuiteAccessPolicy
<a name="AmazonQuickSuiteAccessPolicy"></a>

**Description**: Provides permissions for Amazon Quick Suite to manage its IAM Identity Center application, identity store users and groups, user subscriptions, and QuickSight resources on your behalf.

`AmazonQuickSuiteAccessPolicy` is an [AWS managed policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies).

## Using this policy
<a name="AmazonQuickSuiteAccessPolicy-how-to-use"></a>

You can attach `AmazonQuickSuiteAccessPolicy` to your users, groups, and roles.

## Policy details
<a name="AmazonQuickSuiteAccessPolicy-details"></a>
+ **Type**: Service role policy 
+ **Creation time**: October 19, 2026, 23:57 UTC 
+ **Edited time:** October 19, 2026, 23:57 UTC
+ **ARN**: `arn:aws:iam::aws:policy/service-role/AmazonQuickSuiteAccessPolicy`

## Policy version
<a name="AmazonQuickSuiteAccessPolicy-version"></a>

**Policy version:** v1 (default)

The policy's default version is the version that defines the permissions for the policy. When a user or role with the policy makes a request to access an AWS resource, AWS checks the default version of the policy to determine whether to allow the request. 

## JSON policy document
<a name="AmazonQuickSuiteAccessPolicy-json"></a>

```
{
  "Version" : "2012-10-17",
  "Statement" : [
    {
      "Sid" : "quicksight",
      "Effect" : "Allow",
      "Action" : "quicksight:*",
      "Resource" : "*"
    },
    {
      "Sid" : "identitystore",
      "Effect" : "Allow",
      "Action" : [
        "identitystore:ListUsers",
        "identitystore:ListGroups",
        "identitystore:DescribeUser",
        "identitystore:DescribeGroup",
        "identitystore:CreateUser",
        "identitystore:CreateGroup",
        "identitystore:UpdateUser",
        "identitystore:UpdateGroup",
        "identitystore:DeleteUser",
        "identitystore:DeleteGroup",
        "identitystore:ReserveUser",
        "identitystore:GetUserId",
        "identitystore:GetGroupId",
        "identitystore:ListGroupMembershipsForMember"
      ],
      "Resource" : "*"
    },
    {
      "Sid" : "ssoControlPlane",
      "Effect" : "Allow",
      "Action" : [
        "sso:DescribeInstance",
        "sso:ListInstances",
        "sso:DescribeRegisteredRegions",
        "sso:CreateApplication",
        "sso:UpdateApplication",
        "sso:DeleteApplication",
        "sso:DescribeApplication",
        "sso:ListApplications",
        "sso:PutApplicationAuthenticationMethod",
        "sso:PutApplicationGrant",
        "sso:ListApplicationGrants",
        "sso:PutApplicationAccessScope",
        "sso:DeleteApplicationAccessScope",
        "sso:ListApplicationAccessScopes",
        "sso:CreateApplicationAssignment",
        "sso:DeleteApplicationAssignment",
        "sso:PutApplicationAssignmentConfiguration",
        "sso:AssociateProfile",
        "sso:DisassociateProfile",
        "sso:ListProfiles",
        "sso:GetProfile",
        "sso:ListDirectoryAssociations",
        "sso:SearchGroups"
      ],
      "Resource" : "*"
    },
    {
      "Sid" : "ssoOauthRuntime",
      "Effect" : "Allow",
      "Action" : [
        "sso-oauth:CreateTokenWithIAM",
        "sso-oauth:IntrospectTokenWithIAM",
        "sso-oauth:RevokeTokenWithIAM"
      ],
      "Resource" : "arn:aws:sso::*:application/*"
    },
    {
      "Sid" : "signin",
      "Effect" : "Allow",
      "Action" : "signin:CreateOAuth2Token",
      "Resource" : [
        "arn:aws:signin:*:*:*"
      ],
      "Condition" : {
        "StringEquals" : {
          "aws:ResourceAccount" : "${aws:PrincipalAccount}"
        }
      }
    },
    {
      "Sid" : "stsSelf",
      "Effect" : "Allow",
      "Action" : [
        "sts:AssumeRole",
        "sts:SetContext",
        "sts:TagSession"
      ],
      "Resource" : [
        "arn:aws:iam::*:role/AmazonQuickSuiteAccessRole"
      ],
      "Condition" : {
        "StringEquals" : {
          "aws:ResourceAccount" : "${aws:PrincipalAccount}"
        }
      }
    },
    {
      "Sid" : "passRoleSelf",
      "Effect" : "Allow",
      "Action" : "iam:PassRole",
      "Resource" : [
        "arn:aws:iam::*:role/AmazonQuickSuiteAccessRole"
      ],
      "Condition" : {
        "StringEquals" : {
          "aws:ResourceAccount" : "${aws:PrincipalAccount}"
        }
      }
    },
    {
      "Sid" : "userSubscriptions",
      "Effect" : "Allow",
      "Action" : [
        "user-subscriptions:SetOverageConfig",
        "user-subscriptions:GetCurrentPlanDetails",
        "user-subscriptions:ListApplicationClaims",
        "user-subscriptions:CreateUpdatePlanPreview",
        "user-subscriptions:UpdateClaim",
        "user-subscriptions:CreateClaim"
      ],
      "Resource" : "*"
    },
    {
      "Sid" : "organizations",
      "Effect" : "Allow",
      "Action" : [
        "organizations:DescribeOrganization",
        "organizations:ListAWSServiceAccessForOrganization"
      ],
      "Resource" : "*"
    }
  ]
}
```

## Learn more
<a name="AmazonQuickSuiteAccessPolicy-learn-more"></a>
+ [Create a permission set using AWS managed policies in IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/howtocreatepermissionset.html) 
+ [Adding and removing IAM identity permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-attach-detach.html) 
+ [Understand versioning for IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-versioning.html)
+ [Get started with AWS managed policies and move toward least-privilege permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#bp-use-aws-defined-policies)