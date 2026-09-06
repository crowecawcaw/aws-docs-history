

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# SVV\_RLS\_ATTACHED\_POLICY
<a name="r_SVV_RLS_ATTACHED_POLICY"></a>

Use SVV\_RLS\_ATTACHED\_POLICY to view a list of all relations and users that have one or more row-level security policies attached on the currently connected database.

Only users with the sys:secadmin role can query this view.

## Table columns
<a name="r_SVV_RLS_ATTACHED_POLICY-table-columns"></a>


| Column name  | Data type  | Description | 
| --- | --- | --- | 
| relschema | text | The name of the schema of the relation to which the row-level security policy is attached. | 
| relname | text | The name of the relation to which the row-level security policy is attached. | 
| relkind | text | The type of the object, such as table. | 
| polname | text | The name of the row-level security policy that is attached to the relation. | 
| grantor | text | The name of the user that has attached this policy. | 
| grantee | text | The name of the user or role that this policy has been attached to. | 
| granteekind | text | The type of grantee. Possible values are user or role. | 
| is\_pol\_on | boolean | The parameter that indicates whether a row-level security policy is turned on or off on a table. Possible values are true and false. | 
| is\_rls\_on | boolean | The parameter that indicates whether a row-level security is turned on or off on a table. Possible values are true and false. | 
| rls\_conjunction\_type | character(3) | The parameter that indicates whether relation combine RLS policies with and or or. | 

## Sample query
<a name="r_SVV_RLS_ATTACHED_POLICY-sample-query"></a>

The following example displays the result of the SVV\_RLS\_ATTACHED\_POLICY.

```
--Inspect the policy in SVV_RLS_ATTACHED_POLICY
SELECT * FROM svv_rls_attached_policy;

 relschema |        relname           | relkind |     polname     | grantor | grantee  | granteekind | is_pol_on | is_rls_on | rls_conjuntion_type
-----------+--------------------------+---------+-----------------+---------+----------+-------------+-----------+-----------+---------------------
 public    | tickit_category_redshift |  table  | policy_concerts |   bob   |  analyst |    role     |    True   |    True   |      and
 public    | tickit_category_redshift |  table  | policy_concerts |   bob   |  dbadmin |    role     |    True   |    True   |      and
```