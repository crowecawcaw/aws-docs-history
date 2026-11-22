

# Knowledge bases

With AWS Quick knowledge bases, you can bring your organization's content into one unified search experience. Built-in integrations set up in a few steps and sync your data across sources such as Google Drive, OneDrive, Confluence, SharePoint, S3, and a web crawler, so your team can find information no matter where it is stored.

## How knowledge bases work
<a name="how-knowledge-bases-work"></a>

A knowledge base is an organized, indexed collection of your content, optimized for generative AI-powered retrieval and question answering. Multiple knowledge bases can be created from the same source, and all can reside within a shared Quick Index. For example, if you sync two folders from Google Drive and create two knowledge bases — one for “Policy Documents” to answer queries such as *“What’s our refund policy”* and one for “Customer feedback” to answer queries such as *“What are the common customer complaints”* — both can be part of the same index. Quick distinguishes between them using the knowledge base id, so queries can be filtered to retrieve only the relevant documents from the desired knowledge base. This allows users to organize, secure, and retrieve information relevant to different domains or use cases, even though the underlying data is indexed together.

Your knowledge bases can be used individually or shared with team members through AWS Quick spaces. Entity-Level Access Control (ELAC) enables security at the knowledge base level, ensuring that users only receive information from knowledge bases they're authorized to access. For more information, see [Sharing and access control](managing-knowledge-bases-managing-knowledge-bases.md#managing-knowledge-bases-sharing-and-access-control).

### Creation process
<a name="knowledge-base-creation-process"></a>

You can create knowledge bases while setting up a new data access integration and use existing integrations to create additional knowledge bases:

1. **Data access integration setup** - Connect to your external data source

1. **Content selection** - Choose which content to include through filters and scope settings

1. **Indexing** - AWS Quick processes and indexes the selected content

1. **Availability** - The knowledge base becomes available for use in spaces and by AI agents

For step-by-step instructions, see [Creating knowledge bases in AWS Quick](creating-knowledge-bases-creating-knowledge-bases.md).

### Capabilities
<a name="knowledge-base-capabilities"></a>

Each knowledge base provides the following capabilities:
+ **Content indexing** - Processes text, documents, and structured data from external sources
+ **Semantic search** - Enables AI-powered search across indexed content
+ **Automatic synchronization** - Keeps content up-to-date with configurable sync schedules
+ **Entity-Level Access Control (ELAC)** - Ensures that users only receive information from knowledge bases they're authorized to access. For more information, see [Sharing and access control](managing-knowledge-bases-managing-knowledge-bases.md#managing-knowledge-bases-sharing-and-access-control).
+ **Multi-space usage** - Can be used across multiple spaces and by different AI agents

## General workflow
<a name="general-workflow"></a>

The typical workflow for working with knowledge bases follows these steps:

1. **Set up data source integration** - Connect to your external application (such as SharePoint, Google Drive, or Confluence) with appropriate authentication. For more information, see [Integration-specific guides](integration-guides.md).

1. **Create a knowledge base** - You can create a knowledge base while configuring your new integration. Configure your content filters by setting up include filters, file type restrictions, and folder selections to focus on relevant content. For more information, see [Creating knowledge bases in AWS Quick](creating-knowledge-bases-creating-knowledge-bases.md).

1. **Set sync schedule** - Configure how often the knowledge base updates with new content from the source. For more information, see [Sync frequency](#sync-frequency).

1. **Monitor and manage** - Review sync status, manage access permissions.

## Common configuration settings
<a name="common-configuration-settings"></a>

Knowledge bases share common configuration patterns across different data source integrations. Understanding these settings helps you optimize content indexing and manage sync behavior effectively.

**Note**  
While these configuration options are available across most integrations, specific settings and available options may vary depending on your chosen data source integration.

### Service principal for knowledge base operations
<a name="kb-service-principal"></a>

If you use a customer-managed key (CMK) as your default CMK and Q data key (see [Encrypting your AWS Quick data with AWS Key Management Service customer managed keys](customer-managed-keys.md)), AWS Quick accesses your AWS KMS key using the `qbusiness.amazonaws.com` and `quicksight.amazonaws.com` service principals during knowledge base sync operations.

**Note**  
Ensure that any policies governing access to your CMK permit both the `qbusiness.amazonaws.com` and `quicksight.amazonaws.com` service principals.

### File size and content limits
<a name="file-size-and-content-limits"></a>

Configure file size limits to optimize processing performance and manage storage costs. The specific limits vary by content type and are displayed in the console when you configure your knowledge base.

**Standard text documents**  
Applies to documents like PDFs, Word files, and text files. File size limit is 500 MB.

**Tabular files**  
Applies to tabular files like CSV and XLS files. File size limit is 50 MB.

**Video files**  
Available when video processing is enabled. Supported formats include `.mp4`, `.mov`, `.m4v`. File size limit is 10 GB (10240 MB). Quick Index supports up to **10 video files per GB of storage**. If your use case requires higher video volumes, please open a ticket with AWS support to extend this limit.

**Audio files**  
Available when audio processing is enabled. Supported formats include `.mp3`,` .wav`,` .m4a`, `.flac`, and` .ogg`. Limit is 2 GB (2048 MB) for audio files.  
The maximum amount of text that can be extracted from a single document is 30 MB.

**Images**  
Quick Index applies the following limits for images:  
+ **Per-document limit**: 500 images per document
+ **Per-GB limit**: 10K images per GB of index storage
+ **Per-index limit**: 2M images per index
If your use case requires higher image volumes, please open a ticket with AWS support to extend these limits.

### Sync schedule and safeguards
<a name="sync-schedule-and-safeguards"></a>

Configure how often your knowledge base updates and protect against unintended content deletion:

#### Sync frequency
<a name="sync-frequency"></a>

Data refresh frequency is set to daily by default. You can edit the sync frequency to configure how often the knowledge base updates with new content from the source.

#### Document deletion safeguard
<a name="document-deletion-safeguard"></a>

Protect your indexed content from accidental mass deletion by setting a maximum deletion percentage threshold. If a sync job would delete more documents than your threshold allows, the deletion phase is skipped, preserving your existing indexed content.

This safeguard protects against temporary network issues, permission changes, or source system problems that might make content temporarily unavailable.

#### Maximum sync duration
<a name="maximum-sync-duration"></a>

Each sync run has a maximum runtime of 14 days. If a sync run is still in progress after 14 days, AWS Quick ends the run with a status of **FAILED** and the following error message:

Maximum sync time exceeded: Please edit your sync configuration to reduce the number of files to be crawled and ingested. For web crawler data sources, we recommend using Web Search feature if you want to chat with public websites like wikipedia.org.

If your sync run reaches this limit, edit your knowledge base to narrow the sync scope. For example, apply include or exclude filters, restrict the file types or folders being crawled, or split the content across multiple knowledge bases. For web crawler data sources, consider using the Web Search feature instead when your goal is to chat with large public websites.