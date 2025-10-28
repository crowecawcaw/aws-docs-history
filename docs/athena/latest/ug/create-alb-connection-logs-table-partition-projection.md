# Create the

table for ALB connection logs in Athena using partition projection

Because ALB connection logs have a known structure whose partition scheme you can
specify in advance, you can reduce query runtime and automate partition management by
using the Athena partition projection feature. Partition projection automatically adds
new partitions as new data is added. This removes the need for you to manually add
partitions by using `ALTER TABLE ADD PARTITION`.

The following example `CREATE TABLE` statement automatically uses partition
projection on ALB connection logs from a specified date until the present for a single
AWS region. The statement is based on the example in the previous section but adds
`PARTITIONED BY` and `TBLPROPERTIES` clauses to enable
partition projection. In the `LOCATION` and
`storage.location.template` clauses, replace the placeholders with values
that identify the Amazon S3 bucket location of your ALB connection logs. For more information
about connection log file location, see [Connection log files](../../../elasticloadbalancing/latest/application/load-balancer-connection-logs.md#connection-log-file-format "../../../elasticloadbalancing/latest/application/load-balancer-connection-logs.md#connection-log-file-format") in the _User Guide for Application Load Balancers_. For
`projection.day.range`, replace
`2023`/`01`/`01`
with the starting date that you want to use. After you run the query successfully, you
can query the table. You do not have to run `ALTER TABLE ADD PARTITION` to
load the partitions. For information about each log file field, see [Connection log entries](../../../elasticloadbalancing/latest/application/load-balancer-connection-logs.md#connection-log-entry-format "../../../elasticloadbalancing/latest/application/load-balancer-connection-logs.md#connection-log-entry-format").

```
CREATE EXTERNAL TABLE IF NOT EXISTS alb_connection_logs (
         time string,
         client_ip string,
         client_port int,
         listener_port int,
         tls_protocol string,
         tls_cipher string,
         tls_handshake_latency double,
         leaf_client_cert_subject string,
         leaf_client_cert_validity string,
         leaf_client_cert_serial_number string,
         tls_verify_status string,
         conn_trace_id string
         )
            PARTITIONED BY
            (
             day STRING
            )
            ROW FORMAT SERDE 'org.apache.hadoop.hive.serde2.RegexSerDe'
            WITH SERDEPROPERTIES (
            'serialization.format' = '1',
            'input.regex' =
             '([^ ]*) ([^ ]*) ([0-9]*) ([0-9]*) ([A-Za-z0-9.-]*) ([^ ]*) ([-.0-9]*) \"([^\"]*)\" ([^ ]*) ([^ ]*) ([^ ]*) ?([^ ]*)?( .*)?'
            )
            LOCATION 's3://amzn-s3-demo-bucket/AWSLogs/`<ACCOUNT-NUMBER>`/elasticloadbalancing/`<REGION>`/'
            TBLPROPERTIES
            (
             "projection.enabled" = "true",
             "projection.day.type" = "date",
             "projection.day.range" = "2023/01/01,NOW",
             "projection.day.format" = "yyyy/MM/dd",
             "projection.day.interval" = "1",
             "projection.day.interval.unit" = "DAYS",
             "storage.location.template" = "s3://amzn-s3-demo-bucket/AWSLogs/`<ACCOUNT-NUMBER>`/elasticloadbalancing/`<REGION>`/${day}"
            )
```

For more information about partition projection, see [Use partition projection with Amazon Athena](partition-projection.md "partition-projection.md").
