# Best practices for understanding your AWS billing and usage reports in DynamoDB

This document explains the `UsageType` billing codes for charges related to DynamoDB.

AWS provides cost and usage reports (CUR) that contain data for the
services used. You can use AWS Cost and Usage Report to publish billing reports to Amazon S3 in a CSV format.
When setting up the CUR you can choose to break time periods down by hour, day, or
month, and you can choose if you want to break out usage by resource ID or not. For more
details on generating CUR, please
see [Creating Cost and Usage Reports](../../../cur/latest/userguide/creating-cur.md "../../../cur/latest/userguide/creating-cur.md")

Within the CSV export, you will find relevant attributes listed for each line. The following are
examples of attributes that may be included:

- **lineitem/UsageStartDate:** The start date and time for the line item in UTC, inclusive.
- **lineitem/UsageEndDate:** The end date and time for the corresponding line item in UTC, exclusive.
- **lineitem/ProductCode:** For DynamoDB this will be “AmazonDynamoDB”
- **lineitem/UsageType:** A specific description code for the type of usage, as enumerated in this document
- **lineitem/Operation:** A name that provides context to the charge such as the operation name that incurred the charge (optional).
- **lineitem/ResourceId:** The identifier for the resource that incurred the usage.
  Available if the CUR includes a breakdown by resource ID.
- **lineitem/UsageAmount:** The amount of usage incurred during the specified time period.
- **lineitem/UnblendedCost:** The cost of this usage.
- **lineitem/LineItemDescription:** Textual description of the line item.
  For more information about the CUR data dictionary,
  see [Cost and Usage Report (CUR) 2.0](../../../cur/latest/userguide/table-dictionary-cur2.md "../../../cur/latest/userguide/table-dictionary-cur2.md").
  Note that the exact names vary depending on context.

A `UsageType` is a string with a value such as `ReadCapacityUnit-Hrs`,
`USW2-ReadRequestUnits`, `EU-WriteCapacityUnit-Hrs`, or `USE1-TimedPITRStorage-ByteHrs`. Each
usage type begins with an optional Region prefix. If absent, that indicates the us-east-1
Region. If present, the below table maps the short billing Region code to the conventional
Region code and name.

For example, the usage named `USW2-ReadRequestUnits` indicates read request units
consumed in us-west-2.

| Billing Region Code | Region Code    | Region Name               |
| ------------------- | -------------- | ------------------------- |
| AFS1                | af-south-1     | Africa (Cape Town)        |
| APE1                | ap-east-1      | Asia Pacific (Hong Kong)  |
| APN1                | ap-northeast-1 | Asia Pacific (Tokyo)      |
| APN2                | ap-northeast-2 | Asia Pacific (Seoul)      |
| APN3                | ap-northeast-3 | Asia Pacific (Osaka)      |
| APS1                | ap-southeast-1 | Asia Pacific (Singapore)  |
| APS2                | ap-southeast-2 | Asia Pacific (Sydney)     |
| APS3                | ap-south-1     | Asia Pacific (Mumbai)     |
| APS4                | ap-southeast-3 | Asia Pacific (Jakarta)    |
| APS5                | ap-south-2     | Asia Pacific (Hyderabad)  |
| APS6                | ap-southeast-4 | Asia Pacific (Melbourne)  |
| CAN1                | ca-central-1   | Canada (Central)          |
| EU                  | eu-west-1      | Europe (Ireland)          |
| EUC1                | eu-central-1   | Europe (Frankfurt)        |
| EUC2                | eu-central-2   | Europe (Zurich)           |
| EUN1                | eu-north-1     | Europe (Stockholm)        |
| EUS1                | eu-south-1     | Europe (Milan)            |
| EUS2                | eu-south-2     | Europe (Spain)            |
| EUW1                | eu-west-1      | Europe (Ireland)          |
| EUW2                | eu-west-2      | Europe (London)           |
| EUW3                | eu-west-3      | Europe (Paris)            |
| ILC1                | Il-central-1   | Israel (Tel Aviv)         |
| MEC1                | me-central-1   | Middle East (UAE)         |
| MES1                | me-south-1     | Middle East (Bahrain)     |
| SAE1                | sa-east-1      | South America (São Paulo) |
| USE1 (default)      | us-east-1      | US East (N. Virginia)     |
| USE2                | us-east-2      | US East (Ohio)            |
| UGE1                | us-gov-east-1  | US Government East        |
| UGW1                | us-gov-west-1  | US Government West        |
| USW1                | us-west-1      | US West (N. California)   |
| USW2                | us-west-2      | US West (Oregon)          |

