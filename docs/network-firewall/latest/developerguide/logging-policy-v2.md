

# Logging for a Next Generation policy in AWS Network Firewall
<a name="logging-policy-v2"></a>

A firewall that uses a Next Generation policy logs events the same way as a firewall that uses a Classic Network Firewall policy. You configure logging in the same way, and there's no new log type and no new logging configuration to set up. For information about Next Generation policies, see [Next Generation policies](firewall-policies-v2.md). For information about configuring logging, see [Logging network traffic from AWS Network Firewall](firewall-logging.md).

Even though a Next Generation policy uses two inspection engines, both engines report through the same `alert` EVE event type, into the same log destination you already configure. There's no separate log stream for each engine.

**Telling firewall engine events from IPS engine events**  
To tell which engine produced a log record, use the `engine` field inside the `alert` object. It has one of the following values:
+ `fw` – The event came from the firewall engine.
+ `td` – The event came from the IPS engine.

In the following example alert log entry, `"engine": "fw"` shows that the event came from the firewall engine. The `firewall` object reports the hook that the packet was evaluated at and the policy that was applied, and the `verdict` object reports the action that Network Firewall took. In this example, the firewall engine's default action dropped the packet.

```
{
    "firewall_name": "example-fw",
    "availability_zone": "us-east-1d",
    "event_timestamp": "1600000000",
    "event": {
        "app_proto": "ntp",
        "ip_v": 4,
        "src_ip": "10.0.2.53",
        "src_port": 49152,
        "event_type": "alert",
        "alert": {
            "severity": 3,
            "signature_id": 2201000,
            "rev": 1,
            "engine": "fw",
            "signature": "SURICATA FW default packet policy",
            "action": "blocked",
            "category": ""
        },
        "firewall": {
            "hook": "packet:filter",
            "policy": "drop:flow,alert"
        },
        "flow_id": 1111111111111111,
        "dest_ip": "10.0.2.100",
        "proto": "UDP",
        "verdict": {
            "action": "drop"
        },
        "dest_port": 123,
        "timestamp": "2020-09-13T12:26:40.000000+0000",
        "direction": "to_server"
    }
}
```

The following example shows a firewall engine alert under an **Alert** default action, or under any default action while the policy is in monitor mode. The `policy` is `accept:hook,alert` and the `verdict` action is `accept`, so the packet was allowed and recorded in the alert log.

```
{
    "firewall_name": "example-fw",
    "availability_zone": "us-east-1d",
    "event_timestamp": "1600000000",
    "event": {
        "app_proto": "tls",
        "ip_v": 4,
        "src_ip": "10.0.2.53",
        "src_port": 47610,
        "event_type": "alert",
        "alert": {
            "severity": 3,
            "signature_id": 2201000,
            "rev": 1,
            "engine": "fw",
            "signature": "SURICATA FW default packet policy",
            "action": "allowed",
            "category": ""
        },
        "firewall": {
            "hook": "packet:filter",
            "policy": "accept:hook,alert"
        },
        "flow_id": 1111111111111111,
        "dest_ip": "10.0.2.100",
        "proto": "TCP",
        "verdict": {
            "action": "accept"
        },
        "dest_port": 443,
        "timestamp": "2020-09-13T12:26:40.000000+0000",
        "direction": "to_server"
    }
}
```

You can also use the `resource_arn` field to identify the source of an event. The resource type in the ARN distinguishes a firewall rule group (`firewall-rulegroup/`), an IPS rule group (`ips-rulegroup/`), and a Next Generation policy (`firewall-policy-v2/`). The policy ARN (`firewall-policy-v2/`) is carried when the event isn't attributable to one of your own rule groups—for example, when the firewall engine's default action is applied. An alert from a managed rule carries the managed rule group's ARN (an `ips-rulegroup/` ARN under your account), not the policy ARN. Use the `engine` field or the `resource_arn` resource type as a stable key for filtering your logs—for example, to separate access-control events (the firewall engine) from threat-detection events (the IPS engine).

**Logging in monitor mode**  
When a Next Generation policy is in monitor mode, both engines still generate the same `alert` event records, but no traffic is dropped or rejected. If you use monitor mode to validate rules before enforcing them, your logs continue to show the actions the engines would have applied. For more information about monitor mode, see [Policy mode: enforce and monitor](firewall-policy-v2-policy-mode.md).