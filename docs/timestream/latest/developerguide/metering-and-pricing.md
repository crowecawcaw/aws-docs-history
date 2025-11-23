For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified
data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](timestream-for-influxdb.md "timestream-for-influxdb.md").

# Storage

The storage size of each time series event in the memory store
and the magnetic store is calculated as the sum of the size of the timestamp, dimension names,
dimension values, measure names, and measure values.
The size of the timestamp is 8 bytes.
The size of dimension names, dimension values,
and measure names are the length of the UTF-8 encoded bytes of each string representing the dimension name,
dimension value, and measure name. The size of the measure value depends on the data type.
It is 1 byte for boolean data types,
8 bytes for bigint and double, and the length of the UTF-8 encoded bytes for strings.
Each measure is stored as a separate record in Amazon Timestream for LiveAnalytics, i.e.
if your time series event has four measures, there will be four records for that time series event in storage.

Considering the example of the time series event representing the CPU utilization of an EC2 instance
(see [Calculating the write size of a time series event](metering-and-pricing.md#metering-and-pricing.writes.write-size-one-event "metering-and-pricing.md#metering-and-pricing.writes.write-size-one-event")),
the storage size of the time series event is calculated as:

- time = 8 bytes
- first dimension = 15 bytes (`region`+`us-east-1`)
- second dimension = 4 bytes (`az`+`1d`)
- third dimension = 15 bytes (`vpc`+`vpc-1a2b3c4d`)
- fourth dimension = 18 bytes (`hostname`+`host-24Gju`)
- name of the measure = 15 bytes (`cpu_utilization`)
- value of the measure = 8 bytes
  **Storage size of the time series event = 83 bytes**

###### Note

The memory store is metered in GB-hour and the magnetic store is metered in GB-month.
