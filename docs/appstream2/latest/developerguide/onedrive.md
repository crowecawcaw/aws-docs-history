# Enable and Administer OneDrive for Business for Your AppStream 2.0

Users

AppStream 2.0 supports the following persistent storage options for users in your
organization.

- OneDrive for Business
- Google Drive for Google Workspace
- Home folders
  You can enable one or more options for your organization. When you enable OneDrive for
  Business for an AppStream 2.0 stack, users of the stack can link their OneDrive for Business
  account to AppStream 2.0. Then they can sign into their OneDrive for Business account and
  access their OneDrive folder during application streaming sessions. Any changes that
  they make to files or folders in OneDrive during those sessions are automatically backed
  up and synchronized, so that they are available to users outside of their streaming
  sessions.

###### Important

You can enable OneDrive for Business for accounts in your OneDrive domains only,
but not for personal accounts. AppStream 2.0 requires that you configure your Microsoft
Azure Active Directory environment to allow end-user consent to applications. For
more information, see [Configure how end-users consent to applications](https://docs.microsoft.com/en-us/azure/active-directory/manage-apps/configure-user-consent "https://docs.microsoft.com/en-us/azure/active-directory/manage-apps/configure-user-consent") in the Azure Active
Directory [Application management](https://docs.microsoft.com/en-us/azure/active-directory/manage-apps/ "https://docs.microsoft.com/en-us/azure/active-directory/manage-apps/") documentation.

The admin consent workflow lets administrators grant access to applications that
require administrator approval. If the admin consent workflow is configured in your
Azure Active Directory environment, follow the step given in [Enable OneDrive for Your AppStream 2.0 Users](enable-onedrive.md "enable-onedrive.md") to specify the domains that require admin consent.

###### Note

You can enable OneDrive for Business for Windows stacks, but not for Linux stacks
or stacks associated with multi-session fleets.

###### Contents

- [Enable OneDrive for Your AppStream 2.0 Users](enable-onedrive.md "enable-onedrive.md")
- [Disable OneDrive for Your AppStream 2.0 Users](disable-onedrive.md "disable-onedrive.md")
