For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified
data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](timestream-for-influxdb.md "timestream-for-influxdb.md").

# API reference

This section contains the API Reference documentation for Amazon Timestream.

Timestream has two APIs: Query and Write.

- The **Write API** allows you to perform operations like table creation,
  resource tagging, and writing of records to Timestream.
- The **Query API** allows you to perform query operations.

###### Note

Both APIs include the DescribeEndpoints action. _For both Query and Write, the
DescribeEndpoints action are identical._

You can read more about each API below, along with data types, common errors and
parameters.

###### Note

For error codes common to all AWS services, see
the [AWS
Support section](../../../awssupport/latest/APIReference/CommonErrors.md "../../../awssupport/latest/APIReference/CommonErrors.md").

###### Topics

- [Actions](API_Operations.md "API_Operations.md")
- [Data Types](API_Types.md "API_Types.md")
- [Common Errors](CommonErrors.md "CommonErrors.md")
- [Common Parameters](CommonParameters.md "CommonParameters.md")
