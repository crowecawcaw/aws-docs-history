# Step-By-Step Migration

The following steps provide instructions for migrating Amazon RDS for MySQL databases to an Amazon S3 data lake.

###### Topics

- [Step 0: Configure the source Amazon RDS for MySQL database](#mysql-s3datalake.stepbystep.0 "#mysql-s3datalake.stepbystep.0")
- [Step 1: Create a replication instance](#mysql-s3datalake.stepbystep.1 "#mysql-s3datalake.stepbystep.1")
- [Step 2: Create an AWS DMS source endpoint](#mysql-s3datalake.stepbystep.2 "#mysql-s3datalake.stepbystep.2")
- [Step 3: Configure a target Amazon S3 bucket](#mysql-s3datalake.stepbystep.3 "#mysql-s3datalake.stepbystep.3")
- [Step 4: Create an AWS DMS Task](#mysql-s3datalake.stepbystep.5 "#mysql-s3datalake.stepbystep.5")
- [Step 5: Run and monitor your AWS DMS Task](#mysql-s3datalake.stepbystep.6 "#mysql-s3datalake.stepbystep.6")
- [Step 6: Monitor your migration](#mysql-s3datalake.stepbystep.7 "#mysql-s3datalake.stepbystep.7")
- [Conclusion](#mysql-s3datalake.conclusion "#mysql-s3datalake.conclusion")

## Step 0: Configure the source Amazon RDS for MySQL database

Before setting up AWS DMS resources, you need to configure your Amazon RDS for MySQL database instances as a source for AWS DMS.

### Amazon RDS Backup configuration

Your Amazon RDS for MySQL instance must have **Automatic Backups** turned on to use CDC. Otherwise, binary logging will not be enabled at the MySQL level. Enabling automatic backups enables binary logging for the database instance. The backup retention period can be any value from one to 35 days. One day is enough for this walkthrough.

### Binary logging configuration

To use AWS DMS CDC, the following parameters must be set correctly in the parameter group attached to your database instances.

- `binlog_format : "ROW"`
- `binlog_row_image` : "Full"`
- `binlog_checksum` : "NONE"`

The default **binlog_format** is “Mixed”. AWS DMS requires the “ROW” format, and all columns before and after the imaging. We recommend that **binlog_checksum** set to NONE.

### Binary logging retention hours

AWS DMS requires binary logs to be local to the Amazon RDS for MySQL database instance. To ensure that binary logs are available to AWS DMS, you should increase the length of time that the logs remain available in the database instance host. For example, to increase log retention to 24 hours, run the following command. 24 hours are enough for this walkthrough.

```
call mysql.rds_set_configuration('binlog retention hours', 24);
```

### VPC, Subnet and Network ACL configuration

In this walkthrough, the database instance and the replication instance are placed in the same VPC and the same subnet, so all you need to do is configure security groups, network ACLs, and route tables so that your Amazon RDS for MySQL database instance and AWS DMS replication instance can communicate within the same subnet. If you have source databases in a different subnet, VPC, or different location outside AWS, you need to configure your network to allow communication between your Amazon RDS for MySQL database instance and your AWS DMS replication instance.

### Inbound connection rule

To ensure that AWS DMS can access your database server, you need to make changes to the relevant security groups and network access control lists. AWS DMS only requires access to the MySQL database listener port (the default is 3306). The connection always starts from the AWS DMS replication instance to MySQL. Therefore, you add allowed connections from the replication instance to the ingress rule of the security group attached to the database instance. We recommend you add all subnet group ranges to the ingress rule, because replication instances are a managed service, and the IP address of a replication instance may change automatically.

You have now completed all necessary setup for your Amazon RDS for MySQL database instance. Next, create a replication instance.

## Step 1: Create a replication instance

To create an AWS DMS replication instance, do the following:

1. Sign in to the AWS Management Console, and open the [AWS DMS console](https://console.aws.amazon.com/dms/v2 "https://console.aws.amazon.com/dms/v2").
2. If you are signed in as an AWS Identity and Access Management (IAM) user, you must have the appropriate permissions to access AWS DMS. For more information about the permissions required, see IAM permissions.
3. On the Welcome page, choose **Create replication instance**` to start a database migration.
4. On the **Create replication instance** page, specify your replication instance information.

|                             |                                                                                                                                                                                                              |
| --------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| For this parameter          | Do this                                                                                                                                                                                                      |
| **Name**                    | Enter `s3-datalake-migration-ri`. If you are using multiple replication servers or sharing an account, choose a name that helps you quickly differentiate between the different servers.                     |
| **Description**             | Enter `Migrate MySQL to [.shared]`S3` data lake`.                                                                                                                                                            |
| **Instance class**          | Choose `dms.c5.9xlarge`. Each size and type of instance class has increasing CPU, memory, and I/O capacity.                                                                                                  |
| **Engine version**          | Leave the default value, which is the latest stable version of the AWS DMS replication engine.                                                                                                               |
| **Allocated storage (GiB)** | Choose `100 GiB`.                                                                                                                                                                                            |
| **VPC**                     | Choose the virtual private cloud (VPC) in which your replication instance will launch. Select the same VPC in which your source is placed.                                                                   |
| **Multi AZ**                | In this scenario, choose **No**. If you choose **Yes**, AWS DMS creates a second replication server in a different Availability Zone for failover if there is a problem with the primary replication server. |
| **Publicly accessible**     | Choose **Yes**. If either your source or target database resides outside of the VPC in which your replication server resides, you must make your replication server policy publicly accessible.              |

Once the creation of the replication instance starts, it usually becomes available in about ten minutes or more. The next endpoint can be created even when the replication instance is in the `creating` status, but the connection test cannot be performed unless the replication instance is in the `available` status.

## Step 2: Create an AWS DMS source endpoint

To create a source endpoint, do the following:

1. Open the AWS DMS console at [https://console.aws.amazon.com/dms/v2/](https://console.aws.amazon.com/dms/v2/ "https://console.aws.amazon.com/dms/v2/").
2. Choose **Endpoints**.
3. Choose **Create endpoint**.
4. On the **Create endpoint** page, enter the following information.

**Source endpoint 1:**

|                                                                                                            |
| ---------------------------------------------------------------------------------------------------------- |
| **Endpoint type**                                                                                          |
| Choose **Source endpoint**, **Select RDS DB instance**, and choose the `datalake-source-db1` RDS instance. |
| **Endpoint identifier**                                                                                    |
| Enter **mysql-dms-s3-source-1**                                                                            |
| **Source engine**                                                                                          |
| Choose **MySQL**.                                                                                          |
| **Access to endpoint database**                                                                            |
| Choose **Provide access information manually**.                                                            |
| **Server name**                                                                                            |
| Enter the Amazon RDS database server name.                                                                 |
| **Port**                                                                                                   |
| Enter **3306**.                                                                                            |
| **Secure Socket Layer (SSL) mode**                                                                         |
| Choose **none**.                                                                                           |
| **User name**                                                                                              |
| Enter **dms_user**.                                                                                        |
| **Password**                                                                                               |
| Enter the password that you created for the `dms_user` user.                                               |

**Source endpoint 2:**

|                                                                                                            |
| ---------------------------------------------------------------------------------------------------------- |
| **Endpoint type**                                                                                          |
| Choose **Source endpoint**, **Select RDS DB instance**, and choose the `datalake-source-db2` RDS instance. |
| **Endpoint identifier**                                                                                    |
| Enter **mysql-dms-s3-source-2**                                                                            |
| **Source engine**                                                                                          |
| Choose **MySQL**.                                                                                          |
| **Access to endpoint database**                                                                            |
| Choose **Provide access information manually**.                                                            |
| **Server name**                                                                                            |
| Enter the [.shared]`RDS`database server name.                                                              |
| **Port**                                                                                                   |
| Enter **3306**.                                                                                            |
| **Secure Socket Layer (SSL) mode**                                                                         |
| Choose **none**.                                                                                           |
| **User name**                                                                                              |
| Enter **dms_user**.                                                                                        |
| **Password**                                                                                               |
| Enter the password that you created for the `dms_user` user.                                               |

You can try testing the connection before you finish creating the endpoint. Test Connection attempts to connect from the replication instance to the source database and verify that the replication instance can connect to MySQL with the settings provided. If the connection test succeeds, go to the next step; otherwise, check if the values you set for the endpoint are correct. If correct, check if the network between the source and the replication instance is configured correctly.

## Step 3: Configure a target Amazon S3 bucket

To create the Amazon S3 bucket, do the following:

1. Open the Amazon S3 console at [https://s3.console.aws.amazon.com/s3/home](https://s3.console.aws.amazon.com/s3/home "https://s3.console.aws.amazon.com/s3/home").
2. Choose **Create bucket**.
3. For **Bucket name**, enter \*\*<your-bucket-name>\*\*. Note: The bucket name needs to be unique globally.
4. For **AWS Region**, choose the region that hosts your AWS DMS replication instance.
5. Leave the default values in the other fields and choose **Create bucket**.

To use Amazon S3 as an AWS Database Migration Service (AWS DMS) target endpoint, create an IAM role with write and delete access to the S3 bucket. Then add DMS (dms.amazonaws.com) as trusted entity in this IAM role. This is a minimum required assume role policy and policy document. For more information, see [Prerequisites for using Amazon S3 as a target](../userguide/CHAP_Target.md#CHAP_Target.S3.Prerequisites "../userguide/CHAP_Target.md#CHAP_Target.S3.Prerequisites").

Assume role policy:

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": {
                "Service": [
                    "dms.amazonaws.com",
                ]
            },
            "Action": "sts:AssumeRole"
        }
    ]
}
```

Policy:

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Action": [
                "s3:PutObject",
                "s3:DeleteObject",
                "s3:PutObjectTagging"
            ],
            "Resource": [
                "arn:aws:s3:::mysql2s3walkthough/*"
            ],
            "Effect": "Allow"
        },
        {
            "Action": "s3:ListBucket",
            "Resource": "arn:aws:s3:::mysql2s3walkthough",
            "Effect": "Allow"
        }
    ]
}
```

To create a target endpoint, do the following:

1. Open the AWS DMS console at [https://console.aws.amazon.com/dms/v2/](https://console.aws.amazon.com/dms/v2/ "https://console.aws.amazon.com/dms/v2/").
2. Choose **Endpoints**, and then choose **Create endpoint**.
3. On the **Create endpoint** page, enter the following information.

|                             |                                                                      |
| --------------------------- | -------------------------------------------------------------------- |
| **Endpoint type**           | Choose **Target endpoint**, and turn off **Select RDS DB instance**. |
| **Endpoint identifier**     | Enter **mysql-dms-s3-target.**                                       |
| **Target engine**           | Choose \*_Amazon S3_<br>• .                                          |
| **Service access role ARN** | Enter the IAM role that can access your Amazon S3 data lake.         |
| **Bucket name**             | Enter **<your-bucket-name>.**                                        |

Expand the **Endpoint settings** section, choose **Wizard**, and then choose **Add new setting** to add the settings as shown on the following image.

When using AWS DMS to migrate data to an Amazon Simple Storage Service (Amazon S3) data lake, you can change the default task behavior, such as file formats, partitioning, file sizing, etc. This leads to minimizing post-migration processing and helps downstream applications consume data efficiently. You can customize task behavior using endpoint settings and extra connection attributes (ECA). Most of the Amazon S3 endpoint settings and ECA settings overlap, except for a few parameters. In this walkthrough, we will configure Amazon S3 endpoint settings.

### Choose file format (`dataFormat`)

AWS DMS supports CSV and Parquet formats for outputing data to an S3 target. Each file format has its own benefits. Choose the right file format depending on your consumption pattern. Apache Parquet is an open-source file format that stores data in a columnar format, which is built to support efficient compression and encoding schemes providing storage space savings and performance benefits. CSV files are helpful when you plan to keep data in human readable format, or share or transfer Amazon S3 files into other downstream systems for further processing. In this scenario, we will use the CSV format.

### Date based partitioning (`DatePartitionEnabled`)

In addition to using optimized file formats like Parquet, another common approach for further optimization is to partition the data. AWS DMS supports date-based folder partitioning based on transaction commit dates. The data is stored in different folders based on a timestamp which has following benefits:

- Better management for your S3 objects.
- Limiting the size of each S3 folder.
- Optimizing data lake queries or other subsequent operations.

```
dms_sample/post_history/LOAD00000001.csv
dms_sample/post_history/LOAD00000002.csv
...
dms_sample/posts/LOAD00000001.csv
dms_sample/posts/LOAD00000002.csv
dms_sample/posts/LOAD00000003.csv
...
...
dms_sample/posts/2022/5/21/20220521-145815742.csv
dms_sample/posts/2022/5/21/20220521-145918391.csv
```

### Determine file size

By default, an AWS DMS task writes captured data to an Amazon S3 bucket either if the file size reaches 32 MB or if the previous file write was more than 60 seconds ago. These settings ensure that the data capture latency is low. However, this approach creates a large number of small files in the target Amazon S3 bucket. This value can be changed with `CdcMaxBatchInterval` in the S3 target endpoint settings.

However, we need to optimize this schema for cost and performance. When you use distributed processing frameworks such as Amazon Athena, AWS Glue or Amazon EMR, it is recommended to avoid having many small files (less than 64 MB). Small files tend to cause operational overhead in various distributed processing frameworks. Since we plan to use Amazon Athena to query data from our Amazon S3 bucket, we need to make sure our target file size is at least 64 MB.

In this scenario, we’ll use the following endpoint settings: `MaxFileSize=64000`, `CdcMaxBatchInterval=3600` and `CdcMinFileSize=64000`. These settings ensure that AWS DMS does not write the file until its size reaches 64 MB or if the last file write was more than an hour ago.

### Serialize ongoing replication events

A common challenge when using Amazon S3 as a target involves identifying the ongoing replication event sequence when multiple records are updated at the same time on the source database. AWS DMS provides two options to help serialize such events for Amazon S3. You can use the `TimeStampColumnName` endpoint setting or use transformation rules to include a LSN column. Here, we will discuss the first option. For more information about the second option, see [Step 6: Create an AWS DMS Task](chap-rdssqlserver2s3datalake.steps.md "chap-rdssqlserver2s3datalake.steps.md").

### Use the TimeStampColumnName endpoint setting

The `TimeStampColumnName` setting adds an additional `STRING` column to the target Parquet file created by AWS DMS. During ongoing replication, the column value represents the commit timestamp of the event in SQL Server. For the full load phase, the columns' values represent the timestamp of the data transfer to Amazon S3. The default format is `yyyy-MM-dd HH:mm:ss.SSSSSS`. This format provides a microsecond precision, but also depends on the source database transaction log timestamp precision.

### Include full load operation field

All files created during ongoing replication have the first column marked with `I`, `U`, or `D`. These symbols represent the DML operation on the source and stand for **Insert**, **Update**, or **Delete**. For full load files, you can add this column by configuring the following endpoint setting.

```
includeOpForFullLoad=true
```

This ensures that all full load files are marked with an `I` operation.

When you use this approach, new subscribers can consume the entire data set or prepare a fresh copy in case of any downstream processing issues.

AWS DMS outputs an extra column (`Op`) where each record has one of the DML flags (I: Insert, U: Update, or D: Delete) in addition to the existing columns in the source tables, indicating which operation generated the change at that time.

In the following example, a source table has a structure similar to the following:

|     |       |     |      |
| --- | ----- | --- | ---- |
| id  | name  | age | year |
| 1   | Scott | 36  | 1986 |
| 2   | Mike  | 27  | 1995 |
| 3   | Bob   | 42  | 1980 |

For this example, we insert a record into this table such as the following:

```
INSERT INTO dms_example.users (id, name, age, birthday) VALUES (4, 'Kate', 23, 1999);
```

The generated record will look similar to the following:

```
I, 4, Kate, 23, 1999
```

To handle these changed data, you need to take the operation flag into consideration when querying the file output in the S3 bucket, or alternatively you can process those files using AWS Glue and store the output in another S3 bucket which can then be queried using Amazon Athena.

There are several possible methods depending on what software stack you want to achieve. The last section in this document, Next Steps, references specific examples.

In this scenario, we’ll use the following settings:

**Endpoint 1:**

```
{
  "ServiceAccessRoleArn": "arn:aws:iam::<ACCOUNT_ID>:role/mysql2s3-walkthrough-dms-s3-target-access-role",
  "CsvRowDelimiter": "\\n",
  "CsvDelimiter": ",",
  "BucketName": "<S3_BUCKET_NAME>",
  "BucketFolder": "endpoint1",
  "CompressionType": "NONE",
  "DataFormat": "CSV",
  "EnableStatistics": true,
  "DatePartitionEnabled": true,
  "MaxFileSize": 64000,
  "CdcMaxBatchInterval": 3600,
  "CdcMinFileSize": 64000,
  "IncludeOpForFullLoad": true
}
```

**Endpoint 2:**

```
{
  "ServiceAccessRoleArn": "arn:aws:iam::<ACCOUNT_ID>:role/mysql2s3-walkthrough-dms-s3-target-access-role",
  "CsvRowDelimiter": "\\n",
  "CsvDelimiter": ",",
  "BucketName": "<S3_BUCKET_NAME>",
  "BucketFolder": "endpoint2",
  "CompressionType": "NONE",
  "DataFormat": "CSV",
  "EnableStatistics": true,
  "DatePartitionEnabled": true,
  "MaxFileSize": 64000,
  "CdcMaxBatchInterval": 3600,
  "CdcMinFileSize": 64000,
  "IncludeOpForFullLoad": true
}
```

By using this configuration, data on two sharded database instances will be migrated to different bucket folders in the same bucket.

## Step 4: Create an AWS DMS Task

After you configure the replication instance and endpoints, the next step is creating the AWS DMS task. In this scenario, we will
create a task that performs both full-load and CDC. To create a database migration task, do the following:

1. Open the AWS DMS console at [https://console.aws.amazon.com/dms/v2/](https://console.aws.amazon.com/dms/v2/ "https://console.aws.amazon.com/dms/v2/").
2. Select **Database migration tasks**, and then choose **Create task**.
3. On the **Create database migration task** page, enter the following information.

**Replication task 1:**

|                                                  |                                                                                  |
| ------------------------------------------------ | -------------------------------------------------------------------------------- |
| For this parameter                               | Do this                                                                          |
| **Task identifier**                              | Enter **mysql-dms-s3-task-1**                                                    |
| **Replication instance**                         | Choose \*_datalake-migration-ri_<br>• (the value that you configured on Step 1). |
| **Source database endpoint**                     | Choose \*_mysql-dms-s3-source-1_<br>• (the value that you configured on Step 3). |
| **Target database endpoint**                     | Choose \*_mysql-dms-s3-target_<br>• (the value that you configured on Step 4).   |
| **Migration type**                               | Choose **Migrate existing data and replicate ongoing changes**.                  |
| **Editing mode**                                 | Choose **Wizard**.                                                               |
| **Custom CDC stop mode for source transactions** | Choose **Disable custom CDC stop mode**.                                         |
| **Target table preparation mode**                | Choose **Drop and create**                                                       |
| **Stop task after full load completes**          | Choose **Don’t stop**.                                                           |
| **Include LOB columns in replication**           | Choose **Limited LOB mode**.                                                     |
| **Maximum LOB size (KB)**                        | Enter **1024**                                                                   |
| **Enable validation**                            | Enter **1024**                                                                   |
| **Enable validation**                            | Turn off because Amazon S3 does not support validation.                          |
| **Enable CloudWatch logs**                       | Turn on.                                                                         |

**Replication task 2:**

|                                                  |                                                                                  |
| ------------------------------------------------ | -------------------------------------------------------------------------------- |
| For this parameter                               | Do this                                                                          |
| **Task identifier**                              | Enter **mysql-dms-s3-task-2**                                                    |
| **Replication instance**                         | Choose \*_datalake-migration-ri_<br>• (the value that you configured on Step 1). |
| **Source database endpoint**                     | Choose \*_mysql-dms-s3-source-2_<br>• (the value that you configured on Step 3). |
| **Target database endpoint**                     | Choose \*_mysql-dms-s3-target_<br>• (the value that you configured on Step 4).   |
| **Migration type**                               | Choose **Migrate existing data and replicate ongoing changes**.                  |
| **Editing mode**                                 | Choose **Wizard**.                                                               |
| **Custom CDC stop mode for source transactions** | Choose **Disable custom CDC stop mode**.                                         |
| **Target table preparation mode**                | Choose **Drop and create**                                                       |
| **Stop task after full load completes**          | Choose **Don’t stop**.                                                           |
| **Include LOB columns in replication**           | Choose **Limited LOB mode**.                                                     |
| **Maximum LOB size (KB)**                        | Enter **1024**                                                                   |
| **Enable validation**                            | Enter **1024**                                                                   |
| **Enable validation**                            | Turn off because Amazon S3 does not support validation.                          |
| **Enable CloudWatch logs**                       | Turn on.                                                                         |

Table mappings:

```
{
  "rules": [
    {
      "rule-type": "selection",
      "rule-id": 1,
      "rule-name": "1",
      "object-locator": {
        "schema-name": "dms_sample",
        "table-name": "%"
      },
      "rule-action": "include"
    },
    {
      "rule-type": "table-settings",
      "rule-id": 2,
      "rule-name": "2",
      "object-locator": {
        "schema-name": "dms_sample",
        "table-name": "post_history"
      },
      "parallel-load": {
        "type": "partitions-auto"
      }
    },
    {
      "rule-type": "table-settings",
      "rule-id": 3,
      "rule-name": "3",
      "object-locator": {
        "schema-name": "dms_sample",
        "table-name": "posts"
      },
      "parallel-load": {
        "type": "partitions-auto"
      }
    },
    {
      "rule-type": "table-settings",
      "rule-id": 4,
      "rule-name": "3",
      "object-locator": {
        "schema-name": "dms_sample",
        "table-name": "votes"
      },
      "parallel-load": {
        "type": "partitions-auto"
      }
    }
  ]
}
```

Task settings:

```
{
  "TargetMetadata": {
    "SupportLobs": true,
    "LimitedSizeLobMode": true,
    "LobMaxSize": 1024,
  },
  "FullLoadSettings": {
    "TargetTablePrepMode": "TRUNCATE_BEFORE_LOAD",
    "MaxFullLoadSubTasks": 49,
    "CommitRate": 50000
  },
  "Logging": {
    "EnableLogging": true
  }
}
```

## Step 5: Run and monitor your AWS DMS Task

After you created your AWS Database Migration Service (AWS DMS) task, start your replication tasks. To start your AWS DMS task, do the following:

1. Open the AWS DMS console at [https://console.aws.amazon.com/dms/v2/](https://console.aws.amazon.com/dms/v2/ "https://console.aws.amazon.com/dms/v2/").
2. Select **Database migration tasks**, and then choose **Create task**.
3. On the **Create database migration task** page, select your replication task.
4. Choose **Actions**, **“Restart / Resume”**.

## Step 6: Monitor your migration

### Task status and Table statistics

After you start the task, the full load operation starts loading tables. Your replication task status will be
**“Running”** until full-load completes. After the AWS DMS task completes full load, the task status changes
to the **Load complete, replication ongoing** phase. The following image shows the updated status of the task.

You can see the table load completion status in the **Table statistics** section and the corresponding target files
in the Amazon S3 bucket. You can check the progress of replication on the **Table statistics** tab. AWS DMS
first does full-load on each table. Meanwhile, the task status is **Running**, and at least one of the tables' Load
states is **“Before Load”** or **“Full load”**. Tables that have been loaded are displayed as **“Table completed”**. When
all tables have been fully loaded, the task status becomes **“Load completed, replication ongoing”**. The task continues
to capture source changes and apply them to the target.

In this scenario, the full-load phase typically completes in about 20 minutes. If you don’t use **partitions-auto** for table mapping,
the same full-load phase takes about an hour. Parallel full load can significantly improve full load performance.

### Cloudwatch Metrics

The AWS DMS console shows CloudWatch statistics for each task. To see metrics, select the replication task and then
select the **CloudWatch metrics** tab.

Task metrics are divided into statistics between the replication host and the source endpoint, and statistics between the
replication host and the target endpoint. You can determine the total statistic for a task by adding two related statistics
together. For example, you can determine the total latency, or replica lag, for a task by combining the **CDCLatencySource**
and **CDCLatencyTarget** values.

**CDCLatencySource** is the gap, in seconds, between the last event captured from the source endpoint and current system time
stamp of the AWS DMS instance. CDCLatencySource represents the latency between source and replication instance. High
CDCLatencySource means the process of capturing changes from source is delayed. To identify latency in an ongoing replication,
you can view this metric together with CDCLatencyTarget. If both CDCLatencySource and CDCLatencyTarget are high, investigate
CDCLatencySource first.

**CDCLatencyTarget** is the gap, in seconds, between the first event timestamp waiting to commit on the target and the current
timestamp of the AWS DMS instance. Target latency is the difference between the replication instance server time and the oldest
unconfirmed event id forwarded to a target component. In other words, target latency is the timestamp difference between the
replication instance and the oldest event applied but unconfirmed by the TRG endpoint. When CDCLatencyTarget is high, it indicates
that the process of applying change events to the target is delayed.

These metrics are useful for knowing what state your tasks are in.

## Conclusion

In this walkthrough, we covered most prerequisites that help avoid configuration related errors. You can get started on your
own migrations using the following documentation.

- [Getting started with Database Migration Service](../userguide/CHAP_GettingStarted.md "../userguide/CHAP_GettingStarted.md").
- [Using a MySQL-compatible database as a source for AWS DMS](../userguide/CHAP_Source.md "../userguide/CHAP_Source.md")
- [Using Amazon S3 as a target](../userguide/CHAP_Target.md "../userguide/CHAP_Target.md")

If you observe issues when running your task, see
[Troubleshooting migration tasks](../userguide/CHAP_Troubleshooting.md "../userguide/CHAP_Troubleshooting.md")
and [Best practices](../userguide/CHAP_BestPractices.md "../userguide/CHAP_BestPractices.md") in the AWS DMS public
documentation, or reach out to AWS Support for further assistance.
