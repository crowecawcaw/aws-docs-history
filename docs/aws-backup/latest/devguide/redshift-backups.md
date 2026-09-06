

# Amazon Redshift backups
<a name="redshift-backups"></a>

Amazon Redshift is a fully managed, scalable cloud data warehouse that accelerates your time to insights with fast, easy, and secure analytics. You can use AWS Backup to protect your data warehouses with immutable backups, separate access policies, and centralized organizational governance of backup and restore jobs.

An Amazon Redshift data warehouse is a collection of computing resources called nodes, which are organized into a group called a cluster. AWS Backup can backup these clusters.

For information on [Amazon Redshift](https://docs.aws.amazon.com/redshift/index.html) , see the [ Amazon Redshift Getting Started Guide](https://docs.aws.amazon.com/redshift/latest/gsg/index.html), the [Amazon Redshift Database Developer Guide](https://docs.aws.amazon.com/redshift/latest/dg/index.html), and the [Amazon Redshift Cluster Management Guide](https://docs.aws.amazon.com/redshift/latest/mgmt/index.html).

## Back up Amazon Redshift provisioned clusters
<a name="backupredshift"></a>

You can protect your Amazon Redshift clusters using the AWS Backup console or programmatically using API or CLI. These clusters can be backed up on a regular schedule as part of a backup plan, or they can be backed up as needed via on-demand backup.

You can restore a single table (also known as item-level restore) or an entire cluster. Note that tables cannot be backed up by themselves; tables are backed up as part of a cluster when the cluster is backed up.

Using AWS Backup allows you to view your resources in a centralized way; however, if Amazon Redshift is the only resource you use, you can continue to use the automated snapshot scheduler in Amazon Redshift. Note that you cannot continue to manage manual snapshot settings using Amazon Redshift if you choose to manage these via AWS Backup.

You can backup Amazon Redshift clusters either through the AWS Backup console or using the AWS CLI.

There are two ways to use the AWS Backup console to backup a Amazon Redshift cluster: on demand or as part of a backup plan.

### Create on-demand Amazon Redshift backups
<a name="ondemandredshiftbackups"></a>

See [ Creating an on-demand backup](https://docs.aws.amazon.com/aws-backup/latest/devguide/recov-point-create-on-demand-backup.html) type page for more information.

To create a manual snapshot, leave the continuous backup checkbox unchecked when you create a backup plan that includes Amazon Redshift resources.

### Create scheduled Amazon Redshift backups in a backup plan
<a name="scheduledredshiftbackups"></a>

Your scheduled backups can include Amazon Redshift clusters if they are a protected resource. To opt into protecting Amazon Redshift clusters:

1. Open the AWS Backup console at [https://console.aws.amazon.com/backup](https://console.aws.amazon.com/backup).

1. Using the navigation pane, choose **Protected resources**.

1. Toggle Amazon Redshift to **On**.

1. See [ Assigning resources to the console](https://docs.aws.amazon.com/aws-backup/latest/devguide/assigning-resources.html#assigning-resources-console) to include Amazon Redshift clusters in an existing or new plan.

Under **Manage Backup plans**, you can choose to [create a backup plan](https://docs.aws.amazon.com/aws-backup/latest/devguide/creating-a-backup-plan.html) and include Amazon Redshift clusters, or you can [update an existing one](https://docs.aws.amazon.com/aws-backup/latest/devguide/updating-a-backup-plan.html) to include Amazon Redshift clusters. When adding the resource type *Amazon Redshift*, you can choose to add **All Amazon Redshift clusters**, or check the boxes next to the clusters you wish to include in your backup plan.

### Back up programmatically
<a name="redshiftbackupapi"></a>

You can also define your backup plan in a JSON document and provide it using the AWS Backup console or AWS CLI. See [ Creating backup plans using a JSON document and the AWS Backup CLI](https://docs.aws.amazon.com/aws-backup/latest/devguide/creating-a-backup-plan.html#create-backup-plan-cli) for information on how to create a backup plan programatically.

You can do the following operations using API:
+ Start a backup job
+ Describe a backup job
+ Get recovery point metadata
**Note**  
`BackupSizeInBytes` metadata is supported for the following resource types: Amazon EBS volumes, Amazon EFS file systems, Amazon RDS databases, DynamoDB tables, Amazon EC2 instances, Amazon FSx file systems, and Amazon S3 buckets. This field provides the size of the backup in bytes and is available through the `DescribeRecoveryPoint` API and AWS Backup console. For unsupported resource types, this field will not be populated.
+ List recovery points by resources
+ List tags for the recovery point

### View Amazon Redshift cluster backups
<a name="viewredshiftbackups"></a>

To view and modify your Amazon Redshift table backups within the console:

1. Open the AWS Backup console at [https://console.aws.amazon.com/backup](https://console.aws.amazon.com/backup).

1. Choose **Backup vaults**. Then, click on the backup vault name that contains your Amazon Redshift clusters.

1. The backup vault will display a summary and a list of backups. You can click on the link in the column **Recovery point ID**.

1. To delete one or more recovery points, check the box(es) you wish to delete. Under the button **Actions**, you can select **Delete**.

### Restore a Amazon Redshift cluster
<a name="w2aac17c19c31c11c11c11"></a>

See how to [Restore a Amazon Redshift cluster](https://docs.aws.amazon.com/aws-backup/latest/devguide/redshift-restores.html) for more information.