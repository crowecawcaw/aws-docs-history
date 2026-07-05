Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026.
We will start enforcing it in phases. For more information on the details of Python end of life
and migration options, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") that was published on June 30, 2025.

# SYS\_SPATIAL\_SIMPLIFY

You can query the system view SYS\_SPATIAL\_SIMPLIFY to get information about simplified
spatial geometry objects using the COPY command. When you use COPY on a shapefile, you
can specify SIMPLIFY `tolerance`, SIMPLIFY AUTO, and SIMPLIFY AUTO
`max_tolerance` ingestion options. The result of the simplification is
summarized in SYS\_SPATIAL\_SIMPLIFY system view.

When SIMPLIFY AUTO `max_tolerance` is set, this view contains a row for
each geometry that exceeded the maximum size. When SIMPLIFY `tolerance` is
set, then one row for the entire COPY operation is stored. This row references the COPY
query ID and the specified simplification tolerance.

For more information about loading a shapefile, see [Loading a shapefile into Amazon Redshift](spatial-copy-shapefile.md "spatial-copy-shapefile.md").

SYS\_SPATIAL\_SIMPLIFY is visible to all users. Superusers can see all rows; regular users can see only their own data. For more information, see [Visibility of data in system tables and views](cm_chap_system-tables.md#c_visibility-of-data "cm_chap_system-tables.md#c_visibility-of-data").

## Table columns

| Column name        | Data type        | Description                                                                                                                                                                                                                                                                                                  |
| ------------------ | ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| query\_id          | bigint           | The ID of the query (COPY command) that generated<br>this row.                                                                                                                                                                                                                                               |
| line\_number       | bigint           | When COPY `SIMPLIFY AUTO` option is<br>specified, this value is the record number of the simplified record<br>in the shapefile.                                                                                                                                                                              |
| maximum\_tolerance | double precision | The distance tolerance value specified in the COPY<br>command. This is either the maximum tolerance value using the<br>`SIMPLIFY AUTO` option, or the fixed tolerance value<br>using the `SIMPLIFY` option.                                                                                                  |
| initial\_size      | bigint           | The size in bytes of the `GEOMETRY`<br>data value before simplification.                                                                                                                                                                                                                                     |
| simplified         | char(1)          | When the COPY `SIMPLIFY AUTO` option is<br>specified, `t` if the geometry was successfully<br>simplified, or `f` otherwise. The geometry might not be<br>simplified successfully if after the simplification with the given<br>maximum tolerance its size is still larger than the maximum geometry<br>size. |
| final\_size        | bigint           | When the COPY `SIMPLIFY AUTO` option is<br>specified, this is the size in bytes of the geometry after<br>simplification.                                                                                                                                                                                     |
| final\_tolerance   | double precision | Final tolerance chosen for the simplification.                                                                                                                                                                                                                                                               |

## Sample query

The following query returns the list of records that COPY simplified.

```
`SELECT * FROM sys_spatial_simplify;`

 `query_id | line_number | maximum_tolerance | initial_size | simplified | final_size | final_tolerance
----------+-------------+-------------------+--------------+------------+------------+----------------------
 20 | 1184704 | -1 | 1513736 | t | 1008808 | 1.276386653895e-05
 20 | 1664115 | -1 | 1233456 | t | 1023584 | 6.11707814796635e-06`

```
