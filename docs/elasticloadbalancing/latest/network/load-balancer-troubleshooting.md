# Troubleshoot your Network Load Balancer

The following information can help you troubleshoot issues with your Network Load Balancer.

## A registered target is not in service

If a target is taking longer than expected to enter the `InService` state,
it might be failing health checks. Your target is not in service until it passes one
health check. For more information, see [Health checks for Network Load Balancer target groups](target-group-health-checks.md "target-group-health-checks.md").

Verify that your instance is failing health checks and then check for the
following:

**A security group does not allow traffic**

The security groups associated with an instance must allow traffic from
the load balancer using the health check port and health check protocol. For
more information, see [Target security groups](target-group-register-targets.md#target-security-groups "target-group-register-targets.md#target-security-groups"). Also, the security group for
your load balancer must allow traffic to the instances. For more information,
see [Update the security groups for your Network Load Balancer](load-balancer-security-groups.md "load-balancer-security-groups.md").

**A network access control list (ACL) does not allow traffic**

The network ACL associated with the subnets for your instances and the
subnets for your load balancer must allow traffic and health checks from the
load balancer. For more information, see [Network ACLs](target-group-register-targets.md#network-acls "target-group-register-targets.md#network-acls").

## Requests are not routed to targets

Check for the following:

**A security group does not allow traffic**

The security groups associated with the instances must allow traffic on
the listener port from client IP addresses (if targets are specified by
instance ID) or load balancer nodes (if targets are specified by IP
address). For more information, see [Target security groups](target-group-register-targets.md#target-security-groups "target-group-register-targets.md#target-security-groups"). Also, the security group for
your load balancer must allow traffic to the instances. For more information,
see [Update the security groups for your Network Load Balancer](load-balancer-security-groups.md "load-balancer-security-groups.md").

**A network access control list (ACL) does not allow traffic**

The network ACLs associated with the subnets for your VPC must allow the
load balancer and targets to communicate in both directions on the listener
port. For more information, see [Network ACLs](target-group-register-targets.md#network-acls "target-group-register-targets.md#network-acls").

**The targets are in an Availability Zone that is not enabled**

If you register targets in an Availability Zone but do not enable the
Availability Zone, these registered targets do not receive traffic from the
load balancer.

**The instance is in a peered VPC**

If you have instances in a VPC that is peered with the load balancer VPC,
you must register them with your load balancer by IP address, not by
instance ID.

**The server ID configured doesn't match the ID configured on the target.**

If you are using QUIC listeners, ensure that the ID configured on the target matches
the ID configured with the Network Load Balancer target group.

## Targets receive more health check requests than

expected

Health checks for a Network Load Balancer are distributed and use a consensus mechanism to determine
target health. Therefore, targets receive more than the number of health checks
configured through the `HealthCheckIntervalSeconds` setting.

## Targets receive fewer health check requests than

expected

Check whether `net.ipv4.tcp_tw_recycle` is enabled. This setting is known
to cause issues with load balancers. The `net.ipv4.tcp_tw_reuse` setting is
considered a safer alternative.

## Unhealthy targets receive requests from the load balancer

This occurs when all registered targets are unhealthy. If there is at least one healthy
registered target, your Network Load Balancer routes requests only to its healthy registered targets.

When there are only unhealthy registered targets, the Network Load Balancer routes requests to all the
registered targets, known as fail-open mode. The Network Load Balancer does this instead of removing all
the IP addresses from DNS when all the targets are unhealthy and respective Availability
Zones do not have healthy target to send request to.

## Target fails HTTP or HTTPS health checks due to

host header mismatch

The HTTP host header in the health check request contains the IP address of the load
balancer node and the listener port, not the IP address of the target and the health
check port. If you are mapping incoming requests by host header, you must ensure that
health checks match any HTTP host header. Another option is to add a separate HTTP
service on a different port and configure the target group to use that port for health
checks instead. Alternatively, consider using TCP health checks.

## Unable to associate a security group

with a load balancer

If the Network Load Balancer was created without security groups, it can't support security groups
after creation. You can only associate a security group to a load balancer during
creation, or to an existing load balancer that was originally created with security
groups.

## Unable to remove all security

groups

If the Network Load Balancer was created with security groups, there must be at least one security
group associated with it at all times. You cannot remove all security groups from the
load balancer at the same time.

## Increase in TCP_ELB_Reset_Count metric

For each TCP request that a client makes through a Network Load Balancer, the state of that connection
is tracked. If no data is sent through the connection by either the client or the target
for longer than the idle timeout, the connection is closed. If a client or a target
sends data after the idle timeout period elapses, it receives a TCP RST packet to
indicate that the connection is no longer valid. Additionally, if a target becomes
unhealthy, the load balancer sends a TCP RST for packets received on the client
connections associated with the target, unless the unhealthy target triggers the load
balancer to fail open.

If you see a spike in the `TCP_ELB_Reset_Count` metric just before or just
as the `UnhealthyHostCount` metric increases, it is likely that the TCP RST
packets were sent because the target was starting to fail but hadn't been marked
unhealthy. If you see persistent increases in `TCP_ELB_Reset_Count` without
targets being marked unhealthy, you can check the VPC flow logs for clients sending data
on expired flows.

## Connections time out for requests from a target to

its load balancer

Check whether client IP preservation is enabled on your target group. NAT loopback,
also known as hairpinning, is not supported when client IP preservation is enabled.

If an instance is a client of a load balancer that it's registered with and it has
client IP preservation enabled, the connection succeeds only if the request is routed to a
different instance. If the request is routed to the same instance it was sent from,
the connection times out because the source and destination IP addresses are the same.
Note that this applies to Amazon EKS pods running in the same EC2 worker node instance, even
though they have different IP addresses.

If an instance must send requests to a load balancer that it's registered with, do one
of the following:

- Disable client IP preservation. Instead, use Proxy Protocol v2 to get the client
  IP address.
- Ensure that containers that must communicate are on different container
  instances.

## Performance decreases when moving targets to a

Network Load Balancer

Both Classic Load Balancers and Application Load Balancers use connection multiplexing, but Network Load Balancers do not. Therefore, your
targets can receive more TCP connections behind a Network Load Balancer. Be sure that your targets are
prepared to handle the volume of connection requests they might receive.

## Port allocation errors for backend flows

With PrivateLink traffic or when [client IP
preservation](edit-target-group-attributes.md#client-ip-preservation "edit-target-group-attributes.md#client-ip-preservation") is disabled, a Network Load Balancer supports 55,000 simultaneous connections or
about 55,000 connections per minute to each unique target (IP address and port). If you
exceed these limits, there is an increased chance of port allocation errors. You can
track port allocation errors using the `PortAllocationErrorCount` metric.
You can track active connections using the `ActiveFlowCount` metric.
For more information, see [CloudWatch metrics for your Network Load Balancer](load-balancer-cloudwatch-metrics.md "load-balancer-cloudwatch-metrics.md").

To fix port allocation errors, we recommend that you add targets to the target
group.

Alternatively, if you can't add targets to the target group, you can add up to 7 [secondary IP addresses](edit-load-balancer-attributes.md#secondary-ip-addresses "edit-load-balancer-attributes.md#secondary-ip-addresses") to the load balancer
network interfaces. The secondary IP addresses are automatically allocated from the IPv4
CIDR blocks of the corresponding subnets. Each secondary IP address consumes 6 network
addressing units. Note that after you add a secondary IP address you can't remove it.
The only way to release the secondary IP addresses is to delete the load balancer.

## Intermittent TCP connection establishment

failure or TCP connection establishment delays

When client IP address preservation is enabled, a client may connect to different
destination IP address using the same source ephemeral port. These destination IP
addresses can be from the same load balancer (in different Availability Zones) when
cross-zone load balancing enabled or different Network Load Balancers that uses the same target IP
address and port registered. In this case, if these connections are routed to the
same target IP address and port, the target will see a duplicated connection, since
they come from the same client IP address and port. This leads to connection errors
and delays when establishing one of these connections. This occurs frequently when
a NAT device in front of the client, and the same source IP address and source port
is allocated when connecting to multiple Network Load Balancer IP addresses simultaneously.

You can reduce this type of connection error by increasing the number of source
ephemeral ports allocated by the client or NAT device, or by increasing the number
of targets for the load balancer. We recommend clients change the source port used
when reconnecting after these connection failures. To prevent this type of connection
error, if you are using a single Network Load Balancer, you can consider disabling cross-zone load
balancing, or if using multiple Network Load Balancers, you can consider not using the same target
IP address and port registered in multiple target groups. Alternatively, you can
consider disabling client IP preservation. If you need the client IP you can use
retrieve it using Proxy Protocol v2. To learn more about Proxy Protocol v2, see
[Proxy protocol](edit-target-group-attributes.md#proxy-protocol "edit-target-group-attributes.md#proxy-protocol").

## Potential failure when the load

balancer is being provisioned

One of the reasons a Network Load Balancer could fail when it is being provisioned is if you use an IP
address that is already assigned or allocated elsewhere (for example, assigned as a
secondary IP address for an EC2 instance). This IP address prevents the load balancer
from being set up, and its state is `failed`. You can resolve this by
de-allocating the associated IP address and retrying the creation process.

## Traffic is distributed unevenly between targets

TCP and TLS listeners route TCP connections and UDP listeners route UDP streams.
The load balancer selects targets using a flow hash algorithm. A single connection
from a client is inherently sticky.

If you notice that some targets appear to receive more traffic than others, we
recommend that you review the VPC flow logs. Compare the number of unique connections
for each target IP address. Keep the time window as short as possible, as target
registration, deregistration, and unhealthy targets influence these connection numbers.

The following are possible scenarios where connections can be distributed unevenly:

- If you start with a small number of targets and then register additional targets
  later on, the original targets still have connections with clients. With an
  HTTP workload, keepalives ensure that clients reuse connections. If you lower
  the max keepalives on your web application, clients would open new connections
  more often.
- If target group stickiness is enabled, there is a small number of clients, and the
  clients communicate through a NAT device with a single source IP address, connections
  from these clients are routed to the same target.
- If cross-zone load balancing is disabled and clients prefer the load balancer
  IP address from one of the load balancer zones, connections would be distributed
  unevenly between the load balancer zones.

## DNS name resolution contains fewer IP addresses

than enabled Availability Zones

Ideally your Network Load Balancer provides one IP address per enabled Availability Zone, when
they have at least one healthy host in the Availability Zone. When there are no
healthy host in a particular Availability Zone, and cross-zone load balancing is
disabled, the IP address of the Network Load Balancer respective of that AZ will be removed from DNS.

For example, suppose your Network Load Balancer has three Availability Zones enabled, all of which
have at least one healthy registered target instance.

- If the registered target instance(s) in Availability Zone A become unhealthy,
  the corresponding IP address of Availability Zone A for the Network Load Balancer is removed
  from DNS.
- If any two of the enabled Availability Zones have no healthy registered target
  instance(s), the respective two IP addresses of the Network Load Balancer will be removed from DNS.
- If there are no healthy registered target instance(s) in all the enabled Availability
  Zones, the fail-open mode is enabled and DNS will provide all the IP addresses from the
  three enabled AZs in the result.

## IP fragmented packets are not routed to targets

Network Load Balancers do not support IP fragmented packets for non-UDP traffic.

## Troubleshoot unhealthy targets using the resource map

If your Network Load Balancer targets are failing health checks, you can use the
resource map to find unhealthy targets and take actions based
on the failure reason code. For more information, see
[View the Network Load Balancer resource map](view-resource-map.md "view-resource-map.md").

Resource map provides two views: **Overview**, and **Unhealthy
Target Map**. **Overview** is selected by default and displays
all of your load balancer's resources. Selecting the **Unhealthy Target Map**
view will display only the unhealthy targets in each target group associated to the Network Load Balancer.

###### Note

**Show resource details** must be enabled to view the health
check summary and error messages for all applicable resources within the resource map.
When not enabled, you must select each resource to view its details.

The **Target groups** column displays a summary of the healthy and
unhealthy targets for each target group. This can help determine if all the targets
are failing health checks, or only specific targets are failing. If all targets in a
target group are failing health checks, check the target group's health check settings.
Select a target group's name to open its detail page in a new tab.

The **Targets** column displays the TargetID and the current health
check status for each target. When a target is unhealthy, the health check failure
reason code is displayed. When a single target is failing a health check, verify the
target has sufficient resources. Select a target's ID to open its detail page in a new tab.

Selecting **Export** gives you the option of exporting the current
view of your Network Load Balancer's resource map as a PDF.

Verify that your instance is failing health checks and then based on the failure
reason code check for the following issues:

- **Unhealthy: Request timed out**
  - Verify the security groups and network access control lists (ACL) associated
    with your targets and Network Load Balancer are not blocking connectivity.
  - Verify the target has sufficient capacity available to accept connections
    from the Network Load Balancer.
  - The Network Load Balancer's health check responses can be viewed in each target's
    application logs. For more information, see
    [Health check reason codes](target-group-health-checks.md#target-health-reason-codes "target-group-health-checks.md#target-health-reason-codes").

- **Unhealthy: FailedHealthChecks**
  - Verify the target is listening for traffic on the health check port.

  ###### When using a TLS listener

  You choose which security policy is used for front-end connections.
  The security policy used for back-end connections is automatically selected
  based on the front-end security policy in use.

      - If your TLS listener is using a TLS 1.3 security policy for
       front-end connections, the `ELBSecurityPolicy-TLS13-1-0-2021-06`
       security policy is used for back-end connections.
      - If your TLS listener is not using a TLS 1.3 security policy for
       front-end connections, the `ELBSecurityPolicy-2016-08`
       security policy is used for back-end connections.For more information, see

  [Security policies](describe-ssl-policies.md "describe-ssl-policies.md").
  - Verify the target is providing a server certificate and key in the correct format
    specified by the security policy.
  - Verify the target supports one or more matching ciphers, and a protocol provided
    by the Network Load Balancer to establish TLS handshakes.
