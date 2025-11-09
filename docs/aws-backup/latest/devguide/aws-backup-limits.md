# AWS Backup quotas

The following quotas apply when working with AWS Backup.

###### Quotas

- [Backup](#aws-backup-quotas-table "#aws-backup-quotas-table")
- [Backup index and search quotas](#aws-backup-search-quotas-table "#aws-backup-search-quotas-table")
- [Policy quotas](#aws-backup-policies-quotas-table "#aws-backup-policies-quotas-table")
- [Amazon Timestream resource quotas](#backup-timestream-quotas-table "#backup-timestream-quotas-table")
- [AWS Backup Audit Manager quotas](#backup-audit-manager-quotas-table "#backup-audit-manager-quotas-table")
- [Restore testing plan quotas](#backup-restore-testing-quotas-table "#backup-restore-testing-quotas-table")
- [AWS Backup gateway quotas](#backup-gateway-quotas-table "#backup-gateway-quotas-table")
- [Related quotas](#backup-related-quotas "#backup-related-quotas")

## Backup

| Name                                                                                                                         | Default   | Adjustable                                                                        |
| ---------------------------------------------------------------------------------------------------------------------------- | --------- | --------------------------------------------------------------------------------- |
| Total vaults (backup and logically air-gapped) per Region per account                                                        | 300       | Yes                                                                               |
| Recovery points per backup vault                                                                                             | 1,000,000 | Yes                                                                               |
| Backup plans per Region per account                                                                                          | 300       | Yes                                                                               |
| Versions per backup plan                                                                                                     | 2,000     | Yes                                                                               |
| Resource assignments per backup plan                                                                                         | 100       | No                                                                                |
| Amazon S3 buckets per account                                                                                                | 100       | Yes                                                                               |
| Concurrent cross-Region copy jobs per account in destination Region                                                          | 1002      | No                                                                                |
| Additional cross-Region copy jobs per vault in a destination Region<br>after the limit in row above entry has been reached.1 | 52        | No                                                                                |
| Concurrent cross-account copies that can be made of the same resource to the same destination<br>Region                      | 30        | No                                                                                |
| Concurrent backup and copy jobs per resource                                                                                 | 1         | No                                                                                |
| Tags per resource selection in a cross account backup policy                                                                 | 30        | No. Include additional tags using multiple resource assignments or backups plans. |
| Hypervisors                                                                                                                  | 10        | No                                                                                |
| Legal holds per account                                                                                                      | 50        | No                                                                                |
| Nested backup layers of application stacks                                                                                   | 10        | No                                                                                |

1The limit for concurrent copy jobs from one Region to
another Region is 100 per account per Region. Once this limit is reached, if a specific
vault in the destination Region has fewer than 5 concurrent copy jobs, new copy jobs
can begin, up to a maximum of 5 concurrently.

2Limit only apply to resource types [fully managed by AWS Backup](backup-feature-availability.md "backup-feature-availability.md").

## Backup index and search quotas

| Name                                                                                                                                                         | Default | Adjustable |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------- | ---------- |
| Concurrent indexing jobs in account (most AWS Regions)                                                                                                       | 40      | Yes        |
| Concurrent indexing jobs in account in Asia Pacific (Malaysia),<br>Canada (Central), Asia Pacific (Thailand), and<br>Mexico (Central) AWS Regions.           | 10      | Yes        |
| Concurrent indexing jobs for each resource                                                                                                                   | 5       | No         |
| Concurrent on-demand indexing job                                                                                                                            | 1       | No         |
| Concurrent search jobs in account                                                                                                                            | 10      |            |
| Concurrent export jobs                                                                                                                                       | 5       |            |
| Number of recovery points included in search job                                                                                                             | 20      |            |
| Concurrent Amazon EBS file level restore jobs (most AWS Regions)                                                                                             | 25      |            |
| Concurrent Amazon EBS file level restore jobs in Asia Pacific (Malaysia),<br>Canada (Central), Asia Pacific (Thailand), and<br>Mexico (Central) AWS Regions. | 5       |            |

## Policy quotas

| Name                                                 | Default | Adjustable |
| ---------------------------------------------------- | ------- | ---------- |
| Resource assignments per backup plan                 | 100     | No         |
| Tags in a resource selection                         | 30      | No         |
| Resource selections that use tags in a plan          | 10      | No         |
| Backup plan rules in a plan                          | 10      | No         |
| Tags added to a recovery point                       | 10      | No         |
| Copy actions per backup rule                         | 5       | No         |
| Conditions in a resource assignment in a backup plan | 30      | No         |

## Amazon Timestream resource quotas

| Name                                           | Default | Adjustable |
| ---------------------------------------------- | ------- | ---------- |
| Concurrent Timestream backup jobs per account  | 4       | Yes        |
| Concurrent Timestream restore jobs per account | 1       | Yes        |

## AWS Backup Audit Manager quotas

| Name                                                                                                                                              | Default | Adjustable |
| ------------------------------------------------------------------------------------------------------------------------------------------------- | ------- | ---------- |
| Frameworks per account per Region                                                                                                                 | 15      | Yes        |
| Controls per account per Region                                                                                                                   | 50      | Yes        |
| Report plans per account                                                                                                                          | 20      | Yes        |
| Frameworks per report plan                                                                                                                        | 1,000   | No         |
| [Number of accounts] multiplied by [number of Regions in a report plan]                                                                           | 300     | No         |
| [Number of accounts] multiplied by [number of Regions in a report plan]<br>multiplied by [number of daily jobs plus evaluations in a report plan] | 100,000 | No         |

## [Restore testing](restore-testing.md "restore-testing.md") plan quotas

| Name                                                                    | Default                                                       | Adjustable |
| ----------------------------------------------------------------------- | ------------------------------------------------------------- | ---------- |
| Restore testing plans                                                   | 100                                                           | No         |
| Tags per plan                                                           | 50                                                            | No         |
| Selections per plan                                                     | 30                                                            | No         |
| ARNs per restore testing selection                                      | 30                                                            | No         |
| Conditions per selection (both `StringEquals` and<br>`StringNotEquals`) | 30                                                            | No         |
| Vault selectors per restore testing selection                           | 30                                                            | No         |
| Maximum value (in days) of selection window                             | 365 days                                                      | No         |
| Boundaries of start window hours                                        | Minimum: 1 hour; Maximum: 168 hours                           | No         |
| Maximum character length of restore testing plan name                   | 50 characters (alphanumeric and underscores, no white spaces) | No         |
| Maximum character length of restore testing selection name              | 50 characters (alphanumeric and underscores, no white spaces) | No         |

Each resource type has a limit on the number of concurrent restore jobs that can exist
at one time for restore jobs that are created through a restore testing plan. Once this
limit is reached, no new restore jobs for that resource type will be created until a job
in a state of `RUNNING` transitions to `COMPLETED`.

If a scheduled restore job did not start due to this quota, that job will result in a
`FAILED` status with the status message `"Restore job was unable to
 start within the specified start window. Try increasing your start window."`.
If you receive a failed job with this status message, the best practice is to first
increase your start window with sufficient time to allow jobs to finish. Then, retry the
jobs.

Note quotas do not apply to on-demand restore jobs, but to restore jobs created by a
[restore testing plan](restore-testing.md#restore-testing-create "restore-testing.md#restore-testing-create"). For some
resource types, you may request an increase in the quota limit.

| Name              | Default | Adjustable |
| ----------------- | ------- | ---------- |
| Amazon Aurora     | 40      | Yes        |
| Amazon DocumentDB | 40      | Yes        |
| Amazon DynamoDB   | 40      | No         |
| Amazon EBS        | 100     | Yes        |
| Amazon EC2        | 100     | Yes        |
| Amazon EFS        | 30      | Yes        |
| Amazon FSx        | 40      | Yes        |
| Amazon Neptune    | 40      | Yes        |
| Amazon RDS        | 40      | Yes        |
| Amazon S3         | 30      | Yes        |

## AWS Backup gateway quotas

| Name                               | Default | Adjustable                                                    |
| ---------------------------------- | ------- | ------------------------------------------------------------- |
| Backup or restore jobs per gateway | 4       | No. Create more gateways and connect them to your hypervisor. |

## Related quotas

There are [quotas on a single resource assignment](assigning-resources.md#assigning-resources-quotas "assigning-resources.md#assigning-resources-quotas") in a single backup rule. You can create a backup plan
with multiple backup rules.

When you manage backups across multiple accounts using AWS Organizations, you might encounter
quotas that AWS Organizations imposes. For these quotas, see [Quotas for
AWS Organizations](../../../organizations/latest/userguide/orgs_reference_limits.md "../../../organizations/latest/userguide/orgs_reference_limits.md") in the _AWS Organizations User Guide_.

You might also encounter quotas imposed by a AWS Backup-supported service,
including the following:

- [Amazon Elastic File System](../../../efs/latest/ug/limits.md "../../../efs/latest/ug/limits.md")
- [Amazon Elastic Block Store](../../../ebs/latest/userguide/ebs-resource-quotas.md "../../../ebs/latest/userguide/ebs-resource-quotas.md")
- [Amazon RDS](../../../AmazonRDS/latest/UserGuide/CHAP_Limits.md "../../../AmazonRDS/latest/UserGuide/CHAP_Limits.md")
- [Amazon Aurora](../../../AmazonRDS/latest/AuroraUserGuide/CHAP_Limits.md "../../../AmazonRDS/latest/AuroraUserGuide/CHAP_Limits.md")
- [Amazon EC2](../../../AWSEC2/latest/UserGuide/ec2-resource-limits.md "../../../AWSEC2/latest/UserGuide/ec2-resource-limits.md")
- [AWS Storage Gateway](../../../storagegateway/latest/userguide/resource-gateway-limits.md "../../../storagegateway/latest/userguide/resource-gateway-limits.md")
- [Amazon DynamoDB](../../../amazondynamodb/latest/developerguide/ServiceQuotas.md "../../../amazondynamodb/latest/developerguide/ServiceQuotas.md")
- [Amazon FSx for Lustre](../../../fsx/latest/LustreGuide/limits.md "../../../fsx/latest/LustreGuide/limits.md")
- [Amazon FSx for Windows File Server](../../../fsx/latest/WindowsGuide/managing-user-quotas.md "../../../fsx/latest/WindowsGuide/managing-user-quotas.md")
- [Amazon DocumentDB](../../../documentdb/latest/developerguide/limits.md "../../../documentdb/latest/developerguide/limits.md")
- [Amazon Neptune](../../../neptune/latest/userguide/limits.md "../../../neptune/latest/userguide/limits.md")
- [Amazon Simple Storage Service](../../../general/latest/gr/s3.md#limits_s3 "../../../general/latest/gr/s3.md#limits_s3")
- [Amazon Timestream](../../../timestream/latest/developerguide/backups-limits.md "../../../timestream/latest/developerguide/backups-limits.md")
