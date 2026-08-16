Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026.
We will start enforcing it in phases. For more information on the details of Python end of life
and migration options, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") that was published on June 30, 2025.

# SYS\_EXTERNAL\_QUERY\_ERROR

You can query the system view SYS\_EXTERNAL\_QUERY\_ERROR to get information about Redshift Spectrum
scan errors. SYS\_EXTERNAL\_QUERY\_ERROR displays a sample of logged errors. The default is
10 entries per query.

SYS\_EXTERNAL\_QUERY\_ERROR is visible to all users. Superusers can see all rows; regular users can see only their own data. For more information, see [Visibility of data in system tables and views](cm_chap_system-tables.md#c_visibility-of-data "cm_chap_system-tables.md#c_visibility-of-data").

## Table columns

| Column name     | Data type     | Description                                                                                                                                                                                                                                                                                                                                                                                                                  |
| --------------- | ------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| user\_id        | integer       | The identifier of the user that generated this<br>row.                                                                                                                                                                                                                                                                                                                                                                       |
| query\_id       | bigint        | The query identifier of the query that generated<br>this row.                                                                                                                                                                                                                                                                                                                                                                |
| file\_location  | char(256)     | The location of the data being queried.                                                                                                                                                                                                                                                                                                                                                                                      |
| rowid           | char(2100)    | The location of the error within the file. The<br>`rowid` parts are separated with a `:`<br>(colon) and additional parts might be added in the future.<br>`<br>*row\_offset*:*row\_group*:*row\_id*<br>`<br>A row\_offset is the offset (in bytes) of the row within the file and<br>is set to `-1` for unsupported file formats. A table is<br>divided into row\_groups, and each group has rows with distinct<br>row\_ids. |
| column\_name    | char(127)     | The name of the column returned by the query.                                                                                                                                                                                                                                                                                                                                                                                |
| original\_value | char(1024)    | Original value queried.                                                                                                                                                                                                                                                                                                                                                                                                      |
| modified\_value | char(1024)    | Modified value returned based on the data handling<br>configuration option specified in the query.                                                                                                                                                                                                                                                                                                                           |
| trigger         | char(128)     | Data handling option specified in the query.                                                                                                                                                                                                                                                                                                                                                                                 |
| action          | char(128)     | Action associated with the data handling option<br>specified in the query.                                                                                                                                                                                                                                                                                                                                                   |
| action\_value   | char(128)     | Value of action parameter associated with the data<br>handling option specified in the query.                                                                                                                                                                                                                                                                                                                                |
| error\_code     | integer       | Result code of the data handling option specified<br>in the query.                                                                                                                                                                                                                                                                                                                                                           |
| query\_uuid     | character(36) | A globally unique identifier (UUID) of the query.                                                                                                                                                                                                                                                                                                                                                                            |

## Sample query

The following query returns the list of rows for which data handling operations
were performed.

```
SELECT * FROM sys_external_query_error;
```

The query returns results similar to the following.

```

   user_id   query_id  file_location                                rowid    column_name           original_value             modified_value       trigger          action               action_value                 error_code
     100     1574007   s3://spectrum-uddh/league/spi_global_rankings.0:0     league_name           Barclays Premier League    Barclays Premier Lea UNSPECIFIED      TRUNCATE                                          156
     100     1574007   s3://spectrum-uddh/league/spi_global_rankings.0:0     league_nspi           34595                      32767                UNSPECIFIED      OVERFLOW_VALUE                                    199
     100     1574007   s3://spectrum-uddh/league/spi_global_rankings.0:1     league_nspi           34151                      32767                UNSPECIFIED      OVERFLOW_VALUE                                    199
     100     1574007   s3://spectrum-uddh/league/spi_global_rankings.0:2     league_name           Barclays Premier League    Barclays Premier Lea UNSPECIFIED      TRUNCATE                                          156
     100     1574007   s3://spectrum-uddh/league/spi_global_rankings.0:2     league_nspi           33223                      32767                UNSPECIFIED      OVERFLOW_VALUE                                    199
     100     1574007   s3://spectrum-uddh/league/spi_global_rankings.0:3     league_name           Barclays Premier League    Barclays Premier Lea UNSPECIFIED      TRUNCATE                                          156
     100     1574007   s3://spectrum-uddh/league/spi_global_rankings.0:3     league_nspi           32808                      32767                UNSPECIFIED      OVERFLOW_VALUE                                    199
     100     1574007   s3://spectrum-uddh/league/spi_global_rankings.0:4     league_nspi           32790                      32767                UNSPECIFIED      OVERFLOW_VALUE                                    199
     100     1574007   s3://spectrum-uddh/league/spi_global_rankings.0:5     league_name           Spanish Primera Division   Spanish Primera Divi UNSPECIFIED      TRUNCATE                                          156
     100     1574007   s3://spectrum-uddh/league/spi_global_rankings.0:6     league_name           Spanish Primera Division   Spanish Primera Divi UNSPECIFIED      TRUNCATE                                          156

```
