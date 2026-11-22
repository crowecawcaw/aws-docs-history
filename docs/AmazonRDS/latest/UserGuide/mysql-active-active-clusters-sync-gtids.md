

# Synchronizing local GTIDs before a DB instance joins an active-active cluster (MySQL 9.7)

When you create an RDS for MySQL 9.7 DB instance, Amazon RDS can write transactions with global transaction identifiers (GTIDs) under the DB instance's own server UUID. Amazon RDS writes these local GTIDs periodically until the active-active cluster parameters in the DB instance's parameter group take effect.

If a DB instance that joins the group has executed GTIDs that the group members don't have, the DB instance can't join the group. In this case, `mysql.rds_group_replication_start` returns error 3092, and the error log shows error `MY-011526` (the member has more executed transactions than those present in the group).

Before a DB instance joins or rejoins an active-active cluster, compare its executed GTIDs with the executed GTIDs of each `ONLINE` group member. If the executed GTIDs differ, use the [mysql.rds\_group\_replication\_advance\_gtid](mysql-stored-proc-active-active-clusters.md#mysql_rds_group_replication_advance_gtid) stored procedure to create placeholder GTIDs for the missing local GTIDs. Do this in both directions: on each group member for the local GTIDs of the joining DB instance, and on the joining DB instance for the local GTIDs of each group member.

If a DB instance is rejoining the group, the comparisons in this procedure usually return no initialization GTIDs. If they return GTIDs under the rejoining DB instance's own server UUID, the DB instance wrote those transactions while it was out of the group. Don't create placeholder GTIDs for them.

**Important**  
Use this procedure only for the local GTIDs that a new DB instance writes under its own server UUID before the active-active cluster parameters take effect. Before you create placeholder GTIDs, confirm that the transactions don't contain changes to your data. Never create placeholder GTIDs whose UUID is the group name (`group_replication_group_name`) or the server UUID of the DB instance that you converted to an active-active cluster. Those GTIDs belong to transactions that contain data.

**To synchronize local GTIDs before a DB instance joins an active-active cluster**

1. Connect to the DB instance that is joining the group in a SQL client, and get its server UUID and executed GTIDs:

   ```sql
   SELECT @@server_uuid, @@GLOBAL.gtid_executed;
   ```

   Record both values. In the following steps, the executed GTIDs of the joining DB instance are {{joining\_instance\_gtid\_executed}}.

1. Connect to each of the other DB instances in the active-active cluster, and check that the DB instance is an `ONLINE` member of the group:

   ```sql
   SELECT MEMBER_STATE FROM performance_schema.replication_group_members WHERE MEMBER_ID = @@server_uuid;
   ```

   Skip any DB instance that doesn't return `ONLINE`. On each `ONLINE` member, get the group name, the server UUID, and the executed GTIDs:

   ```sql
   SELECT @@GLOBAL.group_replication_group_name, @@server_uuid, @@GLOBAL.gtid_executed;
   ```

   Record all three values for each member. In the following steps, the executed GTIDs of a member are {{member\_gtid\_executed}}.

1. On each `ONLINE` member, find the GTIDs that the joining DB instance has executed but the member hasn't:

   ```sql
   SELECT GTID_SUBTRACT('{{joining_instance_gtid_executed}}', @@GLOBAL.gtid_executed);
   ```

   If the result is empty, the member already has all of the GTIDs of the joining DB instance. Otherwise, the result contains one or more GTID sets, separated by commas, in the format {{uuid}}:{{interval}}[:{{interval}}...]. Each interval is either {{begin\_id}}-{{end\_id}} or a single {{id}}, which you use as both {{begin\_id}} and {{end\_id}}. Call the procedure once for each interval. The result can span several lines.

   Create placeholder GTIDs only for the initialization GTIDs of a new DB instance. These are ranges whose {{uuid}} is the server UUID (`@@server_uuid`) of a DB instance that you created for the active-active cluster, and that the DB instance wrote when it was created, before it first joined the group. Don't create placeholder GTIDs for any other range. This includes ranges whose {{uuid}} is the group name or the server UUID of the DB instance that you converted to an active-active cluster, and ranges that a DB instance wrote after it first joined the group. Those GTIDs belong to transactions that contain data.

   Call the following stored procedure on that member:

   ```sql
   CALL mysql.rds_group_replication_advance_gtid({{begin_id}}, {{end_id}}, '{{uuid}}');
   ```

1. On the joining DB instance, repeat the previous step in the other direction for each `ONLINE` member. Run the following query with the executed GTIDs of the member:

   ```sql
   SELECT GTID_SUBTRACT('{{member_gtid_executed}}', @@GLOBAL.gtid_executed);
   ```

   Create placeholder GTIDs only for the initialization GTIDs of a new DB instance. These are ranges whose {{uuid}} is the server UUID (`@@server_uuid`) of a DB instance that you created for the active-active cluster, and that the DB instance wrote when it was created, before it first joined the group. Don't create placeholder GTIDs for any other range. This includes ranges whose {{uuid}} is the group name or the server UUID of the DB instance that you converted to an active-active cluster, and ranges that a DB instance wrote after it first joined the group. Those GTIDs belong to transactions that contain data. The joining DB instance receives them from the group when it starts replication.

   For each of those intervals, call the following stored procedure on the joining DB instance:

   ```sql
   CALL mysql.rds_group_replication_advance_gtid({{begin_id}}, {{end_id}}, '{{uuid}}');
   ```

1. Return to the procedure that you're following and continue with the step that starts Group Replication on the joining DB instance.