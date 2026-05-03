# Amazon Quick Microsoft Word extension (Preview)

###### Note

This extension is currently available as a preview. During the preview period,
the extension is fully functional for end users and production workloads.
Administrative features such as centralized deployment controls and usage monitoring
are being developed and will be available when the extension becomes generally
available. Functionality and features may change during the preview period. We
recommend using this extension instead of the legacy Microsoft Word
extension for new deployments.

The Quick extension for Microsoft Word integrates
AI-powered assistance directly in your Word document. Users can leverage
Quick within Word to draft content, make formatted edits,
and perform reviews with track changes and comments enabled.

The Word extension enables users to:

- Generate formatted documents using style guides and templates and
  Quick's enterprise data and apps.
- Make small- or large-scale edits to your document while maintaining its
  writing style and structure.
- Format or restructure your documents.
- Redline your documents with track changes and/or comments enabled.
  The Quick Word extension is available within Amazon Quick
  to all eligible users by default and requires no administrative setup for user access if
  users can access the Microsoft Word app store. Users can search for
  Amazon Quick in the Microsoft Word app store or visit the [Quick
  for Word Microsoft store page](https://marketplace.microsoft.com/en-us/product/WA200010615 "https://marketplace.microsoft.com/en-us/product/WA200010615") to add the extension.

###### Important

- The Amazon Quick Word extension uses generative AI to
  create and execute code within your Word application sandbox
  to help you perform tasks within Word. AI can make mistakes
  and perform inaccurate actions within your Word
  document.
- Amazon Quick does not use your user data for service improvement or for
  training its underlying large language models (LLMs).
  The following procedures are for IT administrators who want to automatically deploy
  the Amazon Quick Word extension across their organization on behalf of
  their users.

###### Topics

- [Prerequisites for deploying the Microsoft Word extension to your organization](#word-preview-prerequisites "#word-preview-prerequisites")
- [Deploying the Microsoft Word extension to your organization](#word-preview-deployment "#word-preview-deployment")

## Prerequisites for deploying the Microsoft Word extension to your organization

Before configuring access to the Amazon Quick extension to Microsoft
Word, administrators must complete the following steps:

1. Have a Microsoft 365 Business subscription and be a Global
   Admin or have administrative permissions (specifically
   `AppCatalog.ReadWrite.All`).
2. Have an Amazon Quick instance.

## Deploying the Microsoft Word extension to your organization

Follow these steps to deploy the extension to your users:

1. Login to M365 admin center.
2. Select **Settings** > **Integrated
   apps** in the left navigation menu.
3. Click on **Get apps**.
4. Search for "Amazon Quick".
5. Locate the tile for the Amazon Quick in Word and click on
   **Get it now**.
6. Confirm that you want to add the app.
7. Under **Assign users**, you can choose
   **Entire organization** or **Specific
   users/groups** depending on your needs.
8. After selecting the users, review the app's requested permissions and
   capabilities and click **Next**.
9. Click **Finish Deployment**.
