

# Limitations
<a name="zero-etl-limitations"></a>

The following are general limitations of or considerations about zero-ETL integrations:
+ Resource properties have a one-to-one relationship with the corresponding resource. Consequently, all integrations created using that resource must adhere to the singular resource property. Modifying a resource property will therefore impact all integrations associated with that resource.
+ Table properties have a one-to-one relationship with the corresponding table or object within a resource. As a result, all integrations that process the same table to or from the same resource must adhere to the singular table property.
+ You cannot rename a column at the source. If a column is renamed then there is no guarantee that the schema detection will be accurately done by AWS Glue and the repercussions on the integration are undefined.
+ The following consideration applies to how the integration works with AWS Lake Formation managed tables: By default, you use the IAM/AWS Glue policy to manage your table and databases.
+ If you want to use AWS Lake Formation to manage the table creation in that database, you need to make sure that the role is given sufficient Lake Formation permissions to create, modify and delete the table and database.
+ The zero-ETL summary page does not contain any metrics at this time.

The following are source-specific limitations of zero-ETL integrations:
+ Zero-ETL integrations with an SAP OData source now supports entities starting with `EntityOf`. The ability to override the primary key is currently supported only for SAPOData `EntityOf` objects. Once this property has been set, it cannot be modified.
+ Zero-ETL integrations from Amazon DynamoDB to Amazon SageMaker Lakehouse (via S3) support a maximum DynamoDB table size of 100TB.
+ The source DynamoDB table must be encrypted with either an Amazon-owned or customer-managed AWS KMS key. Amazon managed encryption is not supported for the source DynamoDB table.
+ SAP OData works using a delta token, where the combination of an OAuth client plus an entity, or basic authentication plus an entity, can have only a single delta token. Avoid using the same entity in two different integrations with the same client.
+ The following Salesforce entities or fields are unsupported for use in a zero-ETL integration with a Salesforce source. See [Unsupported entities and fields for Salesforce](zero-etl-sources.md#zero-etl-config-source-salesforce-unsupported).
+ For zero-ETL integrations with a Salesforce source, the integration does not detect when a record is archived. Archived records remain in your target dataset without being removed or updated.
+ The following ServiceNow entities or fields are unsupported for use in a zero-ETL integration with a ServiceNow source. See [Unsupported entities and fields for ServiceNow](zero-etl-sources.md#zero-etl-config-source-servicenow-unsupported).

The following are target-specific limitations of zero-ETL integrations:
+ Due to limitation in Data Catalog, AWS Glue Zero ETL can only support replication of tables with table names smaller than 255 characters.
+ Due to limitation in Athena, the source column/nested field name should not contain special characters ":", which will cause the target table schema metadata showing up incorrectly. In such cases, AWS Glue Zero ETL will move the integration to FAILED state.
+ Due to limitation in Iceberg, AWS Glue Zero ETL target can only support replication of 1000 columns per table. If chosen table in any integration has more than 1000 columns, AWS Glue Zero ETL will move the integration to FAILED state.
+ Due to limitation in Data Catalog, AWS Glue Zero ETL can only support replicating table of schema size 10 MB. If chosen table in any integration has schema size larger than 10 MB, AWS Glue Zero ETL will move the integration to FAILED state.