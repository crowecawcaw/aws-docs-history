Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026.
We will start enforcing it in phases. For more information on the details of Python end of life
and migration options, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") that was published on June 30, 2025.

# SVV\_ATTACHED\_MASKING\_POLICY

Use SVV\_ATTACHED\_MASKING\_POLICY to view all the relations and roles/users with policies attached on the currently connected database.

Only superusers and users with the [`sys:secadmin`](r_roles-default.md "r_roles-default.md") role can view SVV\_ATTACHED\_MASKING\_POLICY. Regular users will see 0 rows.

## Table columns

| Column name                | Data type | Description                                                                         |
| -------------------------- | --------- | ----------------------------------------------------------------------------------- |
| policy\_name               | text      | The name of the masking policy attached to the table.                               |
| schema\_name               | text      | The schema of the table to which the policy is attached.                            |
| table\_name                | text      | The name of the table to which the policy is attached.                              |
| table\_type                | text      | The type of the table to which the policy is attached.                              |
| grantor                    | text      | The name of the user that attached the policy.                                      |
| grantee                    | text      | The name of the user/role to whom the policy is attached.                           |
| grantee\_type              | text      | The type of grantee. This can be _role_,<br>_user_, or _public_.                    |
| priority                   | int       | The priority of the attached policy.                                                |
| input\_columns             | text      | The input column attributes of the attached policy.                                 |
| output\_columns            | text      | The output column attributes of the attached policy.                                |
| is\_masking\_datashare\_on | boolean   | Whether the table to which the policy is attached is DDM-protected over datashares. |

## Internal functions

SVV\_ATTACHED\_MASKING\_POLICY supports the following internal functions:

### mask\_get\_policy\_for\_role\_on\_column

Get the highest priority policy that applies to a given column/role pair.

#### Syntax

```
mask_get_policy_for_role_on_column
                        (relschema,
                        relname,
                        colname,
                        rolename);

```

#### Parameters

_relschema_

The name of the schema the policy is in.

_relname_

The name of the table the policy is in.

_colname_

The name of the column the policy is attached to.

_rolename_

The name of the role the policy is attached to.

### mask\_get\_policy\_for\_user\_on\_column

Get the highest priority policy that applies to a given column/user pair.

#### Syntax

```
mask_get_policy_for_user_on_column
                        (relschema,
                        relname,
                        colname,
                        username);

```

#### Parameters

_relschema_

The name of the schema the policy is in.

_relname_

The name of the table the policy is in.

_colname_

The name of the column the policy is attached to.

_rolename_

The name of the user the policy is attached to.
