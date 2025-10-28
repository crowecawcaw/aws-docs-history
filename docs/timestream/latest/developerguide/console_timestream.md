For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified
data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](timestream-for-influxdb.md "timestream-for-influxdb.md").

# Using the console

You can use the AWS Management Console for Timestream Live Analytics to create, edit, delete,
describe, and list databases and tables. You can also use the console to run
queries.

###### Topics

- [Tutorial](#console_timestream.db-w-sample-data "#console_timestream.db-w-sample-data")
- [Create a database](#console_timestream.db.using-console "#console_timestream.db.using-console")
- [Create a table](#console_timestream.table.using-console "#console_timestream.table.using-console")
- [Run a query](#console_timestream.queries.using-console "#console_timestream.queries.using-console")
- [Create a scheduled
  query](#console_timestream.scheduledquery.using-console "#console_timestream.scheduledquery.using-console")
- [Delete a scheduled query](#console_timestream.scheduledquerydeletedisable.using-console "#console_timestream.scheduledquerydeletedisable.using-console")
- [Delete a
  table](#console_timestream.delete-table.using-console "#console_timestream.delete-table.using-console")
- [Delete a database](#console_timestream.delete-db.using-console "#console_timestream.delete-db.using-console")
- [Edit a table](#console_timestream.edit-table.using-console "#console_timestream.edit-table.using-console")
- [Edit a database](#console_timestream.edit-db.using-console "#console_timestream.edit-db.using-console")

## Tutorial

This tutorial shows you how to create a database populated with sample data sets
and run sample queries. The sample datasets used in this tutorial are frequently
seen in IoT and DevOps scenarios. The IoT dataset contains time series data such as
the speed, location, and load of a truck, to streamline fleet management and
identify optimization opportunities. The DevOps dataset contains EC2 instance
metrics such as CPU, network, and memory utilization to improve application
performance and availability. Here's a [video tutorial](https://www.youtube.com/watch?v=YBWCGDd4ChQ "https://www.youtube.com/watch?v=YBWCGDd4ChQ") for the
instructions described in this section

Follow these steps to create a database populated with the sample data sets and
run sample queries using the AWS Console.

1. Open the [AWS
   Console](https://console.aws.amazon.com/timestream "https://console.aws.amazon.com/timestream").
2. In the navigation pane, choose **Databases**
3. Click on **Create database**.
4. On the create database page, enter the following:
   - **Choose configuration**—Select
     **Sample database**.
   - **Name**—Enter a database name of your
     choice.
   - **Choose sample datasets**—Select
     **IoT** and **DevOps**.
   - Click on **Create database** to create a
     database containing two tables—IoT and DevOps populated with
     sample data.

5. In the navigation pane, choose **Query editor**
6. Select **Sample queries** from the top menu.
7. Click on one of the sample queries. This will take you back to the query
   editor with the editor populated with the sample query.
8. Click **Run** to run the query and see query
   results.

## Create a database

Follow these steps to create a database using the AWS Console.

1. Open the [AWS
   Console](https://console.aws.amazon.com/timestream "https://console.aws.amazon.com/timestream").
2. In the navigation pane, choose **Databases**
3. Click on **Create database**.
4. On the create database page, enter the following.
   - **Choose configuration**—Select
     **Standard database**.
   - **Name**—Enter a database name of your
     choice.
   - **Encryption** —Choose a KMS key or use
     the default option, where Timestream Live Analytics will create a KMS key in
     your account if one does not already exist.

5. Click on **Create database** to create a
   database.

## Create a table

Follow these steps to create a table using the AWS Console.

1. Open the [AWS
   Console](https://console.aws.amazon.com/timestream "https://console.aws.amazon.com/timestream").
2. In the navigation pane, choose **Tables**
3. Click on **Create table**.
4. On the create table page, enter the following.
   - **Database name**—Select the name of the
     database created in [Create a database](#console_timestream.db.using-console "#console_timestream.db.using-console").
   - **Table name**—Enter a table name of your
     choice.
   - **Memory store retention**—Specify how
     long you want to retain data in the memory store. The memory store
     processes incoming data, including late arriving data (data with a
     timestamp earlier than the current time) and is optimized for fast
     point-in-time queries.
   - **Magnetic store retention**—Specify how
     long you want to retain data in the magnetic store. The magnetic
     store is meant for long term storage and is optimized for fast
     analytical queries.

5. Click on **Create table**.

## Run a query

Follow these steps to run queries using the AWS Console.

1. Open the [AWS
   Console](https://console.aws.amazon.com/timestream "https://console.aws.amazon.com/timestream").
2. In the navigation pane, choose **Query editor**
3. In the left pane, select the database created in [Create a database](#console_timestream.db.using-console "#console_timestream.db.using-console").
4. In the left pane, select the database created in [Create a table](#console_timestream.table.using-console "#console_timestream.table.using-console").
5. In the query editor, you can run a query. To see the latest 10 rows in the
   table, run:

```
SELECT * FROM <database_name>.<table_name> ORDER BY time DESC LIMIT 10
```

6. (Optional) Turn on **Enable Insights** to get insights about the efficiency of your queries.

## Create a scheduled

query

Follow these steps to create a scheduled query using the AWS Console.

1. Open the [AWS
   Console](https://console.aws.amazon.com/timestream "https://console.aws.amazon.com/timestream").
2. In the navigation pane, choose **Scheduled
   queries**.
3. Click on **Create scheduled query**.
4. In the **Query Name** and **Destination
   Table** sections, enter the following.
   - **Name**—Enter a query name.
   - **Database name**—Select the name of the
     database created in [Create a database](#console_timestream.db.using-console "#console_timestream.db.using-console").
   - **Table name**—Select the name of the
     table created in [Create a table](#console_timestream.table.using-console "#console_timestream.table.using-console").

5. In the **Query Statement** section, enter a valid query
   statement. Then click **Validate query**.
6. From **Destination table model**, define the model for
   any undefined attributes. You can use **Visual builder** or
   JSON.
7. In the **Run schedule** section, choose **Fixed
   rate** or **Chron expression**.For chron
   expressions, refer to [Schedule Expressions
   for Scheduled Queries](scheduledqueries-schedule.md "scheduledqueries-schedule.md") for more details on schedule expressions.
8. In the **SNS topic** section, enter the SNS topic that
   will be used to for notification.
9. In the **Error log report** section enter the S3 location
   that will be used to report errors.

Choose the **Encryption key type**. 10. In the **Security settings** section from **AWS
KMS key**, choose the type of AWS KMS key.

Enter the **IAM role** that Timestream for LiveAnalytics will use to run the
scheduled query. Refer to the [IAM policy examples for scheduled queries](security_iam_id-based-policy-examples.md#security_iam_id-based-policy-examples-sheduledqueries "security_iam_id-based-policy-examples.md#security_iam_id-based-policy-examples-sheduledqueries") for details on the
required permissions and trust relationship for the role. 11. Click **Create scheduled query**.

## Delete a scheduled query

Follow these steps to delete or disable a scheduled query using the AWS
Console.

1. Open the [AWS
   Console](https://console.aws.amazon.com/timestream "https://console.aws.amazon.com/timestream").
2. In the navigation pane, choose **Scheduled
   queries**
3. Select the scheduled query created in [Create a scheduled
   query](#console_timestream.scheduledquery.using-console "#console_timestream.scheduledquery.using-console").
4. Select **Actions**.
5. Choose **Disable** or **Delete**.
6. If you selected Delete, confirm the action and select
   **Delete**.

## Delete a

table

Follow these steps to delete a database using the AWS Console.

1. Open the [AWS
   Console](https://console.aws.amazon.com/timestream "https://console.aws.amazon.com/timestream").
2. In the navigation pane, choose **Tables**
3. Select the table that you created in [Create a table](#console_timestream.table.using-console "#console_timestream.table.using-console").
4. Click **Delete**.
5. Type _delete_ in the confirmation box.

## Delete a database

Follow these steps to delete a database using the AWS Console:

1. Open the [AWS
   Console](https://console.aws.amazon.com/timestream "https://console.aws.amazon.com/timestream").
2. In the navigation pane, choose **Databases**
3. Select the database that you created in **Create a
   database**.
4. Click **Delete**.
5. Type _delete_ in the confirmation box.

## Edit a table

Follow these steps to edit a table using the AWS Console.

1. Open the [AWS
   Console](https://console.aws.amazon.com/timestream "https://console.aws.amazon.com/timestream").
2. In the navigation pane, choose **Tables**
3. Select the table that you created in [Create a table](#console_timestream.table.using-console "#console_timestream.table.using-console").
4. Click **Edit**
5. Edit the table details and save.
   - **Memory store retention**—Specify how
     long you want to retain data in the memory store. The memory store
     processes incoming data, including late arriving data (data with a
     timestamp earlier than the current time) and is optimized for fast
     point-in-time queries.
   - **Magnetic store retention**—Specify how
     long you want to retain data in the magnetic store. The magnetic
     store is meant for long term storage and is optimized for fast
     analytical queries.

## Edit a database

Follow these steps to edit a database using the AWS Console.

1. Open the [AWS
   Console](https://console.aws.amazon.com/timestream "https://console.aws.amazon.com/timestream").
2. In the navigation pane, choose **Databases**
3. Select the database that you created in **Create a
   database**.
4. Click **Edit**
5. Edit the database details and save.
