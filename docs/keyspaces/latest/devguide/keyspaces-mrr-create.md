# Create a multi-Region keyspace in Amazon Keyspaces

This section provides examples of how to create a multi-Region keyspace. You can
do this on the Amazon Keyspaces console, using CQL or the AWS CLI. All tables that you create in a
multi-Region keyspace automatically inherit the multi-Region settings from the keyspace.

###### Note

When creating a multi-Region keyspace, Amazon Keyspaces creates a service-linked role
with the name `AWSServiceRoleForAmazonKeyspacesReplication` in
your account. This role allows Amazon Keyspaces to replicate writes to all replicas of
a multi-Region table on your behalf. To learn more, see [Using roles for Amazon Keyspaces Multi-Region Replication](using-service-linked-roles-multi-region-replication.md "using-service-linked-roles-multi-region-replication.md").

Console

###### Create a multi-Region keyspace (console)

1. Sign in to the AWS Management Console, and open the Amazon Keyspaces console at [https://console.aws.amazon.com/keyspaces/home](https://console.aws.amazon.com/keyspaces/home "https://console.aws.amazon.com/keyspaces/home").
2. In the navigation pane, choose **Keyspaces**, and then choose
   **Create keyspace**.
3. For **Keyspace name**, enter the name for the
   keyspace.
4. In the **Multi-Region replication** section, you can add the additional Regions that are available in the list.
5. To finish, choose **Create keyspace**.

Cassandra Query Language (CQL)

###### Create a multi-Region keyspace using CQL

1. To create a multi-Region keyspace, use `NetworkTopologyStrategy` to specify
   the AWS Regions that the keyspace is going to be replicated in. You must include your
   current Region and at least one additional Region.

All tables in the keyspace inherit the replication strategy from the keyspace. You
can't change the replication strategy at the table level.

`NetworkTopologyStrategy` – The replication factor for each Region is
three because Amazon Keyspaces replicates data across three [Availability
Zones](https://aws.amazon.com/about-aws/global-infrastructure/regions_az/ "https://aws.amazon.com/about-aws/global-infrastructure/regions_az/") within the same AWS Region, by default.

The following CQL statement is an
example of this.

```
CREATE KEYSPACE `mykeyspace`
WITH REPLICATION = {'class':'NetworkTopologyStrategy', 'us-east-1':'3', 'ap-southeast-1':'3','eu-west-1':'3' };
```

2. You can use a CQL statement to query the `tables` table in the
   `system_multiregion_info` keyspace to programmatically list the Regions
   and the status of the multi-Region table that you specify. The following code is an
   example of this.

```
SELECT * from system_multiregion_info.tables WHERE keyspace_name = '`mykeyspace`' AND table_name = '`mytable`';
```

The output of the statement looks like the following:

```
 `keyspace_name | table_name | region | status
----------------+----------------+----------------+--------
 mykeyspace | mytable | us-east-1 | ACTIVE
 mykeyspace | mytable | ap-southeast-1 | ACTIVE
 mykeyspace | mytable | eu-west-1 | ACTIVE`
```

CLI

###### Create a new multi-Region keyspace using the AWS CLI

- To create a multi-Region keyspace, you can use the following CLI statement. Specify
  your current Region and at least one additional Region in the
  `regionList`.

```
aws keyspaces create-keyspace --keyspace-name `mykeyspace` \
--replication-specification replicationStrategy=MULTI_REGION,regionList=us-east-1,eu-west-1
```

To create a multi-Region table, see [Create a multi-Region table with default settings in Amazon Keyspaces](tables-mrr-create-default.md "tables-mrr-create-default.md") and
[Create a multi-Region table in provisioned mode with auto scaling in Amazon Keyspaces](tables-mrr-create-provisioned.md "tables-mrr-create-provisioned.md").
