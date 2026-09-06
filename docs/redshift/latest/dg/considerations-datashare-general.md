

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# General considerations for data sharing in Amazon Redshift
<a name="considerations-datashare-general"></a>

The following are general considerations when working with datashares in Amazon Redshift:
+ *Default database* – When you read data from a datashare, you remain connected to your local cluster database. For more information about setting up and reading from a database created from a datashare, see [Querying datashare objects](https://docs.aws.amazon.com/redshift/latest/mgmt/query-editor-v2-datashare-using.html#query-editor-v2-datashare-consumer) and [Materialized views on external data lake tables in Amazon Redshift Spectrum](materialized-view-external-table.md).
+ *Connections* – You must be connected directly to a datashare database or run the USE command to write to datashares. You can also use three-part notation. The USE command is not supported on external tables. 
+ *Performance* – The performance of the queries on shared data depends on the compute capacity of the consumer clusters.
+ *Data transfer charges* – Cross-Region data sharing includes additional cross-Region data-transfer charges. 
  + These data-transfer charges don't apply within the same Region, only across Regions. For more information, see [Managing cost control for cross-Region data sharing](cross-region-billing.md). 
  + The consumer is charged for all compute and cross-region data transfer fees required to query the producer's data. The producer is charged for the underlying storage of data in their provisioned cluster or serverless namespace.
+ *Data sharing within and between clusters* – You only need datashares when you are sharing data between different Amazon Redshift provisioned clusters or serverless workgroups. Within the same cluster, you can query another database using simple three-part notation `database.schema.table` as long as you have the required permissions on the objects in the other database.
+ *Metadata Discovery* – When you're a consumer connected directly to a datashare database through the Redshift JDBC, ODBC, or Python drivers, you can view catalog data in the following ways: 
  + SQL [SHOW](https://docs.aws.amazon.com/redshift/latest/dg/r_SHOW.html) commands.
  + Querying information\_schema tables and views.
  + Querying [SVV metadata views](https://docs.aws.amazon.com/redshift/latest/dg/svv_views.html).
+ *Permissions visibility* – Consumers can see the permissions granted to the datashares through the SHOW GRANTS SQL command.
+ *Cluster encryption management for data sharing* – To share data across an AWS account, both the producer and consumer cluster must be encrypted. 
  + If both the producer and consumer clusters and serverless namespaces are in the same account, they must have the same encryption type (either both unencrypted, or both encrypted). In every other case, including Lake Formation managed datashares, both the consumer and producer must be encrypted. This is for security purposes. However, they don't need to share the same encryption key.
  + To protect data in transit, all data is encrypted in transit through the encryption schema of the producer cluster. The consumer cluster adopts this encryption schema when data is loaded. The consumer cluster then operates as a normal encrypted cluster. Communications between the producer and consumer are also encrypted using a shared key schema. For more information about encryption in transit, [Encryption in transit](https://docs.aws.amazon.com/redshift/latest/mgmt/security-encryption-in-transit.html).