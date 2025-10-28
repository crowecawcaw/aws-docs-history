# AWS Serverless Application Repository Identity-Based

Policy Examples

By default, IAM users and roles don't have permission to create or modify
AWS Serverless Application Repository resources. They also can't perform tasks using the AWS Management Console, AWS CLI, or
AWS API. An IAM administrator must create IAM policies that grant users and roles
permission to perform specific API operations on the specified resources they need. The
administrator must then attach those policies to the IAM users or groups that require
those permissions.

To learn how to create an IAM identity-based policy by using these example JSON policy
documents, see [Creating Policies on the JSON Tab](../../../IAM/latest/UserGuide/access_policies_create.md#access_policies_create-json-editor "../../../IAM/latest/UserGuide/access_policies_create.md#access_policies_create-json-editor") in the
_IAM User Guide_.

###### Topics

- [Policy Best
  Practices](#security_iam_service-with-iam-policy-best-practices "#security_iam_service-with-iam-policy-best-practices")
- [Using the
  AWS Serverless Application Repository Console](#security_iam_id-based-policy-examples-console "#security_iam_id-based-policy-examples-console")
- [Allow Users
  to View Their Own Permissions](#security_iam_id-based-policy-examples-view-own-permissions "#security_iam_id-based-policy-examples-view-own-permissions")
- [Customer Managed Policy Examples](#security_iam_id-examples "#security_iam_id-examples")

## Policy Best

Practices

Identity-based policies are very powerful. They determine whether someone can create, access, or delete AWS Serverless Application Repository resources in your
account. These actions can incur costs for your AWS account. When you create or edit identity-based policies, follow these guidelines and
recommendations:

- **Grant least privilege** – When you
  create custom policies, grant only the permissions required to perform a task.
  Start with a minimum set of permissions and grant additional permissions as
  necessary. Doing so is more secure than starting with permissions that are too
  lenient and then trying to tighten them later. For more information, see [Grant Least
  Privilege](../../../IAM/latest/UserGuide/best-practices.md#grant-least-privilege "../../../IAM/latest/UserGuide/best-practices.md#grant-least-privilege") in the _IAM User Guide_.
- **Enable MFA for sensitive operations** –
  For extra security, require IAM users to use multi-factor authentication (MFA)
  to access sensitive resources or API operations. For more information, see
  [Using Multi-Factor
  Authentication (MFA) in AWS](../../../IAM/latest/UserGuide/id_credentials_mfa.md "../../../IAM/latest/UserGuide/id_credentials_mfa.md") in the
  _IAM User Guide_.
- **Use policy conditions for extra security**
  – To the extent that it's practical, define the conditions under
  which your identity-based policies allow access to a resource. For example, you
  can write conditions to specify a range of allowable IP addresses that a request
  must come from. You can also write conditions to allow requests only within a
  specified date or time range, or to require the use of SSL or MFA. For more
  information, see [IAM JSON
  Policy Elements: Condition](../../../IAM/latest/UserGuide/reference_policies_elements_condition.md "../../../IAM/latest/UserGuide/reference_policies_elements_condition.md") in the
  _IAM User Guide_.

## Using the

AWS Serverless Application Repository Console

The AWS Serverless Application Repository console provides an integrated environment for you to discover and
manage AWS Serverless Application Repository applications. The console provides features and workflows that often
require permissions to manage an AWS Serverless Application Repository application in addition to the API-specific
permissions documented in the [AWS Serverless Application Repository API Permissions: Actions and
Resources Reference](serverlessrepo-api-permissions-ref.md "serverlessrepo-api-permissions-ref.md").

For more information about permissions needed to use the AWS Serverless Application Repository console, see [Customer Managed Policy Examples](#security_iam_id-examples "#security_iam_id-examples").

## Allow Users

to View Their Own Permissions

This example shows how you might create a policy that allows IAM users to view the inline and managed policies that are attached to their user
identity. This policy includes permissions to complete this action on the console or programmatically using the AWS CLI or AWS API.

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

## Customer Managed Policy Examples

The examples in this section provide a group of sample policies that you can attach to
a user. If you're new to creating policies, we recommend that you first create an IAM
user in your account and attach the policies to the user in sequence. You can also use
these examples to create a single customized policy that includes permissions to perform
multiple actions, and then attach it to the user.

For more information about how to attach policies to users, see [Adding Permissions to a User](../../../IAM/latest/UserGuide/id_users_change-permissions.md#users_change_permissions-add-console "../../../IAM/latest/UserGuide/id_users_change-permissions.md#users_change_permissions-add-console") in the
_IAM User Guide_.

###### Examples

- [Publisher Example 1:
  Allow a Publisher to List Applications](#security_iam_id-example-publisher-list-apps "#security_iam_id-example-publisher-list-apps")
- [Publisher
  Example 2: Allow a Publisher to View Details of an Application or Application
  Version](#security_iam_id-example-publisher-view-app-details "#security_iam_id-example-publisher-view-app-details")
- [Publisher Example 3:
  Allow a Publisher to Create an Application or Application Version](#security_iam_id-example-publisher-create-apps "#security_iam_id-example-publisher-create-apps")
- [Publisher
  Example 4: Allow a Publisher to Create an Application Policy to Share
  Applications with Others](#security_iam_id-example-publisher-create-app-policies "#security_iam_id-example-publisher-create-app-policies")
- [Consumer Example 1:
  Allow a Consumer to Search for Applications](#security_iam_id-example-consumer-search-apps "#security_iam_id-example-consumer-search-apps")
- [Consumer Example
  2: Allow a Consumer to View Details of an Application](#security_iam_id-example-consumer-view-app-details "#security_iam_id-example-consumer-view-app-details")
- [Consumer Example 3: Allow
  a Consumer to Deploy an Application](#security_iam_id-example-consumer-deploy-apps "#security_iam_id-example-consumer-deploy-apps")
- [Consumer
  Example 4: Deny Access to Deployment Assets](#security_iam_id-example-consumer-deny-deployment-assets "#security_iam_id-example-consumer-deny-deployment-assets")
- [Consumer Example 5: Prevent a Consumer Searching and Deploying Public Applications](#access-control-identity-based-example-consumer-deny-public-apps "#access-control-identity-based-example-consumer-deny-public-apps")

### Publisher Example 1:

Allow a Publisher to List Applications

An IAM user in your account must have permissions for the
`serverlessrepo:ListApplications` operation before the user can see
anything in the console. When you grant these permissions, the console can show the
list of AWS Serverless Application Repository applications in the AWS account created in the specific AWS Region
that the user belongs to.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "ListExistingApplications",
 "Effect": "Allow",
 "Action": [
 "serverlessrepo:ListApplications"
 ],
 "Resource": "*"
 }
 ]
}`

```

 

### Publisher

Example 2: Allow a Publisher to View Details of an Application or Application
Version

A user can select an AWS Serverless Application Repository application and view details of the application. Such
details include author, description, versions, and other configuration information.
To do this, the user needs permissions for the
`serverlessrepo:GetApplication` and
`serverlessrepo:ListApplicationVersions` API operations for the
AWS Serverless Application Repository.

In the following example, these permissions are granted for the specific
application whose Amazon Resource Name (ARN) is specified as the
`Resource` value.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "ViewApplication",
 "Effect": "Allow",
 "Action": [
 "serverlessrepo:GetApplication",
 "serverlessrepo:ListApplicationVersions"
 ],
 "Resource": "arn:aws:serverlessrepo:`us-east-1`:`111122223333`:applications/`application-name`"
 }
 ]
}`

```

 

### Publisher Example 3:

Allow a Publisher to Create an Application or Application Version

If you want to allow a user to have permissions to create AWS Serverless Application Repository applications, you
need to grant permissions to the `serverlessrepo:CreateApplication` and
`serverlessrepo:CreateApplicationVersions` operations, as shown in
the following policy.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "CreateApplication",
 "Effect": "Allow",
 "Action": [
 "serverlessrepo:CreateApplication",
 "serverlessrepo:CreateApplicationVersion"
 ],
 "Resource": "*"
 }
 ]
}`

```

 

### Publisher

Example 4: Allow a Publisher to Create an Application Policy to Share
Applications with Others

In order for users to share applications with others, you must grant them
permissions to create application policies, as shown in the following policy.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "ShareApplication",
 "Effect": "Allow",
 "Action": [
 "serverlessrepo:PutApplicationPolicy",
 "serverlessrepo:GetApplicationPolicy"
 ],
 "Resource": "*"
 }
 ]
}`

```

 

### Consumer Example 1:

Allow a Consumer to Search for Applications

For consumers to search for applications, you must grant them the following
permissions.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "SearchApplications",
 "Effect": "Allow",
 "Action": [
 "serverlessrepo:SearchApplications"
 ],
 "Resource": "*"
 }
 ]
}`

```

 

### Consumer Example

2: Allow a Consumer to View Details of an Application

A user can select an AWS Serverless Application Repository application and view details of the application, such
as author, description, versions, and other configuration information. To do so, the
user must have permissions for the following AWS Serverless Application Repository operations.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "ViewApplication",
 "Effect": "Allow",
 "Action": [
 "serverlessrepo:GetApplication",
 "serverlessrepo:ListApplicationVersions"
 ],
 "Resource": "*"
 }
 ]
}`

```

 

