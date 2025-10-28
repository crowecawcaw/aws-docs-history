# AWS Billing reports for Amazon EFS

Your monthly bill from AWS separates your usage information and cost by AWS service and
function. There are several AWS billing reports available: the monthly report, the cost
allocation report, and detailed billing reports. For more information, see [Understanding
your bill](../../../awsaccountbilling/latest/aboutv2/getting-viewing-bill.md "../../../awsaccountbilling/latest/aboutv2/getting-viewing-bill.md") in the _AWS Billing_ User Guide.

For more detailed reports about your Amazon EFS storage usage, use AWS Data Exports to create exports of
the AWS Cost and Usage Report (AWS CUR). With AWS CUR 2.0, you publish your AWS billing reports to an
Amazon Simple Storage Service (Amazon S3) bucket that you own. The Amazon EFS usage report lists operations by usage type and
AWS Region. For more
information, see [Cost and Usage Report (CUR) 2.0](../../../cur/latest/userguide/table-dictionary-cur2.md "../../../cur/latest/userguide/table-dictionary-cur2.md")
in the _AWS Data Exports User Guide_.

EFS file systems are billed based on the following categories of usage.

- Storage (per gigabyte [GB]) – The amount of data stored in your EFS
  file systems per month, with different prices depending on the storage class
  (EFS Standard, EFS Infrequent Access (IA) and
  EFS Archive).
- Throughput (per GB or mebibytes per second [MiBps]) – The amount of data transferred
  (read/write operations) or the amount that exceeds your provisioned amount, depending on
  the file system's throughput, per month.
- Data access and transition (per MiBps) – The amount of data read and
  transferred to the EFS Infrequent Access (IA) and
  EFS Archive storage classes per month.
- Backup storage (per GB) – The amount of storage space consumed by backups per month.
  Increasing your backup retention period or taking additional user-initiated volume backups
  increases the amount of backup storage your file system consumes. For more information,
  see [Backing up EFS file systems](awsbackup.md "awsbackup.md")
- Replication (per GB) – The prevailing storage and read, write, and tiering activity
  rates for your source and destination EFS file systems, as well as any
  applicable charges for data transfer activity between them, per month.
  For detailed information about Amazon EFS charges, see [Amazon EFS Pricing](https://aws.amazon.com/efs/pricing/ "https://aws.amazon.com/efs/pricing/").

For information about understanding the codes and abbreviations used in the billing and
usage reports for Amazon EFS, see [Understanding billing and
usage reports for Amazon EFS](billing-usage-reports-understand.md "billing-usage-reports-understand.md").
