# Email one-time password to users created with API or
 CLI

When you create users with the [CreateUser](../IdentityStoreAPIReference/API_CreateUser.md "../IdentityStoreAPIReference/API_CreateUser.md") API operation or the `create-user`
 CLI command, the users do not have passwords. You can update the settings in IAM Identity Center to send these users a verification email after their first attempt to sign in, if you’ve specified an
 email for the user when they were created. After receiving the verification email, the
 user must set a password to sign in.

 If you don’t enable this setting, you must [generate a one-time password](reset-password-for-user.md "reset-password-for-user.md") and
 share it with users that you create using the CreateUser API
 or `create-user` CLI command.

###### To send an email address verification email to users created with the 
 CreateUser API or `create-user` CLI command

1. Open the [IAM Identity Center
 console](https://console.aws.amazon.com/singlesignon "https://console.aws.amazon.com/singlesignon").
2. Choose **Settings**.
3. On the **Settings** page, choose the **Authentication**
 tab.
4. In the **Standard authentication** section, choose **Configure**.
5. In the **Configure standard authentication** dialog box,
 select the **Send email
 OTP** check box. Then, choose **Save**. The status
 updates from **Disabled** to **Enabled**.
