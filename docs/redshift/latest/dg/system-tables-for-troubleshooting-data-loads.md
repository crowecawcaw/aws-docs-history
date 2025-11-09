Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# System tables for

troubleshooting data loads

The following Amazon Redshift system tables can be helpful in troubleshooting data load
issues:

- Query [STL_LOAD_ERRORS](r_STL_LOAD_ERRORS.md "r_STL_LOAD_ERRORS.md")
  to discover the errors that occurred during specific loads.
- Query [STL_FILE_SCAN](r_STL_FILE_SCAN.md "r_STL_FILE_SCAN.md") to
  view load times for specific files or to see if a specific file was even
  read.
- Query [STL_S3CLIENT_ERROR](r_STL_S3CLIENT_ERROR.md "r_STL_S3CLIENT_ERROR.md") to find details for errors
  encountered while transferring data from Amazon S3.

###### To find and diagnose load errors

1. Create a view or define a query that returns details about load errors. The
   following example joins the STL_LOAD_ERRORS table to the STV_TBL_PERM table to
   match table IDs with actual table names.

```
create view loadview as
(select distinct tbl, trim(name) as table_name, query, starttime,
trim(filename) as input, line_number, colname, err_code,
trim(err_reason) as reason
from stl_load_errors sl, stv_tbl_perm sp
where sl.tbl = sp.id);
```

2. Set the MAXERRORS option in your COPY command to a large enough value to
   enable COPY to return useful information about your data. If the COPY
   encounters errors, an error message directs you to consult the STL_LOAD_ERRORS
   table for details.
3. Query the LOADVIEW view to see error details. For example:

```
select * from loadview where table_name='venue';
```

```

  tbl   | table_name | query |         starttime
--------+------------+-------+----------------------------
 100551 | venue      | 20974 | 2013-01-29 19:05:58.365391

|     input      | line_number | colname | err_code |       reason
+----------------+-------------+---------+----------+--------------------
| venue_pipe.txt |           1 |       0 |     1214 | Delimiter not found
```

4. Fix the problem in the input file or the load script, based on the
   information that the view returns. Some typical load errors to watch for
   include:
   - Mismatch between data types in table and values in input data
     fields.
   - Mismatch between number of columns in table and number of fields in
     input data.
   - Mismatched quotation marks. Amazon Redshift supports both single and double quotation marks;
     however, these quotation marks must be balanced appropriately.
   - Incorrect format for date/time data in input files.
   - Out-of-range values in input files (for numeric columns).
   - Number of distinct values for a column exceeds the limitation for its
     compression encoding.
