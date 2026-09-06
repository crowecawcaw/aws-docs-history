

# Change email address of an enrolled account
<a name="change-account-email"></a>

To change the email address of an enrolled AWS Control Tower account, follow the procedure in this section.

**Changing management account email addresses**  
To change the email address of an AWS management account, sign in as the root user with administrator permissions.

**Change the email address by using AWS Organizations**

1. For instructions on updating the root user email address, see [Update the root user email address for a member account](https://docs.aws.amazon.com/accounts/latest/reference/manage-acct-update-root-user-email.html#root-user-email-orgs) in the *AWS Account Management Reference Guide*.

1. After you update the email address, update the account in AWS Control Tower. This update associates the new email address with the account in AWS Control Tower. If updating the account through the Service Catalog provisioned product, specify the old email address as the value for the `AccountEmail` parameter.

**Change the email address by using root user credentials**

1. Recover the root user password for the account. For instructions on recovering a lost password, see [How do I recover a lost or forgotten AWS password?](https://aws.amazon.com/premiumsupport/knowledge-center/recover-aws-password/)

1. Sign in to the account with the root user password.

1. Change the email address as you would for any other AWS account, and wait for the change to take effect in AWS Organizations. You might experience a delay while the email address change finishes updating.

1. After you update the email address, update the account in AWS Control Tower. This update associates the new email address with the account in AWS Control Tower. If updating the account through the Service Catalog provisioned product, specify the old email address as the value for the `AccountEmail` parameter.