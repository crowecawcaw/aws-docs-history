

# Configure attribute mappings for your sync
<a name="manage-sync-configure-attribute-mapping-configurable-ADsync"></a>

For more information about available attributes, see [Attribute mappings between IAM Identity Center and External Identity Providers directory](attributemappingsconcept.md).

**To configure attribute mappings in IAM Identity Center to your directory**

1. Open the [IAM Identity Center console.](https://console.aws.amazon.com/singlesignon)

1. Choose **Settings**.

1. On the **Settings** page, choose the **Identity source** tab, choose **Actions**, and then choose **Manage Sync**.

1. Under **Manage Sync**, choose **View attribute mapping**.

1. Under **Active Directory user attributes**, configure **IAM Identity Center identity store attributes** and **Active Directory user attributes**. For example, you might want to map the IAM Identity Center identity store attribute `email` to the Active Directory user directory attribute `${objectguid}`.
**Note**  
Under **Group attributes**, **IAM Identity Center identity store attributes** and **Active Directory group attributes** cannot be changed.

1. Choose **Save changes**. This returns you to the **Manage Sync** page.