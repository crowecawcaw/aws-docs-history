

# Change the name of an enrolled account
<a name="change-account-name"></a>

Follow the procedure in this section to change the name of an enrolled AWS Control Tower account.

**Note**  
To change the name of an AWS *administrator* account, you must have admin permissions and be logged in as the account's root user. 

**To change the name of an account created by AWS Control Tower, by using AWS Organizations console or APIs**
+ Follow the [instructions available](https://docs.aws.amazon.com/accounts/latest/reference/manage-acct-update-acct-name.html#update-account-name-orgs) in the *AWS Account Management Reference Guide*.

**Alternative method to change the name of an account created by AWS Control Tower**

1. Recover the root password for the account. You can follow the steps outlined in this article, [How do I recover a lost or forgotten AWS password?](https://aws.amazon.com/premiumsupport/knowledge-center/recover-aws-password/)

1. Sign in to the account with the root password.

1. In the AWS Billing console, navigate to the **Account settings** page.

1. Change the name in **Account settings**, as you would for any other AWS account.

1. AWS Control Tower automatically updates itself to reflect the name change. This update will not be reflected in the provisioned product in AWS Service Catalog.