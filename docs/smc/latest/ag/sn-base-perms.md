# Setting baseline

permissions for AWS Service Management Connector for ServiceNow

This section describes how to configure Identity and Access Management (IAM)
permissions, AWS Service Catalog, and other AWS services to use AWS Service Management
Connector for ServiceNow.

To use an AWS CloudFormation template to set up the AWS configurations of the Connector for
ServiceNow, refer to the AWS configurations for Connector for ServiceNow
[AWS commercial Regions](https://servicecatalogconnector.s3.amazonaws.com/SM_ConnectorForServiceNow-AWS_Configurations_Commercialv5.0.0.json "https://servicecatalogconnector.s3.amazonaws.com/SM_ConnectorForServiceNow-AWS_Configurations_Commercialv5.0.0.json") , [AWS GovCloud Regions](https://servicecatalogconnector.s3.amazonaws.com/SM_ConnectorForServiceNow-AWS_Configurations_GovCloudv5.0.0.json "https://servicecatalogconnector.s3.amazonaws.com/SM_ConnectorForServiceNow-AWS_Configurations_GovCloudv5.0.0.json"), and [AWS China Regions](https://servicecatalogconnector.s3.amazonaws.com/SM_ConnectorForServiceNow-Amazon_Configurations_Chinav5.0.0.json "https://servicecatalogconnector.s3.amazonaws.com/SM_ConnectorForServiceNow-Amazon_Configurations_Chinav5.0.0.json").

###### Note

The AWS CloudFormation template creates IAM users with permissions to all existing integrations, and _is intended to
enable all supported integrations in a sandbox or developer ServiceNow instance_. For quality-assurance and production,
you must apply least-privilege permissions based on the integrations enabled through the connector.
Review the Creating users section for additional information.

###### Note

If you choose to use the Connector for ServiceNow AWS Configuration template, go to the
[AWS Service Catalog Administrator Guide](../../../servicecatalog/latest/adminguide/introduction.md "../../../servicecatalog/latest/adminguide/introduction.md") .
