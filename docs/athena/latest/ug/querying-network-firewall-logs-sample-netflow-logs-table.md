# Create and query a table for netflow logs

1. Modify the following sample DDL statement to conform to the structure of your
   netflow logs. You may need to update the statement to include the columns for
   the latest version of the logs. For more information, see [Contents of a firewall log](../../../network-firewall/latest/developerguide/firewall-logging.md#firewall-logging-contents "../../../network-firewall/latest/developerguide/firewall-logging.md#firewall-logging-contents") in the
   _AWS Network Firewall Developer Guide_.

```
CREATE EXTERNAL TABLE network_firewall_netflow_logs (
  firewall_name string,
  availability_zone string,
  event_timestamp string,
  event struct<
    timestamp:string,
    flow_id:bigint,
    event_type:string,
    src_ip:string,
    src_port:int,
    dest_ip:string,
    dest_port:int,
    proto:string,
    app_proto:string,
    tls_inspected:boolean,
    netflow:struct<
      pkts:int,
      bytes:bigint,
      start:string,
      `end`:string,
      age:int,
      min_ttl:int,
      max_ttl:int,
      tcp_flags:struct<
        syn:boolean,
        fin:boolean,
        rst:boolean,
        psh:boolean,
        ack:boolean,
        urg:boolean
        >
      >
    >
)
ROW FORMAT SERDE 'org.openx.data.jsonserde.JsonSerDe'
LOCATION 's3://amzn-s3-demo-bucket/`path_to_netflow_logs_folder`/';
```

2. Modify the `LOCATION` clause to specify the folder for your logs in
   Amazon S3.
3. Run the `CREATE TABLE` query in the Athena query editor. After the
   query completes, Athena registers the `network_firewall_netflow_logs`
   table, making the data that it points to ready for queries.

## Example query

The sample netflow log query in this section filters for events in which TLS
inspection was performed.

The query uses aliases to create output column headings that show the
`struct` that the column belongs to. For example, the column heading
for the `event.netflow.bytes` field is `event_netflow_bytes`
instead of just `bytes`. To customize the column names further, you can
modify the aliases to suit your preferences. For example, you can use underscores or
other separators to delimit the `struct` names and field names.

Remember to modify column names and `struct` references based on your
table definition and on the fields that you want in the query result.

```
SELECT
  event.src_ip AS event_src_ip,
  event.dest_ip AS event_dest_ip,
  event.proto AS event_proto,
  event.app_proto AS event_app_proto,
  event.tls_inspected AS event_tls_inspected,
  event.netflow.pkts AS event_netflow_pkts,
  event.netflow.bytes AS event_netflow_bytes,
  event.netflow.tcp_flags.syn AS event_netflow_tcp_flags_syn
FROM network_firewall_netflow_logs
WHERE event.tls_inspected = true
```
