Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# SYS_APPLIED_MASKING_POLICY_LOG

Use SYS_APPLIED_MASKING_POLICY_LOG to trace the application of dynamic data masking
policies on queries that reference DDM-protected relations.

SYS_APPLIED_MASKING_POLICY_LOG is visible to the following users:

- Superusers
- Users with the `sys:operator` role
- Users with the ACCESS SYSTEM TABLE permission
  Regular users will see 0 rows.

Note that SYS_APPLIED_MASKING_POLICY_LOG isn’t visible to users with the
`sys:secadmin` role.

For more information on dynamic data masking, go to [Dynamic data masking](t_ddm.md "t_ddm.md").

## Table columns

| Column name    | Data type | Description                                                                                                                                                 |
| -------------- | --------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| policy_name    | text      | The name of the masking policy.                                                                                                                             |
| user_id        | text      | The ID of the user who ran the query.                                                                                                                       |
| record_time    | timestamp | The time that the system view entry was<br>recorded.                                                                                                        |
| session_id     | int       | The process ID.                                                                                                                                             |
| transaction_id | long      | The transaction ID.                                                                                                                                         |
| query_id       | int       | The query ID.                                                                                                                                               |
| database_name  | text      | The name of the database on which the query was<br>run.                                                                                                     |
| relation_name  | text      | The name of the table that the masking policy is<br>applied to.                                                                                             |
| schema_name    | text      | The name of the schema that the table is<br>in.                                                                                                             |
| attachment_id  | long      | The attached masking policy's ID.                                                                                                                           |
| relation_kind  | text      | The type of the relation that the masking policy<br>is applied to. Possible values are `TABLE`,<br>`VIEW`, `LATE BINDING VIEW`, and<br>`MATERIALIZED VIEW`. |

## Sample

queries

The following example shows that the `mask_credit_card_full` masking
policy is attached to the `credit_db.public.credit_cards` table.

```
select policy_name, database_name, relation_name, schema_name, relation_kind
from sys_applied_masking_policy_log;

policy_name           | database_name | relation_name | schema_name | relation_kind
----------------------+---------------+---------------+-------------+---------------
mask_credit_card_full | credit_db     | credit_cards  | public      | table

(1 row)
```
