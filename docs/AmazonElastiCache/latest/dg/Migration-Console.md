

# Performing online data migration using the Console
<a name="Migration-Console"></a>

You can use the AWS Management Console to migrate your data from a self-managed Valkey or Redis OSS source on Amazon EC2 to a node-based ElastiCache cluster.

**To perform online data migration using the console**

1. Sign in to the console and open the ElastiCache console at [https://console.aws.amazon.com/elasticache/](https://console.aws.amazon.com/elasticache/home/home).

1. Either create a new Valkey or Redis OSS cluster or choose an existing cluster. Make sure that your source and the cluster meet the requirements in [Preparing your source and target for migration](Migration-Prepare.md), and that the following is true:
   + The cluster is in **available** status.

1. Open the migration form in one of the following ways:
   + In the navigation pane, choose **Migrations**. Choose **Create migration**, and then choose **Migrate to node-based**. On the **Migrate data from endpoint** page, for **Target ElastiCache cluster name**, choose your cluster.
   + In the cluster list, select your cluster. For **Actions**, choose **Migrate data from endpoint**. The **Migrate data to {{cluster-name}}?** dialog box opens with your cluster as the target.

   Choosing **Start migration** on the cluster details page opens the same dialog box.

1. For **Source endpoint**, enter the IP address of your source Valkey or Redis OSS cluster. For **Source port**, enter the port where your source is available.
**Important**  
The IP address must be exact. If you enter the address incorrectly, the migration fails.

1. (Optional) To validate your setup without migrating any data, choose **Test migration**. For more information, see [Testing the data migration](Migration-Test.md).

1. 
**Important**  
When the migration starts, ElastiCache deletes all existing data in the target cluster and replaces it with data from your source.

   Choose **Start migration**.

   As the cluster begins migration, it changes to **Modifying** and then **Migrating** status.

1. Monitor the migration progress by choosing **Events** on the navigation pane.

At any point during the migration, you can stop it. In the cluster list, select your cluster. For **Actions**, choose **Stop data migration**. This option is available while the cluster is in **Migrating** status. In the **Stop data migration to {{cluster-name}}?** dialog box, choose **Stop data migration**.

Stopping the migration completes it, the same way as the `CompleteMigration` API operation. ElastiCache stops replicating from your source and promotes your ElastiCache cluster to primary. The data that already synced stays in the cluster, and writes that reach your source after that point aren't copied. If the data isn't in sync, the request can fail and the cluster stays in **Migrating** status. To stop without checking that the data is in sync, select **Force** under **Force migration stop**. For more information, see [Completing the data migration](Migration-Complete.md). The cluster then goes to **Available** status.