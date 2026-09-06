

For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](https://docs.aws.amazon.com/timestream/latest/developerguide/timestream-for-influxdb.html).

# `snapshotted-wal-files-to-keep`
<a name="snapshotted-wal-files-to-keep"></a>


**Parameter Details**  

|  |  | 
| --- |--- |
| Default | 300 | 
| Allowed Values | Integer: 1 – 10,000 | 
| Category | WAL / Durability | 

**Note**  
This value must always be non-zero. Replicas pull WAL data from snapshotted WAL files. Setting this to 0 would prevent replicas from catching up after a snapshot.

**Detailed Explanation:**

Controls the number of already-snapshotted WAL files to retain on disk. These files have been persisted to Parquet but are kept so that replicas can pull the WAL data. Essential for replication in Enterprise clusters.

**Recommendation:** Keep at 300 (default). Increase to 500–1000 for mission-critical workloads where replicas may experience extended outages.