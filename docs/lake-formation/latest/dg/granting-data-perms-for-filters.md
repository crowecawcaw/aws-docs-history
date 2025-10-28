# Granting data permissions provided by data

filters

Data filters represent a subset of data within a table. To provide data access to
principals, `SELECT` permissions need to be granted to those principals. With this
permission the principals can:

- View the actual table name in list of tables shared with their account.
- Create data filters on the shared table and grant permissions to their users on those
  data filters.

Console

###### To grant SELECT permissions

1. Go to the **Permissions** page in the Lake Formation console, and then
   choose **Grant**.

![The image is a screenshot of the top page of the Permissions page in the console. In the Data Permissions section, the Grant button is highlighted.](images/permissions-grant-action.png) 2. Select the principals you want to provide access to, and select **Named
data catalog resources**.

![The image is a screenshot of the Permissions page in the console. The "LF-Tags or catalog resources" section is shown, with the "Named data catalog resources" option selected. Under Databases, there is one value provided: cloudtrail. For Tables, there is one value provided: cloudtrail-logs-aws_logs. For Data Filters, there is one value provided: cloudtrail_lakeformation_filter.](images/grant-data-filter-perms-step2.png) 3. To provide access to the data that the filter represents, choose
**Select** under **Data filter
permissions**.

![The image is a screenshot of the top page of the Permissions page in the console. In the "Data filter permissions" section, the SELECT option is selected. The DESCRIBE and DROP options are not selected. In the "Grantable permissions" section, none of the options are selected (Select, Describe, Drop). There is an informational message at the bottom of the screenshot which says "Select permissions on data filters will grant access to the table 'cloudtrail_logs_awslogs'."](images/grant-data-filter-perms-step3.png)

CLI
Enter a `grant-permissions` command. Specify `DataCellsFilter`
for the resource argument, and specify `SELECT` for the Permissions argument.

The following example grants `SELECT` with the grant option to user
`datalake_user1` on the data filter `restrict-pharma`, which
belongs to the `orders` table in the `sales` database in
AWS account `1111-2222-3333`.

```
aws lakeformation grant-permissions --cli-input-json file://grant-params.json
```

The following are the contents of file `grant-params.json`.

```
{
    "Principal": {
        "DataLakePrincipalIdentifier": "arn:aws:iam::111122223333:user/datalake_user1"
    },
    "Resource": {
        "DataCellsFilter": {
            "TableCatalogId": "111122223333",
            "DatabaseName": "sales",
            "TableName": "orders",
            "Name": "restrict-pharma"
        }
    },
    "Permissions": ["SELECT"]
}
```
