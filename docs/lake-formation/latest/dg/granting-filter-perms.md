# Granting data filter permissions

You can grant the `SELECT`, `DESCRIBE` and `DROP` Lake Formation
permissions on data filters to principals.

At first, only you can view the data filters that you create for a table. To enable another
principal to view a data filter and grant Data Catalog permissions with the data filter, you must
either:

- Grant `SELECT` on a table to the principal with the grant option, and apply
  the data filter to the grant.
- Grant the `DESCRIBE` or `DROP` permission on the data filter to the
  principal.
  You can grant the `SELECT` permission to an external AWS account. A data
  lake administrator in that account can then grant that permission to other principals in the
  account. When granting to an external account, you must include the grant option so that
  administrator of the external account can further cascade the permission to other users in
  his/her account. When granting to a principal in your account, granting with the grant option
  is optional.

You can grant and revoke permissions on data filters by using the AWS Lake Formation console, the API,
or the AWS Command Line Interface (AWS CLI).

Console

1. Sign in to the AWS Management Console and open the Lake Formation console at
   [https://console.aws.amazon.com/lakeformation/](https://console.aws.amazon.com/lakeformation/ "https://console.aws.amazon.com/lakeformation/").
2. In the navigation pane, under **Permissions**, choose
   **Data lake permissions**.
3. On the **Permissions** page, in the **Data
   permissions** section, choose **Grant**.
4. On the **Grant data permissions** page, choose the principals
   to grant the permissions to.
5. In the LF-Tags or catalog resources section, choose **Named data catalog
   resources**. Then choose the database, table, and data filter for which
   you want to grant permissions.

![The image is a screenshot of the Permissions page in the console. The "LF-Tags or catalog resources" section is shown, with the "Named data catalog resources" option selected. Under Databases, there is one value provided: cloudtrail. For Tables, there is one value provided: cloudtrail-logs-aws_logs. For data filters, there is one value provided: cloudtrail_lakeformation_filter.](images/grant-data-filter-perms-step2.png) 6. In the **Data filter permissions** section, choose the
permissions you want to grant to the selected principals.

![The image is a screenshot of the Data filter permissions section on the Permissions page in the Lake Formation console. For "Data filter permissions", the Select permission is not selected, and the Describe and Drop permissions are selected. Under "Grantable permissions", none of the permissions are selected (Select, Describe, Drop).](images/grant-perms-on-filters.png)

AWS CLI

- Enter a `grant-permissions` command. Specify `DataCellsFilter`
  for the `resource` argument, and specify `DESCRIBE` or
  `DROP` for the `Permissions` argument and, optionally, for the
  `PermissionsWithGrantOption` argument.

The following example grants `DESCRIBE` with the grant option to
user `datalake_user1` on the data filter `restrict-pharma`,
which belongs to the `orders` table in the `sales` database in
AWS account 1111-2222-3333.

```
aws lakeformation grant-permissions --cli-input-json file://grant-params.json
```

The following are the contents of file `grant-params.json`.

```
{
    "Principal": {"DataLakePrincipalIdentifier": "arn:aws:iam::111122223333:user/datalake_user1"},
    "Resource": {
        "DataCellsFilter": {
            "TableCatalogId": "111122223333",
            "DatabaseName": "sales",
            "TableName": "orders",
            "Name": "restrict-pharma"
        }
    },
    "Permissions": ["DESCRIBE"],
    "PermissionsWithGrantOption": ["DESCRIBE"]
}
```
