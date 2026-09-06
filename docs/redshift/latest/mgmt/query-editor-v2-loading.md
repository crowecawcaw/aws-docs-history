

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# Loading data into a database
<a name="query-editor-v2-loading"></a>

You can use query editor v2 to load data into a database in an Amazon Redshift cluster or workgroup. This section covers how to load sample data, data from S3, and data from a local file setup and workflow.

## Sample data
<a name="query-editor-v2-loading-sample-data"></a>

The query editor v2 comes with sample data and notebooks available to be loaded into a sample database and corresponding schema. 

To load sample data, choose the ![External](http://docs.aws.amazon.com/redshift/latest/mgmt/images/external.png) icon associated with the sample data you want to load. The query editor v2 then loads the data into a schema in database `sample_data_dev` and creates a folder of saved notebooks. 

The following sample datasets are available.

**tickit**  
Most of the examples in the Amazon Redshift documentation use sample data called `tickit`. This data consists of seven tables: two fact tables and five dimensions. When you load this data, the schema `tickit` is updated with sample data. For more information about the `tickit` data, see [Sample database](https://docs.aws.amazon.com/redshift/latest/dg/c_sampledb.html) in the *Amazon Redshift Database Developer Guide*. 

**tpch**  
This data is used for a decision support benchmark. When you load this data, the schema `tpch` is updated with sample data. For more information about the `tpch` data, see [TPC-H](http://www.tpc.org/tpch/). 

**tpcds**  
This data is used for a decision support benchmark. When you load this data, the schema `tpcds` is updated with sample data. For more information about the `tpcds` data, see [TPC-DS](http://www.tpc.org/tpcds/). 