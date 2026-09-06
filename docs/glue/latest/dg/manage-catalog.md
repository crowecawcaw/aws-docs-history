

# Managing the Data Catalog
<a name="manage-catalog"></a>

 The AWS Glue Data Catalog is a central metadata repository that stores structural and operational metadata for your Amazon S3 data sets. Managing the Data Catalog effectively is crucial for maintaining data quality, performance, security, and governance.

 By understanding and applying these Data Catalog management practices, you can ensure your metadata remains accurate, performant, secure, and well-governed as your data landscape evolves. 

This section covers the following aspects of Data Catalog management:
+ *Updating table schema and partitions*   As your data evolves, you may need to update the table schema or partition structure defined in the Data Catalog. For more information on how to make these updates programmatically using the AWS Glue ETL, see [Updating the schema, and adding new partitions in the Data Catalog using AWS Glue ETL jobs](update-from-job.md).
+ *Managing column statistics*: Accurate column statistics help optimize query plans and improve performance. For more information on how to generate, update, and manage column statistics, see [Optimizing query performance using column statistics](column-statistics.md). 
+  *Encrypting the Data Catalog*   To protect sensitive metadata, you can encrypt your Data Catalog using AWS Key Management Service (AWS KMS). This section explains how to enable and manage encryption for your Data Catalog. 
+ *Securing the Data Catalog with AWS Lake Formation*   Lake Formation provides a comprehensive approach to data lake security and access control. You can use Lake Formation to secure and govern access to your Data Catalog and underlying data. 

**Topics**
+ [Updating the schema, and adding new partitions in the Data Catalog using AWS Glue ETL jobs](update-from-job.md)
+ [Optimizing query performance using column statistics](column-statistics.md)
+ [Encrypting your Data Catalog](catalog-encryption.md)
+ [Securing your Data Catalog using Lake Formation](secure-catalog.md)
+ [Working with AWS Glue Data Catalog views in AWS Glue](catalog-views.md)
+ [Export metadata to S3 Tables (preview)](catalog-export-s3-tables.md)