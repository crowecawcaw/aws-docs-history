

# Amazon S3 integration
<a name="s3-integration"></a>

With Amazon S3 integration in Amazon Quick, you can create knowledge bases from documents stored in S3 buckets. This integration supports data ingestion capabilities for indexing and searching S3 content.

**Note**  
This guide covers Amazon S3 data ingestion integration for knowledge base creation. For Amazon S3 connectors that perform Amazon S3 operations such as uploading, downloading, and deleting files, see [AWS service connectors](builtin-services-integration.md). Amazon S3 actions are only supported for Quick Automate.

## What you can do
<a name="s3-integration-capabilities"></a>

Amazon S3 users can ask questions about content stored in their Amazon S3 buckets. For example, users can inquire about key findings from documents, search for specific information across multiple file types, or analyze data patterns.

The integration enables users to quickly access and understand information from their Amazon S3 content, regardless of file location or type. It also provides contextual details such as modification dates and file metadata, contributing to more efficient information discovery and better-informed decision making.

## Before you begin
<a name="s3-integration-prerequisites"></a>

Before you set up Amazon S3 integration, make sure you have the following:
+ AWS account with Amazon S3 access.
+ Amazon S3 bucket with documents to index.
+ Amazon Quick Enterprise subscription.
+ Necessary permissions to create Amazon S3 integrations.
+ Your administrator must grant Amazon Quick access to the Amazon S3 buckets you want to use. For more information, see [Grant Amazon Quick access to Amazon S3 buckets](s3-admin-setup.md#s3-grant-bucket-access).

**Note**  
Cross-account Amazon S3 access is only supported within the same AWS region.