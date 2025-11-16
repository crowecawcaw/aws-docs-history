# Metrics and dimensions

The storage metrics and dimensions that S3 Tables sends to Amazon CloudWatch are listed in the following tables.

###### Note

**Best-effort CloudWatch metrics delivery**

CloudWatch metrics are delivered on a best-effort basis. Most requests for an Amazon S3 object that have request metrics result in a data point being sent to CloudWatch.

The completeness and timeliness of metrics are not guaranteed. The data point for a particular request might be returned with a timestamp that is later than when the request was actually processed. The data point for a minute might be delayed before being available through CloudWatch, or it might not be delivered at all. CloudWatch request metrics give you an idea of the nature of traffic against your bucket in near-real time. It is not meant to be a complete accounting of all requests. It follows from the best-effort nature of this feature that the reports available at the Billing & Cost Management Dashboard might include one or more access requests that do not appear in the bucket metrics.

## Daily storage metrics for table buckets in CloudWatch

The `AWS/S3/Tables` namespace includes the following daily storage metrics which are available at no additional cost. You can filter these metrics by table bucket, table, or namespace name.

| Daily storage metrics | Metric Name                                                         | Description | Units | Statistics | Granularity |
| --------------------- | ------------------------------------------------------------------- | ----------- | ----- | ---------- | ----------- |
| Total Bucket Storage  | The amount of storage in bytes used by all tables in a table bucket | Bytes       | Sum   | Daily      |
| Total number of files | The total count of all files stored in a table bucket               | Count       | Sum   | Daily      |

## Table maintenance metrics

The `AWS/S3/Tables` namespace includes the following table maintenance metrics which are available at no additional cost. You can filter these metrics by table bucket, table, or namespace name.

| Table maintenance metrics | Metric Name                                                        | Description | Units | Statistics | Granularity |
| ------------------------- | ------------------------------------------------------------------ | ----------- | ----- | ---------- | ----------- |
| CompactionBytesProcessed  | The number of bytes processed during table compaction operations   | Bytes       | Sum   | Daily      |
| CompactionObjectsCount    | The number of objects processed during table compaction operations | Count       | Sum   | Daily      |

## Request metrics for tables and table buckets in CloudWatch

The `AWS/S3/Tables` namespace includes the following request metrics which are billed at the same rate as CloudWatch custom metrics. You can filter these metrics by table bucket, table, or namespace name.

| Request metrics                            | Metric Name                                                                                              | Description  | Units | Statistics | Granularity |
| ------------------------------------------ | -------------------------------------------------------------------------------------------------------- | ------------ | ----- | ---------- | ----------- |
| All requests count                         | The total number of HTTP requests made to a table bucket                                                 | Count        | Sum   | 1-minute   |
| Get requests count                         | The number of HTTP GET requests made to retrieve objects from tables                                     | Count        | Sum   | 1-minute   |
| Put requests count                         | The number of HTTP PUT requests made to add objects to tables                                            | Count        | Sum   | 1-minute   |
| Head requests count                        | The number of HTTP HEAD requests made to retrieve metadata from tables                                   | Count        | Sum   | 1-minute   |
| Post requests counts                       | The number of HTTP POST requests made to tables                                                          | Count        | Sum   | 1-minute   |
| UpdateTableMetadataLocation requests count | The number of requests made to update table metadata locations                                           | Count        | Sum   | 1-minute   |
| GetTableMetadataLocation requests count    | The number of requests made to retrieve table metadata locations                                         | Count        | Sum   | 1-minute   |
| BytesDownloaded                            | The number of bytes downloaded for table requests                                                        | Bytes        | Sum   | 1-minute   |
| BytesUploaded                              | The number of bytes uploaded for table requests                                                          | Bytes        | Sum   | 1-minute   |
| 4xxErrors                                  | The count of HTTP 4xx client error status codes returned                                                 | Count        | Sum   | 1-minute   |
| 5xxErrors                                  | The count of HTTP 5xx server error status codes returned                                                 | Count        | Sum   | 1-minute   |
| FirstByteLatency                           | The per-request time from the complete request being received to when the response starts being returned | Milliseconds | Sum   | 1-minute   |
| TotalRequestLatency                        | The elapsed per-request time from the first byte received to the last byte sent                          | Milliseconds | Sum   | 1-minute   |

## S3 Tables dimensions in CloudWatch

The following dimensions are used to filter S3 Tables metrics.

| S3 Tables dimensions | Dimension Name                                                         | Description       | Example Value |
| -------------------- | ---------------------------------------------------------------------- | ----------------- | ------------- |
| `TableBucketName`    | The name of the Amazon S3 table bucket                                 | `my-table-bucket` |
| `Namespace`          | The namespace within the table bucket that contains one or more tables | `my-department`   |
| `TableName`          | The name of a specific table within a namespace                        | `transactions`    |
