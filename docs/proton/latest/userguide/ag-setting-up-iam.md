End of support notice: On October 7, 2026, AWS will end support for AWS Proton. After October
7, 2026, you will no longer be able to access the AWS Proton console or AWS Proton resources. Your deployed infrastructure
will remain intact. For more information, see [AWS Proton Service Deprecation and Migration
Guide](proton-end-of-support.md "proton-end-of-support.md").

# Setting up with IAM

When you sign up for AWS, your AWS account is automatically signed up for all services in AWS, including AWS Proton. You're charged only for the
services and resources that you use.

###### Note

You and your team, including administrators and developers, must all be under the same account.

## Sign up for AWS

If you do not have an AWS account, complete the following steps to create one.

###### To sign up for an AWS account

1. Open [https://portal.aws.amazon.com/billing/signup](https://portal.aws.amazon.com/billing/signup "https://portal.aws.amazon.com/billing/signup").
2. Follow the online instructions.

Part of the sign-up procedure involves receiving a phone call or text message and entering
a verification code on the phone keypad.

When you sign up for an AWS account, an _AWS account root user_ is created. The root user has access to all AWS services
and resources in the account. As a security best practice, assign administrative access to a user, and use only the root user to perform [tasks that require root user access](../../../IAM/latest/UserGuide/id_root-user.md#root-user-tasks "../../../IAM/latest/UserGuide/id_root-user.md#root-user-tasks").

## Create an IAM user

To create an administrator user, choose one of the following options.

| Choose one way to manage your administrator | To                                                                                                                                                                                                                                                                                                                                                  | By                                                                                                                                                                                                                                          | You can also                                                                                                                                                                                                                                          |
| ------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| In IAM Identity Center (Recommended)        | Use short-term credentials to access AWS.This aligns with the security best<br>practices. For information about best practices, see [Security best<br>practices in IAM](../../../IAM/latest/UserGuide/best-practices.md#bp-users-federation-idp "../../../IAM/latest/UserGuide/best-practices.md#bp-users-federation-idp") in the _IAM User Guide_. | Following the instructions in [Getting started](../../../singlesignon/latest/userguide/getting-started.md "../../../singlesignon/latest/userguide/getting-started.md") in the<br>_AWS IAM Identity Center User Guide_.                      | Configure programmatic access by [Configuring the AWS CLI to use<br>AWS IAM Identity Center](../../../cli/latest/userguide/cli-configure-sso.md "../../../cli/latest/userguide/cli-configure-sso.md") in the _AWS Command Line Interface User Guide_. |
| In IAM (Not recommended)                    | Use long-term credentials to access AWS.                                                                                                                                                                                                                                                                                                            | Following the instructions in [Create an IAM user for emergency access](../../../IAM/latest/UserGuide/getting-started-emergency-iam-user.md "../../../IAM/latest/UserGuide/getting-started-emergency-iam-user.md") in the _IAM User Guide_. | Configure programmatic access by [Manage access keys for IAM<br>users](../../../IAM/latest/UserGuide/id_credentials_access-keys.md "../../../IAM/latest/UserGuide/id_credentials_access-keys.md") in the _IAM User Guide_.                            |

## Setting up AWS Proton service roles

There are a few IAM roles that you might want to create for different parts of your AWS Proton solution. You can create them in advance using the IAM
console, or you can use the AWS Proton console to create them for you.

Create AWS Proton _environment roles_ to allow AWS Proton to make API calls to other AWS services, like AWS CloudFormation, AWS CodeBuild, and various
compute and storage services, on your behalf to provision resources for you. A _AWS-managed provisioning role_ is required when an environment or
any of the service instances running in it use [AWS-managed provisioning](ag-works-prov-methods.md#ag-works-prov-methods-direct "ag-works-prov-methods.md#ag-works-prov-methods-direct"). A _CodeBuild
role_ is required when an environment or any of its service instances use [CodeBuild
provisioning](ag-works-prov-methods.md#ag-works-prov-methods-codebuild "ag-works-prov-methods.md#ag-works-prov-methods-codebuild"). To learn more about the AWS Proton environment roles, see [IAM Roles](ag-environment-roles.md "ag-environment-roles.md"). When you [create an environment](ag-create-env.md "ag-create-env.md"), you can use the AWS Proton console to choose an existing role for either of these two roles, or to
create a role with administrative privileges for you.

Similarly, create AWS Proton _pipeline roles_ to allow AWS Proton to make API calls to other services on your behalf to provision a CI/CD
pipeline for you. To learn more about the AWS Proton pipeline roles, see [AWS Proton pipeline service roles](security_iam_service-role-policy-examples.md#codepipeline-proton-svc-role "security_iam_service-role-policy-examples.md#codepipeline-proton-svc-role"). For more information about
configuring CI/CD settings, see [Setting up account CI/CD pipeline settings](setting-up-for-service.md#setting-up-pr-pipelines "setting-up-for-service.md#setting-up-pr-pipelines").

###### Note

Because we don't know which resources you will define in your AWS Proton templates, the roles that you create using the console have broad permissions
and can be used as both the AWS Proton pipeline service roles and the AWS Proton service roles. For production deployments, we recommend that you scope down the
permissions to the specific resources that will be deployed by creating customized policies for both the AWS Proton pipeline service roles and the AWS Proton
environment service roles. You can create and customize these roles by using the AWS CLI or IAM. For more information, see [Service roles for AWS Proton](security_iam_service-with-iam.md#security_iam_service-with-iam-roles-service "security_iam_service-with-iam.md#security_iam_service-with-iam-roles-service") and [Create a service](ag-create-svc.md "ag-create-svc.md").
