# Signing up for an Amazon Quick Suite subscription

When you first sign up for Amazon Quick Suite, you get a free trial subscription for twenty-five
users for 30 days. During the process of signing up, you may set options for your
identity provider.

Before you begin, make sure that you can connect to an existing AWS account. If you
don't have an AWS account, see [Complete initial configuration tasks](setting-up.md "setting-up.md"). The person who
signs up for Quick Suite needs to have the correct AWS Identity and Access Management (IAM) permissions.
For more information, see [IAM policy examples for Quick Suite](../../../quicksight/latest/user/iam-policy-examples.md "../../../quicksight/latest/user/iam-policy-examples.md").

To test your permissions, you can use the IAM policy simulator; for more
information, see [Testing IAM
policies with the IAM policy simulator](../../../IAM/latest/UserGuide/access_policies_testing-policies.md "../../../IAM/latest/UserGuide/access_policies_testing-policies.md"). Also, check whether your
AWS account is part of an organization based on the AWS Organizations service. If so and you
sign in as an IAM user, make sure that you didn't inherit any IAM permissions that
deny access to the required permissions. For more information on Organizations, see [What is AWS Organizations?](../../../organizations/latest/userguide/orgs_introduction.md "../../../organizations/latest/userguide/orgs_introduction.md")

###### Note

Your data is encrypted by default using AWS-managed keys. Admins can adjust
settings for custom encryption in the admin portal after signing up.

###### To subscribe to Quick Suite

1. Sign in to your AWS account and open Quick Suite from the AWS Management Console.
   You can find it under **Analytics** or by searching for
   _Quick Suite_.

Your AWS account number is displayed for verification purposes. 2. Enter a unique account name for Quick Suite.

    * Enter a notification email address for the Quick Suite account
     owner or group. This email address receives service and usage
     notifications.

3. Choose the AWS Region that you want to use for your initial data storage
   capacity, called SPICE.
4. Choose an authentication method that you want to connect to Quick Suite
   with. Select from one of the following:
   - **(Recommended) Password-based or Single-Sign
     On**
   - **IAM Identity Center**
   - **Single-Sign On Only**
   - **Active Directory**

5. Review the choices that you made, then choose **Create
   account**.
6. Upon completion, your Quick Suite account will be created. To open
   Quick Suite, choose **Go to Quick Suite**.
