# Using the Timestream data

source

## Query editor

The query editor accepts Timestream syntax in addition to the macros
listed previously and any dashboard template variables.

Press **Ctrl+Space** to open the
IntelliSense suggestions.

## Macros

To simplify syntax and to allow for dynamic parts, such as date range
filters, the query can contain macros.

| Macro example      | Description                                                                                                                                |
| ------------------ | ------------------------------------------------------------------------------------------------------------------------------------------ |
| _$\_\_database_    | Will specify the selected database. This uses the default from the data source configuration, or the explicit value from the query editor. |
| _$\_\_table_       | Will specify the selected database. This uses the default from the datasource config, or the explicit value from the query editor.         |
| _$\_\_measure_     | Will specify the selected measure. This uses the default from the datasource config, or the explicit value from the query editor.          |
| _$\_\_timeFilter_  | Will be replaced by an expression that limits the time to the dashboard range                                                              |
| _$\_\_interval_ms_ | Will be replaced by a number that represents the amount of time a single pixel in the graph should cover.                                  |
