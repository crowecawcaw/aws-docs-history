

# Creating Data Catalog views using AWS Glue APIs
<a name="views-api-usage"></a>

You can use AWS Glue [CreateTable](https://docs.aws.amazon.com/glue/latest/webapi/API_CreateTable.html), and [UpdateTable](https://docs.aws.amazon.com/glue/latest/webapi/API_UpdateTable.html) APIs to create and update views in the Data Catalog. The `CreateTable` and `UpdateTable` operations have a new `TableInput` structure for `ViewDefinition`, while `SearchTables`, `GetTable`, `GetTables`, `GetTableVersion`, `GetTableVersions` operations provide the `ViewDefinition` in their output syntax for views. Additionally, there is a new `Status` field in the `GetTable` API output. 

Two new AWS Glue connections are available for validating the SQL dialect for each supported query engine, Amazon Athena and Amazon Redshift.

The `CreateTable` and `UpdateTable` APIs are asynchronous when used with views. When these APIs are called with multiple SQL dialects, the call are validated with each engine to determine whether the dialect can be run on that engine, and if the resulting schema of the view from each dialect matches. The AWS Glue service uses these connections to make internal calls to the analytical engines. These calls simulates what the engine does to validate if a `CREATE VIEW` or `ALTER VIEW` SQL DDL were executed on the engine.

If the SQL provided is valid, and the schemas match between view dialects, the AWS Glue API atomically commits the result. Atomicity allows views with multiple dialects to be created or altered without any downtime. 

**Topics**
+ [Creating AWS Glue connections to validate status](views-api-usage-connection.md)
+ [Validating the view generation status](views-api-usage-get-table.md)
+ [Asynchronous states and operations](views-api-usage-async-states.md)
+ [View creation failure scenarios during asynchronous operations](views-api-usage-errors.md)