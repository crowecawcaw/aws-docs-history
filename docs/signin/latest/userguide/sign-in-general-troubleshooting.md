# Help me sign in to AWS

###### Warning

We're currently releasing our new experience to a limited number of customers. You might not be able to access this experience yet.

There are multiple ways to sign in to AWS. Each access point supports certain user types.
Identify where you're trying to sign in, then follow the guidance for that access point.

## Are you trying to access the AWS Management Console?

If you're trying to access the AWS Management Console, you are one of the following user types:

- **[Project owner](user-types-list.md#project-owner-type "user-types-list.md#project-owner-type") or [Project team member](user-types-list.md#project-team-member-type "user-types-list.md#project-team-member-type")** — You
  were invited to or created a project and are using a sign-in method like Google, GitHub,
  Apple, or Amazon. You also have access to AWS Settings. To sign in to a project, see
  [Sign in to a project](sign-in-project.md "sign-in-project.md").
- **[Root user](user-types-list.md#account-root-user-type "user-types-list.md#account-root-user-type")** — The root user has unrestricted
  account access and is associated with the email used to create the AWS account. If you
  need to perform any of the tasks listed in [Tasks that require root user
  credentials](../../../IAM/latest/UserGuide/id_root-user.md "../../../IAM/latest/UserGuide/id_root-user.md"), including certain billing tasks, you are the root user. To sign in
  as the root user, see [Sign in to the AWS Management Console as the root user](introduction-to-root-user-sign-in-tutorial.md "introduction-to-root-user-sign-in-tutorial.md").
- **[IAM user](user-types-list.md#iam-user-type "user-types-list.md#iam-user-type")** — An IAM user is an entity within
  your AWS account that's granted specific custom permissions. To sign in as an IAM user,
  see [Sign in to the AWS Management Console as an IAM user](introduction-to-iam-user-sign-in-tutorial.md "introduction-to-iam-user-sign-in-tutorial.md").
- **[Federated identity](user-types-list.md#federated-identity-type "user-types-list.md#federated-identity-type")** — If you sign in
  through your company's single sign-on portal, you are a federated identity user. Contact
  your administrator for your organization's sign-in URL and credentials.

### Troubleshoot your access to the AWS Management Console

The following is brief troubleshooting information for accessing the AWS Management Console. For more
troubleshooting guidance, see [Troubleshooting AWS account sign-in issues](troubleshooting-sign-in-issues.md "troubleshooting-sign-in-issues.md").

How can I find my AWS account ID or alias?

If you are an IAM user and you aren't signed in, ask your administrator for the
AWS account ID or alias. Your administrator is typically an Information Technology
(IT) personnel who has a higher level of permissions to the AWS account than other
members of your organization. This individual created your account and provides users
with their access credentials to sign in.

How can I find my project name?

You don't need to use your project name to sign in to your account. However, you
can find your project name in AWS Settings, or if you're a project team member, in
the invitation email sent to the email address you use to sign in.

I forgot my root user password for my AWS account

If you are a root user and you have lost or forgotten the password for your
AWS account, you can reset your password by choosing **Forgot
Password** on the AWS Management Console sign-in page. You must know your AWS account's
email address and have access to the email account. You will be emailed a link to reset
your password. The link will be sent to the email address you used to create your
AWS account.

I forgot my IAM user password for my AWS account

To change your IAM user password, you must have the proper permissions. For more
information about resetting your IAM user password, see [How an IAM
user changes their own password](../../../IAM/latest/UserGuide/id_credentials_passwords_user-change-own.md "../../../IAM/latest/UserGuide/id_credentials_passwords_user-change-own.md").

If you do not have the permission to reset your password, only your IAM
administrator can reset it. Contact your IAM administrator to reset your
password.

## Are you trying to access AWS Settings?

If you're trying to access AWS Settings at [https://settings.aws.com](https://settings.aws.com "https://settings.aws.com"), you are either a [Project owner](user-types-list.md#project-owner-type "user-types-list.md#project-owner-type") or a [Project team member](user-types-list.md#project-team-member-type "user-types-list.md#project-team-member-type"). To learn how
to access AWS Settings, see [Sign in to AWS Settings](sign-in-aws-settings.md "sign-in-aws-settings.md").

### Troubleshoot your access to AWS Settings

The following is brief troubleshooting information for accessing AWS Settings. For more
troubleshooting guidance, see [Troubleshooting our new AWS experience issues](troubleshooting-sign-in-new.md "troubleshooting-sign-in-new.md").

AWS is telling me to choose an account to access

If AWS provides a list of accounts to access, you have multiple active sessions
on your browser. This could be an AWS Builder ID session or a session with a project
or AWS account. Choose the account you want to access. To prevent this from happening
in the future, sign out of all active sessions when you are done.

I can't access a project shared with me

Contact the owner of your project. You might have been removed from a project, or
the project owner might have activated advanced features and you can no longer use AWS
Settings to access the project.

## Are you trying to access an AWS access portal?

If you're trying to access a specific sign-in portal with a URL like one of the
following, you're an [IAM Identity Center user](user-types-list.md#sso-user-type "user-types-list.md#sso-user-type").

```
https://d-`xxxxxxxxxx`.awsapps.com/start
```

```
https://`your_subdomain`.awsapps.com/start
```

To learn how to access an AWS access portal, see [How to sign in to the AWS access
portal](../../../singlesignon/latest/userguide/howtosignin.md "../../../singlesignon/latest/userguide/howtosignin.md").

### Troubleshoot your access to an AWS access portal

The following is brief troubleshooting information for accessing an AWS access portal.
For more troubleshooting guidance, see [Troubleshooting AWS account sign-in issues](troubleshooting-sign-in-issues.md "troubleshooting-sign-in-issues.md").

I don't know my access portal URL

Check your email, secure password storage, browser favorites, or browser history
for a URL that includes `awsapps.com/start` or
`signin.aws/platform/login`. If you can't find your portal
link, contact your administrator. Support can't help you recover this
information.

## Are you trying to access your AWS Builder ID profile?

If you're trying to access your AWS Builder ID profile or the sign-in page of an AWS tool or
service, you are an AWS Builder ID user. AWS Builder ID is a personal profile that provides access to
select tools and services including Amazon CodeCatalyst, Amazon Q Developer, and AWS Training
and Certification. You can also use your AWS Builder ID to access your projects as a project owner
or team member. To sign in to your AWS Builder ID profile, see [Sign in with AWS Builder ID](sign-in-builder-id.md "sign-in-builder-id.md").

### Troubleshoot your access to your AWS Builder ID profile

The following is brief troubleshooting information for accessing your AWS Builder ID profile.
For more troubleshooting guidance, see [Troubleshooting AWS Builder ID issues](troubleshooting-builder-id-issues.md "troubleshooting-builder-id-issues.md").

My email is already in use

If the email that you entered is already in use and you recognize it as your own,
you may already have an AWS Builder ID. Try signing in using that email address. If you
don't remember your password, see [I forgot my password](troubleshooting-builder-id-issues.md#forgot-password-aws_builder_id "troubleshooting-builder-id-issues.md#forgot-password-aws_builder_id").

To access the AWS Builder ID recovery page, do the following:

1. Open the [AWS Builder ID
   profile](https://profile.aws.amazon.com/ "https://profile.aws.amazon.com/").
2. Choose **Trouble signing in**.

This will take you to the recovery options page.

## Are you trying to access the AWS CLI?

If you ran `aws login` or `aws configure` in your terminal, you need
to sign in as one of the following: a [Root user](user-types-list.md#account-root-user-type "user-types-list.md#account-root-user-type"), an [IAM user](user-types-list.md#iam-user-type "user-types-list.md#iam-user-type"), an [IAM Identity Center user](user-types-list.md#sso-user-type "user-types-list.md#sso-user-type"), or a [Project owner](user-types-list.md#project-owner-type "user-types-list.md#project-owner-type") or [Project team member](user-types-list.md#project-team-member-type "user-types-list.md#project-team-member-type"). To sign in using the AWS CLI, see [Sign in through the AWS Command Line Interface](command-line-sign-in.md "command-line-sign-in.md").

### Troubleshoot your access to the AWS CLI

The following is brief troubleshooting information for accessing the AWS CLI.

I get "command not found" when I run an aws command

The AWS CLI is not installed or is not in your system's PATH. To install or update
the AWS CLI, see [Installing or updating to the
latest version of the AWS CLI](../../../cli/latest/userguide/getting-started-install.md "../../../cli/latest/userguide/getting-started-install.md"). After installation, close and reopen your
terminal for the changes to take effect.

## I need to contact Support for sign-in issues

If the guidance on this page doesn't resolve your issue, you can get help from Support by
completing the [Billing and Account Support request](https://support.aws.amazon.com/#/contacts/aws-account-support/ "https://support.aws.amazon.com/#/contacts/aws-account-support/").
