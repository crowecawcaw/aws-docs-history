AWS Migration Hub is no longer open to new customers as of November 7, 2025. For capabilities similar to AWS Migration Hub, explore [AWS Transform](https://aws.amazon.com/transform "https://aws.amazon.com/transform").

# Setting up AWS Migration Hub

Before you use AWS Migration Hub for the first time, if you have not done so, complete the
following tasks:

###### Topics

- [Sign up for AWS](setting-up-signup.md "setting-up-signup.md")
- [Create an IAM user](#setting-up-iam "#setting-up-iam")

## Create an IAM user

Services in AWS, such as AWS Migration Hub, require that you provide credentials when you access
them, so that the service can determine whether you have permissions to access its resources.
AWS recommends that you do not use the root credentials of your AWS account to make requests.
Instead, create an IAM user, and grant that user full access. We refer to these users as
administrator users. You can use the administrator user credentials, instead of root
credentials of your account, to interact with AWS and perform tasks, such as create a bucket,
create users, and grant them permissions. For more information, see [Root Account Credentials vs. IAM User
Credentials](../../../general/latest/gr/root-vs-iam.md "../../../general/latest/gr/root-vs-iam.md") in the _AWS General Reference_ and
[IAM Best Practices](../../../IAM/latest/UserGuide/best-practices.md "../../../IAM/latest/UserGuide/best-practices.md") in the
_IAM User Guide_.

If you signed up for AWS but have not created an IAM user for yourself, you can create
one using the IAM console.

To create an administrator user, choose one of the following options.

| Choose one way to manage your administrator | To                                                                                                                                                                                                                                                                                                                                                  | By                                                                                                                                                                                                                                          | You can also                                                                                                                                                                                                                                          |
| ------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| In IAM Identity Center (Recommended)        | Use short-term credentials to access AWS.This aligns with the security best<br>practices. For information about best practices, see [Security best<br>practices in IAM](../../../IAM/latest/UserGuide/best-practices.md#bp-users-federation-idp "../../../IAM/latest/UserGuide/best-practices.md#bp-users-federation-idp") in the _IAM User Guide_. | Following the instructions in [Getting started](../../../singlesignon/latest/userguide/getting-started.md "../../../singlesignon/latest/userguide/getting-started.md") in the<br>_AWS IAM Identity Center User Guide_.                      | Configure programmatic access by [Configuring the AWS CLI to use<br>AWS IAM Identity Center](../../../cli/latest/userguide/cli-configure-sso.md "../../../cli/latest/userguide/cli-configure-sso.md") in the _AWS Command Line Interface User Guide_. |
| In IAM (Not recommended)                    | Use long-term credentials to access AWS.                                                                                                                                                                                                                                                                                                            | Following the instructions in [Create an IAM user for emergency access](../../../IAM/latest/UserGuide/getting-started-emergency-iam-user.md "../../../IAM/latest/UserGuide/getting-started-emergency-iam-user.md") in the _IAM User Guide_. | Configure programmatic access by [Manage access keys for IAM<br>users](../../../IAM/latest/UserGuide/id_credentials_access-keys.md "../../../IAM/latest/UserGuide/id_credentials_access-keys.md") in the _IAM User Guide_.                            |

To sign in as this
new IAM user, sign out of the AWS Management Console, and then use the following URL, where
_your_aws_account_id_ is your AWS account number without the hyphens (for
example, if your AWS account number is `1234-5678-9012`, your AWS account ID is
`123456789012`):

```
https://`your_aws_account_id`.signin.aws.amazon.com/console/
```

Enter the IAM user name and password that you just created. When you're signed in, the
navigation bar displays
**\*your_user_name\*\*\***@**\***your_aws_account_id\*\*\*.

If you don't want the URL for your sign-in page to contain your AWS account ID, you can
create an account alias. From the IAM dashboard, click **Create Account
Alias** and enter an alias, such as your company name. To sign in after you create
an account alias, use the following URL:

```
https://`your_account_alias`.signin.aws.amazon.com/console/
```

To verify the sign-in link for IAM users for your account, open the IAM console and
check under **AWS Account Alias** on the dashboard.
