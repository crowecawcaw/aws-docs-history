

# Troubleshooting AWS account sign-in issues
<a name="troubleshooting-sign-in-issues"></a>

This troubleshooting information is for issues related to AWS account sign-in (advanced). If you use our new AWS experience and have access to AWS Settings and projects, use [Troubleshooting our new AWS experience issues](troubleshooting-sign-in-new.md) to troubleshoot.

Use the information here to help you troubleshoot sign-in and other AWS account issues. For step-by-step directions on signing in to an AWS account, see [Sign in to the AWS Management Console](how-to-sign-in.md). 

If none of the troubleshooting topics help you address your sign-in issue, you can create a case with Support by filling out this form: [I'm an AWS customer and I'm looking for billing or account support](https://support.aws.amazon.com/#/contacts/aws-account-support/). As a security best practice, Support can't discuss the details of any AWS account other than the account that you're signed in to. AWS Support also can't change the credentials associated with an account for any reason.

**Note**  
Support does not publish a direct phone number for reaching a support representative.

For more assistance on troubleshooting your sign-in issues, see [What do I do if I'm having trouble signing in to or accessing my AWS account?](https://aws.amazon.com/premiumsupport/knowledge-center/sign-in-account/) If you are having trouble signing in to Amazon.com, see [Amazon Customer Service](https://www.amazon.com/gp/help/customer/contact-us/) instead of this page.

**Topics**
+ [My AWS Management Console credentials aren't working](#credentials-not-working-console)
+ [Password reset is required for my root user](#password-reset-required)
+ [I don't have access to the email for my AWS account](#troubleshoot-lost-email)
+ [My MFA device is lost or stopped working](#troubleshoot-MFA-issues)
+ [I can’t access the AWS Management Console sign-in page](#troubleshoot-firewalls)
+ [I cannot sign in due to network conditions in Sign-in resource-based policies](#troubleshoot-rbp-network)
+ [I am locked out of my account after enabling console authorization](#troubleshoot-rbp-lockout)
+ [My policy changes are not taking effect](#troubleshoot-rbp-replication)
+ [How can I find my AWS account ID or alias](#troubleshoot-find-aws-account-id-or-alias)
+ [I need my account verification code](#troubleshoot_general_cant-sign-in)
+ [I forgot my root user password for my AWS account](#troubleshoot-forgot-root-password)
+ [I forgot my IAM user password for my AWS account](#troubleshoot-forgot-iam-password)
+ [I forgot my federated identity password for my AWS account](#troubleshoot-forgot-federated-identity-password)
+ [I can’t sign in to my existing AWS account and I can't create a new AWS account with the same email address](#troubleshoot-cannot-create-new-acc)
+ [I need to reactivate my suspended AWS account](#troubleshoot-suspended-aws-account)
+ [I need to contact Support for sign-in issues](#troubleshoot-contact-support)
+ [I need to contact AWS Billing for billing issues](#troubleshoot-contact-billing)
+ [I have a question about a retail order](#troubleshoot-retail-issue)
+ [I need help managing my AWS account](#troubleshoot-other-issues)
+ [My AWS access portal credentials aren't working](#credentials-not-working-portal)
+ [I forgot my IAM Identity Center password for my AWS account](#troubleshoot-forgot-iam-identity-center-password)
+ [I receive an error that states ‘It’s not you, it’s us’ when I try to sign in to the IAM Identity Center console](#error-sign-in-idc)

## My AWS Management Console credentials aren't working
<a name="credentials-not-working-console"></a>

If you remember your username and password, but your credentials don't work, you might be on the wrong page. Try signing in on a different page:

**Root user sign-in page**
+ If you created or own an AWS account and are performing a task that requires root user credentials, enter your account email address in the [AWS Management Console](https://console.aws.amazon.com/). To learn how to access the root user, see [To sign in as the root user](introduction-to-root-user-sign-in-tutorial.md#root-user-sign-in-tutorial). If you forgot your root user password, you can reset it. See [I forgot my root user password for my AWS account](#troubleshoot-forgot-root-password) for more information. If you forgot your root user email address, check your email inbox for an email from AWS.
+ If you tried to sign in to your root user account and received the error: **Password recovery is disabled for my root user account**, you have no root user credentials. You can't sign in as a root user or perform password recovery for your account’s root user. AWS member accounts managed using AWS Organizations may not have a root user password, access keys, signing certificates, or active multi-factor authentication (MFA).

  Only the management account or delegated administrator for IAM can perform root user actions in your member account. Contact your administrator if you need to perform a task that requires root user credentials. For more information, see [Centrally manage root access for member accounts](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_root-user.html#id_root-user-access-management) in the *AWS Identity and Access Management User Guide*.

**IAM user sign-in page**
+ If you or someone else created an IAM user within an AWS account, you must know that AWS account ID or alias to sign in. Enter your account ID or alias, username, and password in to the [AWS Management Console](https://console.aws.amazon.com/). To learn how to access the IAM user sign-in page, see [To sign in as an IAM user](introduction-to-iam-user-sign-in-tutorial.md#iam-user-sign-in-tutorial). If you forgot your IAM user password, you can see [I forgot my IAM user password for my AWS account](#troubleshoot-forgot-iam-password) for information on resetting your IAM user password. If you forgot your account number, search your email, browser favorites, or browser history for a URL that includes `signin.aws.amazon.com/`. Your account ID or alias will follow the `"account="` text in the URL. If you can’t find your account ID or alias, contact your administrator. Support can’t help you recover this information. You can’t see your account ID or alias until after you sign in. 

## Password reset is required for my root user
<a name="password-reset-required"></a>

For your account protection, you may receive the following message when you try to sign in to the AWS Management Console:

Password reset is required. For security concerns, you need to reset your password. To keep your account secure, you must choose **Forgot password** below and reset your password.

In addition to this message, AWS also notifies you when we identify a potential issue through the email associated with your account. This email includes the reason the password reset is required. For example, when we identify unusual login activity to your AWS account or credentials associated with your AWS account are publicly available online.

Update your password to ensure your root user credentials stay secure. To learn how to reset your root user password, see [I forgot my root user password for my AWS account](#troubleshoot-forgot-root-password).

## I don't have access to the email for my AWS account
<a name="troubleshoot-lost-email"></a>

When you create an AWS account, you provide an email address and password. These are the credentials for the AWS account root user. If you aren't sure of the email address associated with your AWS account, look for saved correspondence ending in @signin.aws or @verify.signin.aws to any email address for your organization that might have been used to open the AWS account. Ask other members of your team, organization, or family. If someone you know created the account, they can help you get access.

If you know the email address but no longer have access to the email, first try to recover access to the email using one of the following options:
+ If you own the domain for the email address, you can restore a deleted email address. Alternatively, you can set up a catch-all for your email account, which "catches all" messages sent to email addresses that no longer exist in the mail server and redirects them to another email address.
+ If the email address on the account is part of your corporate email system, we recommend that you contact your IT system administrators. They might be able to help you regain access to the email.

If you're still not able to sign in to your AWS account, you can find alternate support options by contacting [Support](https://support.aws.amazon.com/#/contacts/aws-account-support/).

## My MFA device is lost or stopped working
<a name="troubleshoot-MFA-issues"></a>

If your MFA device is lost, damaged, or not working, you don't receive a one-time passcode (OTP) when you send an MFA verification request.

**IAM users**  
You can sign in using another MFA device registered to the same IAM user.  
IAM users must contact an administrator to deactivate an MFA device that is not working. These users can't recover their MFA device without the administrator's assistance. Your administrator is typically an Information Technology (IT) personnel who has a higher level of permissions to the AWS account than other members of your organization. This individual created your account and provides users with their access credentials to sign in.

**Root users**  
To recover access to the root user, you must sign in using another MFA device registered to the same root user. Then, review the following options to recover or update your MFA device:  
+ For step-by-step directions to recover an MFA device, see [What if an MFA device is lost or stops working?](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_mfa_lost-or-broken.html)
+ For step-by-step directions on how to update a telephone number for an MFA device, see [How do I update my telephone number to reset my lost MFA device?](https://aws.amazon.com/premiumsupport/knowledge-center/reset-mfa-device/)
+ For step-by-step directions to activate MFA devices, see [Enabling MFA devices for users in AWS](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_mfa_enable.html).
+ If you can't recover your MFA device, contact [Support](https://support.aws.amazon.com/#/contacts/aws-mfa-support).
**Note**  
IAM users must contact their administrator for assistance with MFA devices. Support can't assist IAM users with MFA device issues.

## I can’t access the AWS Management Console sign-in page
<a name="troubleshoot-firewalls"></a>

If you can't see your sign-in page, the domain might be blocked by a firewall. Contact your network administrator to add the following domains or URL endpoints to your web-content filtering solution allow-lists depending on what type of user you are and how you sign in.



|  |  | 
| --- |--- |
| Root user and IAM users | \*.signin.aws.amazon.com | 
| Amazon.com account sign-in | www.amazon.com | 
| IAM Identity Center users and first-party application sign-in | +  \*.awsapps.com (http://awsapps.com/) <br />+  \*.signin.aws  | 

## I cannot sign in due to network conditions in Sign-in resource-based policies
<a name="troubleshoot-rbp-network"></a>

If you see one of the following error messages, a Sign-in resource-based policy or resource control policy (RCP) might be restricting access based on your network location:
+ "Your authentication information is incorrect. Please try again."
+ "Authentication failed Invalid request"
+ "Authentication failed: To access this account, sign in from a different network, or contact your administrator for more information"

Contact your administrator or see [I cannot sign in due to network conditions in Sign-in resource-based policies](console-access-control.md#console-access-control-ts-network) for detailed troubleshooting steps.

## I am locked out of my account after enabling console authorization
<a name="troubleshoot-rbp-lockout"></a>

If you configured console authorization and can no longer access your account, you might not have configured excluded principals or emergency recovery access before enforcing the policy. For resolution steps including AWS CLI self-service, the `OrganizationAccountAccessRole`, and AWS Support options, see [I am locked out of my account after enabling console authorization](console-access-control.md#console-access-control-ts-lockout).

## My policy changes are not taking effect
<a name="troubleshoot-rbp-replication"></a>

Changes to console authorization configuration and resource permission statements replicate globally and may take a few minutes to take effect. If your changes are not visible after waiting, see [Changes that I make are not always immediately visible](console-access-control.md#console-access-control-ts-replication) for troubleshooting steps.

## How can I find my AWS account ID or alias
<a name="troubleshoot-find-aws-account-id-or-alias"></a>

If you are an IAM user and you aren't signed in, ask your administrator for the AWS account ID or alias. Your administrator is typically an Information Technology (IT) personnel who has a higher level of permissions to the AWS account than other members of your organization. This individual created your account and provides users with their access credentials to sign in. 

If you are an IAM user with access to the AWS Management Console, your account ID can be found in your sign-in URL. Check your emails from your administrator for the sign-in URL. The account ID is the first twelve digits in the sign-in URL. For example, in the following URL, `https://{{111122223333}}.signin.aws.amazon.com/console`, your AWS account ID is 111122223333.

After you sign in to the AWS Management Console, you can find your account information located in the navigation bar next to your Region. For example in the following screenshot, the IAM user Carlos has an AWS account of 1111-2222-3333.

![Account information drop-down box with account ID highlighted](http://docs.aws.amazon.com/signin/latest/userguide/images/find-account-id.png)




For more information about your AWS account ID and alias and how to find it, see [Your AWS account ID and its alias](https://docs.aws.amazon.com/IAM/latest/UserGuide/console_account-alias.html).

## I need my account verification code
<a name="troubleshoot_general_cant-sign-in"></a>

If you provided your account email address and password, AWS sometimes requires you to provide a one-time verification code. To retrieve the verification code, check the email that's associated with your AWS account for a message from Amazon Web Services. The email address ends in @signin.aws or @verify.signin.aws. Follow the directions in the message. If you don't see the message in your account, check your spam and junk folders. If you no longer have access to the email, see [I don't have access to the email for my AWS account](#troubleshoot-lost-email).

## I forgot my root user password for my AWS account
<a name="troubleshoot-forgot-root-password"></a>

If you are a root user and you have lost or forgotten the password for your AWS account, you can reset your password by selecting the "Forgot Password" link in the AWS Management Console. You must know your AWS account's email address and must have access to the email account. You will be emailed a link during the password recovery process to reset your password. The link will be sent to the email address you used to create your AWS account.

To reset the password for an account that you created using AWS Organizations, see [Accessing a member account as the root user](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_accounts_access.html#orgs_manage_accounts_access-as-root).

**To reset your root user password**

1. Use your AWS email address to begin signing in to the [AWS Management Console](http://signin.aws.amazon.com/console/) as the **root user**. Then, choose **Next**.   
![Root user entering their email address in to the AWS Management Console.](http://docs.aws.amazon.com/signin/latest/userguide/images/reset-root-user-pswd-step-1.png)
**Note**  
If you are signed in to the [AWS Management Console](http://signin.aws.amazon.com/console/) with IAM user credentials, then you must sign out before you can reset the root user password. If you see the account-specific IAM user sign-in page, choose **Sign-in using root account credentials** near the bottom of the page. If necessary, provide your account email address and choose **Next** to access the **Root user sign in** page. 

1. Choose **Forgot password?**  
![Forgot password link highlighted on AWS Management Console page.](http://docs.aws.amazon.com/signin/latest/userguide/images/reset-root-user-pswd-step-2.png)

1. Complete the password recovery steps. If you can't complete the security check, try listening to the audio or refreshing the security check for a new set of characters. An example of a password recovery page is shown in the following image.  
![Password recovery steps to reset root user user password.](http://docs.aws.amazon.com/signin/latest/userguide/images/reset-root-user-pswd-step-3.png)

1. After you complete the password recovery steps, you receive a message that further instructions have been sent to the email address associated with your AWS account.

   An email with a link to reset your password is sent to the email used to create the AWS account.
**Note**  
The email will come from an address ending in @signin.aws or @verify.signin.aws.

1. Select the link provided in the AWS email to reset your AWS root user password.

1. The link directs you to a new webpage to create a new root user password.  
![Creating a new root user user password.](http://docs.aws.amazon.com/signin/latest/userguide/images/reset-root-user-pswd-step-6.png)

   You receive a confirmation that your password reset was successful. A successful password reset is shown in the following image.  
![Confirmation for successfully resetting root user user password.](http://docs.aws.amazon.com/signin/latest/userguide/images/reset-root-user-pswd-step-7.png)

For more information on resetting your root user password, see [How do I recover a lost or forgotten AWS password?](https://aws.amazon.com/premiumsupport/knowledge-center/recover-aws-password/)

## I forgot my IAM user password for my AWS account
<a name="troubleshoot-forgot-iam-password"></a>

To change your IAM user password, you must have the proper permissions. For more information about resetting your IAM user password, see [How an IAM user changes their own password](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_passwords_user-change-own.html).

If you do not have the permission to reset your password, then only your IAM administrator can reset the IAM user password. IAM users should contact their IAM administrator to reset their password. Your administrator is typically an Information Technology (IT) personnel who has a higher level of permissions to the AWS account than other members of your organization. This individual created your account and provides users with their access credentials to sign in.

![AWS Management Console showing the IAM user forgot password link.](http://docs.aws.amazon.com/signin/latest/userguide/images/iam-user-reset-pswd-message.png)


For security purposes, Support doesn't have access to view, provide, or change your credentials.

For more information on resetting your IAM user password, see [How do I recover a lost or forgotten AWS password?](https://aws.amazon.com/premiumsupport/knowledge-center/recover-aws-password/)

To learn how an administrator can manage your password, see [Managing passwords for IAM users](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_passwords_admin-change-user.html).

## I forgot my federated identity password for my AWS account
<a name="troubleshoot-forgot-federated-identity-password"></a>

Federated identities sign in to access AWS accounts with external identities. The type of external identity in use determines how federated identities sign in. Your administrator creates federated identities. Check with your administrator for more details on how to reset your password. Your administrator is typically an Information Technology (IT) personnel who has a higher level of permissions to the AWS account than other members of your organization. This individual created your account and provides users with their access credentials to sign in. 

## I can’t sign in to my existing AWS account and I can't create a new AWS account with the same email address
<a name="troubleshoot-cannot-create-new-acc"></a>

You can associate an email address with only one AWS account root user. If you close your root user account and it remains closed for more than 90 days, then you are not able to reopen your account or create a new AWS account using the e-mail address associated with this account.

To fix this issue, you can use subaddressing where you add a plus sign (\+) after your usual email address when you sign up for a new account. The plus sign (\+) can be followed by uppercase or lowercase letters, numbers, or other Simple Mail Transfer Protocol (SMTP) supported characters. For example, you can use `email+1@yourcompany.com` or `email+tag@yourcompany.com` where your usual email is `email@yourcompany.com`. This is considered a new address even though it’s connected to the same inbox as your usual email address. Before you sign up for a new account, we recommend that you send a test email to your appended email address to confirm that your email provider supports subaddressing.

## I need to reactivate my suspended AWS account
<a name="troubleshoot-suspended-aws-account"></a>

If your AWS account is suspended and you want to reinstate it, see [How can I reactivate my suspended AWS account?](https://aws.amazon.com/premiumsupport/knowledge-center/reactivate-suspended-account/)

## I need to contact Support for sign-in issues
<a name="troubleshoot-contact-support"></a>

If you tried everything, you can get help from Support by completing the [Billing and Account Support request](https://support.aws.amazon.com/#/contacts/aws-account-support/).

## I need to contact AWS Billing for billing issues
<a name="troubleshoot-contact-billing"></a>

If you can't sign in to your AWS account and would like to contact AWS Billing for billing issues, you can do so through a [Billing and Account Support request](https://support.aws.amazon.com/#/contacts/aws-account-support/). For more information about AWS Billing and Cost Management, including your charges and payment methods, see [Getting help with AWS Billing](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/billing-get-answers.html). 

## I have a question about a retail order
<a name="troubleshoot-retail-issue"></a>

If you have an issue with your www.amazon.com account or a question about a retail order, see [Support Options & Contact Us](https://www.amazon.com/gp/help/customer/display.html?nodeId=GSD587LKW72HKU2V). 

## I need help managing my AWS account
<a name="troubleshoot-other-issues"></a>

If you need help changing a credit card for your AWS account, reporting fraudulent activity, or closing your AWS account, see [Troubleshooting other issues with AWS accounts](https://docs.aws.amazon.com/accounts/latest/reference/troubleshooting_other.html).

## My AWS access portal credentials aren't working
<a name="credentials-not-working-portal"></a>

When you can't sign in to your AWS access portal, try to remember how you previously accessed AWS.

**If you don't remember using a password at all**

You might have previously accessed AWS without using AWS credentials. This is common for enterprise single sign-on through IAM Identity Center. Accessing AWS this way means that you use your corporate credentials to access AWS accounts or applications without entering your credentials.
+ **AWS access portal** – If an administrator allows you to use credentials from outside AWS to access AWS, you need the URL for your portal. Check your email, browser favorites, or browser history for a URL that includes `awsapps.com/start` or `signin.aws/platform/login`.

  For example, your custom URL might include an ID or a domain such as `https://{{d-1234567890}}.awsapps.com/start`. If you can't find your portal link, contact your administrator. Support can't help you recover this information. 

If you remember your username and password, but your credentials don't work, you might be on the wrong page. Look at the URL in your web browser, if it's https://signin.aws.amazon.com/ then a federated user or IAM Identity Center user can't sign-in using their credentials.
+ **AWS access portal** – If an administrator set up an AWS IAM Identity Center (successor to AWS Single Sign-On) identity source for AWS, you must sign in using your username and password at your AWS access portal for your organization. To locate the URL for your portal check your email, secure password storage, browser favorites, or browser history for a URL that includes `awsapps.com/start` or `signin.aws/platform/login`. For example, your custom URL might include an ID or a domain such as `https://{{d-1234567890}}.awsapps.com/start.` If you can’t find your portal link, contact your administrator. Support can’t help you recover this information.

## I forgot my IAM Identity Center password for my AWS account
<a name="troubleshoot-forgot-iam-identity-center-password"></a>

If you are a user in IAM Identity Center and you have lost or forgotten the password for your AWS account, you can reset your password. You must know the email address used for the IAM Identity Center account and have access to it. A link to reset your password is sent to your AWS account email.

**To reset your user in IAM Identity Center password**

1. Use your AWS access portal URL link and enter your username. Then, choose **Next**.  
![user in IAM Identity Center signing in to AWS access portal.](http://docs.aws.amazon.com/signin/latest/userguide/images/iam-identity-center-user-reset-pswd-step-1.png)

1. Select **Forgot password** as shown in the following image.  
![Forgot password link highlighted on your AWS access portal.](http://docs.aws.amazon.com/signin/latest/userguide/images/iam-identity-center-user-reset-pswd-step-2.png)

1. Complete the password recovery steps.  
![Password recovery step for user in IAM Identity Center to reset their password.](http://docs.aws.amazon.com/signin/latest/userguide/images/iam-identity-center-user-reset-pswd-step-3.png)

1. After you complete the password recovery steps, you receive the following message confirming that you've been sent an email message that you can use to reset your password.  
![Confirmation for successfully completing the password recovery step for user in IAM Identity Center.](http://docs.aws.amazon.com/signin/latest/userguide/images/iam-identity-center-user-reset-pswd-step-4.png)

   An email with a link to reset your password is sent to the email associated with the IAM Identity Center user account. Select the link provided in the AWS email to reset your password. The link directs you to a new web page to create a new password. After creating a new password, you receive confirmation that the password reset was successful.

   If you didn't receive an email to reset your password, ask your administrator to confirm which email is registered with your user in IAM Identity Center.

## I receive an error that states ‘It’s not you, it’s us’ when I try to sign in to the IAM Identity Center console
<a name="error-sign-in-idc"></a>

This error indicates there is a setup problem with your instance of IAM Identity Center or the external identity provider (IdP) it’s using as its identity source. We recommend that you verify the following:
+ Verify the date and time settings on the device you’re using to sign in. We recommend that you allow the date and time to be set automatically. If that’s not available, we recommend syncing your date and time to a known [Network Time Protocol (NTP)](https://en.wikipedia.org/wiki/Network_Time_Protocol) server.
+ Verify that the IdP certificate uploaded to IAM Identity Center is the same one provided by your identity provider. You can check the certificate from the [IAM Identity Center console](https://console.aws.amazon.com/singlesignon/) by navigating to **Settings**. In the **Identity Source** tab, under **Action**, choose **Manage Authentication**. You may need to import a new certificate.
+ In your IdP’s SAML metadata file, ensure that the NameID Format is `urn:oasis:names:tc:SAML:1.1:nameid-format:emailAddress`.
+ If you're using AD Connector, verify that the credentials for the service account are correct and have not expired. For more information, see [ Update your AD Connector service account credentials in Directory Service](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ad_connector_update_creds.html).