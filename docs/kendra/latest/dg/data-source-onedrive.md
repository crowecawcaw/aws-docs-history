

Amazon Kendra is no longer open to new customers. For capabilities similar to Amazon Kendra, explore Amazon Bedrock Knowledge Bases. [Learn more](https://docs.aws.amazon.com/kendra/latest/dg/kendra-availability-change.html).

# Microsoft OneDrive
<a name="data-source-onedrive"></a>

Microsoft OneDrive is cloud-based storage service that you can use to store, share, and host your content. You can use Amazon Kendra to index your OneDrive data source.

You can connect Amazon Kendra to your OneDrive data source using the [Amazon Kendra console](https://console.aws.amazon.com/kendra/) and the [OneDriveConfiguration](https://docs.aws.amazon.com/kendra/latest/APIReference/API_OneDriveConfiguration.html) API.

Amazon Kendra has two versions of the OneDrive connector. Supported features of each version include:

**Microsoft OneDrive connector V1.0 / [OneDriveConfiguration](https://docs.aws.amazon.com/kendra/latest/APIReference/API_OneDriveConfiguration.html) API**
+ Field mappings
+ Inclusion/exclusion filters

**Microsoft OneDrive connector V2.0 / [TemplateConfiguration](https://docs.aws.amazon.com/kendra/latest/APIReference/API_TemplateConfiguration.html) API**
+ User context filtering
+ User identity crawler
+ Inclusion/exclusion filters
+ Full and incremental content syncs
+ Virtual private cloud (VPC)

**Note**  
Support for OneDrive connector V1.0 / OneDriveConfiguration API is scheduled to end by June 2023. We recommend using OneDrive connector V2.0 / TemplateConfiguration API.

For troubleshooting your Amazon Kendra OneDrive data source connector, see [Troubleshooting data sources](troubleshooting-data-sources.md).

**Topics**
+ [Microsoft OneDrive connector V1.0](data-source-v1-onedrive.md)
+ [Microsoft OneDrive connector V2.0](data-source-v2-onedrive.md)
+ [Learn more](#onedrive-learn-more)
+ [Notes](#onedrive-notes)

## Learn more
<a name="onedrive-learn-more"></a>

To learn more about integrating Amazon Kendra with your OneDrive data source, see:
+ [Announcing the updated Microsoft OneDrive connector (V2) for Amazon Kendra](https://aws.amazon.com/blogs/machine-learning/announcing-the-updated-microsoft-onedrive-connector-v2-for-amazon-kendra/).

## Notes
<a name="onedrive-notes"></a>
+ When Access Control Lists (ACLs) are enabled, the "Sync only new or modified content" option is not available due to OneDrive API limitations. We recommend using "Full sync" or "New, modified, or deleted content sync" modes instead, or disable ACLs if you need to use this sync mode.