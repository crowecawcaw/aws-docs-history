# Multi-factor authentication (MFA)

Multi-factor authentication (MFA) adds an additional layer of protection to your AWS Partner Central account. When enabled, users must enter a verification code sent to their registered email address in addition to their username and password during login. When logging in, users have the option to mark a device as trusted for 30 days. After 30 days, users need to obtain a new one-time password. To sign in with MFA enabled, see [Signing in to AWS Partner Central](signing-in.md "signing-in.md").

###### Note

If your team shares login credentials, we highly recommend your alliance lead or cloud admin to deactivate and reassign any shared logins. If shared credentials are not deactivated when MFA is enabled, users without access to the registered email inbox may potentially be unable to retrieve the one-time password required for login, locking users out of their accounts. More information on this process can be found in [AWS Partner Central permissions best practices](permissions-best-practices.md "permissions-best-practices.md").

###### To manage MFA for your AWS Partner Central accounts

An alliance lead or cloud admin can manage MFA for all users in their organziation. Any changes to MFA settings made by an alliance lead or cloud administrator affect all users within their organization.

1. Sign in to [AWS Partner Central](https://partnercentral.awspartner.com/APNLogin "https://partnercentral.awspartner.com/APNLogin") as a user with the alliance lead or cloud admin role.
2. On the **My Company** menu, choose **User
   Management**.
3. On the **User management** page, choose the **Security** tab.
4. Choose **Edit**.
5. Select a **Multi-factor authentication (MFA) status** option.
   - **Enabled** – To sign in to AWS Partner Central, users must enter a verification code sent to their registered email address in addition to their username and password.
   - **Disabled** – To sign in to AWS Partner Central, users must only enter their username and password.

6. Choose **Save**.

###### Important

If you are locked out of AWS Partner Central and need support, do the following:

1. Navigate to the [AWS Partner Team contact page](https://www.apn-portal.com/knowledgebase/?cu=1&fs=ContactUs&l=en_US "https://www.apn-portal.com/knowledgebase/?cu=1&fs=ContactUs&l=en_US") of the AWS Partner Network Knowledge Base.
2. Complete the contact form and choose **Submit**.
