

# Identity and access management for Amazon Connect Health
<a name="security-iam"></a>

AWS Identity and Access Management (IAM) is an AWS service that helps an administrator securely control access to AWS resources. IAM administrators control who can be *authenticated* (signed in) and *authorized* (have permissions) to use Amazon Connect Health resources. IAM is an AWS service that you can use with no additional charge.

## Audience
<a name="iam-audience"></a>

How you use AWS Identity and Access Management (IAM) differs, depending on the work that you do in Amazon Connect Health.

 **Service user** — If you use the Amazon Connect Health service to do your job, then your administrator provides you with the credentials and permissions that you need. As you use more Amazon Connect Health features for your work, you might need additional permissions. Understanding how access is managed can help you request the right permissions from your administrator.

 **Service administrator** — If you’re in charge of Amazon Connect Health resources at your company, you probably have full access to Amazon Connect Health. It’s your job to determine which Amazon Connect Health features and resources your service users should access. You must then submit requests to your IAM administrator to change the permissions of your service users. Review the information on this page to understand the basic concepts of IAM.

 **IAM administrator** — If you’re an IAM administrator, you might want to learn details about how you can write policies to manage access to Amazon Connect Health.

## Authenticating with identities
<a name="iam-authentication"></a>

Authentication is how you sign in to AWS using your identity credentials. You must be authenticated (signed in to AWS) as the AWS account root user, as an IAM user, or by assuming an IAM role.

For programmatic access, AWS provides an SDK and CLI that cryptographically sign your requests using your credentials. If you don’t use AWS tools, you must sign requests yourself. Amazon Connect Health supports Signature Version 4, a protocol for authenticating inbound API requests. For more information about authenticating requests, see [AWS Signature Version 4 for API requests](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-signing.html) in the *IAM User Guide*.

Regardless of the authentication method that you use, you might also be required to provide additional security information. For example, AWS recommends that you use multi-factor authentication (MFA) to increase the security of your account.

 **AWS account root user** — When you create an AWS account, you begin with one sign-in identity that has complete access to all AWS services and resources in the account. This identity is called the AWS account root user. Do not use the root user for your everyday tasks. Safeguard your root user credentials and use them to perform the tasks that only the root user can perform.

 **IAM users and groups** — An [IAM user](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users.html) is an identity within your AWS account that has specific permissions for a single person or application. Where possible, we recommend relying on temporary credentials instead of creating IAM users who have long-term credentials such as passwords and access keys.

 **IAM roles** — An [IAM role](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html) is an identity within your AWS account that has specific permissions. It is similar to an IAM user, but is not associated with a specific person. You can temporarily assume an IAM role in the AWS Management Console by switching roles.

 **Federated identities** — As a best practice, require human users, including users that require administrator access, to use federation with an identity provider to access AWS services by using temporary credentials. A federated identity is a user from your enterprise user directory, a web identity provider, the AWS Directory Service, the Identity Center directory, or any user that accesses AWS services by using credentials provided through an identity source.

## Managing access using policies
<a name="iam-policies"></a>

You control access in AWS by creating policies and attaching them to AWS identities or resources. A policy is an object in AWS that, when associated with an identity or resource, defines their permissions. AWS evaluates these policies when a principal (user or role) makes a request. Permissions in the policies determine whether the request is allowed or denied. Most policies are stored in AWS as JSON documents.

 **Identity-based policies** — Identity-based policies are JSON permissions policy documents that you can attach to an identity, such as an IAM user, group of users, or role. These policies control what actions users and roles can perform, on which resources, and under what conditions.

 **Resource-based policies** — Resource-based policies are JSON policy documents that you attach to a resource. Examples of resource-based policies are IAM role trust policies and Amazon S3 bucket policies.

 **Other policy types** — AWS supports additional, less-common policy types, including permissions boundaries, service control policies (SCPs), resource control policies (RCPs), and session policies.

## How Amazon Connect Health works with IAM
<a name="iam-how-it-works"></a>

Amazon Connect Health uses IAM identity-based policies to control access to Connect Health operations and resources. Administrators should apply least-privilege principles, granting only the permissions required for each role.

