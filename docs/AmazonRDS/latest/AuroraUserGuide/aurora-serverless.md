# Deleting an Aurora Serverless v1 DB cluster

###### Important

AWS has [announced the end-of-life date for Aurora Serverless v1: March 31st, 2025](https://repost.aws/questions/QUhcMVoChXRm2HLi8F-yih1g/announcement-support-for-aurora-s/announcement-support-for-aurora-serverless-v1-ending-soon "https://repost.aws/questions/QUhcMVoChXRm2HLi8F-yih1g/announcement-support-for-aurora-s/announcement-support-for-aurora-serverless-v1-ending-soon"). All Aurora Serverless v1 clusters that are
not migrated by March 31, 2025 will be migrated to Aurora Serverless v2 during the maintenance window. If the upgrade fails, Amazon Aurora converts the Serverless v1
cluster to a provisioned cluster with the equivalent engine version during the maintenance window. If applicable, Amazon Aurora will enroll the
converted provisioned cluster in Amazon RDS Extended Support. For more information, see [Amazon RDS Extended Support with Amazon Aurora](extended-support.md "extended-support.md").

Depending on how you create an Aurora Serverless v1 DB cluster, deletion protection might be turned on by default.
You can't immediately delete an Aurora Serverless v1 DB cluster that has **Deletion protection** enabled.
To delete Aurora Serverless v1 DB clusters that have deletion protection by using the AWS Management Console, you first
modify the cluster to remove this protection. For information about using the AWS CLI for this task, see
[AWS CLI](#aurora-serverless.delete.cli "#aurora-serverless.delete.cli").

###### To disable deletion protection using the AWS Management Console

1. Sign in to the AWS Management Console and open the Amazon RDS console at
   [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/ "https://console.aws.amazon.com/rds/").
2. In the navigation pane, choose **DB clusters**.
3. Choose your Aurora Serverless v1 DB cluster from the list.
4. Choose **Modify** to open your DB cluster's configuration. The Modify DB cluster
   page opens the Settings, Capacity settings, and other configuration details for your Aurora Serverless v1 DB
   cluster. Deletion protection is in the **Additional configuration** section.
5. Clear the **Enable deletion protection** check box in the
   **Additional configuration** properties card.
6. Choose **Continue**. The **Summary of modifications** appears.
7. Choose **Modify cluster** to accept the summary of modifications. You can also choose
   **Back** to modify your changes or **Cancel** to discard your changes.

After deletion protection is no longer active, you can delete your Aurora Serverless v1 DB cluster by using the
AWS Management Console.

###### To delete an Aurora Serverless v1 DB cluster

1. Sign in to the AWS Management Console and open the Amazon RDS console at
   [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/ "https://console.aws.amazon.com/rds/").
2. In the **Resources** section, choose **DB Clusters**.
3. Choose the Aurora Serverless v1 DB cluster that you want to delete.
4. For **Actions**, choose **Delete**. You're prompted to confirm
   that you want to delete your Aurora Serverless v1 DB cluster.
5. We recommend that you keep the preselected options:
   - **Yes** for **Create final snapshot?**
   - Your Aurora Serverless v1 DB cluster name plus `-final-snapshot` for **Final
     snapshot name**. However, you can change the name for your final snapshot in this field.

![Screenshot of deleting Aurora Serverless v1 database cluster](images/aurora-sles-delete-db-1.png)

If you choose **No** for **Create final snapshot?** you can't
restore your DB cluster using snapshots or point-in-time recovery. 6. Choose **Delete DB cluster**.

Aurora Serverless v1 deletes your DB cluster. If you chose to have a final snapshot, you see your
Aurora Serverless v1 DB cluster's status change to "Backing-up" before it's deleted and no longer
appears in the list.

Before you begin, configure your AWS CLI with your AWS Access Key ID, AWS Secret Access Key, and the
AWS Region where your Aurora Serverless v1 DB cluster is. For more information, see
[Configuration
basics](../../../cli/latest/userguide/cli-configure-quickstart.md#cli-configure-quickstart-config "../../../cli/latest/userguide/cli-configure-quickstart.md#cli-configure-quickstart-config") in the AWS Command Line Interface User Guide.

You can't delete an Aurora Serverless v1 DB cluster until after you first disable deletion protection
for clusters configured with this option. If you try to delete a cluster that has this protection option
enabled, you see the following error message.

```
An error occurred (InvalidParameterCombination) when calling the DeleteDBCluster
  operation: Cannot delete protected Cluster, please disable deletion protection and try again.
```

You can change your Aurora Serverless v1 DB cluster's deletion-protection setting by using the
[modify-db-cluster](../../../cli/latest/reference/rds/modify-db-cluster.md "../../../cli/latest/reference/rds/modify-db-cluster.md") AWS CLI command as shown in
the following:

```
aws rds modify-db-cluster --db-cluster-identifier `your-cluster-name` --no-deletion-protection
```

This command returns the revised properties for the specified DB cluster. You can now delete your
Aurora Serverless v1 DB cluster.

We recommend that you always create a final snapshot whenever you delete an Aurora Serverless v1 DB cluster.
The following example of using the AWS CLI
[delete-db-cluster](../../../cli/latest/reference/rds/delete-db-cluster.md "../../../cli/latest/reference/rds/delete-db-cluster.md") shows you how. You provide
the name of your DB cluster and a name for the snapshot.

For Linux, macOS, or Unix:

```
aws rds delete-db-cluster --db-cluster-identifier \
  `your-cluster-name` --no-skip-final-snapshot \
  --final-db-snapshot-identifier `name-your-snapshot`
```

For Windows:

```
aws rds delete-db-cluster --db-cluster-identifier ^
  `your-cluster-name` --no-skip-final-snapshot ^
  --final-db-snapshot-identifier `name-your-snapshot`
```
