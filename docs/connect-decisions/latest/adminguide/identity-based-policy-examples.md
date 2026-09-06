# Identity-based policy examples

By default, users and roles don't have permission to create or modify
Amazon Connect Decisions resources. They also can't perform tasks by using the AWS Management Console,
AWS Command Line Interface (AWS CLI), or AWS API. To grant users permission to perform actions on
the resources that they need, an IAM administrator can create IAM policies. The administrator can
then add the IAM policies to roles, and users can assume the roles.

To learn how to create an IAM identity-based policy by using these example JSON policy
documents, see [Creating IAM policies](../../../IAM/latest/UserGuide/access_policies_create-console.md "../../../IAM/latest/UserGuide/access_policies_create-console.md") in the IAM User Guide.

## Instance Management IAM Policy

Below is the IAM policy needed to create, update, or delete instances through the
console or public API (excludes all Webapp operations).

```
{
            "Version": "2012-10-17",
            "Statement": [
                {
                    "Action": "scn:*",
                    "Resource": "*",
                    "Effect": "Allow"
                },
                {
                    "Action": [
                        "s3:GetObject",
                        "s3:PutObject",
                        "s3:ListBucket",
                        "s3:CreateBucket",
                        "s3:PutBucketVersioning",
                        "s3:PutBucketObjectLockConfiguration",
                        "s3:PutEncryptionConfiguration",
                        "s3:PutBucketPolicy",
                        "s3:PutLifecycleConfiguration",
                        "s3:PutBucketPublicAccessBlock",
                        "s3:DeleteObject",
                        "s3:ListAllMyBuckets",
                        "s3:PutBucketOwnershipControls",
                        "s3:PutBucketNotification",
                        "s3:PutAccountPublicAccessBlock",
                        "s3:PutBucketLogging",
                        "s3:PutBucketTagging"
                    ],
                    "Resource": "arn:aws:s3:::aws-supply-chain-*",
                    "Effect": "Allow"
                },
                {
                    "Action": [
                        "cloudtrail:CreateTrail",
                        "cloudtrail:PutEventSelectors",
                        "cloudtrail:GetEventSelectors",
                        "cloudtrail:StartLogging"
                    ],
                    "Resource": "*",
                    "Effect": "Allow"
                },
                {
                    "Action": [
                        "events:DescribeRule",
                        "events:PutRule",
                        "events:PutTargets"
                    ],
                    "Resource": "*",
                    "Effect": "Allow"
                },
                {
                    "Action": [
                        "cloudwatch:PutMetricData",
                        "cloudwatch:Describe*",
                        "cloudwatch:Get*",
                        "cloudwatch:List*"
                    ],
                    "Resource": "*",
                    "Effect": "Allow"
                },
                {
                    "Action": [
                        "organizations:CreateOrganization",
                        "organizations:DescribeAccount",
                        "organizations:DescribeOrganization",
                        "organizations:EnableAWSServiceAccess",
                        "organizations:ListDelegatedAdministrators"
                    ],
                    "Resource": "*",
                    "Effect": "Allow"
                },
                {
                    "Action": [
                        "kms:ListAliases"
                    ],
                    "Resource": "*",
                    "Effect": "Allow"
                },
                {
                    "Action": [
                        "iam:CreateRole",
                        "iam:CreatePolicy",
                        "iam:GetRole",
                        "iam:PutRolePolicy",
                        "iam:AttachRolePolicy",
                        "iam:CreateServiceLinkedRole"
                    ],
                    "Resource": "*",
                    "Effect": "Allow"
                },
                {
                    "Action": [
                        "sso:AssociateDirectory",
                        "sso:AssociateProfile",
                        "sso:CreateApplication",
                        "sso:CreateApplicationAssignment",
                        "sso:CreateInstance",
                        "sso:CreateManagedApplicationInstance",
                        "sso:DeleteApplication",
                        "sso:DeleteApplicationAssignment",
                        "sso:DeleteManagedApplicationInstance",
                        "sso:DescribeApplication",
                        "sso:DescribeDirectories",
                        "sso:DescribeInstance",
                        "sso:DescribeRegisteredRegions",
                        "sso:DescribeTrusts",
                        "sso:DisassociateProfile",
                        "sso:GetManagedApplicationInstance",
                        "sso:GetPeregrineStatus",
                        "sso:GetProfile",
                        "sso:GetSharedSsoConfiguration",
                        "sso:GetSsoConfiguration",
                        "sso:GetSSOStatus",
                        "sso:ListApplicationAssignments",
                        "sso:ListApplicationTemplates",
                        "sso:ListDirectoryAssociations",
                        "sso:ListInstances",
                        "sso:ListProfileAssociations",
                        "sso:ListProfiles",
                        "sso:PutApplicationAuthenticationMethod",
                        "sso:PutApplicationGrant",
                        "sso:RegisterRegion",
                        "sso:SearchDirectoryGroups",
                        "sso:SearchDirectoryUsers",
                        "sso:SearchGroups",
                        "sso:SearchUsers",
                        "sso:StartPeregrine",
                        "sso:StartSSO",
                        "sso:UpdateSsoConfiguration",
                        "sso-directory:SearchUsers"
                    ],
                    "Resource": "*",
                    "Effect": "Allow"
                }
            ]
        }
```

