

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# Querying your data lake
<a name="data-lake"></a>

You can use Amazon Redshift to query data in Amazon S3 without having to load the data into Amazon Redshift tables. Amazon Redshift provides SQL capability designed for fast online analytical processing (OLAP) of very large datasets that are stored in both Amazon Redshift clusters and Amazon S3 data lakes. You can query data in many formats, including [Iceberg](https://docs.aws.amazon.com/redshift/latest/dg/querying-iceberg.html), Parquet, ORC, RCFile, TextFile, SequenceFile, RegexSerde, OpenCSV, and AVRO. To define the structure of the files in Amazon S3, you create external schemas and tables. Then, you use an external data catalog such as AWS Glue or your own Apache Hive metastore. Changes to either type of data catalog are immediately available to any of your Amazon Redshift clusters.

After your data is registered with an AWS Glue Data Catalog and enabled with AWS Lake Formation, you can start querying your data lake.

You can partition the external tables on one or more columns to optimize query performance through partition elimination. You can query and join the external tables with Amazon Redshift tables. You can access external tables from multiple Amazon Redshift clusters and query the Amazon S3 data from any cluster in the same AWS Region. When you update Amazon S3 data files, the data is immediately available for queries from any of your Amazon Redshift clusters. 

**Using the integrated data lake query engine for RG and Redshift Serverless**

Amazon Redshift RG clusters and Amazon Redshift Serverless include an integrated data lake query engine that runs on the cluster's own compute resources, providing a unified experience for both data lake and data warehouse use cases.

The integrated data lake query engine eliminates the requirement to use Redshift Spectrum and eliminates the associated Redshift Spectrum charges. The integrated data lake query engine also supports querying data in Amazon S3 buckets located in a different AWS Region. Cross-region queries incur additional data transfer charges. No additional configuration is required to enable the integrated data lake query engine as it is enabled by default.

**Note**  
In some cases, you may observe slower performance on RG compared to RA3 clusters running Redshift Spectrum, which scales independently using dedicated compute resources. If you observe slower query performance, consider adding more nodes or upgrading to larger RG instance sizes.

**Using Redshift Spectrum for DC2 and RA3**

On DC2 and RA3 provisioned clusters, Redshift Spectrum resides on dedicated Amazon Redshift servers that are independent of your cluster. Redshift Spectrum pushes many compute-intensive tasks, such as predicate filtering and aggregation, to the Redshift Spectrum layer. Redshift Spectrum also scales intelligently to take advantage of massively parallel processing.

For more information about Redshift Spectrum, including how to work with Redshift Spectrum and data lakes, see [Getting started with Amazon Redshift Spectrum](https://docs.aws.amazon.com/redshift/latest/dg/c-getting-started-using-spectrum.html) in *Amazon Redshift Database Developer Guide*.