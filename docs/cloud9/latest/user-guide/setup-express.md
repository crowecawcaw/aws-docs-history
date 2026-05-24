AWS Cloud9 is no longer available to new customers. Existing customers of
AWS Cloud9 can continue to use the service as normal.
[Learn more](https://aws.amazon.com/blogs/devops/how-to-migrate-from-aws-cloud9-to-aws-ide-toolkits-or-aws-cloudshell/ "https://aws.amazon.com/blogs/devops/how-to-migrate-from-aws-cloud9-to-aws-ide-toolkits-or-aws-cloudshell/")

# Individual user setup for AWS Cloud9

This topic describes how to set up and use AWS Cloud9 as the only user in your AWS account
when you're not a student. You can set up AWS Cloud9 for any other usage pattern. For more
information, see [Setting up AWS Cloud9](setting-up.md "setting-up.md").

To use AWS Cloud9 as the only user in your AWS account, sign up for an AWS account if you
don't already have one. Next, sign in to the AWS Cloud9 console.

###### Topics

- [Prerequisites](#setup-prerequisites "#setup-prerequisites")
- [Other ways to authenticate](#setup-express-sign-in-ide "#setup-express-sign-in-ide")
- [Next steps](#setup-express-next-steps "#setup-express-next-steps")

## Prerequisites

### Sign up for an AWS account

To get started with AWS, you need an AWS account. For information about creating an AWS account, see
[Getting started with an AWS account](../../../accounts/latest/reference/getting-started.md "../../../accounts/latest/reference/getting-started.md")
in the _AWS Account Management Reference Guide_.

## Other ways to authenticate

###### Warning

To avoid security risks, don't use IAM users for authentication when developing purpose-built software
or working with real data. Instead, use federation with an identity provider such as
[AWS IAM Identity Center](../../../singlesignon/latest/userguide/what-is.md "../../../singlesignon/latest/userguide/what-is.md").

### Manage access across AWS accounts

As a security best practice, we recommend using AWS Organizations with IAM Identity Center to manage access
across all your AWS accounts. For more information, see
[Security best practices in IAM](../../../IAM/latest/UserGuide/best-practices.md "../../../IAM/latest/UserGuide/best-practices.md")
in the _IAM User Guide_.

You can create users in IAM Identity Center, use Microsoft Active Directory, use a SAML 2.0 identity provider (IdP),
or individually federate your IdP to AWS accounts. Using one of these approaches, you can provide a single
sign-on experience for your users. You can also enforce multi-factor authentication (MFA) and use
temporary credentials for AWS account access. This differs from an IAM user, which is a
long-term credential that can be shared and which might increase the security risk to your
AWS resources.

### Create IAM users for sandbox environments only

If you're new to AWS, you might create a test IAM user and then use it to run tutorials
and explore what AWS has to offer. It's okay to use this type of credential when you're
learning, but we recommend that you avoid using it outside of a sandbox environment.

For the following use cases, it might make sense to get started with IAM users in AWS:

- Getting started with your AWS SDK or tool and exploring AWS services in a
  sandbox environment.
- Running scheduled scripts, jobs, and other automated processes that don't support
  a human-attended sign-in process as part of your learning.

If you're using IAM users outside of these use cases, then transition to IAM Identity Center or federate
your identity provider to AWS accounts as soon as possible. For more information, see
[Identity federation in AWS](https://aws.amazon.com/identity/federation/ "https://aws.amazon.com/identity/federation/").

### Secure IAM user access keys

You should rotate IAM user access keys regularly. Follow the guidance in
[Rotating access keys](../../../IAM/latest/UserGuide/id_credentials_access-keys.md#Using_RotateAccessKey "../../../IAM/latest/UserGuide/id_credentials_access-keys.md#Using_RotateAccessKey") in the _IAM User Guide_. If you believe that you
have accidentally shared your IAM user access keys, then rotate your access keys.

IAM user access keys should be stored in the shared AWS `credentials` file on the local machine.
Don't store the IAM user access keys in your code. Don't include configuration files
that contain your IAM user access keys inside of any source code management software.
External tools, such as the open source project
[git-secrets](https://github.com/awslabs/git-secrets "https://github.com/awslabs/git-secrets"), can help you from
inadvertently committing sensitive information to a Git repository. For more information, see
[IAM Identities (users, user groups, and roles)](../../../IAM/latest/UserGuide/id.md "../../../IAM/latest/UserGuide/id.md")
in the _IAM User Guide_.

## Next steps

| **Task for learning**                | **Topic**                                                                                                                  |
| ------------------------------------ | -------------------------------------------------------------------------------------------------------------------------- |
| Learn how to use the AWS Cloud9 IDE. | [Getting started: basic<br>tutorials](tutorials-basic.md "tutorials-basic.md") and [Working with the IDE](ide.md "ide.md") |

| **More advanced tasks**                                                                                                  | **Topics**                                                                      |
| ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------- |
| Create an AWS Cloud9 development environment, and then use the AWS Cloud9 IDE to work with code in your new environment. | [Creating an Environment](create-environment.md "create-environment.md")        |
| Invite others to use your new environment along with you in real time and with<br>text chat support.                     | [Working with Shared Environments](share-environment.md "share-environment.md") |
