

# Working with other AWS services
<a name="working-with-services"></a>

 AWS services such as Amazon Athena, AWS Glue, Amazon Redshift Spectrum, and Amazon EMR can use AWS Lake Formation to securely access data in Amazon S3 locations registered with Lake Formation. With Lake Formation, you can define and manage fine-grained access control (FGAC) permissions for your tables in the AWS Glue Data Catalog. Each of these AWS services is a trusted caller to Lake Formation, and Lake Formation provides access to data stored in Amazon S3 through temporary credentials. For more information, see [How Lake Formation application integration works](how-vending-works.md).

To avail these capabilities, Lake Formation requires you to first register the Amazon S3 location, and assign appropriate permissions to the IAM principal for accessing the table, the database, and the Amazon S3 location. For more information see, [Managing Lake Formation permissions](managing-permissions.md).

The following tables lists the types of Lake Formation permissions supported by Amazon Athena, AWS Glue, Amazon EMR, and Amazon Redshift Spectrum to access data from AWS Glue standard tables and transactional tables ([Apache Iceberg](https://iceberg.apache.org/), [Apache Hudi](https://hudi.incubator.apache.org/), and [Linux foundation Delta Lake](https://delta.io/)) with data stored in Amazon S3 and table metadata in the Data Catalog .


**AWS services and supported permission types for AWS Glue standard tables and views**  

| AWS service | Table-level permissions | Column-level permissions | Row and cell-level permissions | 
| --- | --- | --- | --- | 
| [Athena SQL](https://docs.aws.amazon.com/lake-formation/latest/dg/athena-lf.html) | Read/write access | Read access | Read access | 
| Athena Spark | Not supported | Not supported | Not supported | 
| [Redshift Spectrum](https://docs.aws.amazon.com/lake-formation/latest/dg/RSPC-lf.html) on a provisioned cluster or Amazon Redshift serverless | Read/write access | Read access | Read access | 
| [Apache Spark on Amazon EMR (EC2)](https://docs.aws.amazon.com/lake-formation/latest/dg/emr-integ-lf.html) | Read/write access | Read access | Read access | 
| [Apache Hive on Amazon EMR (EC2)](https://docs.aws.amazon.com/lake-formation/latest/dg/emr-integ-lf.html) | Read/write access | Read access | Not supported | 
| [Apache Spark on EMR Serverless](https://docs.aws.amazon.com/lake-formation/latest/dg/emr-integ-lf.html) | Read/write access | Read access | Read access | 
| Apache Hive on EMR Serverless | Not supported | Not supported | Not supported | 
| Amazon EMR on EKS | Not supported | Not supported | Not supported | 
| [AWS Glue ETL](https://docs.aws.amazon.com/lake-formation/latest/dg/glue-features-lf.html) | Read/write access | AWS Glue 5.0 or higher supports read access. | AWS Glue 5.0 or higher supports read access. | 

**Considerations and limitations**
+ Athena Spark doesn't support querying Data Catalog tables with Lake Formation permissions.
+ Athena SAML-based users can read data sources secured using Lake Formation permissions by enabling SAML 2.0-based federation. SAML users can insert data into Parquet tables.
+ Apache Spark on EMR Serverless doesn't support querying Data Catalog views.
+ Apache Hive on EMR Serverless doesn't support querying tables with Lake Formation permissions.
+ AWS Glue 5.0 or higher supports fine-grained access controls on Iceberg and Hive tables in the Data Catalog that are backed by S3. This capability lets you configure table, row, column, and cell level access controls for read queries within your AWS Glue for Apache Spark jobs.

  For more information, see [AWS Glue versions](https://docs.aws.amazon.com/glue/latest/dg/release-notes.html).


**AWS services and supported permission types for transactional table formats**  

| AWS service | Iceberg | Hudi | Delta Lake (native) | Delta Lake (symlink tables) | 
| --- | --- | --- | --- | --- | 
| [Athena SQL](https://docs.aws.amazon.com/lake-formation/latest/dg/athena-lf.html) | Supports reading tables with table, column, row, and cell-level permissions. Write operations require full table access. | Supports read and create operations on tables with table, column, row, and cell-level permissions. Write operations are not supported. | Athena (engine version 3) supports reading native Delta Lake tables with table, column, row, and cell-level permissions. Write operations are not supported. | Athena (engine version 3) supports reading symlink Delta Lake tables with table, column, row, and cell-level permissions. Write operations are not supported. | 
| [Redshift Spectrum](https://docs.aws.amazon.com/lake-formation/latest/dg/RSPC-lf.html) on a provisioned cluster | Supports reading tables with table, column, row, and cell-level permissions. Write operations are not supported. | Supports reading tables with table, column, row, and cell-level permissions. Write operations are not supported. | No supported | Supports reading Delta Lake tables via symlink manifest with table, column, row, and cell-level permissions. Write operations are not supported. | 
| [Apache Spark on Amazon EMR (EC2)](https://docs.aws.amazon.com/lake-formation/latest/dg/emr-integ-lf.html) | Supports reading tables with table, column, row, and cell-level permissions. Write operations require full table access. | Supports reading tables with table, column, row, and cell-level permissions. Write operations require full table access. | Supports reading tables with table, column, row, and cell-level permissions. Write operations are not supported. | Supports reading tables with table, column, row, and cell-level permissions. Write operations require full table access. | 
| [AWS Glue ETL](https://docs.aws.amazon.com/lake-formation/latest/dg/glue-features-lf.html) | AWS Glue 5.0 or higher supports reading tables with table, column, row, and cell-level permissions. | Supports read/write on tables with table-level permissions. | Supports read/write on tables with table-level permissions. | Supports read/write on tables with table-level permissions. | 

**Topics**
+ [Using AWS Lake Formation with Amazon Athena](athena-lf.md)
+ [Using AWS Lake Formation with Amazon Redshift Spectrum](RSPC-lf.md)
+ [Using AWS Lake Formation with AWS Glue](glue-features-lf.md)
+ [Using AWS Lake Formation with Amazon EMR](emr-integ-lf.md)
+ [Using AWS Lake Formation with Quick](qs-integ-lf.md)
+ [Using AWS Lake Formation with AWS CloudTrail Lake](cloudtrail-lake-integ-lf.md)