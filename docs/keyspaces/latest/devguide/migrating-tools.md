# How to select the right tool for bulk uploading or migrating data to Amazon Keyspaces

In this section you can review the different tools that you can use to bulk upload or
migrate data to Amazon Keyspaces, and learn how to select the correct tool based on your needs. In
addition, this section provides an overview and use cases for the available step-by-step
tutorials that demonstrate how to import data into Amazon Keyspaces.

To review the available strategies to migrate workloads from Apache Cassandra to Amazon Keyspaces,
see [Create a migration plan for migrating from Apache Cassandra to Amazon Keyspaces](migrating-cassandra.md "migrating-cassandra.md").

- **Migration tools**

      + With the [pricing calculator for Amazon Keyspaces (for Apache Cassandra)](https://aws-samples.github.io/sample-pricing-calculator-for-keyspaces/#cassandra "https://aws-samples.github.io/sample-pricing-calculator-for-keyspaces/#cassandra") available on Github, you can estimate your
       monthly costs for Amazon Keyspaces based on your existing Apache Cassandra workload. Enter metrics from
       your Cassandra nodetool status output and intended serverless configuration for Amazon Keyspaces to
       compare direct costs between the two solutions. Note that this calculator focuses only on the
       operational costs of Amazon Keyspaces compared to your existing Cassandra deployment. It doesn't include
       total cost of ownership (TCO) factors like infrastructure maintenance, operational overhead,
       or support costs for Cassandra.
      + **ZDM Dual Write Proxy for Amazon Keyspaces Migration** – ZDM Dual Write Proxy available on
       [Github](https://github.com/aws-samples/amazon-keyspaces-examples/blob/main/migration/online/zdm-proxy/README.md "https://github.com/aws-samples/amazon-keyspaces-examples/blob/main/migration/online/zdm-proxy/README.md")
       supports zero-downtime migration from Apache Cassandra to Amazon Keyspaces.
      + **CQLReplicator** – CQLReplicator is an open source utility
       available on [Github](https://github.com/aws-samples/cql-replicator "https://github.com/aws-samples/cql-replicator") that helps you to migrate data from Apache Cassandra to Amazon Keyspaces in
       near real time.


      For more information, see [Migrate data using CQLReplicator](migration-hybrid-cql-rep.md "migration-hybrid-cql-rep.md").
      + To learn more about how to use Amazon Managed Streaming for Apache Kafka to implement an [online migration](migrating-online.md "migrating-online.md") process with dual-writes, see [Guidance for continuous data migration from Apache Cassandra to
       Amazon Keyspaces](https://aws.amazon.com/solutions/guidance/continuous-data-migration-from-apache-cassandra-to-amazon-keyspaces/ "https://aws.amazon.com/solutions/guidance/continuous-data-migration-from-apache-cassandra-to-amazon-keyspaces/").
      + For large migrations, consider using an extract, transform, and load (ETL) tool. You can use
       AWS Glue to quickly and effectively perform data transformation migrations. For
       more information, see [Offline migration process: Apache Cassandra to Amazon Keyspaces](migrating-offline.md "migrating-offline.md").
      + To learn how to use the Apache Cassandra Spark connector to write data to Amazon Keyspaces, see [Tutorial: Integrate with Apache Spark to import or export data](spark-integrating.md "spark-integrating.md").
      + Get started quickly with loading data into Amazon Keyspaces by using the cqlsh `COPY FROM`
       command. cqlsh is included with Apache Cassandra and is best suited for loading
       small datasets or test data. For step-by-step instructions, see [Tutorial: Loading data into Amazon Keyspaces using cqlsh](bulk-upload.md "bulk-upload.md").
      + You can also use the DataStax Bulk Loader for Apache
       Cassandra to load data into Amazon Keyspaces using the `dsbulk` command. DSBulk
       provides more robust import capabilities than cqlsh and is available from the [GitHub repository](https://github.com/datastax/dsbulk "https://github.com/datastax/dsbulk"). For
       step-by-step instructions, see [Tutorial: Loading data into Amazon Keyspaces using DSBulk](dsbulk-upload.md "dsbulk-upload.md").

  General considerations for data uploads to Amazon Keyspaces

- **Break the data upload down into smaller components.**

Consider the following units of migration and their potential footprint in terms
of raw data size. Uploading smaller amounts of data in one or more phases may help
simplify your migration.

    + **By cluster** – Migrate all of your Cassandra
     data at once. This approach may be fine for smaller clusters.
    + **By keyspace or table** – Break up your
     migration into groups of keyspaces or tables. This approach can help you migrate data in
     phases based on your requirements for each workload.
    + **By data** – Consider migrating data for a
     specific group of users or products, to bring the size of data down even more.

- **Prioritize what data to upload first based on simplicity.**

Consider if you have data that could be migrated first more easily—for example, data
that does not change during specific times, data from nightly batch jobs, data not used
during offline hours, or data from internal apps.

###### Topics

- [Tutorial: Loading data into Amazon Keyspaces using cqlsh](bulk-upload.md "bulk-upload.md")
- [Tutorial: Loading data into Amazon Keyspaces using DSBulk](dsbulk-upload.md "dsbulk-upload.md")
