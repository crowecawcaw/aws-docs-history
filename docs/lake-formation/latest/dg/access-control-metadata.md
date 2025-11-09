# Metadata access control

For access control for Data Catalog resources, the following discussion assumes fine-grained
access control with Lake Formation permissions and coarse-grained access control with IAM
policies.

There are two distinct methods for granting Lake Formation permissions on Data Catalog
resources:

- Named resource access control – With this
  method, you grant permissions on specific databases or tables by specifying database or
  table names. The grants have this form:

Grant _permissions_ to _principals_ on _resources_ [with grant
option].

With the grant option, you can allow the grantee to grant the permissions to other
principals.

- Tag-based access control – With this method,
  you assign one or more LF-Tags to Data Catalog
  databases, tables, and columns, and grant permissions on one or more LF-Tags to principals.
  Each LF-Tag is a key-value pair, such as `department=sales`. A principal
  that has LF-Tags that match the LF-Tags on a Data Catalog resource can access that resource. This
  method is recommended for data lakes with a large number of databases and tables. It's
  explained in detail in [Lake Formation tag-based access control](tag-based-access-control.md "tag-based-access-control.md").
  The permissions that a principal has on a resource is the union of the permissions
  granted by both the methods.

The following table summarizes the available Lake Formation permissions on Data Catalog resources. The
column headings indicate the resource on which the permission is granted.

| Catalog           | Database       | Table      |
| ----------------- | -------------- | ---------- |
| `CREATE_DATABASE` | `CREATE_TABLE` | `ALTER`    |
|                   | `ALTER`        | `DROP`     |
|                   | `DROP`         | `DESCRIBE` |
|                   | `DESCRIBE`     | `SELECT`\* |
|                   |                | `INSERT`\* |
|                   |                | `DELETE`\* |

For example, the `CREATE_TABLE` permission is granted on a database. This
means that the principal is allowed to create tables in that database.

The permissions with an asterisk (\*) are granted on Data Catalog resources, but they apply to
the underlying data. For example, the `DROP` permission on a metadata table
enables you to drop the table from the Data Catalog. However, the `DELETE` permission
granted on the same table enables you to delete the table's underlying data in Amazon S3, using,
for example, a SQL `DELETE` statement. With these permissions, you also can view
the table on the Lake Formation console and retrieve information about the table with the AWS Glue API.
Thus, `SELECT`, `INSERT`, and `DELETE` are both Data Catalog
permissions and data access permissions.

When granting `SELECT` on a table, you can add a filter that includes or
excludes one or more columns. This permits fine-grained access control on metadata table
columns, limiting the columns that users of integrated services can see when running
queries. This capability is not available using just IAM policies.

There is also a special permission named `Super`. The `Super`
permission enables a principal to perform every supported Lake Formation operation on the database or
table on which it is granted. This permission can coexist with the other Lake Formation permissions.
For example, you can grant `Super`, `SELECT`, and `INSERT`
on a metadata table. The principal can perform all supported actions on the table, and when
you revoke `Super`, the `SELECT` and `INSERT` permissions
remain.

For details on each permission, see [Lake Formation permissions reference](lf-permissions-reference.md "lf-permissions-reference.md").

###### Important

To be able to see a Data Catalog table created by another user, you must be granted at
least one Lake Formation permission on the table. If you are granted at least one permission on the
table, you can also see the table's containing database.

You can grant or revoke Data Catalog permissions using the Lake Formation console, the API, or the
AWS Command Line Interface (AWS CLI). The following is an example of an AWS CLI command that grants the user
`datalake_user1` permission to create tables in the `retail`
database.

```
aws lakeformation grant-permissions --principal DataLakePrincipalIdentifier=arn:aws:iam::111122223333:user/datalake_user1
 --permissions "CREATE_TABLE" --resource '{ "Database": {"Name":"retail"}}'
```

The following is an example of a coarse-grained access control IAM policy that
complements fine-grained access control with Lake Formation permissions. It permits all operations on
any metadata database or table.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "glue:*Database*",
 "glue:*Table*",
 "glue:*Partition*"
 ],
 "Resource": "*"
 }
 ]
}`

```

The next example is also coarse-grained but somewhat more restrictive. It permits
read-only operations on all metadata databases and tables in the Data Catalog in the designated
account and Region.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "glue:GetTables",
 "glue:SearchTables",
 "glue:GetTable",
 "glue:GetDatabase",
 "glue:GetDatabases"
 ],
 "Resource": "arn:aws:glue:us-east-1:111122223333:*"
 }
 ]
}`

```

Compare these policies to the following policy, which implements IAM-based
fine-grained access control. It grants permissions only on a subset of tables in the
customer relationship management (CRM) metadata database in the designated account and
Region.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "glue:GetTables",
 "glue:SearchTables",
 "glue:GetTable",
 "glue:GetDatabase",
 "glue:GetDatabases"
 ],
 "Resource": [
 "arn:aws:glue:us-east-1:111122223333:catalog",
 "arn:aws:glue:us-east-1:111122223333:database/CRM",
 "arn:aws:glue:us-east-1:111122223333:table/CRM/P*"
 ]
 }
 ]
}`

```

For more examples of coarse-grained access control policies, see [Lake Formation personas and IAM permissions reference](permissions-reference.md "permissions-reference.md").
