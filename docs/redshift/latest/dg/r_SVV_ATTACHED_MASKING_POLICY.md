

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# SVV\_ATTACHED\_MASKING\_POLICY
<a name="r_SVV_ATTACHED_MASKING_POLICY"></a>

Use SVV\_ATTACHED\_MASKING\_POLICY to view all the relations and roles/users with policies attached on the currently connected database. 

Only superusers and users with the [`sys:secadmin`](https://docs.aws.amazon.com/redshift/latest/dg/r_roles-default.html) role can view SVV\_ATTACHED\_MASKING\_POLICY. Regular users will see 0 rows.

## Table columns
<a name="r_SVV_ATTACHED_MASKING_POLICY-table-columns"></a>


| Column name  | Data type  | Description  | 
| --- | --- | --- | 
| policy\_name | text | The name of the masking policy attached to the table. | 
| schema\_name | text | The schema of the table to which the policy is attached. | 
| table\_name | text | The name of the table to which the policy is attached. | 
| table\_type | text | The type of the table to which the policy is attached. | 
| grantor | text | The name of the user that attached the policy. | 
| grantee | text | The name of the user/role to whom the policy is attached. | 
| grantee\_type | text | The type of grantee. This can be role, user, or public. | 
| priority | int | The priority of the attached policy. | 
| input\_columns | text | The input column attributes of the attached policy. | 
| output\_columns | text | The output column attributes of the attached policy. | 
| is\_masking\_datashare\_on | boolean | Whether the table to which the policy is attached is DDM-protected over datashares. | 

## Internal functions
<a name="r_SVV_ATTACHED_MASKING_POLICY-internal-functions"></a>

SVV\_ATTACHED\_MASKING\_POLICY supports the following internal functions: 

### mask\_get\_policy\_for\_role\_on\_column
<a name="r_SVV_ATTACHED_MASKING_POLICY-internal-functions-get-pol-role"></a>

Get the highest priority policy that applies to a given column/role pair.

#### Syntax
<a name="r_SVV_ATTACHED_MASKING_POLICY-internal-functions-get-pol-role-syntax"></a>

```
mask_get_policy_for_role_on_column 
                        (relschema, 
                        relname, 
                        colname, 
                        rolename);
```

#### Parameters
<a name="r_SVV_ATTACHED_MASKING_POLICY-internal-functions-get-pol-role-parameters"></a>

 *relschema*   
The name of the schema the policy is in.

 *relname*   
The name of the table the policy is in.

 *colname*   
The name of the column the policy is attached to.

 *rolename*   
The name of the role the policy is attached to.

### mask\_get\_policy\_for\_user\_on\_column
<a name="r_SVV_ATTACHED_MASKING_POLICY-internal-functions-get-pol-user"></a>

Get the highest priority policy that applies to a given column/user pair.

#### Syntax
<a name="r_SVV_ATTACHED_MASKING_POLICY-internal-functions-get-pol-user-syntax"></a>

```
mask_get_policy_for_user_on_column 
                        (relschema, 
                        relname, 
                        colname, 
                        username);
```

#### Parameters
<a name="r_SVV_ATTACHED_MASKING_POLICY-internal-functions-get-pol-user-parameters"></a>

 *relschema*   
The name of the schema the policy is in.

 *relname*   
The name of the table the policy is in.

 *colname*   
The name of the column the policy is attached to.

 *rolename*   
The name of the user the policy is attached to.