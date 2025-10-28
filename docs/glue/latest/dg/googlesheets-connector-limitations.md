# Limitations for Google Sheets connector

The following are limitations for the Google Sheets connector:

- Google Sheets connector does not support Filters. Hence, filter based partitioning cannot be supported.
- In Record Base Partitioning, there is no provision to return exact record count by SAAS. As a result, there can be
  scenarios where files with empty records are created.
- Since the Google Sheets connector does not support filter-based partitioning, `partitionField`, `lowerbound`,
  and `upperbound` are not valid connection options. If these options are provided, the AWS Glue job is expected to fail.
- It is essential to designate the first row of the sheet as the header row to avoid data processing issues.
  - If not provided, header row will be replaced with `Unnamed:1`, `Unnamed:2`, `Unnamed:3`...
    if the sheet contains data with the first row empty.
  - If header row is provided, empty column names will be replaced with `Unnamed:<number of column>`. For
    example, if header row is `['ColumnName1', 'ColumnName2', '', '', 'ColumnName5', 'ColumnName6']`, then it will
    become `['ColumnName1', 'ColumnName2', 'Unnamed:3', 'Unnamed:4', 'ColumnName5', 'ColumnName6'].`

- The Google Sheets connector does not support Incremental transfer.
- Google Sheets connector supports only String datatype.
- Duplicate headers in a sheet will be iteratively renamed with a numeric suffix.
  Header names provided by the user will have precedence while renaming the duplicate headers. For
  example, if the header row is ["Name", "", "Name", null, "Unnamed:6", ""], it will
  change to: ["Name", "Unnamed:2", "Name1", "Unnamed:4", "Unnamed:6", "Unnamed:61"].
- Google Sheets connector does not support spaces for a tabName.
- A folder name can't have the following special characters:
  - #
  - /
