# Create a data source connection

To use an Athena data source connector, you create the AWS Glue connection that stores the
connection information about the connector and your data source. When you create the
connection, you give the data source a name that you will use to reference your data source
in your SQL queries.

You can create and configure a data source connection in Athena by using the [console](connect-to-a-data-source-console-steps.md "connect-to-a-data-source-console-steps.md") or the [CreateDataCatalog
API](../APIReference/API_CreateDataCatalog.md "../APIReference/API_CreateDataCatalog.md") operations.

###### Topics

- [Permissions to create and use a data source in Athena](connect-to-a-data-source-permissions.md "connect-to-a-data-source-permissions.md")
- [Use the Athena console to connect to a data source](connect-to-a-data-source-console-steps.md "connect-to-a-data-source-console-steps.md")
- [Use the AWS Serverless Application Repository to deploy a data source connector](connect-data-source-serverless-app-repo.md "connect-data-source-serverless-app-repo.md")
- [Create a VPC for a data source connector or AWS Glue connection](athena-connectors-vpc-creation.md "athena-connectors-vpc-creation.md")
- [Pull ECR images to your AWS account](pull-ecr-customer-account.md "pull-ecr-customer-account.md")
- [Register your connection as a Glue Data Catalog](register-connection-as-gdc.md "register-connection-as-gdc.md")
- [Enable cross-account federated queries](xacct-fed-query-enable.md "xacct-fed-query-enable.md")
- [Update a data source connector](connectors-updating.md "connectors-updating.md")
