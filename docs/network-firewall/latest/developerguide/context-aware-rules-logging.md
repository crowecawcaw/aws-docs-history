

# Context in your network firewall logs

After you associate the transit gateway for your network firewall with a context store, the firewall adds a `context` object to its flow log and alert log entries. This topic describes the fields in that object.

## Flow logs
<a name="context-logs-flow"></a>

Each flow log entry for traffic that carries context includes a `context` object with the following fields. The fields appear for every protocol, whether or not any rule matches:
+ `src` – The source identity of the flow: its VPC, subnet, transit gateway attachment, and Amazon VPC security groups.
+ `dst` – The learned destination identity of the flow, when one is available. The firewall learns the destination from the flow's first response packet, so a one-way flow has no destination context.

The following example shows a flow log entry:

```
{
    "firewall_name": "example-firewall",
    "availability_zone": "us-east-1a",
    "event_timestamp": "1728930100",
    "event": {
        "event_type": "netflow",
        "flow_id": 78037291810002,
        "src_ip": "10.0.1.25",
        "dest_ip": "10.0.2.87",
        "src_port": 44956,
        "dest_port": 8080,
        "proto": "TCP",
        "context": {
            "src": [
                "vpc-1234567890abcdef0",
                "subnet-0123456789abcdef0",
                "tgw-attach-0123456789abcdef0",
                "sg-1234567890abcdef0"
            ],
            "dst": [
                "vpc-021345abcdef6789a",
                "subnet-021345abcdef6789a",
                "tgw-attach-021345abcdef6789a",
                "sg-021345abcdef6789a"
            ]
        },
        "netflow": {
            "pkts": 10,
            "bytes": 840
        }
    }
}
```

Because flow logs record resource identity for every flow with no rules required, you can use them to discover traffic before you write rules. See [Getting started with context-aware rules](context-aware-rules-getting-started.md).

## Alert logs
<a name="context-logs-alert"></a>

When a rule that references context IDs generates an alert, the alert log entry includes a `context` object with the following field:
+ `matched` – The context IDs that the rule matched.

The following example shows an alert log entry:

```
{
    "firewall_name": "example-firewall",
    "availability_zone": "us-east-1a",
    "event_timestamp": "1728930000",
    "event": {
        "event_type": "alert",
        "flow_id": 78037291810002,
        "src_ip": "10.0.1.25",
        "dest_ip": "10.0.2.87",
        "src_port": 44956,
        "dest_port": 8080,
        "proto": "TCP",
        "context": {
            "matched": [
                "vpc-1234567890abcdef0"
            ]
        },
        "alert": {
            "action": "allowed",
            "signature_id": 1001,
            "signature": "Traffic from quarantined resources",
            "severity": 3
        }
    }
}
```

Keep the following in mind when you work with context in logs:
+ **Alert entries record the matched subset** – The alert's `context` object lists only the context IDs that the rule matched on. The flow log entry for the same flow records the source identity, and the destination identity when the firewall has learned it. The `flow_id` field joins the two. Alerts from rules that don't match on context don't include the `context` object, even when the traffic carries resource identity.
+ **Traffic without context has no context key** – Log entries for traffic that carries no resource identity omit the `context` object. The firewall never writes an empty `context` object.
+ **Flow entries record the latest identity** – If a resource's context changes during a flow, for example when you attach a different Amazon VPC security group, the flow log entry shows the identity that the flow ended with.

You can query context fields in your log destination like any other log field. The following Amazon CloudWatch Logs Insights queries find traffic from a specific Amazon VPC security group, and alerts that matched a specific VPC:

```
filter event.context.src = "sg-1234567890abcdef0"
```

```
filter event.event_type = "alert" and event.context.matched = "vpc-1234567890abcdef0"
| fields event.flow_id, event.alert.signature, event.src_ip, event.dest_ip
```

For general information about firewall logging, including destinations and permissions, see [Logging network traffic from AWS Network Firewall](firewall-logging.md).