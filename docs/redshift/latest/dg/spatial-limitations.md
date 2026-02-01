Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Considerations when using spatial data with Amazon Redshift

The following are considerations when using spatial data with Amazon Redshift:

- The maximum size of a `GEOMETRY` or `GEOGRAPHY` object is 1,048,447 bytes.
- Amazon Redshift Spectrum doesn't natively support spatial data. Therefore, you can't create or alter an
  external table with a `GEOMETRY` or `GEOGRAPHY` column.
- Data types for Python user-defined functions (UDFs) don't support the `GEOMETRY`
  or `GEOGRAPHY` data type.
- You can't use a `GEOMETRY` or `GEOGRAPHY` column as a sort key or a distribution key for an Amazon Redshift
  table.
- You can't use `GEOMETRY` or `GEOGRAPHY` columns in SQL ORDER BY, GROUP BY, or DISTINCT clauses.
- You can't use `GEOMETRY` or `GEOGRAPHY` columns in many SQL functions.
- You can't perform an UNLOAD operation on `GEOMETRY` or `GEOGRAPHY` columns into every format. You can UNLOAD
  `GEOMETRY` or `GEOGRAPHY` columns to text or comma-separated value (CSV) files. Doing
  this writes `GEOMETRY` or `GEOGRAPHY` data in hexadecimal EWKB format. If the size of the
  EWKB data is more than 4 MB, then a warning occurs because the data can't later be
  loaded into a table.
- The supported compression encoding of `GEOMETRY` or `GEOGRAPHY` data is RAW.
- When using JDBC or ODBC drivers, use customized type mappings. In this case, the client
  application must have information on which parameters of a `ResultSet`
  object are `GEOMETRY` or `GEOGRAPHY` objects. The `ResultSetMetadata`
  operation returns type `VARCHAR`.
- To copy geographic date from a `SHAPEFILE`, first ingest into a `GEOMETRY` column,
  and then cast the objects to `GEOGRAPHY` objects.
  .
  The following nonspatial functions can accept an input of type `GEOMETRY` or `GEOGRAPHY`, or
  columns of type `GEOMETRY` or `GEOGRAPHY`:

- The aggregate function COUNT
- The conditional expressions COALESCE and NVL
- CASE expressions
- The default encoding for `GEOMETRY` and `GEOGRAPHY` is RAW.
  For more information, see [Compression encodings](c_Compression_encodings.md "c_Compression_encodings.md").
