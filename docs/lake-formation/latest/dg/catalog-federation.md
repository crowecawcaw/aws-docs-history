

# Catalog federation to remote Iceberg catalogs
<a name="catalog-federation"></a>

Catalog federation in AWS Glue provides direct and secure access to Iceberg tables, stored in Amazon S3 and cataloged in remote catalogs, using AWS analytics engines. Catalog federation synchronizes metadata across Data Catalog and remote catalogs when you access remote tables. It is supported by a wide variety of analytics engines, including Amazon Redshift, Amazon EMR, Amazon Athena, AWS Glue, third-party engines like Apache Spark, and more.

Catalog federation uses AWS Glue Data Catalog to discover Iceberg tables in external catalogs and Lake Formation to authorize data access. When you query a federated table, Data Catalog discovers the latest table information in the remote catalog at query time, getting the table's Amazon S3 location, current schema, and partition information. Your analytics engine (Amazon Athena, Amazon Redshift, Amazon EMR) then uses this information to access Iceberg data files directly from Amazon S3. Lake Formation manages access to table(s) by vending scoped credentials to the table data stored in Amazon S3, allowing the engines to apply fine-grained permissions to federated table(s). Depending on how you configure the federated catalog, these credentials come either from Lake Formation, which uses an IAM role you register, or from the remote catalog itself. AWS analytics engines enforce Lake Formation permissions to federated tables. For more information, see [Access delegation modes](#access-delegation-modes).

## Features of catalog federation
<a name="catalog-federation-features"></a>

**Governed using Lake Formation**  
Federated Iceberg catalogs in Data Catalog are Lake Formation registered resources. You can grant fine-grained row-level, column-level, and cell-level permissions to Iceberg tables in federated Iceberg catalogs by using Lake Formation grants. You can securely share federated Iceberg catalogs and associated objects across AWS accounts. Federated Iceberg catalogs also work with Lake Formation Tag-based access control, so you can scale governance by using tags.

**Networking configurations**  
Catalog federation supports direct connections to remote catalog sources by using standard HTTPS connectivity. It also supports connectivity through Amazon VPC when you want to maintain network isolation. In addition, it supports proxy connections when you want secure communication through organization firewalls.

### Access delegation modes
<a name="access-delegation-modes"></a>

AWS Glue supports two access delegation modes when you connect Data Catalog to external Iceberg catalogs: Registered role and Vended credentials. The mode determines which catalog issues the temporary security credentials to Amazon S3 prefix that engines use to read Iceberg data files. You choose the mode when you create the integration.

In vended-credential mode, the external catalog's grants still apply. If you revoke access in the external catalog, queries from an AWS analytics engine fail the next time the engine loads the table, with no change needed in AWS. All Lake Formation fine-grained permissions (row, column, and cell level, and Lake Formation-Tag–based access) still apply on top of the coarse-grained table grants in the external catalog. The external catalog sets how long the vended Amazon S3 credentials last. AWS Glue refreshes them during long-running queries, so queries don't fail when the original credentials expire.


**Access delegation modes**  

| Property | Registered role (aws-vended) | Vended credential (source-vended) | 
| --- | --- | --- | 
| Who issues Amazon S3 credentials | Lake Formation, by assuming the IAM role you register | The remote catalog, through its Iceberg REST loadTable response | 
| IAM role needs Amazon S3 access to table data | Yes | No | 
| Who controls data access scope | Lake Formation permissions and your IAM role | Lake Formation permissions and the remote catalog's grants | 
| Typical use | You own or can grant access to the Amazon S3 buckets that hold the remote tables | The remote catalog service owns the storage, or you don't want AWS roles to read it directly | 
| Connection property CREDENTIAL\_VENDING\_MODE | AWS\_VENDED (default) | SOURCE\_VENDED | 

## Limitations
<a name="catalog-federation-limitations"></a>
+  **Iceberg table metadata size limit** – For federated Iceberg catalogs, AWS Glue Data Catalog supports a maximum metadata size of 5 MB per REST API call. AWS Glue Data Catalog rejects requests to tables with metadata exceeding this limit. 

**Topics**
+ [Features of catalog federation](#catalog-federation-features)
+ [Limitations](#catalog-federation-limitations)
+ [Federate to Snowflake Iceberg Catalog](catalog-federation-snowflake.md)
+ [Federate to Databricks Unity Catalog](catalog-federation-databricks.md)