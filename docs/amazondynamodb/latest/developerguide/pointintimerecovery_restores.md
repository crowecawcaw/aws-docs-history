# Restore a table in DynamoDB

You can restore a DynamoDB table from your PITR backup or your on-demand backups using the
AWS Management Console, the AWS Command Line Interface (AWS CLI), or the DynamoDB API. The recovery process
restores to a new DynamoDB table.

## Restoring a table using point-in-time

recovery

You can restore your table to any point in time up till the
`EarliestRestoreableDateTime`.

###### Important

If you disable point-in-time recovery and later enable it on a table, you reset the start
time for which you can recover that table. As a result, you can only immediately restore that
table using the `LatestRestorableDateTime`.

When you restore using point-in-time recovery, DynamoDB restores your table data to the state
based on the selected date and time (day:hour:minute:second) to a new table. You restore a table
without consuming any provisioned throughput on the table. You can do a full table restore using
point-in-time recovery, or you can configure the destination table settings. You can change the
following table settings on the restored table:

- Global secondary indexes (GSIs)
- Local secondary indexes (LSIs)
- Billing mode
- Provisioned read and write capacity
- Encryption settings

###### Important

When you do a full table restore, the destination table is set with the same provisioned
read capacity units and write capacity units that the source table had when the backup was
requested. For example, suppose that a table's provisioned throughput was recently lowered to 50
read capacity units and 50 write capacity units. You then restore the table's state to three
weeks ago, at which time its provisioned throughput was set to 100 read capacity units and 100
write capacity units. In this case, DynamoDB restores your table data to that point in time with
the provisioned throughput from that time (100 read capacity units and 100 write capacity
units).

You can also restore your DynamoDB table data across AWS Regions such that the restored table
is created in a different Region from where the source table resides. You can do cross-Region
restores between AWS commercial Regions, AWS China Regions, and AWS GovCloud (US). You pay only
for the data you transfer out of the source Region and for restoring to a new table in the
destination Region.

###### Note

Cross-Region restore isn't supported if the source or destination Region is Asia Pacific
(Hong Kong) or Middle East (Bahrain).

Restores can be faster and more cost-efficient if you exclude some or all indexes from being
created on the restored table. You must manually set the following on the restored table:

- Auto scaling policies
- AWS Identity and Access Management policies
- Amazon CloudWatch Events metrics and alarms
- Tags
- Stream settings
- Time to Live (TTL) settings
- Point-in-time recovery settings

The time it takes you to restore a table varies based on multiple factors and isn't always
correlated with the size of the table.
