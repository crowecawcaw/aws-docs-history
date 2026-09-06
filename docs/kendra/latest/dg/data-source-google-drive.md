

Amazon Kendra is no longer open to new customers. For capabilities similar to Amazon Kendra, explore Amazon Bedrock Knowledge Bases. [Learn more](https://docs.aws.amazon.com/kendra/latest/dg/kendra-availability-change.html).

# Google Drive
<a name="data-source-google-drive"></a>

Google Drive is a cloud-based file storage service. You can use Amazon Kendra to index documents stored in shared drives, My Drives, and Shared with me folders in your Google Drive data source. You can index both Google Workspace documents as well as documents listed in [Types of documentation](https://docs.aws.amazon.com/kendra/latest/dg/index-document-types.html). You can also use inclusion and exclusion filters to index content by file name, file type, and file path.

You can connect Amazon Kendra to your Google Drive data source using the [Amazon Kendra console](https://console.aws.amazon.com/kendra/), the [TemplateConfiguration](https://docs.aws.amazon.com/kendra/latest/APIReference/API_TemplateConfiguration.html) API, or the [GoogleDriveConfiguration](https://docs.aws.amazon.com/kendra/latest/APIReference/API_GoogleDriveConfiguration.html) API.

Amazon Kendra has two versions of the Google Drive connector. Supported features of each version include:

**Google Drive connector V1.0 / [GoogleDriveConfiguration](https://docs.aws.amazon.com/kendra/latest/APIReference/API_GoogleDriveConfiguration.html) API**
+ Field mappings
+ User access control
+ Inclusion/exclusion filters

**Google Drive connector V2.0 / [TemplateConfiguration](https://docs.aws.amazon.com/kendra/latest/APIReference/API_TemplateConfiguration.html) API**
+ Field mappings
+ User access control
+ Inclusion/exclusion filters
+ Full and incremental content syncs
+ Virtual private cloud (VPC)

**Note**  
Google Drive connector V1.0 / Google DriveConfiguration API ended in 2023. We recommend migrating to or using Google Drive connector V2.0 / TemplateConfiguration API.

For troubleshooting your Amazon Kendra Google Drive data source connector, see [Troubleshooting data sources](troubleshooting-data-sources.md).

**Topics**
+ [Google Drive connector V1.0](data-source-v1-google-drive.md)
+ [Google Drive connector V2.0](data-source-v2-google-drive.md)