### Consumer Example 3: Allow

a Consumer to Deploy an Application

For customers to deploy applications, you must grant them permissions to perform a
number of operations. The following policy provides customers with the required
permissions.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "DeployApplication",
 "Effect": "Allow",
 "Action": [
 "serverlessrepo:CreateCloudFormationChangeSet",
 "cloudformation:CreateChangeSet",
 "cloudformation:ExecuteChangeSet",
 "cloudformation:DescribeStacks"

 ],
 "Resource": "*"
 }
 ]
}`

```

###### Note

Deploying an application might require permissions to use additional AWS
resources. Because the AWS Serverless Application Repository uses the same underlying deployment mechanism as
AWS CloudFormation, see [Controlling Access
with AWS Identity and Access Management](../../../AWSCloudFormation/latest/UserGuide/using-iam-template.md "../../../AWSCloudFormation/latest/UserGuide/using-iam-template.md") for more information. For
help with deployment issues related to permissions, see [Troubleshooting: Insufficient IAM Permissions](../../../AWSCloudFormation/latest/UserGuide/troubleshooting.md#troubleshooting-errors-insufficient-iam-permissions "../../../AWSCloudFormation/latest/UserGuide/troubleshooting.md#troubleshooting-errors-insufficient-iam-permissions").

### Consumer

Example 4: Deny Access to Deployment Assets

When an application is privately shared with an AWS account, by default, all users
in that account can access the deployment assets of all other users in the same
account. The following policy prevents users in an account from accessing deployment
assets, which are stored in the Amazon S3 bucket for the AWS Serverless Application Repository.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "DenyDeploymentAssetAccess",
 "Effect": "Deny",
 "Action": [
 "s3:GetObject"
 ],
 "Resource": [
 "arn:aws:s3:::awsserverlessrepo-changesets*/*"
 ]
 }
 ]
}`

```

