# Microsoft SharePoint

SharePoint is a collaborative website building service that you can use to
customize web content and create pages, sites, document libraries, and lists. You can use
Amazon Kendra to index your SharePoint data source.

Amazon Kendra currently supports SharePoint Online and SharePoint
Server (versions 2013, 2016, 2019, and Subscription Edition).

You can connect Amazon Kendra to your SharePoint data source using either the
[Amazon Kendra console](https://console.aws.amazon.com/kendra/ "https://console.aws.amazon.com/kendra/"), the [TemplateConfiguration](../APIReference/API_TemplateConfiguration.md "../APIReference/API_TemplateConfiguration.md") API, or the [SharePointConfiguration](../APIReference/API_SharePointConfiguration.md "../APIReference/API_SharePointConfiguration.md") API.

Amazon Kendra has two versions of the SharePoint connector. Supported
features of each version include:

**SharePoint Connector V1.0 / [SharePointConfiguration](../APIReference/API_SharePointConfiguration.md "../APIReference/API_SharePointConfiguration.md") API**

- Field mappings
- User access control
- Inclusion/exclusion filters
- Change log
- Virtual private cloud (VPC)
  **SharePoint Connector V2.0 / [TemplateConfiguration](../APIReference/API_TemplateConfiguration.md "../APIReference/API_TemplateConfiguration.md") API**

- Field mappings
- User access control
- Inclusion/exclusion filters
- Full and incremental content syncs
- Virtual private cloud (VPC)

###### Note

SharePoint connector V1.0 / SharePointConfiguration API ended in 2023. We recommend
migrating to or using SharePoint connector V2.0 / TemplateConfiguration API.

For troubleshooting your Amazon Kendra SharePoint data source connector, see [Troubleshooting data sources](troubleshooting-data-sources.md "troubleshooting-data-sources.md").

###### Topics

- [SharePoint connector
  V1.0](data-source-v1-sharepoint.md "data-source-v1-sharepoint.md")
- [SharePoint connector
  V2.0](data-source-v2-sharepoint.md "data-source-v2-sharepoint.md")
