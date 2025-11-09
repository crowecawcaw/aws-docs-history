# Understanding billing and

usage reports for Amazon EFS

Amazon EFS billing and usage reports use codes and abbreviations. For usage types in the table
that follows, replace `region` with abbreviations from
this list:

- **APE1:** Asia Pacific (Hong Kong)
- **APN1:** Asia Pacific (Tokyo)
- **APN2:** Asia Pacific (Seoul)
- **APN3:** Asia Pacific (Osaka)
- **APS1:** Asia Pacific (Singapore)
- **APS2:** Asia Pacific (Sydney)
- **APS3:** Asia Pacific (Mumbai)
- **APS4:** Asia Pacific (Jakarta)
- **APS5:** Asia Pacific (Hyderabad)
- **APS6:** Asia Pacific (Melbourne)
- **CAN1:** Canada (Central)
- **CAN2:** Canada West (Calgary)
- **CNN1:** China (Beijing)
- **CNW1:** China (Ningxia)
- **AFS1:** Africa (Cape Town)
- **EUC2:** Europe (Zurich)
- **EUN1:** Europe (Stockholm)
- **EUS2:** Europe (Spain)
- **EUC1:** Europe (Frankfurt)
- **EU:** Europe (Ireland)
- **EUS1:** Europe (Milan)
- **EUW2:** Europe (London)
- **EUW3:** Europe (Paris)
- **ILC1:** Israel (Tel Aviv)
- **MEC1:** Middle East (UAE)
- **MES1:** Middle East (Bahrain)
- **SAE1:** South America (São Paulo)
- **UGW1:** AWS GovCloud (US-West)
- **UGE1:** AWS GovCloud (US-East)
- **USE1 (or no prefix):** US East (N. Virginia)
- **USE2:** US East (Ohio)
- **USW1:** US West (N. California)
- **USW2:** US West (Oregon)
  For information about pricing by AWS Region, see [Amazon EFS Pricing](https://aws.amazon.com/efs/pricing/ "https://aws.amazon.com/efs/pricing/").

The first column in the following table lists usage types that appear in your billing and
usage reports. The typical unit of measurement for data is gigabytes (GB). For provisioned
throughput amount, however, mebibytes per second (MiBps) is used instead.

| Usage types for Amazon EFS                | Usage type                                                                                          | CloudWatch metric | Units  | Granularity                                                                                                                                               | Description |
| ----------------------------------------- | --------------------------------------------------------------------------------------------------- | ----------------- | ------ | --------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| ``region`-ArchiveDataAccess-Bytes`        | N/A                                                                                                 | GB                | N/A    | The amount of data that was transferred to or accessed in EFS Archive<br>storage.                                                                         |
| ``region`-ArchiveEarlyDelete-ByteHrs`     | N/A                                                                                                 | GB-Mo             | N/A    | Prorated storage usage for files deleted from EFS Archive storage before the<br>90-day minimum commitment ended.                                          |
| ``region`-ArchiveEarlyDelete-SmallFiles`  | N/A                                                                                                 | GB-Mo             | N/A    | Prorated storage usage for small files (smaller than 128 KB) that were deleted from<br>EFS Archive storage before the 90-day minimum commitment<br>ended. |
| ``region`-ArchiveTimedStorage-ByteHrs`    | [StorageBytes.Archive](efs-metrics.md#archivebytes "efs-metrics.md#archivebytes")                   | GB-Mo             | Hourly | The number of GB-months that data was stored in EFS Archive<br>storage.                                                                                   |
| ``region`-ArchiveTimedStorage-SmallFiles` | [StorageBytes.ArchiveSizeOverhead](efs-metrics.md#archiveoverhead "efs-metrics.md#archiveoverhead") | GB-Mo             | Hourly | The number of GB-months that small objects (smaller than 128 KB) were<br>stored in EFS Archive storage.                                                   |
| ``region`-ETDataAccess-Bytes`             | [TotalIOBytes](efs-metrics.md#totaliobytes "efs-metrics.md#totaliobytes")                           | GB                | Hourly | The amount of data that was written or read for files using Elastic throughput.                                                                           |
| ``region`-IADataAccess-Bytes`             | N/A                                                                                                 | GB                | Hourly | The amount of data that was transferred to or accessed in EFS Infrequent Access<br>(IA) storage.                                                          |
| ``region`-IATimedStorage-ByteHrs`         | [StorageBytes.IA](efs-metrics.md#iabytes "efs-metrics.md#iabytes")                                  | GB-Mo             | Hourly | The number of GB-months that data was stored in EFS<br>IA storage.                                                                                        |
| ``region`-IATimedStorage-ET-ByteHrs`      | [StorageBytes.IA](efs-metrics.md#iabytes "efs-metrics.md#iabytes")                                  | GB-Mo             | Hourly | The number of GB-months that data for files using Elastic throughput was<br>stored in EFS IA storage.                                                     |
| ``region`-IATimedStorage-ET-SmallFiles`   | [StorageBytes.IASizeOverhead](efs-metrics.md#iaoverhead "efs-metrics.md#iaoverhead")                | GB-Mo             | Hourly | The number of GB-months that small files (smaller than 128 KB) were<br>stored in EFS IA storage, for files using Elastic throughput.                      |
| ``region`-IATimedStorage-SmallFiles`      | [StorageBytes.IASizeOverhead](efs-metrics.md#iaoverhead "efs-metrics.md#iaoverhead")                | GB-Mo             | Hourly | The number of GB-months that small files (smaller than 128 KB) were<br>stored in EFS IA storage.                                                          |
| ``region`-IATimedStorage-Z-ByteHrs`       | [StorageBytes.IA](efs-metrics.md#iabytes "efs-metrics.md#iabytes")                                  | GB-Mo             | Hourly | The actual size of data stored in EFS IA storage<br>for One Zone file systems.                                                                            |
| ``region`-IATimedStorage-Z-SmallFiles`    | [StorageBytes.IASizeOverhead](efs-metrics.md#iaoverhead "efs-metrics.md#iaoverhead")                | GB-Mo             | Hourly | The number of GB-months that small files (smaller than 128 KB) were<br>stored in EFS IA storage for One Zone<br>file systems.                             |
| ``region`-IncludedTP-MiBpsHrs`            | [PermittedThroughput](efs-metrics.md#permittedtp "efs-metrics.md#permittedtp")                      | MiBps-Mo          | Hourly | The maximum amount of throughput that a file system can drive.                                                                                            |
| ``region`-ProvisionedTP-MiBpsHrs`         | [PermittedThroughput](efs-metrics.md#permittedtp "efs-metrics.md#permittedtp")                      | MiBps-Mo          | Hourly | For file systems using Provisioned throughput, the<br>throughput provisioned or maximum permitted throughput.                                             |
| ``region`-TimedStorage-ByteHrs`           | [StorageBytes.Standard](efs-metrics.md#standardbytes "efs-metrics.md#standardbytes")                | GB-Mo             | Hourly | The actual total amount of data stored in EFS Standard storage for regional file<br>systems.                                                              |
| ``region`-TimedStorage-Z-ByteHrs`         | [StorageBytes.Standard](efs-metrics.md#standardbytes "efs-metrics.md#standardbytes")                | GB-Mo             | Hourly | The actual total amount of data stored in EFS Standard storage<br>for One Zone file systems.                                                              |

###### Notes

- EFS Archive storage is charged for a minimum storage duration of 90 days,
  even if the data is deleted before 90 days.
- A tiering charge applies to data tiered from EFS Standard storage to
  EFS Infrequent Access (IA) storage, and from EFS IA
  storage to EFS Standard storage.
- EFS IA and EFS Archive storage have a minimum
  billable file size of 128 KiB. Files smaller than 128 KiB can be tiered to these
  storage classes but are charged for 128 KiB of storage at the appropriate storage
  class rate.
- For file systems using Elastic throughput, metadata operations are metered
  in 1 KiB increments after the first 4 KiB and data operations are metered in 1 KiB
  increments after the first 32 KiB.
- Storage usage is calculated in binary gigabytes (GB), where 1 GB is 230 bytes. See [How Amazon EFS reports file system and object
  sizes](metered-sizes.md "metered-sizes.md") for additional details on how storage and throughput usage are
  metered to calculate your Amazon EFS bill.
- GB-Month is derived by taking the total number of GB-hours, aggregating these over the
  course of a month, and then dividing by the number of hours in that month.

## Tracking operations in your usage

reports

Operations describe the action taken on your EFS file system by the
specified usage type. Operations are indicated by self-explanatory codes, such as
`Read` or `Delete`. To see which actions on your file system
generated a specific type of usage, use these codes. When you create a usage report, you
can choose to include **All Operations**, or a specific operation, for
example, `Write`, to report on.
