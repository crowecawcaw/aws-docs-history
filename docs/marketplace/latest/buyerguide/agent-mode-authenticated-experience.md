

# Use the authenticated experience in agent mode

When you are signed in, you can also buy or subscribe to products and deploy them through agent mode. These actions are part of the authenticated experience and require sign-in. You can keep your agent mode projects in your AWS account and open them on any device.

**Before you start**

You need an AWS account and the permissions described in the following section.

**Permissions you need**

To sign in to agent mode, your IAM user or role needs the `signin:CreateOAuth2Token` permission. With it, you can move projects to your AWS account and let agent mode act on your account. Ask your administrator to add the following policy to your role. Alternatively, use the `AWSMarketplaceFullAccess` managed policy, which already includes this permission.

```JSON
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": "signin:CreateOAuth2Token",
      "Resource": "arn:aws:signin:*:*:service-principal/marketplace-mcp.amazonaws.com",
      "Condition": {
        "StringEquals": { "signin:OAuthGrantType": "client_credentials" }
      }
    }
  ]
}
```

If your role has this permission and you still see "Access denied", a policy in your AWS organization might block it (for example, a service control policy). Ask your administrator to check your organization's policies.

To buy, subscribe, and deploy, you also need the following managed policies:
+ To buy or subscribe, you need the [AWSMarketplaceFullAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSMarketplaceFullAccess.html) managed policy.
+ To deploy, in addition to the preceding policy, you also need both the [AmazonSSMFullAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AmazonSSMFullAccess.html) and [AmazonEC2FullAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AmazonEC2FullAccess.html) managed policies.

**To sign in to AWS**

1. At the top right, choose **Sign in**.

1. Sign in on the AWS sign-in page. Agent mode returns you to the page you left.

   After you sign in, the Home page shows your browser projects and your AWS account projects in one list.

**To move a browser project to your AWS account**

1. On the Home page, select one or more projects that show **Browser** as the saved location.

1. Choose **Move to AWS account**. For multiple projects, choose **Move projects**.

1. Read the warning in the dialog. Anyone who shares this AWS account gets access to the projects you move. If you are not signed in, sign in when prompted and the move continues.

1. Confirm the move. The project then shows **AWS account**.

**To open your projects on another device**
+ Open agent mode on the other device or browser and sign in to the same AWS account.

  Your **AWS account** projects appear on the Home page. **Browser** projects remain only in the browser where you created them.

**Let agent mode act on your AWS account**

Some tasks need your AWS account, for example, purchasing or deploying. If you are not signed in, the conversation shows "To continue, sign in to AWS". Choose **Sign in** and the task continues. Agent mode then asks you to confirm the action and the account. Review what it will do and choose **Allow** or **Deny**.

Auto-approve is turned off by default. To turn it on or off, use the auto-approve toggle in the chat box. This setting applies per project.

**Warning**  
When auto-approve is turned on, agent mode can take actions in your AWS account without asking for your approval each time. AI can make mistakes.

**Fix sign-in problems**


| What you see | What to do | 
| --- | --- | 
| "Your session has expired. To continue, sign in to AWS again." | Sign in again. Your project and conversation stay. | 
| "Sign in again" in the sign-in prompt | Choose it. Agent mode ends your old AWS session and starts a new sign-in. | 
| "Access denied" with a Copy button | Choose Copy and send the text to your AWS administrator. It names the service, action, and resource you need. | 
| "Your account isn't permitted to authorize agent mode." | Signing in again doesn't fix this. Contact your AWS account administrator. | 