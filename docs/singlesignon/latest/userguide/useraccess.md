# Single sign-on access to AWS accounts

You can assign users in your connected directory permissions to the management account
 or member accounts in your organization in AWS Organizations based on [common job functions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_job-functions.html "https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_job-functions.html"). Or you can use custom permissions to meet your
 specific security requirements. For example, you can grant database administrators broad
 permissions to Amazon RDS in development accounts but limit their permissions in production
 accounts. IAM Identity Center configures all the necessary user permissions in your AWS accounts
 automatically.

###### Note

You might need to grant users or groups permissions to operate in the AWS Organizations management account. Because it is a highly privileged account, additional security restrictions require you to have the [IAMFullAccess](https://console.aws.amazon.com/iam/home#policies/arn:aws:iam::aws:policy/IAMFullAccess "https://console.aws.amazon.com/iam/home#policies/arn:aws:iam::aws:policy/IAMFullAccess") policy or equivalent permissions before you can set this up. These additional security restrictions are not required for any of the member accounts in your AWS organization.

###### Topics

* [Assign user or group access to AWS accounts](assignusers.md "assignusers.md")
* [Remove user and group access to an
 AWS account](howtoremoveaccess.md "howtoremoveaccess.md")
* [Revoke active IAM role sessions created
 by permission sets](revoke-user-permissions.md "revoke-user-permissions.md")
* [Delegate who can assign single sign-on
 access to users and groups in the management account](howtodelegatessoaccess.md "howtodelegatessoaccess.md")
