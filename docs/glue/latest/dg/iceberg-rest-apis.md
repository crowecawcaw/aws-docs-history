

# AWS Glue REST APIs for Apache Iceberg specifications
<a name="iceberg-rest-apis"></a>

This section contains specifications about the AWS Glue Iceberg REST catalog and AWS Glue extension APIs, and considerations when using these APIs. 

API requests to the AWS Glue Data Catalog endpoints are authenticated using AWS Signature Version 4 (SigV4). See [AWS Signature Version 4 for API requests](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_sigv.html) section to learn more about AWS SigV4.

When accessing the AWS Glue service endpoint, and AWS Glue metadata, the application assumes an IAM role which requires `glue:getCatalog` IAM action. 

Access to the Data Catalog, and its objects can be managed using IAM, Lake Formation, or Lake Formation hybrid mode permissions.

Federated catalogs in the Data Catalog have Lake Formation registered data locations. Lake Formation works with the Data Catalog to provide database-style permissions to manage user access to Data Catalog objects. 

You can use IAM, AWS Lake Formation, or Lake Formation hybrid mode permissions to manage access to the default Data Catalog and its objects. 

To create, insert, or delete data in Lake Formation managed objects, you must set up specific permissions for the IAM user or role. 
+ CREATE\_CATALOG – Required to create catalogs 
+ CREATE\_DATABASE – Required to create databases
+ CREATE\_TABLE – Required to create tables
+ DELETE – Required to delete data from a table
+ DESCRIBE – Required to read metadata 
+ DROP – Required to drop/delete a table or database
+ INSERT – Needed when the principal needs to insert data into a table
+ SELECT – Needed when the principal needs to select data from a table

For more information, see [Lake Formation permissions reference](https://docs.aws.amazon.com/lake-formation/latest/dg/lf-permissions-reference.html) in the AWS Lake Formation Developer Guide.

## LoadNamespaceMetadata
<a name="load-ns-metadata"></a>


**General information**  

|  |  | 
| --- |--- |
| Operation name | LoadNamespaceMetadata | 
| Type | Iceberg REST Catalog API | 
| REST path | GET/iceberg/v1/catalogs/{catalog}/namespaces/{ns} | 
| IAM action | glue:GetDatabase | 
| Lake Formation permissions | ALL, DESCRIBE, SELECT | 
| CloudTrail event | glue:GetDatabase | 
| Open API definition | https://github.com/apache/iceberg/blob/apache-iceberg-1.6.1/open-api/rest-catalog-open-api.yaml\#L302 | 

****Considerations and limitations****
+ The catalog path parameter must follow the style described in the [Prefix and catalog path parameters](connect-glu-iceberg-rest.md#prefix-catalog-path-parameters) section.
+ You can specify only a single-level namespace in the REST path parameter. For more in formation, see the [Namespace path parameter](connect-glu-iceberg-rest.md#ns-path-param) section.

## UpdateNamespaceProperties
<a name="w2aac20c31c16c21c13"></a>


**General information**  

|  |  | 
| --- |--- |
| Operation name | UpdateNamespaceProperties | 
| Type | Iceberg REST Catalog API | 
| REST path | POST /iceberg/v1/catalogs/{catalog}/namespaces/{ns}/properties | 
| IAM action | glue:UpdateDatabase | 
| Lake Formation permissions | ALL, ALTER | 
| CloudTrail event | glue:UpdateDatabase | 
| Open API definition | https://github.com/apache/iceberg/blob/apache-iceberg-1.6.1/open-api/rest-catalog-open-api.yaml\#L400 | 

****Considerations and limitations****
+ The catalog path parameter must follow the style described in the [Prefix and catalog path parameters](connect-glu-iceberg-rest.md#prefix-catalog-path-parameters) section.
+ You can specify only a single-level namespace in the REST path parameter. For more in formation, see the [Namespace path parameter](connect-glu-iceberg-rest.md#ns-path-param) section.