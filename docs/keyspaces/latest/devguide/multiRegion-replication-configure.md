# Configure multi-Region replication for Amazon Keyspaces (for Apache Cassandra)

You can use the console, Cassandra Query Language (CQL), or the AWS Command Line Interface to create and manage multi-Region keyspaces and
tables in Amazon Keyspaces.

This section provides examples of how to create and manage multi-Region keyspaces and tables.
All tables that you create in a multi-Region keyspace automatically inherit the multi-Region
settings from the keyspace.

For more information about supported configurations and features, see [Amazon Keyspaces multi-Region replication usage notes](multiRegion-replication_usage-notes.md "multiRegion-replication_usage-notes.md").

###### Topics

- [Configure the IAM permissions required to
  create multi-Region keyspaces and tables](howitworks_replication_permissions.md "howitworks_replication_permissions.md")
- [Configure the IAM permissions required to
  add an AWS Region to a keyspace](howitworks_replication_permissions_addReplica.md "howitworks_replication_permissions_addReplica.md")
- [Create a multi-Region keyspace in Amazon Keyspaces](keyspaces-mrr-create.md "keyspaces-mrr-create.md")
- [Add an AWS Region to a keyspace in Amazon Keyspaces](keyspaces-multi-region-add-replica.md "keyspaces-multi-region-add-replica.md")
- [Check the replication progress when adding a new Region to a keyspace](keyspaces-multi-region-replica-status.md "keyspaces-multi-region-replica-status.md")
- [Create a multi-Region table with default settings in Amazon Keyspaces](tables-mrr-create-default.md "tables-mrr-create-default.md")
- [Create a multi-Region table in provisioned mode with auto scaling in Amazon Keyspaces](tables-mrr-create-provisioned.md "tables-mrr-create-provisioned.md")
- [Update the provisioned capacity and auto scaling settings for a multi-Region table in Amazon Keyspaces](tables-mrr-autoscaling.md "tables-mrr-autoscaling.md")
- [View the provisioned capacity and auto scaling settings for a multi-Region table in Amazon Keyspaces](tables-mrr-view.md "tables-mrr-view.md")
- [Turn off auto scaling for a table in Amazon Keyspaces](tables-mrr-autoscaling-off.md "tables-mrr-autoscaling-off.md")
- [Set the provisioned capacity of a multi-Region table manually in Amazon Keyspaces](tables-mrr-capacity-manually.md "tables-mrr-capacity-manually.md")
