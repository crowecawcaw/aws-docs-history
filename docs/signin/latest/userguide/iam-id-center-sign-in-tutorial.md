

# Sign in to your AWS access portal
<a name="iam-id-center-sign-in-tutorial"></a>

A user in IAM Identity Center is a member of AWS Organizations. A user in IAM Identity Center can access multiple AWS accounts and business applications by signing in to your AWS access portal with a specific sign-in URL. For more information about the specific sign-in URL, see [AWS access portal](sign-in-urls-defined.md#access-portal-url).

This sign-in method is only supported for accounts created with Sign up for AWS (advanced). For more information, see [Compare sign-up options](https://docs.aws.amazon.com/accounts/latest/reference/sign-up-for-aws.html).

Before you sign in to an AWS account as a user in IAM Identity Center, gather the following required information.
+ Corporate user name
+ Corporate password
+ Specific sign-in URL

**Note**  
After you sign in, your AWS access portal session is valid for 8 hours. You are required to sign in again after 8 hours.

## To sign in to your AWS access portal
<a name="iam-idc-user-sign-in-tutorial"></a>

1.  In your browser window, paste in the sign-in URL that you were provided through email, such as `https://{{your_subdomain}}.awsapps.com/start` or the dual-stack URL format `https://{{[IAM Identity Center instance ID]}}.portal.{{[Region]}}.app.aws`. Then, press **Enter**. 

1. Sign in using your corporate credentials (like a user name and password). 
**Note**  
If your administrator sent you an email one-time password (OTP) and this is your first time signing in, enter that password. After you're signed in, you must create a new password for future sign-ins.

1. If you are asked for a verification code, check your email for it. Then copy and paste the code into the sign-in page.
**Note**  
Verification codes are typically sent through email, but the delivery method might vary. If haven't received one in your email, check with your administrator for details about your verification code.

1. If MFA is enabled for your user in IAM Identity Center, you then authenticate using it.

1. After authentication, you can access any AWS account and application that appears in the portal.

   1. To sign in to the AWS Management Console choose the **Accounts** tab and select the individual account to manage.

      The role for your user is displayed. Choose the role name for the account to open the AWS Management Console. Choose **Access keys** to get credentials for command line or programmatic access.

   1. Choose the **Applications** tab to display available applications and choose the icon of the application that you want to access. 

Signing in as an user in IAM Identity Center provides you credentials to access resources for a set duration of time, called a session. By default, a user can be signed into an AWS account for 8 hours. The IAM Identity Center Administrator can specify a different duration, from a minimum of 15 minutes to a maximum of 90 days. After your session ends, you can sign in again.

### Additional information
<a name="iam-idc-user-sign-in-tutorial-more-info"></a>

If you want more information about users in IAM Identity Center, refer to the following resources.
+ For an overview of IAM Identity Center, see [What is IAM Identity Center?](https://docs.aws.amazon.com/singlesignon/latest/userguide/what-is.html)
+ For details about your AWS access portal, see [Using the AWS access portal](https://docs.aws.amazon.com/singlesignon/latest/userguide/using-the-portal.html).
+ For details about IAM Identity Center sessions, see [User authentications](https://docs.aws.amazon.com/singlesignon/latest/userguide/authconcept.html).
+ For step-by-step directions on how to reset your IAM Identity Center user password, see [I forgot my IAM Identity Center password for my AWS account](troubleshooting-sign-in-issues.md#troubleshoot-forgot-iam-identity-center-password).
+ If you or your organization implement IP or domain filtering, you may need to allowlist domains to create and use your AWS access portal. IAM Identity Center supports both IPv4 and dual-stack endpoints. If your network uses IPv6, use the dual-stack endpoint domains. For details about allowlisting domains, see [Domains to add to your allow list](allowlist-domains.md).