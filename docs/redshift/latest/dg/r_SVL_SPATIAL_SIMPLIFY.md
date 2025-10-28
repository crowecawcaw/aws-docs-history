Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# SVL_SPATIAL_SIMPLIFY

You can query the system view SVL_SPATIAL_SIMPLIFY to get information about simplified
spatial geometry objects using the COPY command. When you use COPY on a shapefile, you
can specify SIMPLIFY `tolerance`, SIMPLIFY AUTO, and SIMPLIFY AUTO
`max_tolerance` ingestion options. The result of the simplification is
summarized in SVL_SPATIAL_SIMPLIFY system view.

When SIMPLIFY AUTO `max_tolerance` is set, this view contains a row for
each geometry that exceeded the maximum size. When SIMPLIFY `tolerance` is
set, then one row for the entire COPY operation is stored. This row references the COPY
query ID and the specified simplification tolerance.

SVL_SPATIAL_SIMPLIFY is visible to all users. Superusers can see all rows; regular users can see only their own data. For more information, see [Visibility of data in system tables and
views](cm_chap_system-tables.md#c_visibility-of-data "cm_chap_system-tables.md#c_visibility-of-data").

Some or all of the data in this table can also be found in the SYS monitoring view [SYS_SPATIAL_SIMPLIFY](SYS_SPATIAL_SIMPLIFY.md "SYS_SPATIAL_SIMPLIFY.md"). The data in the SYS monitoring view is formatted to be easier to use and understand.
We recommend that you use the SYS monitoring view for your queries.

## Table columns

| Column name       | Data type | Description                                                                                                                                                                                                                                                                                   |
| ----------------- | --------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- | ----------------- | ------------ | ---------- | ---------- | ---------------------------------------------------------------------------------------------------------------------------- | ------- | --- | ------- | --- | ------- | --------------------- | ------- | --- | ------- | --- | ------- | ------------------------ |
| query             | integer   | The ID of the query (COPY command) that generated this row.                                                                                                                                                                                                                                   |
| line_number       | integer   | When COPY `SIMPLIFY AUTO` option is specified, this value is the record number of the simplified record in the shapefile.                                                                                                                                                                     |
| maximum_tolerance | double    | The distance tolerance value specified in the COPY command. This is either the maximum tolerance value using the `SIMPLIFY AUTO` option, or the fixed tolerance value using the `SIMPLIFY` option.                                                                                            |
| initial_size      | integer   | The size in bytes of the `GEOMETRY` data value before simplification.                                                                                                                                                                                                                         |
| simplified        | char(1)   | When the COPY `SIMPLIFY AUTO` option is specified, `t` if the geometry was successfully simplified, or `f` otherwise. The geometry might not be simplified successfully if after the simplification with the given maximum tolerance its size is still larger than the maximum geometry size. |
| final_size        | integer   | When the COPY `SIMPLIFY AUTO` option is specified, this is the size in bytes of the geometry after simplification.                                                                                                                                                                            |
| final_tolerance   | double    |                                                                                                                                                                                                                                                                                               | ## Sample query The following query returns the list of records that COPY simplified. ``` SELECT \* FROM svl_spatial_simplify WHERE query = pg_last_copy_id(); query | line_number | maximum_tolerance | initial_size | simplified | final_size | final_tolerance -------+-------------+-------------------+--------------+------------+------------+---------------------- 20 | 1184704 | -1  | 1513736 | t   | 1008808 | 1.276386653895e-05 20 | 1664115 | -1  | 1233456 | t   | 1023584 | 6.11707814796635e-06 ``` |
