

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# CREATE RLS POLICY
<a name="r_CREATE_RLS_POLICY"></a>

Creates a new row-level security policy to provide granular access to database objects.

Superusers and users or roles that have the sys:secadmin role can create a policy.

## Syntax
<a name="r_CREATE_RLS_POLICY-synopsis"></a>

```
CREATE RLS POLICY { policy_name | database_name.policy_name }
[ WITH (column_name data_type [, ...]) [ [AS] relation_alias ] ]
USING ( using_predicate_exp )
```

## Parameters
<a name="r_CREATE_RLS_POLICY-parameters"></a>

 *policy\_name*   
The name of the policy.

database\_name  
The database name of where the policy will be created. Policy can be created on the connected database or on a database that supports Amazon Redshift federated permissions.

WITH (*column\_name data\_type [, ...]*)   
Specifies the *column\_name* and *data\_type* referenced to the columns of tables to which the policy is attached.   
You can omit the WITH clause only when the RLS policy doesn't reference any columns of tables to which the policy is attached.

AS *relation\_alias*  
Specifies an optional alias for the table that the RLS policy will be attached to.

USING (* using\_predicate\_exp *)  
Specifies a filter that is applied to the WHERE clause of the query. Amazon Redshift applies a policy predicate before the query-level user predicates. For example, **current\_user = ‘joe’ and price > 10** limits Joe to see only records with the price greater than $10.

For the usage of CREATE RLS POLICY on Amazon Redshift Federated Permissions Catalog, see [ Managing access control with Amazon Redshift federated permissions](https://docs.aws.amazon.com/redshift/latest/dg/federated-permissions-managing-access.html).

## Usage notes
<a name="r_CREATE_RLS_POLICY-usage"></a>

When working with the CREATE RLS POLICY statement, observe the following:
+ Amazon Redshift supports filters that can be part of a WHERE clause of a query.
+ All policies being attached to a table must have been created with the same table alias.
+ You must use the GRANT and REVOKE statements to explicitly grant and revoke SELECT permissions to RLS policies that reference lookup tables. A lookup table is a table object used inside a policy definition. For more information, see [GRANT](r_GRANT.md) and [REVOKE](r_REVOKE.md). 
+ Amazon Redshift row-level security doesn't support the following object types inside a policy definition: catalog tables, cross-database relations, external tables, regular views, late-binding views, tables with RLS policies turned on, and temporary tables.

## Examples
<a name="r_CREATE_RLS_POLICY-examples"></a>

The following example creates an RLS policy called policy\_concerts. This policy applies to a VARCHAR(10) column called catgroup and and sets the USING filter to only return rows where the value of catgroup is `'Concerts'`.

```
CREATE RLS POLICY policy_concerts
WITH (catgroup VARCHAR(10))
USING (catgroup = 'Concerts');
```

For an end-to-end example of using RLS policies, see [Row-level security end-to-end example](t_rls-example.md).