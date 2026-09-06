

# Skipping corrupt blocks
<a name="Appendix.Oracle.CommonDBATasks.SkippingCorruptBlocks"></a>

To skip corrupt blocks during index and table scans, use the `rdsadmin.rdsadmin_dbms_repair` package.

The following procedures wrap the functionality of the `sys.dbms_repair.admin_table` procedure and take no parameters:
+ `rdsadmin.rdsadmin_dbms_repair.create_repair_table`
+ `rdsadmin.rdsadmin_dbms_repair.create_orphan_keys_table`
+ `rdsadmin.rdsadmin_dbms_repair.drop_repair_table`
+ `rdsadmin.rdsadmin_dbms_repair.drop_orphan_keys_table`
+ `rdsadmin.rdsadmin_dbms_repair.purge_repair_table`
+ `rdsadmin.rdsadmin_dbms_repair.purge_orphan_keys_table`

The following procedures take the same parameters as their counterparts in the `DBMS_REPAIR` package for Oracle databases:
+ `rdsadmin.rdsadmin_dbms_repair.check_object`
+ `rdsadmin.rdsadmin_dbms_repair.dump_orphan_keys`
+ `rdsadmin.rdsadmin_dbms_repair.fix_corrupt_blocks`
+ `rdsadmin.rdsadmin_dbms_repair.rebuild_freelists`
+ `rdsadmin.rdsadmin_dbms_repair.segment_fix_status`
+ `rdsadmin.rdsadmin_dbms_repair.skip_corrupt_blocks`

For more information about handling database corruption, see [DBMS\_REPAIR](https://docs.oracle.com/en/database/oracle/oracle-database/19/arpls/DBMS_REPAIR.html#GUID-B8EC4AB3-4D6A-46C9-857F-4ED53CD9C948) in the Oracle documentation.

**Example Responding to corrupt blocks**  
This example shows the basic workflow for responding to corrupt blocks. Your steps will depend on the location and nature of your block corruption.  
Before attempting to repair corrupt blocks, review the [DBMS\_REPAIR](https://docs.oracle.com/en/database/oracle/oracle-database/19/arpls/DBMS_REPAIR.html#GUID-B8EC4AB3-4D6A-46C9-857F-4ED53CD9C948) documentation carefully.

**To skip corrupt blocks during index and table scans**

1. Run the following procedures to create repair tables if they don't already exist.

   ```
   EXEC rdsadmin.rdsadmin_dbms_repair.create_repair_table;
   EXEC rdsadmin.rdsadmin_dbms_repair.create_orphan_keys_table;
   ```

1. Run the following procedures to check for existing records and purge them if appropriate.

   ```
   SELECT COUNT(*) FROM SYS.REPAIR_TABLE;
   SELECT COUNT(*) FROM SYS.ORPHAN_KEY_TABLE;
   SELECT COUNT(*) FROM SYS.DBA_REPAIR_TABLE;
   SELECT COUNT(*) FROM SYS.DBA_ORPHAN_KEY_TABLE;
   
   EXEC rdsadmin.rdsadmin_dbms_repair.purge_repair_table;
   EXEC rdsadmin.rdsadmin_dbms_repair.purge_orphan_keys_table;
   ```

1. Run the following procedure to check for corrupt blocks.

   ```
   SET SERVEROUTPUT ON
   DECLARE v_num_corrupt INT;
   BEGIN
     v_num_corrupt := 0;
     rdsadmin.rdsadmin_dbms_repair.check_object (
       schema_name => '&corruptionOwner',
       object_name => '&corruptionTable',
       corrupt_count =>  v_num_corrupt
     );
     dbms_output.put_line('number corrupt: '||to_char(v_num_corrupt));
   END;
   /
   
   COL CORRUPT_DESCRIPTION FORMAT a30
   COL REPAIR_DESCRIPTION FORMAT a30
   
   SELECT OBJECT_NAME, BLOCK_ID, CORRUPT_TYPE, MARKED_CORRUPT, 
          CORRUPT_DESCRIPTION, REPAIR_DESCRIPTION 
   FROM   SYS.REPAIR_TABLE;
   
   SELECT SKIP_CORRUPT 
   FROM   DBA_TABLES 
   WHERE  OWNER = '&corruptionOwner'
   AND    TABLE_NAME = '&corruptionTable';
   ```

1. Use the `skip_corrupt_blocks` procedure to enable or disable corruption skipping for affected tables. Depending on the situation, you may also need to extract data to a new table, and then drop the table containing the corrupt block.

   Run the following procedure to enable corruption skipping for affected tables.

   ```
   begin
     rdsadmin.rdsadmin_dbms_repair.skip_corrupt_blocks (
       schema_name => '&corruptionOwner',
       object_name => '&corruptionTable',
       object_type => rdsadmin.rdsadmin_dbms_repair.table_object,
       flags => rdsadmin.rdsadmin_dbms_repair.skip_flag);
   end;
   /
   select skip_corrupt from dba_tables where owner = '&corruptionOwner' and table_name = '&corruptionTable';
   ```

   Run the following procedure to disable corruption skipping.

   ```
   begin
     rdsadmin.rdsadmin_dbms_repair.skip_corrupt_blocks (
       schema_name => '&corruptionOwner',
       object_name => '&corruptionTable',
       object_type => rdsadmin.rdsadmin_dbms_repair.table_object,
       flags => rdsadmin.rdsadmin_dbms_repair.noskip_flag);
   end;
   /
   
   select skip_corrupt from dba_tables where owner = '&corruptionOwner' and table_name = '&corruptionTable';
   ```

1. When you have completed all repair work, run the following procedures to drop the repair tables.

   ```
   EXEC rdsadmin.rdsadmin_dbms_repair.drop_repair_table;
   EXEC rdsadmin.rdsadmin_dbms_repair.drop_orphan_keys_table;
   ```