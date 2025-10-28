# User-defined types (UDTs) in Amazon Keyspaces

A user-defined type (UDT) is a grouping of fields and data types that you can use to
define a single column in Amazon Keyspaces. Valid data types for UDTs are all supported Cassandra
data types, including collections and other UDTs that you've already created in the same
keyspace. For more information about supported Cassandra data types, see [Cassandra data type support](cassandra-apis.md#cassandra-data-type "cassandra-apis.md#cassandra-data-type").

You can use user-defined types (UDTs) in Amazon Keyspaces to organize data in a more efficient way.
For example, you can create UDTs with nested collections which allows you to implement more complex
data modeling in your applications. You can also use the frozen keyword for
defining UDTs.

UDTs are bound to a keyspace and available to all tables and UDTs in the same keyspace.
You can create UDTs in single-Region and multi-Region keyspaces.

You can create new tables or alter existing tables and add new columns that use a UDT.
To create a UDT with a nested UDT, the nested UDT has to be frozen.

To review how many UDTs are supported per keyspace, supported levels of nesting,
and other default values and quotas related to UDTs, see [Quotas and default values for user-defined types (UDTs) in Amazon Keyspaces](quotas.md#quotas-udts "quotas.md#quotas-udts").

For information about how to calculate the encoded size of UDTs, see [Estimate the encoded size of
data values based on data type](calculating-row-size.md#calculating-row-size-data-types "calculating-row-size.md#calculating-row-size-data-types").

For more information about CQL syntax, see [User-defined types (UDTs)](cql.ddl.md "cql.ddl.md").

To learn more about UDTs and point-in time restore, see [PITR restore of tables with user-defined types (UDTs)](PointInTimeRecovery_HowItWorks.md#howitworks_backup_udt "PointInTimeRecovery_HowItWorks.md#howitworks_backup_udt").

###### Topics

- [Configure permissions](configure-udt-permissions.md "configure-udt-permissions.md")
- [Create a UDT](keyspaces-create-udt.md "keyspaces-create-udt.md")
- [View UDTs](keyspaces-view-udt.md "keyspaces-view-udt.md")
- [Delete a UDT](keyspaces-delete-udt.md "keyspaces-delete-udt.md")
