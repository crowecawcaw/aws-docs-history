

# Working with AWS IAM Identity Center and AWS Control Tower
<a name="sso"></a>

In AWS Control Tower, IAM Identity Center allows central cloud administrators and end-users to manage access to multiple AWS accounts and business applications. By default, AWS Control Tower uses this service to set up and manage access to the accounts created through Account Factory, unless you have selected the option to self-manage your identity and access control.

For more information about selecting an identity provider, see [IAM Identity Center guidance](sso-guidance.md).

For a brief tutorial about how to set up your IAM Identity Center users and permissions in AWS Control Tower, you can view this video (6:23). For better viewing, select the icon at the lower right corner of the video to enlarge it to full screen. Captioning is available.

[![AWS Videos](http://img.youtube.com/vi/y_n9xN5mg1g/0.jpg)](http://www.youtube.com/watch?v=y_n9xN5mg1g)


**About setting up AWS Control Tower with IAM Identity Center **

When you initially set up AWS Control Tower, only the root user user and any IAM users with the correct permissions can add IAM Identity Center users. However, after end users have been added in the **AWSAccountFactory** group, they can create new IAM Identity Center users from the Account Factory wizard. For more information, see [Provision and manage accounts with Account Factory](account-factory.md).

If you choose the recommended default, AWS Control Tower sets up your landing zone with a preconfigured directory that helps you manage user identities and single sign-on, so that your users have federated access across accounts. When you set up your landing zone, this default directory is created to contain *user groups* and *permission sets*.

**Note**  
You can delegate administration of AWS IAM Identity Center in your organization to an account other than the management account, by using the delegated administrator feature of IAM Identity Center. If you choose to use this feature, be aware that Administrators with access to manage group membership *also* can manage groups assigned to the management account. For more information, see this blog post, entitled, [Getting started with AWS SSO delegated administration](https://aws.amazon.com/blogs/security/getting-started-with-aws-sso-delegated-administration/)

## Things to know about IAM Identity Center accounts and AWS Control Tower
<a name="sso-good-to-know"></a>

Here are some good things to know when working with IAM Identity Center user accounts in AWS Control Tower.
+ If your AWS IAM Identity Center user account is disabled, you'll get an error message when trying to provision new accounts in Account Factory. You can re-enable your IAM Identity Center user in the IAM Identity Center console.
+ If you specify a new IAM Identity Center user email address when you update the provisioned product associated with an account that was vended by Account Factory, AWS Control Tower creates a new IAM Identity Center user account. The previously created user account is not removed. If you prefer to remove the previous IAM Identity Center user email address from AWS IAM Identity Center, see [Disabling a User](https://docs.aws.amazon.com/singlesignon/latest/userguide/disableuser.html).
+ AWS IAM Identity Center has been [integrated with Azure Active Directory](https://aws.amazon.com/blogs/aws/the-next-evolution-in-aws-single-sign-on/), and you can connect your existing Azure Active Directory to AWS Control Tower.
+ For more information about how the behavior of AWS Control Tower interacts with AWS IAM Identity Center and different identity sources, refer to the [Considerations for Changing Your Identity Source](https://docs.aws.amazon.com/singlesignon/latest/userguide/manage-your-identity-source-considerations.html) in the AWS IAM Identity Center documentation.