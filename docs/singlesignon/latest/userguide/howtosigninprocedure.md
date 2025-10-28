# Confirm users can sign in to the AWS access portal

The following steps are for IAM Identity Center administrator to confirm that the IAM Identity Center user can sign
in to the AWS access portal and access the AWS account.

###### Sign in to the AWS access portal

1. Do either of the following to sign in to the AWS Management Console.
   - **New to AWS (root user)** – Sign in as the
     account owner by choosing **Root user** and entering your
     AWS account email address. On the next page, enter your password.
   - **Already using AWS (IAM credentials)**
     – Sign in with your IAM credentials and select an admin role.

2. Open the [IAM Identity Center
   console](https://console.aws.amazon.com/singlesignon "https://console.aws.amazon.com/singlesignon").
3. In the navigation pane, choose **Dashboard**.
4. On the **Dashboard** page, under **Settings
   summary**, choose the AWS access portal URL.
5. Sign in by using either of the following:
   - If you are using Active Directory or an external identity provider (IdP) as your
     identity source, sign in by using the credentials of the Active Directory or IdP
     user.
   - If you are using the default Identity Center directory as your identity source, sign
     in by using the username that you specified when you created the user and the new
     password that you specified for the user.

6. In the **Accounts** tab, locate your AWS account and expand
   it.
7. The roles available to you are displayed. For example, if you are assigned both the
   **AdministratorAccess** permission set and
   **Billing** permissions sets, those roles are displayed in the
   AWS access portal. Choose the IAM role name you want to use for the session.
8. If you are redirected to the AWS Management Console you successfully finished
   setting up access to the AWS account.

###### Note

If you do not see any **AWS accounts** listed, it is likely that
the user hasn't yet been assigned to a permission set for that account. For
instructions on assigning users to a permission set, see [Assign user or group access to AWS accounts](assignusers.md "assignusers.md").
Now that you've confirmed that you can sign in using IAM Identity Center credentials, switch to the
browser that you used to sign into the AWS Management Console and sign out from your root user or IAM user
credentials.

###### Important

We strongly recommend that you use the credentials of the IAM Identity Center administrative user
when you sign in to the AWS access portal to perform administrative tasks instead of using
IAM user or root user credentials. Safeguard your root user credentials and use them to
perform the tasks that only the root user can perform. To enable other users to access your
accounts and applications, and to administer IAM Identity Center, create and assign permission sets only
through IAM Identity Center.
