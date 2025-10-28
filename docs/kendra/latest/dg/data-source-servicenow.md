# ServiceNow

ServiceNow provides a cloud-based service management system to create and manage
organization-level workflows, such as IT services, ticketing systems, and support. You can use
Amazon Kendra to index your ServiceNow catalogs, knowledge articles, incidents, and
their attachments.

You can connect Amazon Kendra to your ServiceNow data source using either the
[Amazon Kendra console](https://console.aws.amazon.com/kendra/ "https://console.aws.amazon.com/kendra/"), the [TemplateConfiguration](../APIReference/API_TemplateConfiguration.md "../APIReference/API_TemplateConfiguration.md") API, or the [ServiceNowConfiguration](../APIReference/API_ServiceNowConfiguration.md "../APIReference/API_ServiceNowConfiguration.md") API.

Amazon Kendra has two versions of the ServiceNow connector. Supported features
of each version include:

**ServiceNow connector V1.0 / [ServiceNowConfiguration](../APIReference/API_ServiceNowConfiguration.md "../APIReference/API_ServiceNowConfiguration.md") API**

- Field mappings
- ServiceNow instance versions: London, Others
- Inclusion/exclusion filters
  **ServiceNow connector V2.0 / [TemplateConfiguration](../APIReference/API_TemplateConfiguration.md "../APIReference/API_TemplateConfiguration.md")
  API**

- Field mappings
- User access control
- Inclusion/exclusion filters
- Full and incremental content syncs
- ServiceNow instance versions: Rome, Sandiego, Tokyo, Others
- Virtual private cloud (VPC)

###### Note

ServiceNow connector V1.0 / ServiceNowConfiguration API ended in 2023. We recommend
migrating to or using ServiceNow connector V2.0 / TemplateConfiguration API.

For troubleshooting your Amazon Kendra ServiceNow data source connector, see [Troubleshooting data sources](troubleshooting-data-sources.md "troubleshooting-data-sources.md").

###### Topics

- [ServiceNow connector V1.0](data-source-v1-servicenow.md "data-source-v1-servicenow.md")
- [ServiceNow connector V2.0](data-source-v2-servicenow.md "data-source-v2-servicenow.md")
- [Specifying documents to index with a query](servicenow-query.md "servicenow-query.md")
