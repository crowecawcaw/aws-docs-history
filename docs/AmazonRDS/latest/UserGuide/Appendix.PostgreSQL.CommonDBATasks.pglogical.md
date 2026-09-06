

# Using pglogical to synchronize data across instances
<a name="Appendix.PostgreSQL.CommonDBATasks.pglogical"></a>

All currently available RDS for PostgreSQL versions support the `pglogical` extension. The pglogical extension predates the functionally similar logical replication feature that was introduced by PostgreSQL in version 10. For more information, see [Performing logical replication for Amazon RDS for PostgreSQL](PostgreSQL.Concepts.General.FeatureSupport.LogicalReplication.md).

The `pglogical` extension supports logical replication between two or more RDS for PostgreSQL DB instances. It also supports replication between different PostgreSQL versions, and between databases running on RDS for PostgreSQL DB instances and Aurora PostgreSQL DB clusters. The `pglogical` extension uses a publish-subscribe model to replicate changes to tables and other objects, such as sequences, from a publisher to a subscriber. It relies on a replication slot to ensure that changes are synchronized from a publisher node to a subscriber node, defined as follows. 
+ The *publisher node* is the RDS for PostgreSQL DB instance that's the source of data to be replicated to other nodes. The publisher node defines the tables to be replicated in a publication set. 
+ The *subscriber node* is the RDS for PostgreSQL DB instance that receives WAL updates from the publisher. The subscriber creates a subscription to connect to the publisher and get the decoded WAL data. When the subscriber creates the subscription, the replication slot is created on the publisher node. 

Following, you can find information about setting up the `pglogical` extension. 

**Topics**
+ [Requirements and limitations for the pglogical extension](#Appendix.PostgreSQL.CommonDBATasks.pglogical.requirements-limitations)
+ [Setting up the pglogical extension](Appendix.PostgreSQL.CommonDBATasks.pglogical.basic-setup.md)
+ [Setting up logical replication for RDS for PostgreSQL DB instance](Appendix.PostgreSQL.CommonDBATasks.pglogical.setup-replication.md)
+ [Reestablishing logical replication after a major upgrade](Appendix.PostgreSQL.CommonDBATasks.pglogical.recover-replication-after-upgrade.md)
+ [Managing logical replication slots for RDS for PostgreSQL](Appendix.PostgreSQL.CommonDBATasks.pglogical.handle-slots.md)
+ [Parameter reference for the pglogical extension](Appendix.PostgreSQL.CommonDBATasks.pglogical.reference.md)

## Requirements and limitations for the pglogical extension
<a name="Appendix.PostgreSQL.CommonDBATasks.pglogical.requirements-limitations"></a>

All currently available releases of RDS for PostgreSQL support the `pglogical` extension. 

Both the publisher node and the subscriber node must be set up for logical replication.

The tables that you want to replicate from a publisher to a subscriber must have the same names and the same schema. These tables must also contain the same columns, and the columns must use the same data types. Both publisher and subscriber tables must have the same primary keys. We recommend that you use only the PRIMARY KEY as the unique constraint.

The tables on the subscriber node can have more permissive constraints than those on the publisher node for CHECK constraints and NOT NULL constraints. 

The `pglogical` extension provides features such as two-way replication that aren't supported by the logical replication feature built into PostgreSQL (version 10 and higher). For more information, see [PostgreSQL bi-directional replication using pglogical](https://aws.amazon.com/blogs/database/postgresql-bi-directional-replication-using-pglogical/).