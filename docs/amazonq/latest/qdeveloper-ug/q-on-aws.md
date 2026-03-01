# Using Amazon Q Developer on AWS apps and websites

Use Amazon Q Developer in the AWS Management Console, AWS Console Mobile Application, AWS Marketing website, AWS Documentation website,
and supported chat applications to ask questions about AWS. You can ask Amazon Q
about AWS architecture, best practices, support, and documentation. Amazon Q can also help
with code that you're writing with the AWS SDKs and AWS Command Line Interface (AWS CLI).

In the AWS Management Console, you can ask Amazon Q about your AWS resources and costs, contact Support
directly, and diagnose common console errors.

To quickly provide access to features of Amazon Q Developer on AWS, attach the `AmazonQDeveloperAccess`
AWS managed policy to the IAM identity using Amazon Q. For permissions needed for specific
features, see the topic for the feature you want to use.

###### Topics

- [Authenticating to your Amazon Q Developer Pro subscription](#qdevpro-authentication "#qdevpro-authentication")
- [Chatting with Amazon Q Developer about AWS](chat-with-q.md "chat-with-q.md")
- [Using Amazon Q Developer plugins](plugins.md "plugins.md")
- [Automating AWS services with Amazon Q Developer Console-to-Code](console-to-code.md "console-to-code.md")
- [Diagnosing common errors in the console with Amazon Q Developer](diagnose-console-errors.md "diagnose-console-errors.md")
- [Using Amazon Q Developer to chat with Support](support-chat.md "support-chat.md")

## Authenticating to your Amazon Q Developer Pro subscription

To access Amazon Q at the Free tier, sign in to the AWS Management Console. Any Free tier features
are available as long as you have the required permissions.

To access Amazon Q at the Pro tier, sign to the console with IAM Identity Center. When you sign in
with IAM Identity Center, including authenticating through an external identity provider that is
connected to IAM Identity Center, you will automatically have access to the Pro tier if your IAM Identity Center
identity is subscribed to Amazon Q Developer Pro.

For more information on the Amazon Q Developer Pro tier, see [Tiers of service for Q Developer – Free and Pro](q-tiers.md "q-tiers.md").

###### Note

If you see an error message that starts with, `Your account has not been
 configured to use an Amazon Q subscription`, see [Troubleshooting Amazon Q Developer Pro subscriptions](q-admin-setup-subscribe-troubleshooting.md "q-admin-setup-subscribe-troubleshooting.md") for troubleshooting
tips.

If you sign in to the AWS console with IAM or federation with IAM, then you will
be prompted to authenticate with IAM Identity Center when you reach a Free tier limit or attempt to
use a feature only available at the Pro tier.
