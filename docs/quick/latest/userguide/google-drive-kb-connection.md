

# Creating a knowledge base in Amazon Quick
<a name="google-drive-kb-connection"></a>

In this phase, you create a knowledge base in Amazon Quick and provide the service account credentials from the Google Workspace configuration. Any enterprise user can complete this phase. Amazon Quick administrator access is not required.

If a Google Workspace administrator completed the Google Workspace configuration on your behalf, you need the JSON key file and the delegated admin email address before you proceed.

## Setting up the knowledge base
<a name="google-drive-kb-connection-setup"></a>

1. In the Amazon Quick console, choose **Knowledge**.

1. Under **Knowledge bases**, find **Google Drive**, and then choose the **Add** (\+) icon.

1. In the **Create Google Drive knowledge base** dialog, choose **Have admin credentials? Configure document-level access control.**

1. In the **Connected account** dropdown, choose **Add account**.

1. For **Name**, enter a name for the connection. Use a descriptive name such as your Google Workspace domain.
**Important**  
You cannot change the connection name after you save it.

1. Choose **Upload .JSON key**, and then choose the JSON file that you downloaded during the Google Workspace configuration.

1. For **Google workspace admin email**, enter the email address of the delegated admin user that you created during the Google Workspace configuration.

1. Choose **Next**.

## Choosing content to sync
<a name="google-drive-kb-connection-content"></a>

1. Enter a **Name** and optional **Description** for your knowledge base.

1. Choose which Google Drive content to include:
   + **My Drive (all users)** – Includes files from all users' My Drive in your organization.
   + **Shared with me (all users)** – Includes files that are shared with your users.
   + **Shared drives** – All shared drives sync by default. To include or exclude specific drives, use the **Filter type** dropdown and **Add shared drive IDs** field. You can enter 1 to 100 shared drive IDs.

1. Choose **Next** to configure advanced settings.

## Configuring advanced settings
<a name="google-drive-kb-connection-advanced"></a>

In the **Advanced settings** step, you can configure optional settings for the knowledge base.

Filter content by date  
Limit which documents are crawled based on their last modified date. The start date defaults to one year before today. You can change or clear the start date, and optionally set an end date.

Multi-media content, file size, and file patterns  
Choose which content types to include in the knowledge base.  
+ **Visual content in documents** – Extracts and indexes visual elements from supported document formats. This option is enabled by default.
+ **Audio files** – Transcribes and indexes audio files.
+ **Video files** – Transcribes and indexes video files.

Choose **Create** to create the knowledge base. After you choose **Create**, the data sync starts automatically.

## Managing and troubleshooting
<a name="google-drive-kb-admin-managed-manage"></a>

To edit, share, or delete your integration, see [Managing existing integrations](integration-workflows.md#managing-existing-integrations).

For information about knowledge base troubleshooting, including sync issues and missing documents, see [Troubleshooting knowledge bases](troubleshooting-knowledge-bases.md).

For information about sync reports, sync schedules, and verifying document-level access controls, see [Sync reports and observability](sync-reports-observability.md).

### Admin-managed setup issues
<a name="google-drive-kb-admin-troubleshooting"></a>
+ **Google API rate limiting** – Google Drive might throttle requests during high usage periods. If syncs fail or are incomplete, retry during off-peak hours.
+ **SSL certificate errors** – If you receive an error about SSL certificate errors when you create your knowledge base, verify the OAuth scopes that you configured during domain-wide delegation.