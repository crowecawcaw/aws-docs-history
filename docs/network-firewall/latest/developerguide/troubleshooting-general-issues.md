# Troubleshooting general issues in AWS Network Firewall

Use the information here to help you diagnose and fix common issues when you work with Network Firewall.

## Firewall endpoint creation or deletion fails

If Network Firewall can't create or delete a firewall endpoint in the subnet because of an error, the service displays a status message describing how to resolve the issues. You can view the status message in the console or API. For more information about troubleshooting firewall creation and deletion issues, see [Troubleshooting firewall endpoint
failures](firewall-troubleshooting-endpoint-failures.md "firewall-troubleshooting-endpoint-failures.md").

## Availability Zone is unsupported

When you try to create a firewall, you get the following error “Availability zone subnet(s) cannot be updated or added because this Availability Zone is not supported by Network Firewall”.

You might be trying to create the Network Firewall in a constrained Availability Zone—a zone in which our ability to expand is constrained. We cannot support Network Firewall in these Availability Zones. You can move your resources to an unconstrained Availability Zone so that your resources and your Network Firewall are in the same zone.

## How do I check if I have asymmetric routing?

AWS Network Firewall doesn't support asymmetric routing. Request and response traffic must be routed to the same firewall endpoint. The recommended best practice is to route traffic to the firewall endpoint closest to the client in both directions. Failure to route traffic symmetrically to the same firewall endpoint prevents stateful features from working correctly, such as application layer inspection. You can use the Amazon VPC [Reachability Analyzer](../../../vpc/latest/reachability/what-is-reachability-analyzer.md "../../../vpc/latest/reachability/what-is-reachability-analyzer.md"), or in Network Firewall, you can use either the [stateless rule group analyzer](stateless-rule-group-analyzer.md "stateless-rule-group-analyzer.md") or flow and alert logging as outlined in the following section.

###### To test whether routing is symmetric using Network Firewall flow and alert logs:

1. Create a firewall using the procedure, and associate an empty **Strict order** rule evaluation order policy to it. The stateless default action should **Forward to stateful rule groups** for both full and fragmented packets. For this test, you don't need to enable any stateful default actions.
2. From the console, select the firewall you created in the previous step. On the **Firewall details** tab, navigate to the **Logging** tab and select **Edit**. Choose **Alert** and **Flow**, and select a separate Amazon CloudWatch log group for each log type. For example, choose `my-firewall-flow-logs` and `my-firewall-alert-logs`. If the log groups don't exist, choose **Create log group** to be redirected to the CloudWatch log groups console. Once created, you can refresh the log group list in the firewall logging console. After you select the log groups, select **Save**.
3. Create a Suricata-compatible rule group using the [Creating a stateful rule
   group](rule-group-stateful-creating.md "rule-group-stateful-creating.md"), and include the following Suricata rule:

```
alert tcp any any -> any any (msg:"Routing is symmetric. You can safely remove this test rule."; flow:established; sid:123456;)
```

4. From an instance behind the firewall, attempt to connect to `https://www.amazon.com` using cURL or a web browser. The test should succeed based on the firewall policy and rule configuration you created in the previous steps. If the request and response traffic routes symmetrically through the same firewall endpoint, the alert rule should match the established TCP flow and an alert log event should be published to the CloudWatch log group. Be aware that there might be a delay to publish the alert log event to the log destination.
5. From the CloudWatch log groups console, search the firewall alert log group for `www.amazon.com`.
6. An alert log event similar to the following means the stateful engine saw the TCP 3-way handshake bidirectionally (`flow:established`) and was able to reassemble the flow as application layer protocol TLS. This is a positive indication that routing is configured symmetrically.

```
{
    "firewall_name": "protected-vpc-fw",
    "availability_zone": "us-east-1a",
    "event_timestamp": "1122334455",
    "event": {
       ** "app_proto": "tls",
        "src_ip": "18.154.234.51",
        "src_port": 443,
        "event_type": "alert",
        "alert": {
            "severity": 3,
            "signature_id": 123456,
            "rev": 0,
            "signature": "Routing is symmetric. You can safely remove this test rule.",
            "action": "allowed",
            "category": ""
        },
        "flow_id": 49218262306386,
        "dest_ip": "10.170.19.217",
        "proto": "TCP",
        "tls": {
            "subject": "CN=www.amazon.com",
            "issuerdn": "C=US, O=DigiCert Inc, CN=DigiCert Global CA G2",
            "serial": "05:21:67:4F:03:57:5F:5B:A5:BD:6B:2B:CC:A0:EB:4B",
            "fingerprint": "91:78:b8:6a:9b:40:ad:af:ad:6b:25:ad:a3:d2:39:e5:39:af:86:9a",
            "sni": "www.amazon.com",
            "version": "TLS 1.2",
            "notbefore": "2023-01-17T00:00:00",
            "notafter": "2024-01-16T23:59:59",
            "ja3": {},
            "ja3s": {}
        },
        "dest_port": 60460,
        "timestamp": "2023-07-27T14:56:49.250792+0000"
    }
}
```