### Consumer Example 5: Prevent a Consumer Searching and Deploying Public Applications

You can prevent users from performing certain actions on applications.

The following policy applies to public applications by specifying
`serverlessrepo:applicationType` to be `public`. It prevents
users from performing a number of actions by specifying `Effect` to be
`Deny`. For more information about condition keys available for AWS Serverless Application Repository,
see [Actions, Resources, and Condition Keys for AWS Serverless Application Repository](../../../IAM/latest/UserGuide/list_awsserverlessapplicationrepository.md "../../../IAM/latest/UserGuide/list_awsserverlessapplicationrepository.md").

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Condition": {
 "StringEquals": {
 "serverlessrepo:applicationType": "public"
 }
 },
 "Action": [
 "serverlessrepo:SearchApplications",
 "serverlessrepo:GetApplication",
 "serverlessrepo:CreateCloudFormationTemplate",
 "serverlessrepo:CreateCloudFormationChangeSet",
 "serverlessrepo:ListApplicationVersions",
 "serverlessrepo:ListApplicationDependencies"
 ],
 "Resource": "*",
 "Effect": "Deny"
 }
 ]
}`

```

###### Note

This policy statement can also be used as a Service Control
Policy and applied to an AWS organization. For more information about Service Control Policies, see
[Service Control Policies](../../../organizations/latest/userguide/orgs_manage_policies_scp.md "../../../organizations/latest/userguide/orgs_manage_policies_scp.md")
in the _AWS Organizations User Guide_.
