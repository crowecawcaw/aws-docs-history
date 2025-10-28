# Signing in to multiple accounts

You can sign in to up to five different identities simultaneously in a single web browser in the AWS Management Console. These can be any combination of root, IAM, or federated roles in different accounts or in the same account.
Each identity you sign in to opens its own instance of the AWS Management Console in a new tab.

When you enable multi-session support, the console URL contains a subdomain (for example, `https://000000000000-aaaaaaaa.us-east-1.console.aws.amazon.com/console/home?region=us-east-1`).
Be sure to update your bookmarks and console links.

###### Note

You must opt-in to multi-session support by choosing **Turn on multi-session** in the account menu in the AWS Management Console, or by choosing **Enable multi-session**
on [https://console.aws.amazon.com/](https://console.aws.amazon.com/ "https://console.aws.amazon.com/"). You can opt-out of multi-sessions at any time by choosing **Disable multi-session** on [https://console.aws.amazon.com/](https://console.aws.amazon.com/ "https://console.aws.amazon.com/") or by clearing your browser cookies. Opt-in is browser specific.

###### To sign in to multiple identities

1. Sign in to the [AWS Management Console](https://console.aws.amazon.com/ "https://console.aws.amazon.com/").
2. In the navigation bar, choose your account name.
3. Choose **Add session** and choose **Sign in**. A new tab will open for you to sign in.

###### Note

For more information about signing in as a root or IAM user, see [Sign in to the AWS Management Console](../../../signin/latest/userguide/how-to-sign-in.md "../../../signin/latest/userguide/how-to-sign-in.md") in the _AWS Sign-in_ User Guide. 4. Enter your credentials. 5. Choose **Sign in**. The AWS Management Console loads in this tab as your chosen AWS identity. 6. ###### (Optional) To federate into additional roles

    1. In the AWS IAM Identity Center access portal or your single-sign on (SSO) portal, sign in to
     the additional role.
    2. In the AWS Management Console choose your account name.
    3. View the additional sessions that you can choose.
