

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# SHOW POLICIES
<a name="r_SHOW_POLICIES"></a>

Displays the row-level security (RLS) and dynamic data masking (DDM) policies defined in a database, as well as the RLS and DDM policies applied to specific relations. Only a superuser or a user with the `sys:secadmin` role on the database can view the results of these policies.

## Syntax
<a name="r_SHOW_POLICIES-synopsis"></a>

```
SHOW { RLS | MASKING } POLICIES
[
    ON { database_name.schema_name.relation_name
       | schema_name.relation_name
       }
    [ FOR { user_name | ROLE role_name | PUBLIC } ]
  |
    FROM DATABASE database_name
]
[ LIMIT row_limit ];
```

## Parameters
<a name="r_SHOW_POLICIES-parameters"></a>

*database\_name*  
The name of the database to show policies from.

*schema\_name*  
Schema name of the relation to show attached policies on.

*relation\_name*  
The name of the relation to show attached policies on.

*user\_name*  
The name of the user for whom the policy is attached on relation.

*role\_name*  
The name of the role for which the policy is attached on relation.

*row\_limit*  
The maximum number of rows to return. The *row\_limit* can be 0–10,000.

**Note**  
Show policies from a database different from the connected database is supported on Amazon Redshift Federated Permissions Catalog. SHOW POLICIES command supports cross-database queries for all databases in warehouses with Amazon Redshift federated permissions

## Examples
<a name="r_SHOW_POLICIES-examples"></a>

The following command shows RLS policies from the connected database.

```
SHOW RLS POLICIES;

  policy_name   | policy_alias |                           policy_atts                            |                                                                  policy_qual                                                                         | policy_enabled | policy_modified_by |    policy_modified_time    
----------------+--------------+------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------+----------------+--------------------+----------------------------
 policy_america | rls_table    | [{"colname":"region","type":"character varying(10)"}]            | (("rls_table"."region" = CAST('USA' AS TEXT)) OR ("rls_table"."region" = CAST('CANADA' AS TEXT)) OR ("rls_table"."region" = CAST('Mexico' AS TEXT))) | t              | admin              | 2025-11-07 14:57:27
```

The following command shows masking policies from the database "sales\_db.finance-catalog";

```
SHOW MASKING POLICIES FROM DATABASE "sales_db@finance-catalog";

  policy_name  |                          input_columns                           |                                                  policy_expression                                                  | policy_modified_by |    policy_modified_time    
---------------+------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------+--------------------+----------------------------
 hash_credit   | [{"colname":"credit_card","type":"character varying(256)"}]      | [{"expr":"SHA2((\"masked_table\".\"credit_card\" + CAST('testSalt' AS TEXT)), CAST(256 AS INT4))","type":"text"}]   | admin              | 2025-11-07 16:05:54
 hash_username | [{"colname":"username","type":"character varying(256)"}]         | [{"expr":"SHA2((\"masked_table\".\"username\" + CAST('otherTestSalt' AS TEXT)), CAST(256 AS INT4))","type":"text"}] | admin              | 2025-11-07 16:07:08
(2 rows)
```

The following command shows RLS policies attached on the relation sales\_table;

```
SHOW RLS POLICIES ON sales_schema.sales_table;

  policy_name   | schema_name  | relation_name | relation_kind | grantor  |          grantee          | grantee_kind | is_policy_on | is_rls_on | rls_conjunction_type 
----------------+--------------+---------------+---------------+----------+---------------------------+--------------+--------------+-----------+----------------------
 policy_global  | sales_schema | sales_table   | table         | admin    | sales_analyst_role_global | role         | t            | t         | and
 policy_america | sales_schema | sales_table   | table         | admin    | sales_analyst_usa         | user         | t            | t         | and
```

The following command shows masking policies attached on the relation transaction\_table from the database "sales\_db.finance-catalog".

```
SHOW MASKING POLICIES ON "sales_db@finance-catalog".sales_schema.transaction_table LIMIT 1;

  policy_name  | schema_name  |   relation_name   | relation_type | grantor  |         grantee          | grantee_type | priority |   input_columns   |   output_columns   
---------------+--------------+-------------------+---------------+----------+--------------------------+--------------+----------+-------------------+-------------------
 hash_username | sales_schema | transaction_table | table         | admin    | transaction_analyst_role | role         |      100 | ["user_name"]     | ["user_name"]
```

The following command shows RLS policies attached on the relation sales\_table from the database "sales\_db.finance-catalog" for the user "IAMR:sales\_analyst\_usa".

```
SHOW RLS POLICIES ON "sales_db@finance-catalog".sales_schema.sales_table FOR "IAMR:sales_analyst_usa";

  policy_name   | schema_name  | relation_name | relation_kind | grantor  |      grantee           | grantee_kind | is_policy_on | is_rls_on | rls_conjunction_type 
----------------+--------------+---------------+---------------+----------+------------------------+--------------+--------------+-----------+----------------------
 policy_america | sales_schema | sales_table   | table         | admin    | IAMR:sales_analyst_usa | user         | t            | t         | and
```

The following command shows RLS policies attached on the relation transaction\_table from the database "sales\_db.finance-catalog" for the role transaction\_analyst\_role.

```
SHOW MASKING POLICIES ON sales_schema.transaction_table FOR ROLE transaction_analyst_role;

  policy_name  | schema_name  |   relation_name   | relation_type | grantor  |         grantee          | grantee_type | priority | input_columns | output_columns 
---------------+--------------+-------------------+---------------+----------+--------------------------+--------------+----------+---------------+----------------
 hash_username | sales_schema | transaction_table | table         | admin    | transaction_analyst_role | role         |      100 | ["user_name"] | ["user_name"]
```