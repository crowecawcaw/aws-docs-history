AWS Data Pipeline is no longer available to new customers. Existing customers of AWS Data Pipeline can continue to use the service as normal. [Learn more](https://aws.amazon.com/blogs/big-data/migrate-workloads-from-aws-data-pipeline/ "https://aws.amazon.com/blogs/big-data/migrate-workloads-from-aws-data-pipeline/")

# Setting up for AWS Data Pipeline

Before you use AWS Data Pipeline for the first time, complete the following tasks.

###### Tasks

- [Sign up for AWS](#dp-sign-up "#dp-sign-up")
- [Create IAM Roles for AWS Data Pipeline and Pipeline Resources](#dp-iam-roles-new "#dp-iam-roles-new")
- [Allow IAM Principals (Users and Groups) to Perform Necessary Actions](#dp-iam-create-user-groups "#dp-iam-create-user-groups")
- [Granting programmatic access](#dp-grant-programmatic-access "#dp-grant-programmatic-access")
  After you complete these tasks, you can start using AWS Data Pipeline. For a basic tutorial, see [Getting Started with AWS Data Pipeline](dp-getting-started.md "dp-getting-started.md").

## Sign up for AWS

When you sign up for Amazon Web Services (AWS), your AWS account is automatically signed
up for all services in AWS, including AWS Data Pipeline. You are charged only for the services that you
use. For more information about AWS Data Pipeline usage rates, see [AWS Data Pipeline](http://aws.amazon.com/datapipeline/ "http://aws.amazon.com/datapipeline/").

### Sign up for an AWS account

To get started with AWS, you need an AWS account. For information about creating an AWS account, see
[Getting started with an AWS account](../../../accounts/latest/reference/getting-started.md "../../../accounts/latest/reference/getting-started.md")
in the _AWS Account Management Reference Guide_.

## Create IAM Roles for AWS Data Pipeline and Pipeline Resources

AWS Data Pipeline requires IAM roles that determine the permissions to perform actions and access AWS resources. The _pipeline role_ determines the permissions that AWS Data Pipeline has, and a _resource role_ determines the permissions that applications running on pipeline resources, such as EC2 instances, have. You specify these roles when you create a pipeline. Even if you do not specify a custom role and use the default roles `DataPipelineDefaultRole` and `DataPipelineDefaultResourceRole`, you must first create the roles and attach permissions policies. For more information, see [IAM Roles for AWS Data Pipeline](dp-iam-roles.md "dp-iam-roles.md").

## Allow IAM Principals (Users and Groups) to Perform Necessary Actions

To work with a pipeline, an IAM principal (a user or group) in your account must be allowed to perform required [AWS Data Pipeline actions](../APIReference/API_Operations.md "../APIReference/API_Operations.md") and actions for other services as defined by your pipeline.

To simplify permissions, the **AWSDataPipeline_FullAccess** managed policy is available for you to attach to IAM principals. This managed policy allows the principal to perform all actions that a user requires and the `iam:PassRole` action on the default roles used with AWS Data Pipeline when a custom role is not specified.

We highly recommend that you carefully evaluate this managed policy and restrict permissions only to those that your users require. If necessary, use this policy as a starting point, and then remove permissions to create a more restrictive inline permissions policy that you can attach to IAM principals. For more information and example permissions policies, see [Example Policies for AWS Data Pipeline](dp-example-tag-policies.md "dp-example-tag-policies.md")

A policy statement similar to the following example must be included in a policy attached to any IAM principal that uses the pipeline. This statement allows the IAM principal to perform the `PassRole` action on the roles that a pipeline uses. If you do not use default roles, replace `MyPipelineRole` and `MyResourceRole` with the custom roles that you create.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Action": "iam:PassRole",
 "Effect": "Allow",
 "Resource": [
 "arn:aws:iam::*:role/`MyPipelineRole`",
 "arn:aws:iam::*:role/`MyResourceRole`"
 ]
 }
 ]
}`

```

The following procedure demonstrates how to create an IAM group, attach the **AWSDataPipeline_FullAccess** managed policy to the group, and then add users to the group. You can use this procedure for any inline policy

###### To create a user group `DataPipelineDevelopers` and attach the **AWSDataPipeline_FullAccess** policy

1. Open the IAM console at
   [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. In the navigation pane, choose **Groups**, **Create New
   Group**.
3. Enter a **Group Name**, for example, `DataPipelineDevelopers`, and then choose **Next Step**.
4. Enter `AWSDataPipeline_FullAccess` for **Filter** and then select it from the list.
5. Choose **Next Step** and then choose **Create Group**.
6. To add users to the group:

   1. Select the group you created from the list of groups.
   2. Choose **Group Actions**, **Add Users to Group**.
   3. Select the users you want to add from the list and then choose **Add Users to Group**.

## Granting programmatic access

Users need programmatic access if they want to interact with AWS outside of the AWS Management Console. The way to grant programmatic access depends on the type of user that's accessing AWS.

To grant users programmatic access, choose one of the following options.

| Which user needs programmatic access?                        | To                                                                                                                                  | By                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| ------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| IAM                                                          | (Recommended) Use console credentials as temporary credentials to sign programmatic requests to the AWS CLI, AWS SDKs, or AWS APIs. | Following the instructions for the interface that you want to use.<br>• For the AWS CLI, see [Login for AWS local development](../../../cli/latest/userguide/cli-configure-sign-in.md "../../../cli/latest/userguide/cli-configure-sign-in.md") in<br>the _AWS Command Line Interface User Guide_.<br>• For AWS SDKs, see [Login for AWS local development](../../../sdkref/latest/guide/access-login.md "../../../sdkref/latest/guide/access-login.md") in the<br>_AWS SDKs and Tools Reference Guide_.                                                                                                                                                                                                                                                             |
| Workforce identity<br>(Users managed in IAM Identity Center) | Use temporary credentials to sign programmatic requests to the AWS CLI, AWS SDKs, or<br>AWS APIs.                                   | Following the instructions for the interface that you want to use.<br>• For the AWS CLI, see [Configuring the AWS CLI to use AWS IAM Identity Center](../../../cli/latest/userguide/cli-configure-sso.md "../../../cli/latest/userguide/cli-configure-sso.md") in the<br>_AWS Command Line Interface User Guide_.<br>• For AWS SDKs, tools, and AWS APIs, see [IAM Identity Center<br>authentication](../../../sdkref/latest/guide/access-sso.md "../../../sdkref/latest/guide/access-sso.md") in the _AWS SDKs and Tools Reference Guide_.                                                                                                                                                                                                                          |
| IAM                                                          | Use temporary credentials to sign programmatic requests to the AWS CLI, AWS SDKs, or<br>AWS APIs.                                   | Following the instructions in [Using temporary<br>credentials with AWS resources](../../../IAM/latest/UserGuide/id_credentials_temp_use-resources.md "../../../IAM/latest/UserGuide/id_credentials_temp_use-resources.md") in the _IAM User Guide_.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| IAM                                                          | (Not recommended)Use long-term credentials to sign programmatic requests<br>to the AWS CLI, AWS SDKs, or AWS APIs.                  | Following the instructions for the interface that you want to use.<br>• For the AWS CLI, see [Authenticating using IAM user credentials](../../../cli/latest/userguide/cli-authentication-user.md "../../../cli/latest/userguide/cli-authentication-user.md") in<br>the _AWS Command Line Interface User Guide_.<br>• For AWS SDKs and tools, see [Authenticate using long-term credentials](../../../sdkref/latest/guide/access-iam-users.md "../../../sdkref/latest/guide/access-iam-users.md") in the<br>_AWS SDKs and Tools Reference Guide_.<br>• For AWS APIs, see [Managing access keys for<br>IAM users](../../../IAM/latest/UserGuide/id_credentials_access-keys.md "../../../IAM/latest/UserGuide/id_credentials_access-keys.md") in the _IAM User Guide_. |
