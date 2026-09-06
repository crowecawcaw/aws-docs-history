

AWS Migration Hub is no longer open to new customers as of November 7, 2025. For capabilities similar to AWS Migration Hub, explore [AWS Transform](https://aws.amazon.com/transform).

# Setting up AWS Migration Hub
<a name="setting-up"></a>

Before you use AWS Migration Hub for the first time, if you have not done so, complete the following tasks:

**Topics**
+ [Sign up for AWS](setting-up-signup.md)
+ [Create an IAM user](#setting-up-iam)

## Create an IAM user
<a name="setting-up-iam"></a>

Services in AWS, such as AWS Migration Hub, require that you provide credentials when you access them, so that the service can determine whether you have permissions to access its resources. AWS recommends that you do not use the root credentials of your AWS account to make requests. Instead, create an IAM user, and grant that user full access. We refer to these users as administrator users. You can use the administrator user credentials, instead of root credentials of your account, to interact with AWS and perform tasks, such as create a bucket, create users, and grant them permissions. For more information, see [Root Account Credentials vs. IAM User Credentials](https://docs.aws.amazon.com/general/latest/gr/root-vs-iam.html) in the *AWS General Reference* and [IAM Best Practices](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html) in the *IAM User Guide*. 

If you signed up for AWS but have not created an IAM user for yourself, you can create one using the IAM console.

To create an administrator user, choose one of the following options.



| Choose one way to manage your administrator | To | By | You can also | 
| --- | --- | --- | --- | 
| In IAM Identity Center (Recommended) | Use short-term credentials to access AWS.This aligns with the security best practices. For information about best practices, see [Security best practices in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#bp-users-federation-idp) in the *IAM User Guide*. | Following the instructions in [Getting started](https://docs.aws.amazon.com/singlesignon/latest/userguide/getting-started.html) in the AWS IAM Identity Center User Guide. | Configure programmatic access by [Configuring the AWS CLI to use AWS IAM Identity Center](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-sso.html) in the AWS Command Line Interface User Guide. | 
| In IAM (Not recommended) | Use long-term credentials to access AWS. | Following the instructions in [ Create an IAM user for emergency access](https://docs.aws.amazon.com/IAM/latest/UserGuide/getting-started-emergency-iam-user.html) in the IAM User Guide. | Configure programmatic access by [Manage access keys for IAM users](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html) in the IAM User Guide. | 

To sign in as this new IAM user, sign out of the AWS Management Console, and then use the following URL, where *your\_aws\_account\_id* is your AWS account number without the hyphens (for example, if your AWS account number is `1234-5678-9012`, your AWS account ID is `123456789012`):

```
https://{{your_aws_account_id}}.signin.aws.amazon.com/console/
```

Enter the IAM user name and password that you just created. When you're signed in, the navigation bar displays ***your\_user\_name*****@*****your\_aws\_account\_id***.

If you don't want the URL for your sign-in page to contain your AWS account ID, you can create an account alias. From the IAM dashboard, click **Create Account Alias** and enter an alias, such as your company name. To sign in after you create an account alias, use the following URL:

```
https://{{your_account_alias}}.signin.aws.amazon.com/console/
```

To verify the sign-in link for IAM users for your account, open the IAM console and check under **AWS Account Alias** on the dashboard.