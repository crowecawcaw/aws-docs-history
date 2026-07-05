Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026.
We will start enforcing it in phases. For more information on the details of Python end of life
and migration options, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") that was published on June 30, 2025.

# SVV\_RLS\_POLICY

Use SVV\_RLS\_POLICY to view a list of all row-level security policies created on the Amazon Redshift cluster.

SVV\_RLS\_POLICY is visible to all users. Superusers can see all rows; regular users can see only their own data. For more information, see [Visibility of data in system tables and views](cm_chap_system-tables.md#c_visibility-of-data "cm_chap_system-tables.md#c_visibility-of-data").

For more information about best practices when querying system tables and views, see
[Querying System Tables](../mgmt/discovering-metadata-system-tables.md "../mgmt/discovering-metadata-system-tables.md").

###### Note

Use the [SHOW POLICIES](r_SHOW_POLICIES.md "r_SHOW_POLICIES.md") command for policy discovery. SHOW POLICIES works consistently
across local, datashare, and external catalog contexts and is updated as new features are released.
For more information, see [Best practices for discovering metadata](../mgmt/best-practices-discovering-metadata.md "../mgmt/best-practices-discovering-metadata.md").

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

The following example displays the result of the SVV\_RLS\_POLICY.

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
