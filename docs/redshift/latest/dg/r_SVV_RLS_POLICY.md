Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# SVV_RLS_POLICY

Use SVV_RLS_POLICY to view a list of all row-level security policies created on the Amazon Redshift cluster.

SVV_RLS_POLICY is visible to all users. Superusers can see all rows; regular users can see only their own data. For more information, see [Visibility of data in system tables and
views](cm_chap_system-tables.md#c_visibility-of-data "cm_chap_system-tables.md#c_visibility-of-data").

## Table columns

| Column name     | Data type | Description                                                                          |
| --------------- | --------- | ------------------------------------------------------------------------------------ |
| poldb           | text      | The name of the database in which the row-level<br>security policy is created.       |
| polname         | text      | The name of the row-level security policy.                                           |
| polalias        | text      | The table alias used in the policy<br>definition.                                    |
| polatts         | text      | The attributes provided to the policy<br>definition.                                 |
| polqual         | text      | The policy condition provided in the USING clause<br>of the CREATE POLICY statement. |
| polenabled      | boolean   | Whether the policy is turned on globally.                                            |
| polmodifiedby   | text      | The name of the user that created or modified the<br>policy most recently.           |
| polmodifiedtime | timestamp | The timestamp of when the policy is created or<br>last modified.                     |

## Sample query

The following example displays the result of the SVV_RLS_POLICY.

```
-- Create some policies.
CREATE RLS POLICY pol1 WITH (a int) AS t USING ( t.a IS NOT NULL );
CREATE RLS POLICY pol2 WITH (c varchar(10)) AS t USING ( c LIKE '%public%');

-- Inspect the policy in SVV_RLS_POLICY
SELECT * FROM svv_rls_policy;

 poldb | polname | polalias |                     polatts                      |                polqual                | polenabled | polmodifiedby |   polmodifiedtime
-------+---------+----------+--------------------------------------------------+---------------------------------------+------------+---------------+---------------------
 my_db | pol1    | t        | [{"colname":"a","type":"integer"}]               | "t"."a" IS NOT NULL                   | t          | policy_admin  | 2022-02-11 14:40:49
 my_db | pol2    | t        | [{"colname":"c","type":"character varying(10)"}] | "t"."c" LIKE CAST('%public%' AS TEXT) | t          | policy_admin  | 2022-02-11 14:41:28
```
