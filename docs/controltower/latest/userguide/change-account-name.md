# Change the name of an enrolled account

Follow the procedure in this section to change the name of an enrolled
AWS Control Tower account.

###### Note

To change the name of an AWS _administrator_ account, you must have admin
permissions and be logged in as the account's root user.

###### To change the name of an account created by AWS Control Tower, by using AWS Organizations console or APIs

- Follow the [instructions available](../../../accounts/latest/reference/manage-acct-update-acct-name.md#update-account-name-orgs "../../../accounts/latest/reference/manage-acct-update-acct-name.md#update-account-name-orgs") in the _AWS Account Management Reference Guide_.

###### Alternative method to change the name of an account created by AWS Control Tower

1. Recover the root password for the account. You can follow the steps outlined
   in this article, [How do I
   recover a lost or forgotten AWS password?](https://aws.amazon.com/premiumsupport/knowledge-center/recover-aws-password/ "https://aws.amazon.com/premiumsupport/knowledge-center/recover-aws-password/")
2. Sign in to the account with the root password.
3. In the AWS Billing console, navigate to the **Account settings** page.
4. Change the name in **Account settings**, as you would for any
   other AWS account.
5. AWS Control Tower automatically updates itself to reflect the name change. This update
   will not be reflected in the provisioned product in AWS Service Catalog.
