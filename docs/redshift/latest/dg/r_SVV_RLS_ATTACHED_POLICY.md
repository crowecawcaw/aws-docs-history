Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# SVV_RLS_ATTACHED_POLICY

Use SVV_RLS_ATTACHED_POLICY to view a list of all relations and users that have one or more row-level security policies attached on the currently connected database.

Only users with the sys:secadmin role can query this view.

## Table columns

| Column name          | Data type    | Description                                                                                                                                |
| -------------------- | ------------ | ------------------------------------------------------------------------------------------------------------------------------------------ |
| relschema            | text         | The name of the schema of the relation to which<br>the row-level security policy is attached.                                              |
| relname              | text         | The name of the relation to which the row-level<br>security policy is attached.                                                            |
| relkind              | text         | The type of the object, such as table.                                                                                                     |
| polname              | text         | The name of the row-level security policy that is<br>attached to the relation.                                                             |
| grantor              | text         | The name of the user that has attached this<br>policy.                                                                                     |
| grantee              | text         | The name of the user or role that this policy has<br>been attached to.                                                                     |
| granteekind          | text         | The type of grantee. Possible values are user or<br>role.                                                                                  |
| is_pol_on            | boolean      | The parameter that indicates whether a row-level<br>security policy is turned on or off on a table. Possible values are<br>true and false. |
| is_rls_on            | boolean      | The parameter that indicates whether a row-level<br>security is turned on or off on a table. Possible values are true<br>and false.        |
| rls_conjunction_type | character(3) | The parameter that indicates whether relation combine RLS policies with `and` or `or`.                                                     |

## Sample query

The following example displays the result of the SVV_RLS_ATTACHED_POLICY.

```
--Inspect the policy in SVV_RLS_ATTACHED_POLICY
SELECT * FROM svv_rls_attached_policy;

 relschema |        relname           | relkind |     polname     | grantor | grantee  | granteekind | is_pol_on | is_rls_on | rls_conjuntion_type
-----------+--------------------------+---------+-----------------+---------+----------+-------------+-----------+-----------+---------------------
 public    | tickit_category_redshift |  table  | policy_concerts |   bob   |  analyst |    role     |    True   |    True   |      and
 public    | tickit_category_redshift |  table  | policy_concerts |   bob   |  dbadmin |    role     |    True   |    True   |      and
```