7. (Optional) To further confirm that routing is configured symmetrically, you can copy the `flow_id` value from the alert log event (for example, `77665544332211`). From the CloudWatch log groups console, search the firewall flow log group for the `flow_id` value from the alert log event. For flow `77665544332211` in this example, separate firewall flow log events were published for the request and response traffic. This is a positive indication that routing is configured symmetrically. If you only see a flow log event for the request side of the conversation, the routing in the response path may be directing traffic around the firewall endpoint. It could also be an indication that routing is configured symmetrically but a Network ACL or security group are blocking the inbound traffic on the server.

```
Request flow (client > server):

{
    "firewall_name": "protected-vpc-fw",
    "availability_zone": "us-east-1a",
    "event_timestamp": "3344556677",
    "event": {
        "tcp": {
            "tcp_flags": "1b",
            "syn": true,
            "fin": true,
            "psh": true,
            "ack": true
        },
        "app_proto": "tls",
        "src_ip": "10.170.19.217",
        "src_port": 60460,
        "netflow": {
            "pkts": 13,
            "bytes": 1527,
            "start": "2023-07-27T14:54:02.888402+0000",
            "end": "2023-07-27T14:54:02.923400+0000",
            "age": 0,
            "min_ttl": 254,
            "max_ttl": 254
        },
        "event_type": "netflow",
        "flow_id": 77665544332211,
        "dest_ip": "18.154.234.51",
        "proto": "TCP",
        "dest_port": 443,
        "timestamp": "2023-07-27T14:56:49.250816+0000"
    }
}

Response flow (server > client):

{
    "firewall_name": "protected-vpc-fw",
    "availability_zone": "us-east-1a",
    "event_timestamp": "2233445566",
    "event": {
        "tcp": {
            "tcp_flags": "1b",
            "syn": true,
            "fin": true,
            "psh": true,
            "ack": true
        },
        "app_proto": "tls",
        "src_ip": "18.154.234.51",
        "src_port": 443,
        "netflow": {
            "pkts": 16,
            "bytes": 9125,
            "start": "2023-07-27T14:54:02.888402+0000",
            "end": "2023-07-27T14:54:02.923400+0000",
            "age": 0,
            "min_ttl": 246,
            "max_ttl": 246
        },
        "event_type": "netflow",
        "flow_id": 49218262306386,
        "dest_ip": "10.170.19.217",
        "proto": "TCP",
        "dest_port": 60460,
        "timestamp": "2023-07-27T14:56:49.250823+0000"
    }
}
```

For more information about asymmetric routing, see [Avoiding asymmetric routing with AWS Network Firewall](asymmetric-routing.md "asymmetric-routing.md").

## I'm using Network Firewall with AWS Transit Gateway and Network Firewall is dropping traffic

Network Firewall is a managed service that uses a Gateway Load Balancer to distribute traffic flows across backend firewall appliances for high availability and scale. Network Firewall requires symmetric routing, and needs to see the forward and return traffic flow to track flow state and apply stateful rules. Many customers use a centralized architecture to inspect VPC-to-VPC or VPC-to-on-premise traffic. In a centralized architecture, Network Firewall is deployed in an inspection VPC and customers use a AWS Transit Gateway transit gateway to route the traffic through inspection VPC.

If you have a centralized architecture, make sure that appliance mode is enabled on the transit gateway. When you enable the appliance mode, a transit gateway selects a single network interface in the appliance VPC, using a flow hash algorithm, to send traffic to same backend firewall appliance for the life of the flow. The transit gateway uses the same network interface for the return traffic. This ensures that bi-directional traffic is routed symmetrically; in other words, it's routed through the same Availability Zone in the VPC attachment for the life of the flow. For information about appliance mode in Transit Gateway, see [Example: Appliance in a shared services VPC](../../../vpc/latest/tgw/transit-gateway-appliance-scenario.md "../../../vpc/latest/tgw/transit-gateway-appliance-scenario.md") in the _Amazon VPC Transit Gateways_.

## High latency and intermittent packet drops when traffic passes through Network Firewall

Network latency and packet drops can occur for multiple reasons such as a sudden burst in
traffic, asymmetric routing, applications with longer TCP timeouts, or issues
occurring outside of the Network Firewall service. Try these steps to identify the root
cause:

1. **Monitor CloudWatch metrics** – You can monitor [CloudWatch metrics for AWS PrivateLink](../../../vpc/latest/privatelink/privatelink-cloudwatch-metrics.md "../../../vpc/latest/privatelink/privatelink-cloudwatch-metrics.md") such as `ActiveConnections`, `BytesProcessed`, and `PacketsDropped` for the Gateway Load Balancer endpoint interfaces in your VPC. Create a ticket with AWS Support if the `PacketsDropped` metric is increasing. To understand what traffic is traversing a Gateway Load Balancer endpoint, you can enable [custom format](../../../vpc/latest/userguide/flow-logs.md#flow-logs-custom "../../../vpc/latest/userguide/flow-logs.md#flow-logs-custom") Amazon VPC flow logs for each interface. For traffic routed to Network Firewall, you can review stateless and stateful [Network Firewall metrics](monitoring-cloudwatch.md#metrics "monitoring-cloudwatch.md#metrics") such as `ReceivedPackets` to understand the volume of packets when high latency is observed.
2. **Asymmetrically-forward connections** – Check if you have asymmetrically-forward connections on your network. For more information about how to check asymmetric routing, see [How do I check if I have asymmetric routing?](#troubleshoot-check-asymmetric-routing-tg "#troubleshoot-check-asymmetric-routing-tg"). When forwarding traffic from the stateless engine to stateful, you must forward the request and response traffic bi-directionally. Be aware that unidirectional pass rules can create asymmetric forwarding when the policy's stateless default action is **Forward to stateful rule groups**.

Make sure that your stateless rules forward traffic symmetrically to the stateful engine using the **forward to stateful rule groups** action. Often this means writing pairs of rules to match both forward and return direction traffic. Asymmetrically forwarded packets are subject to the [stream exception policy](stream-exception-policy.md "stream-exception-policy.md") action, which by default is configured to **drop**. You can check the `StreamExceptionPolicyPackets` metric in CloudWatch, which counts the number of times that stream exception policy is invoked. If you have asymmetrically-forwarded connections, this metric count will be high during the time you noticed high latency or packet drops. You can change the stream exception policy configuration in the firewall policy to determine how Network Firewall handles asymmetrically-forwarded connections. The following stream exception policy actions correlate to the specified CloudWatch metrics:

    * `DROP` – Matching packets are dropped and counted in both the `StreamExceptionPolicyPackets` metric as well as the `DroppedPackets` metric.
    * `REJECT` – Matching packets receive a TCP reset response and are counted in both the `StreamExceptionPolicyPackets` metric as well as the `RejectedPackets` metric. Any further packets from these rejected connections are dropped and reflected in the `DroppedPackets` metric.
    * `CONTINUE` Matching packets are counted in the `StreamExceptionPolicyPackets` metric but continue to be processed by rules. Therefore if you use the `CONTINUE` value in the stream exception policy, elevated values of this metric aren't necessarily a cause for concern. Please note that Network Firewall will continue to inspect these connections using your firewall rules and a connection can be dropped if it matches with a drop action rule.

For information about using CloudWatch metrics for Network Firewall, see [Metrics in CloudWatch](monitoring-cloudwatch.md "monitoring-cloudwatch.md"). 3. **Long TCP idle timeouts** – Check if you have applications with long TCP timeouts. Network Firewall uses a Gateway Load Balancer (GWLB) endpoint to distribute flows to backend firewall instances. By default, Gateway Load Balancer has a [fixed idle timeout](../../../elasticloadbalancing/latest/gateway/gateway-load-balancers.md#idle-timeout "../../../elasticloadbalancing/latest/gateway/gateway-load-balancers.md#idle-timeout") of 350 seconds for TCP flows. Once the idle timeout is reached or a TCP connection is closed for a flow, it is removed from the firewall's connection state table. This can result in the flow timing out on the client side. Subsequent non-SYN TCP packets for a removed flow may be dropped by Gateway Load Balancer. New TCP connection requests using the same 5-tuple (source/destination IP, source/destination port and protocol) might be routed to a different backend firewall instance than before. In this case, since the Gateway Load Balancer timeout is lower than the timeout value on your application, Gateway Load Balancer removes the flow without the application being aware it was dropped.

To prevent this from happening, we recommend either configuring the **TCP keep-alive** setting on your client and server's application or operating system or configuring the idle timeout period in the Network Firewall console. If you choose to update the TCP keep-alive setting, set the value to a shorter period than the default 350 seconds. This ensures that the client and server keep the flow alive if there's inactivity, or the flow is removed from Network Firewall. If you choose to update the idle timeout value in the Network Firewall console, set the value to a longer period than the default 350 seconds. This ensures that your firewall can go without detecting traffic for longer than 350 seconds without dropping traffic. For more information about Gateway Load Balancer, see [Gateway Load Balancers](../../../elasticloadbalancing/latest/gateway/gateway-load-balancers.md "../../../elasticloadbalancing/latest/gateway/gateway-load-balancers.md") in the _Elastic Load Balancing User Guide_. For more information about the idle timeout setting in Network Firewall, see [Firewall policy settings](firewall-policy-settings.md "firewall-policy-settings.md"). 4. **Amazon Virtual Private Cloud NAT gateway port allocation errors** – - Sometimes you'll see increased latency or packet drops on your traffic if your Amazon VPC NAT gateway is running out of ports to establish new connections which can result in packet drops and high latency. You can look at the NAT gateway `ErrorPortAllocation` errors to ensure NAT gateway is able to support new connections. If you notice NAT gateway `ErrorPortAllocation` errors, create a support case and the AWS Support team can help you resolve it. To troubleshoot your NAT gateway, you can look at `IdleTimeoutCount`, `PacketsDropCount` and other metrics as described in the [Monitor NAT gateways with CloudWatch](../../../vpc/latest/userguide/vpc-nat-gateway-cloudwatch.md "../../../vpc/latest/userguide/vpc-nat-gateway-cloudwatch.md") topic in the _Amazon VPC Developer Guide_.
