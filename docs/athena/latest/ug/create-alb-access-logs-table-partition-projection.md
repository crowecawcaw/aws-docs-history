# Create the table

for ALB access logs in Athena using partition projection

Because ALB access logs have a known structure whose partition scheme you can specify
in advance, you can reduce query runtime and automate partition management by using the
Athena partition projection feature. Partition projection automatically adds new
partitions as new data is added. This removes the need for you to manually add
partitions by using `ALTER TABLE ADD PARTITION`.

The following example `CREATE TABLE` statement automatically uses partition
projection on ALB access logs from a specified date until the present for a single AWS
region. The statement is based on the example in the previous section but adds
`PARTITIONED BY` and `TBLPROPERTIES` clauses to enable
partition projection. In the `LOCATION` and
`storage.location.template` clauses, replace the placeholders with values
that identify the Amazon S3 bucket location of your ALB access logs. For more information
about access log file location, see [Access log files](../../../elasticloadbalancing/latest/application/load-balancer-access-logs.md#access-log-file-format "../../../elasticloadbalancing/latest/application/load-balancer-access-logs.md#access-log-file-format") in the _User Guide for Application Load Balancers_. For
`projection.day.range`, replace
`2022`/`01`/`01`
with the starting date that you want to use. After you run the query successfully, you
can query the table. You do not have to run `ALTER TABLE ADD PARTITION` to
load the partitions. For information about each log file field, see [Access log entries](../../../elasticloadbalancing/latest/application/load-balancer-access-logs.md#access-log-entry-format "../../../elasticloadbalancing/latest/application/load-balancer-access-logs.md#access-log-entry-format").

```
CREATE EXTERNAL TABLE IF NOT EXISTS alb_access_logs (
            type string,
            time string,
            elb string,
            client_ip string,
            client_port int,
            target_ip string,
            target_port int,
            request_processing_time double,
            target_processing_time double,
            response_processing_time double,
            elb_status_code int,
            target_status_code string,
            received_bytes bigint,
            sent_bytes bigint,
            request_verb string,
            request_url string,
            request_proto string,
            user_agent string,
            ssl_cipher string,
            ssl_protocol string,
            target_group_arn string,
            trace_id string,
            domain_name string,
            chosen_cert_arn string,
            matched_rule_priority string,
            request_creation_time string,
            actions_executed string,
            redirect_url string,
            lambda_error_reason string,
            target_port_list string,
            target_status_code_list string,
            classification string,
            classification_reason string,
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
        '([^ ]*) ([^ ]*) ([^ ]*) ([^ ]*):([0-9]*) ([^ ]*)[:-]([0-9]*) ([-.0-9]*) ([-.0-9]*) ([-.0-9]*) (|[-0-9]*) (-|[-0-9]*) ([-0-9]*) ([-0-9]*) \"([^ ]*) (.*) (- |[^ ]*)\" \"([^\"]*)\" ([A-Z0-9-_]+) ([A-Za-z0-9.-]*) ([^ ]*) \"([^\"]*)\" \"([^\"]*)\" \"([^\"]*)\" ([-.0-9]*) ([^ ]*) \"([^\"]*)\" \"([^\"]*)\" \"([^ ]*)\" \"([^\\s]+?)\" \"([^\\s]+)\" \"([^ ]*)\" \"([^ ]*)\" ?([^ ]*)? ?( .*)?'
            )
            LOCATION 's3://amzn-s3-demo-bucket/AWSLogs/`<ACCOUNT-NUMBER>`/elasticloadbalancing/`<REGION>`/'
            TBLPROPERTIES
            (
             "projection.enabled" = "true",
             "projection.day.type" = "date",
             "projection.day.range" = "2022/01/01,NOW",
             "projection.day.format" = "yyyy/MM/dd",
             "projection.day.interval" = "1",
             "projection.day.interval.unit" = "DAYS",
             "storage.location.template" = "s3://amzn-s3-demo-bucket/AWSLogs/`<ACCOUNT-NUMBER>`/elasticloadbalancing/`<REGION>`/${day}"
            )
```

For more information about partition projection, see [Use partition projection with Amazon Athena](partition-projection.md "partition-projection.md").

###### Note

We suggest that the pattern `?( .*)?` at the end of the
`input.regex` parameter always remain in place to handle future log
entries in case new ALB log fields are added.
