# Create the table for ALB access

logs

1. Copy and paste the following `CREATE TABLE` statement into the
   query editor in the Athena console, and then modify it as necessary for your own
   log entry requirements. For information about getting started with the Athena
   console, see [Get started](getting-started.md "getting-started.md").
   Replace the path in the `LOCATION` clause with your Amazon S3 access log
   folder location. For more information about access log file location, see [Access log files](../../../elasticloadbalancing/latest/application/load-balancer-access-logs.md#access-log-file-format "../../../elasticloadbalancing/latest/application/load-balancer-access-logs.md#access-log-file-format") in the _User Guide for Application Load Balancers_.

For information about each log file field, see [Access log entries](../../../elasticloadbalancing/latest/application/load-balancer-access-logs.md#access-log-entry-format "../../../elasticloadbalancing/latest/application/load-balancer-access-logs.md#access-log-entry-format") in the
_User Guide for Application Load Balancers_.

###### Note

The following example `CREATE TABLE` statement includes the
recently added `classification`,
`classification_reason`, and `conn_trace_id`
('traceability ID', or TID) columns. To create a table for Application Load Balancer access logs
that do not contain these entries, remove the corresponding columns from the
`CREATE TABLE` statement and modify the regular expression
accordingly.

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
            ROW FORMAT SERDE 'org.apache.hadoop.hive.serde2.RegexSerDe'
            WITH SERDEPROPERTIES (
            'serialization.format' = '1',
            'input.regex' =
        '([^ ]*) ([^ ]*) ([^ ]*) ([^ ]*):([0-9]*) ([^ ]*)[:-]([0-9]*) ([-.0-9]*) ([-.0-9]*) ([-.0-9]*) (|[-0-9]*) (-|[-0-9]*) ([-0-9]*) ([-0-9]*) \"([^ ]*) (.*) (- |[^ ]*)\" \"([^\"]*)\" ([A-Z0-9-_]+) ([A-Za-z0-9.-]*) ([^ ]*) \"([^\"]*)\" \"([^\"]*)\" \"([^\"]*)\" ([-.0-9]*) ([^ ]*) \"([^\"]*)\" \"([^\"]*)\" \"([^ ]*)\" \"([^\\s]+?)\" \"([^\\s]+)\" \"([^ ]*)\" \"([^ ]*)\" ?([^ ]*)? ?( .*)?'
            )
            LOCATION 's3://amzn-s3-demo-bucket/`access-log-folder-path`/'

```

###### Note

We suggest that the pattern `?( .*)?` at the end of the
`input.regex` parameter always remain in place to handle
future log entries in case new ALB log fields are added. 2. Run the query in the Athena console. After the query completes, Athena registers
the `alb_access_logs` table, making the data in it ready for you to
issue queries.
