# Connecting a client machine to an Amazon RDS for Db2 DB instance

To use any of the native Db2 tools to move data from a Db2 database to an Amazon RDS for Db2
database, you must first connect your client machine to an RDS for Db2 DB instance.

The client machine can be any of the following:

- An Amazon Elastic Compute Cloud (Amazon EC2) instance on Linux, Windows,
  or macOS. This instance should be in the same virtual private
  cloud (VPC) as your RDS for Db2 DB instance, AWS Cloud9, or AWS CloudShell.
- A self-managed Db2 instance in an Amazon EC2 instance. The instances should be in
  the same VPC.
- A self-managed Db2 instance in an Amazon EC2 instance. The instances can be in
  different VPCs if you enabled VPC peering. For more information, see [Create a VPC
  peering connection](../../../vpc/latest/peering/create-vpc-peering-connection.md "../../../vpc/latest/peering/create-vpc-peering-connection.md") in the _Amazon Virtual Private Cloud VPC Peering
  Guide_.
- A local machine running Linux, Windows, or
  macOS in a self-managed environment. You must either have
  public connectivity to RDS for Db2 or enable VPN connectivity between self-managed
  Db2 instances and AWS.
  To connect your client machine to your RDS for Db2 DB instance, log in to your client
  machine with IBM Db2 Data Management Console. For more information, see [Creating an Amazon RDS DB instance](USER_CreateDBInstance.md "USER_CreateDBInstance.md") and [IBM Db2 Data Management Console](db2-connecting-with-ibm-data-management-console.md "db2-connecting-with-ibm-data-management-console.md").

You can use AWS Database Migration Service (AWS DMS) to run queries against the database, run an SQL
execution plan, and monitor the database. For more information, see [What is AWS Database
Migration Service?](../../../dms/latest/userguide/Welcome.md "../../../dms/latest/userguide/Welcome.md") in the _AWS Database Migration Service User Guide_.

After you successfully connect your client machine to your RDS for Db2 DB instance, you
are ready to use any native Db2 tool to copy data. For more information, see [Using native Db2 tools to migrate data from Db2 to Amazon RDS for Db2](db2-native-db2-tools.md "db2-native-db2-tools.md").
