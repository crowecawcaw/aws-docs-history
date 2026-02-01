Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Managing access control on Amazon Redshift federated permissions catalog

With Amazon Redshift federated permissions, users can define both coarse-grained and fine-grained access controls from any Redshift warehouse in the AWS account. Coarse-grained permissions manage access to tables, views, and database objects, including scoped permissions, while fine-grained controls allow column-level privileges and the application of security policies such as row-level security (RLS) and dynamic data masking (DDM).

## Grant / Revoke

With federated permissions, you can define permissions on table level accesses such as access to read, write data in tables and views in Redshift Federated Permissions database from any of the Redshift warehouse.

```
GRANT SELECT ON "sales_db@finance-catalog".sales_schema.sales_table TO "IAMR:sales_analyst";

GRANT INSERT ON "sales_db@finance-catalog".sales_schema.sales_view TO "IAMR:sales_data_engineer";

REVOKE UPDATE ON "sales_db@finance-catalog".sales_schema.us_sales_view FROM "IAMR:us_sales_analyst";

REVOKE DELETE ON "sales_db@finance-catalog".sales_schema.us_sales_view FROM "IAMR:us_sales_analyst";
```

Amazon Redshift federated permissions support scoped permissions to let you grant or revoke permissions on all objects of a type within a database or schema.

```
GRANT SELECT FOR TABLES IN SCHEMA "sales_db@finance-catalog".sales_schema TO "IAMR:sales_manager";

REVOKE UPDATE FOR TABLES IN SCHEMA sales_schmea DATABASE "sales_db@finance-catalog" FROM "IAMR:sales_analyst";
```

You can define grant / revoke access permissions on database.

```
GRANT CREATE ON DATABASE "sales_db@finance-catalog" TO "IAMR:sales_admin";

REVOKE TEMP ON DATABASE "sales_db@finance-catalog" FROM "IAMR:sales_analyst";
```

