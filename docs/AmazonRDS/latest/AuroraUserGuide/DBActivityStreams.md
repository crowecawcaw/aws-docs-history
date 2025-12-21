# Starting a database activity stream

To monitor database activity for all instances in your Aurora DB cluster, start an activity stream at the cluster level. Any
DB instances that you add to the cluster are also automatically monitored. If you use an Aurora global database, start a database activity stream
on each DB cluster separately. Each cluster delivers audit data to its own Kinesis stream within its own AWS Region.

When you start an activity stream, each database activity event that you configured in the audit policy generates an activity stream event.
SQL commands such as `CONNECT` and `SELECT`
generate access events. SQL commands such as `CREATE` and `INSERT`
generate change events.

Console###### To start a database activity stream

1. Open the Amazon RDS console at [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/ "https://console.aws.amazon.com/rds/").
2. In the navigation pane, choose **Databases**.
3. Choose the DB cluster on which you want to
   start an activity stream.
4. For **Actions**, choose **Start activity stream**.

The **Start database activity stream:** `name` window appears,
where `name` is your DB cluster. 5. Enter the following settings:

    * For **AWS KMS key**, choose a key from the list of AWS KMS keys.


    ###### Note

     If your Aurora MySQL cluster can't access KMS keys, follow the instructions
     in [Network prerequisites for Aurora MySQL database activity streams](DBActivityStreams.md "DBActivityStreams.md") to enable such
     access first.


    Aurora uses the
     KMS key to encrypt the key that in turn encrypts database activity. Choose a KMS key other than the
     default key. For more information about encryption keys and AWS KMS, see [What is AWS Key Management Service?](../../../kms/latest/developerguide/overview.md "../../../kms/latest/developerguide/overview.md") in the *AWS Key Management Service Developer Guide.*
    * For **Database activity stream mode**, choose **Asynchronous** or
     **Synchronous**.


    ###### Note

    This choice applies only to Aurora PostgreSQL. For Aurora MySQL, you can use only asynchronous mode.
    * Choose **Immediately**.


    When you choose **Immediately**, the DB
     cluster restarts right away. If you choose
     **During the next maintenance window**, the DB
     cluster doesn't restart right away. In
     this case, the database activity stream doesn't start until the next maintenance window.

6. Choose **Start database activity stream**.

The status for the DB cluster shows that the activity stream is
starting.

###### Note

If you get the error `You can't start a database activity stream in this
 configuration`, check [Supported DB instance classes for database activity streams](DBActivityStreams.md#DBActivityStreams.Overview.requirements.classes "DBActivityStreams.md#DBActivityStreams.Overview.requirements.classes") to see whether
your DB cluster is using a supported instance class.

AWS CLITo start database activity streams for a DB cluster
, configure the DB cluster using the [start-activity-stream](../../../cli/latest/reference/rds/start-activity-stream.md "../../../cli/latest/reference/rds/start-activity-stream.md")
AWS CLI command.

- `--resource-arn `arn`` – Specifies the Amazon Resource Name (ARN) of
  the DB cluster.
- `--mode `sync-or-async`` – Specifies either
synchronous (`sync`) or asynchronous (`async`) mode. For Aurora PostgreSQL, you can choose either value. For Aurora MySQL,
specify `async`.
- `--kms-key-id `key`` – Specifies the KMS key identifier for encrypting messages in the database
  activity stream. The AWS KMS key identifier is the key ARN, key ID, alias ARN, or alias name for the AWS KMS key.

The following example starts a database activity stream for a
DB cluster
in asynchronous mode.

For Linux, macOS, or Unix:

```
aws rds start-activity-stream \
    --mode async \
    --kms-key-id `my-kms-key-arn` \
    --resource-arn `my-cluster-arn` \
    --apply-immediately
```

For Windows:

```
aws rds start-activity-stream ^
    --mode async ^
    --kms-key-id `my-kms-key-arn` ^
    --resource-arn `my-cluster-arn` ^
    --apply-immediately
```

Amazon RDS API
To start database activity streams for a DB cluster,
configure the cluster using the
[StartActivityStream](../APIReference/API_StartActivityStream.md "../APIReference/API_StartActivityStream.md") operation.

Call the action with the parameters below:

- `Region`
- `KmsKeyId`
- `ResourceArn`
- `Mode`

###### Note

If you get an error stating that you can't start a database activity stream with the current version of your Aurora PostgreSQL database,
apply the latest patch for Aurora PostgreSQL before starting a database activity stream. For information about upgrading your Aurora PostgreSQL
database, see [Upgrading Amazon Aurora DB clusters](Aurora.VersionPolicy.md "Aurora.VersionPolicy.md").

Following are the minimum patch versions to start database activity streams with Aurora PostgreSQL.

- 3.4.15 (11.9.15), 11.21.10
- 12.9.15, 12.15.9, 12.16.10, 12.17.7, 12.18.5, 12.19.4, 12.20.3, 12.22.3
- 13.9.12, 13.11.9, 13.12.10, 13.13.7, 13.14.5, 13.15.4, 13.16.3, 13.18.3
- 14.6.12, 14.8.9, 14.9.10, 14.10.7, 14.11.5, 14.12.4, 14.13.3, 14.15.3
- 15.3.9, 15.4.10, 15.5.7, 15.6.5, 15.7.4, 15.8.3, 15.10.3
- 16.1.7, 16.2.5, 16.3.4, 16.4.3, 16.6.3
