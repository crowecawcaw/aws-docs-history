

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# ANALYZE COMPRESSION
<a name="r_ANALYZE_COMPRESSION"></a>

Performs compression analysis and produces a report with the suggested compression encoding for the tables analyzed. For each column, the report includes an estimate of the potential reduction in disk space compared to the RAW encoding.

## Syntax
<a name="r_ANALYZE_COMPRESSION-synopsis"></a>

```
ANALYZE COMPRESSION
[ [ table_name ]
[ ( column_name [, ...] ) ] ]
[COMPROWS numrows]
```

## Parameters
<a name="r_ANALYZE_COMPRESSION-parameters"></a>

 *table\_name*   
You can analyze compression for specific tables, including temporary tables. You can qualify the table with its schema name. You can optionally specify a *table\_name* to analyze a single table. If you don't specify a *table\_name*, all of the tables in the currently connected database are analyzed. You can't specify more than one *table\_name* with a single ANALYZE COMPRESSION statement.

 *column\_name*   
If you specify a *table\_name*, you can also specify one or more columns in the table (as a column-separated list within parentheses).

COMPROWS  
Number of rows to be used as the sample size for compression analysis. The analysis is run on rows from each data slice. For example, if you specify COMPROWS 1000000 (1,000,000) and the system contains 4 total slices, no more than 250,000 rows per slice are read and analyzed. If COMPROWS isn't specified, the sample size defaults to 100,000 per slice. Values of COMPROWS lower than the default of 100,000 rows per slice are automatically upgraded to the default value. However, compression analysis doesn't produce recommendations if the amount of data in the table is insufficient to produce a meaningful sample. If the COMPROWS number is greater than the number of rows in the table, the ANALYZE COMPRESSION command still proceeds and runs the compression analysis against all of the available rows. Using COMPROWS results in an error if a table isn't specified.

 *numrows*   
Number of rows to be used as the sample size for compression analysis. The accepted range for *numrows* is a number between 1000 and 1000000000 (1,000,000,000).

## Usage notes
<a name="r_ANALYZE_COMPRESSION_usage_notes"></a>

ANALYZE COMPRESSION acquires an exclusive table lock, which prevents concurrent reads and writes against the table. Only run the ANALYZE COMPRESSION command when the table is idle.

Run ANALYZE COMPRESSION to get recommendations for column encoding schemes, based on a sample of the table's contents. ANALYZE COMPRESSION is an advisory tool and doesn't modify the column encodings of the table. You can apply the suggested encoding by recreating the table or by creating a new table with the same schema. Recreating an uncompressed table with appropriate encoding schemes can significantly reduce its on-disk footprint. This approach saves disk space and improves query performance for I/O-bound workloads.

ANALYZE COMPRESSION skips the actual analysis phase and directly returns the original encoding type on any column that is designated as a SORTKEY. It does this because range-restricted scans might perform poorly when SORTKEY columns are compressed much more highly than other columns.

## Examples
<a name="r_ANALYZE_COMPRESSION-examples"></a>

The following example shows the encoding and estimated percent reduction for the columns in the LISTING table only:

```
analyze compression listing;
  
  Table  |     Column     | Encoding | Est_reduction_pct 
---------+----------------+----------+-------------------
 listing | listid         | az64     | 40.96
 listing | sellerid       | az64     | 46.92
 listing | eventid        | az64     | 53.37
 listing | dateid         | raw      | 0.00
 listing | numtickets     | az64     | 65.66
 listing | priceperticket | az64     | 72.94
 listing | totalprice     | az64     | 68.05
 listing | listtime       | az64     | 49.74
```

The following example analyzes the QTYSOLD, COMMISSION, and SALETIME columns in the SALES table.

```
analyze compression sales(qtysold, commission, saletime);

 Table |   Column   | Encoding | Est_reduction_pct 
-------+------------+----------+-------------------
 sales | salesid    | N/A      | 0.00
 sales | listid     | N/A      | 0.00
 sales | sellerid   | N/A      | 0.00
 sales | buyerid    | N/A      | 0.00
 sales | eventid    | N/A      | 0.00
 sales | dateid     | N/A      | 0.00
 sales | qtysold    | az64     | 83.06
 sales | pricepaid  | N/A      | 0.00
 sales | commission | az64     | 71.85
 sales | saletime   | az64     | 49.63
```