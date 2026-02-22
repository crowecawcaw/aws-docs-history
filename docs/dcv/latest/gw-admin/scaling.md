# Scaling the Amazon DCV Connection Gateway

The following topics describe how to scale Amazon DCV Connection Gateway using a fleet of gateway hosts and a
[Network Load Balancer](../../../elasticloadbalancing/latest/network/introduction.md "../../../elasticloadbalancing/latest/network/introduction.md").

###### Topics

- [Reporting the Health of the Connection Gateway](#configuring-health-check "#configuring-health-check")
- [Configuring a Network Load Balancer](#configuring-nlb "#configuring-nlb")
  The simplified [high-level overview](what-is-gw.md#how-gw-works "what-is-gw.md#how-gw-works") includes a single Connection Gateway which forwards
  connections to a fleet of Amazon DCV server hosts. In this architecture the Connection Gateway is a single point of failure. To increase
  robustness and scalability, we can use a fleet of Connection Gateway hosts and front them with a Network Load Balancer, in order
  to preserve the ability for clients to target a single entry point to the server-side infrastructure.

![Amazon DCV Connection Gateway with NLB](images/gw-nlb.png)
With this architecture, gateway nodes can be added or removed according to the system load without any disruption for the clients.

The Network Load Balancer can _check the health_ of each instance of the Connection Gateway and
uses this information to select whether one of the Connection Gateway should or should not be used to handle incoming connections.

## Reporting the Health of the Connection Gateway

The Amazon DCV Connection Gateway can be configured to listen on an additional TCP port that will be used to check the health of the Connection Gateway service.

To enable the health check service in the Amazon DCV Connection Gateway, edit the `/etc/dcv-connection-gateway/dcv-connection-gateway.conf` and add the following:

```
[health-check]
bind-addr = "::"
port = 8989

```

The `bind-addr` and `port` are the IP address and TCP port used by the health check service.
They need to be reachable from the Network Load Balancer. `bind-addr` can use IPv4 or IPv6 addresses.

## Configuring a Network Load Balancer

The following steps summarize how to create a Network Load Balancer and highlight the settings which are needed to use
a Network Load Balancer with Amazon DCV Connection Gateway. See the [Network Load Balancer documentation](../../../elasticloadbalancing/latest/network/introduction.md "../../../elasticloadbalancing/latest/network/introduction.md") for more detailed information.

###### To create a Network Load Balancer for a fleet of Amazon DCV Connection Gateway hosts

1. Navigate to the [EC2 Console](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/"), select **Load Balancer** from
   the navigation pane and then choose **Create Load Balancer**. For load balancer type, choose **Network Load Balancer**.
2. For **Basic Configuration** assign a **Name**, set **Scheme** to **internet-facing**,
   and set **Ip address type** to **IPv4**.
3. For **Network mapping** select your **VPC** and then select all the availability zones and subnets in that VPC.
   Make sure that your DCV Connection Gateway instances security groups allow traffic from the selected subnets.
4. For **Listeners and routing** create a TCP target group, specifying the `web-port` of the Amazon DCV Connection Gateway configuration as the port.

For the _health check_, make sure TCP is used and override the TCP port with the one specified in the `[health-check]` section of the Amazon DCV Connection Gateway configuration.

If you also want QUIC support, create a UDP target group, specifying the `quic-port` of the Amazon DCV Connection Gateway configuration as the port.

For the _health check_ use the same values as before: make sure TCP is used and override the TCP port with the one specified in the `[health-check]` section of the Amazon DCV Connection Gateway configuration.

###### Note

When using a TLS listener on your Elastic Load Balancer, the Target Group also needs to be set to TLS.

If you have enabled QUIC, once the Network Load Balancer is created, select it from the list, select the _UDP listener_
and make sure the **Stickiness** check box is active.
