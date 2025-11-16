# Tutorial: Restoring a DB cluster from a DB cluster snapshot using the Amazon RDS console

In this tutorial, you restore a DB cluster from a DB cluster snapshot using the Amazon RDS console. When you restore a DB cluster from a snapshot using the AWS Management Console, the primary (writer) DB instance is also created.

###### Note

While the primary DB instance is being created, it appears as a reader instance, but after creation it's a writer
instance.

###### To restore a DB cluster from a DB cluster snapshot

1. Sign in to the AWS Management Console and open the Amazon RDS console at
   [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/ "https://console.aws.amazon.com/rds/").
2. In the navigation pane, choose **Snapshots**.
3. Choose the DB cluster snapshot that you want to restore from.
4. For **Actions**, choose **Restore snapshot**.

![Restore snapshot option in the Actions menu in the RDS console](images/tut-restore-cluster1.png)

The **Restore snapshot** page appears. 5. Under **DB instance settings**, do the following:

    1. Use the default setting for **DB engine**.
    2. For **Available versions**, choose a MySQL–8.0 compatible version, such as
     **Aurora MySQL 3.04.0 (compatible with MySQL 8.0.28)**.

![Restore snapshot page](images/tut-restore-cluster2.png) 6. Under **Settings**, for **DB instance identifier** enter the unique name that you
want to use for the restored DB instance, for example `my-80`.

###### Note

To create the DB cluster identifier, Amazon RDS appends `-cluster` to the DB instance identifier you specify. 7. Under **Connectivity**, use the default settings for the following:

    * **Virtual private cloud (VPC)**
    * **DB subnet group**
    * **Public access**
    * **VPC security group (firewall)**

8. Choose the **DB instance class**.

For this tutorial, choose **Burstable classes (includes t classes)**, and then choose
**db.t3.medium**.

###### Note

We recommend using the T DB instance classes only for development and test servers, or other non-production
servers. For more details on the T instance classes, see [DB instance class types](Concepts.DBInstanceClass.md "Concepts.DBInstanceClass.md").

![DB instance configuration panel with options for instance class, availability, and performance settings during restore.](images/tut-restore-cluster3.png) 9. For **Database authentication**, use the default setting. 10. For **Encryption**, use the default settings.

If the source DB cluster for the snapshot was encrypted, the restored DB cluster is also encrypted. You can't
make it unencrypted. 11. Expand **Additional configuration** at the bottom of the page.

![Additional configuration options for database restore including network settings, encryption, and maintenance preferences.](images/tut-restore-cluster4.png) 12. Make the following choices:

    1. For this tutorial, use the default value for **DB cluster
     parameter group**.
    2. For this tutorial, use the default value for **DB parameter
     group**.
    3. For **Log exports**, select all of the check boxes.
    4. For **Deletion protection**, select the **Enable deletion protection** check
     box.

13. Choose **Restore DB instance**.
    The **Databases** page displays the restored DB cluster, with a status of `Creating`.

![Restored DB cluster on the Databases page](images/tut-restore-cluster5.png)
While the primary DB instance is being created, it appears as a reader instance, but after creation it's a writer
instance.
