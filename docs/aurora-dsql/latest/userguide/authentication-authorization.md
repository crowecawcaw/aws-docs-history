# Authentication and authorization for

Aurora DSQL

Aurora DSQL uses IAM roles and policies for cluster authorization. You associate IAM roles
with [PostgreSQL
database roles](https://www.postgresql.org/docs/current/user-manag.html "https://www.postgresql.org/docs/current/user-manag.html") for database authorization. This approach combines [benefits from
IAM](../../../IAM/latest/UserGuide/intro-iam-features.md "../../../IAM/latest/UserGuide/intro-iam-features.md") with [PostgreSQL privileges](https://www.postgresql.org/docs/current/user-manag.html "https://www.postgresql.org/docs/current/user-manag.html"). Aurora DSQL uses these features to provide a comprehensive
authorization and access policy for your cluster, database, and data.

## Managing your cluster

using IAM

To manage your cluster, use IAM for authentication and authorization:

**IAM authentication**

To authenticate your IAM identity when you manage Aurora DSQL clusters, you
must use IAM. You can provide authentication using the [AWS Management Console](../../../signin/latest/userguide/how-to-sign-in.md "../../../signin/latest/userguide/how-to-sign-in.md"), [AWS CLI](../../../cli/latest/userguide/cli-chap-configure.md "../../../cli/latest/userguide/cli-chap-configure.md"), or the
[AWS
SDK](../../../sdkref/latest/guide/access.md "../../../sdkref/latest/guide/access.md").

**IAM authorization**

To manage Aurora DSQL clusters, grant authorization using IAM actions for
Aurora DSQL. For example, to describe a cluster, make sure that your IAM identity
has permissions for the IAM action `dsql:GetCluster`, as in
the following sample policy action.

```
{
  "Effect": "Allow",
  "Action": "dsql:GetCluster",
  "Resource": "arn:aws:dsql:us-east-1:`123456789012`:cluster/`my-cluster`"
}
```

For more information, see [Using IAM policy
actions to manage clusters](#authentication-authorization-iam-policy-manage "#authentication-authorization-iam-policy-manage").

## Connecting to your

cluster using IAM

To connect to your cluster, use IAM for authentication and authorization:

**IAM authentication**

Generate a temporary authentication token using an IAM identity with
authorization to connect to your cluster. To learn more, see [Generating an authentication token in Amazon Aurora DSQL](SECTION_authentication-token.md "SECTION_authentication-token.md").

**IAM authorization**

Grant the following IAM policy actions to the IAM identity you’re
using to establish the connection to your cluster’s endpoint:

- Use `dsql:DbConnectAdmin` if you're using the
  `admin` role. Aurora DSQL creates and manages this role
  for you. The following sample IAM policy action permits
  `admin` to connect to
  `my-cluster`.

```
{
  "Effect": "Allow",
  "Action": "dsql:DbConnectAdmin",
  "Resource": "arn:aws:dsql:us-east-1:`123456789012`:cluster/`my-cluster`"
}
```

- Use `dsql:DbConnect` if you're using a custom database
  role. You create and manage this role by using SQL commands in your
  database. The following sample IAM policy action permits a custom
  database role to connect to `my-cluster`
  for up to one hour.

```
{
  "Effect": "Allow",
  "Action": "dsql:DbConnect",
  "Resource": "arn:aws:dsql:us-east-1:`123456789012`:cluster/`my-cluster`"
}
```

After you establish a connection, your role is authorized for up to one hour
for the connection.

## Interacting with

your database using PostgreSQL database roles and IAM roles

PostgreSQL manages database access permissions using the concept of roles. A role can
be thought of as either a database user, or a group of database users, depending on how
the role is set up. You create PostgreSQL roles using SQL commands. To manage
database-level authorization, grant PostgreSQL permissions to your PostgreSQL database
roles.

Aurora DSQL supports two types of database roles: an `admin` role and custom
roles. Aurora DSQL automatically creates a predefined `admin` role for you in your
Aurora DSQL cluster. You can't modify the `admin` role. When you connect to your
database as `admin`, you can issue SQL to create new database-level roles to
associate with your IAM roles. To let IAM roles connect to your database, associate
your custom database roles with your IAM roles.

**Authentication**

Use the `admin` role to connect to your cluster. After you
connect your database, use the command `AWS IAM GRANT` to
associate a custom database role with the IAM identity authorized to
connect to the cluster, as in the following example.

```
AWS IAM GRANT `custom-db-role` TO 'arn:aws:iam::`account-id`:role/`iam-role-name`';
```

To learn more, see [Authorizing
database roles to connect to your cluster](using-database-and-iam-roles.md#using-database-and-iam-roles-custom-database-roles "using-database-and-iam-roles.md#using-database-and-iam-roles-custom-database-roles").

**Authorization**

Use the `admin` role to connect to your cluster. Run SQL
commands to set up custom database roles and grant permissions. To learn
more, see [PostgreSQL
database roles](https://www.postgresql.org/docs/current/user-manag.html "https://www.postgresql.org/docs/current/user-manag.html") and [PostgreSQL
privileges](https://www.postgresql.org/docs/current/ddl-priv.html "https://www.postgresql.org/docs/current/ddl-priv.html") in the PostgreSQL documentation.

## Using IAM policy actions

with Aurora DSQL

The IAM policy action you use depends on the role you use to connect to your
cluster: either `admin` or a custom database role. The policy also depends on
the IAM actions required for this role.

### Using IAM policy

actions to connect to clusters

When you connect to your cluster with the default database role of
`admin`, use an IAM identity with authorization to perform the
following IAM policy action.

```
"dsql:DbConnectAdmin"
```

When you connect to your cluster with a custom database role, first associate the
IAM role with the database role. The IAM identity you use to connect to your
cluster must have authorization to perform the following IAM policy action.

```
"dsql:DbConnect"
```

To learn more about custom database roles, see [Using database roles and IAM authentication](using-database-and-iam-roles.md "using-database-and-iam-roles.md").

### Using IAM policy

actions to manage clusters

When managing your Aurora DSQL clusters, specify policy actions only for the actions
that your role needs to perform. For example, if your role only needs to get cluster
information, you might limit role permissions to only the `GetCluster`
and `ListClusters` permissions, as in the following sample policy

JSON

```
`{
"Version":"2012-10-17",
 "Statement" : [
 {
 "Effect" : "Allow",
 "Action" : [
 "dsql:GetCluster",
 "dsql:ListClusters"
 ],
 "Resource": "arn:aws:dsql:us-east-1:`123456789012`:cluster/`my-cluster`"
 }
 ]
}`

```

The following example policy shows all available IAM policy actions for managing
clusters.

JSON

```
`{
"Version":"2012-10-17",
 "Statement" : [
 {
 "Effect" : "Allow",
 "Action" : [
 "dsql:CreateCluster",
 "dsql:GetCluster",
 "dsql:UpdateCluster",
 "dsql:DeleteCluster",
 "dsql:ListClusters",
 "dsql:TagResource",
 "dsql:ListTagsForResource",
 "dsql:UntagResource"
 ],
 "Resource" : "*"
 }
 ]
}`

```

## Revoking authorization using IAM and PostgreSQL

You can revoke permissions for your IAM roles to access your database-level
roles:

**Revoking admin authorization to connect to
clusters**

To revoke authorization to connect to your cluster with the
`admin` role, revoke the IAM identity's access to
`dsql:DbConnectAdmin`. Either edit the IAM policy or detach
the policy from the identity.

After revoking connection authorization from the IAM identity, Aurora DSQL
rejects all new connection attempts from that IAM identity. Any active
connections that use the IAM identity might stay authorized for the
duration of the connection. For more information on connection durations, see [Quotas and limits](CHAP_quotas.md "CHAP_quotas.md").

**Revoking custom role authorization to connect to
clusters**

To revoke access to database roles other than `admin`, revoke
the IAM identity’s access to `dsql:DbConnect`. Either edit the
IAM policy or detach the policy from the identity.

You can also remove the association between the database role and IAM by
using the command `AWS IAM REVOKE` in your database. To learn
more about revoking access from database roles, see [Revoking database
authorization from an IAM role](using-database-and-iam-roles.md#using-database-and-iam-roles-revoke "using-database-and-iam-roles.md#using-database-and-iam-roles-revoke").

You can't manage permissions of the predefined `admin` database role. To
learn how to manage permissions for custom database roles, see [PostgreSQL
privileges](https://www.postgresql.org/docs/current/ddl-priv.html "https://www.postgresql.org/docs/current/ddl-priv.html"). Modifications to privileges take effect on the next transaction
after Aurora DSQL successfully commits the modification transaction.
