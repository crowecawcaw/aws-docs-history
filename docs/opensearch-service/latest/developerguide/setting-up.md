# Setting up Amazon OpenSearch Service

## Grant permissions

In production environments, we recommend that you use finer-grained policies. To learn
more about access management, see [Access management for AWS resources](../../../IAM/latest/UserGuide/access.md "../../../IAM/latest/UserGuide/access.md")
in the IAM User Guide.

To provide access, add permissions to your users, groups, or roles:

- Users and groups in AWS IAM Identity Center:

Create a permission set. Follow the instructions in [Create a permission set](../../../singlesignon/latest/userguide/howtocreatepermissionset.md "../../../singlesignon/latest/userguide/howtocreatepermissionset.md") in the _AWS IAM Identity Center User Guide_.

- Users managed in IAM through an identity provider:

Create a role for identity federation. Follow the instructions in [Create a role for a third-party identity provider (federation)](../../../IAM/latest/UserGuide/id_roles_create_for-idp.md "../../../IAM/latest/UserGuide/id_roles_create_for-idp.md")
in the _IAM User Guide_.

- IAM users:
  - Create a role that your user can assume. Follow the instructions in [Create a role for an IAM user](../../../IAM/latest/UserGuide/id_roles_create_for-user.md "../../../IAM/latest/UserGuide/id_roles_create_for-user.md") in the _IAM User Guide_.
  - (Not recommended) Attach a policy directly to a user or add a user to a user group. Follow the instructions in [Adding permissions to a user (console)](../../../IAM/latest/UserGuide/id_users_change-permissions.md#users_change_permissions-add-console "../../../IAM/latest/UserGuide/id_users_change-permissions.md#users_change_permissions-add-console") in the _IAM User Guide_.

### Grant programmatic access

Users need programmatic access if they want to interact with AWS outside of the AWS Management Console. The way to grant programmatic access depends on the type of user that's accessing AWS.

To grant users programmatic access, choose one of the following options.

| Which user needs programmatic access?                        | To                                                                                                                 | By                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| ------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Workforce identity<br>(Users managed in IAM Identity Center) | Use temporary credentials to sign programmatic requests to the AWS CLI, AWS SDKs, or<br>AWS APIs.                  | Following the instructions for the interface that you want to use.<br>• For the AWS CLI, see [Configuring the AWS CLI to use AWS IAM Identity Center](../../../cli/latest/userguide/cli-configure-sso.md "../../../cli/latest/userguide/cli-configure-sso.md") in the<br>_AWS Command Line Interface User Guide_.<br>• For AWS SDKs, tools, and AWS APIs, see [IAM Identity Center<br>authentication](../../../sdkref/latest/guide/access-sso.md "../../../sdkref/latest/guide/access-sso.md") in the _AWS SDKs and Tools Reference Guide_.                                                                                                                                                                                                                          |
| IAM                                                          | Use temporary credentials to sign programmatic requests to the AWS CLI, AWS SDKs, or<br>AWS APIs.                  | Following the instructions in [Using temporary<br>credentials with AWS resources](../../../IAM/latest/UserGuide/id_credentials_temp_use-resources.md "../../../IAM/latest/UserGuide/id_credentials_temp_use-resources.md") in the _IAM User Guide_.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| IAM                                                          | (Not recommended)Use long-term credentials to sign programmatic requests<br>to the AWS CLI, AWS SDKs, or AWS APIs. | Following the instructions for the interface that you want to use.<br>• For the AWS CLI, see [Authenticating using IAM user credentials](../../../cli/latest/userguide/cli-authentication-user.md "../../../cli/latest/userguide/cli-authentication-user.md") in<br>the _AWS Command Line Interface User Guide_.<br>• For AWS SDKs and tools, see [Authenticate using long-term credentials](../../../sdkref/latest/guide/access-iam-users.md "../../../sdkref/latest/guide/access-iam-users.md") in the<br>_AWS SDKs and Tools Reference Guide_.<br>• For AWS APIs, see [Managing access keys for<br>IAM users](../../../IAM/latest/UserGuide/id_credentials_access-keys.md "../../../IAM/latest/UserGuide/id_credentials_access-keys.md") in the _IAM User Guide_. |

## Install and configure the AWS CLI

If you want to use OpenSearch Service APIs, you must install the latest version of the
AWS Command Line Interface (AWS CLI). You don't need the AWS CLI to use OpenSearch Service from the console, and
you can get started without the CLI by following the steps in [Getting started with Amazon OpenSearch Service](gsg.md "gsg.md").

###### To set up the AWS CLI

1. To install the latest version of the AWS CLI for macOS, Linux, or Windows, see
   [Installing or
   updating the latest version of the AWS CLI](../../../cli/latest/userguide/getting-started-install.md "../../../cli/latest/userguide/getting-started-install.md").
2. To configure the AWS CLI and secure setup of your access to AWS services,
   including OpenSearch Service, see [Quick configuration with `aws configure`](../../../cli/latest/userguide/cli-configure-quickstart.md#cli-configure-quickstart-config "../../../cli/latest/userguide/cli-configure-quickstart.md#cli-configure-quickstart-config").
3. To verify the setup, enter the following DataBrew command at the command
   prompt.

```
aws opensearch help
```

AWS CLI commands use the default AWS Region from your configuration, unless
you set it with a parameter or a profile. To set your AWS Region with a
parameter, you can add the `--region` parameter to each
command.

To set your AWS Region with a profile, first add a named profile in the
`~/.aws/config` file or the
`%UserProfile%/.aws/config` file (for Microsoft Windows). Follow
the steps in [Named profiles for
the AWS CLI](../../../cli/latest/userguide/cli-configure-profiles.md "../../../cli/latest/userguide/cli-configure-profiles.md"). Next, set your AWS Region and other settings with a
command similar to the one in the following example.

```
[profile opensearch]
aws_access_key_id = ACCESS-KEY-ID-OF-IAM-USER
aws_secret_access_key = SECRET-ACCESS-KEY-ID-OF-IAM-USER
region = us-east-1
output = text
```

## Open the console

Most of the console-oriented topics in this section start from the [OpenSearch Service console](https://console.aws.amazon.com/aos/home "https://console.aws.amazon.com/aos/home"). If you aren't already signed in
to your AWS account, sign in, then open the [OpenSearch Service
console](https://console.aws.amazon.com/aos/home "https://console.aws.amazon.com/aos/home") and continue to the next section to continue getting started with
OpenSearch Service.