In the following sections, we use `REG-UsageType` pattern when going through the
charges for DynamoDB, where REG specifies the region where usage occurred and usageType is the
code for the type of charge. For example if you see a line item for `USW1-
 ReadCapacityUnit-Hrs` in your CSV file, that means the usage was incurred in US-West-1 for
provisioned read capacity. In that case the listing would say `REG-ReadCapacityUnit-Hrs`.

###### Topics

- [Throughput Capacity](#bp-understanding-billing.throughput "#bp-understanding-billing.throughput")
- [Streams](#bp-understanding-billing.streams "#bp-understanding-billing.streams")
- [Storage](#bp-understanding-billing.storage "#bp-understanding-billing.storage")
- [Backup and Restore](#bp-understanding-billing.backup "#bp-understanding-billing.backup")
- [Data Transfer](#bp-understanding-billing.datatransfer "#bp-understanding-billing.datatransfer")
- [CloudWatch Contributor Insights](#bp-understanding-billing.cw "#bp-understanding-billing.cw")
- [DynamoDB Accelerator (DAX)](#bp-understanding-billing.dax "#bp-understanding-billing.dax")

## Throughput Capacity

**Provisioned Capacity Reads and Writes**

When you create a DynamoDB table in provisioned capacity mode, you specify the read and
write capacity that you expect your application to require. The usage type depends on your
table class (Standard or Standard-Infrequent Access). You provision read and writes based
on consumption rate per second, but the charges are priced per hour based on provisioned
capacity.

| UsageType                    | Units     | Granularity | Description                                                                              |
| ---------------------------- | --------- | ----------- | ---------------------------------------------------------------------------------------- |
| REG-ReadCapacityUnit-Hrs     | RCU-hours | Hour        | Charges for reads in provisioned<br>capacity mode using the Standard<br>table class.     |
| REG-IA-ReadCapacityUnit-Hrs  | RCU-hours | Hour        | Charges for reads in provisioned<br>capacity mode using the<br>Standard-IA table class.  |
| REG-WriteCapacityUnit-Hrs    | WCU-hours | Hour        | Charges for writes in provisioned<br>capacity mode using the Standard<br>table class.    |
| REG-IA-WriteCapacityUnit-Hrs | WCU-hours | Hour        | Charges for writes in provisioned<br>capacity mode using the<br>Standard-IA table class. |

**Reserved Capacity Reads and Writes**

With reserved capacity, you pay a one-time upfront fee and commit to a minimum
provisioned usage level over a period of time. Reserved capacity is billed at a discounted
hourly rate. Any capacity that you provision in excess of your reserved capacity is billed at
standard provisioned capacity rates. Reserved capacity is available for single-region,
provisioned read and write capacity units (RCU and WCU) on DynamoDB tables that use
the standard table class. Both 1-year and 3-year reserved capacity are billed using the
same SKUs.

| UsageType                     | Units     | Granularity                 | Description                                                                                                                                                                                                                                                                |
| ----------------------------- | --------- | --------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| REG-HeavyUsage:dynamodb.read  | RCU-hours | Up-front<br>then<br>monthly | Charges for reserved capacity reads:<br>a one-time up-front charge and a<br>monthly charge at the start of each<br>month covering all the discounted<br>committed RCU-hours during the<br>month. Will have matching zero-cost<br>REG-ReadCapacityUnit-Hrs line<br>items.   |
| REG-HeavyUsage:dynamodb.write | WCU-hours | Up-front<br>then<br>monthly | Charges for reserved capacity writes:<br>a one-time up-front charge and a<br>monthly charge at the start of each<br>month covering all the discounted<br>committed WCU-hours during the<br>month. Will have matching zero-cost<br>REG-WriteCapacityUnit-Hrs line<br>items. |

**On-Demand Capacity Reads and Writes**

When you create a DynamoDB table in on-demand capacity mode, you pay only for the
reads and writes your application performs. The prices for read and write requests depend on
your table class.

| UsageType                | Units | Granularity | Description                                                                       |
| ------------------------ | ----- | ----------- | --------------------------------------------------------------------------------- |
| REG-ReadRequestUnits     | RRUs  | Unit        | Charges for reads in on-demand<br>capacity mode with Standard table<br>class.     |
| REG-IA-ReadRequestUnits  | RRUs  | Unit        | Charges for reads in on-demand<br>capacity mode with Standard-IA table<br>class.  |
| REG-WriteRequestUnits    | WRUs  | Unit        | Charges for writes in on-demand<br>capacity mode with Standard table<br>class.    |
| REG-IA-WriteRequestUnits | WRUs  | Unit        | Charges for writes in on-demand<br>capacity mode with Standard-IA table<br>class. |

**Global Tables Reads and Writes**

DynamoDB charges for global tables usage based on the resources used on each replica
table. For provisioned global tables, write requests for global tables are measured in
replicated WCUs (rWCU) instead of standard WCUs and writes to global secondary indexes
in global tables are measured in WCUs. For on-demand global tables, write
requests are measured in replicated WRUs (rWRU) instead of standard WRUs. The number
of rWCUs or rWRUs consumed for replication depends on the version of global tables you
are using. The pricing depends on your table class.

Writes to global secondary indexes (GSIs) are billed using standard write units (WCUs and
WRUs). Read requests and data storage are billed identically to single-region tables.

If you add a table replica to create or extend a global table in new Regions, DynamoDB
charges for a table restore in the added Regions per gigabyte of data restored. Restored
Data is charged as REG-RestoreDataSize-Bytes. Please refer to
[Backup and restore for DynamoDB](Backup-and-Restore.md "Backup-and-Restore.md")
for details. Cross-Region replication and adding replicas to tables that contain data
also incur charges for data transfer out.

When you select on-demand capacity mode for your DynamoDB global tables, you pay only
for the resources your application uses on each replica table.

| UsageType                        | Units      | Granularity | Description                                          |
| -------------------------------- | ---------- | ----------- | ---------------------------------------------------- |
| REG-ReplWriteCapacityUnit-Hrs    | rWCU-hours | Hour        | Global table, provisioned, Standard<br>table class.  |
| REG-IA-ReplWriteCapacityUnit-Hrs | rWCU-hours | Hour        | Global table, provisioned, Standard-IA table class.  |
| REG-ReplWriteRequestUnits        | rWRU       | Unit        | Global table, on-demand, Standard<br>table class.    |
| REG-IA-ReplWriteRequestUnits     | rWRU       | Unit        | Global table, on-demand, Standard-<br>IA table class |

## Streams

DynamoDB has two streaming technologies, DynamoDB Streams and Kinesis. Each have separate
pricing.

DynamoDB Streams charges for reading data in read request units. Each `GetRecords` API
call is billed as a streams read request. You are not charged for `GetRecords` API calls
invoked by AWS Lambda as part of DynamoDB triggers or by DynamoDB global tables as
part of replication.

| UsageType                 | Units | Granularity | Description                                 |
| ------------------------- | ----- | ----------- | ------------------------------------------- |
| REG-Streams-RequestsCount | Count | Unit        | Read request units for DynamoDB<br>Streams. |

Amazon Kinesis Data Streams charges in change data capture units. DynamoDB charges
one change data capture unit for each write (up to 1 KB). For items larger than 1 KB, additional
change data capture units are required. You pay only for the writes your application performs
without having to manage throughput capacity on the table.

| UsageType                          | Units     | Granularity | Description                                            |
| ---------------------------------- | --------- | ----------- | ------------------------------------------------------ |
| REG-ChangeDataCaptureUnits-Kinesis | CDC Units | Unit        | Change data capture units for<br>Kinesis Data Streams. |

## Storage

DynamoDB measures the size of your billable data by adding the raw byte size of your data
plus a per-item storage overhead that depends on the features you have enabled.

###### Note

Storage usage values in the CUR will be higher compared with the storage
values when using `DescribeTable`, because `DescribeTable` does not include the per-item storage
overhead.

Storage is calculated hourly but priced monthly as calculated from an average of the hourly
charges.

Although the storage `UsageType` uses `ByteHrs` as a suffix, storage usage
in the CUR is measured in GB and priced by GB-month.

| UsageType                       | Units | Granularity | Description                                                                                                    |
| ------------------------------- | ----- | ----------- | -------------------------------------------------------------------------------------------------------------- |
| REG-TimedStorage-ByteHrs        | GB    | Month       | Amount of storage used by your<br>DynamoDB tables and indexes, for<br>tables with the Standard table class.    |
| REG-IA-TimedStorage-<br>ByteHrs | GB    | Month       | Amount of storage used by your<br>DynamoDB tables and indexes, for<br>tables with the Standard-IA table class. |

## Backup and Restore

DynamoDB offers two types of backups: Point In Time Recovery (PITR) backups and on-
demand backups. Users can also restore from those backups into DynamoDB tables. The
charges below refers to both backups and restores.

Backup storage charges are incurred on the first of the month with adjustments made
throughout the month as backups are added or removed.
See the [Understanding Amazon
DynamoDB On-demand Backups and Billing](https://repost.aws/articles/AR74LYumctRa-t7Z87uwKrlw "https://repost.aws/articles/AR74LYumctRa-t7Z87uwKrlw") blog for more information

| UsageType                      | Units | Granularity | Description                                                                                                                                                                                                                                              |
| ------------------------------ | ----- | ----------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| REG-TimedBackupStorage-ByteHrs | GB    | Month       | The storage consumed by on-demand<br>backups of your DynamoDB tables and<br>Local Secondary Indexes.                                                                                                                                                     |
| TimedPITRStorage-ByteHrs       | GB    | Month       | The storage used by point-in-time<br>recovery (PITR) backups. DynamoDB<br>monitors the size of your PITR-enabled<br>tables continuously throughout the<br>month to determine your backup<br>charges and bills for storage as long as<br>PITR is enabled. |
| REG-RestoreDataSize-Bytes      | GB    | Size        | The total size of data restored<br>(including table data, local secondary<br>indexes and global secondary indexes)<br>measured in GB from DynamoDB<br>backups.                                                                                           |

### AWS Backup

AWS Backup is a fully managed backup service that makes it easy to centralize and
automate the backup of data across AWS services in the cloud as well as on premises.
AWS Backup is charged for storage (warm or cold storage), restoration activities,
and cross-Region data transfer. The following `UsageType` charges appear under
the “AWSBackup” ProductCode rather than “AmazonDynamoDB”.

| UsageType                            | Units | Granularity | Description                                                                                                                                                                                                                                                                                                   |
| ------------------------------------ | ----- | ----------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| REG-WarmStorage-<br>ByteHrs-DynamoDB | GB    | Month       | The storage used by DynamoDB<br>backups managed by AWS Backup<br>throughout the month, measured in<br>GB-Month.                                                                                                                                                                                               |
| REG-CrossRegion-WarmBytes-DynamoDB   | GB    | Size        | The data transferred to a different<br>AWS Region either within the same<br>account or to a different AWS account.<br>Cross-Region transfers charges occur<br>when copying backups from one<br>Region to another Region. The<br>charge is always billed to the account<br>where the data is transferred from. |
| REG-Restore-WarmBytes-DynamoDB       | GB    | Size        | The total size of the data restored from<br>warm storage, measured in GB.                                                                                                                                                                                                                                     |
| REG-ColdStorage-ByteHrs-DynamoDB     | GB    | Month       | The cold storage used by DynamoDB<br>backups managed by AWS Backup<br>throughout the month, measured in<br>GB-Month.                                                                                                                                                                                          |
| REG-Restore-ColdBytes-DynamoDB       | GB    | Month       | The total size of the data restored from<br>cold storage, measured in GB.                                                                                                                                                                                                                                     |

### Export and Import

You can export data from DynamoDB to Amazon S3 or import data from Amazon S3 to a new DynamoDB
table.

Although the `UsageType` uses `Bytes` as a suffix, export and
import usage in the CUR is measured and priced in GB.

| UsageType                           | Units | Granularity | Description                                                                                                                                                                                                                                   |
| ----------------------------------- | ----- | ----------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| REG-ExportDataSize-Bytes            | GB    | Size        | The charge for exporting data to S3.<br>DynamoDB charges for data you<br>export based on the size of the<br>DynamoDB base table (table data and<br>local secondary indexes) at the<br>specified point in time when the export<br>was created. |
| REG-ImportDataSize-Bytes            | GB    | Size        | The charge for importing data from S3.<br>The size is calculated based on the<br>uncompressed object size of the data<br>within Amazon S3. There are no extra<br>charges for importing to tables with<br>GSIs.                                |
| REG-IncrementalExportDataSize-Bytes | GB    | Size        | The charge for size of the data<br>processed from the continuous backup<br>to produce incremental exports.                                                                                                                                    |

## Data Transfer

Data transfer activity may appear associated with the DynamoDB service. DynamoDB does
not charge for inbound data transfer, and it does not charge for data transferred between
DynamoDB and other AWS services within the same AWS Region (in other words, $0.00 per
GB). Data transferred across AWS Regions (such as between DynamoDB in the US East [N.
Virginia] Region and Amazon EC2 in the EU [Ireland] Region) is charged on both sides of the
transfer.

| UsageType                  | Units | Granularity | Description                                            |
| -------------------------- | ----- | ----------- | ------------------------------------------------------ |
| REG-DataTransfer-In-Bytes  | GB    | Units       | Data transferred in to DynamoDB from<br>the internet.  |
| REG-DataTransfer-Out-Bytes | GB    | Units       | Data transferred out from DynamoDB<br>to the internet. |

## CloudWatch Contributor Insights

CloudWatch Contributor Insights for DynamoDB is a diagnostic tool for identifying the most
frequently accessed and throttled keys in your DynamoDB table. The following
`UsageType` charges appear under the “AmazonCloudWatch” ProductCode rather than “AmazonDynamoDB”.

| UsageType                       | Units               | Granularity | Description                                                                                                                                                                                                                                                                                 |
| ------------------------------- | ------------------- | ----------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| REG-CW:ContributorEventsManaged | Events<br>processed | Units       | The amount of DynamoDB events<br>processed. For example for a table<br>with CloudWatch Contributor Insights<br>enabled, anytime an item is read or<br>written, it’s counted as one event. If<br>the table has a sort key, it results in<br>charges for two events.                          |
| REG-CW:ContributorRulesManaged  | Rule count          | Month       | DynamoDB creates rules to identify<br>most accessed items and most<br>throttled keys when you enable Cloud<br>Watch Contributor Insights. This<br>charge is incurred for the rules added<br>for each entity (tables and GSIs)<br>configured for logging CloudWatch<br>contributor insights. |

## DynamoDB Accelerator (DAX)

DynamoDB Accelerator (DAX) is billed by the hour based on the instance type selected for
the service. The charges below refers to the DynamoDB Accelerator instances provisioned.
The following `UsageType` charges appear under the “AmazonDAX” ProductCode rather than “AmazonDynamoDB”.

| UsageType                        | Units     | Granularity | Description                                                                                                                                                                                                                                                                                                                                                                            |
| -------------------------------- | --------- | ----------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| REG-NodeUsage:dax-<INSTANCETYPE> | Node-hour | Hour        | The hourly usage of a particular<br>instance type. Pricing is per node-hour<br>consumed, from the time a node is<br>launched until it is terminated. Each<br>partial node-hour consumed will be<br>billed as a full hour. DAX charges for<br>each node in a DAX cluster. If you<br>have a cluster with multiple nodes, you<br>would see multiple line items in your<br>billing report. |

The instance type will be one of the values from the following list.
For details about node types, see [Nodes](DAX.concepts.md#DAX.concepts.nodes "DAX.concepts.md#DAX.concepts.nodes").

- r3.2xlarge, r4.8xlarge, or r5.8xlarge
- r3.4xlarge, r4.large, or r5.large
- r3.8xlarge, r4.xlarge, or r5.xlarge
- r3.2xlarge, r5.12xlarge, or t2.medium
- r3.4xlarge, r4.large, or r5.large
- r3.xlarge, r5.16xlarge, or t2.small
- r4.16xlarge, r5.24xlarge, or t3.medium
- r4.2xlarge, r5.2xlarge, or t3.small
- r4.4xlarge or r5.4xlarge