Amazon Connect Health supports the following IAM features:
+  **Identity-based policies**: Yes
+  **Resource-based policies**: No
+  **Policy actions**: Yes (`health-agent:*`)
+  **Policy resources**: Yes (domain, agent, integration ARNs)
+  **Policy condition keys**: Yes (`aws:RequestTag`, `aws:ResourceTag`, `aws:TagKeys`)
+  **ABAC (attribute-based access control)**: Yes

Amazon Connect Health supports attribute-based access control (ABAC) through IAM tags for domain and agent related operations. Resource-level permissions can be applied to restrict access to specific domains, agents, and integrations. There are minimum IAM permissions required for administrators to access Amazon Connect Health through the AWS console.

Read-only console policy:

```
{
  "Version": "2012-10-17" ,
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "health-agent:ListDomains",
        "health-agent:GetDomain",
        "health-agent:ListIntegrations",
        "health-agent:ListAgents"
      ],
      "Resource": "*"
    }
  ]
}
```

Full access console policy:

```
{
  "Version": "2012-10-17" ,
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "cloudformation:CreateStack",
        "cloudformation:DescribeStackEvents",
        "cloudformation:DescribeStacks",
        "cloudformation:GetTemplate",
        "cloudformation:ListStacks",
        "connect:AssociatePhoneNumberContactFlow",
        "connect:ClaimPhoneNumber",
        "connect:DescribeInstance",
        "connect:DescribePhoneNumber",
        "connect:ListInstances",
        "connect:ListPhoneNumbersV2",
        "connect:ReleasePhoneNumber",
        "connect:SearchAvailablePhoneNumbers",
        "connect:TagResource",
        "connect:UpdatePhoneNumber",
        "connect:UpdatePhoneNumberMetadata",
        "ds:DescribeDirectories",
        "health-agent:CreateAgent",
        "health-agent:CreateDomain",
        "health-agent:CreateIntegration",
        "health-agent:DeleteAgent",
        "health-agent:DeleteDomain",
        "health-agent:DeleteIntegration",
        "health-agent:GenerateMedicalCodes",
        "health-agent:GetAgent",
        "health-agent:GetDomain",
        "health-agent:GetIntegration",
        "health-agent:GetPatientInsightsJob",
        "health-agent:ListAgents",
        "health-agent:ListDomains",
        "health-agent:ListIntegrations",
        "health-agent:PublishAgent",
        "health-agent:StartPatientInsightsJob",
        "health-agent:UpdateAgent",
        "health-agent:UpdateIntegration",
        "healthlake:ReadResource",
        "healthlake:SearchEverything",
        "healthlake:SearchWithGet",
        "healthlake:SearchWithPost",
        "iam:AttachRolePolicy",
        "iam:CreatePolicy",
        "iam:CreatePolicyVersion",
        "iam:CreateRole",
        "iam:CreateServiceLinkedRole",
        "iam:DeletePolicyVersion",
        "iam:GetRole",
        "iam:GetRolePolicy",
        "iam:PassRole",
        "iam:PutRolePolicy",
        "kms:DescribeKey",
        "kms:ListAliases",
        "kms:ListKeys",
        "lambda:AddPermission",
        "lambda:CreateFunction",
        "lambda:GetFunction",
        "lex:BuildBotLocale",
        "lex:CreateBot",
        "lex:CreateBotAlias",
        "lex:CreateBotLocale",
        "lex:CreateBotVersion",
        "lex:CreateCustomVocabulary",
        "lex:CreateIntent",
        "lex:CreateResourcePolicy",
        "lex:CreateSlot",
        "lex:CreateSlotType",
        "lex:CreateUploadUrl",
        "lex:DeleteBotLocale",
        "lex:DeleteCustomVocabulary",
        "lex:DeleteIntent",
        "lex:DeleteSlot",
        "lex:DeleteSlotType",
        "lex:DescribeBot",
        "lex:DescribeBotAlias",
        "lex:DescribeBotLocale",
        "lex:DescribeBotVersion",
        "lex:DescribeImport",
        "lex:ListBotLocales",
        "lex:ListBots",
        "lex:ListTagsForResource",
        "lex:StartImport",
        "lex:TagResource",
        "lex:UpdateBot",
        "lex:UpdateBotAlias",
        "lex:UpdateBotLocale",
        "lex:UpdateCustomVocabulary",
        "lex:UpdateIntent",
        "lex:UpdateResourcePolicy",
        "lex:UpdateSlot",
        "lex:UpdateSlotType",
        "organizations:DescribeOrganization",
        "organizations:ListAccounts",
        "s3:GetObject",
        "s3:ListAllMyBuckets",
        "s3:ListBucket",
        "s3:PutObject",
        "sso:CreateApplication",
        "sso:CreateApplicationAssignment",
        "sso:CreateInstance",
        "sso:ListDirectoryAssociations",
        "sso:ListInstances",
        "sso:PutApplicationAuthenticationMethod",
        "sso:PutApplicationGrant",
        "sso-directory:CreateUser",
        "sso-directory:SearchUsers"
      ],
      "Resource": "*"
    }
  ]
}
```

