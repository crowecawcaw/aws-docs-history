

# Enable and Administer OneDrive for Business for Your WorkSpaces Applications Users
<a name="onedrive"></a>

WorkSpaces Applications supports the following persistent storage options for users in your organization. 
+ OneDrive for Business
+ Google Drive for Google Workspace
+ Home folders

You can enable one or more options for your organization. When you enable OneDrive for Business for an WorkSpaces Applications stack, users of the stack can link their OneDrive for Business account to WorkSpaces Applications. Then they can sign into their OneDrive for Business account and access their OneDrive folder during application streaming sessions. Any changes that they make to files or folders in OneDrive during those sessions are automatically backed up and synchronized, so that they are available to users outside of their streaming sessions. 

**Important**  
You can enable OneDrive for Business for accounts in your OneDrive domains only, but not for personal accounts. Unless an administrator grants consent for the whole tenant and you select **Reuse existing Microsoft consent** for the domain, you must configure your Microsoft Azure Active Directory environment to allow end-user consent to applications. For more information, see [Configure how end-users consent to applications](https://docs.microsoft.com/en-us/azure/active-directory/manage-apps/configure-user-consent) in the Azure Active Directory [Application management](https://docs.microsoft.com/en-us/azure/active-directory/manage-apps/) documentation.   
Your Azure Active Directory environment, not WorkSpaces Applications, decides whether users can consent on their own or need administrator approval. If your environment requires administrator consent, an administrator must grant consent to WorkSpaces Applications for the whole tenant. Then select **Reuse existing Microsoft consent** for each domain, as described in [Enable OneDrive for Your WorkSpaces Applications Users](enable-onedrive.md). If that option is cleared, users are prompted for consent every time they link their account, and users who can't consent on their own are blocked even after an administrator grants consent.

**Note**  
You can enable OneDrive for Business for Windows stacks, but not for Linux stacks.  
To enable OneDrive for Business for stacks associated with multi-session fleets, the image must use [WorkSpaces Applications Agent Release Notes](agent-software-versions.md) released on or after June 29, 2026 or your image is using [Update an Image by Using Managed WorkSpaces Applications Image Updates](keep-image-updated-managed-image-updates.md) released on or after June 29, 2026.

**Topics**
+ [Enable OneDrive for Your WorkSpaces Applications Users](enable-onedrive.md)
+ [Disable OneDrive for Your WorkSpaces Applications Users](disable-onedrive.md)