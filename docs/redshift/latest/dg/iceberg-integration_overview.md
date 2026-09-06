

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# Apache Iceberg compatibility for Amazon Redshift
<a name="iceberg-integration_overview"></a>

You can register entire Amazon Redshift provisioned clusters or serverless namespaces to the AWS Glue Data Catalog to create catalogs that securely share live data across AWS accounts. You can access these catalogs from any SQL query engine that supports the Apache Iceberg REST API. AWS Lake Formation manages the permissions for the catalogs, letting you manage a single copy of data with a single set of permissions while leveraging Amazon Redshift features such as materialized views and zero-ETL integrations. 

All catalogs created from registered Amazon Redshift provisioned clusters and serverless namespaces in the AWS Glue Data Catalog are automatically mounted as external databases on all provisioned clusters and serverless workgroups in the same AWS Region under the same account. Catalogs created in the AWS Glue Data Catalog to store data in Redshift Managed Storage (RMS) are similarly mounted as external databases. After the databases are mounted, you can directly connect to these databases and query the objects using the three-part notation `database@namespace-catalog.schema.table`.

## Regions where Apache Iceberg compatibility is available
<a name="iceberg-integration-regions"></a>

Apache Iceberg compatibility with Amazon Redshift is available in the following AWS Regions:
+  US East (N. Virginia) 
+  US East (Ohio) 
+  US West (N. California) 
+  Asia Pacific (Hong Kong) 
+  Asia Pacific (Seoul); 
+  Asia Pacific (Singapore) 
+  Asia Pacific (Sydney) 
+  Asia Pacific (Tokyo) 
+  Canada (Central) 
+  Europe (Frankfurt) 
+  Europe (Ireland) 
+  Europe (London) 
+  Europe (Stockholm) 
+  South America (São Paulo) 

## Considerations and limitations when using Amazon Redshift catalogs in the AWS Glue Data Catalog
<a name="iceberg-integration-considerations"></a>

When using Amazon Redshift catalogs in the AWS Glue Data Catalog, consider the following:
+  Data warehouses registered to the AWS Glue Data Catalog follow the three-part syntax for accessing tables (`database@namespace-catalog.schema.table`). For example, if you registered an Amazon Redshift namespace named a, populated by a database named b, which held a schema named c, in which was a table named d, you would select from d using the following statement: 

  ```
  SELECT * FROM b@a.c.d;
  ```

  Note that the combined length of the `database@namespace-catalog` part of the syntax must be 127 characters or less.
+  When you register a cluster or namespace to the AWS Glue Data Catalog, Amazon Redshift registers all databases and relations in that cluster or namespace. 
+  You can register multiple Redshift clusters and namespaces to the AWS Glue Data Catalog. 
+  Registering a cluster or namespace only registers the internal schemas and relations in that cluster or namespace. The following aren’t registered: 
  +  External schemas. 
  +  External tables. Note that late-binding views created from external tables will be registered. 
  +  User-created functions. 
  +  Procedures. 
  +  Tables with row-level security or dynamic data masking policies attached. 
  +  Database objects with uppercase or mixed-case names. Tables containing uppercase or mixed-case columns aren’t registered. This applies even when [enable\_case\_sensitive\_identifier](r_enable_case_sensitive_identifier.md) is disabled. 
+  Amazon Redshift database permissions, such as roles granted by role-based access control, don’t transfer to catalogs in the AWS Glue Data Catalog. Use AWS Lake Formation to configure permissions for the AWS Glue Data Catalog. For more information on using Lake Formation to configure permissions, see [ Setting up permissions for Amazon Redshift datashares](https://docs.aws.amazon.com/lake-formation/latest/dg/setup-ds-perms.html) in the *AWS Lake Formation Developer Guide*.
+  When you create a catalog from a registered cluster or serverless namespace, the AWS Glue Data Catalog creates an Amazon Redshift managed workgroup using Amazon Redshift compute resources to handle compute requirements when querying that catalog. You can view the managed workgroup in the Amazon Redshift Serverless console and manage it in AWS Glue. 
+  When you register a paused cluster, the AWS Glue Data Catalog won’t mount that cluster as a catalog until the cluster is resumed. 
+  When you register a serverless namespace that’s not being actively used, the AWS Glue Data Catalog won’t mount that namespace as a catalog until the namespace is used again. 
+  To access tables in data warehouses registered to the AWS Glue Data Catalog, the database’s isolation level must be SNAPSHOT. Attempting to access tables with an isolation level of SERIALIZABLE will result in an error. For more information on serializable isolation, see [Isolation levels in Amazon Redshift](c_serial_isolation.md). For information on changing the isolation level of a database, see [ALTER DATABASE](r_ALTER_DATABASE.md). 

   Note that the isolation level of the default `dev` database can’t be altered. Consequently, this means that tables in the `dev` database won’t be included in the accessible data when registering data warehouses to the AWS Glue Data Catalog.