For more information about Amazon Redshift federated permissions supported syntax for grant, see [Permissions you can grant on Amazon Redshift federated permissions catalog](#federated-permissions-managing-access-grant-allowed "#federated-permissions-managing-access-grant-allowed").

## Fine-grained access control

You can define fine-grained access control over sensitive data using column-level access control, row-level security (RLS) and dynamic data masking (DDM) in a database with Amazon Redshift federation permissions. Column-level access control allows to define finer grained column level access privileges on tables and views. Superusers and users or roles with the `sys:secadmin` role on the database can create RLS and DDM policies, attach these policies to specific relations, and enable RLS on a relation.

### Column-level access control:

You can grant or revoke specific privileges on individual columns of a table or view.

```
GRANT SELECT ON "sales_db@finance-catalog".sales_schema.sales_table(order_number, sales_date, purchase_amount, sale_amount) TO "IAMR:sales_revenue_analyst";

REVOKE UPDATE ON "sales_db@finance-catalog".sales_schema.us_sales_view(order_number, sales_date, purchase_amount, sale_amount) FROM "IAMR:sales_revenue_analyst";
```

### Row-level security (RLS):

You can turn on or off row-level security for a relation.

```
ALTER TABLE "sales_db@finance-catalog".sales_schema.sales_table ROW LEVEL SECURITY ON;
```

You can create, alter, drop RLS policy on the database.

```
-- Create an RLS policy
CREATE RLS POLICY "sales_db@finance-catalog".policy_america
WITH (region VARCHAR(10))
USING (region = 'USA');

-- Alter an RLS policy
ALTER RLS POLICY "sales_db@finance-catalog".policy_america
USING (region IN ('USA', 'CANADA', 'Mexico'));

-- Drop an RLS policy
DROP RLS POLICY "sales_db@finance-catalog".policy_america;
```

You can attach or detach an RLS policy on a relation.

```
-- Attach an RLS policy
ATTACH RLS POLICY "sales_db@finance-catalog".policy_america
ON "sales_db@finance-catalog".sales_schema.sales_table
TO "IAMR:america_sales_analyst";

-- Detach an RLS policy
DETACH RLS POLICY "sales_db@finance-catalog".policy_america
ON "sales_db@finance-catalog".sales_schema.sales_view_america
FROM "IAMR:global_sales_analyst";
```

### Dynamic data masking (DDM):

You can create, alter, drop masking policy on the database.

```
-- Create a masking policy
CREATE MASKING POLICY "sales_db@finance-catalog".hash_credit
WITH (credit_card varchar(256))
USING (sha2(credit_card + 'testSalt', 256));

-- Alter an masking policy
ALTER MASKING POLICY "sales_db@finance-catalog".hash_credit
USING (sha2(credit_card + 'otherTestSalt', 256));

-- Drop an masking policy
DROP MASKING POLICY "sales_db@finance-catalog".hash_credit;
```

You can attach or detach a masking policy on a relation.

```
-- Attach a masking policy
 ATTACH MASKING POLICY hash_credit
ON "sales_db@finance-catalog".sales_schema.transaction_table (credit_card)
TO "IAMR:sales_analyst" PRIORITY 30;

-- Detach a masking policy
DETACH MASKING POLICY hash_credit
ON "sales_db@finance-catalog".sales_schema.transaction_view (credit_card)
FROM "IAMR:transaction_analyst";
```

A superuser or a user with the `sys:secadmin` privilege can view RLS and DDM policies, as well as their attachments on a relation with federated permissions, by using the [SHOW POLICIES](r_SHOW_POLICIES.md "r_SHOW_POLICIES.md") command.

###### Note

- User defined functions (UDF) in RLS, DDM policy definitions are not supported with Amazon Redshift federated permissions.
- Redshift SQL functions user_is_member_of, role_is_member_of, user_is_member_of_role are not supported with Amazon Redshift federated permissions.

### Permissions you can grant on Amazon Redshift federated permissions catalog

SQL statements to support permission management on database with Amazon Redshift federated permission on resources at different levels of granularity. The syntax supports both local table references (when connected to the database containing the resource or when the source database is in USE) and fully qualified cross-database references.

**Note**

- `username` can refer to an IAM user, IAM role, or IdC (AWS IAM Identity Center) user.
- `role_name` can refer to an IdC group. IAM groups are not supported.

#### Coarse Grained Permissions

```
GRANT { SELECT | INSERT | UPDATE | DELETE | TRUNCATE} ON
[ TABLE ] { table_name | database@catalog.schema_name.table_name }
TO { username | ROLE role_name | PUBLIC }

REVOKE { SELECT | INSERT | UPDATE | DELETE | TRUNCATE } ON
[ TABLE ] { table_name | database@catalog.schema_name.table_name }
FROM { username | ROLE role_name | PUBLIC }

```

#### Column Level Privileges

```
GRANT { { SELECT | UPDATE | DELETE }
( column_name [, ...] ) [, ...] | ALL [ PRIVILEGES ] ( column_name [,...] ) }
ON { table_name | database@catalog.schema_name.table_name }
TO { username | ROLE role_name | PUBLIC }

REVOKE { { SELECT | UPDATE | DELETE }
( column_name [, ...] ) [, ...] | ALL [ PRIVILEGES ] ( column_name [,...] ) }
ON { table_name | database@catalog.schema_name.table_name }
FROM { username | ROLE role_name | PUBLIC }

```

### Scoped Permissions

```
GRANT { CREATE | USAGE | ALTER | DROP } [,...] | ALL [ PRIVILEGES ] }
FOR SCHEMAS IN
DATABASE `database@catalog`
TO { `username` [ WITH GRANT OPTION ] | ROLE `role_name` } [, ...]

GRANT
{ { SELECT | INSERT | UPDATE | DELETE | DROP | ALTER | TRUNCATE | REFERENCES } [, ...] } | ALL [ PRIVILEGES ] } }
FOR TABLES IN
{ SCHEMA `schema_name` [DATABASE `database@catalog` ] | DATABASE `database@catalog` }
TO { `username` [ WITH GRANT OPTION ] | ROLE `role_name` } [, ...]

REVOKE [ GRANT OPTION ] { CREATE | USAGE | ALTER | DROP } [,...] | ALL [ PRIVILEGES ] }
FOR SCHEMAS IN
DATABASE `database@catalog`
FROM { `username` | ROLE `role_name` } [, ...]

REVOKE [ GRANT OPTION ] { { SELECT | INSERT | UPDATE | DELETE | DROP | ALTER | TRUNCATE | REFERENCES } [, ...] } | ALL [ PRIVILEGES ] } }
FOR TABLES IN
{ SCHEMA `schema_name` [ DATABASE `database@catalog` ] | DATABASE `database@catalog` }
FROM { `username` | ROLE `role_name` } [, ...]

```
