# Granting Programmatic Access

You can run the AWS CLI and code examples in this guide on your local computer or other
AWS enviroments, such as an Amazon Elastic Compute Cloud instance.
To use the features in the Amazon Textract SDK, you'll need to grant your user access. This section
will discuss what permissions a use might need for the
Amazon Textract SDK, and assigning permissions to users.

## Setting up SDK Permissions

We reccomend that you only grant permissions required to perform a task (least-privilege permissions)
For example to call AnalyzeDocumentText, you need permission to perform `textract:AnalyzeDocumentText`.
When starting out with the application you might not know what permissions you need, so you can start with
broader permissions. You can use the `AmazonTextractFullAccess` managed policy to get complete access
to the Amazon Textract API.

## Running Code on your Local Computer

To run code on a local computer, we recommend that you use short-term credentials to
grant a user access to AWS SDK operations. For specific information about running the
AWS CLI and code examples on a local computer, see [Using a profile on your local computer](#local-profiles "#local-profiles").

Users need programmatic access if they want to interact with AWS outside of the AWS Management Console. The way to grant programmatic access depends on the type of user that's accessing AWS.

To grant users programmatic access, choose one of the following options.

| Which user needs programmatic access?                        | To                                                                                                                                  | By                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| ------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| IAM                                                          | (Recommended) Use console credentials as temporary credentials to sign programmatic requests to the AWS CLI, AWS SDKs, or AWS APIs. | Following the instructions for the interface that you want to use.<br>• For the AWS CLI, see [Login for AWS local development](../../../cli/latest/userguide/cli-configure-sign-in.md "../../../cli/latest/userguide/cli-configure-sign-in.md") in<br>the _AWS Command Line Interface User Guide_.<br>• For AWS SDKs, see [Login for AWS local development](../../../sdkref/latest/guide/access-login.md "../../../sdkref/latest/guide/access-login.md") in the<br>_AWS SDKs and Tools Reference Guide_.                                                                                                                                                                                                                                                             |
| Workforce identity<br>(Users managed in IAM Identity Center) | Use temporary credentials to sign programmatic requests to the AWS CLI, AWS SDKs, or<br>AWS APIs.                                   | Following the instructions for the interface that you want to use.<br>• For the AWS CLI, see [Configuring the AWS CLI to use AWS IAM Identity Center](../../../cli/latest/userguide/cli-configure-sso.md "../../../cli/latest/userguide/cli-configure-sso.md") in the<br>_AWS Command Line Interface User Guide_.<br>• For AWS SDKs, tools, and AWS APIs, see [IAM Identity Center<br>authentication](../../../sdkref/latest/guide/access-sso.md "../../../sdkref/latest/guide/access-sso.md") in the _AWS SDKs and Tools Reference Guide_.                                                                                                                                                                                                                          |
| IAM                                                          | Use temporary credentials to sign programmatic requests to the AWS CLI, AWS SDKs, or<br>AWS APIs.                                   | Following the instructions in [Using temporary<br>credentials with AWS resources](../../../IAM/latest/UserGuide/id_credentials_temp_use-resources.md "../../../IAM/latest/UserGuide/id_credentials_temp_use-resources.md") in the _IAM User Guide_.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| IAM                                                          | (Not recommended)Use long-term credentials to sign programmatic requests<br>to the AWS CLI, AWS SDKs, or AWS APIs.                  | Following the instructions for the interface that you want to use.<br>• For the AWS CLI, see [Authenticating using IAM user credentials](../../../cli/latest/userguide/cli-authentication-user.md "../../../cli/latest/userguide/cli-authentication-user.md") in<br>the _AWS Command Line Interface User Guide_.<br>• For AWS SDKs and tools, see [Authenticate using long-term credentials](../../../sdkref/latest/guide/access-iam-users.md "../../../sdkref/latest/guide/access-iam-users.md") in the<br>_AWS SDKs and Tools Reference Guide_.<br>• For AWS APIs, see [Managing access keys for<br>IAM users](../../../IAM/latest/UserGuide/id_credentials_access-keys.md "../../../IAM/latest/UserGuide/id_credentials_access-keys.md") in the _IAM User Guide_. |

### Using a profile on your local computer

You can run the AWS CLI and code examples in this guide with the short-term credentials
you create in Running code on your local computer. To get the credentials and other settings
information, the examples use a profile named `profile-name` For example:

```

                            session = boto3.Session(profile_name="profile-name")
                            client = session.client("textract")

```

The user that the profile represents must have permissions to call the Textract SDK operations
and other AWS SDK operations needed by the examples.

To create a profile that works with the AWS CLI and code examples, choose one of the following.
Make sure the name of the profile you create is `profile-name`.

- Users managed by IAM - Follow the instructions at
  [Switching to an IAM role (AWS CLI)](../../../IAM/latest/UserGuide/id_roles_use_switch-role-cli.md "../../../IAM/latest/UserGuide/id_roles_use_switch-role-cli.md").
- Workforce identity (Users managed by AWS IAM Identity Center (successor to AWS Single Sign-On)) —
  Follow the instructions at [Configuring the AWS CLI to use AWS IAM Identity Center
  (successor to AWS Single Sign-On)](../../../cli/latest/userguide/cli-configure-sso.md "../../../cli/latest/userguide/cli-configure-sso.md"). For the code examples, we recommend using an Integrated Development
  Environment (IDE), which supports the AWS Toolkit enabling authentication through IAM Identity Center.
  For the Java examples, see [Start building with Java](https://aws.amazon.com/developer/language/java/ "https://aws.amazon.com/developer/language/java/").
  For the Python examples, see [Start building with Python](https://aws.amazon.com/developer/tools/#IDE_and_IDE_Toolkits "https://aws.amazon.com/developer/tools/#IDE_and_IDE_Toolkits").
  For more information, see [IAM Identity Center credentials](../../../sdkref/latest/guide/feature-sso-credentials.md "../../../sdkref/latest/guide/feature-sso-credentials.md").

## Running code in AWS enviroments

You shouldn't use user credentials to sign AWS SDK calls in AWS environments, such as production code
running in an AWS Lambda function. Instead, you configure a role that defines the permissions that your
code needs. You then attach the role to the environment that your code runs in. How you attach the role
and make temporary credentials available varies depending on the environment that your code runs in:

- AWS Lambda function — Use the temporary credentials that Lambda automatically provides to
  your function when it assumes the Lambda function's execution role. The credentials are available
  in the Lambda environment variables. You don't need to specify a profile. For more information,
  see [Lambda execution role](../../../lambda/latest/dg/lambda-intro-execution-role.md "../../../lambda/latest/dg/lambda-intro-execution-role.md").
- Amazon EC2 — Use the Amazon EC2 instance metadata endpoint credentials provider. The provider
  automatically generates and refreshes credentials for you using the Amazon EC2 instance profile
  you attach to the Amazon EC2 instance. For more information, see [Using an IAM role to grant
  permissions to applications running on Amazon EC2 instances](../../../IAM/latest/UserGuide/id_roles_use_switch-role-ec2.md "../../../IAM/latest/UserGuide/id_roles_use_switch-role-ec2.md").
- Amazon Elastic Container Service — Use the Container credentials provider. Amazon ECS sends
  and refreshes credentials to a metadata endpoint. A task IAM role that you specify provides a
  strategy for managing the credentials that your application uses. For more information, see
  [Interact with AWS services](../../../AmazonECS/latest/developerguide/task-iam-roles.md "../../../AmazonECS/latest/developerguide/task-iam-roles.md").

For more information about credential providers, see [Standardized credential providers](../../../sdkref/latest/guide/standardized-credentials.md "../../../sdkref/latest/guide/standardized-credentials.md").

## Assigning permissions

To provide access, add permissions to your users, groups, or roles:

- Users and groups in AWS IAM Identity Center:

Create a permission set. Follow the instructions in [Create a permission set](../../../singlesignon/latest/userguide/howtocreatepermissionset.md "../../../singlesignon/latest/userguide/howtocreatepermissionset.md") in the _AWS IAM Identity Center User Guide_.

- Users managed in IAM through an identity provider:

Create a role for identity federation. Follow the instructions in [Create a role for a third-party identity provider (federation)](../../../IAM/latest/UserGuide/id_roles_create_for-idp.md "../../../IAM/latest/UserGuide/id_roles_create_for-idp.md")
in the _IAM User Guide_.

- IAM users:
  - Create a role that your user can assume. Follow the instructions in [Create a role for an IAM user](../../../IAM/latest/UserGuide/id_roles_create_for-user.md "../../../IAM/latest/UserGuide/id_roles_create_for-user.md") in the _IAM User Guide_.
  - (Not recommended) Attach a policy directly to a user or add a user to a user group. Follow the instructions in [Adding permissions to a user (console)](../../../IAM/latest/UserGuide/id_users_change-permissions.md#users_change_permissions-add-console "../../../IAM/latest/UserGuide/id_users_change-permissions.md#users_change_permissions-add-console") in the _IAM User Guide_.
