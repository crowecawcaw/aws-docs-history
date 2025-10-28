# Viewing database and table permissions in Lake Formation

You can view the Lake Formation permissions that are granted on a Data Catalog database or table. You can
do so by using the Lake Formation console, the API, or the AWS Command Line Interface (AWS CLI).

Using the console, you can view permissions starting from the **Databases**
or **Tables** pages, or from the **Data permissions**
page.

###### Note

If you're not a database administrator or resource owner, you can view permissions that
other principals have on the resource only if you have a Lake Formation permission on the resource with
the grant option.

In addition to the required Lake Formation permissions, you need the AWS Identity and Access Management (IAM) permissions
`glue:GetDatabases`, `glue:GetDatabase`, `glue:GetTables`,
`glue:GetTable`, and `lakeformation:ListPermissions`.

###### To view permissions on a database (console, starting from the Databases page)

1. Open the Lake Formation console at
   [https://console.aws.amazon.com/lakeformation/](https://console.aws.amazon.com/lakeformation/ "https://console.aws.amazon.com/lakeformation/").

Sign in as a data lake administrator, the database creator, or as a user who has any
Lake Formation permission on the database with the grant option. 2. In the navigation pane, choose **Databases**. 3. Choose a database, and on the **Actions** menu, choose **View
permissions**.

###### Note

If you choose a database resource link, Lake Formation displays the permissions on the resource
link, not on the target database of the resource link.

The **Data permissions** page lists all Lake Formation permissions for the
database. The database name and catalog ID (AWS account ID) of the database owner appear
as labels under the search box. The tiles indicate that a filter has been applied to list
permissions only for that database. You can adjust the filter by closing a tile or choosing
**Clear filter**.

![The Data permissions page displays a search box at the top, with two tiles underneath. The tiles are labeled Database:logs and Catalog ID:111122223333. Next to the tiles is a Clear filter button. Below is the list of databases and their permissions. This example has only one row in the list. It's for the logs database, and the permissions Alter, Create table, and Drop are granted to IAM user Administrator with the grant option. The list includes an Owner account ID column, and the one row has 11112222333 in that column.](images/permissions-page-database.png)

###### To view permissions on a database (console, starting from the Data permissions

page)

1. Open the Lake Formation console at
   [https://console.aws.amazon.com/lakeformation/](https://console.aws.amazon.com/lakeformation/ "https://console.aws.amazon.com/lakeformation/").

Sign in as a data lake administrator, the database creator, or as a user who has any
Lake Formation permission on the database with the grant option. 2. In the navigation pane, choose **Data permissions**. 3. Position the cursor in the search box at the top of the page, and on the
**Properties** menu that appears, choose
**Database**. 4. On the **Databases** menu that appears, choose a database.

###### Note

If you choose a database resource link, Lake Formation displays the permissions on the resource
link, not on the target database of the resource link.

The **Data permissions** page lists all Lake Formation permissions for the
database. The database name appears as a tile under the search box. The tile indicates that
a filter has been applied to list permissions only for that database. You can remove the
filter by closing the tile or choosing **Clear filter**.

###### To view permissions on a table (console, starting from the Tables page)

1. Open the Lake Formation console at
   [https://console.aws.amazon.com/lakeformation/](https://console.aws.amazon.com/lakeformation/ "https://console.aws.amazon.com/lakeformation/").

Sign in as a data lake administrator, the table creator, or as a user who has any Lake Formation
permission on the table with the grant option. 2. In the navigation pane, choose **Tables**. 3. Choose a table, and on the **Actions** menu, choose **View
permissions**.

###### Note

If you choose a table resource link, Lake Formation displays the permissions on the resource
link, not on the target table of the resource link.

The **Data permissions** page lists all Lake Formation permissions for the table.
The table name, the database name of the database that contains the table, and the catalog
ID (AWS account ID) of the table owner appear as labels under the search box. The labels
indicate that a filter has been applied to list permissions only for that table. You can
adjust the filter by closing a label or choosing **Clear filter**.

![The Data permissions page displays a search field at the top, with three tiles underneath. The tiles are labeled Database:logs, Table:alexa-logs, and Catalog ID:111122223333, going from left to right. Next to the tiles is a Clear filter button. Below is the list of tables and their permissions. This example has only one row in the list. It's for the alexa-logs table, and the Super permissions is granted to IAM user Administrator with the grant option. The list includes an Owner account ID column, and the one row has 11112222333 in that column.](images/permissions-page-table.png)

###### To view permissions on a table (console, starting from the Data permissions page)

1. Open the Lake Formation console at
   [https://console.aws.amazon.com/lakeformation/](https://console.aws.amazon.com/lakeformation/ "https://console.aws.amazon.com/lakeformation/").

Sign in as a data lake administrator, the table creator, or as a user who has any Lake Formation
permission on the table with the grant option. 2. In the navigation pane, choose **Data permissions**. 3. Position the cursor in the search box at the top of the page, and on the
**Properties** menu that appears, choose
**Database**. 4. On the **Databases** menu that appears, choose a database.

###### Important

If you want to view permissions on a table that was shared with your AWS account
from an external account, you must choose the database in the external account that
contains the table, not a resource link to the database.

The **Data permissions** page lists all Lake Formation permissions for the
database. 5. Position the cursor in the search box again, and on the **Properties**
menu that appears, choose **Table**. 6. On the **Tables** menu that appears, choose a table.

The **Data permissions** page lists all Lake Formation permissions for the table.
The table name and the database name of the database that contains the table appear as tiles
under the search box. The tiles indicate that a filter has been applied to list permissions
only for that table. You can adjust the filter by closing a tile or choosing **Clear
filter**.

###### To view permissions on a table (AWS CLI)

- Enter a `list-permissions` command.

The following example lists permissions on a table shared from an external account. The
`CatalogId` property is the AWS account ID of the external account, and the
database name refers to the database in the external account that contains the table.

```
aws lakeformation list-permissions  --resource-type TABLE --resource '{ "Table": {"DatabaseName":"logs", "Name":"alexa-logs", "CatalogId":"123456789012"}}'
```
