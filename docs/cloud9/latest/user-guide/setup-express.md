

 AWS Cloud9 is no longer available to new customers. Existing customers of AWS Cloud9 can continue to use the service as normal. [Learn more](https://aws.amazon.com/blogs/devops/how-to-migrate-from-aws-cloud9-to-aws-ide-toolkits-or-aws-cloudshell/)

# Individual user setup for AWS Cloud9
<a name="setup-express"></a>

This topic describes how to set up and use AWS Cloud9 as the only user in your AWS account when you're not a student. You can set up AWS Cloud9 for any other usage pattern. For more information, see [Setting up AWS Cloud9](setting-up.md).

To use AWS Cloud9 as the only user in your AWS account, sign up for an AWS account if you don't already have one. Next, sign in to the AWS Cloud9 console.

**Topics**
+ [Prerequisites](#setup-prerequisites)
+ [Other ways to authenticate](#setup-express-sign-in-ide)
+ [Next steps](#setup-express-next-steps)

## Prerequisites
<a name="setup-prerequisites"></a>

### Sign up for an AWS account
<a name="sign-up-for-aws"></a>

To get started with AWS, you need an AWS account. For information about creating an AWS account, see [Getting started with an AWS account](https://docs.aws.amazon.com/accounts/latest/reference/getting-started.html) in the *AWS Account Management Reference Guide*.

## Other ways to authenticate
<a name="setup-express-sign-in-ide"></a>

**Warning**  
To avoid security risks, don't use IAM users for authentication when developing purpose-built software or working with real data. Instead, use federation with an identity provider such as [AWS IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/what-is.html).

### Manage access across AWS accounts
<a name="manage-access-accounts"></a>

As a security best practice, we recommend using AWS Organizations with IAM Identity Center to manage access across all your AWS accounts. For more information, see [Security best practices in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html) in the *IAM User Guide*.

You can create users in IAM Identity Center, use Microsoft Active Directory, use a SAML 2.0 identity provider (IdP), or individually federate your IdP to AWS accounts. Using one of these approaches, you can provide a single sign-on experience for your users. You can also enforce multi-factor authentication (MFA) and use temporary credentials for AWS account access. This differs from an IAM user, which is a long-term credential that can be shared and which might increase the security risk to your AWS resources.

### Create IAM users for sandbox environments only
<a name="create-iam-user-sandbox"></a>

If you're new to AWS, you might create a test IAM user and then use it to run tutorials and explore what AWS has to offer. It's okay to use this type of credential when you're learning, but we recommend that you avoid using it outside of a sandbox environment.

For the following use cases, it might make sense to get started with IAM users in AWS:
+ Getting started with your AWS SDK or tool and exploring AWS services in a sandbox environment.
+ Running scheduled scripts, jobs, and other automated processes that don't support a human-attended sign-in process as part of your learning.

If you're using IAM users outside of these use cases, then transition to IAM Identity Center or federate your identity provider to AWS accounts as soon as possible. For more information, see [Identity federation in AWS](https://aws.amazon.com/identity/federation/).

### Secure IAM user access keys
<a name="secure-iam-access-keys"></a>

You should rotate IAM user access keys regularly. Follow the guidance in [ Rotating access keys](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html#Using_RotateAccessKey) in the *IAM User Guide*. If you believe that you have accidentally shared your IAM user access keys, then rotate your access keys.

IAM user access keys should be stored in the shared AWS `credentials` file on the local machine. Don't store the IAM user access keys in your code. Don't include configuration files that contain your IAM user access keys inside of any source code management software. External tools, such as the open source project [git-secrets](https://github.com/awslabs/git-secrets), can help you from inadvertently committing sensitive information to a Git repository. For more information, see [IAM Identities (users, user groups, and roles)](https://docs.aws.amazon.com/IAM/latest/UserGuide/id.html) in the *IAM User Guide*.



## Next steps
<a name="setup-express-next-steps"></a>



|  **Task for learning**  |  **Topic**  | 
| --- | --- | 
| Learn how to use the AWS Cloud9 IDE. |  [Getting started: basic tutorials](tutorials-basic.md) and [Working with the IDE](ide.md)  | 



|  **More advanced tasks**  |  **Topics**  | 
| --- | --- | 
| Create an AWS Cloud9 development environment, and then use the AWS Cloud9 IDE to work with code in your new environment. |  [Creating an Environment](create-environment.md)  | 
| Invite others to use your new environment along with you in real time and with text chat support. |  [Working with Shared Environments](share-environment.md)  | 