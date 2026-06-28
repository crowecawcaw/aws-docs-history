# Procedures for managing data masking policies

You can manage masking policies using procedures provided by the `pg_columnmask` extension.
To create, modify, or drop masking policies, you must have one of the following privileges:

- Owner of the table on which you are creating the `pg_columnmask` policy.
- Member of `rds_superuser`.
- Member of `pg_columnmask` policy manager role set by the `pgcolumnmask.policy_admin_rolname` parameter.
  The following command creates a table that is used in subsequent sections:

```
CREATE TABLE public.customers (
    id SERIAL PRIMARY KEY,
    name TEXT,
    phone TEXT,
    address TEXT,
    email TEXT
);
```

## CREATE\_MASKING\_POLICY

The following procedure creates a new masking policy for a user table:

**Syntax**

```
create_masking_policy(
    policy_name,
    table_name,
    masking_expressions,
    roles,
    weight)
```

**Arguments**

| Parameter             | Datatype | Description                                                                                                                                                                                                                                                                                |
| --------------------- | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `policy_name`         | NAME     | The name of the masking policy. Must be unique per<br>table.                                                                                                                                                                                                                               |
| `table_name`          | REGCLASS | The qualified/unqualified name or oid of the table to apply<br>masking policy.                                                                                                                                                                                                             |
| `masking_expressions` | JSONB    | JSON object containing column name and masking function pairs.<br>Each key is a column name and its value is the masking<br>expression to be applied on that column.                                                                                                                       |
| `roles`               | NAME[]   | The roles to which this masking policy applies. Default is<br>PUBLIC.                                                                                                                                                                                                                      |
| `weight`              | INT      | Weight of the masking policy. When multiple policies are<br>applicable to a given user's query, the policy with the highest<br>weight (higher integer number) will be applied to each masked<br>column.<br>Default is 0. No two masking policies on the table can have<br>the same wieght. |

**Return type**

None

###### Example of creating a masking policy that masks the email column for the `test_user` role:

```
CALL pgcolumnmask.create_masking_policy(
    'customer_mask',
    'public.customers',
    JSON_OBJECT('{
        "email", "pgcolumnmask.mask_email(email)"
    }')::JSONB,
    ARRAY['test_user'],
    100
);
```

## ALTER\_MASKING\_POLICY

This procedure modifies an existing masking policy. `ALTER_MASKING_POLICY` can modify the policy masking expressions,
set of roles to which the policy applies and the weight of the masking policy. When one of those parameters is omitted,
the corresponding part of the policy is unchanged.

**Syntax**

```
alter_masking_policy(
    policy_name,
    table_name,
    masking_expressions,
    roles,
    weight)
```

**Arguments**

| Parameter             | Datatype | Description                                                                             |
| --------------------- | -------- | --------------------------------------------------------------------------------------- |
| `policy_name`         | NAME     | Existing name of the masking policy.                                                    |
| `table_name`          | REGCLASS | The qualified/unqualified name oid of the table containing the<br>masking policy.       |
| `masking_expressions` | JSONB    | New JSON object containing column name and masking function pairs<br>or NULL otherwise. |
| `roles`               | NAME[]   | The list of new roles to which this masking policy applies or NULL<br>otherwise.        |
| `weight`              | INT      | New weight for the masking policy or NULL otherwise.                                    |

**Return type**

None

###### Example of adding the analyst role to an existing masking policy without changing other policy attributes.

```
CALL pgcolumnmask.alter_masking_policy(
    'customer_mask',
    'public.customers',
    NULL,
    ARRAY['test_user', 'analyst'],
    NULL
);

-- Alter the weight of the policy without altering other details
CALL pgcolumnmask.alter_masking_policy(
    'customer_mask',
    'customers',
    NULL,
    NULL,
    4
);
```

## DROP\_MASKING\_POLICY

This procedure removes an existing masking policy.

**Syntax**

```
drop_masking_policy(
        policy_name,
        table_name)
```

**Arguments**

| Parameter     | Datatype | Description                                                                       |
| ------------- | -------- | --------------------------------------------------------------------------------- |
| `policy_name` | NAME     | Existing name of the masking policy.                                              |
| `table_name`  | REGCLASS | The qualified/unqualified name oid of the table containing the<br>masking policy. |

**Return type**

None

###### Example of dropping the masking policy customer\_mask

```
-- Drop a masking policy
    CALL pgcolumnmask.drop_masking_policy(
        'customer_mask',
        'public.customers',
    );
```
