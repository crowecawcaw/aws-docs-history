

# Box knowledge base integration
<a name="box-knowledge-base"></a>

Use the Box knowledge base integration to index Box content so that Amazon Quick agents can search and answer questions about it. You can sync all of the Box content that you have access to, or choose specific Box folders and files. You can also configure advanced indexing settings when needed.

**Access control limitation**  
This user-managed setup does not support document-level access controls (ACLs). ACLs are mechanisms that control which users can access specific documents.

## Before you begin
<a name="box-kb-prerequisites"></a>

Make sure you have the following before you set up the integration.
+ A Box account with access to the files and folders that you want to include in the knowledge base.
+ For Quick subscription requirements, see [Set up integrations in the console](integration-console-setup-process.md).

## Setting up the knowledge base integration
<a name="box-kb-setup"></a>

The setup wizard has two steps: create the knowledge base, and configure optional additional settings.

### Creating the knowledge base
<a name="box-kb-setup-create"></a>

1. Sign in to the Amazon Quick console, and then choose **Knowledge**.

1. Under **Knowledge bases**, find **Box**, and then choose the **Add** (\+) icon.

1. In the **Create Box knowledge base** dialog, under **Connected account**, choose **Sign in to Box**. Complete the Box sign-in flow and grant the requested permissions.
**Note**  
The Box knowledge base integration uses Default OAuth app authentication. You authenticate directly with your Box account, and no additional credentials are needed.

1. Under **Create knowledge base**, enter a **Name** for your knowledge base.

1. (Optional) Enter a **Description** with notes about how the knowledge base will be used.

1. Under **Content**, choose which Box content to include:
   + **Add all content** – Includes all of the Box content that you have access to.
   + **Add specific content** – Includes only the Box folders and files that you specify. In the **Box file or folder URLs** field, enter a Box file or folder URL (for example, `https://app.box.com/file/987654321`) and choose **Add**. Repeat for each URL that you want to include.

1. Choose **Next: Additional settings** to configure indexing options, or choose **Create** to create the knowledge base with default settings.

### Configuring additional settings
<a name="box-kb-setup-settings"></a>

In the **Additional settings (optional)** step, you can configure indexing options under **Multi-media content, file size, and file patterns**.

Under **Advanced indexing**, configure the following options as needed:
+ **Visual content in documents** – Extracts and indexes visual content such as images and charts embedded in documents. This option is enabled by default.
+ **Audio files** – Transcribes and indexes audio files.
+ **Video files** – Transcribes and indexes video files.
+ **Maximum single file size** – The maximum file size for individual files, in MB (default: 500 MB).

Choose **Create** to create the knowledge base. After you choose **Create**, the data sync starts automatically.

## Managing knowledge bases
<a name="box-kb-management"></a>

### Editing existing knowledge bases
<a name="box-kb-edit"></a>

1. Sign in to the Amazon Quick console, and then choose **Knowledge bases**.

1. Select your Box knowledge base from the list.

1. Choose the **More options** icon (⋮) under **Actions**, then choose **Edit knowledge base**.

1. Update your configuration settings as needed and choose **Save**.

## Troubleshoot the Box knowledge base integration
<a name="box-kb-troubleshooting"></a>

To edit, share, or delete your integration, see [Managing existing integrations](integration-workflows.md#managing-existing-integrations).

For general knowledge base troubleshooting, including sync issues and missing documents, see [Troubleshooting knowledge bases](troubleshooting-knowledge-bases.md).