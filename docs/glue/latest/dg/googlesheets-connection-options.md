# Google Sheets connection options

The following are connection options for Google Sheets:

- `ENTITY_NAME`(String) - (Required) Used for Read. The `SpreadSheet ID` and
  `sheetTabName` in Google Sheets.
  Example: `{SpreadSheetID}#{SheetTabName}`.
- `API_VERSION`(String) - (Required) Used for Read. Google Sheets Rest API version you want to use.
- `SELECTED_FIELDS`(List<String>) - Default: empty(SELECT \*). Used for Read. Columns you want to select
  for the object.
- `FILTER_PREDICATE`(String) - Default: empty. Used for Read. It should be in the Spark SQL format.
- `QUERY`(String) - Default: empty. Used for Read. Full Spark SQL query.
- `NUM_PARTITIONS`(Integer) - Default: 1. Used for Read. Number of partitions for read.
