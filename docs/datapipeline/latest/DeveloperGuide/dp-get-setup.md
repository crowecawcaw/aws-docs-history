

AWS Data Pipeline is no longer available to new customers. Existing customers of AWS Data Pipeline can continue to use the service as normal. [Learn more](https://aws.amazon.com/blogs/big-data/migrate-workloads-from-aws-data-pipeline/)

# Setting up for AWS Data Pipeline
<a name="dp-get-setup"></a>

Before you use AWS Data Pipeline for the first time, complete the following tasks.

**Topics**
+ [Sign up for AWS](#dp-sign-up)
+ [Create IAM Roles for AWS Data Pipeline and Pipeline Resources](#dp-iam-roles-new)
+ [Allow IAM Principals (Users and Groups) to Perform Necessary Actions](#dp-iam-create-user-groups)
+ [Granting programmatic access](#dp-grant-programmatic-access)

After you complete these tasks, you can start using AWS Data Pipeline. For a basic tutorial, see [Getting Started with AWS Data Pipeline](dp-getting-started.md).

## Sign up for AWS
<a name="dp-sign-up"></a>

When you sign up for Amazon Web Services (AWS), your AWS account is automatically signed up for all services in AWS, including AWS Data Pipeline. You are charged only for the services that you use. For more information about AWS Data Pipeline usage rates, see [AWS Data Pipeline](http://aws.amazon.com/datapipeline/).

### Sign up for an AWS account
<a name="sign-up-for-aws"></a>

To get started with AWS, you need an AWS account. For information about creating an AWS account, see [Getting started with an AWS account](https://docs.aws.amazon.com/accounts/latest/reference/getting-started.html) in the *AWS Account Management Reference Guide*.

## Create IAM Roles for AWS Data Pipeline and Pipeline Resources
<a name="dp-iam-roles-new"></a>

AWS Data Pipeline requires IAM roles that determine the permissions to perform actions and access AWS resources. The *pipeline role* determines the permissions that AWS Data Pipeline has, and a *resource role* determines the permissions that applications running on pipeline resources, such as EC2 instances, have. You specify these roles when you create a pipeline. Even if you do not specify a custom role and use the default roles `DataPipelineDefaultRole` and `DataPipelineDefaultResourceRole`, you must first create the roles and attach permissions policies. For more information, see [IAM Roles for AWS Data Pipeline](dp-iam-roles.md).

## Allow IAM Principals (Users and Groups) to Perform Necessary Actions
<a name="dp-iam-create-user-groups"></a>

To work with a pipeline, an IAM principal (a user or group) in your account must be allowed to perform required [AWS Data Pipeline actions](https://docs.aws.amazon.com/datapipeline/latest/APIReference/API_Operations.html) and actions for other services as defined by your pipeline.

To simplify permissions, the **AWSDataPipeline\_FullAccess** managed policy is available for you to attach to IAM principals. This managed policy allows the principal to perform all actions that a user requires and the `iam:PassRole` action on the default roles used with AWS Data Pipeline when a custom role is not specified.

We highly recommend that you carefully evaluate this managed policy and restrict permissions only to those that your users require. If necessary, use this policy as a starting point, and then remove permissions to create a more restrictive inline permissions policy that you can attach to IAM principals. For more information and example permissions policies, see [Example Policies for AWS Data Pipeline](dp-example-tag-policies.md)

A policy statement similar to the following example must be included in a policy attached to any IAM principal that uses the pipeline. This statement allows the IAM principal to perform the `PassRole` action on the roles that a pipeline uses. If you do not use default roles, replace `{{MyPipelineRole}}` and `{{MyResourceRole}}` with the custom roles that you create.

------
#### [ JSON ]

****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
        {
            "Action": "iam:PassRole",
            "Effect": "Allow",
            "Resource": [
                "arn:aws:iam::*:role/{{MyPipelineRole}}",
                "arn:aws:iam::*:role/{{MyResourceRole}}"
            ]
        }
    ]
}
```

------

The following procedure demonstrates how to create an IAM group, attach the **AWSDataPipeline\_FullAccess** managed policy to the group, and then add users to the group. You can use this procedure for any inline policy

**To create a user group `DataPipelineDevelopers` and attach the **AWSDataPipeline\_FullAccess** policy**

1. Open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/).

1. In the navigation pane, choose **Groups**, **Create New Group**.

1. Enter a **Group Name**, for example, **DataPipelineDevelopers**, and then choose **Next Step**.

1. Enter **AWSDataPipeline\_FullAccess** for **Filter** and then select it from the list.

1. Choose **Next Step** and then choose **Create Group**.

1. To add users to the group:

   1. Select the group you created from the list of groups.

   1. Choose **Group Actions**, **Add Users to Group**.

   1. Select the users you want to add from the list and then choose **Add Users to Group**.

## Granting programmatic access
<a name="dp-grant-programmatic-access"></a>

Users need programmatic access if they want to interact with AWS outside of the AWS Management Console. The way to grant programmatic access depends on the type of user that's accessing AWS.

To grant users programmatic access, choose one of the following options.



| Which user needs programmatic access? | To | By | 
| --- | --- | --- | 
| IAM | (Recommended) Use console credentials as temporary credentials to sign programmatic requests to the AWS CLI, AWS SDKs, or AWS APIs. | Following the instructions for the interface that you want to use.+  For the AWS CLI, see [Login for AWS local development](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-sign-in.html) in the *AWS Command Line Interface User Guide*. <br />+  For AWS SDKs, see [Login for AWS local development](https://docs.aws.amazon.com/sdkref/latest/guide/access-login.html) in the *AWS SDKs and Tools Reference Guide*.  | 
| Workforce identity<br />(Users managed in IAM Identity Center) | Use temporary credentials to sign programmatic requests to the AWS CLI, AWS SDKs, or AWS APIs. | Following the instructions for the interface that you want to use.+  For the AWS CLI, see [Configuring the AWS CLI to use AWS IAM Identity Center](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-sso.html) in the *AWS Command Line Interface User Guide*. <br />+  For AWS SDKs, tools, and AWS APIs, see [IAM Identity Center authentication](https://docs.aws.amazon.com/sdkref/latest/guide/access-sso.html) in the *AWS SDKs and Tools Reference Guide*.  | 
| IAM | Use temporary credentials to sign programmatic requests to the AWS CLI, AWS SDKs, or AWS APIs. | Following the instructions in [Using temporary credentials with AWS resources](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp_use-resources.html) in the IAM User Guide. | 
| IAM | (Not recommended)Use long-term credentials to sign programmatic requests to the AWS CLI, AWS SDKs, or AWS APIs. | Following the instructions for the interface that you want to use.+  For the AWS CLI, see [Authenticating using IAM user credentials](https://docs.aws.amazon.com/cli/latest/userguide/cli-authentication-user.html) in the *AWS Command Line Interface User Guide*. <br />+  For AWS SDKs and tools, see [Authenticate using long-term credentials](https://docs.aws.amazon.com/sdkref/latest/guide/access-iam-users.html) in the *AWS SDKs and Tools Reference Guide*. <br />+  For AWS APIs, see [Managing access keys for IAM users](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html) in the *IAM User Guide*.  | 