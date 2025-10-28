# Setting up

Before you use Amazon File Cache for the first time, complete the tasks
in the [Sign up for Amazon Web Services](#setting-up-aws "#setting-up-aws") section.
To complete the [Getting started tutorial](getting-started.md "getting-started.md"), make
sure the Amazon S3 bucket that you'll link to your cache has the permissions listed
in [Adding permissions to use data repositories in
Amazon S3](#fsx-adding-permissions-s3 "#fsx-adding-permissions-s3").

###### Topics

- [Sign up for Amazon Web Services](#setting-up-aws "#setting-up-aws")
- [Adding permissions to use data repositories in
  Amazon S3](#fsx-adding-permissions-s3 "#fsx-adding-permissions-s3")
- [How Amazon File Cache checks for access
  to linked S3 buckets](#fsx-lustre-permissions-s3-bucket "#fsx-lustre-permissions-s3-bucket")
- [Next step](#setting-up-next-step "#setting-up-next-step")

## Sign up for Amazon Web Services

To set up for AWS, complete the following tasks:

1. [Sign up for an AWS account](#sign-up-for-aws "#sign-up-for-aws")
2. [Create a user with administrative access](#create-an-admin "#create-an-admin")

### Sign up for an AWS account

If you do not have an AWS account, complete the following steps to create one.

###### To sign up for an AWS account

1. Open [https://portal.aws.amazon.com/billing/signup](https://portal.aws.amazon.com/billing/signup "https://portal.aws.amazon.com/billing/signup").
2. Follow the online instructions.

Part of the sign-up procedure involves receiving a phone call or text message and entering
a verification code on the phone keypad.

When you sign up for an AWS account, an _AWS account root user_ is created. The root user has access to all AWS services
and resources in the account. As a security best practice, assign administrative access to a user, and use only the root user to perform [tasks that require root user access](../../../IAM/latest/UserGuide/id_root-user.md#root-user-tasks "../../../IAM/latest/UserGuide/id_root-user.md#root-user-tasks").

AWS sends you a confirmation email after the sign-up process is
complete. At any time, you can view your current account activity and manage your account by
going to [https://aws.amazon.com/](https://aws.amazon.com/ "https://aws.amazon.com/") and choosing **My
Account**.

### Create a user with administrative access

After you sign up for an AWS account, secure your AWS account root user, enable AWS IAM Identity Center, and create an administrative user so that you
don't use the root user for everyday tasks.

###### Secure your AWS account root user

1. Sign in to the [AWS Management Console](https://console.aws.amazon.com/ "https://console.aws.amazon.com/") as the account owner by choosing **Root user** and entering your AWS account email address. On the next page, enter your password.

For help signing in by using root user, see [Signing in as the root user](../../../signin/latest/userguide/console-sign-in-tutorials.md#introduction-to-root-user-sign-in-tutorial "../../../signin/latest/userguide/console-sign-in-tutorials.md#introduction-to-root-user-sign-in-tutorial") in the _AWS Sign-In User Guide_. 2. Turn on multi-factor authentication (MFA) for your root user.

For instructions, see [Enable a virtual MFA device for your AWS account root user (console)](../../../IAM/latest/UserGuide/enable-virt-mfa-for-root.md "../../../IAM/latest/UserGuide/enable-virt-mfa-for-root.md") in the _IAM User Guide_.

###### Create a user with administrative access

1. Enable IAM Identity Center.

For instructions, see [Enabling
AWS IAM Identity Center](../../../singlesignon/latest/userguide/get-set-up-for-idc.md "../../../singlesignon/latest/userguide/get-set-up-for-idc.md") in the
_AWS IAM Identity Center User Guide_. 2. In IAM Identity Center, grant administrative access to a user.

For a tutorial about using the IAM Identity Center directory as your identity source, see [Configure user access with the default IAM Identity Center directory](../../../singlesignon/latest/userguide/quick-start-default-idc.md "../../../singlesignon/latest/userguide/quick-start-default-idc.md") in the
_AWS IAM Identity Center User Guide_.

###### Sign in as the user with administrative access

- To sign in with your IAM Identity Center user, use the sign-in URL that was sent to your email address when you created the IAM Identity Center user.

For help signing in using an IAM Identity Center user, see [Signing in to the AWS access portal](../../../signin/latest/userguide/iam-id-center-sign-in-tutorial.md "../../../signin/latest/userguide/iam-id-center-sign-in-tutorial.md") in the _AWS Sign-In User Guide_.

###### Assign access to additional users

1. In IAM Identity Center, create a permission set that follows the best practice of applying least-privilege permissions.

For instructions, see [Create a permission set](../../../singlesignon/latest/userguide/get-started-create-a-permission-set.md "../../../singlesignon/latest/userguide/get-started-create-a-permission-set.md") in the _AWS IAM Identity Center User Guide_. 2. Assign users to a group, and then assign single sign-on access to the group.

For instructions, see [Add groups](../../../singlesignon/latest/userguide/addgroups.md "../../../singlesignon/latest/userguide/addgroups.md") in the _AWS IAM Identity Center User Guide_.

## Adding permissions to use data repositories in

Amazon S3

Amazon File Cache is deeply integrated with Amazon Simple Storage Service (Amazon S3). This integration means
that applications that access your cache can also seamlessly access the objects stored in your
linked Amazon S3 bucket. For more information, see [Using data repositories with Amazon File Cache](using-data-repositories.md "using-data-repositories.md").

To use data repositories, you must first allow Amazon File Cache certain IAM permissions in a role
associated with the account for your administrator user.

###### To embed an inline policy for a role using the console

1. Sign in to the AWS Management Console and open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. In the navigation pane, choose **Roles**.
3. In the list, choose the name of the role to embed a policy in.
4. Choose the **Permissions** tab.
5. Scroll to the bottom of the page and choose **Add inline
   policy**.

###### Note

You can't embed an inline policy in a service-linked role in IAM. Because the
linked service defines whether you can modify the permissions of the role, you might be
able to add additional policies from the service console, API, or AWS Command Line Interface (AWS CLI). To
view the service-linked role documentation for a service, see
**AWS Services That Work with IAM** and choose
**Yes** in the **Service-Linked
Role** column for your service. 6. Choose **Creating Policies with the Visual Editor**. 7. Add the following permissions policy statement.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": {
 "Effect": "Allow",
 "Action": [
 "iam:CreateServiceLinkedRole",
 "iam:AttachRolePolicy",
 "iam:PutRolePolicy"
 ],
 "Resource": "arn:aws:iam::*:role/aws-service-role/s3.data-source.lustre.fsx.amazonaws.com/*"
 }
}`

```

After you create an inline policy, it's automatically embedded in your role. For more
information about service-linked roles, see [Using service-linked roles for
Amazon FSx](using-service-linked-roles.md "using-service-linked-roles.md").

## How Amazon File Cache checks for access

to linked S3 buckets

If the IAM role that you used to create the Amazon File Cache resource doesn't have the
`iam:AttachRolePolicy` and `iam:PutRolePolicy` permissions,
Amazon File Cache checks whether it can update your S3 bucket policy. Amazon File Cache can update
your bucket policy if the `s3:PutBucketPolicy` permission is included in your IAM
role to allow the Amazon File Cache resource to import or export data to your S3 bucket. If
allowed to modify the bucket policy, Amazon File Cache adds the following permissions to the
bucket policy:

- `s3:AbortMultipartUpload`
- `s3:DeleteObject`
- `s3:PutObject`
- `s3:Get*`
- `s3:List*`
- `s3:PutBucketNotification`
- `s3:PutBucketPolicy`
- `s3:DeleteBucketPolicy`

If Amazon File Cache can't modify the bucket policy, it then checks if the existing bucket policy
grants Amazon File Cache access to the bucket.

If all of these options fail, then the request to create the DRA to the S3 bucket fails.

## Next step

[Getting started with Amazon File Cache](getting-started.md "getting-started.md")
