

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# Amazon Redshift Spectrum overview
<a name="c-spectrum-overview"></a>

This topic describes details for using Redshift Spectrum to efficiently read from Amazon S3.

**Note**  
Amazon Redshift DC2 and RA3 instances use Redshift Spectrum to run data lake queries on a dedicated server fleet outside of the cluster. Amazon Redshift RG instances and Amazon Redshift Serverless include an integrated data lake query engine that runs on the cluster's own compute resources. For information, see [Querying your data lake](https://docs.aws.amazon.com/redshift/latest/gsg/data-lake.html).

Amazon Redshift Spectrum resides on dedicated Amazon Redshift servers that are independent of your cluster. Amazon Redshift pushes many compute-intensive tasks, such as predicate filtering and aggregation, down to the Redshift Spectrum layer. Thus, Redshift Spectrum queries use much less of your cluster's processing capacity than other queries. Redshift Spectrum also scales intelligently. Based on the demands of your queries, Redshift Spectrum can potentially use thousands of instances to take advantage of massively parallel processing.

You create Redshift Spectrum tables by defining the structure for your files and registering them as tables in an external data catalog. The external data catalog can be AWS Glue, the data catalog that comes with Amazon Athena, or your own Apache Hive metastore. You can create and manage external tables either from Amazon Redshift using data definition language (DDL) commands or using any other tool that connects to the external data catalog. Changes to the external data catalog are immediately available to any of your Amazon Redshift clusters. 

Optionally, you can partition the external tables on one or more columns. Defining partitions as part of the external table can improve performance. The improvement occurs because the Amazon Redshift query optimizer eliminates partitions that don't contain data for the query. 

Materialized views on Spectrum tables can greatly improve cost and performance. For more information, see [Materialized views on external data lake tables in Amazon Redshift Spectrum](materialized-view-external-table.md). 

After your Redshift Spectrum tables have been defined, you can query and join the tables just as you do any other Amazon Redshift table. Redshift Spectrum doesn't support update operations on external tables. You can add Redshift Spectrum tables to multiple Amazon Redshift clusters and query the same data on Amazon S3 from any cluster in the same AWS Region. When you update Amazon S3 data files, the data is immediately available for query from any of your Amazon Redshift clusters. 

The AWS Glue Data Catalog that you access might be encrypted to increase security. If the AWS Glue catalog is encrypted, you need the AWS Key Management Service (AWS KMS) key for AWS Glue to access the AWS Glue catalog. AWS Glue catalog encryption is not available in all AWS Regions. For a list of supported AWS Regions, see [Encryption and Secure Access for AWS Glue](https://docs.aws.amazon.com/glue/latest/dg/encryption-glue-resources.html) in the *[AWS Glue Developer Guide](https://docs.aws.amazon.com/glue/latest/dg/). *For more information about AWS Glue Data Catalog encryption, see [Encrypting Your AWS Glue Data Catalog](https://docs.aws.amazon.com/glue/latest/dg/encrypt-glue-data-catalog.html) in the *[AWS Glue Developer Guide](https://docs.aws.amazon.com/glue/latest/dg/). * 

**Note**  
You can't view details for Redshift Spectrum tables using the same resources that you use for standard Amazon Redshift tables, such as [PG\_TABLE\_DEF](r_PG_TABLE_DEF.md), [STV\_TBL\_PERM](r_STV_TBL_PERM.md), PG\_CLASS, or information\_schema. If your business intelligence or analytics tool doesn't recognize Redshift Spectrum external tables, configure your application to query [SVV\_EXTERNAL\_TABLES](r_SVV_EXTERNAL_TABLES.md) and [SVV\_EXTERNAL\_COLUMNS](r_SVV_EXTERNAL_COLUMNS.md).

## Amazon Redshift Spectrum Regions
<a name="c-spectrum-regions"></a>

Redshift Spectrum is available in AWS Regions where Amazon Redshift is available, unless otherwise specified in Region specific documentation. For AWS Region availability in commercial Regions, see [Service endpoints](https://docs.aws.amazon.com/general/latest/gr/redshift-service.html#redshift_region) for the **Redshift API** in the *Amazon Web Services General Reference*. 