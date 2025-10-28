# Salesforce

Salesforce is a customer relationship management (CRM) tool for managing support,
sales, and marketing teams. You can use Amazon Kendra to index your Salesforce
standard objects and even custom objects.

You can connect Amazon Kendra to your Salesforce data source using either the
[Amazon Kendra console](https://console.aws.amazon.com/kendra/ "https://console.aws.amazon.com/kendra/"), the [TemplateConfiguration](../APIReference/API_TemplateConfiguration.md "../APIReference/API_TemplateConfiguration.md") API, or the [SalesforceConfiguration](../APIReference/API_SalesforceConfiguration.md "../APIReference/API_SalesforceConfiguration.md") API.

Amazon Kendra has two versions of the Salesforce connector. Supported features
of each version include:

**Salesforce connector V1.0 / [SalesforceConfiguration](../APIReference/API_SalesforceConfiguration.md "../APIReference/API_SalesforceConfiguration.md") API**

- Field mappings
- User access control
- Inclusion/exclusion filters
  **Salesforce connector V2.0 / [TemplateConfiguration](../APIReference/API_TemplateConfiguration.md "../APIReference/API_TemplateConfiguration.md")
  API**

- Field mappings
- User access control
- Inclusion/exclusion filters
- Full and incremental content syncs
- Virtual private cloud (VPC)

###### Note

Salesforce connector V1.0 / SalesforceConfiguration API ended in 2023. We recommend
migrating to or using Salesforce connector V2.0 / TemplateConfiguration API.

For troubleshooting your Amazon Kendra Salesforce data source connector, see [Troubleshooting data sources](troubleshooting-data-sources.md "troubleshooting-data-sources.md").

###### Topics

- [Salesforce connector V1.0](data-source-v1-salesforce.md "data-source-v1-salesforce.md")
- [Salesforce connector V2.0](data-source-v2-salesforce.md "data-source-v2-salesforce.md")
