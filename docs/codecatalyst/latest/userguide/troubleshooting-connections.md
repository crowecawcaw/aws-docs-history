Amazon CodeCatalyst will no longer be open to new customers starting on November
7, 2025. If you would like to use the service, please sign up prior to November 7, 2025. For
more information, see [How to migrate from CodeCatalyst](migration.md "migration.md").

# Troubleshooting problems with accounts

associated with your space

In CodeCatalyst, you can add an AWS account to your space to grant permissions to
resources and for billing purposes. The following information can help you troubleshoot
common issues with associated accounts in CodeCatalyst.

###### Topics

- [My AWS account connection request
  receives an invalid token error](#troubleshooting-connection-token "#troubleshooting-connection-token")
- [My Amazon CodeCatalyst project workflow fails
  with an error for the configured account, environment, or IAM role](#connections-troubleshoot-workflow "#connections-troubleshoot-workflow")
- [I need an associated account,
  role, and environment to create a project](#connections-troubleshoot-environment "#connections-troubleshoot-environment")
- [I cannot access the
  Amazon CodeCatalyst Spaces page in the AWS Management Console](#connections-troubleshoot-console "#connections-troubleshoot-console")
- [I want a different account as my
  billing account](#connections-troubleshoot-billing "#connections-troubleshoot-billing")
- [My project workflow fails with a connection name error](#connections-troubleshoot-restriction "#connections-troubleshoot-restriction")

## My AWS account connection request

receives an invalid token error

**Problem:** When creating a connection request with a
connection token, the page does not accept the token and shows an error stating that the
token is not valid.

**Possible fixes:** Make sure you provide the account ID
that you want to add to your space. You must have administrative permissions for
your AWS account or be able to work with your administrator to add the account.

When you choose to verify the account, a new browser window will open in the
AWS Management Console. The same account is required to be logged in on the console side. Try again
after verifying the following:

- You are logged in to the AWS Management Console with the same AWS account that you want
  to add to your space.
- You are logged in to the AWS Management Console with the Region set to the correct Region
  for your space.
- If you have arrived from the billing page and you want to add the
  AWS account as a specified billing account for your space, make sure the
  account has not reached the quota as a billing account for another space or
  spaces.

## My Amazon CodeCatalyst project workflow fails

with an error for the configured account, environment, or IAM role

**Problem:** When the workflow runs and does not find a
configured account or IAM roles associated with your space, you must fill in the
role, connection, and environment fields manually in the workflow YAML. View the failed
workflow action, and note whether the error messages are as follows:

- **`The role is not available for use with the connection associated
with the environment.`**
- **`Action did not succeed. Status: FAILED; The provided value for
account connection or environment is not valid. Verify the connection is
associated with your space and the environment is associated with your
project.`**
- **`Action did not succeed. Status: FAILED; The provided value for
IAM role is not valid. Verify the name exists, the IAM role is added to
your account connection, and the connection is already associated with your
Amazon CodeCatalyst space`**

**Possible fixes:** Make sure that the workflow YAML
fields have accurate values for [Environment](build-action-ref.md#build.environment "build-action-ref.md#build.environment"),
[Connections](build-action-ref.md#build.environment.connections "build-action-ref.md#build.environment.connections"), and [Role](build-action-ref.md#build.environment.connections.role "build-action-ref.md#build.environment.connections.role"). The CodeCatalyst workflow
actions that require an environment are build or deploy actions that run AWS resources
or that generate AWS resource stacks.

Choose the failed workflow action block and then choose **Visual**.
Choose the **Configuration** tab. If the
**Environment**,**Connection name**, and
**Role name** fields are not populated, then you will need to
manually update the workflow. Use the following steps to edit your workflow YAML:

- Expand the `/.codecatalyst` directory, and then expand the
  `/workflows` directory. Open the workflow YAML file. Make sure
  that the IAM roles and account information are specified in the YAML that you
  have configured for your workflow. Example:

```
Actions:
  cdk_bootstrap:
    Identifier: action-@v1
    Inputs:
      Sources:
        - WorkflowSource
    Environment:
      Name: Staging
      Connections:
        - Name: account-connection
          Role: build-role
```

The **Environment, Connection, and Role**
properties are required to run CodeCatalyst workflow build and deploy actions with
AWS resources. For an example, see the CodeCatalyst build action reference YAML
parameters for [Environment](build-action-ref.md#build.environment "build-action-ref.md#build.environment"), [Connections](build-action-ref.md#build.environment.connections "build-action-ref.md#build.environment.connections"), and [Role](build-action-ref.md#build.environment.connections.role "build-action-ref.md#build.environment.connections.role").

- Make sure your space has an account added to it, and make sure that the
  account has the appropriate IAM role or roles added to the account. You can
  adjust or add accounts if you have the **Space administrator**
  role. For more information, see [Allowing access to AWS resources with connected
  AWS accounts](ipa-connect-account.md "ipa-connect-account.md").

## I need an associated account,

role, and environment to create a project

**Problem:** In the project creation options, my project
either doesn’t have an added account available in my space, or I need another
account added to my space for my project to use.

**Possible fixes:** For your space, you can add
authorized AWS accounts to add them to your project if you have the
**Space administrator** role. You must also have an AWS account
where you have administrative permissions or can work with your AWS
administrator.

To make sure an account and role will be available in the project creation screen, you
must first add the account and roles. For more information, see [Allowing access to AWS resources with connected
AWS accounts](ipa-connect-account.md "ipa-connect-account.md").

You have the option to choose to create a service role with a role policy called the
**CodeCatalystWorkflowDevelopmentRole-`spaceName`** role policy. The role will have a name `CodeCatalystWorkflowDevelopmentRole-`spaceName`` with a unique identifier
appended. For more information about the role and role policy, see [Understanding the CodeCatalystWorkflowDevelopmentRole-spaceName service role](ipa-iam-roles.md#ipa-iam-roles-service-role "ipa-iam-roles.md#ipa-iam-roles-service-role").
For the steps to create the role, see [Creating the CodeCatalystWorkflowDevelopmentRole-spaceName role for your account
and space](ipa-iam-roles.md#ipa-iam-roles-service-create "ipa-iam-roles.md#ipa-iam-roles-service-create"). The role is added to your account and
available in project creation pages in CodeCatalyst.

## I cannot access the

Amazon CodeCatalyst Spaces page in the AWS Management Console

**Problem:** When I try to access the Amazon CodeCatalyst page in the AWS Management Console
to add an account to my CodeCatalyst space or add roles to an account in AWS, I receive
a permissions error.

**Possible fixes:**

For your space, you can add authorized AWS accounts to add them to your project
if you have the **Space administrator** role. You must also have an
AWS account where you have administrative permissions or can work with your AWS
administrator. You must first make sure you are signed in to the AWS Management Console with the same
account that you want to manage. After you are signed in to the AWS Management Console, you can open
the console and try again.

Open the Amazon CodeCatalyst page in the AWS Management Console at [https://us-west-2.console.aws.amazon.com/codecatalyst/home?region=us-west-2#/](https://us-west-2.console.aws.amazon.com/codecatalyst/home?region=us-west-2#/ "https://us-west-2.console.aws.amazon.com/codecatalyst/home?region=us-west-2#/").

## I want a different account as my

billing account

**Problem:** When I set up my CodeCatalyst login, I completed
several steps to set up my space and associate an authorized AWS account. Now, I
want to authorize a different account for billing.

**Possible fixes:** For your space, you can
authorize billing accounts if you have the **Space administrator** role.
You must also have an AWS account where you have administrative permissions or can
work with your AWS administrator.

For more information, see [Managing
billing](../adminguide/managing-billing.md "../adminguide/managing-billing.md") in the Amazon CodeCatalyst Administrator Guide.

## My project workflow fails with a connection name error

**Problem:** When creating a project and then running the
project workflow, the workflow fails and shows an error stating that the connection name
is not valid, as follows:

**`Failed at <action_name>: The connection name is not
 valid.`**

**Possible fixes:** Make sure you provide the account ID
that you want to add to your space, and make sure that the account is not enabled
for project-restricted account connections. If the account is enabled for
project-restricted account connections, then you might need to update the account
connection by enabling access to the new project. For more information, see [Configuring project-restricted account connections](../adminguide/managing-accounts.md#managing-accounts-restriction "../adminguide/managing-accounts.md#managing-accounts-restriction").
