# Listing data filter permissions

You can use the Lake Formation console to view the permissions granted on data filters.

To view permissions on a data filter, you must be a Data Lake administrator or have the
required permissions on the data filter.

Console

1. Sign in to the AWS Management Console and open the Lake Formation console at
   [https://console.aws.amazon.com/lakeformation/](https://console.aws.amazon.com/lakeformation/ "https://console.aws.amazon.com/lakeformation/").
2. In the navigation pane, under **Permissions**, choose
   **Data permissions**.
3. On the **Data Permissions** page, click or tap in the search
   field, and on the **Properties** menu, choose **Resource
   type**.
4. On the **Resource type** menu, choose **Resource type:
   Data cell filter**.

The data filters that you have permissions on are listed. You might have to
scroll horizontally to see the **Permissions** and
**Grantable** columns.

![The Data Permissions page displays a table of permissions with the following columns: Principal, Resource type, Database, Table, Resource, Catalog, and Permissions. The Resource type column shows "Data cell filter" in all four rows. The permissions for the first and second rows are Describe, Drop, and Select. The permissions for the third row is Describe. Above the table is a Clear filter button and a tile indicating that the current search is for Resource type: Data cell filter. Above those is a search (text) field, and above that are Refresh, Revoke, and Grant buttons.](images/data-permissions-cell-filters.png)

AWS CLI

- Enter a `list-permissions` command. Specify
  `DataCellsFilter` for the `resource` argument, and specify
  `DESCRIBE` or `DROP` for the `Permissions`
  argument and, optionally, for the `PermissionsWithGrantOption`
  argument.

The following example lists `DESCRIBE` permissions with the grant
option on the data filter `restrict-pharma`. The results are limited to
permissions granted for the principal `datalake_user1` and the
`orders` table in the `sales` database in AWS account
1111-2222-3333.

```
aws lakeformation list-permissions --cli-input-json file://list-params.json
```

The following are the contents of file
`grant-params.json`.

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
