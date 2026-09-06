

# Syslog ingestion
<a name="CWL_Syslog"></a>

Amazon CloudWatch Logs managed syslog ingestion lets you send syslog messages (RFC 5424, RFC 3164, and Cisco FTD/ASA) from firewalls, routers, switches, and Linux servers directly into CloudWatch Logs – without installing or managing any agents. Your syslog sources send messages over TCP, TCP\+TLS, or UDP to a VPC endpoint in your account. The traffic is tunneled via AWS PrivateLink to the CloudWatch Logs syslog service, which automatically parses incoming messages and extracts structured fields such as facility, severity, hostname, and application name – eliminating the need for custom parsing pipelines. You can then query these fields using CloudWatch Logs Analytics to investigate security events or troubleshoot connectivity issues. This helps you centralize infrastructure log visibility, simplify operational workflows, and reduce the overhead of deploying and maintaining log collection agents across distributed environments.

If your syslog sources are already within your Amazon VPC, they can send messages directly to the VPC endpoint. If your sources are outside AWS (on-premises data centers, branch offices, or co-location facilities), they can reach the VPC endpoint through your VPN or Direct Connect connection.

## Supported protocols and ports
<a name="CWL_Syslog_Protocols"></a>


| Protocol | Port | Notes | 
| --- | --- | --- | 
| TCP \+ TLS | 6514 | Encrypted in transit. Recommended for compliance requirements. | 
| TCP plaintext | 1514 | Plaintext over AWS PrivateLink (network-isolated). | 
| UDP | 514 | Best-effort delivery. | 

TLS on port 6514 is terminated at the network load balancer using an AWS-managed certificate issued by Amazon Trust Services. Your syslog clients trust this certificate automatically without any special configuration.

**Note**  
UDP is a best-effort protocol. Messages may be lost due to network conditions. Use TCP for reliable delivery.

## Supported syslog formats
<a name="CWL_Syslog_Formats"></a>

CloudWatch Logs automatically detects and parses the following syslog formats:
+ **RFC 5424** (the newer format) – Includes structured data, ISO 8601 timestamps, and explicit application name and process ID fields.
+ **RFC 3164** (BSD syslog, the legacy format) – Includes BSD-style timestamps and a TAG field. Still widely used by network devices such as firewalls, routers, and switches.
+ **Cisco FTD/ASA** – The syslog format used by Cisco Firepower Threat Defense (FTD) and Adaptive Security Appliance (ASA) devices. Messages are identified by the `%FTD-` or `%ASA-` tag in the message body.

Messages are stored in your log group in their original raw format. CloudWatch Logs automatically extracts structured fields from each format, which you can query using CloudWatch Logs Insights.

### RFC 5424 extracted fields
<a name="CWL_Syslog_Formats_Fields_RFC5424"></a>


| Field | Description | 
| --- | --- | 
| facility | Log category name (for example, kern, auth, local0). | 
| facilityCode | Numeric facility code (0–23). | 
| severity | Severity level name (for example, emerg, err, info). | 
| severityCode | Numeric severity code (0–7). | 
| timestamp | Message timestamp in ISO 8601 format. | 
| hostname | Source device hostname. | 
| appName | Application name. | 
| procId | Process ID. | 
| msgId | Message identifier. | 
| structuredData | RFC 5424 structured data elements (key-value metadata). | 
| message | Message body. | 

### RFC 3164 extracted fields
<a name="CWL_Syslog_Formats_Fields_RFC3164"></a>


| Field | Description | 
| --- | --- | 
| facility | Log category name. | 
| facilityCode | Numeric facility code (0–23). | 
| severity | Severity level name. | 
| severityCode | Numeric severity code (0–7). | 
| timestamp | Message timestamp (converted from BSD format to ISO 8601). | 
| hostname | Source device hostname. | 
| appName | Application name (extracted from TAG field). | 
| procId | Process ID (extracted from TAG field, if present). | 
| message | Message body. | 

### Cisco FTD/ASA extracted fields
<a name="CWL_Syslog_Formats_Fields_Cisco"></a>


| Field | Description | 
| --- | --- | 
| device | Device type (FTD, ASA, or FMC-AUDIT-LOG). | 
| timestamp | Message timestamp (RFC 3164 or RFC 5424 format, depending on device configuration). | 
| deviceId | Device hostname (present when device-id logging is configured on the appliance). | 
| severity | Severity level name (for example, informational, warning, critical). | 
| severityLevel | Numeric severity level (0–7). | 
| messageId | Cisco numeric message identifier (for example, 106023, 302013). | 
| subsystem | Subsystem name (present for certain message types). | 
| message | Message body (plain text), or individual key-value fields when the body uses Cisco's structured format. | 

## Message delivery
<a name="CWL_Syslog_Delivery"></a>

Unlike HTTP-based ingestion where the server returns a status code for each request, syslog does not provide a per-message success acknowledgment back to the sender. Once messages are received by the service, they are buffered and delivered to your log group with retries for transient errors. Delivery guarantees depend on the transport protocol you choose:
+ **TCP (ports 6514 and 1514)** – Provides reliable delivery under normal operating conditions.

  When delivery is not possible, the service resets the TCP connection to signal the failure to your client. Messages in flight on that connection may be dropped, but the connection reset provides immediate backpressure so your client can detect the issue and buffer messages locally until the condition is resolved. Under capacity pressure, the service rejects new TCP connections early, providing the same backpressure signal.

  Conditions that cause a connection reset include:
  + The VPC endpoint policy denies access
  + Your account's `PutLogEvents` quota is exceeded
  + The target log group does not exist
  + The resource policy on the log group denies access
+ **UDP (port 514)** – Best-effort delivery. Messages that cannot be delivered are dropped with no feedback to the sender. Messages may also be lost due to network congestion or capacity constraints. Use TCP if reliable delivery is important for your use case.

To detect and respond to delivery issues, monitor the `SyslogMessagesDropped` metric in CloudWatch. The `Reason` dimension indicates why messages were dropped so you can take corrective action. For more information, see [Monitoring syslog ingestion](CWL_Syslog_Monitoring.md).

## Quotas and limits
<a name="CWL_Syslog_Limits"></a>


| Limit | Value | Notes | 
| --- | --- | --- | 
| Maximum message size (TCP) | 64 KB | Standard syslog messages are typically well under this limit. If you have a use case that requires larger messages, contact AWS Support. | 
| Maximum message size (UDP) | 8 KB | Standard syslog messages are typically well under this limit. If you have a use case that requires larger messages, contact AWS Support. | 
| Ingestion throughput | Shared with PutLogEvents | Syslog ingestion counts against your account's PutLogEvents quota (5,000 requests per second per account per Region by default). | 

The `PutLogEvents` quota is adjustable. If your syslog traffic requires higher throughput, request a quota increase through [Service Quotas](https://docs.aws.amazon.com/servicequotas/latest/userguide/request-quota-increase.html).