# Connecting Amazon Q Business data source connectors

###### Note

Before you connect an Amazon Q Business data source to your application, you [must add an index and retriever](select-retriever.md "select-retriever.md") to it.

To connect a data source to your Amazon Q Business application environment, you can use
the AWS Management Console or the [CreateDataSource](../api-reference/API_CreateDataSource.md "../api-reference/API_CreateDataSource.md") API operation.

By using the `CreateDataSource` API operation, you can configure tags, sync
run schedules, and configure Amazon VPC settings. Then, you can use the
`configuration` parameter to provide all other configuration information
specific to your data source connector.

###### Note

This procedure is available if you chose to [add
a new Amazon Q Business index](native-retriever.md "native-retriever.md") to your application environment.

This section contains an overview of data source connector features, recommended best
practices for configuration, and configuration information specific to your data source
connector.

###### Topics

- [Data source connector concepts](connector-concepts.md "connector-concepts.md")
- [What is a document?](connector-doc-crawl.md "connector-doc-crawl.md")
- [Best practices for data source connector configuration in Amazon Q Business](connector-best-practices.md "connector-best-practices.md")
- [Supported connectors](connectors-list.md "connectors-list.md")
- [Understanding Amazon Q Business User Store](connector-principal-store.md "connector-principal-store.md")
- [Using Amazon VPC with Amazon Q Business connectors](connector-vpc.md "connector-vpc.md")
