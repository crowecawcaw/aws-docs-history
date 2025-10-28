For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified
data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](timestream-for-influxdb.md "timestream-for-influxdb.md").

# Setup to view InfluxDB logs on Timestream Influxdb Instances

By default InfluxDB generates logs that go to stdout. For more information, see [Manage InfluxDB logs](https://docs.influxdata.com/influxdb/v2/admin/logs "https://docs.influxdata.com/influxdb/v2/admin/logs")

To view InfluxDB logs generated from the Instance you have created through Timestream InfluxDB, we provide the opportunity to provide hourly logs. These logs will go to a specified S3 bucket that you must create before creating your instance.

- Before creating the instance, the provided Amazon S3 bucket must also give Timestream-InfluxDB permission to send logs to this bucket by providing a bucket policy with Timestream InfluxDB Service Principal
  as following (replace `{BUCKET_NAME}` with the actual name of your Amazon S3 bucket:

JSON

```
`{
 "Version":"2012-10-17",
 "Id": "PolicyForInfluxLogs",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "Service": "timestream-influxdb.amazonaws.com"
 },
 "Action": "s3:PutObject",
 "Resource": "arn:aws:s3:::`{BUCKET_NAME}`/InfluxLogs/*"
 }
 ]
}`

```

- The bucket provided must be in the same account and same Region of your created Timestream InfluxDB instance

Here is the command you can call to make an instance to receive influx logs:

```
aws timestream-influxdb create-db-instance \
    --name myinfluxDbinstance \
    --allocated-storage 400 \
    --db-instance-type db.influx.4xlarge \
    --vpc-subnet-ids subnetid1 subnetid2
    --vpc-security-group-ids mysecuritygroup \
    --username masterawsuser \
    --password \
    --db-storage-type InfluxIOIncludedT2
```

Here is the format of this parameter.

```
-- log-delivery-configuration
{
    "S3Configuration": {
      "BucketName": "string",
      "Enabled": true|false
    }
}
```

- This field is not required and logging is not enabled by default.
- Not setting this field is the same as not having logs enabled.
- Logs will be sent to specified bucket with a prefix of `InfluxLogs/`.
- After creating the instance, you can modify the log delivery configuration with the `update-db-instance` API command.
  InfluxDB offers different types of logs. These can be configured by setting the InfluxDB Parameters. Use the flux-log-enabled
  and log-level parameters to configure the type of logs that is emitted from the instance. For more information, see
  [Supported parameters and parameter values](timestream-for-influx-db-connecting.md#timestream-for-influx-parameter-groups-overview-supported-parameters "timestream-for-influx-db-connecting.md#timestream-for-influx-parameter-groups-overview-supported-parameters").
