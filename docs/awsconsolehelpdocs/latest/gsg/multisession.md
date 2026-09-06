

# Signing in to multiple accounts
<a name="multisession"></a>

You can sign in to up to five different identities simultaneously in a single web browser in the AWS Management Console. These can be any combination of root, IAM, or federated roles in different accounts or in the same account. Each identity you sign in to opens its own instance of the AWS Management Console in a new tab. 

When you enable multi-session support, the console URL contains a subdomain (for example, `https://000000000000-aaaaaaaa.us-east-1.console.aws.amazon.com/console/home?region=us-east-1`). Be sure to update your bookmarks and console links.

**Note**  
You must opt-in to multi-session support by choosing **Turn on multi-session** in the account menu in the AWS Management Console, or by choosing **Enable multi-session** on [https://console.aws.amazon.com/](https://console.aws.amazon.com/). You can opt-out of multi-sessions at any time by choosing **Disable multi-session** on [https://console.aws.amazon.com/](https://console.aws.amazon.com/) or by clearing your browser cookies. Opt-in is browser specific. 

**To sign in to multiple identities**

1. Sign in to the [AWS Management Console](https://console.aws.amazon.com/).

1. In the navigation bar, choose your account name.

1. Choose **Add session** and choose **Sign in**. A new tab will open for you to sign in.
**Note**  
For more information about signing in as a root or IAM user, see [Sign in to the AWS Management Console](https://docs.aws.amazon.com/signin/latest/userguide/how-to-sign-in.html) in the *AWS Sign-in* User Guide.

1. Enter your credentials.

1. Choose **Sign in**. The AWS Management Console loads in this tab as your chosen AWS identity.

1. 

**(Optional) To federate into additional roles**

   1. In the AWS IAM Identity Center access portal or your single-sign on (SSO) portal, sign in to the additional role.

   1. In the AWS Management Console choose your account name.

   1. View the additional sessions that you can choose.