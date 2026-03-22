# Escaping identifiers in masking policy DDL procedure

When creating data masking policies with quoted identifiers, proper escaping is required to ensure correct object references
and policy application. To use quoted identifiers inside the `pg_columnmask` masking policy management procedures:

- **Policy name** – Must be enclosed in double quotes.
- **Table name** – Both schema name and table name must be enclosed in double quotes individually when required.
- **Masking expressions** – Column and function names in masking expressions must be enclosed in
  double quotes and the quotes themselves must be escaped using a backslash.
- **Roles** – The array of role names is automatically quoted.
  The role name should exactly match the name as seen in `pg_roles` including case sensitivity.

###### Example of escaping and quoting syntax

This example shows the proper escaping and quoting syntax when creating masking policies for tables,
columns, functions, and roles that use mixed-case names or require quoted identifiers in Aurora PostgreSQL.

```
-- Create a table and columns with mixed case name
CREATE TABLE public."Employees" (
    "Name" TEXT,
    "Email" TEXT,
    ssn VARCHAR(20)
);

-- Create a role with mixed case name
CREATE ROLE "Masked_user";

-- Create a function with mixed case name
CREATE OR REPLACE FUNCTION public."MaskEmail"(text)
    RETURNS character varying
    LANGUAGE plpgsql
    IMMUTABLE PARALLEL SAFE
    AS $$ BEGIN
        RETURN 'XXXXXXXX'::text;
    END $$;

-- Now use these objects with mixed case names in
-- masking policy management procedures
CALL pgcolumnmask.create_masking_policy(
    '"Policy1"',  -- policy name should be surrounded with double quotes for quoting
    'public."Employees"', -- table and schema name should be individually
                          -- surrounded with double quotes for quoting
    JSON_OBJECT('{
        "\"Email\"", "\"MaskEmail\"(\"Email\")"
    }')::JSONB, -- masking expression should have double quotes around function names
                -- and columns names etc when needed. Also the double quotes itself
                -- should be escaped using \ (backslash) since this is a JSON string
    ARRAY['Masked_user'], -- Rolename do not need quoting
                          -- (this behaviour may change in future release)
    100
);

SELECT * FROM pgcolumnmask.pg_columnmask_policies
    WHERE tablename = 'Employees';
-[ RECORD 1 ]-----+-------------------------------------
schemaname        | public
tablename         | Employees
policyname        | Policy1
roles             | {Masked_user}
masked_columns    | {Email}
masking_functions | {"(\"MaskEmail\"(\"Email\"))::text"}
weight            | 100


```

## Administrative views

You can review all the `pg_columnmask` policy using the publicly accessible `pgcolumnmask.pg_columnmask_policies` administrative view.
Following information is available using this view. The view only returns the masking policies owned by current user.

| Column name       | Data type | Description                                                           |
| ----------------- | --------- | --------------------------------------------------------------------- |
| schemaname        | NAME      | Schema of the relation to which the policy is attached                |
| tablename         | NAME      | Name of the relation to which the policy is attached                  |
| policyname        | NAME      | Name of the masking policy, all masking policies have unique<br>names |
| roles             | TEXT[]    | Role to which policy applies.                                         |
| masked_columns    | TEXT[]    | Masked columns                                                        |
| masking_functions | TEXT[]    | Masking functions                                                     |
| weight            | INT       | Weight of the attached policy                                         |
