

# Identity-based policy examples for AWS Continuum
<a name="security_iam_id-based-policy-examples"></a>

By default, users and roles don't have permission to create or modify AWS Continuum resources. An IAM administrator can grant these permissions through policies.

The IAM action prefix for AWS Continuum is `continuum`. For instructions on creating IAM policies, see [Creating IAM policies (console)](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_create-console.html) in the *IAM User Guide*. For information about collector authorization policies, see [Authorizing an environment to use collector data](cv-adding-context.md#cv-adding-context-cross-account).

**Topics**
+ [Policy best practices](#security_iam_service-with-iam-policy-best-practices)
+ [Using the AWS Continuum console](#security_iam_id-based-policy-examples-console)
+ [Allow users to view their own permissions](#security_iam_id-based-policy-examples-view-own-permissions)
+ [Allow users to view findings and issues](#security_iam_id-based-policy-examples-view-findings)
+ [Allow users to submit custom findings](#security_iam_id-based-policy-examples-submit-findings)

## Policy best practices
<a name="security_iam_service-with-iam-policy-best-practices"></a>

Identity-based policies determine whether someone can create, access, or delete AWS Continuum resources in your account. These actions can incur costs for your AWS account. When you create or edit identity-based policies, follow these guidelines and recommendations:
+ **Get started with AWS managed policies and move toward least-privilege permissions** – To get started granting permissions to your users and workloads, use the *AWS managed policies* that grant permissions for many common use cases. They are available in your AWS account. We recommend that you reduce permissions further by defining AWS customer managed policies that are specific to your use cases. For more information, see [AWS managed policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies) or [AWS managed policies for job functions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_job-functions.html) in the *IAM User Guide*.
+ **Apply least-privilege permissions** – When you set permissions with IAM policies, grant only the permissions required to perform a task. You do this by defining the actions that can be taken on specific resources under specific conditions, also known as *least-privilege permissions*. For more information about using IAM to apply permissions, see [ Policies and permissions in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html) in the *IAM User Guide*.
+ **Use conditions in IAM policies to further restrict access** – You can add a condition to your policies to limit access to actions and resources. For example, you can write a policy condition to specify that all requests must be sent using SSL. You can also use conditions to grant access to service actions if they are used through a specific AWS service, such as CloudFormation. For more information, see [ IAM JSON policy elements: Condition](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_condition.html) in the *IAM User Guide*.
+ **Use IAM Access Analyzer to validate your IAM policies to ensure secure and functional permissions** – IAM Access Analyzer validates new and existing policies so that the policies adhere to the IAM policy language (JSON) and IAM best practices. IAM Access Analyzer provides more than 100 policy checks and actionable recommendations to help you author secure and functional policies. For more information, see [Validate policies with IAM Access Analyzer](https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-policy-validation.html) in the *IAM User Guide*.
+ **Require multi-factor authentication (MFA)** – If you have a scenario that requires IAM users or a root user in your AWS account, turn on MFA for additional security. To require MFA when API operations are called, add MFA conditions to your policies. For more information, see [ Secure API access with MFA](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_mfa_configure-api-require.html) in the *IAM User Guide*.

For more information about best practices in IAM, see [Security best practices in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html) in the *IAM User Guide*.

## Using the AWS Continuum console
<a name="security_iam_id-based-policy-examples-console"></a>

To access the AWS Continuum console, you must have a minimum set of permissions. These permissions must allow you to list and view details about the AWS Continuum resources in your AWS account. If you create an identity-based policy that is more restrictive than the minimum required permissions, the console won't function as intended for entities (users or roles) with that policy.

You don't need to allow minimum console permissions for users that are making calls only to the AWS CLI or the AWS API. Instead, allow access to only the actions that match the API operation that they're trying to perform.

To use the AWS Continuum console, grant the operator the `continuum:` actions for their tasks. A broad operator grant of `continuum:*` includes all AWS Continuum actions. It does not grant IAM, AWS Config, or Amazon S3 permissions.

The following tables list permissions for console tasks. Grant the read actions for the pages and selectors that the operator uses in addition to each action that changes a resource. These action tables are not a complete IAM policy.

Use the following permissions for environment, scan, and results tasks.


| Task | Principal | Permissions and role requirements | 
| --- | --- | --- | 
| Open the overview and navigation | Console operator | `continuum:ListEnvironments`, `continuum:ListIntegrations`, and `continuum:ListCollectors`. The environment inventory can also require `continuum:GetEnvironment`. | 
| View an environment | Console operator | `continuum:ListEnvironments` and `continuum:GetEnvironment`. Scope these actions to the intended environment collection and resources. | 
| View issues, findings, and issue artifacts | Console operator | `continuum:ListCodeIssues`, `continuum:GetCodeIssue`, `continuum:ListCodeFindings`, `continuum:GetCodeFinding`, `continuum:ListCodeIssueArtifacts`, and `continuum:GetCodeIssueArtifact`. Issue and finding lists use the environment resource. Artifact actions use the code issue resource. Issue and finding detail actions use their corresponding resources. | 
| Create an environment that uses an integration | Console operator | `continuum:CreateEnvironment`, `continuum:ListIntegrations`, and `continuum:GetEnvironment`. Allow `continuum:CreateEnvironment` on `arn:aws:continuum:{{region}}:{{account-id}}:environments/*` for your account and Region, and on every referenced integration ARN. | 
| Edit an environment or its scan schedule | Console operator | `continuum:GetEnvironment` and `continuum:UpdateEnvironment`. Choosing sources also requires `continuum:ListIntegrations`. A source-bearing update requires `continuum:UpdateEnvironment` on the environment and every referenced integration ARN. | 
| Queue a scan and view scan history | Console operator | `continuum:CreateCodeScan` and `continuum:ListCodeScans`. Scan creation requires access to the environment and code-scan resources. | 
| Delete an environment | Console operator | `continuum:DeleteEnvironment`, `continuum:ListEnvironments`, and `continuum:GetEnvironment`. | 
| Submit a custom finding | Console operator | `continuum:CreateCodeFinding`, `continuum:ListCodeFindings`, and `continuum:GetCodeFinding`. | 

Use the following permissions to create and manage integrations and their roles.


| Task | Principal | Permissions and role requirements | 
| --- | --- | --- | 
| View integrations | Console operator | `continuum:ListIntegrations` and `continuum:GetIntegration`. These read permissions do not grant permission to reference an integration from an environment. | 
| Create a GitHub integration | Console operator | `continuum:StartIntegrationAuthorization`, `continuum:CreateIntegration`, `continuum:ListIntegrations`, and `continuum:GetIntegration`. GitHub installation and OAuth authorization are separate prerequisites. Creating a GitHub integration does not require `iam:PassRole`. | 
| Create an Amazon S3 integration | Console operator | `continuum:CreateIntegration`, `continuum:ListIntegrations`, and `continuum:GetIntegration`. The role picker requires `iam:ListRoles` with `Resource: "*"`. Bucket browsing requires `s3:ListAllMyBuckets` with `Resource: "*"`. Creation also requires `iam:PassRole` on the exact same-account integration role under `/continuum/integrations/`. Restrict `iam:PassRole` with `iam:PassedToService` set to `continuum.amazonaws.com`. | 
| Create the Amazon S3 integration role | Customer administrator | `iam:CreateRole` and `iam:PutRolePolicy`. The verification command also requires `iam:GetRole`. Create the role under `/continuum/integrations/`. For the trust and access policies, see [Granting access to the bucket](cv-getting-started.md#cv-getting-started-s3-role). | 
| Read source code and deliver patches | Amazon S3 integration role | AWS Continuum assumes this role by using its trust policy and matching external ID. Grant the integration role these permissions:+ Bucket – unconditional `s3:ListBucket` on the bucket.<br />+ Source objects – `s3:GetObject` and `s3:GetObjectVersion`.<br />+ Patch destination – `s3:PutObject`, `s3:GetObject`, and `s3:GetObjectVersion`.<br />These permissions belong to the integration role, not the console operator. | 
| Delete an integration | Console operator | `continuum:DeleteIntegration`, `continuum:ListIntegrations`, and `continuum:GetIntegration`. You cannot delete an integration that an environment references. | 

Use the following permissions for collector tasks.


| Task | Principal | Permissions and role requirements | 
| --- | --- | --- | 
| View collectors and their connections | Console operator | `continuum:ListCollectors`, `continuum:GetCollector`, `continuum:ListAssociatedEnvironments`, and `continuum:ListAssociatedCollectors`. | 
| Enable the AWS collector | Console operator | `continuum:CreateCollector`, `continuum:ListCollectors`, and `continuum:GetCollector`. The setup also requires `iam:CreateServiceLinkedRole`, `config:DescribeConfigurationRecorders`, and `config:PutServiceLinkedConfigurationRecorder`. The collector service-linked role is separate from integration and collector data-access roles. For more information, see [Using service-linked roles for AWS Continuum](using-service-linked-roles.md). | 
| Change a collector name or Kubernetes role | Console operator | `continuum:UpdateCollector`, `continuum:ListCollectors`, and `continuum:GetCollector`. Selecting an existing role also requires `iam:ListRoles` with `Resource: "*"`. Setting a Kubernetes role requires `iam:PassRole` on that exact role. Renaming the collector or removing the role does not require `iam:PassRole`. | 
| Associate a collector with an environment | Console operator and collector data-access role | The operator needs `continuum:AssociateCollector`, `continuum:ListEnvironments`, `continuum:GetEnvironment`, `continuum:ListCollectors`, `continuum:GetCollector`, `continuum:ListAssociatedCollectors`, and `continuum:ListAssociatedEnvironments`. The operator also needs `iam:PassRole` for the exact data-access role. The data-access role needs `continuum:GetCollectorDataAccessAuthorization` on the collector. Cross-account access also requires the collector resource policy to grant that action. | 
| Disassociate a collector from an environment | Console operator | `continuum:DisassociateCollector`, `continuum:GetEnvironment`, `continuum:GetCollector`, `continuum:ListAssociatedCollectors`, and `continuum:ListAssociatedEnvironments`. Disassociating a collector does not require `iam:PassRole`. | 
| View or edit a collector access policy | Console operator | `continuum:ListCollectors`, `continuum:GetCollector`, `continuum:GetResourcePolicy`, and `continuum:PutResourcePolicy`. Scope `continuum:GetResourcePolicy` and `continuum:PutResourcePolicy` to the collector ARN. A policy update replaces the policy document, so retain intended grants and use the current revision. | 
| Delete a collector | Console operator | `continuum:DeleteCollector`, `continuum:ListCollectors`, and `continuum:GetCollector`. Deleting a collector also requires `config:DeleteServiceLinkedConfigurationRecorder`. | 

For more information, see [Adding permissions to a user](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users_change-permissions.html#users_change_permissions-add-console) in the *IAM User Guide*.

## Allow users to view their own permissions
<a name="security_iam_id-based-policy-examples-view-own-permissions"></a>

This example shows how you might create a policy that allows IAM users to view the inline and managed policies that are attached to their user identity. This policy includes permissions to complete this action on the console or programmatically using the AWS CLI or AWS API.

```
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

## Allow users to view findings and issues
<a name="security_iam_id-based-policy-examples-view-findings"></a>

Use this policy to view findings and issues in one environment through the AWS Continuum API.

The `ListFindingsAndIssuesInEnvironment` statement grants list permissions on the environment's Amazon Resource Name (ARN). The `GetFindingsAndIssuesInEnvironment` statement grants get permissions on finding and issue ARNs within that environment.

For more information about permissions to use the console, see [Using the AWS Continuum console](#security_iam_id-based-policy-examples-console).

Replace {{region}} with your AWS Region. Replace {{account-id}} with your AWS account ID. Replace {{environment-id}} with the ID of the environment that you want to access.

Use the following policy:

```
{
   "Version": "2012-10-17",
   "Statement": [
      {
         "Sid": "ListFindingsAndIssuesInEnvironment",
         "Effect": "Allow",
         "Action": [
            "continuum:ListCodeFindings",
            "continuum:ListCodeIssues"
         ],
         "Resource": "arn:aws:continuum:{{region}}:{{account-id}}:environments/{{environment-id}}"
      },
      {
         "Sid": "GetFindingsAndIssuesInEnvironment",
         "Effect": "Allow",
         "Action": [
            "continuum:GetCodeFinding",
            "continuum:GetCodeIssue"
         ],
         "Resource": [
            "arn:aws:continuum:{{region}}:{{account-id}}:environments/{{environment-id}}/code-findings/*",
            "arn:aws:continuum:{{region}}:{{account-id}}:environments/{{environment-id}}/code-issues/*"
         ]
      }
   ]
}
```

## Allow users to submit custom findings
<a name="security_iam_id-based-policy-examples-submit-findings"></a>

Use this policy to submit custom findings to one environment through the AWS Continuum API.

`continuum:CreateCodeFinding` requires permission on both the environment ARN and the `code-findings/*` resources within that environment. Granting access to only one of these resources doesn't authorize the request.

For more information about permissions to use the console, see [Using the AWS Continuum console](#security_iam_id-based-policy-examples-console).

Replace {{region}} with your AWS Region. Replace {{account-id}} with your AWS account ID. Replace {{environment-id}} with the ID of the environment that you want to access.

Use the following policy:

```
{
   "Version": "2012-10-17",
   "Statement": [
      {
         "Sid": "SubmitCustomFindings",
         "Effect": "Allow",
         "Action": "continuum:CreateCodeFinding",
         "Resource": [
            "arn:aws:continuum:{{region}}:{{account-id}}:environments/{{environment-id}}",
            "arn:aws:continuum:{{region}}:{{account-id}}:environments/{{environment-id}}/code-findings/*"
         ]
      }
   ]
}
```