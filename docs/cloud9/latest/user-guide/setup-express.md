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

* [Prerequisites](#setup-prerequisites "#setup-prerequisites")
* [Other ways to authenticate](#setup-express-sign-in-ide "#setup-express-sign-in-ide")
* [Next steps](#setup-express-next-steps "#setup-express-next-steps")

## Prerequisites


### Sign up for an AWS account


If you do not have an AWS account, complete the following steps to create one.


###### To sign up for an AWS account

1. Open [https://portal.aws.amazon.com/billing/signup](https://portal.aws.amazon.com/billing/signup "https://portal.aws.amazon.com/billing/signup").
2. Follow the online instructions.


Part of the sign-up procedure involves receiving a phone call or text message and entering 
 a verification code on the phone keypad.


When you sign up for an AWS account, an *AWS account root user* is created. The root user has access to all AWS services
 and resources in the account. As a security best practice, assign administrative access to a user, and use only the root user to perform [tasks that require root user access](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_root-user.html#root-user-tasks "https://docs.aws.amazon.com/IAM/latest/UserGuide/id_root-user.html#root-user-tasks").

AWS sends you a confirmation email after the sign-up process is
complete. At any time, you can view your current account activity and manage your account by
going to [https://aws.amazon.com/](https://aws.amazon.com/ "https://aws.amazon.com/") and choosing **My
 Account**.


### Create a user with administrative access


After you sign up for an AWS account, secure your AWS account root user, enable AWS IAM Identity Center, and create an administrative user so that you 
don't use the root user for everyday tasks.


###### Secure your AWS account root user

1. Sign in to the [AWS Management Console](https://console.aws.amazon.com/ "https://console.aws.amazon.com/") as the account owner by choosing **Root user** and entering your AWS account email address. On the next page, enter your password.


For help signing in by using root user, see [Signing in as the root user](https://docs.aws.amazon.com/signin/latest/userguide/console-sign-in-tutorials.html#introduction-to-root-user-sign-in-tutorial "https://docs.aws.amazon.com/signin/latest/userguide/console-sign-in-tutorials.html#introduction-to-root-user-sign-in-tutorial") in the *AWS Sign-In User Guide*.
2. Turn on multi-factor authentication (MFA) for your root user.


For instructions, see [Enable a virtual MFA device for your AWS account root user (console)](https://docs.aws.amazon.com/IAM/latest/UserGuide/enable-virt-mfa-for-root.html "https://docs.aws.amazon.com/IAM/latest/UserGuide/enable-virt-mfa-for-root.html") in the *IAM User Guide*.

###### Create a user with administrative access

1. Enable IAM Identity Center.


For instructions, see [Enabling
 AWS IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/get-set-up-for-idc.html "https://docs.aws.amazon.com/singlesignon/latest/userguide/get-set-up-for-idc.html") in the
 *AWS IAM Identity Center User Guide*.
2. In IAM Identity Center, grant administrative access to a user.


For a tutorial about using the IAM Identity Center directory as your identity source, see [Configure user access with the default IAM Identity Center directory](https://docs.aws.amazon.com/singlesignon/latest/userguide/quick-start-default-idc.html "https://docs.aws.amazon.com/singlesignon/latest/userguide/quick-start-default-idc.html") in the
 *AWS IAM Identity Center User Guide*.

###### Sign in as the user with administrative access

* To sign in with your IAM Identity Center user, use the sign-in URL that was sent to your email address when you created the IAM Identity Center user.


For help signing in using an IAM Identity Center user, see [Signing in to the AWS access portal](https://docs.aws.amazon.com/signin/latest/userguide/iam-id-center-sign-in-tutorial.html "https://docs.aws.amazon.com/signin/latest/userguide/iam-id-center-sign-in-tutorial.html") in the *AWS Sign-In User Guide*.

###### Assign access to additional users

1. In IAM Identity Center, create a permission set that follows the best practice of applying least-privilege permissions.


For instructions, see [Create a permission set](https://docs.aws.amazon.com/singlesignon/latest/userguide/get-started-create-a-permission-set.html "https://docs.aws.amazon.com/singlesignon/latest/userguide/get-started-create-a-permission-set.html") in the *AWS IAM Identity Center User Guide*.
2. Assign users to a group, and then assign single sign-on access to the group.


For instructions, see [Add groups](https://docs.aws.amazon.com/singlesignon/latest/userguide/addgroups.html "https://docs.aws.amazon.com/singlesignon/latest/userguide/addgroups.html") in the *AWS IAM Identity Center User Guide*.

## Other ways to authenticate


###### Warning

To avoid security risks, don't use IAM users for authentication when developing purpose-built software
 or working with real data. Instead, use federation with an identity provider such as
 [AWS IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/what-is.html "https://docs.aws.amazon.com/singlesignon/latest/userguide/what-is.html").


### Manage access across AWS accounts


As a security best practice, we recommend using AWS Organizations with IAM Identity Center to manage access
 across all your AWS accounts. For more information, see 
 [Security best practices in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html "https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html") 
 in the *IAM User Guide*.


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



* Getting started with your AWS SDK or tool and exploring AWS services in a
 sandbox environment.
* Running scheduled scripts, jobs, and other automated processes that don't support
 a human-attended sign-in process as part of your learning.

If you're using IAM users outside of these use cases, then transition to IAM Identity Center or federate
 your identity provider to AWS accounts as soon as possible. For more information, see
 [Identity federation in AWS](https://aws.amazon.com/identity/federation/ "https://aws.amazon.com/identity/federation/").


### Secure IAM user access keys


You should rotate IAM user access keys regularly. Follow the guidance in 
 [Rotating access keys](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html#Using_RotateAccessKey "https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html#Using_RotateAccessKey") in the *IAM User Guide*. If you believe that you
 have accidentally shared your IAM user access keys, then rotate your access keys.


IAM user access keys should be stored in the shared AWS `credentials` file on the local machine. 
 Don't store the IAM user access keys in your code. Don't include configuration files
 that contain your IAM user access keys inside of any source code management software.
 External tools, such as the open source project 
 [git-secrets](https://github.com/awslabs/git-secrets "https://github.com/awslabs/git-secrets"), can help you from
 inadvertently committing sensitive information to a Git repository. For more information, see 
 [IAM Identities (users, user groups, and roles)](https://docs.aws.amazon.com/IAM/latest/UserGuide/id.html "https://docs.aws.amazon.com/IAM/latest/UserGuide/id.html") 
 in the *IAM User Guide*.



## Next steps




| **Task for learning** | **Topic** |
| --- | --- |
| Learn how to use the AWS Cloud9 IDE. | [Getting started: basic tutorials](tutorials-basic.md "tutorials-basic.md") and [Working with the IDE](ide.md "ide.md") |
| **More advanced tasks** | **Topics** |
| --- | --- |
| Create an AWS Cloud9 development environment, and then use the AWS Cloud9 IDE to work with code in your new environment. | [Creating an Environment](create-environment.md "create-environment.md") |
| Invite others to use your new environment along with you in real time and with text chat support. | [Working with Shared Environments](share-environment.md "share-environment.md") |
