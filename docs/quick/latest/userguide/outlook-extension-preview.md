# Amazon Quick Microsoft Outlook extension (Preview)

###### Note

This extension is currently available as a preview. During the preview period,
the extension is fully functional for end users and production workloads.
Administrative features such as centralized deployment controls and usage monitoring
are being developed and will be available when the extension becomes generally
available. Functionality and features may change during the preview period. We
recommend using this extension instead of the legacy Microsoft Outlook
extension for new deployments.

The Quick extension for Microsoft Outlook integrates
AI-powered assistance directly into your email workflows. Users can leverage
Quick within Outlook to streamline their inbox and calendar
management, draft contextual emails using their Quick data, and perform
external actions without switching applications.

The Outlook extension enables users to:

- Prioritize and organize their inbox.
- Search for relevant email content for a topic using natural language.
- Schedule meetings and manage their calendars.
- Summarize emails and draft contextual responses using Quick data.
- Access their enterprise data and perform actions in external applications.
  The Amazon Quick Outlook extension is available within Amazon Quick
  to all eligible users by default and requires no administrative setup for user access if
  users can access the Microsoft Outlook app store. Users can search for
  Amazon Quick in the Microsoft Outlook app store or visit the [Quick
  for Outlook Microsoft store page](https://marketplace.microsoft.com/en-us/product/WA200010695 "https://marketplace.microsoft.com/en-us/product/WA200010695") to add the extension.

###### Important

- The Amazon Quick Outlook extension uses generative AI to
  create and execute code within your Outlook application
  sandbox to help you perform your Outlook tasks. AI can make
  mistakes and perform inaccurate actions within your Outlook
  mailbox.
- Amazon Quick does not use your user data for service improvement or for
  training its underlying large language models (LLMs).
  The following procedures are for IT administrators who want to automatically deploy
  the Amazon Quick Outlook extension across their organization on behalf
  of their users.

###### Topics

- [Prerequisites for deploying the Microsoft Outlook extension to your organization](#outlook-preview-prerequisites "#outlook-preview-prerequisites")
- [Deploying the Microsoft Outlook extension to your organization](#outlook-preview-deployment "#outlook-preview-deployment")

## Prerequisites for deploying the Microsoft Outlook extension to your organization

Before configuring access to the Amazon Quick extension to Microsoft
Outlook, administrators must complete the following steps:

1. Have a Microsoft 365 Business subscription and be a Global
   Admin or have administrative permissions (specifically
   `AppCatalog.ReadWrite.All`).
2. Have an Amazon Quick instance.

## Deploying the Microsoft Outlook extension to your organization

Follow these steps to deploy the extension to your users:

1. Login to M365 admin center.
2. Select **Settings** > **Integrated
   apps** in the left navigation menu.
3. Click on **Get apps**.
4. Search for "Amazon Quick".
5. Locate the tile for the Amazon Quick in Outlook and click
   on **Get it now**.
6. Confirm that you want to add the app.
7. Under **Assign users** you can choose
   **Entire organization** or **Specific
   users/groups** depending on your needs.
8. After selecting the users, review the app's requested permissions and
   capabilities and click **Next**.
9. Click **Finish Deployment**.
