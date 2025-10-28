# Query data from AWS IoT SiteWise

You can use the AWS IoT SiteWise API operations to query your asset properties' current values,
historical values, and aggregates over specific time intervals. AWS IoT SiteWise provides multiple query interfaces to meet different integration needs:

- **Direct API operations** - Simple, targeted API calls for specific data retrieval needs
- **SQL-like query language** - Powerful, flexible queries for complex data analysis
- **ODBC driver** - Integration with business intelligence tools and applications
  Use these query capabilities to:

- Gain real-time insights into operational data
- Analyze historical trends and patterns
- Calculate performance metrics across your industrial assets
- Integrate IoT data with enterprise systems and dashboards
- Build custom applications that leverage industrial data
  For example, you can discover all assets with specific property values, build custom representations of your data, or develop software solutions that integrate with the industrial data stored in your AWS IoT SiteWise assets. You can also explore your asset data live in AWS IoT SiteWise Monitor. To learn how to configure SiteWise Monitor, see [Monitor data with AWS IoT SiteWise Monitor](monitor-data.md "monitor-data.md").

The operations described in this section return property value objects that contain
timestamp, quality, value (TQV) structures:

- The `timestamp` contains the current Unix epoch time in seconds
  with nanosecond offset.
- The `quality` contains one of the following strings that indicate the quality
  of the data point:
  - `GOOD` – The data isn't affected by any issues.
  - `BAD` – The data is affected by an issue such as sensor
    failure.
  - `UNCERTAIN` – The data is affected by an issue such as sensor
    inaccuracy.

- The `value` contains one of the following fields, depending on the type of the property:
  - `booleanValue`
  - `doubleValue`
  - `integerValue`
  - `stringValue`
  - `nullValue`

###### Topics

- [Query current asset property values in AWS IoT SiteWise](current-values.md "current-values.md")
- [Query historical asset property values in AWS IoT SiteWise](historical-values.md "historical-values.md")
- [Query asset property aggregates in AWS IoT SiteWise](aggregates.md "aggregates.md")
- [AWS IoT SiteWise query language](sql.md "sql.md")
- [Query optimization](query-optimize.md "query-optimize.md")
- [ODBC](query-ODBC.md "query-ODBC.md")
