# Add an AWS Region to a keyspace in Amazon Keyspaces

You can add a new AWS Region to a keyspace that is either a single or a multi-Region keyspace.
The new replica Region is applied to all tables in the keyspace.

To change a single-Region to a multi-Region keyspace, you have to enable client-side timestamps
for all tables in the keyspace. For more information, see
[Client-side timestamps in Amazon Keyspaces](client-side-timestamps.md "client-side-timestamps.md").

If you're adding an additional Region to a multi-Region keyspace, Amazon Keyspaces has to
replicate the existing table(s) into the new Region using a one-time cross-Region
restore for each existing table. The restore charges for each table are billed per GB,
for more information see [Backup and restore](https://aws.amazon.com/keyspaces/pricing/#:~:text=per%20GB-month-,Restoring%20a%20table,-Restoring%20a%20table "https://aws.amazon.com/keyspaces/pricing/#:~:text=per%20GB-month-,Restoring%20a%20table,-Restoring%20a%20table") on the Amazon Keyspaces (for Apache Cassandra) pricing page. There's no charge for
data transfer across Regions for this restore operation. In addition to data, all table
properties with the exception of tags are going to be replicated to the new
Region.

You can use the `ALTER KEYSPACE` statement in CQL, the `update-keyspace` command with the AWS CLI, or
the console to add a new Region to a single or to a multi-Region keyspace in Amazon Keyspaces.
In order to run the statement successfully, the account you're using has to be located in one of the Regions where the keyspace is already
available. While the replica is being added, you can't perform any other data definition language (DDL) operations on the resources that are
being updated and replicated.

For more information about the permissions required to add a Region, see [Configure the IAM permissions required to
add an AWS Region to a keyspace](howitworks_replication_permissions_addReplica.md "howitworks_replication_permissions_addReplica.md").

###### Note

When adding an additional Region to a single-Region keyspace, Amazon Keyspaces creates a service-linked role
with the name `AWSServiceRoleForAmazonKeyspacesReplication` in
your account. This role allows Amazon Keyspaces to replicate tables to new Regions and to replicate writes from one table
to all replicas of a multi-Region table on your behalf. To learn more, see [Using roles for Amazon Keyspaces Multi-Region Replication](using-service-linked-roles-multi-region-replication.md "using-service-linked-roles-multi-region-replication.md").

Console
Follow these steps to add a Region to a keyspace using the Amazon Keyspaces
console.

###### Add a Region to a keyspace (console)

1. Sign in to the AWS Management Console, and open the Amazon Keyspaces console at [https://console.aws.amazon.com/keyspaces/home](https://console.aws.amazon.com/keyspaces/home "https://console.aws.amazon.com/keyspaces/home").
2. In the navigation pane, choose **Keyspaces**, and then choose
   a keyspace from the list.
3. Choose the **AWS Regions** tab.
4. On the **AWS Regions** tab, choose **Add Region**.
5. In the **Add Region** dialog, choose the additional Region that you want to add to the keyspace.
6. To finish, choose **Add**.

Cassandra Query Language (CQL)

###### Add a Region to a keyspace using CQL

- To add a new Region to a keyspace, you can use the following statement. In this example,
  the keyspace is already available in the US East (N. Virginia) Region and US West (Oregon) Region Regions, and the CQL statement is
  adding the Region US West (N. California) Region.

```
ALTER KEYSPACE `my_keyspace`
WITH REPLICATION = {
    'class': 'NetworkTopologyStrategy',
    'us-east-1': '3',
    'us-west-2': '3',
    'us-west-1': '3'
} AND CLIENT_SIDE_TIMESTAMPS = {'status': 'ENABLED'};
```

CLI

###### Add a Region to a keyspace using the AWS CLI

- To add a new Region to a keyspace using the CLI, you can use the following example.
  Note that the default value for `client-side-timestamps` is `DISABLED`.
  With the `update-keyspace` command, you must change the value to `ENABLED`.

```
aws keyspaces update-keyspace \
--keyspace-name `my_keyspace` \
--replication-specification '{"replicationStrategy": "MULTI_REGION", "regionList": ["us-east-1", "eu-west-1", "eu-west-3"] }' \
--client-side-timestamps '{"status": "ENABLED"}'
```
