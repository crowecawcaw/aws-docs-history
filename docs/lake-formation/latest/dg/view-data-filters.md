# Viewing data filters

You can use the Lake Formation console, AWS CLI, or the Lake Formation API to view data filters.

To view data filters, you must be a Data Lake administrator or have the required
permissions on the data filters.

Console

1. Sign in to the AWS Management Console and open the Lake Formation console at
   [https://console.aws.amazon.com/lakeformation/](https://console.aws.amazon.com/lakeformation/ "https://console.aws.amazon.com/lakeformation/").
2. In the navigation pane, under **Data catalog**, choose
   **Data filters**.

The page displays the data filters you have access to.

![The Data filters page displays the available data filters with the following columns: Filter name, Table, Database, and Table catalog ID. The screenshot shows a single data filter with the following values: test-df, cloudtrailtest_cloudtrail, lakeformation_cloudtrail, redacted account ID. Above the table there are four buttons (from left to right): Refresh/reload, View (grayed out), Delete (grayed out), and "Create new filter". There is also a search field, which is empty.](images/list-data-filters.jpg) 3. To view the data filter details, choose the data filter, and then choose View. A
new window appears with the data filter detailed information.

![The "View data filter" window shows additional information about the selected data filter. The information displayed includes the name, database, table, column-level access setting, row filter expression, and the columns.](images/list-data-filters-details.jpg)

AWS CLI
Enter a `list-data-cells-filter` command and specify a table
resource.

The following example lists the data filters for the
`cloudtrailtest_cloudtrail` table.

```
aws lakeformation list-data-cells-filter --table '{ "CatalogId":"123456789012",
"DatabaseName":"lakeformation_cloudtrail", "Name":"cloudtrailtest_cloudtrail"}'
```

API/SDK
Use the `ListDataCellsFilter` API and specify a table resource.

The following example uses Python to list the first 20 data filters for the
`myTable` table.

```
response = client.list_data_cells_filter(
    Table = {
        'CatalogId': '111122223333',
        'DatabaseName': 'mydb',
        'Name': 'myTable'
    },
    MaxResults=20
)

```
