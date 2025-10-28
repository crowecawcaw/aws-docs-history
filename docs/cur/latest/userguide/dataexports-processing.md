# Processing data exports

In the following sections, you'll find information about processing your data
exports.

## Configuring Amazon Athena

Unlike Cost and Usage Reports (CUR), Data Exports doesn't offer an SQL file for setting up Athena to query
your exports. You'll need to either use a CloudFormation template for Data Exports (see option 1) or
manually configure Athena (see option 2).

**(Option 1) Use a CloudFormation template:** To locate the
CloudFormation template and instructions for setting up Athena with Data Exports, refer to [Data Exports in the Cloud Intelligence
Dashboards Framework](https://catalog.workshops.aws/awscid/en-US/data-exports "https://catalog.workshops.aws/awscid/en-US/data-exports").

**(Option 2) Use an AWS Glue crawler to build your table and
partitions for Athena:** When creating CUR or carbon emissions data exports for
Athena, we suggest using the Apache Parquet file format; it offers better compression and
column-oriented storage which contributes to smaller and less expensive Athena queries. The
overwrite delivery preference is required so that each monthly partition always contains only
one copy of each file and no duplicate line items appear when you execute queries with Amazon
Athena.

We also recommend using AWS Glue with a Glue crawler to load your data into
Athena.

###### To build a table and partitions for Athena using an AWS Glue crawler

1. Create an export of CUR 2.0 or Carbon emissions with the following data export
   delivery options:
   - Compression type and file format: Parquet - Parquet
   - File versioning: Overwrite existing data export file

2. In Athena, use the notebook editor with Trino SQL and choose
   **Create** to create a table with "AWS Glue crawler". Using the Glue
   crawler workflow, point the Glue crawler to run on the
   s3://<bucket-name>/<prefix>/<export-name>/data folder to automatically load all
   of the delivered partitions for the specified export to Athena.
3. After the Glue crawler is complete, you can use Athena to write queries on the table
   created by the Glue crawler.

## Configuring Amazon Redshift

Amazon Redshift is a cloud data warehouse that can be accessed either in a provisioned
capacity or serverless model. Amazon Redshift offers fast query performance for processing
your data from Data Exports.

Currently, Data Exports doesn't provide the SQL file for setting up Redshift to query your exports
like Cost and Usage Reports (CUR) does. However, you can still manually set up Redshift to
query your exports. We recommend that you use the gzip/csv compression and file format for
Redshift.

For information on setting up Redshift, see the _[Amazon Redshift
Getting Started Guide](../../../redshift/latest/gsg/new-user-serverless.md "../../../redshift/latest/gsg/new-user-serverless.md")_.

## Recommended SQL queries for processing

CUR 2.0

After loading your CUR 2.0 export data into a data analytics tool such as Amazon Athena or
Amazon Redshift, you can process it in order to gain cost and usage insights. AWS
Well-Architected Labs provides a CUR query library that you can use to process CUR. For more
information, see [AWS CUR Query Library](https://wellarchitectedlabs.com/cost-optimization/cur_queries/ "https://wellarchitectedlabs.com/cost-optimization/cur_queries/").

Note the following two pieces of information about SQL queries:

- The Well-Architected Labs SQL queries won't work in the data export query field,
  because Data Exports doesn't support aggregations and some of the other SQL syntax used in these
  queries.
- The Well-Architected Labs SQL queries will only work if you haven’t renamed your
  columns from the default names. Depending on the query, you may need to query some of the
  product columns as separate columns using the dot operator. For more information, see
  [Data
  query–SQL query and table configurations](dataexports-data-query.md "dataexports-data-query.md").

## Recommended SQL queries for processing carbon

emissions data exports

To get the total carbon emissions per payer_account_id:

```
SELECT payer_account_id, SUM(total_mbm_emissions_value) AS total_emissions
FROM "ccft-data-exports"."ccft-data-exports-data" -- change to your table name
GROUP BY payer_account_id
ORDER BY total_emissions DESC;

```

To get the total carbon emissions per payer_account_id and per product_code:

```
SELECT payer_account_id, product_code, SUM(total_mbm_emissions_value) AS total_emissions
FROM "ccft-data-exports"."ccft-data-exports-data"-- change to your table name
GROUP BY payer_account_id, product_code
ORDER BY total_emissions DESC;
```

To get the total carbon emissions per payer_account_id and per region_code:

```
SELECT payer_account_id, region_code, SUM(total_mbm_emissions_value) AS total_emissions
FROM "ccft-data-exports"."ccft-data-exports-data" -- change to your table name
GROUP BY payer_account_id, region_code
ORDER BY total_emissions DESC;
```
