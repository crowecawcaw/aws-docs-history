# Google Drive

Google Drive is a cloud-based file storage service. You can use Amazon Kendra
to index documents stored in shared drives, My Drives, and Shared with me folders in your
Google Drive data source. You can index both Google Workspace documents as well as
documents listed in [Types of documentation](index-document-types.md "index-document-types.md"). You can
also use inclusion and exclusion filters to index content by file name, file type, and file
path.

You can connect Amazon Kendra to your Google Drive data source using the [Amazon Kendra console](https://console.aws.amazon.com/kendra/ "https://console.aws.amazon.com/kendra/"), the [TemplateConfiguration](../APIReference/API_TemplateConfiguration.md "../APIReference/API_TemplateConfiguration.md") API, or the [GoogleDriveConfiguration](../APIReference/API_GoogleDriveConfiguration.md "../APIReference/API_GoogleDriveConfiguration.md") API.

Amazon Kendra has two versions of the Google Drive connector. Supported
features of each version include:

**Google Drive connector V1.0 / [GoogleDriveConfiguration](../APIReference/API_GoogleDriveConfiguration.md "../APIReference/API_GoogleDriveConfiguration.md") API**

- Field mappings
- User access control
- Inclusion/exclusion filters
  **Google Drive connector V2.0 / [TemplateConfiguration](../APIReference/API_TemplateConfiguration.md "../APIReference/API_TemplateConfiguration.md") API**

- Field mappings
- User access control
- Inclusion/exclusion filters
- Full and incremental content syncs
- Virtual private cloud (VPC)

###### Note

Google Drive connector V1.0 / Google DriveConfiguration API ended in 2023. We recommend
migrating to or using Google Drive connector V2.0 / TemplateConfiguration API.

For troubleshooting your Amazon Kendra Google Drive data source connector, see [Troubleshooting data sources](troubleshooting-data-sources.md "troubleshooting-data-sources.md").

###### Topics

- [Google Drive connector
  V1.0](data-source-v1-google-drive.md "data-source-v1-google-drive.md")
- [Google Drive connector V2.0](data-source-v2-google-drive.md "data-source-v2-google-drive.md")
