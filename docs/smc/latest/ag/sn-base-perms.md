

End of support notice: On March 31, 2027, AWS will end support for AWS Service Management Connector. After March 31, 2027, you will no longer be able to access the AWS Service Management Connector console or AWS Service Management Connector resources. For more information, see [AWS Service Management Connector end of support](https://docs.aws.amazon.com/smc/latest/ag/smc-end-of-support.html). 

# Setting baseline permissions for AWS Service Management Connector for ServiceNow
<a name="sn-base-perms"></a>

This section describes how to configure Identity and Access Management (IAM) permissions, AWS Service Catalog, and other AWS services to use AWS Service Management Connector for ServiceNow.

To use an CloudFormation template to set up the AWS configurations of the Connector for ServiceNow, refer to the AWS configurations for Connector for ServiceNow [AWS commercial Regions ](https://servicecatalogconnector.s3.amazonaws.com/SM_ConnectorForServiceNow-AWS_Configurations_Commercialv5.0.0.json), [AWS GovCloud Regions](https://servicecatalogconnector.s3.amazonaws.com/SM_ConnectorForServiceNow-AWS_Configurations_GovCloudv5.0.0.json), and [AWS China Regions](https://servicecatalogconnector.s3.amazonaws.com/SM_ConnectorForServiceNow-Amazon_Configurations_Chinav5.0.0.json). 

**Note**  
The CloudFormation template creates IAM users with permissions to all existing integrations, and *is intended to enable all supported integrations in a sandbox or developer ServiceNow instance*. For quality-assurance and production, you must apply least-privilege permissions based on the integrations enabled through the connector. Review the [Creating users]() section for additional information. 

**Note**  
If you choose to use the Connector for ServiceNow AWS Configuration template, go to the [AWS Service Catalog Administrator Guide ](https://docs.aws.amazon.com/servicecatalog/latest/adminguide/introduction.html). 