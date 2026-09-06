

# Recovery by initiating a table restore
<a name="bp-pitr-recovery-table-restore"></a>

With PITR, you can restore a table to any specific second in the PITR recovery window. The PITR recovery window begins when PITR is enabled and holds up to 35 days of history. You can also configure it for a shorter duration.

Consider the following when you initiate a full PITR table restore:
+ The restore creates a new table. A table restore action does not operate in-place on top of the original table. For in-place options, see [Recovery by rolling back unwanted writes in-place](bp-pitr-recovery-inplace-rollback.md).
+ You can restore to a new table in the same Region or to a different Region. Restoring to a different Region incurs data transfer charges.
+ You can restore the table with or without secondary indexes. Restoring without secondary indexes can be faster and more cost efficient.
+ The restore can take several hours to complete. Restore time varies based on multiple factors and doesn't always correlate with table size.

After the PITR table restore, you can put the new table into service as a full replacement for the original. You can also compare it to the original table to find differences. For a simpler approach, see [Recovery by rolling back unwanted writes in-place](bp-pitr-recovery-inplace-rollback.md).

Consider the following when you put a restored table into service:
+ For infrastructure as code environments (AWS CloudFormation, AWS Cloud Development Kit (AWS CDK), Terraform), adopt the restored table into your IaC environment to bring it under management.
+ Update client connections to refer to the new table by its new name.
+ Re-add stream settings if they were on the original. The DynamoDB stream name includes the time of stream creation, so the new stream has a different name than the old stream. Update any references to the old stream name in IAM or in downstream consumer code.
+ Re-enable PITR on the new table if it was on the original.
+ Re-enable deletion protection on the new table if it was on the original.
+ Re-add tags to the new table if tags were on the original.
+ Re-add the resource-based policies on the new table if RBPs were on the original.
+ Update any cross-account access IAM policies that reference the original table.
+ Adjust the auto scaling settings on the new table.
+ Set the TTL attribute on the new table if TTL was on the original.
+ Adjust the table class on the new table if the original had a custom table class.
+ Review the warm throughput settings on the new table and raise the read and write values if necessary.
+ Add replicas for the new table to match the original table if it was a global table.
+ Delete the original table after the restored table has been fully configured and put into service.

If restoring an MRSC global table, the newly restored table cannot be made into an MRSC table because only empty tables can be made into MRSC tables. One solution is to restore the table and then copy the data from the restored table into an empty MRSC table.