# Using database roles and IAM authentication

Aurora DSQL supports authentication using both IAM roles and IAM users. You can use either method to authenticate and access Aurora DSQL databases.

## IAM roles

An IAM role is an identity within your AWS account that has specific permissions but is not associated with a specific person. Using IAM roles provide temporary security credentials. You can temporarily assume an IAM role in several ways:

- By switching roles in the AWS Management Console
- By calling an AWS CLI or AWS API operation
- By using a custom URL

After assuming a role, you can access Aurora DSQL using the role's temporary credentials. For more information about methods for using roles, see [IAM Identities](../../../IAM/latest/UserGuide/id.md "../../../IAM/latest/UserGuide/id.md") in the _IAM user guide_.

## IAM users

An IAM user is an identity within your AWS account that has specific
permissions and is associated with a single person or application. IAM users
have long-term credentials such as passwords and access keys that can be used to
access Aurora DSQL.

###### Note

To run SQL commands with IAM authentication, you can use either IAM role ARNs
or IAM user ARNs in the examples below.

## Authorizing

database roles to connect to your cluster

Create an IAM role and grant connection authorization with the IAM policy action:
`dsql:DbConnect`.

The IAM policy must also grant permission to access the cluster resources. Use a
wildcard (`*`) or follow the instructions in [Using IAM condition keys with Amazon Aurora DSQL](using-iam-condition-keys.md#using-iam-condition-keys-create-cluster "using-iam-condition-keys.md#using-iam-condition-keys-create-cluster").

## Authorizing

database roles to use SQL in your database

You must use an IAM role with authorization to connect to your cluster.

1. Connect to your Aurora DSQL cluster using a SQL utility.

Use the `admin` database role with an IAM identity that is
authorized for IAM action `dsql:DbConnectAdmin` to connect to
your cluster. 2. Create a new database role, making sure to specify the `WITH
 LOGIN` option.

```
CREATE ROLE example WITH LOGIN;
```

3. Associate the database role with the IAM role ARN.

```
AWS IAM GRANT example TO 'arn:aws:iam::`012345678912`:role/`example`';
```

4. Grant database-level permissions to the database role

The following examples use the `GRANT` command to provide
authorization within the database.

```
GRANT USAGE ON SCHEMA myschema TO example;
GRANT SELECT, INSERT, UPDATE ON ALL TABLES IN SCHEMA myschema TO example;
```

For more information, see [PostgreSQL
`GRANT`](https://www.postgresql.org/docs/current/sql-grant.html "https://www.postgresql.org/docs/current/sql-grant.html") and [PostgreSQL
Privileges](https://www.postgresql.org/docs/current/ddl-priv.html "https://www.postgresql.org/docs/current/ddl-priv.html") in the PostgreSQL documentation.

## Viewing IAM to database role mappings

To view the mappings between IAM roles and database roles, query the `sys.iam_pg_role_mappings` system table.

```
SELECT * FROM sys.iam_pg_role_mappings;
```

Example output:

```
 iam_oid |                  arn                   | pg_role_oid | pg_role_name | grantor_pg_role_oid | grantor_pg_role_name
---------+----------------------------------------+-------------+--------------+---------------------+----------------------
   26398 | arn:aws:iam::012345678912:role/example |       26396 | example      |               15579 | admin
(1 row)
```

This table shows all the mappings between IAM roles (identified by their ARN) and PostgreSQL database roles.

## Revoking database

authorization from an IAM role

To revoke database authorization, use the `AWS IAM REVOKE`
operation.

```
AWS IAM REVOKE example FROM 'arn:aws:iam::`012345678912`:role/`example`';
```

To learn more about revoking authorization, see [Revoking authorization using IAM and PostgreSQL](authentication-authorization.md#authentication-authorization-revoke "authentication-authorization.md#authentication-authorization-revoke").
