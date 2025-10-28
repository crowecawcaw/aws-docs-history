# Using a hybrid migration solution: Apache Cassandra to Amazon Keyspaces

The following migration solution can be considered a hybrid between online and offline
migration. With this hybrid approach, data is written to the destination database in
near real time without providing read after write consistency. This means that newly written
data won’t be immediately available and delays are to be expected. If you need read after
write consistency, see [Online migration to Amazon Keyspaces: strategies and best practices](migrating-online.md "migrating-online.md").

For a near real time migration from Apache Cassandra to Amazon Keyspaces, you can choose between two available methods.

- **CQLReplicator** – (Recommended) CQLReplicator is an open source utility
  available on [Github](https://github.com/aws-samples/cql-replicator "https://github.com/aws-samples/cql-replicator") that helps you to migrate data from Apache Cassandra to Amazon Keyspaces in
  near real time.

To determine the writes and updates to propagate to the destination database, CQLReplicator
scans the Apache Cassandra token range and uses an AWS Glue job to remove duplicate events and apply writes and updates
directly to Amazon Keyspaces.

- **Change data capture (CDC)** – If you are familiar with
  Cassandra CDC, the Apache Cassandra built-in CDC feature that allows capturing
  changes by copying the commit log to a separate CDC directory is another option for
  implementing a hybrid migration.

You can do this by replicating the data changes to Amazon Keyspaces,
making CDC an alternative option for data migration scenarios.
If you don't need read after write consistency, you can use either the CQLReplicator or a CDC pipeline to migrate
data from Apache Cassandra to Amazon Keyspaces based on your preferences and familiarity with the tools and AWS services used in each
solution. Using these methods to migrate data in near real time can be considered
a hybrid approach to migration that offers an alternative to online migration.

This strategy is considered a hybrid approach, because in addition to the options outlined in this topic,
you have to implement some steps of the online migration progress, for example historical data
copy and the application migration strategies discussed in the [online migration](migrating-online.md "migrating-online.md") topic.

The following sections go over the hybrid migration options in more detail.

###### Topics

- [Migrate data using CQLReplicator](migration-hybrid-cql-rep.md "migration-hybrid-cql-rep.md")
- [Migrate data using change data capture (CDC)](migration-hybrid-cdc.md "migration-hybrid-cdc.md")
