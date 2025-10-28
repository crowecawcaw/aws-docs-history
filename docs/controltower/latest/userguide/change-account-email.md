# Change email address of an enrolled

account

To change the email address of an enrolled member account in AWS Control Tower, follow the
procedure in this section.

###### Note

The following procedure doesn't allow you to change the email address of a
**management account**, **log
archive account**, or **audit account**.
For more information about that, see [How do I change the
email address associated with my AWS account?](https://aws.amazon.com/premiumsupport/knowledge-center/change-email-address/ "https://aws.amazon.com/premiumsupport/knowledge-center/change-email-address/") or contact AWS
Support.

###### To change the email address of an account that AWS Control Tower creates

1. Recover the root user password for the account. You can follow the steps in the
   article [How do I
   recover a lost or forgotten AWS password?](https://aws.amazon.com/premiumsupport/knowledge-center/recover-aws-password/ "https://aws.amazon.com/premiumsupport/knowledge-center/recover-aws-password/")
2. Sign in to the account with the root user password.
3. Change the email address as you would for any other AWS account, and wait
   for the change to reflect in AWS Organizations. You might experience a delay while the
   email address change finishes updating.
4. Update the provisioned product in Service Catalog using the email address that
   previously belonged to the account. The process for updating the provisioned
   product includes associating the new email address with the provisioned product.
   This way the email address change takes effect in AWS Control Tower. Use the new email
   address for updates to subsequently provisioned products.
   To change the password or email address of a member account that you created with
   AWS Organizations, see [Accessing a member account as the root user](../../../organizations/latest/userguide/orgs_manage_accounts_access.md#orgs_manage_accounts_access-as-root "../../../organizations/latest/userguide/orgs_manage_accounts_access.md#orgs_manage_accounts_access-as-root") in the _AWS Organizations User
   Guide_.

Alternatively, you can update the email address for an Account Factory or other member account
from the AWS Organizations console without logging in as the root user. For more information, see
[Updating the root user email address for a member account with AWS Organizations](../../../organizations/latest/userguide/orgs_manage_accounts_update_primary_email.md "../../../organizations/latest/userguide/orgs_manage_accounts_update_primary_email.md") in the _AWS Organizations User
Guide_.
