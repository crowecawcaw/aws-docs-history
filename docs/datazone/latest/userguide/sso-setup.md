# Setting up AWS IAM Identity Center for Amazon DataZone

###### Note

AWS Identity Center must be enabled in the same AWS Region as your Amazon DataZone
domain. Currently, AWS Identity Center can only be enabled in a single AWS Region.

You can access the Amazon DataZone data portal by using either your single sign-on (SSO)
credentials or AWS credentials. Follow the instructions in this section to set up AWS
IAM Identity Center for Amazon DataZone. For more information about using Amazon DataZone with your
AWS credentials, see [Configure the IAM permissions required to use the
Amazon DataZone management console](create-iam-roles.md "create-iam-roles.md").

You can skip the procedures in this section if you already have AWS IAM Identity
Center (successor to AWS Single Sign-On) enabled and configured in the same AWS region
where you want to create your Amazon DataZone domain.

Complete the following procedure to enable AWS IAM Identity Center (successor to AWS
Single Sign-On).

1. To enable AWS IAM Identity Center, you must sign in to the AWS Management
   Console by using the credentials of your AWS Organizations management account. You
   can't enable IAM Identity Center while signed in with credentials from an AWS
   Organizations member account. For more information, see [Creating and managing an organization](../../../organizations/latest/userguide/orgs_manage_org.md "../../../organizations/latest/userguide/orgs_manage_org.md") in the AWS Organizations User
   Guide.
2. Open the [AWS IAM
   Identity Center (successor to AWS Single Sign-On) console](https://console.aws.amazon.com/singlesignon "https://console.aws.amazon.com/singlesignon") and use the
   region selector in the top navigation bar to choose the AWS region in which you
   want create your Amazon DataZone domain.
3. Choose **Enable**.
4. Choose your identity source.

By default, you get an IAM Identity Center store for quick and easy user
management. Optionally, you can connect an external identity provider instead. In
this procedure, we use the default IAM Identity Center store.

For more information, see [Choose your identity source](../../../singlesignon/latest/userguide/get-started-choose-identity-source.md "../../../singlesignon/latest/userguide/get-started-choose-identity-source.md"). 5. In the IAM Identity Center navigation pane, choose **Groups**,
and choose **Create group**. Enter the group name and choose
**Create**. 6. In the IAM Identity Center navigation pane, choose
**Users**. 7. On the **Add user** screen, enter the required information and
choose **Send an email to the user with password setup
instructions**. The user should get an email about the next setup
steps. 8. Choose **Next: Groups**, choose the group that you want, and
choose **Add user**. Users should receive an email inviting them to
use SSO. In this email, they need to choose Accept invitation and set the password.
After you create your Amazon DataZone domain, you can enable AWS Identity Center for
Amazon DataZone and provide access to your SSO users and SSO groups. For more information, see
[Enable IAM Identity Center for
Amazon DataZone](enable-IAM-identity-center-for-datazone.md "enable-IAM-identity-center-for-datazone.md").
