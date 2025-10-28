For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified
data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](timestream-for-influxdb.md "timestream-for-influxdb.md").

# Writing data to your Timestream for InfluxDB 3

cluster

Amazon Timestream for InfluxDB 3 provides robust capabilities for ingesting time-series data
efficiently. Understanding the proper methods for writing data is essential for maximizing
performance and ensuring data integrity.

Timestream for InfluxDB 3 provides multiple HTTP API endpoints for writing time-series data,
offering flexibility for different integration methods and compatibility with existing InfluxDB
workloads.

## Line protocol overview

InfluxDB 3 is designed for high write-throughput and uses an efficient, human-readable
write syntax called [line protocol](https://docs.influxdata.com/influxdb3/core/reference/line-protocol/ "https://docs.influxdata.com/influxdb3/core/reference/line-protocol/").
As a schema-on-write database, InfluxDB automatically creates the logical database, tables, and
their schemas when you start writing data, without requiring any manual setup. Once the schema is
created, InfluxDB validates future write requests against it before accepting new data, while
still allowing schema evolution as your needs change.

### Line protocol structure

Line protocol consists of the following essential elements:

- **Table**: A string identifier for the table where
  data will be stored.
- (Optional) **Tag set**: Comma-delimited key-value pairs representing
  metadata (indexed).
- **Field set**: Comma-delimited key-value pairs
  representing the actual measurements.
- (Optional) **Timestamp**: Unix timestamp associated with the data point
  up to nanosecond precision.

Field values can be one of the following data types:

- Strings (must be quoted)
- Floats (for example, 23.4)
- Integers (for example, 10i)
- Unsigned integers (for example, 10u)
- Booleans (true/false)

Line protocol follows this general syntax:

```
myTable,tag1=val1,tag2=val2 field1="v1",field2=1i 0000000000000000000
```

Example data point using line protocol:

```
home,room=Living\ Room temp=21.1,hum=35.9,co=0i 1735545600

```

This creates a point in the "home" table with:

- Tag: room="Living Room"
- Fields: temp=21.1 (float), hum=35.9 (float), co=0 (integer)
- Timestamp: 1735545600 (Unix seconds)

## API endpoints overview

InfluxDB 3 supports three primary write endpoints:

1. **Native v3 API** (`/api/v3/write_lp`): The recommended
   endpoint for new implementations.
2. **v2 Compatibility API** (`/api/v2/write`): For
   migrating InfluxDB v2.x workloads.
3. **v1 Compatibility API** (`/write`): For migrating
   InfluxDB v1.x workloads.

### Using the Native v3 write API

The `/api/v3/write_lp` endpoint is the native InfluxDB 3 API for writing line
protocol data.

Request format:

```
POST /api/v3/write_lp?db=DATABASE_NAME&precision=PRECISION&accept_partial=BOOLEAN&no_sync=BOOLEAN

```

Query parameters:

| **Parameter**      | **Description**                     | **Default**                               |
| ------------------ | ----------------------------------- | ----------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `db`               | Database name (required)            | -                                         |
| `precision`        | Timestamp precision (ns, us, ms, s) | Auto-detected                             |
| `accept_partial`   | Accept partial writes on errors     | true                                      |
| `no_sync`          | Acknowledge before WAL persistence  | false                                     | #### Example write request: `curl -v "https://your-cluster-endpoint:8086/api/v3/write_lp?db=sensors&precision=s" \ --header "Authorization: Bearer YOUR_TOKEN" \ --data-raw "home,room=Living\ Room temp=21.1,hum=35.9,co=0i 1735545600 home,room=Kitchen temp=21.0,hum=35.9,co=0i 1735545600"` ### Write response modes Standard Mode (`no_sync`=false) <br>• Waits for data to be written to the WAL (Write-Ahead Log) before acknowledging. <br>• Provides durability guarantees. <br>• Higher latency due to WAL persistence wait. <br>• Recommended for critical data where durability is essential. Fast Mode (`no_sync`=true) <br>• Acknowledges immediately without waiting for WAL persistence. <br>• Lowest possible write latency. <br>• Risk of data loss if system crashes before WAL write completes. <br>• Ideal for high-throughput scenarios where speed is prioritized over absolute durability. ### Partial write handling The `accept_partial` parameter controls behavior when write batches contain errors: When `accept_partial` is `true` (default): <br>• Valid lines are written successfully. <br>• Invalid lines are rejected. <br>• Returns 400 status with details about failed lines. <br>• Useful for large batch operations where some failures are acceptable. When `accept_partial` is `false`: <br>• Entire batch is rejected if any line fails. <br>• No data is written. <br>• Returns 400 status with error details. <br>• Ensures all-or-nothing write semantics. ### Compatibility APIs Compatibility APIs enable seamless migration of existing InfluxDB v1 or v2 workloads to InfluxDB 3. These endpoints work with existing InfluxDB client libraries, Telegraf, and third-party integrations. **Important differences:** <br>• Tags in a table (measurement) are immutable once created. <br>• A tag and a field cannot have the same name within a table. <br>• Schema validation is enforced on write. #### InfluxDB v2 compatibility The `/api/v2/write` endpoint provides backwards compatibility for v2 clients: `curl -i "https://your-cluster-endpoint:8086/api/v2/write?bucket=DATABASE_NAME&precision=s" \ --header "Authorization: Bearer DATABASE_TOKEN" \ --header "Content-type: text/plain; charset=utf-8" \ --data-binary 'home,room=kitchen temp=72 1641024000'` V2 API parameters:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| **Parameter**      | **Location**                        | **Description**                           |
| ---                | ---                                 | ---                                       |
| `bucket` \*        | Query string                        | Maps to database name                     |
| `precision`        | Query string                        | Timestamp precision (ns, us, ms, s, m, h) |
| `Authorization`    | Header                              | Bearer or Token scheme                    |
| `Content-Encoding` | Header                              | gzip or identity                          | ##### InfluxDB v1 Compatibility The `/write` endpoint provides backwards compatibility for v1 clients: `curl -i "https://your-cluster-endpoint:8086/write?db=DATABASE_NAME&precision=s" \ --user "any:DATABASE_TOKEN" \ --header "Content-type: text/plain; charset=utf-8" \ --data-binary 'home,room=kitchen temp=72 1641024000'` V1 authentication options: <br>• Basic authentication: Token as password (`--user "any:TOKEN"`). <br>• Query parameter: `p=TOKEN` in URL. <br>• Bearer/Token header: Standard authorization header. V1 API parameters:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| **Parameter**      | **Location**                        | **Description**                           |
| ---                | ---                                 | ---                                       |
| `db` \*            | Query string                        | Database name                             |
| `precision`        | Query string                        | Timestamp precision                       |
| `p`                | Query string                        | Token for query auth                      |
| `u`                | Query string                        | Username (ignored)                        |
| `Authorization`    | Header                              | Multiple schemes supported                |
| `Content-Encoding` | Header                              | gzip or identity                          | ## Client libraries and integrations ### Official InfluxDB 3 client libraries InfluxDB 3 client libraries provide native language interfaces for constructing and writing time-series data: <br>• **Python**: `influxdb3-python` <br>• **Go**: `influxdb3-go` <br>• **JavaScript/Node.js**: `influxdb3-js` <br>• **Java**: `influxdb3-java` <br>• **C#**: `InfluxDB3.Client` Example: Python client `from influxdb3 import InfluxDBClient3 client = InfluxDBClient3( host="your-cluster-endpoint:8086", token="YOUR_TOKEN", database="DATABASE_NAME" ) # Write using line protocol client.write("home,room=Living\\ Room temp=21.1,hum=35.9,co=0i") # Write using Point objects from influxdb3 import Point point = Point("home") \ .tag("room", "Living Room") \ .field("temp", 21.1) \ .field("hum", 35.9) \ .field("co", 0) client.write(point)` Example: Go client `import "github.com/InfluxCommunity/influxdb3-go/v2/influxdb3" client, err := influxdb3.New(influxdb3.ClientConfig{ Host: "your-cluster-endpoint:8086", Token: "YOUR_TOKEN", Database: "DATABASE_NAME", }) point := influxdb3.NewPoint("home", map[string]string{"room": "Living Room"}, map[string]any{ "temp": 24.5, "hum":  40.5, "co":   15, }, time.Now(), ) err = client.WritePoints(context.Background(), []*influxdb3.Point{point})` ### Legacy client libraries For existing v1 and v2 workloads, you can continue using legacy client libraries with the compatibility endpoints: Example: Node.js v1 client: `const Influx = require('influx') const client = new Influx.InfluxDB({ host: 'your-cluster-endpoint', port: 8086, protocol: 'https', database: 'DATABASE_NAME', username: 'ignored', password: 'DATABASE_TOKEN' })` ## Best practices for writing data When writing data, we recommend the following: <br>• Batch optimization + Optimal batch size: 5,000-10,000 lines or 10MB per request. + Use compression (gzip) for large payloads. + Sort tags by key in lexicographic order for better performance. <br>• Timestamp precision + Use the coarsest precision that meets your needs. + Explicitly specify precision to avoid ambiguity. + Maintain consistent precision across your application. <br>• Error handling + Implement retry logic for transient failures. + Use accept_partial=true for resilient batch operations. + Monitor write errors through CloudWatch metrics. <br>• Performance tuning + Use no_sync=true for high-throughput scenarios. + Distribute writes across multiple connections. + Use the writer/reader endpoint for all write operations. <br>• Schema considerations + Tags are immutable once created. + Fields and tags cannot share the same nam.e + Design schemas with query patterns in mind. + Keep tag cardinality under control. Important differences from previous versions: <br>• Immutable tags: Once a tag is created in a table, its type cannot be changed <br>• No tag/field name conflicts: A tag and field cannot have the same name within a table <br>• Schema-on-write: InfluxDB 3 validates data types on write <br>• Automatic table creation: Tables are created automatically on first write <br>• Strict type checking: Field types must remain consistent across all writes By leveraging the appropriate write API and following these best practices, you can efficiently ingest time-series data into your Timestream for InfluxDB 3 instance while maintaining high performance and data integrity. |
