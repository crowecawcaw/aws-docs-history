Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# SHOW POLICIES

Displays the row-level security (RLS) and dynamic data masking (DDM) policies defined in a database, as well as the RLS and DDM policies applied to specific relations. Only a superuser or a user with the `sys:secadmin` role on the database can view the results of these policies.

## Syntax

```
SHOW { RLS | MASKING } POLICIES
[
    ON { *database\_name*.*schema\_name*.*relation\_name*
       | *schema\_name*.*relation\_name*
       }
    [ FOR { *user\_name* | ROLE *role\_name* | PUBLIC } ]
  |
    FROM DATABASE *database\_name*
]
[ LIMIT *row\_limit* ];
```

## Parameters

_database_name_

The name of the database to show policies from.

_schema_name_

Schema name of the relation to show attached policies on.

_relation_name_

The name of the relation to show attached policies on.

_user_name_

The name of the user for whom the policy is attached on relation.

_role_name_

The name of the role for which the policy is attached on relation.

_row_limit_

The maximum number of rows to return. The _row_limit_ can be 0–10,000.

###### Note

Show policies from a database different from the connected database is supported on Amazon Redshift Federated Permissions Catalog. SHOW POLICIES command supports cross-database queries for all databases in warehouses with Amazon Redshift federated permissions

## Examples

The following command shows RLS policies from the connected database.

```
SHOW RLS POLICIES;

  policy_name   | policy_alias |                           policy_atts                            |                                                                  policy_qual                                                                         | policy_enabled | policy_modified_by |    policy_modified_time
----------------+--------------+------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------+----------------+--------------------+----------------------------
 policy_america | rls_table    | [{"colname":"region","type":"character varying(10)"}]            | (("rls_table"."region" = CAST('USA' AS TEXT)) OR ("rls_table"."region" = CAST('CANADA' AS TEXT)) OR ("rls_table"."region" = CAST('Mexico' AS TEXT))) | t              | admin              | 2025-11-07 14:57:27
```

The following command shows masking policies from the database "sales_db.finance-catalog";

```
SHOW MASKING POLICIES FROM DATABASE "sales_db@finance-catalog";

  policy_name  |                          input_columns                           |                                                  policy_expression                                                  | policy_modified_by |    policy_modified_time
---------------+------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------+--------------------+----------------------------
 hash_credit   | [{"colname":"credit_card","type":"character varying(256)"}]      | [{"expr":"SHA2((\"masked_table\".\"credit_card\" + CAST('testSalt' AS TEXT)), CAST(256 AS INT4))","type":"text"}]   | admin              | 2025-11-07 16:05:54
 hash_username | [{"colname":"username","type":"character varying(256)"}]         | [{"expr":"SHA2((\"masked_table\".\"username\" + CAST('otherTestSalt' AS TEXT)), CAST(256 AS INT4))","type":"text"}] | admin              | 2025-11-07 16:07:08
(2 rows)
```

The following command shows RLS policies attached on the relation sales_table;

```
SHOW RLS POLICIES ON sales_schema.sales_table;

  policy_name   | schema_name  | relation_name | relation_kind | grantor  |          grantee          | grantee_kind | is_policy_on | is_rls_on | rls_conjunction_type
----------------+--------------+---------------+---------------+----------+---------------------------+--------------+--------------+-----------+----------------------
 policy_global  | sales_schema | sales_table   | table         | admin    | sales_analyst_role_global | role         | t            | t         | and
 policy_america | sales_schema | sales_table   | table         | admin    | sales_analyst_usa         | user         | t            | t         | and
```

The following command shows masking policies attached on the relation transaction_table from the database "sales_db.finance-catalog".

```
SHOW MASKING POLICIES ON "sales_db@finance-catalog".sales_schema.transaction_table LIMIT 1;

  policy_name  | schema_name  |   relation_name   | relation_type | grantor  |         grantee          | grantee_type | priority |   input_columns   |   output_columns
---------------+--------------+-------------------+---------------+----------+--------------------------+--------------+----------+-------------------+-------------------
 hash_username | sales_schema | transaction_table | table         | admin    | transaction_analyst_role | role         |      100 | ["user_name"]     | ["user_name"]
```

The following command shows RLS policies attached on the relation sales_table from the database "sales_db.finance-catalog" for the user "IAMR:sales_analyst_usa".

```
SHOW RLS POLICIES ON "sales_db@finance-catalog".sales_schema.sales_table FOR "IAMR:sales_analyst_usa";

  policy_name   | schema_name  | relation_name | relation_kind | grantor  |      grantee           | grantee_kind | is_policy_on | is_rls_on | rls_conjunction_type
----------------+--------------+---------------+---------------+----------+------------------------+--------------+--------------+-----------+----------------------
 policy_america | sales_schema | sales_table   | table         | admin    | IAMR:sales_analyst_usa | user         | t            | t         | and
```

The following command shows RLS policies attached on the relation transaction_table from the database "sales_db.finance-catalog" for the role transaction_analyst_role.

```
SHOW MASKING POLICIES ON sales_schema.transaction_table FOR ROLE transaction_analyst_role;

  policy_name  | schema_name  |   relation_name   | relation_type | grantor  |         grantee          | grantee_type | priority | input_columns | output_columns
---------------+--------------+-------------------+---------------+----------+--------------------------+--------------+----------+---------------+----------------
 hash_username | sales_schema | transaction_table | table         | admin    | transaction_analyst_role | role         |      100 | ["user_name"] | ["user_name"]
```
