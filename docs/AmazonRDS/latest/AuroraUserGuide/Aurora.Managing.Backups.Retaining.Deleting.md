

# Deleting retained automated backups for Amazon Aurora
<a name="Aurora.Managing.Backups.Retaining.Deleting"></a>

You can delete retained automated backups when they are no longer needed. To delete a retained automated backup using the AWS Management Console, AWS CLI, or Amazon RDS API, use the following procedures.

## Console
<a name="Aurora.Managing.Backups.Retaining.Deleting.CON"></a>

**To delete a retained automated backup**

1. Sign in to the AWS Management Console and open the Amazon RDS console at [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/).

1. In the navigation pane, choose **Automated backups**.

1. Choose the **Retained** tab.  
![Retained automated backups interface showing backup retention settings and available recovery points.](http://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/images/db-cluster-retained-automated-backups.png)

1. Choose the retained automated backup that you want to delete.

1. For **Actions**, choose **Delete**.

1. On the confirmation page, enter **delete me** and choose **Delete**.

## AWS CLI
<a name="Aurora.Managing.Backups.Retaining.Deleting.CLI"></a>

You can delete a retained automated backup by using the AWS CLI command [delete-db-cluster-automated-backup](https://docs.aws.amazon.com/cli/latest/reference/rds/delete-db-cluster-automated-backup.html) with the following option:
+ `--db-cluster-resource-id` – The resource identifier for the source DB cluster.

  You can find the resource identifier for the source DB cluster of a retained automated backup by running the AWS CLI command [describe-db-cluster-automated-backups](https://docs.aws.amazon.com/cli/latest/reference/rds/describe-db-cluster-automated-backups.html).

**Example**  
This example deletes the retained automated backup for the source DB cluster that has the resource ID `cluster-123ABCEXAMPLE`.  
For Linux, macOS, or Unix:  

```
1. aws rds delete-db-cluster-automated-backup \
2.     --db-cluster-resource-id {{cluster-123ABCEXAMPLE}}
```
For Windows:  

```
1. aws rds delete-db-cluster-automated-backup ^
2.     --db-cluster-resource-id {{cluster-123ABCEXAMPLE}}
```

## RDS API
<a name="Aurora.Managing.Backups.Retaining.Deleting.API"></a>

You can delete a retained automated backup by using the Amazon RDS API operation [DeleteDBClusterAutomatedBackup](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_DeleteDBClusterAutomatedBackup.html) with the following parameter:
+ `DbClusterResourceId` – The resource identifier for the source DB cluster.

  You can find the resource identifier for the source DB instance of a retained automated backup using the Amazon RDS API operation [DescribeDBClusterAutomatedBackups](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_DescribeDBClusterAutomatedBackups.html).