## Policy best practices

Identity-based policies determine whether someone can create, access, or delete
Amazon Connect Decisions resources in your account. These actions can incur costs for your AWS
account. When you create or edit identity-based policies, follow these guidelines and
recommendations:

- **Get started with AWS managed policies and move toward
  least-privilege permissions** – To get started granting permissions to
  your users and workloads, use the _AWS managed policies_ that
  grant permissions for many common use cases. They are available in your AWS
  account. We recommend that you reduce permissions further by defining AWS
  customer managed policies that are specific to your use cases. For more
  information, see [AWS managed policies](../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies "../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies") or [AWS managed policies for job functions](../../../IAM/latest/UserGuide/access_policies_job-functions.md "../../../IAM/latest/UserGuide/access_policies_job-functions.md") in the _IAM User
  Guide_.
- **Apply least-privilege permissions** – When you set
  permissions with IAM policies, grant only the permissions required to perform a
  task. You do this by defining the actions that can be taken on specific resources
  under specific conditions, also known as _least-privilege
  permissions_. For more information about using IAM to apply
  permissions, see [Policies and permissions in IAM](../../../IAM/latest/UserGuide/access_policies.md "../../../IAM/latest/UserGuide/access_policies.md") in the _IAM User
  Guide_.
- **Use conditions in IAM policies to further restrict
  access** – You can add a condition to your policies to limit access to
  actions and resources. For example, you can write a policy condition to specify
  that all requests must be sent using SSL. You can also use conditions to grant
  access to service actions if they are used through a specific AWS service, such
  as CloudFormation. For more information, see [IAM JSON policy elements: Condition](../../../IAM/latest/UserGuide/reference_policies_elements_condition.md "../../../IAM/latest/UserGuide/reference_policies_elements_condition.md") in the _IAM User
  Guide_.
- **Use IAM Access Analyzer to validate your IAM policies to
  ensure secure and functional permissions** – IAM Access Analyzer
  validates new and existing policies so that the policies adhere to the IAM policy
  language (JSON) and IAM best practices. IAM Access Analyzer provides more than
  100 policy checks and actionable recommendations to help you author secure and
  functional policies. For more information, see [Validate policies with IAM Access Analyzer](../../../IAM/latest/UserGuide/access-analyzer-policy-validation.md "../../../IAM/latest/UserGuide/access-analyzer-policy-validation.md") in the _IAM
  User Guide_.
- **Require multi-factor authentication (MFA)**
  – If you have a scenario that requires IAM users or a root user in your AWS
  account, turn on MFA for additional security. To require MFA when API operations
  are called, add MFA conditions to your policies. For more information, see
  [Secure API access with MFA](../../../IAM/latest/UserGuide/id_credentials_mfa_configure-api-require.md "../../../IAM/latest/UserGuide/id_credentials_mfa_configure-api-require.md") in the _IAM User
  Guide_.

For more information about best practices in IAM, see [Security
best practices in IAM](../../../IAM/latest/UserGuide/best-practices.md "../../../IAM/latest/UserGuide/best-practices.md") in the _IAM User Guide_.
