# Managing AWS SAM permissions with CloudFormation mechanisms

To control access to AWS resources, the AWS Serverless Application Model (AWS SAM) can use the same mechanisms as CloudFormation. For more
information, see [Controlling access with
AWS Identity and Access Management](../../../AWSCloudFormation/latest/UserGuide/using-iam-template.md "../../../AWSCloudFormation/latest/UserGuide/using-iam-template.md") in the _AWS CloudFormation User Guide_.

There are three main options for granting a user permission to manage serverless
applications. Each option provides users with different levels of access control.

- Grant administrator permissions.
- Attach necessary AWS managed policies.
- Grant specific AWS Identity and Access Management (IAM) permissions.
  Depending on which option you choose, users can manage only serverless applications
  containing AWS resources that they have permission to access.

The following sections describe each option in more detail.

## Grant administrator permissions

If you grant administrator permissions to a user, they can manage serverless
applications that contain any combination of AWS resources. This is the simplest
option, but it also grants users the broadest set of permissions, which therefore
enables them to perform actions with the highest impact.

For more information about granting administrator permissions to a user, see [Creating your
first IAM admin user and group](../../../IAM/latest/UserGuide/getting-started_create-admin-group.md "../../../IAM/latest/UserGuide/getting-started_create-admin-group.md") in the
_IAM User Guide_.

## Attach necessary AWS managed

policies

You can grant users a subset of permissions using [AWS managed policies](../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies "../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies"), rather than granting full administrator
permissions. If you use this option, make sure that the set of AWS managed policies
covers all of the actions and resources required for the serverless applications that
the users manage.

For example, the following AWS managed policies are sufficient to [deploy the sample Hello World
application](serverless-getting-started-hello-world.md "serverless-getting-started-hello-world.md"):

- AWSCloudFormationFullAccess
- IAMFullAccess
- AWSLambda_FullAccess
- AmazonAPIGatewayAdministrator
- AmazonS3FullAccess
- AmazonEC2ContainerRegistryFullAccess

For information about attaching policies to an IAM user, see [Changing permissions for an IAM user](../../../IAM/latest/UserGuide/id_users_change-permissions.md "../../../IAM/latest/UserGuide/id_users_change-permissions.md") in the
_IAM User Guide_.

## Grant specific IAM

permissions

For the most granular level of access control, you can grant specific IAM
permissions to users using [policy
statements](../../../IAM/latest/UserGuide/reference_policies_elements_statement.md "../../../IAM/latest/UserGuide/reference_policies_elements_statement.md"). If you use this option, make sure that the policy statement
includes all of the actions and resources required for the serverless applications that
the users manage.

The best practice with this option is to deny users the permission to create roles,
including Lambda execution roles, so they can't grant themselves escalated permissions.
So, you as the administrator must first create a [Lambda execution role](../../../lambda/latest/dg/lambda-intro-execution-role.md "../../../lambda/latest/dg/lambda-intro-execution-role.md")
that will be specified in the serverless applications that users will manage. For
information about creating Lambda execution roles, see [Creating an execution role in the IAM console](../../../lambda/latest/dg/lambda-intro-execution-role.md#permissions-executionrole-console "../../../lambda/latest/dg/lambda-intro-execution-role.md#permissions-executionrole-console").

For the [sample Hello World
application](serverless-getting-started-hello-world.md "serverless-getting-started-hello-world.md") the **AWSLambdaBasicExecutionRole**
is sufficient to run the application. After you've created a Lambda execution role,
modify the AWS SAM template file of the sample Hello World application to add the
following property to the `AWS::Serverless::Function` resource:

```
  Role: `lambda-execution-role-arn`

```

With the modified Hello World application in place, the following policy statement
grants sufficient permissions for users to deploy, update, and delete the
application:

###### Note

The example policy statement in this section grants sufficient permission for you to
deploy, update, and delete the the [sample Hello World
application](serverless-getting-started-hello-world.md "serverless-getting-started-hello-world.md"). If you add additional resource types to your application,
you need to update the policy statement to include the following:

1. Permission for your application to call the service's actions.
2. The service principal, if needed for the service's actions.
   For example, if you add a Step Functions workflow, you may need to add
   permissions for actions listed [here](../../../service-authorization/latest/reference/list_awsstepfunctions.md#awsstepfunctions-actions-as-permissions "../../../service-authorization/latest/reference/list_awsstepfunctions.md#awsstepfunctions-actions-as-permissions"), and the `states.amazonaws.com` service
   principal.

For more information about IAM policies, see [Managing IAM
policies](../../../IAM/latest/UserGuide/access_policies_manage.md "../../../IAM/latest/UserGuide/access_policies_manage.md") in the _IAM User Guide_.
