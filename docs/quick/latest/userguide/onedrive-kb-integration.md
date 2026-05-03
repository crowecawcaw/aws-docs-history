# Microsoft OneDrive knowledge base integration

Use the Microsoft OneDrive knowledge base integration to index OneDrive content
so that Amazon Quick agents can search and answer questions about it.

Amazon Quick uses a pre-registered multi-tenant application to connect to OneDrive
for knowledge bases. You do not need to create an app registration. When a user first
connects, Microsoft presents a consent dialog. An administrator can grant consent on
behalf of the entire organization, or individual users can consent for
themselves.

## Before you begin

Make sure you have the following before you set up the integration.

- A Microsoft 365 account with OneDrive access.
- For subscription requirements, see [Set up integrations in the console](integration-console-setup-process.md "integration-console-setup-process.md").
- Your Microsoft administrator may need to grant organizational consent
  before users can create a OneDrive knowledge base. Administrators can
  grant organization-wide consent by signing in and choosing
  **Consent on behalf of your organization** during the
  integration creation flow.

###### Note

When an administrator grants organizational consent, Microsoft Entra
automatically creates an Enterprise Application (service principal) in your
tenant. You can disable or delete this service principal at any time from
**Enterprise applications** in the Microsoft Entra admin
center, which immediately revokes all access.

## Set up the knowledge base integration

1. In the Amazon Quick console, choose
   **Knowledge**.
2. Choose **Microsoft OneDrive** and choose the Add
   (plus "+") button.
3. In the **Create OneDrive knowledge base** dialog,
   under **Connected account**, choose
   **Sign in to OneDrive** and complete the Microsoft
   sign-in and consent flow.
4. Under **Create knowledge base**, enter a name and
   an optional description for your knowledge base.
5. In the **Content** section, choose
   **Add content** and select the OneDrive files or
   folders you want to index.
6. Choose **Create**.

## Supported content types

- **Microsoft Office documents:** Word, Excel,
  PowerPoint
- **PDF files**
- **Text files and rich text documents**
- **Text documents with embedded images**
- **Audio and video files**

## Access controls

###### Important

When Amazon Quick indexes OneDrive content, it does not sync access
control lists (ACLs) from OneDrive. All indexed content is accessible to any
user who has access to the knowledge base in Amazon Quick, regardless of their
permissions in OneDrive. Review which content you include when creating a
knowledge base.

## Limitations

- File comments synchronization is not supported.

## Manage and troubleshoot

To edit, share, or delete your integration, see [Managing existing integrations](integration-workflows.md#managing-existing-integrations "integration-workflows.md#managing-existing-integrations").

For general knowledge base troubleshooting, including sync issues and
missing documents, see [Troubleshooting knowledge bases](troubleshooting-knowledge-bases.md "troubleshooting-knowledge-bases.md").
