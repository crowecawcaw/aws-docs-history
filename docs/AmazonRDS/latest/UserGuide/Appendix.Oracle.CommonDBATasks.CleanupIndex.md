

# Cleaning up interrupted online index builds
<a name="Appendix.Oracle.CommonDBATasks.CleanupIndex"></a>

To clean up failed online index builds, use the Amazon RDS procedure `rdsadmin.rdsadmin_dbms_repair.online_index_clean`. 

The `online_index_clean` procedure has the following parameters.



| Parameter name | Data type | Default | Required | Description | 
| --- | --- | --- | --- | --- | 
| `object_id` | binary\_integer | `ALL_INDEX_ID` | No | The object ID of the index. Typically, you can use the object ID from the ORA-08104 error text. | 
| `wait_for_lock` | binary\_integer | `rdsadmin.rdsadmin_dbms_repair.lock_wait` | No | Specify `rdsadmin.rdsadmin_dbms_repair.lock_wait`, the default, to try to get a lock on the underlying object and retry until an internal limit is reached if the lock fails.<br />Specify `rdsadmin.rdsadmin_dbms_repair.lock_nowait` to try to get a lock on the underlying object but not retry if the lock fails. | 

The following example cleans up a failed online index build:

```
declare
  is_clean boolean;
begin
  is_clean := rdsadmin.rdsadmin_dbms_repair.online_index_clean(
    object_id     => 1234567890, 
    wait_for_lock => rdsadmin.rdsadmin_dbms_repair.lock_nowait
  );
end;
/
```

For more information, see [ONLINE\_INDEX\_CLEAN function](https://docs.oracle.com/en/database/oracle/oracle-database/19/arpls/DBMS_REPAIR.html) in the Oracle documentation. 