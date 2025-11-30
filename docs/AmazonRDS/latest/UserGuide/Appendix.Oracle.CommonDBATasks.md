# Creating a temporary tablespace

on the instance store

To create a temporary tablespace on the instance store, use the Amazon RDS procedure
`rdsadmin.rdsadmin_util.create_inst_store_tmp_tblspace`. The `create_inst_store_tmp_tblspace` procedure has
the following parameters.

| Parameter name      | Data type | Default | Required | Description                           |
| ------------------- | --------- | ------- | -------- | ------------------------------------- |
| `p_tablespace_name` | varchar   | —       | Yes      | The name of the temporary tablespace. |

The following example creates the temporary tablespace `temp01` in the instance
store.

```
EXEC rdsadmin.rdsadmin_util.create_inst_store_tmp_tblspace(p_tablespace_name => '`temp01`');
```

###### Important

When you run `rdsadmin_util.create_inst_store_tmp_tblspace`, the newly created temporary tablespace is not
automatically set as the default temporary tablespace. To set it as the default, see [Setting
the default temporary tablespace](Appendix.Oracle.CommonDBATasks.md#Appendix.Oracle.CommonDBATasks.SettingDefTempTablespace "Appendix.Oracle.CommonDBATasks.md#Appendix.Oracle.CommonDBATasks.SettingDefTempTablespace").

For more information, see [Storing temporary data in an RDS for Oracle instance store](CHAP_Oracle.advanced-features.md "CHAP_Oracle.advanced-features.md").
