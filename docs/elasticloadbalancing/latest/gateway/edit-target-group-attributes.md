# Edit target group attributes for your Gateway Load Balancer

After you create a target group for your Gateway Load Balancer, you can edit its target group attributes.

###### Target group attributes

- [Target failover](#target-failover "#target-failover")
- [TCP reset on target failure and deregistration](#send-tcp-reset-target-failover "#send-tcp-reset-target-failover")
- [Deregistration delay](#deregistration-delay "#deregistration-delay")
- [Flow stickiness](#flow-stickiness "#flow-stickiness")

## Target failover

With target failover, you specify how the Gateway Load Balancer handles existing traffic flows after a
target becomes unhealthy or when the target is deregistered. By default, the Gateway Load Balancer
continues to send existing flows to the same target, even if the target has failed or is
deregistered. You can manage these flows by either rehashing them
(`rebalance`) or leaving them at the default state
(`no_rebalance`).

No rebalance:

The Gateway Load Balancer continues to send existing flows to failed or drained targets.
If the Gateway Load Balancer cannot reach the target, the traffic is dropped.

However, new flows are sent to healthy targets. This is the default
behavior.

Rebalance:

The Gateway Load Balancer rehashes existing flows and sends them to healthy targets after
the deregistration delay timeout.

For deregistered targets, the minimum time to failover will depend on the
deregistration delay. The target is not marked as deregistered until
deregistration delay is completed.

For unhealthy targets, the minimum time to failover will depend on the
target group health check configuration (interval times threshold). This is
the minimum time before which a target is flagged as unhealthy. After this
time, the Gateway Load Balancer can take several minutes due to additional propagation time
and TCP retransmission backoff before it reroutes new flows to healthy
targets.

###### To update the target failover attribute using the console

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. On the navigation pane, under **Load Balancing**, choose
   **Target Groups**.
3. Choose the name of the target group to open its details page.
4. On the **Group details** page, in the
   **Attributes** section, choose
   **Edit**.
5. On the **Edit attributes** page, change the value of
   **Target failover** as needed.
6. Choose **Save changes**.

###### To update the target failover attribute using the AWS CLI

Use the [modify-target-group-attributes](../../../cli/latest/reference/elbv2/modify-target-group-attributes.md "../../../cli/latest/reference/elbv2/modify-target-group-attributes.md") command, with the following key value
pairs:

- Key=`target_failover.on_deregistration` and Value=
  `no_rebalance` (default) or `rebalance`
- Key=`target_failover.on_unhealthy` and Value=
  `no_rebalance` (default) or `rebalance`

###### Note

Both attributes (`target_failover.on_deregistration` and
`target_failover.on_unhealthy`) must have the same value.

## TCP reset on target failure and deregistration

When enabled, the Gateway Load Balancer sends a TCP reset (RST) to the sender of traffic when a
target becomes unhealthy or is deregistered, after the connection drain time
elapses. With this feature, traffic senders can recover quickly by establishing new
connections to healthy targets.

`send_tcp_reset.on_unhealthy.enabled`

Indicates whether the Gateway Load Balancer sends a TCP reset when a target becomes
unhealthy. The possible values are `true` and
`false`. The default is `false`.

`send_tcp_reset.on_deregistration.enabled`

Indicates whether the Gateway Load Balancer sends a TCP reset when a target is
deregistered and the connection drain time has elapsed. The possible
values are `true` and `false`. The default is
`false`.

###### To enable TCP reset on target failure and deregistration using the AWS CLI

Use the [modify-target-group-attributes](../../../cli/latest/reference/elbv2/modify-target-group-attributes.md "../../../cli/latest/reference/elbv2/modify-target-group-attributes.md") command, with both attributes set
to `true`.

```
`aws elbv2 modify-target-group-attributes --target-group-arn `target-group-arn` --attributes Key=send_tcp_reset.on_unhealthy.enabled,Value=true Key=send_tcp_reset.on_deregistration.enabled,Value=true`
```

###### To enable TCP reset on target failure and deregistration using the console

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation pane, under **Load Balancing**,
   choose **Target Groups**.
3. Select your target group, choose the **Attributes**
   tab, and then choose **Edit**.
4. Choose the **No rebalance and send TCP reset
   (recommended)** tile.
5. Choose **Send TCP reset on unhealthy** and
   **Send TCP reset on deregister**.
6. Choose **Save changes**.

This feature has the following requirements:

- This feature requires 5-tuple flow stickiness, which the target group
  uses by default when `stickiness.enabled` is set to
  `false`.
- You can't enable `send_tcp_reset.on_unhealthy.enabled` or
  `send_tcp_reset.on_deregistration.enabled` when
  `stickiness.enabled` is set to `true`.
- You can't enable this feature when the target failover attributes
  (`target_failover.on_unhealthy` or
  `target_failover.on_deregistration`) are set to
  `rebalance`.
- This feature applies to TCP traffic only. UDP and other protocols are
  unaffected.
- This feature works with new and existing Gateway Load Balancers.

## Deregistration delay

When you deregister a target, the Gateway Load Balancer manages flows to that target as follows:

**New flows**

The Gateway Load Balancer stops sending new flows.

**Existing flows**

The Gateway Load Balancer handles existing flows based on the protocol:

- TCP: Existing flows are closed
  if they are idle for more than 350 seconds.

- Other protocols: Existing flows
  are closed if they are idle for more than 120 seconds.

To help drain existing flows, you can enable flow rebalancing for your target group.
For more information, see [Target failover](#target-failover "#target-failover").

A deregistered target shows that it is `draining` until the timeout expires.
After the deregistration delay timeout expires, the target transitions to an
`unused` state.

###### To update the deregistration delay attribute using the console

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. On the navigation pane, under **Load Balancing**,
   choose **Target Groups**.
3. Choose the name of the target group to open its details
   page.
4. On the **Group details** page, in the
   **Attributes** section, choose
   **Edit**.
5. On the **Edit attributes** page, change the value
   of **Deregistration delay** as needed.
6. Choose **Save changes**.

###### To update the deregistration delay attribute using the AWS CLI

Use the [modify-target-group-attributes](../../../cli/latest/reference/elbv2/modify-target-group-attributes.md "../../../cli/latest/reference/elbv2/modify-target-group-attributes.md") command.

## Flow stickiness

By default, the Gateway Load Balancer maintains stickiness of flows to a specific target appliance
using 5-tuple (for TCP/UDP flows). 5-tuple includes source IP, source port, destination
IP, destination port, and transport protocol. You can use the stickiness type attribute
to modify the default (5-tuple) and choose either 3-tuple (source IP, destination IP,
and transport protocol) or 2-tuple (source IP and destination IP).

###### Flow stickiness considerations

- Flow stickiness is configured and applied at the target group level, and
  it applies to all traffic that goes to the target group.
- 2-tuple and 3-tuple flow stickiness are not supported when AWS Transit Gateway
  appliance mode is turned on. To use appliance mode on your AWS Transit Gateway,
  use 5-tuple flow stickiness on your Gateway Load Balancer
- Flow stickiness can lead to uneven distribution of connections and flows,
  which can impact the availability of the target. It is recommended that you
  terminate or drain all existing flows before modifying the stickiness type
  of the target group.

###### To update the flow stickiness attribute using the console

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. On the navigation pane, under **Load Balancing**,
   choose **Target Groups**.
3. Choose the name of the target group to open its details
   page.
4. On the **Group details** page, in the
   **Attributes** section, choose
   **Edit**.
5. On the **Edit attributes** page, change the value of
   **Flow stickiness** as needed.
6. Choose **Save changes**.

###### To update the flow stickiness attribute using the AWS CLI

Use the [modify-target-group-attributes](../../../cli/latest/reference/elbv2/modify-target-group-attributes.md "../../../cli/latest/reference/elbv2/modify-target-group-attributes.md") command with the
`stickiness.enabled` and `stickiness.type` target group attributes.
