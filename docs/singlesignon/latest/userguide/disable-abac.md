

# Disable attributes for access control
<a name="disable-abac"></a>

Use the following procedure to disable the ABAC feature and delete all of the attribute mappings that have been configured. 

**To disable Attributes for access control**

1. Open the [IAM Identity Center console](https://console.aws.amazon.com/singlesignon).

1. Choose **Settings**.

1. On the **Settings** page, choose the **Attributes for access control** tab, and then choose **Manage attributes**.

1. On the **Manage attributes for access control** page, choose **Disable**.

1. In the **Disable attributes for access control** dialog window, review the information and when ready enter **DISABLE**, and then choose **Confirm**.
**Important**  
This step deletes all attributes and stops the use of attributes for access control when federating into AWS accounts regardless of whether any attributes are present in SAML assertions from an external identity source provider.