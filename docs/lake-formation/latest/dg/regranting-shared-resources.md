# Granting permissions on a database or table shared

with your account

After a Data Catalog resource belonging to another AWS account is shared with your AWS
account, as a data lake administrator, you can grant permissions on the shared resource to other
principals in your account. You can't, however, grant permissions on the resource to other AWS
accounts or organizations.

You can use the AWS Lake Formation console, the API, or the AWS Command Line Interface (AWS CLI) to grant the
permissions.

###### To grant permissions on a shared database (named resource method, console)

- Follow the instructions in [Granting database permissions using the
  named resource method](granting-database-permissions.md "granting-database-permissions.md"). In the **Database** list
  under **LF-Tags or catalog resources**, ensure that you select the database
  in the external account, not a resource link for the database.

If you don't see the database in the list of databases, ensure that you have accepted the
AWS Resource Access Manager (AWS RAM) resource share invitation for the database. For more information, see [Accepting a resource share invitation from AWS RAM](accepting-ram-invite.md "accepting-ram-invite.md").

Also, for the `CREATE_TABLE` and `ALTER` permissions, follow the
instructions in [Granting data location permissions (same
account)](granting-location-permissions-local.md "granting-location-permissions-local.md"), and be sure to enter the owning
account ID in the **Registered account location** field.

###### To grant permissions on a shared table (named resource method, console)

- Follow the instructions in [Granting table permissions using the named resource method](granting-table-permissions.md "granting-table-permissions.md"). In the **Database** list
  under **LF-Tags or catalog resources**, ensure that you select the database
  in the external account, not a resource link for the database.

If you don't see the table in the list of tables, ensure that you have accepted the AWS RAM
resource share invitation for the table. For more information, see [Accepting a resource share invitation from AWS RAM](accepting-ram-invite.md "accepting-ram-invite.md").

Also, for the `ALTER` permission, follow the instructions in [Granting data location permissions (same
account)](granting-location-permissions-local.md "granting-location-permissions-local.md"), and be sure to enter the owning
account ID in the **Registered account location** field.

###### To grant permissions on shared resources (LF-TBAC method, console)

- Follow the instructions in [Granting Data Catalog permissions](granting-catalog-perms-TBAC.md#granting-cat-perms-TBAC-console "granting-catalog-perms-TBAC.md#granting-cat-perms-TBAC-console") . In the **LF-Tags or catalog
  resources** section, grant the exact LF-Tag expression that the external account
  granted to your account, or a subset of that expression.

For example, if an external account granted the LF-Tag expression
`module=customers AND environment=production` to your account with the grant
option, as a data lake administrator, you can grant that same expression, or
`module=customers` or `environment=production` to a principal in your
account. You can grant only the same or a subset of the Lake Formation permissions (for example,
`SELECT`, `ALTER`, and so on) that were granted on resources through
the LF-Tag expression.

###### To grant permissions on a shared table (named resource method, AWS CLI)

- Enter a command similar to the following. In this example:
  - Your AWS account ID is 1111-2222-3333.
  - The account that owns the table and that granted it to your account is
    1234-5678-9012.
  - The `SELECT` permission is being granted on the shared table
    `pageviews` to user `datalake_user1`. That user is a principal in
    your account.
  - The `pageviews` table is in the `analytics` database, which is
    owned by account 1234-5678-9012.

```
aws lakeformation grant-permissions --principal DataLakePrincipalIdentifier=arn:aws:iam::111122223333:user/datalake_user1 --permissions "SELECT" --resource '{ "Table": {"CatalogId":"123456789012", "DatabaseName":"analytics", "Name":"pageviews"}}'
```

Note that the owning account must be specified in the `CatalogId` property in
the `resource` argument.
