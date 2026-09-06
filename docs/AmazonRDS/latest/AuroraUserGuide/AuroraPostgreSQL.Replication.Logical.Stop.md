

# Turning off logical replication
<a name="AuroraPostgreSQL.Replication.Logical.Stop"></a>

After completing your replication tasks, you should stop the replication process, drop replication slots, and turn off logical replication. Before dropping slots, make sure that they're no longer needed. Active replication slots can't be dropped. 

**To turn off logical replication**

1. Drop all replication slots.

   To drop all of the replication slots, connect to the publisher and run the following SQL command.

   ```
   SELECT pg_drop_replication_slot(slot_name)
     FROM pg_replication_slots
    WHERE slot_name IN (SELECT slot_name FROM pg_replication_slots);
   ```

   The replication slots can't be active when you run this command.

1. Modify the custom DB cluster parameter group associated with the publisher as detailed in [Setting up logical replication for your Aurora PostgreSQL DB cluster](AuroraPostgreSQL.Replication.Logical.Configure.md), but set the `rds.logical_replication` parameter to 0. 

   For more information about custom parameter groups, see [Modifying parameters in a DB cluster parameter groupin Amazon Aurora](USER_WorkingWithParamGroups.ModifyingCluster.md). 

1. Restart the publisher Aurora PostgreSQL DB cluster for the change to the `rds.logical_replication` parameter to take effect.