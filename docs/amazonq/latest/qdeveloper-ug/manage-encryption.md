# Managing the encryption method in Amazon Q Developer

###### Note

This section does not apply to personal accounts (Builder IDs).

By default, Amazon Q Developer uses an AWS managed key for encryption. For some features, you can set
up a customer managed key to encrypt data. For a list of features that support encryption with
customer managed keys, see [Data encryption](data-encryption.md#encryption-rest "data-encryption.md#encryption-rest").

To set the key used for encryption, complete the following procedure.

1. Sign in to the AWS Management Console.
2. Switch to the Amazon Q Developer console.

To use the Amazon Q Developer console, you must have the permissions defined in [Allow administrators to use the Amazon Q Developer console](id-based-policy-examples-admins.md#q-admin-setup-admin-users "id-based-policy-examples-admins.md#q-admin-setup-admin-users")
. 3. Choose **Settings**. 4. Choose **Edit** in the Amazon Q Developer account details panel.

![The Amazon Q Developer console settings page](images/q-dev-console-settings-3.png) 5. On the **Edit details** page, expand the **Encryption key -
optional** section. 6. To use a customer managed key for encryption, select **Customize encryption
settings (advanced)**. 7. In the search bar that appears, search for the name of the key you want to use for
encryption or enter the key ARN.

If you haven't created a key yet, choose **Create an AWS KMS key**, and
then return to this page to add your key. 8. To disable encryption with your customer managed key and revert to an AWS managed key
for encryption, deselect **Customize encryption settings (advanced)**.
