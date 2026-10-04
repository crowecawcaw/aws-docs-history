

# Procedures for managing data masking policies
<a name="AuroraPostgreSQL.Security.DynamicMasking.Procedures"></a>

You can manage masking policies using procedures provided by the `pg_columnmask` extension. To create, modify, or drop masking policies, you must have one of the following privileges:
+ Owner of the table on which you are creating the `pg_columnmask` policy.
+ Member of `rds_superuser`.
+ Member of `pg_columnmask` policy manager role set by the `pgcolumnmask.policy_admin_rolname` parameter.

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
<a name="AuroraPostgreSQL.Security.DynamicMasking.Procedures.CreateMaskingPolicy"></a>

The following procedure creates a new masking policy for a user table:

**Syntax**

```
create_masking_policy(
    policy_name,
    table_name,
    masking_expressions,
    roles,
    weight,
    predicate_allow_list)
```

**Note**  
The `predicate_allow_list` argument requires `pg_columnmask` extension version 1.1 or later, available in Aurora PostgreSQL 16.11 and higher, and 17.7 and higher. To update the extension, run `ALTER EXTENSION pg_columnmask UPDATE;`. For more information, see [ALTER EXTENSION](https://www.postgresql.org/docs/current/sql-alterextension.html) in the PostgreSQL documentation.

**Arguments**


| Parameter | Datatype | Description | 
| --- | --- | --- | 
| policy\_name | NAME | The name of the masking policy. Must be unique per table. | 
| table\_name | REGCLASS | The qualified/unqualified name or oid of the table to apply masking policy. | 
| masking\_expressions | JSONB | JSON object containing column name and masking function pairs. Each key is a column name and its value is the masking expression to be applied on that column. | 
| roles | NAME[] | The roles to which this masking policy applies. Default is PUBLIC. | 
| weight | INT | Weight of the masking policy. When multiple policies are applicable to a given user's query, the policy with the highest weight (higher integer number) will be applied to each masked column.<br />Default is 0. No two masking policies on the table can have the same weight. | 
| predicate\_allow\_list | NAME[] | An array of column names that may be referenced in predicates, join conditions, and other filter expressions even when masked by this policy. Without this setting, predicates on masked columns raise an error. When a column is in the allow list, the predicate executes against the masked values. | 

**Return type**

None

**Example of creating a masking policy that masks the email column for the `test_user` role:**  

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
<a name="AuroraPostgreSQL.Security.DynamicMasking.Procedures.AlterMaskingPolicy"></a>

This procedure modifies an existing masking policy. `ALTER_MASKING_POLICY` can modify the policy masking expressions, set of roles to which the policy applies, the weight, and the predicate allow list of the masking policy. When one of those parameters is omitted, the corresponding part of the policy is unchanged.

**Syntax**

```
alter_masking_policy(
    policy_name,
    table_name,
    masking_expressions,
    roles,
    weight,
    predicate_allow_list)
```

**Note**  
The `predicate_allow_list` argument requires `pg_columnmask` extension version 1.1 or later, available in Aurora PostgreSQL 16.11 and higher, and 17.7 and higher. To update the extension, run `ALTER EXTENSION pg_columnmask UPDATE;`. For more information, see [ALTER EXTENSION](https://www.postgresql.org/docs/current/sql-alterextension.html) in the PostgreSQL documentation.

**Arguments**


| Parameter | Datatype | Description | 
| --- | --- | --- | 
| policy\_name | NAME | Existing name of the masking policy. | 
| table\_name | REGCLASS | The qualified/unqualified name oid of the table containing the masking policy. | 
| masking\_expressions | JSONB | New JSON object containing column name and masking function pairs or NULL otherwise. | 
| roles | NAME[] | The list of new roles to which this masking policy applies or NULL otherwise. | 
| weight | INT | New weight for the masking policy or NULL otherwise. | 
| predicate\_allow\_list | NAME[] | The new array of column names permitted in predicates and filter expressions, or NULL to leave unchanged. | 

**Return type**

None

**Example of adding the analyst role to an existing masking policy without changing other policy attributes.**  

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
<a name="AuroraPostgreSQL.Security.DynamicMasking.Procedures.DropMaskingPolicy"></a>

This procedure removes an existing masking policy.

**Syntax**

```
drop_masking_policy(
        policy_name,
        table_name)
```

**Arguments**


| Parameter | Datatype | Description | 
| --- | --- | --- | 
| policy\_name | NAME | Existing name of the masking policy. | 
| table\_name | REGCLASS | The qualified/unqualified name oid of the table containing the masking policy. | 

**Return type**

None

**Example of dropping the masking policy customer\_mask**  

```
-- Drop a masking policy
    CALL pgcolumnmask.drop_masking_policy(
        'customer_mask',
        'public.customers',
    );
```

## RENAME\_MASKING\_POLICY
<a name="AuroraPostgreSQL.Security.DynamicMasking.Procedures.RenameMaskingPolicy"></a>

This procedure renames an existing masking policy.

**Syntax**

```
rename_masking_policy(
    policy_name,
    table_name,
    new_policy_name)
```

**Arguments**


| Parameter | Datatype | Description | 
| --- | --- | --- | 
| policy\_name | NAME | The current name of the masking policy. | 
| table\_name | REGCLASS | The qualified/unqualified name or oid of the table containing the masking policy. | 
| new\_policy\_name | NAME | The new name for the masking policy. Must be unique per table. | 

## Administrative views
<a name="AuroraPostgreSQL.Security.DynamicMasking.AdminViews"></a>

The `pgcolumnmask.ddm_policies` view shows masking policies on tables that you own or have management privileges on.


| Column name | Data type | Description | 
| --- | --- | --- | 
| schemaname | NAME | The schema of the table to which the policy applies. | 
| tablename | NAME | The name of the table to which the policy applies. | 
| policyname | NAME | The name of the masking policy. | 
| roles | TEXT[] | The roles to which the policy applies. | 
| masked\_columns | TEXT[] | The columns masked by the policy. | 
| masking\_functions | TEXT[] | The masking functions applied to the masked columns. | 
| weight | INT | The weight of the policy. | 
| predicate\_allow\_list | NAME[] | An array of column names permitted in predicates and filter expressions even when masked by the policy. | 

## Quoted identifiers in masking policies
<a name="AuroraPostgreSQL.Security.DynamicMasking.EscapeIdentifiers"></a>

Mixed-case or reserved-word identifiers require double-quote escaping in policy name, schema, table, column, and role arguments. Inside JSON strings, escape double quotes with a backslash. Role names must exactly match `pg_roles` including case.

**Example – quoted and unquoted identifiers**  
Lowercase identifiers (no quoting needed):  

```
CALL pgcolumnmask.create_masking_policy(
    'ssn_policy',
    'public.employees',
    JSON_BUILD_OBJECT('ssn', 'public.mask_ssn(ssn)')::JSONB,
    ARRAY['analyst'],
    10
);
```
The same policy with mixed-case identifiers (quoting required):  

```
CALL pgcolumnmask.create_masking_policy(
    '"SSN_Policy"',
    '"Public"."Employees"',
    JSON_BUILD_OBJECT('"SSN"', 'public."Mask_SSN"("SSN")')::JSONB,
    ARRAY['"Analyst"'],
    10
);
```
Both policies in `pgcolumnmask.ddm_policies`:  

```
SELECT schemaname, tablename, policyname, roles, weight
    FROM pgcolumnmask.ddm_policies
    ORDER BY tablename, weight;
 schemaname | tablename | policyname | roles     | weight
------------+-----------+------------+-----------+--------
 Public     | Employees | SSN_Policy | {Analyst} |     10
 public     | employees | ssn_policy | {analyst} |     10
```

**Note**  
In versions before Aurora PostgreSQL 16.11 and 17.7, the extension automatically quoted role names. In Aurora PostgreSQL 16.11 and 17.7 and later, role names are only quoted when explicitly enclosed in double quotes.