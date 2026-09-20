

# Create a database table
<a name="firehose-redshift-create-db-table"></a>

After you connect to the initial database in Amazon Redshift, you typically use it as the base for creating a new database. However, for passing Amazon SNS notifications through Firehose to Amazon Redshift, you need to create a table that omits the `Message` and `MessageAttributes` fields. This page shows how to create the table using SQL Workbench/J.

**To create a table using SQL Workbench/J**

1. Open SQL Workbench/J and connect to your Amazon Redshift cluster. For instructions, see [Connect to the cluster](https://docs.aws.amazon.com/redshift/latest/gsg/rs-gsg-connect-to-cluster.html) in the *Amazon Redshift Getting Started Guide*.

1. In SQL Workbench/J, copy the following code and paste it into the **Statement 1** window.

   ```
   CREATE TABLE notifications (
       type varchar(256),
       messageid varchar(256),
       topicarn varchar(256),
       subject varchar(256),
       message varchar(2048),
       timestamp timestamptz,
       unsubscribeurl varchar(1024),
       messageattributes varchar(2048)
   );
   ```

1. Place the cursor within the statement (before the semicolon). Then choose the **Execute current statement** button.

1. In the **Messages** pane, verify that your table was successfully created.

You've created the database table. To continue, return to the [Task overview](firehose-redshift-destinations.md).