

Amazon Kendra is no longer open to new customers. For capabilities similar to Amazon Kendra, explore Amazon Bedrock Knowledge Bases. [Learn more](https://docs.aws.amazon.com/kendra/latest/dg/kendra-availability-change.html).

# Salesforce
<a name="data-source-salesforce"></a>

Salesforce is a customer relationship management (CRM) tool for managing support, sales, and marketing teams. You can use Amazon Kendra to index your Salesforce standard objects and even custom objects. 

You can connect Amazon Kendra to your Salesforce data source using either the [Amazon Kendra console](https://console.aws.amazon.com/kendra/), the [TemplateConfiguration](https://docs.aws.amazon.com/kendra/latest/APIReference/API_TemplateConfiguration.html) API, or the [SalesforceConfiguration](https://docs.aws.amazon.com/kendra/latest/APIReference/API_SalesforceConfiguration.html) API.

Amazon Kendra has two versions of the Salesforce connector. Supported features of each version include:

**Salesforce connector V1.0 / [SalesforceConfiguration](https://docs.aws.amazon.com/kendra/latest/APIReference/API_SalesforceConfiguration.html) API**
+ Field mappings
+ User access control
+ Inclusion/exclusion filters

**Salesforce connector V2.0 / [TemplateConfiguration](https://docs.aws.amazon.com/kendra/latest/APIReference/API_TemplateConfiguration.html) API**
+ Field mappings
+ User access control
+ Inclusion/exclusion filters
+ Full and incremental content syncs
+ Virtual private cloud (VPC)

**Note**  
Salesforce connector V1.0 / SalesforceConfiguration API ended in 2023. We recommend migrating to or using Salesforce connector V2.0 / TemplateConfiguration API.

For troubleshooting your Amazon Kendra Salesforce data source connector, see [Troubleshooting data sources](troubleshooting-data-sources.md).

**Topics**
+ [Salesforce connector V1.0](data-source-v1-salesforce.md)
+ [Salesforce connector V2.0](data-source-v2-salesforce.md)