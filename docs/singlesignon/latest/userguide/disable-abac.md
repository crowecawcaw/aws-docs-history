# Disable attributes for access control

Use the following procedure to disable the ABAC feature and delete all of
the attribute mappings that have been configured.

###### To disable Attributes for access control

1. Open the [IAM Identity Center console](https://console.aws.amazon.com/singlesignon "https://console.aws.amazon.com/singlesignon").
2. Choose **Settings**.
3. On the **Settings** page, choose the
   **Attributes for access control** tab, and then
   choose **Manage attributes**.
4. On the **Manage attributes for access control**
   page, choose **Disable**.
5. In the **Disable attributes for access control**
   dialog window, review the information and when ready enter
   `DISABLE`, and then choose
   **Confirm**.

###### Important

This step deletes all attributes and stops the use of
attributes for access control when federating into
AWS accounts regardless of whether any attributes are present
in SAML assertions from an external identity source
provider.
