# Programmatic access with AWS security

credentials

We recommend using short-term access keys when possible to make programmatic calls to AWS
or to use the AWS Command Line Interface or AWS Tools for PowerShell. However, you can also use long-term AWS access keys
for these purposes.

When you create a long-term access key, you create the access key ID (for example,
`AKIAIOSFODNN7EXAMPLE`) and secret access key (for example,
`wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY`) as a set. The secret access key is available for download
only when you create it. If you don't download your secret access key or if you lose it, you
must create a new one.

In many scenarios, you don't need long-term access keys that never expire (as you have when
you create access keys for an IAM user). Instead, you can create IAM roles and generate
temporary security credentials. Temporary security credentials include an access key ID and a
secret access key, but they also include a security token that indicates when the credentials
expire. After they expire, they're no longer valid. For more information, see [Alternatives to
long-term access keys](#security-creds-alternatives-to-long-term-access-keys "#security-creds-alternatives-to-long-term-access-keys")

Access key IDs beginning with `AKIA` are long-term access keys for an IAM user
or an AWS account root user. Access key IDs beginning with `ASIA` are temporary
credentials access keys that you create using AWS STS operations.

Users need programmatic access if they want to interact with AWS outside of the AWS Management Console. The way to grant programmatic access depends on the type of user that's accessing AWS.

To grant users programmatic access, choose one of the following options.

| Which user needs programmatic access?                        | To                                                                                                                 | By                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| ------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Workforce identity<br>(Users managed in IAM Identity Center) | Use temporary credentials to sign programmatic requests to the AWS CLI, AWS SDKs, or<br>AWS APIs.                  | Following the instructions for the interface that you want to use.<br>• For the AWS CLI, see [Configuring the AWS CLI to use AWS IAM Identity Center](../../../cli/latest/userguide/cli-configure-sso.md "../../../cli/latest/userguide/cli-configure-sso.md") in the<br>_AWS Command Line Interface User Guide_.<br>• For AWS SDKs, tools, and AWS APIs, see [IAM Identity Center<br>authentication](../../../sdkref/latest/guide/access-sso.md "../../../sdkref/latest/guide/access-sso.md") in the _AWS SDKs and Tools Reference Guide_.                                                                                                                                                              |
| IAM                                                          | Use temporary credentials to sign programmatic requests to the AWS CLI, AWS SDKs, or<br>AWS APIs.                  | Following the instructions in [Using temporary<br>credentials with AWS resources](id_credentials_temp_use-resources.md "id_credentials_temp_use-resources.md") in the _IAM User Guide_.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| IAM                                                          | (Not recommended)Use long-term credentials to sign programmatic requests<br>to the AWS CLI, AWS SDKs, or AWS APIs. | Following the instructions for the interface that you want to use.<br>• For the AWS CLI, see [Authenticating using IAM user credentials](../../../cli/latest/userguide/cli-authentication-user.md "../../../cli/latest/userguide/cli-authentication-user.md") in<br>the _AWS Command Line Interface User Guide_.<br>• For AWS SDKs and tools, see [Authenticate using long-term credentials](../../../sdkref/latest/guide/access-iam-users.md "../../../sdkref/latest/guide/access-iam-users.md") in the<br>_AWS SDKs and Tools Reference Guide_.<br>• For AWS APIs, see [Managing access keys for<br>IAM users](id_credentials_access-keys.md "id_credentials_access-keys.md") in the _IAM User Guide_. |

## Alternatives to

long-term access keys

For many common use cases, there are alternatives to long-term access keys. To improve
your account security, consider the following.

- Don't embed long-term access keys and secret access keys in your
  application code or in a code repository – Instead, use AWS Secrets Manager, or
  other secrets management solution, so you don't have to hardcode keys in plaintext. The
  application or client can then retrieve secrets when needed. For more information, see
  [What is AWS Secrets Manager?](../../../secretsmanager/latest/userguide/intro.md "../../../secretsmanager/latest/userguide/intro.md") in the
  _AWS Secrets Manager User Guide_.

- Use IAM roles to generate temporary security credentials
  whenever possible – Always use mechanisms to issue temporary security
  credentials when possible, rather than long-term access keys. Temporary security
  credentials are more secure because they are not stored with the user but are generated
  dynamically and provided to the user when requested. Temporary security credentials have a
  limited lifetime so you don't have to manage or update them. Mechanisms that provide
  temporary access keys include IAM roles or the authentication of an IAM Identity Center user. For
  machines that run outside of AWS you can use [AWS Identity and Access Management Roles Anywhere](../../../rolesanywhere/latest/userguide/introduction.md "../../../rolesanywhere/latest/userguide/introduction.md").
- Use alternatives to long-term access keys for the AWS Command Line Interface
  (AWS CLI) or the `aws-shell` – Alternatives include the
  following.
  - **AWS CloudShell** is a browser-based,
    pre-authenticated shell that you can launch directly from the AWS Management Console. You can run
    AWS CLI commands against AWS services through your preferred shell (Bash, Powershell,
    or Z shell). When you do this, you don't need to download or install command line
    tools. For more information, see [What is
    AWS CloudShell?](../../../cloudshell/latest/userguide/welcome.md "../../../cloudshell/latest/userguide/welcome.md") in the _AWS CloudShell User Guide_.
  - **AWS CLI Version 2 integration with AWS IAM Identity Center
    (IAM Identity Center)**. You can authenticate users and provide short-term credentials to
    run AWS CLI commands. To learn more, see [Integrating AWS CLI with IAM Identity Center](../../../singlesignon/latest/userguide/integrating-aws-cli.md "../../../singlesignon/latest/userguide/integrating-aws-cli.md") in
    the _AWS IAM Identity Center User Guide_ and [Configuring the AWS CLI to use
    IAM Identity Center](../../../cli/latest/userguide/cli-configure-sso.md "../../../cli/latest/userguide/cli-configure-sso.md") in the _AWS Command Line Interface User Guide_.

- Don't create long-term access keys for human users who need
  access to applications or AWS services – IAM Identity Center can generate temporary
  access credentials for your external IdP users to access AWS services. This eliminates
  the need to create and manage long-term credentials in IAM. In IAM Identity Center, create an IAM Identity Center
  permission set that grants the external IdP users access. Then assign a group from IAM Identity Center
  to the permission set in the selected AWS accounts. For more information, see [What is AWS IAM Identity Center](../../../singlesignon/latest/userguide/what-is.md "../../../singlesignon/latest/userguide/what-is.md"), [Connect to your external
  identity provider](../../../singlesignon/latest/userguide/manage-your-identity-source-idp.md "../../../singlesignon/latest/userguide/manage-your-identity-source-idp.md"), and [Permission sets](../../../singlesignon/latest/userguide/permissionsetsconcept.md "../../../singlesignon/latest/userguide/permissionsetsconcept.md") in the _AWS IAM Identity Center User Guide_.
- Don't store long-term access keys within an AWS compute
  service – Instead, assign an IAM role to compute resources. This
  automatically supplies temporary credentials to grant access. For example, when you create
  an instance profile that is attached to an Amazon EC2 instance, you can assign an AWS role to
  the instance and make it available to all of its applications. An instance profile
  contains the role and enables programs that are running on the Amazon EC2 instance to get
  temporary credentials. To learn more, see [Using an IAM role to grant
  permissions to applications running on Amazon EC2 instances](id_roles_use_switch-role-ec2.md "id_roles_use_switch-role-ec2.md").
