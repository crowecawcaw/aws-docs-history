For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified
data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](timestream-for-influxdb.md "timestream-for-influxdb.md").

# Schema design best practices for Timestream for InfluxDB 3

By following these guidelines, you can design InfluxDB schemas that enable simpler and more
performant queries while optimizing resource utilization.

## Performance optimization

guidelines

- Sort tags by query priority:
  - The first write to a table determines physical column order in storage.
  - Place most frequently queried tags first for better performance.
  - Column order cannot be changed after initial write.

- Avoid wide schemas:
  - Limit the number of columns (tags and fields) per table.
  - Too many columns can increase resource usage and reduce performance.
  - Consider segmenting fields into separate tables if needed.

- Avoid sparse schemas:
  - Sparse schemas contain many null values across rows.
  - Caused by non-homogenous table schemas or writing individual fields with different
    timestamps.
  - Adds unnecessary overhead to storing and querying data.

- Maintain homogenous table schemas:
  - Each row should have the same tag and field keys.
  - Avoid tables with many null values.

- Use appropriate data types:
  - Use the most appropriate data type for your data.
  - Integer and boolean fields outperform string fields in queries.

- Use [last-value](https://docs.influxdata.com/influxdb3/enterprise/admin/last-value-cache/ "https://docs.influxdata.com/influxdb3/enterprise/admin/last-value-cache/") and [distinct-value](https://docs.influxdata.com/influxdb3/enterprise/admin/distinct-value-cache/ "https://docs.influxdata.com/influxdb3/enterprise/admin/distinct-value-cache/") cache for repetitive queries where possible.

## Query simplicity guidelines

- Keep N=names simple:
  - Use one tag or field for each data attribute.
  - Choose descriptive, simple names for tables, tags, and fields.
  - Avoid embedding multiple data attributes in a single name.

- Avoid keywords and special characters:
  - Do not use SQL or InfluxQL reserved keywords.
  - Avoid special characters in table names, tag keys, and field keys.
  - Using keywords or special characters requires additional quoting in queries.
