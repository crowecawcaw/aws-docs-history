# Create IAM administrative groups for AWS CloudHSM

The first step to getting started with AWS CloudHSM is to set up IAM permissions.

As a [best
 practice](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#create-iam-users "https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#create-iam-users"), don't use your AWS account root user to interact with AWS, including AWS CloudHSM.
 Instead, use AWS Identity and Access Management (IAM) to create an IAM user, IAM role, or federated user.
 Follow the steps in the section [Create an IAM user and administrator group](#create-iam-admin "#create-iam-admin")
 to create an administrator group and attach the
 **AdministratorAccess** policy to it. Then create a new administrator
 user and add the user to the group. Add additional users to the group as needed. Each user
 you add inherits the **AdministratorAccess** policy from the group. 

Another best practice is to create an AWS CloudHSM administrator group that has only the
 permissions required to run AWS CloudHSM. Add individual users to this group as needed. Each user
 inherits the limited permissions that are attached to the group rather than full AWS
 access. The [Customer managed policies for AWS CloudHSM](identity-access-management.md#permissions-for-cloudhsm "identity-access-management.md#permissions-for-cloudhsm") section that follows contains the policy that
 you should attach to your AWS CloudHSM administrator group. 

AWS CloudHSM defines a [service–linked role](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_terms-and-concepts.html#iam-term-service-linked-role "https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_terms-and-concepts.html#iam-term-service-linked-role") for your AWS account. The service–linked role
 currently defines permissions that allow your account to log AWS CloudHSM events. The role can be
 created automatically by AWS CloudHSM or manually by you. You cannot edit the role, but you can
 delete it. For more information, see [Service-linked roles for AWS CloudHSM](service-linked-roles.md "service-linked-roles.md").


## Create an IAM user and administrator group


Start by creating an IAM user along with an administrator group for that
 user.


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

For example policies for AWS CloudHSM that you can attach to your IAM user group, see [Identity and access management for AWS CloudHSM](identity-access-management.md "identity-access-management.md").
