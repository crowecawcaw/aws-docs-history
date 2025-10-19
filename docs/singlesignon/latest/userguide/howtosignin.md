# Signing in to the AWS access portal

The AWS access portal provides IAM Identity Center users with single sign-on access to all their assigned
 AWS accounts and applications through a web portal. The following outlines how you can sign
 in to the AWS access portal, tips for signing in, and how to sign out of the AWS access portal. 


###### Prerequisites


IAM Identity Center needs to be enabled to use the AWS access portal. For more information, see [Enable IAM Identity Center](enable-identity-center.md "enable-identity-center.md").


###### Note

After you sign in, the default duration for your AWS access portal session is 8 hours. Be
 aware that an administrator can [change the
 duration](configure-user-session.md "configure-user-session.md") of this session.


## Sign in to the AWS access portal


###### To sign in to the AWS access portal

1. In your browser window, paste in the sign-in URL that you were provided and choose
 **Enter**. The URL looks like
 `d-xxxxxxxxxx.awsapps.com/start` or
 ``your_subdomain`.awsapps.com/start`. We recommend
 that you bookmark this link to the portal now so that you can quickly access it
 later.
2. Sign in using your standard company sign in credentials.


###### Note

If your administrator sent you an email one-time password (OTP) and this is your
 first time signing in, enter that password. After you are signed in, you must create a
 new password for future sign-ins.


 If you are prompted for a **Verification code**, check
 your email and then copy and paste the code into the sign-in page.


###### Note

Verification codes are typically sent through email, but the delivery method can
 vary. Check with your administrator for details.
3. Once signed in, you can access any AWS account and application that displays in the
 portal.

## Trusted devices


When you choose the option **This is a trusted device** from the
 sign-in page, IAM Identity Center considers all future sign-ins from that device as authorized. This means
 that IAM Identity Center will not present an option to enter in an MFA code as long as you are using that
 trusted device. However, there are some exceptions, including signing in from a new browser
 or when your device has been issued an unknown IP address.


## Sign in tips for the AWS access portal


Here are some tips to help you manage your AWS access portal experience.



* Occasionally, you might need to sign out and sign back in to the AWS access portal. This
 might be necessary to access new applications that your administrator recently assigned
 to you. This is not required, however, because all new applications are refreshed every
 hour.
* When you sign in to the AWS access portal, you can open any of the applications listed in
 the portal by choosing the application’s icon. After you are done using the application,
 you can either close the application or sign out of the AWS access portal. Closing the
 application signs you out of that application only. Any other applications that you have
 opened from the AWS access portal remain open and running.
* Before you can sign in as a different user, you must first sign out of the
 AWS access portal. Signing out from the portal completely removes your credentials from the
 browser session.
* Once you sign in to the AWS access portal, you can switch to a role. Switching roles
 temporarily sets aside your original user permissions and instead gives you the
 permissions assigned to the role.  For more information, see [Switching to a role (console)](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_switch-role-console.html?icmpid=docs_iam_console "https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_switch-role-console.html?icmpid=docs_iam_console").

## Signing out of the AWS access portal


When you sign out from the portal, your credentials are completely removed from the
 browser session. For more information, see  [Sign out of the AWS access portal](https://docs.aws.amazon.com/signin/latest/userguide/aws-access-portal-signing-out-iam-identity-center-user.html "https://docs.aws.amazon.com/signin/latest/userguide/aws-access-portal-signing-out-iam-identity-center-user.html") in the *AWS Sign-In* guide.


###### To sign out of the AWS access portal

* In the AWS access portal, choose **Sign out** from the navigation
 bar.

###### Note

If you want to sign in as a different user, you must first sign out of the
 AWS access portal.
