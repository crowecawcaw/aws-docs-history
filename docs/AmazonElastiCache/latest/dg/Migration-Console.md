# Performing online data migration using the Console

You can use the AWS Management Console to migrate your data from your cluster to your Valkey or Redis OSS cluster.

###### To perform online data migration using the console

1. Sign in to the console and open the ElastiCache console at [https://console.aws.amazon.com/elasticache/](https://console.aws.amazon.com/elasticache/home/home "https://console.aws.amazon.com/elasticache/home/home").
2. Either create a new Valkey or Redis OSS cluster or choose an existing cluster. Make sure
   that the cluster meets the following requirements:
   - Your engine version should be Valkey 7.2 and higher, or Redis OSS 5.0.6 or higher.
   - Your cluster should not have AUTH enabled.
   - The config `protected-mode` should be set to
     `no`.
   - If you have `bind` configuration in your Valkey or Redis OSS config, then
     it should be updated to allow requests from ElastiCache nodes.
   - The number of databases should be the same between the ElastiCache node and
     your Valkey or Redis OSS cluster. This value is set using `databases` in
     the engine config.
   - Valkey or Redis OSS commands that perform data modification should not be renamed to
     allow replication of the data to succeed.
   - To replicate the data from your Valkey or Redis OSS cluster to ElastiCache, make sure that
     there is sufficient CPU and memory to handle this additional load. This
     load comes from the RDB file created by your Valkey or Redis OSS cluster and
     transferred over the network to ElastiCache node.
   - The cluster is in **available** status.

3. With your cluster selected, choose **Migrate Data from
   Endpoint** for **Actions**.
4. In the **Migrate Data from Endpoint** dialog box, enter the
   IP address, and the port where your Valkey or Redis OSS cluster is available.

###### Important

The IP address must be exact. If you enter the address incorrectly, the
migration fails. 5. Choose **Start Migration**.

As the cluster begins migration, it changes to **Modifying**
and then **Migrating** status. 6. Monitor the migration progress by choosing **Events** on the
navigation pane.
At any point during the migration process, you can stop migration. To do so, choose
your cluster and choose **Stop Data Migration** for
**Actions**. The cluster then goes to
**Available** status.

If the migration succeeds, the cluster goes to **Available** status
and the event log shows the following:

`Migration operation succeeded for replication group
 `ElastiCacheClusterName`.`

If the migration fails, the cluster goes to **Available** status and
the event log shows the following:

`Migration operation failed for replication group
 `ElastiCacheClusterName`.`
