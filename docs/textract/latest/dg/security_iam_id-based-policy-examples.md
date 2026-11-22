

# Amazon Textract identity-based policy examples

By default, users and roles don't have permission to create or modify Amazon Textract Core resources. They also can't perform tasks using the AWS Management Console, AWS CLI, or AWS API. An administrator must create IAM policies that grant users and roles permission to perform specific API operations on the specified resources they need. The administrator then grants a user access to a role via temporary security credentials.

To learn how to create an IAM identity-based policy using these example JSON policy documents, see [Creating Policies on the JSON Tab](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_create.html#access_policies_create-json-editor) in the *IAM User Guide*.

**Topics**
+ [Policy best practices](#security_iam_service-with-iam-policy-best-practices)
+ [Allow users to view their own permissions](#security_iam_id-based-policy-examples-view-own-permissions)
+ [Giving access to synchronous operations in Amazon Textract Core](#security_iam_sync-actions)
+ [Giving access to asynchronous operations in Amazon Textract Core](#security_iam_async-actions)
+ [Giving access to specific adapters in inference operations in Amazon Textract Core](#security_iam_adapter-inference)
+ [Disallow user to use adapters in inference operations](#security_iam_disallow-inference)
+ [Allow user to only use a specific group of adapters in inference operations, or no adapters](#security_iam_adapter-groups)
+ [Giving access to Amazon Textract Insights operations](#security_iam_insights-operations)
+ [Allowing a user to run Amazon Textract Insights jobs on existing projects only](#security_iam_insights-existing-projects)
+ [Allowing Amazon Textract Insights jobs only with projects that have a specific tag](#security_iam_insights-tag-scoped)
+ [Allowing Amazon Textract Insights jobs with cross-Region inference](#security_iam_insights-cris)

## Policy best practices
<a name="security_iam_service-with-iam-policy-best-practices"></a>

Identity-based policies determine whether someone can create, access, or delete Amazon Textract resources in your account. These actions can incur costs for your AWS account. When you create or edit identity-based policies, follow these guidelines and recommendations:
+ **Get started with AWS managed policies and move toward least-privilege permissions** – To get started granting permissions to your users and workloads, use the *AWS managed policies* that grant permissions for many common use cases. They are available in your AWS account. We recommend that you reduce permissions further by defining AWS customer managed policies that are specific to your use cases. For more information, see [AWS managed policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies) or [AWS managed policies for job functions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_job-functions.html) in the *IAM User Guide*.
+ **Apply least-privilege permissions** – When you set permissions with IAM policies, grant only the permissions required to perform a task. You do this by defining the actions that can be taken on specific resources under specific conditions, also known as *least-privilege permissions*. For more information about using IAM to apply permissions, see [ Policies and permissions in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html) in the *IAM User Guide*.
+ **Use conditions in IAM policies to further restrict access** – You can add a condition to your policies to limit access to actions and resources. For example, you can write a policy condition to specify that all requests must be sent using SSL. You can also use conditions to grant access to service actions if they are used through a specific AWS service, such as CloudFormation. For more information, see [ IAM JSON policy elements: Condition](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_condition.html) in the *IAM User Guide*.
+ **Use IAM Access Analyzer to validate your IAM policies to ensure secure and functional permissions** – IAM Access Analyzer validates new and existing policies so that the policies adhere to the IAM policy language (JSON) and IAM best practices. IAM Access Analyzer provides more than 100 policy checks and actionable recommendations to help you author secure and functional policies. For more information, see [Validate policies with IAM Access Analyzer](https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-policy-validation.html) in the *IAM User Guide*.
+ **Require multi-factor authentication (MFA)** – If you have a scenario that requires IAM users or a root user in your AWS account, turn on MFA for additional security. To require MFA when API operations are called, add MFA conditions to your policies. For more information, see [ Secure API access with MFA](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_mfa_configure-api-require.html) in the *IAM User Guide*.

For more information about best practices in IAM, see [Security best practices in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html) in the *IAM User Guide*.

## Allow users to view their own permissions
<a name="security_iam_id-based-policy-examples-view-own-permissions"></a>

This example shows how you might create a policy that allows IAM users to view the inline and managed policies that are attached to their user identity. This policy includes permissions to complete this action on the console or programmatically using the AWS CLI or AWS API.

```json
{
    "Version": "2012-10-17",		 	 	 
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

## Giving access to synchronous operations in Amazon Textract Core
<a name="security_iam_sync-actions"></a>

This example policy grants access to the synchronous actions in Amazon Textract Core to an IAM user in your AWS account.

```
"Version": "2012-10-17",		 	 	 
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "textract:DetectDocumentText",
                "textract:AnalyzeDocument"
            ],
            "Resource": "*"
        }
    ]
```

## Giving access to asynchronous operations in Amazon Textract Core
<a name="security_iam_async-actions"></a>

The following example policy gives an IAM user on your AWS account access to all asynchronous operations used in Amazon Textract Core.

------
#### [ JSON ]

****  

```json
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "textract:StartDocumentTextDetection",
                "textract:StartDocumentAnalysis",
                "textract:GetDocumentTextDetection",
                "textract:GetDocumentAnalysis"
            ],
            "Resource": "*"
        }
    ]
}
```

------

## Giving access to specific adapters in inference operations in Amazon Textract Core
<a name="security_iam_adapter-inference"></a>

Although you can use `*` to access all resources in inference operations, you can control a user's access to specific adapters.

## Disallow user to use adapters in inference operations
<a name="security_iam_disallow-inference"></a>

## Allow user to only use a specific group of adapters in inference operations, or no adapters
<a name="security_iam_adapter-groups"></a>

Tag the specific adapters that you want to control by using the `TagResource` operation. The following example controls access to adapters tagged with `{"env":"prod"}`.

### Allow user to manage adapter and versions
<a name="security_iam_adapter-versions"></a>

### Permissions needed for CreateAdapterVersion
<a name="security_iam_create-adapter-version"></a>

In addition to `"textract:CreateAdapterVersion"` permission, the caller identity also needs Amazon S3 and AWS Key Management Service (AWS KMS) permission to your training data in Amazon S3 and the KMS key used to encrypt your data. 

## Giving access to Amazon Textract Insights operations
<a name="security_iam_insights-operations"></a>

A Amazon Textract Insights workflow needs three kinds of permissions:
+ The Amazon Textract Insights actions that it calls. A job needs both `textract:StartDocumentInsights` and `textract:GetDocumentInsights`. Managing projects and blueprints needs the matching project and blueprint actions.
+ `s3:GetObject` on the input location and `s3:PutObject` on the output location.
+ Permission to use your customer managed AWS KMS key, if you use one.

Grant only what your workflow uses. For example, leave out the blueprint actions if you don't create custom blueprints, and the tagging actions if you don't tag resources.

For a complete policy that covers the full workflow, see [Prerequisites and setup](insights-prerequisites.md). For the AWS KMS permissions and an example key policy, see [Data protection and encryption](insights-data-protection.md).

## Allowing a user to run Amazon Textract Insights jobs on existing projects only
<a name="security_iam_insights-existing-projects"></a>

To let an application submit jobs and read the results without creating, changing, or deleting projects or blueprints, start from the full workflow policy in [Prerequisites and setup](insights-prerequisites.md) and keep only the following:
+ `textract:StartDocumentInsights` and `textract:GetDocumentInsights`.
+ `textract:GetProject` and `textract:ListProjects`, if the application looks up projects.
+ `s3:GetObject` on the input location and `s3:PutObject` on the output location.
+ Permission to use the customer managed AWS KMS key, if the project uses one. See [Data protection and encryption](insights-data-protection.md).

`StartDocumentInsights` doesn't require `GetProject` or `GetBlueprint`. When you pass a project, Amazon Textract Insights checks `textract:StartDocumentInsights` only on the project ARN and on `job/*`. To limit the application to specific projects, allow it on those project ARNs and on `job/*`. If the application tags jobs when it starts them, it also needs `textract:TagResource` on `job/*`.

## Allowing Amazon Textract Insights jobs only with projects that have a specific tag
<a name="security_iam_insights-tag-scoped"></a>

The following policy lets a user start jobs only with projects tagged `env=prod`. The user can read the status of any job in the account.

```json
{
    "Version": "2012-10-17",		 	 	 
    "Statement": [
        {
            "Sid": "StartJobsOnProdProjects",
            "Effect": "Allow",
            "Action": "textract:StartDocumentInsights",
            "Resource": "arn:aws:textract:us-east-1:111122223333:project/*",
            "Condition": {
                "StringEquals": { "aws:ResourceTag/env": "prod" }
            }
        },
        {
            "Sid": "CreateJobs",
            "Effect": "Allow",
            "Action": "textract:StartDocumentInsights",
            "Resource": "arn:aws:textract:us-east-1:111122223333:job/*"
        },
        {
            "Sid": "ReadJobStatus",
            "Effect": "Allow",
            "Action": "textract:GetDocumentInsights",
            "Resource": "*"
        }
    ]
}
```

Amazon Textract Insights also checks `textract:StartDocumentInsights` on `job/*` because each request creates a new job, so the policy allows it separately. The user also needs `s3:GetObject` on the input location and `s3:PutObject` on the output location. See [Prerequisites and setup](insights-prerequisites.md).

## Allowing Amazon Textract Insights jobs with cross-Region inference
<a name="security_iam_insights-cris"></a>

The following example IAM policy processes documents for `us-east-1`.

```json
{
    "Version": "2012-10-17",		 	 	 
    "Statement": [
        {
            "Sid": "RunTextractInsightsJobs",
            "Effect": "Allow",
            "Action": [
                "textract:StartDocumentInsights",
                "textract:GetDocumentInsights"
            ],
            "Resource": [
                "arn:aws:textract:us-east-1:111122223333:project/*",
                "arn:aws:textract:us-east-1:111122223333:blueprint/*",
                "arn:aws:textract:us-east-1:aws:blueprint/*",
                "arn:aws:textract:us-east-1:111122223333:job/*"
            ]
        }
    ]
}
```

`arn:aws:textract:us-east-1:aws:blueprint/*` allows public blueprints owned by Amazon Textract. Include it if you pass public blueprints in the `Blueprints` parameter of the request.