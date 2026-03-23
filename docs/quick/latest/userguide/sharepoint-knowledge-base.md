# Microsoft SharePoint knowledge base integration

Use the Microsoft SharePoint knowledge base integration to index SharePoint content
so that Amazon Quick agents can search and answer questions about it.

Amazon Quick uses a pre-registered multi-tenant application to connect to SharePoint
for knowledge bases. You do not need to create an app registration. When a user first
connects, Microsoft presents a consent dialog. An administrator can grant consent on
behalf of the entire organization, or individual users can consent for
themselves.

## Before you begin

Make sure you have the following before you set up the integration.

- A Microsoft 365 account with SharePoint access.
- For subscription requirements, see [Set up integrations in the console](integration-console-setup-process.md "integration-console-setup-process.md").
- Your Microsoft administrator may need to grant organizational consent
  before users can create a SharePoint knowledge base. Administrators can
  grant organization-wide consent by signing in and choosing
  **Consent on behalf of your organization** during the
  integration creation flow.

###### Note

When an administrator grants organizational consent, Microsoft Entra
automatically creates an Enterprise Application (service principal) in your
tenant. You can disable or delete this service principal at any time from
**Enterprise applications** in the Microsoft Entra admin
center, which immediately revokes all access.

## Permissions granted during consent

| SharePoint knowledge base – permissions | Permission                   | API                                                                                 | Description |
| --------------------------------------- | ---------------------------- | ----------------------------------------------------------------------------------- | ----------- |
| `Files.Read.All`                        | Microsoft Graph              | Allows the app to read all files that the user can<br>access.                       |
| `Notes.Read.All`                        | Microsoft Graph              | Allows the app to read all OneNote notebooks that the user can<br>access.           |
| `User.Read`                             | Microsoft Graph              | Allows users to sign in and allows the app to read the<br>signed-in user's profile. |
| `Sites.Read.All`                        | Microsoft Graph              | Allows the app to read documents and list items in all site<br>collections.         |
| `offline_access`                        | Microsoft Graph              | Allows the app to maintain access when the user is not actively<br>signed in.       |
| `AllSites.Read`                         | Office 365 SharePoint Online | Allows the app to read items in all site<br>collections.                            |

## Set up the knowledge base integration

1. In the Amazon Quick console, choose **Integrations**.
2. Choose **Microsoft SharePoint** and choose the Add
   (plus "+") button.
3. In the **Create SharePoint knowledge base** dialog,
   under **Connected account**, choose
   **Sign in to SharePoint** and complete the Microsoft
   sign-in and consent flow.
4. Under **Create knowledge base**, enter a name and
   an optional description for your knowledge base.
5. In the **Content** section, choose
   **Add content** and select the SharePoint pages,
   files, or folders you want to index.
6. Choose **Create**.

## Supported content types

- **Document libraries:** Word, Excel,
  PowerPoint, PDF, OneNote (.one)
- **Media files:** MP3, MP4, MOV,
  WMV
- **Site pages and wiki pages**

## Access controls

###### Important

When Amazon Quick indexes SharePoint content, it does not sync access
control lists (ACLs) from SharePoint. All indexed content is accessible to any
user who has access to the knowledge base in Amazon Quick, regardless of their
permissions in SharePoint. Review which content you include when creating a
knowledge base.

## Manage and troubleshoot

To edit, share, or delete your integration, see [Managing existing integrations](integration-workflows.md#managing-existing-integrations "integration-workflows.md#managing-existing-integrations").

For general knowledge base troubleshooting, including sync issues and
missing documents, see [Troubleshooting knowledge bases](troubleshooting-knowledge-bases.md "troubleshooting-knowledge-bases.md").

### SharePoint-specific issues

- **Admin consent required** – Some
  organizations require an administrator to grant consent before
  individual users can connect. An administrator must sign in and choose
  **Consent on behalf of your organization** during
  the consent flow.
- **Enterprise Application disabled** –
  If the service principal was previously disabled in **Enterprise
  applications** in the Microsoft Entra admin center,
  re-enable it to restore access.
- **SharePoint throttling** – SharePoint
  may throttle requests during high usage periods. Retry the sync during
  off-peak hours.
