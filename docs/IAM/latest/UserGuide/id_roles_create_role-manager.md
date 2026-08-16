# Create roles automatically with role manager

Many AWS services depend on IAM roles to perform actions on your behalf. IAM role
manager is an optional account setting that automatically provisions such roles, so you don't
have to set them up yourself. Role manager is designed to help you get started building with
AWS services without additional manual IAM configuration.

Role manager is available in select AWS service consoles, listed in [AWS service consoles that support role manager](#id_roles_create_role-manager_supported-services "#id_roles_create_role-manager_supported-services") on this page.

## How role manager works

When role manager is enabled, it provides roles appropriate to the service and the resource as
part of the relevant console workflow. Supported service consoles will indicate when role manager is
available. No additional action is required to accept the role that role manager provides. For example,
when you create an AWS Lambda function in the console, Lambda uses role manager to create the function's
execution role by default. To use a different role, choose an existing role or manually create a new one.

Role manager works by applying a role template, a definition of a role's trust policy and permissions for a service and use case.
To learn more about the template that
each service uses, see [Overview of role templates](id_roles_create_role-template.md "id_roles_create_role-template.md"). A template for a defined task grants only the
actions that task needs. A template for open-ended work, such as running your own code, grants broad
access to AWS APIs so you can build without granting access to each service yourself.

IAM roles created by role manager behave like any other role you create. You can view, edit,
or delete them. Each role also records the role template it came from, so you can identify the roles
that role manager created. AWS CloudTrail logs when role manager creates roles so you can audit when
and how each role was created.

## Prerequisites

Enabling or disabling role manager requires the
`iam:PutAccountProperties` permission. The AWS managed policy
`IAMFullAccess` includes it. For all the permissions that role manager
requires, see [Apply least-privilege permissions to a role created automatically](id_roles_create_role-manager_least-privilege.md "id_roles_create_role-manager_least-privilege.md")

## How to enable and disable role manager (console)

Role manager may be enabled or disabled on the **Account settings** page
in the IAM console. That page also shows whether role manager is enabled for the
account.

1. Sign in to the AWS Management Console and open the IAM console.
2. In the navigation pane, choose **Account settings**.
3. In the **role manager** section, choose
   **Enable** or **Disable**.

Roles created by role manager are not deleted when you disable role manager.

## AWS service consoles that support role manager

Role manager supports role creation for the following AWS service consoles:

- AWS Elastic Beanstalk
- Amazon EventBridge
- AWS Lambda
- Amazon SageMaker Unified Studio
- AWS Secrets Manager
- AWS Step Functions

AWS will continue adding service support over time. To learn more about the role
template that each service uses, see [Overview of role templates](id_roles_create_role-template.md "id_roles_create_role-template.md").

## Related information

- [Manage access to role manager](id_roles_create_role-manager_enable-use.md "id_roles_create_role-manager_enable-use.md")
- [Apply least-privilege permissions to a role created automatically](id_roles_create_role-manager_least-privilege.md "id_roles_create_role-manager_least-privilege.md")
- [Overview of role templates](id_roles_create_role-template.md "id_roles_create_role-template.md")
