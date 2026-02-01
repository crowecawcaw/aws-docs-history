Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# SVL_SPECTRUM_SCAN_ERROR

You can query the system view SVL_SPECTRUM_SCAN_ERROR to get information about Redshift Spectrum scan errors.

SVL_SPECTRUM_SCAN_ERROR is visible to all users. Superusers can see all rows; regular users can see only their own data. For more information, see [Visibility of data in system tables and
views](cm_chap_system-tables.md#c_visibility-of-data "cm_chap_system-tables.md#c_visibility-of-data").

Some or all of the data in this table can also be found in the SYS monitoring view [SYS_EXTERNAL_QUERY_ERROR](SYS_EXTERNAL_QUERY_ERROR.md "SYS_EXTERNAL_QUERY_ERROR.md"). The data in the SYS monitoring view is formatted to be easier to use and understand.
We recommend that you use the SYS monitoring view for your queries.

## Table columns

Displays a sample of logged errors. The default is 10 entries per query.

| Column name    | Data type      | Description                                                                                                                                                                                                                                                                                                                                                                                                         |
| -------------- | -------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| userid         | integer        | The ID of the user that generated this row.                                                                                                                                                                                                                                                                                                                                                                         |
| query          | integer        | The ID of the query that generated this row.                                                                                                                                                                                                                                                                                                                                                                        |
| location       | character(128) | The location of the data being queried.                                                                                                                                                                                                                                                                                                                                                                             |
| rowid          | character(128) | The location of the error within the file.<br>The `rowid` parts are separated with a `:` (colon) and additional parts might be added in the future.<br>`<br>*row\_offset*:*row\_group*:*row\_id*<br>`<br>A row_offset is the offset (in bytes) of the row within the file and is set to `-1`<br>for unsupported file formats.<br>A table is divided into row_groups, and each group has rows with distinct row_ids. |
| colname        | character(128) | The name of the column returned by the query.                                                                                                                                                                                                                                                                                                                                                                       |
| original_value | character(128) | Original value queried.                                                                                                                                                                                                                                                                                                                                                                                             |
| modified_value | character(128) | Modified value returned based on the data handling configuration option specified in the query.                                                                                                                                                                                                                                                                                                                     |
| trigger        | character(128) | Data handling option specified in the query.                                                                                                                                                                                                                                                                                                                                                                        |
| action         | character(128) | Action associated with the data handling option specified in the query.                                                                                                                                                                                                                                                                                                                                             |
| action_value   | character(128) | Value of action parameter associated with the data handling option specified in the query.                                                                                                                                                                                                                                                                                                                          |
| error_code     | integer        | Result code of the data handling option specified in the query.                                                                                                                                                                                                                                                                                                                                                     |

## Sample query

The following query returns the list of rows for which data handling operations were performed.

```
SELECT * FROM svl_spectrum_scan_error;

```

The query returns results similar to the following.

```

   userid  query     location                                      rowid   colname               original_value             modified_value       trigger          action                        action_valueerror_code
     100   1574007   s3://spectrum-uddh/league/spi_global_rankings.0:0     league_name           Barclays Premier League    Barclays Premier Lea UNSPECIFIED      TRUNCATE                                          156
     100   1574007   s3://spectrum-uddh/league/spi_global_rankings.0:0     league_nspi           34595                      32767                UNSPECIFIED      OVERFLOW_VALUE                                    199
     100   1574007   s3://spectrum-uddh/league/spi_global_rankings.0:1     league_nspi           34151                      32767                UNSPECIFIED      OVERFLOW_VALUE                                    199
     100   1574007   s3://spectrum-uddh/league/spi_global_rankings.0:2     league_name           Barclays Premier League    Barclays Premier Lea UNSPECIFIED      TRUNCATE                                          156
     100   1574007   s3://spectrum-uddh/league/spi_global_rankings.0:2     league_nspi           33223                      32767                UNSPECIFIED      OVERFLOW_VALUE                                    199
     100   1574007   s3://spectrum-uddh/league/spi_global_rankings.0:3     league_name           Barclays Premier League    Barclays Premier Lea UNSPECIFIED      TRUNCATE                                          156
     100   1574007   s3://spectrum-uddh/league/spi_global_rankings.0:3     league_nspi           32808                      32767                UNSPECIFIED      OVERFLOW_VALUE                                    199
     100   1574007   s3://spectrum-uddh/league/spi_global_rankings.0:4     league_nspi           32790                      32767                UNSPECIFIED      OVERFLOW_VALUE                                    199
     100   1574007   s3://spectrum-uddh/league/spi_global_rankings.0:5     league_name           Spanish Primera Division   Spanish Primera Divi UNSPECIFIED      TRUNCATE                                          156
     100   1574007   s3://spectrum-uddh/league/spi_global_rankings.0:6     league_name           Spanish Primera Division   Spanish Primera Divi UNSPECIFIED      TRUNCATE                                          156

```
