# View properties for widgets

This section describes the configurable view properties for the 4 view types: table, line chart, pie chart, and bar chart.

###### View types:

- [Table](#lake-widget-table "#lake-widget-table")
- [Line chart](#lake-widget-linechart "#lake-widget-linechart")
- [Pie chart](#lake-widget-piechart "#lake-widget-piechart")
- [Bar chart](#lake-widget-barchart "#lake-widget-barchart")

## Table

The following example shows a widget configured as a table.

```
{
    "ViewProperties": {
       "Height": "2",
       "Width": "4",
       "Title": "TopErrors",
       "View": "Table"
    },
    "QueryStatement": "SELECT errorCode, COUNT(*) AS eventCount FROM eds WHERE eventTime > '?' AND eventTime < '?' AND (errorCode is not null) GROUP BY errorCode ORDER BY eventCount DESC LIMIT 100",
    "QueryParameters": ["$StartTime$", "$EndTime$"]
}
```

The following table describes the configurable view properties for a table.

| Parameter      | Required | Value                                                                                                   |
| -------------- | -------- | ------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `Height`       | Yes      | The height of the table in inches.                                                                      |
| `Width`        | Yes      | The width of the table in inches.                                                                       |
| `Title`        | Yes      | The title of the table.                                                                                 |
| `View`         | Yes      | The widget view type. For a table, the value is `Table`.                                                | ## Line chart The following example shows a widget configured as a line chart. `{ "ViewProperties": { "Height": "2", "Width": "4", "Title": "AccountActivity", "View": "LineChart", "YAxisColumn": "eventCount", "XAxisColumn": "eventDate", "FilterColumn": "readOnly" }, "QueryStatement": "SELECT DATE_TRUNC('?', eventTime) AS eventDate, IF(readOnly, 'read', 'write') AS readOnly, COUNT(*) as eventCount FROM eds WHERE eventTime > '?' AND eventTime < '?' GROUP BY DATE_TRUNC('?', eventTime), readOnly ORDER BY DATE_TRUNC('?', eventTime), readOnly", "QueryParameters": ["$Period$", "$StartTime$", "$EndTime$", "$Period$", "$Period$"] }` The following table describes the configurable view properties for a line chart. |
| Parameter      | Required | Value                                                                                                   |
| ---            | ---      | ---                                                                                                     |
| `Height`       | Yes      | The height of the line chart in inches.                                                                 |
| `Width`        | Yes      | The width of the line chart in inches.                                                                  |
| `Title`        | Yes      | The title of the line chart.                                                                            |
| `View`         | Yes      | The widget view type. For a line chart, the value is `LineChart`.                                       |
| `YAxisColumn`  | Yes      | The field from the query results that you want to use for the Y axis column. For example, `eventCount`. |
| `XAxisColumn`  | Yes      | The field from the query results that you want to use for the X axis column. For example, `eventDate`.  |
| `FilterColumn` | No       | The field from the query results that you want to filter on. For example, `readOnly`.                   | ## Pie chart The following example shows a widget configured as a pie chart. `{ "ViewProperties": { "Height": "2", "Width": "4", "Title": "MostActiveRegions", "View": "PieChart", "LabelColumn": "awsRegion", "ValueColumn": "eventCount", "FilterColumn": "awsRegion" }, "QueryStatement": "SELECT awsRegion, COUNT(*) AS eventCount FROM eds where eventTime > '?' and eventTime < '?' GROUP BY awsRegion ORDER BY eventCount LIMIT 100", "QueryParameters": ["$StartTime$", "$EndTime$"] }` The following table describes configurable view properties for a pie chart.                                                                                                                                                              |
| Parameter      | Required | Value                                                                                                   |
| ---            | ---      | ---                                                                                                     |
| `Height`       | Yes      | The height of the pie chart in inches.                                                                  |
| `Width`        | Yes      | The width of the pie chart in inches.                                                                   |
| `Title`        | Yes      | The title of the pie chart.                                                                             |
| `View`         | Yes      | The widget view type. For a pie chart, the value is `PieChart`.                                         |
| `LabelColumn`  | Yes      | The label for segments in the pie chart. For example, `awsRegion`.                                      |
| `ValueColumn`  | Yes      | The value for the segments in the pie chart. For example, `ValueColumn`.                                |
| `FilterColumn` | No       | The field from the query results that you want to filter on. For example, `awsRegion`.                  | ## Bar chart The following example shows a widget configured as a bar chart. `{ "ViewProperties": { "Height": "2", "Width": "4", "Title": "TopServices", "View": "BarChart", "LabelColumn": "service", "ValueColumn": "eventCount", "FilterColumn": "service", "Orientation": "Horizontal" }, "QueryStatement": "SELECT REPLACE(eventSource, '.amazonaws.com') AS service, COUNT(*) AS eventCount FROM eds WHERE eventTime > '?' AND eventTime < '?' GROUP BY eventSource ORDER BY eventCount DESC LIMIT 100", "QueryParameters": ["$StartTime$", "$EndTime$"] }` The following table describes the configurable view properties for a bar chart.                                                                                        |
| Parameter      | Required | Value                                                                                                   |
| ---            | ---      | ---                                                                                                     |
| `Height`       | Yes      | The height of the bar chart in inches.                                                                  |
| `Width`        | Yes      | The width of the bar chart in inches.                                                                   |
| `Title`        | Yes      | The title of the bar chart.                                                                             |
| `View`         | Yes      | The widget view type. For a bar chart, the value is `BarChart`.                                         |
| `LabelColumn`  | Yes      | The label for bars in the bar chart. For example, `service`.                                            |
| `ValueColumn`  | Yes      | The value for the bars in the bar chart. For example, `eventCount`.                                     |
| `FilterColumn` | No       | The field from the query results that you want to filter on. For example, `service`.                    |
| `Orientation`  | No       | The orientation of the bar chart, either `Horizontal` or `Vertical`.                                    |
