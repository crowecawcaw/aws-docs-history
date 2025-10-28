# Identity details

Columns under the **identity** header in AWS Cost and Usage Reports
are static fields that appear in all Cost and Usage Reports.

You can use the identity line items in the report to find specific line items that
have been split across multiple AWS CUR files. These include the following columns:

## identity/LineItemId

- **Description:** This field is generated for
  each line item and is unique in a given partition. This does not guarantee
  that the field will be unique across an entire delivery (that is, all
  partitions in an update) of the AWS CUR. The line item ID isn't consistent
  between different Cost and Usage Reports and can't be used to identify the same line
  item across different reports.
- **Example:** A report created for November 29
  can be large enough to require multiple files. The
  **LineItemId** is consistent between the November 29
  AWS CUR files, but doesn't match the **LineItemId** for the
  same resource in the November 30 report.

## identity/TimeInterval

- **Description:** The time interval that this
  line item applies to, in the following format:
  `YYYY-MM-DDTHH:mm:ssZ/YYYY-MM-DDTHH:mm:ssZ`. The time
  interval is in UTC and can be either daily or hourly, depending on the
  granularity of the report.
- **Example:** The
  **TimeInterval**
  `2017-11-01T00:00:00Z/2017-12-01T00:00:00Z` includes the entire
  month of November 2017.
