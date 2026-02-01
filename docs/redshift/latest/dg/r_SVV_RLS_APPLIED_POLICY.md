Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# SVV_RLS_APPLIED_POLICY

Use SVV_RLS_APPLIED_POLICY to trace the application of RLS policies on queries that reference RLS-protected relations.

SVV_RLS_APPLIED_POLICY is visible to the following users:

- Superusers
- Users with the `sys:operator` role
- Users with the ACCESS SYSTEM TABLE permission
  Note that sys:secadmin isn't granted this system
  permission.

## Table columns

| Column name | Data type | Description                                                                                                                                                                                                                         |
| ----------- | --------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| username    | text      | The name of the user that ran the query.                                                                                                                                                                                            |
| query       | integer   | The ID of the query.                                                                                                                                                                                                                |
| xid         | long      | The context of the transaction.                                                                                                                                                                                                     |
| pid         | integer   | The leader process running the query.                                                                                                                                                                                               |
| recordtime  | time      | The<br>time<br>when the query was recorded.                                                                                                                                                                                         |
| command     | char(1)   | The command for which the RLS policy was applied. Possible values are `k` for unknown, `s` for select, `u` for update, `i` for insert, `y` for utility, and `d` for delete.                                                         |
| datname     | text      | The name of the database of the relation to which the row-level security policy is attached.                                                                                                                                        |
| relschema   | text      | The name of the schema of the relation to which<br>the row-level security policy is attached.                                                                                                                                       |
| relname     | text      | The name of the relation to which the row-level<br>security policy is attached.                                                                                                                                                     |
| polname     | text      | The name of the row-level security policy that is<br>attached to the relation.                                                                                                                                                      |
| poldefault  | char(1)   | The default setting of the row-level security policy that is attached to the relation. Possible vaules are `f` for false if the default false policy has been applied and `t` for true if the default true policy has been applied. |

## Sample query

The following example displays the result of the SVV_RLS_APPLIED_POLICY. To query the SVV_RLS_APPLIED_POLICY, you must have the ACCESS SYSTEM TABLE permission.

```
-- Check what RLS policies were applied to the run query.
SELECT username, command, datname, relschema, relname, polname, poldefault
FROM svv_rls_applied_policy
WHERE datname = CURRENT_DATABASE() AND query = PG_LAST_QUERY_ID();

 username | command |  datname  | relschema |          relname         |      polname    | poldefault
----------+---------+-----------+-----------+--------------------------+-----------------+------------
   molly  |    s    | tickit_db |   public  | tickit_category_redshift | policy_concerts |
```
