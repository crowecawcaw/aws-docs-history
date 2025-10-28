# Work with geospatial data in AWS Glue

AWS Glue does not natively support Well-known Text (WKT), Well-Known Binary (WKB), or
other PostGIS data types. The AWS Glue classifier parses geospatial data and classifies
them using supported data types for the format, such as `varchar` for CSV. As
with other AWS Glue tables, you may need to update the properties of tables created from
geospatial data to allow Athena to parse these data types as-is. For more information,
see [Use a crawler to add a table](schema-crawlers.md "schema-crawlers.md") and [Work with CSV data in AWS Glue](schema-csv.md "schema-csv.md"). Athena may not be able to parse
some geospatial data types in AWS Glue tables as-is. For more information about working
with geospatial data in Athena, see [Query geospatial data](querying-geospatial-data.md "querying-geospatial-data.md").
