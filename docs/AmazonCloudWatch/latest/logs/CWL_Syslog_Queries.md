# Sample queries for syslog data

The following CloudWatch Logs Insights queries demonstrate common analysis patterns for
syslog data. They use the structured fields that CloudWatch Logs automatically extracts from
RFC 5424, RFC 3164, and Cisco FTD/ASA messages. For the complete list of extracted
fields, see [Supported syslog formats](CWL_Syslog.md#CWL_Syslog_Formats "CWL_Syslog.md#CWL_Syslog_Formats").

These queries are also available in the CloudWatch console. In CloudWatch Logs Insights,
choose **Queries**, and then expand the **Syslog**
category.

## Security and access monitoring

### Sudo and privilege escalation events

The following query lists recent sudo privilege-escalation activity on Linux
hosts. It filters for the `sudo` application name and works with both
RFC 3164 and RFC 5424 messages.

```
filter appName="sudo"
| fields @timestamp, hostname, message
| sort @timestamp desc
| limit 50
```

### Top 50 hosts with failed SSH authentication

The following query counts failed SSH authentication attempts for each host. It
matches sshd messages that contain "Failed password" or "Failed publickey". Use it
to identify hosts that are targets of brute-force attacks.

```
filter appName="sshd" and (message like /Failed password/ or message like /Failed publickey/)
| stats count(*) as failedAttempts by hostname
| sort failedAttempts desc
| limit 50
```

## Operational visibility

### Log volume by host over time

The following query counts messages for each host in 5-minute intervals. Use it
to measure fleet activity, identify volume spikes, or detect hosts that have
stopped sending. This query works with all syslog format types.

```
stats count(*) as messages by hostname, bin(5m)
| sort messages desc
```

### Message volume by facility and severity

The following query counts messages grouped by facility and severity level. Use
it to understand which subsystems generate the most log traffic and at what
severity level.

```
stats count(*) as messageCount by facility, severity
| sort messageCount desc
```

### High-severity messages by application

The following query filters to high-priority messages (severityCode 0–3,
which corresponds to emerg, alert, crit, and err) and counts them by application.
Use it to identify which applications are generating the most errors.

```
filter severityCode<=3
| stats count(*) as errorCount by appName
| sort errorCount desc
```

### Warning-and-above trend over time

The following query counts messages at warning severity or higher (severityCode
0–4) in 5-minute intervals. Use it with the visualization feature in Logs
Insights to chart error spikes over time.

```
filter severityCode<=4
| stats count(*) as events by bin(5m)
| sort @timestamp
```

## Firewall and network device queries

### Cisco denied connections (ACL 106023)

The following query is for Cisco ASA and FTD firewalls. It counts ACL-denied
connections (Cisco message ID 106023) grouped by device, which helps you identify
devices with the most denied traffic.

```
filter messageId="106023"
| stats count(*) as denies by deviceId
| sort denies desc
| limit 20
```

### Cisco ASA/FTD events by message ID

The following query is for Cisco FTD and ASA firewalls. It counts events grouped
by Cisco message ID and severity to help you identify the most frequent event types
across your firewall fleet.

```
filter ispresent(messageId)
| stats count(*) as eventCount by messageId, severity
| sort eventCount desc
```

### Firewall dropped packets by source IP

The following query parses firewall DROP messages (for example, from iptables or
nftables) to count dropped packets by source IP address. Use it to identify the top
sources of blocked traffic.

```
filter message like /DROP/
| parse message /SRC=(?<srcAddr>\S+)/
| stats count(*) as drops by srcAddr
| sort drops desc
| limit 20
```