## Identity-based policy examples for Amazon Connect Health
<a name="iam-policy-examples"></a>

By default, users and roles don’t have permission to create or modify Amazon Connect Health resources. They also can’t perform tasks by using the AWS Management Console, AWS CLI, or AWS API. To grant users permission to perform actions on the resources that they need, an IAM administrator can create IAM policies. The administrator can then add the IAM policies to roles, and users can assume the roles.

To learn how to create an IAM identity-based policy by using these example JSON policy documents, see [Creating policies on the JSON tab](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_create-console.html) in the *IAM User Guide*.

Policy best practices:
+ Get started with AWS managed policies and move toward least-privilege permissions.
+ Apply least-privilege permissions — When you set permissions with IAM policies, grant only the permissions required to perform a task.
+ Use conditions in IAM policies to further restrict access.
+ Use IAM Access Analyzer to validate your IAM policies to ensure secure and functional permissions.
+ Require multi-factor authentication (MFA).

### Example 1: Allow full access to a specific domain
<a name="iam-example-domain"></a>

The following policy grants full access to a specific Amazon Connect Health domain and its integrations.

```
{
  "Version": "2012-10-17" ,
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "health-agent:*"
      ],
      "Resource": [
        "arn:aws:health-agent:<region>:<account-id>:domain/<domain-id>",
        "arn:aws:health-agent:<region>:<account-id>:domain/<domain-id>/integration/*"
      ]
    }
  ]
}
```

### Example 2: Allow users to start and view ambient documentation sessions
<a name="iam-example-ambient"></a>

The following policy allows users to start and retrieve ambient documentation sessions.

```
{
  "Version": "2012-10-17" ,
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "health-agent:StartMedicalScribeListeningSession",
        "health-agent:GetMedicalScribeListeningSession"
      ],
      "Resource": "*"
    }
  ]
}
```

### Example 3: Read-only access to ambient documentation
<a name="iam-example-ambient-readonly"></a>

The following policy grants read-only access to ambient documentation sessions.

```
{
  "Version": "2012-10-17" ,
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "health-agent:GetMedicalScribeListeningSession",
        "health-agent:ListMedicalScribeListeningSessions"
      ],
      "Resource": "*"
    }
  ]
}
```

### Example 4: Full access to all Connect Health resources
<a name="iam-example-full-access"></a>

The following policy grants full access to all Amazon Connect Health resources.

```
{
  "Version": "2012-10-17" ,
  "Statement": [
    {
      "Effect": "Allow",
      "Action": "health-agent:*",
      "Resource": "*"
    }
  ]
}
```

### Example 5: Read-only access with deny on destructive actions
<a name="iam-example-deny-delete"></a>

The following policy grants read-only access to domains and agents while explicitly denying delete operations.

```
{
  "Version": "2012-10-17" ,
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "health-agent:GetDomain",
        "health-agent:ListAgents",
        "health-agent:GetAgent"
      ],
      "Resource": "*"
    },
    {
      "Effect": "Deny",
      "Action": [
        "health-agent:DeleteDomain",
        "health-agent:DeleteAgent"
      ],
      "Resource": "*"
    }
  ]
}
```

### Example 6: Allow IAM users to view their own permissions
<a name="iam-example-view-permissions"></a>

This example shows how you might create a policy that allows IAM users to view the inline and managed policies that are attached to their user identity.

