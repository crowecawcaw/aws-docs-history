# Create and query a table for alert logs

1. Modify the following sample DDL statement to conform to the structure of your
   alert log. You may need to update the statement to include the columns for the
   latest version of the logs. For more information, see [Contents of a firewall log](../../../network-firewall/latest/developerguide/firewall-logging.md#firewall-logging-contents "../../../network-firewall/latest/developerguide/firewall-logging.md#firewall-logging-contents") in the
   _AWS Network Firewall Developer Guide_.

```
CREATE EXTERNAL TABLE network_firewall_alert_logs (
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
    sni:string,
    tls_inspected:boolean,
    tls_error:struct<
      error_message:string>,
    revocation_check:struct<
      leaf_cert_fpr:string,
      status:string,
      action:string>,
    alert:struct<
      alert_id:string,
      alert_type:string,
      action:string,
      signature_id:int,
      rev:int,
      signature:string,
      category:string,
      severity:int,
      rule_name:string,
      alert_name:string,
      alert_severity:string,
      alert_description:string,
      file_name:string,
      file_hash:string,
      packet_capture:string,
      reference_links:array<string>
    >,
    src_country:string,
    dest_country:string,
    src_hostname:string,
    dest_hostname:string,
    user_agent:string,
    url:string
   >
)
 ROW FORMAT SERDE 'org.openx.data.jsonserde.JsonSerDe'
 LOCATION 's3://amzn-s3-demo-bucket/`path_to_alert_logs_folder`/';
```

2. Modify the `LOCATION` clause to specify the folder for your logs in
   Amazon S3.
3. Run your `CREATE TABLE` query in the Athena query editor. After the
   query completes, Athena registers the `network_firewall_alert_logs`
   table, making the data that it points to ready for queries.

## Example query

The sample alert log query in this section filters for events in which TLS
inspection was performed that have alerts with a severity level of 2 or
higher.

The query uses aliases to create output column headings that show the
`struct` that the column belongs to. For example, the column heading
for the `event.alert.category` field is `event_alert_category`
instead of just `category`. To customize the column names further, you
can modify the aliases to suit your preferences. For example, you can use
underscores or other separators to delimit the `struct` names and field
names.

Remember to modify column names and `struct` references based on your
table definition and on the fields that you want in the query result.

```
SELECT
  firewall_name,
  availability_zone,
  event_timestamp,
  event.timestamp AS event_timestamp,
  event.flow_id AS event_flow_id,
  event.event_type AS event_type,
  event.src_ip AS event_src_ip,
  event.src_port AS event_src_port,
  event.dest_ip AS event_dest_ip,
  event.dest_port AS event_dest_port,
  event.proto AS event_protol,
  event.app_proto AS event_app_proto,
  event.sni AS event_sni,
  event.tls_inspected AS event_tls_inspected,
  event.tls_error.error_message AS event_tls_error_message,
  event.revocation_check.leaf_cert_fpr AS event_revocation_leaf_cert,
  event.revocation_check.status AS event_revocation_check_status,
  event.revocation_check.action AS event_revocation_check_action,
  event.alert.alert_id AS event_alert_alert_id,
  event.alert.alert_type AS event_alert_alert_type,
  event.alert.action AS event_alert_action,
  event.alert.signature_id AS event_alert_signature_id,
  event.alert.rev AS event_alert_rev,
  event.alert.signature AS event_alert_signature,
  event.alert.category AS event_alert_category,
  event.alert.severity AS event_alert_severity,
  event.alert.rule_name AS event_alert_rule_name,
  event.alert.alert_name AS event_alert_alert_name,
  event.alert.alert_severity AS event_alert_alert_severity,
  event.alert.alert_description AS event_alert_alert_description,
  event.alert.file_name AS event_alert_file_name,
  event.alert.file_hash AS event_alert_file_hash,
  event.alert.packet_capture AS event_alert_packet_capture,
  event.alert.reference_links AS event_alert_reference_links,
  event.src_country AS event_src_country,
  event.dest_country AS event_dest_country,
  event.src_hostname AS event_src_hostname,
  event.dest_hostname AS event_dest_hostname,
  event.user_agent AS event_user_agent,
  event.url AS event_url
FROM
  network_firewall_alert_logs
WHERE
  event.alert.severity >= 2
  AND event.tls_inspected = true
LIMIT 10;
```
