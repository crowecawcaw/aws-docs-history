# MIDAPERF01-BP01 Use time series database for real-time analytics and data lake for

long-term storage

In manufacturing environments, access patterns for operational data vary significantly
based on data age. Current data requires high-performance, low-latency access for real-time
decision making, while historical data typically serves longer-term analysis with less
stringent performance requirements. Implementing a tiered storage architecture with time
series databases for recent data and data lakes for historical information helps optimize both
performance and cost.

**Desired outcome:** A multi-tiered data storage architecture that provides millisecond-level query
performance for recent manufacturing data while cost-effectively storing and enabling
analytics on historical data spanning months or years, with appropriate retention policies and
data lifecycle management.

**Common anti-patterns:**

- Using only one type of database (relational
  or noSQL) for both real-time operational data and years of historical data
- Keeping years of
  manufacturing data in high-performance databases designed for real-time access
- Attempting to store
  millisecond-level sensor data in traditional RDBMs without proper optimization
- Storing data without logical separation by time,
  production line, or equipment type, leading to full table scans
- Relying on manual intervention to move aging data
  between storage tiers
- Allowing unlimited data accumulation in high-performance
  storage without lifecycle rules
- Moving data to archival storage too quickly before
  operational teams have adequate access for troubleshooting
- Moving data between tiers without
  optimizing format, compression, or structure for the target storage
- Running long-term trend analysis
  queries against time series databases optimized for recent data
- Forcing applications to know and manage which storage system
  contains the data they need
- Using generic database indexes instead of
  time-series optimized indexing for temporal queries
- Attempting to join data across time series databases and data
  lakes in real-time queries
- Requiring each application to integrate separately
  with time series databases and data lakes
- No unified query interface, forcing users to learn different query languages and
  APIs for current versus Historical data
- Synchronous data migration, blocking real-time operations while moving data between
  storage tiers
- Direct storage access from applications, allowing applications to directly query
  storage systems without abstraction layers
- Inadequate tagging and dimensions, storing time series data without proper metadata
  tags for equipment, location, or process context
- Row-based storage for analytics, using row-oriented formats in data lakes when
  columnar formats would provide better compression and query performance
- Normalized schemas for time series, applying traditional database normalization to
  high-frequency sensor data
- Using one-size-fits-all schemas instead of optimizing for
  specific manufacturing data patterns

**Benefits of establishing this best practice:**

- Delivers sub-second dashboard response times for real-time operational monitoring
- Reduces query costs for frequent access to current production metrics
- Enables cost-effective long-term storage of complete manufacturing history
- Optimizes storage costs by matching data access patterns to appropriate technologies
- Supports both real-time alerting and historical trend analysis from the same dataset

**Level of risk exposed if this best practice is not
established:** Medium

## Implementation guidance

Implement time series database layer**:** Deploy
Amazon Timestream, a purpose-built time series database optimized for industrial IoT
data from manufacturing equipment like CNC machines, conveyor systems, and temperature
sensors. Configure retention policies (typically 30-90 days in memory store, longer
periods in magnetic store) based on operational requirements such as real-time quality
control monitoring. Design efficient data models with appropriate tags (equipment_id,
production_line, and shift) and dimensions (temperature, pressure, and vibration) to
support common manufacturing queries like equipment performance analysis and predictive
maintenance alerts.

Establish data lake architecture: Create an Amazon S3-based data lake with
appropriate partitioning strategies (by date=2024/01/15, production_line=assembly_1,
product_type=automotive_parts) to optimize query performance on historical manufacturing
data. Implement Apache Parquet columnar storage format to improve compression and query
efficiency for manufacturing analytics such as Overall Equipment Effectiveness (OEE)
calculations, quality trend analysis, and production optimization studies across
multiple factories.

Configure data lifecycle management: Develop AWS Lambda functions triggered by
Amazon EventBridge to automatically migrate data from Amazon Timestream to S3 as it ages
beyond immediate operational relevance (for example, after 90 days). Use AWS Glue ETL
jobs to implement data transformation during migration, converting real-time sensor data
into optimized Parquet format and aggregating metrics for long-term analytics like
annual production trends and equipment lifecycle analysis.

Design unified query interface: Create a query abstraction layer using Amazon Athena for historical data analysis and Amazon Timestream Query for real-time
operational data, with Amazon API Gateway providing a unified REST interface. Implement
intelligent routing logic using AWS Lambda that directs queries to Timestream for recent
data (last 30 days for live production monitoring) and to Athena for historical analysis
(older data for quarterly performance reviews and compliance reporting), verifying that
manufacturing engineers and analysts can access data consistently regardless of storage
location.

## Key AWS services

- Amazon Timestream for time series data storage
- Amazon S3 for data lake foundation
- AWS Glue for data transformation and cataloging
- Amazon Athena for querying historical data
- AWS Lambda for lifecycle management automation

## Resources

- [Amazon Timestream: Purpose-built
  time series database](https://aws.amazon.com/timestream/ "https://aws.amazon.com/timestream/")
- [Guidance for Data Lakes on AWS](https://aws.amazon.com/solutions/implementations/data-lake-solution/ "https://aws.amazon.com/solutions/implementations/data-lake-solution/")
- [Time Series Forecasting Principles with Amazon Forecast](https://d1.awsstatic.com/asset-repository/Amazon%20Forecast%20Technical%20Guide%20to%20Time-Series%20Forecasting%20Principles.pdf "https://d1.awsstatic.com/asset-repository/Amazon%20Forecast%20Technical%20Guide%20to%20Time-Series%20Forecasting%20Principles.pdf")