```
{
  "Version": "2012-10-17" ,
  "Statement": [
    {
      "Sid": "ViewOwnUserInfo",
      "Effect": "Allow",
      "Action": [
        "iam:GetUserPolicy",
        "iam:ListGroupsForUser",
        "iam:ListAttachedUserPolicies",
        "iam:ListUserPolicies",
        "iam:GetUser"
      ],
      "Resource": ["arn:aws:iam::*:user/${aws:username}"]
    },
    {
      "Sid": "NavigateInConsole",
      "Effect": "Allow",
      "Action": [
        "iam:GetGroupPolicy",
        "iam:GetPolicyVersion",
        "iam:GetPolicy",
        "iam:ListAttachedGroupPolicies",
        "iam:ListGroupPolicies",
        "iam:ListPolicyVersions",
        "iam:ListPolicies",
        "iam:ListUsers"
      ],
      "Resource": "*"
    }
  ]
}
```

## Service roles and trust policies
<a name="iam-service-roles"></a>

Amazon Connect Health uses an IAM service role to perform actions on your behalf. Each AWS service component that Amazon Connect Health interacts with operates under a dedicated IAM service role with a trust policy scoped to the specific service principal.

The following example shows a service role policy for Amazon Connect Health that grants permissions for domain, integration, and agent management.

```
{
  "Version": "2012-10-17" ,
  "Statement": [
    {
      "Sid": "DescribeUserWithSourceIdentity",
      "Effect": "Allow",
      "Action": [
        "identitystore:DescribeUser"
      ],
      "Resource": "arn:aws:identitystore:::user/${aws:SourceIdentity}"
    },
    {
      "Sid": "DomainReadAccess",
      "Effect": "Allow",
      "Action": [
        "health-agent:GetDomain"
      ],
      "Resource": "arn:aws:health-agent:<region>:<account-id>:domain/<domain-id>"
    },
    {
      "Sid": "ListOperations",
      "Effect": "Allow",
      "Action": [
        "health-agent:ListIntegrations",
        "health-agent:ListAgents",
        "health-agent:ListAgentVersions"
      ],
      "Resource": "arn:aws:health-agent:<region>:<account-id>:domain/<domain-id>"
    },
    {
      "Sid": "IntegrationManagement",
      "Effect": "Allow",
      "Action": [
        "health-agent:CreateIntegration",
        "health-agent:GetIntegration",
        "health-agent:UpdateIntegration",
        "health-agent:DeleteIntegration"
      ],
      "Resource": [
        "arn:aws:health-agent:<region>:<account-id>:domain/<domain-id>",
        "arn:aws:health-agent:<region>:<account-id>:domain/<domain-id>/integration/*"
      ]
    },
    {
      "Sid": "AgentManagement",
      "Effect": "Allow",
      "Action": [
        "health-agent:CreateAgent",
        "health-agent:UpdateAgent",
        "health-agent:GetAgent",
        "health-agent:PublishAgent",
        "health-agent:DeleteAgent"
      ],
      "Resource": [
        "arn:aws:health-agent:<region>:<account-id>:domain/<domain-id>",
        "arn:aws:health-agent:<region>:<account-id>:domain/<domain-id>/agent/*"
      ]
    }
  ]
}
```

The following example shows a trust policy that allows the Amazon Connect Health service principal to assume the role.

```
{
  "Version": "2012-10-17" ,
  "Statement": [
    {
      "Sid": "AllowHealthAgentServicePrincipal",
      "Effect": "Allow",
      "Principal": {
        "Service": "health-agent.amazonaws.com"
      },
      "Action": [
        "sts:AssumeRole",
        "sts:SetContext",
        "sts:SetSourceIdentity"
      ],
      "Condition": {
        "ArnLike": {
          "aws:SourceArn": "arn:aws:health-agent:<region>:<account-id>:domain/<domain-id>/*"
        },
        "StringEquals": {
          "aws:SourceAccount": "<account-id>"
        }
      }
    }
  ]
}
```

To help prevent the confused deputy problem, we recommend using the `aws:SourceArn` and `aws:SourceAccount` condition keys in the trust policy. The source ARN should be scoped to the specific Amazon Connect Health domain that the role is intended to serve.