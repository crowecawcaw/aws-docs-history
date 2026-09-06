

# Best practices for PITR recovery in DynamoDB
<a name="bp-pitr-recovery"></a>

The following are the best practices for using point-in-time recovery (PITR) to return a table to a previous state.

Use these best practices if you notice mistaken writes to your table that you want to reverse. You can either restore the full table from a point in time, or roll back specific unwanted writes in-place.

**Topics**
+ [Recovery by initiating a table restore](bp-pitr-recovery-table-restore.md)
+ [Recovery by rolling back unwanted writes in-place](bp-pitr-recovery-inplace-rollback.md)