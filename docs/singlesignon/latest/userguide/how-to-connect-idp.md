

# How to connect to an external identity provider
<a name="how-to-connect-idp"></a>

There are different prerequisites, considerations, and provisioning procedures for the supported external IdPs. There are step-by-step tutorials available for several IdPs:
+ [CyberArk](cyberark-idp.md)
+ [Google Workspace](gs-gwp.md)
+ [JumpCloud](jumpcloud-idp.md)
+ [Microsoft Entra ID](idp-microsoft-entra.md)
+ [Okta](gs-okta.md)
+ [OneLogin](onelogin-idp.md)
+ [Ping Identity](pingidentity.md)

For more information on the considerations for external IdPs that IAM Identity Center supports, see [Using SAML and SCIM identity federation with external identity providers](other-idps.md).

 The following procedure provides a general overview of the procedure that is used with all external identity providers.

**To connect to an external identity provider**

1. Open the [IAM Identity Center console](https://console.aws.amazon.com/singlesignon).

1. Choose **Settings**.

1. On the **Settings** page, choose the **Identity source** tab, and then choose **Actions > Change identity source**.

1. Under **Choose identity source**, select **External identity provider**, and then choose **Next**. 

1. Under **Configure external identity provider**, do the following:

   1. Under **Service provider metadata**, choose **Download metadata file** to download the metadata file and save it on your system. The IAM Identity Center SAML metadata file is required by your external identity provider.
**Note**  
The SAML metadata file you download contains both IPv4-only and dual-stack assertion consumer service (ACS) URLs. Further, if your IAM Identity Center is replicated to additional Regions, the metadata file contains ACS URLs for each additional Region. If your external IdP has a limit on the number of ACS URLs, you will need to remove the unnecessary ACS URLs. For example, if your organization has fully adopted dual-stack endpoints and no longer uses IP4v-only ones, you can remove the latter. An alternative approach is to not use the metadata file but to copy and paste the ACS URLs into the external IdP.

   1. Under **Identity provider metadata**, choose **Choose file**, and locate the metadata file that you downloaded from your external identity provider. Then upload the file. This metadata file contains the necessary public x509 certificate used to trust messages that are sent from the IdP.

   1. Choose **Next**.
**Important**  
Changing your source to or from Active Directory removes all existing user and group assignments. You must manually reapply assignments after you have successfully changed your source.

1. After you read the disclaimer and are ready to proceed, enter **ACCEPT**.

1. Choose **Change identity source**. A status message informs you that you successfully changed the identity source.