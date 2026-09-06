

# Querying HealthOmics analytics data
<a name="analytics-query-data"></a>

**Important**  
AWS HealthOmics variant stores and annotation stores are no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [AWS HealthOmics variant store and annotation store availability change](variant-store-availability-change.md).

You can perform queries on your variant stores using AWS Lake Formation and Amazon Athena or Amazon EMR. Before you run any queries, complete the setup procedures (described in the following sections) for Lake Formation and Amazon Athena.

For information about Amazon EMR, see [ Tutorial: Getting started with Amazon EMR](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-gs.html)

For variant stores created after Sept 26, 2024, HealthOmics partitions the store by sample ID. This partitioning means that HealthOmics uses the sample ID to optimize storing of the variant information. Queries that use sample information as filters will return results faster, as the query scans less data. 

HealthOmics uses sample IDs as partition file names. Before you ingest data, check whether the sample ID contains any PHI data. If it does, change the sample ID before you ingest the data. For more information about what content to include and not include in sample IDs, see guidance on the AWS [ HIPAA compliance](https://aws.amazon.com/compliance/hipaa-compliance) web page.

**Topics**
+ [Configuring Lake Formation to use HealthOmics](setting-up-lf.md)
+ [Configuring Athena for queries](analytics-setting-up-athena.md)
+ [Running queries on HealthOmics variant stores](analytics-run-queries.md)