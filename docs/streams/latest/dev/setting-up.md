# Set up an AWS account and create an administrator

user

Before you use Amazon Managed Service for Apache Flink for the first time, complete the following tasks:

1. [Sign up for AWS](#setting-up-signup "#setting-up-signup")
2. [Create an IAM user](#setting-up-iam "#setting-up-iam")

## Sign up for AWS

When you sign up for Amazon Web Services (AWS), your AWS account is automatically signed up
for all services in AWS, including Amazon Managed Service for Apache Flink. You are charged only for the services
that you use.

With Managed Service for Apache Flink, you pay only for the resources that you use. If you are a new AWS
customer, you can get started with Managed Service for Apache Flink for free. For more information, see [AWS Free Tier](https://aws.amazon.com/free/ "https://aws.amazon.com/free/").

If you already have an AWS account, skip to the next task. If you don't have an
AWS account, follow these steps to create one.

###### To create an AWS account

1. Open [https://portal.aws.amazon.com/billing/signup](https://portal.aws.amazon.com/billing/signup "https://portal.aws.amazon.com/billing/signup").
2. Follow the online instructions.

Part of the sign-up procedure involves receiving a phone call or text message and entering
a verification code on the phone keypad.

When you sign up for an AWS account, an _AWS account root user_ is created. The root user has access to all AWS services
and resources in the account. As a security best practice, assign administrative access to a user, and use only the root user to perform [tasks that require root user access](../../../IAM/latest/UserGuide/id_root-user.md#root-user-tasks "../../../IAM/latest/UserGuide/id_root-user.md#root-user-tasks").

Note your AWS account ID because you'll need it for the next task.

## Create an IAM user

Services in AWS, such as Amazon Managed Service for Apache Flink, require that you provide credentials when you
access them. This is so that the service can determine whether you have permissions
to access the resources that are owned by that service. The AWS Management Console requires that
you enter your password.

You can create access keys for your AWS account to access the AWS Command Line Interface (AWS CLI) or
API. However, we don't recommend that you access AWS using the credentials for your
AWS account. Instead, we recommend that you use AWS Identity and Access Management (IAM). Create an IAM
user, add the user to an IAM group with administrative permissions, and then grant
administrative permissions to the IAM user that you created. You can then access
AWS using a special URL and that IAM user's credentials.

If you signed up for AWS, but you haven't created an IAM user for yourself, you
can create one using the IAM console.

The getting started exercises in this guide assume that you have a user
(`adminuser`) with administrator permissions. Follow the procedure to
create `adminuser` in your account.

###### To create a group for administrators

1. Sign in to the AWS Management Console and open the IAM console at
   [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. In the navigation pane, choose **Groups**, and then
   choose **Create New Group**.
3. For **Group Name**, enter a name for your group, such as
   `Administrators`, and then choose **Next
   Step**.
4. In the list of policies, select the check box next to the
   **AdministratorAccess** policy. You can use the
   **Filter** menu and the **Search** box
   to filter the list of policies.
5. Choose **Next Step**, and then choose **Create
   Group**.

Your new group is listed under **Group Name**.

###### To create an IAM user for yourself, add it to the Administrators group, and

create a password

1. In the navigation pane, choose **Users**, and then choose
   **Add user**.
2. In the **User name** box, enter a user name.
3. Choose both **Programmatic access** and **AWS
   Management Console access**.
4. Choose **Next: Permissions**.
5. Select the check box next to the **Administrators**
   group. Then choose **Next: Review**.
6. Choose **Create user**.

###### To sign in as the new IAM user

1. Sign out of the AWS Management Console.
2. Use the following URL format to sign in to the console:

`https://`aws_account_number`.signin.aws.amazon.com/console/`

The `aws_account_number` is your AWS account ID
without any hyphens. For example, if your AWS account ID is 1234-5678-9012,
replace `aws_account_number` with
`123456789012`. For information about how to find
your account number, see [Your AWS Account ID and
Its Alias](../../../IAM/latest/UserGuide/console_account-alias.md "../../../IAM/latest/UserGuide/console_account-alias.md") in the _IAM User Guide_. 3. Enter the IAM user name and password that you just created. When you're
signed in, the navigation bar displays
`your_user_name` @
`your_aws_account_id`.

###### Note

If you don't want the URL for your sign-in page to contain your AWS account
ID, you can create an account alias.

###### To create or remove an account alias

1. Open the IAM console at
   [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. On the navigation pane, choose **Dashboard**.
3. Find the IAM users sign-in link.
4. To create the alias, choose **Customize**. Enter the name
   you want to use for your alias, and then choose **Yes,
   Create**.
5. To remove the alias, choose **Customize**, and then
   choose **Yes, Delete**. The sign-in URL reverts to using
   your AWS account ID.

To sign in after you create an account alias, use the following URL:

`https://`your_account_alias`.signin.aws.amazon.com/console/`

To verify the sign-in link for IAM users for your account, open the IAM
console and check under **IAM users sign-in link** on the
dashboard.

For more information about IAM, see the following:

- [AWS Identity and Access Management (IAM)](https://aws.amazon.com/iam/ "https://aws.amazon.com/iam/")
- [Getting started with IAM](../../../IAM/latest/UserGuide/getting-started.md "../../../IAM/latest/UserGuide/getting-started.md")
- [IAM User Guide](../../../IAM/latest/UserGuide.md "../../../IAM/latest/UserGuide.md")

## Next step

[Set up the AWS Command Line Interface (AWS CLI)](setup-awscli.md "setup-awscli.md")
