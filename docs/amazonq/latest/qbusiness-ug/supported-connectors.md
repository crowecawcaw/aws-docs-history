

Amazon Q Business is no longer open to new customers. For capabilities similar to Q Business, explore Amazon Quick. [Learn more](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/qbusiness-availability-change.html).

# Connecting Amazon Q Business data source connectors
<a name="supported-connectors"></a>

**Note**  
Before you connect an Amazon Q Business data source to your application, you [must add an index and retriever](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/select-retriever.html) to it.

To connect a data source to your Amazon Q Business application environment, you can use the AWS Management Console or the [CreateDataSource](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_CreateDataSource.html) API operation. 

By using the `CreateDataSource` API operation, you can configure tags, sync run schedules, and configure Amazon VPC settings. Then, you can use the `configuration` parameter to provide all other configuration information specific to your data source connector.

**Note**  
This procedure is available if you chose to [add a new Amazon Q Business index](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/native-retriever.html) to your application environment.

This section contains an overview of data source connector features, recommended best practices for configuration, and configuration information specific to your data source connector.

**Topics**
+ [Data source connector concepts](connector-concepts.md)
+ [What is a document?](connector-doc-crawl.md)
+ [Best practices for data source connector configuration in Amazon Q Business](connector-best-practices.md)
+ [Supported connectors](connectors-list.md)
+ [Understanding Amazon Q Business User Store](connector-principal-store.md)
+ [Using Amazon VPC with Amazon Q Business connectors](connector-vpc.md)