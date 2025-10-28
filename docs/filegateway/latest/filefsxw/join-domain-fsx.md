Amazon FSx File Gateway is no longer available to new customers. Existing
customers of FSx File Gateway can continue to use the service normally. For capabilities
similar to FSx File Gateway, visit [this blog post](https://aws.amazon.com/blogs/storage/switch-your-file-share-access-from-amazon-fsx-file-gateway-to-amazon-fsx-for-windows-file-server/ "https://aws.amazon.com/blogs/storage/switch-your-file-share-access-from-amazon-fsx-file-gateway-to-amazon-fsx-for-windows-file-server/").

# Configure Microsoft Active Directory domain access

settings

In this step, you configure access settings to join your Amazon FSx File Gateway to a Microsoft
Active Directory domain.

###### To configure Active Directory settings

1. In the Storage Gateway console, choose **FSx file systems** from the
   navigation menu.
2. Choose **Attach FSx file system**.
3. On the **Confirm gateway** page, choose the gateway you want to
   join to your Active Directory domain from the drop-down menu.

If you don't have a gateway, you must create one. Make sure your gateway can
resolve the name of your Active Directory Domain Controller. For information, see
[Prerequisites](Requirements.md#user-requirements "Requirements.md#user-requirements"). 4. Enter values for the **Active Directory settings**:

###### Note

If your gateway is already joined to a domain, you don't need to join again.
Go to the next step.

    * For **Domain name**, enter the domain name of the Active
     Directory that you want to use.
    * For **Domain user**, enter the user name of the Active
     Directory user that you want to use to join the gateway to the domain. This
     user must have the necessary permissions. For more information, see [Active Directory service account permission
     requirements](ad-serviceaccount-permissions.md "ad-serviceaccount-permissions.md").
    * For **Domain password**, enter the password for the
     user.
    * For **Organizational unit- optional**, you can specify an
     organizational unit the Active Directory belongs to.


    ###### Note

    If you leave this field blank, joining a domain creates an Active
     Directory computer account in the default computers container (which is
     not an OU), using the gateway's **Gateway ID** as the
     account name (for example, SGW-1234ADE). It is not possible to customize
     the name of this account.

    If your Active Directory environment requires that you pre-stage
     accounts to facilitate the join domain process, you will need to create
     this account ahead of time.

    If your Active Directory environment has a designated OU for new
     computer objects, you must specify that OU when joining the
     domain.
    * Enter a value for **Domain controller(s) - optional**.

5. Choose **Next** to open the **Attach FSx File
   system** page.
   **Next step**

[Attach an Amazon FSx for Windows File Server file system](attach-fsxw-filesystem.md "attach-fsxw-filesystem.md")
