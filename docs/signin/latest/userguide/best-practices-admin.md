# Security best practices for AWS account

administrators

If you’re an account administrator who has created a new AWS account, we recommend the
following steps to help your users follow AWS security best practices when they sign in.

1. Sign in as the root user to [Enable
   multi-factor authentication (MFA)](../../../IAM/latest/UserGuide/id_root-user.md#id_root-user_manage_mfa "../../../IAM/latest/UserGuide/id_root-user.md#id_root-user_manage_mfa") and [create an AWS administrative
   user](../../../singlesignon/latest/userguide/getting-started.md "../../../singlesignon/latest/userguide/getting-started.md") in IAM Identity Center if you haven't already done so. Then, [safeguard your
   root credentials](../../../IAM/latest/UserGuide/best-practices.md#lock-away-credentials "../../../IAM/latest/UserGuide/best-practices.md#lock-away-credentials") and don't use them for everyday tasks.
2. Sign in as the AWS account administrator and set up the following identities:
   - Create [least-privilege](../../../IAM/latest/UserGuide/best-practices.md#grant-least-privilege "../../../IAM/latest/UserGuide/best-practices.md#grant-least-privilege") users for other [humans](../../../IAM/latest/UserGuide/best-practices.md#bp-users-federation-idp "../../../IAM/latest/UserGuide/best-practices.md#bp-users-federation-idp").
   - Set up [temporary
     credentials for workloads](../../../IAM/latest/UserGuide/best-practices.md#bp-workloads-use-roles "../../../IAM/latest/UserGuide/best-practices.md#bp-workloads-use-roles").
   - Create access keys only for [use cases that
     require long-term credentials](../../../IAM/latest/UserGuide/best-practices.md#rotate-credentials "../../../IAM/latest/UserGuide/best-practices.md#rotate-credentials").

3. Add permissions to grant access to those identities. You can [get started
   with AWS managed policies](../../../IAM/latest/UserGuide/best-practices.md#bp-use-aws-defined-policies "../../../IAM/latest/UserGuide/best-practices.md#bp-use-aws-defined-policies") and move towards [least-privilege
   permissions](../../../IAM/latest/UserGuide/best-practices.md#grant-least-privilege "../../../IAM/latest/UserGuide/best-practices.md#grant-least-privilege").
   - [Add permission
     sets to AWS IAM Identity Center (successor to AWS Single Sign-On) users](../../../singlesignon/latest/userguide/howtocreatepermissionset.md "../../../singlesignon/latest/userguide/howtocreatepermissionset.md").
   - [Add identity-based policies to IAM roles](../../../IAM/latest/UserGuide/access_policies_manage-attach-detach.md#add-policies-console "../../../IAM/latest/UserGuide/access_policies_manage-attach-detach.md#add-policies-console") used for workloads.
   - [Add identity-based polices for IAM users](../../../IAM/latest/UserGuide/access_policies_manage-attach-detach.md#add-policies-console "../../../IAM/latest/UserGuide/access_policies_manage-attach-detach.md#add-policies-console") for use cases that require
     long-term credentials.
   - For more information about IAM users, see [Security best practices in
     IAM](../../../IAM/latest/UserGuide/best-practices.md "../../../IAM/latest/UserGuide/best-practices.md").

4. Save and share information about [Sign in to the AWS Management Console](how-to-sign-in.md "how-to-sign-in.md"). This information varies, depending on the type of
   identity you created.
5. Keep your root user email address and primary account contact phone number up to date to
   ensure that you can receive important account and security-related notifications.
   - [Modify the account
     name email address, or password for the AWS account root user](../../../accounts/latest/reference/manage-acct-update-root-user.md "../../../accounts/latest/reference/manage-acct-update-root-user.md").
   - [Access or
     update the primary account contact](../../../accounts/latest/reference/manage-acct-update-contact-primary.md "../../../accounts/latest/reference/manage-acct-update-contact-primary.md").

6. Review [Security best practices in IAM](../../../IAM/latest/UserGuide/best-practices.md "../../../IAM/latest/UserGuide/best-practices.md") to learn about additional identity and access
   management best practices.
