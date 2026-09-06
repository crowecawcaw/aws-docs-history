

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see [Amazon CloudWatch Dashboard documentation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.html). 

# How Systems Manager handles cloud resources
<a name="cloud-connector-identifiers"></a>

By enabling Multicloud Integrations for AWS Systems Manager, virtual machine identifiers from other cloud providers are stored in Systems Manager and other AWS services as needed. This metadata relates to the management of corresponding resources collected from other cloud providers. Such identifiers do not constitute Your Content. We recommend you do not include sensitive, confidential, or personally identifiable information in them.

By enabling Multicloud Integrations, the following identifiers from your connected cloud environment are stored and used by AWS to provide multicloud security capabilities:
+ **Resource identifiers**: Azure Tenant ID, Subscription ID, Location (region), Resource ID (Resource Group IDs or Names)