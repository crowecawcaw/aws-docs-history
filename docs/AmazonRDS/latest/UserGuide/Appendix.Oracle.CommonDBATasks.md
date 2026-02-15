# Changing the

global name of a database

To change the global name of a database, use the Amazon RDS procedure
`rdsadmin.rdsadmin_util.rename_global_name`. The
`rename_global_name` procedure has the following parameters.

| Parameter name      | Data type | Default | Required | Description                           |
| ------------------- | --------- | ------- | -------- | ------------------------------------- |
| `p_new_global_name` | varchar2  | —       | Yes      | The new global name for the database. |

The database must be open for the name change to occur. For more information about
changing the global name of a database, see [ALTER DATABASE](http://docs.oracle.com/cd/E11882_01/server.112/e41084/statements_1004.htm#SQLRF52547 "http://docs.oracle.com/cd/E11882_01/server.112/e41084/statements_1004.htm#SQLRF52547") in the Oracle documentation.

The following example changes the global name of a database to
`new_global_name`.

```
EXEC rdsadmin.rdsadmin_util.rename_global_name(p_new_global_name => '`new_global_name`');
```
