# How AWS Global Accelerator works

The static IP addresses provided by AWS Global Accelerator serve as single fixed entry points for your clients. When
you set up your accelerator with Global Accelerator, you associate the static IP addresses to regional
endpoints in one or more AWS Regions. For standard accelerators, the endpoints are Network Load Balancers, Application Load Balancers, Amazon EC2
instances, or Elastic IP addresses. For custom routing accelerators, endpoints are Amazon VPC (VPC)
subnets with one or more EC2 instances. The static IP addresses accept incoming traffic onto the AWS global
network from the edge location that is closest to your users.

###### Note

If you bring your own IP address range to AWS (BYOIP) to use with Global Accelerator, you can instead
assign static IP addresses from your own pool to use with your accelerator. For more information,
see [Bring your own IP addresses (BYOIP) in Global Accelerator](using-byoip.md "using-byoip.md").

From the edge location, traffic for your application is routed based on the type of accelerator that
you configure.

- For standard accelerators, traffic is routed to the optimal AWS endpoint based
  on several factors, including the user’s location, the health of the endpoint, and the endpoint
  weights that you configure.
- For custom routing accelerators, each client is routed to a specific Amazon EC2 instance and port in a VPC subnet,
  based on the external static IP address and listener port that you provide.
  Be aware of the following when you use Global Accelerator:

- **Overriding endpoint weights:** In specific, limited scenarios,
  Global Accelerator overrides the endpoint weights that you set, to help ensure availability. When
  Global Accelerator is load balancing traffic across endpoints in an endpoint
  group, it must, in certain circumstances, choose between preserving availability for client traffic and
  abiding by endpoint weights. For example, with accelerators where the client IP address is preserved, Global Accelerator
  might need to override an endpoint weight setting to help avoid connection collisions.
- **Security groups and rules:** When you add
  an accelerator, security groups and AWS WAF rules that you have already configured
  continue to work as they did before you added the accelerator.
- **IP fragmentation:** IP packets that are too large to fit into a
  standard Ethernet frame (1500+ bytes) when transmitted across the internet or
  other large networks are fragmented by intermediate routers and sent
  individually. The TCP protocol does not require IP fragmentation because clients
  and endpoints automatically negotiate a smaller Maximum Segment Size (MSS).
  However, the UDP protocol requires IP fragmentation. When packets are
  fragmented, Global Accelerator forwards UDP fragments to the configured endpoint, which
  reassembles the original IP packet. Global Accelerator drops TCP fragments at the edge,
  because they are not supported by the AWS network.

###### Topics

- [Overview of how it works](#how-it-works-summary "#how-it-works-summary")
- [Types of accelerators](#introduction-accelerator-types "#introduction-accelerator-types")
- [Idle timeout](#about-idle-timeout "#about-idle-timeout")
- [Global static IP addresses](#about-static-ip-addresses "#about-static-ip-addresses")
- [Health checks](#about-endpoint-groups-automatic-health-checks "#about-endpoint-groups-automatic-health-checks")
- [Traffic dials and endpoint weights](#introduction-traffic-dials-weights "#introduction-traffic-dials-weights")
- [ICMP response messages](#introduction-about-icmp-messages "#introduction-about-icmp-messages")

## Overview of how AWS Global Accelerator works

Traffic travels over the well-monitored, congestion-free, redundant AWS
global network to the endpoint. By maximizing the time that traffic is on the AWS network, Global Accelerator
ensures that traffic is always routed over the optimum network path. Global Accelerator terminates TCP connections from clients at
AWS edge locations and, almost concurrently, establishes a new TCP connection with your endpoints.
This gives clients faster response times (lower latency) and increased throughput.

Global Accelerator always preserves client IP addresses for endpoints on custom routing accelerators. With standard accelerators, you
have the option to preserve and access the client IP address for some endpoint types. For detailed information
about the endpoint types and configurations that Global Accelerator supports, including client IP address preservation
support, see [Requirements for resources you add as accelerator endpoints](about-endpoints-caveats.md "about-endpoints-caveats.md").

With standard accelerators, Global Accelerator continuously monitors the health of all endpoints, and instantly begins directing
traffic for all new connections to another available endpoint when it determines that an active endpoint is unhealthy.
This allows you to create a high-availability architecture for your applications on AWS. Health checks aren't
used with custom routing accelerators and there is no failover, because you specify the destination to route traffic to.

If you want fine-grained control over your global traffic, you can configure _weights_ for
your endpoints in a standard accelerator. In addition, you can use the _traffic dial_
in Global Accelerator to increase (dial up) or decrease (dial down) the percentage
of traffic to a specific endpoint group, for example, for performance testing or stack upgrades.

##

Types of accelerators

There are two types of accelerators that you can use with AWS Global Accelerator: _standard accelerators_
and _custom routing accelerators_. Both types of accelerators route traffic over the AWS global
network to improve performance and stability, but they're each designed for different application needs.

**Standard accelerator**
By using a standard accelerator, you can improve the availability and performance of your
applications running on Application Load Balancers, Network Load Balancers, or Amazon EC2 instances. With a standard
accelerator, Global Accelerator routes client traffic across regional endpoints based on
geo-proximity and endpoint health. It also allows customers to shift client
traffic across endpoints based on controls such as traffic dials and
endpoint weights. This works for a wide variety of use cases, including
blue/green deployment, A/B testing, and multi-Region deployment. To see
more use cases, see [Understanding AWS Global Accelerator use cases](introduction-benefits-of-migrating.md "introduction-benefits-of-migrating.md").

To learn more, see [Working with standard accelerators in AWS Global Accelerator](work-with-standard-accelerators.md "work-with-standard-accelerators.md").

**Custom routing accelerator**
Custom routing accelerators work well for scenarios where you want to use custom application
logic to direct one or more users to a specific destination and port
among many, while still gaining the performance benefits of Global Accelerator. One
example is VoIP applications that assign multiple callers to a specific
media server to start voice, video, and messaging sessions. Another example
is online real-time gaming applications where you want to assign multiple
players to a single session on a game server based on factors such as geographic
location, player skill, and game mode.

###### Note

Custom routing accelerators support only the IPv4 IP address type.

To learn more, see [Working with custom routing accelerators in AWS Global Accelerator](work-with-custom-routing-accelerators.md "work-with-custom-routing-accelerators.md").

Based on your specific needs, you create one of these types of accelerators to accelerate
your customer traffic.

## Understanding idle timeout in AWS Global Accelerator

AWS Global Accelerator sets an idle timeout period that applies to its connections. If no data has been
sent or received by the time that the idle timeout period elapses, Global Accelerator closes the connection. The
idle timeout periods are not customizable.

To prevent connection timeout, Global Accelerator requires that you send a packet with a minimum
of one byte of data, in the ingress or egress direction, within the TCP connection timeout window.
You cannot use TCP keep-alive packets to maintain an open connection.

The Global Accelerator idle timeout for a network connection depends on the type of connection:

- The timeout is 340 seconds for TCP connections.
- The timeout is 30 seconds for UDP connections.

Global Accelerator continues to direct traffic for established connections to an endpoint until the
idle timeout is met, even if the endpoint is marked as unhealthy or if it is removed from
the accelerator. Global Accelerator selects a new endpoint, if needed, only when a new connection starts or
after an idle timeout.

## Using static IP addresses in AWS Global Accelerator

By default, Global Accelerator provides you with static IP addresses that are associated with your accelerator.
You use the static IP addresses that Global Accelerator assigns to your accelerator—or that you
specify from your own IP address pool, for standard accelerators—to route internet
traffic to the AWS global network close to where your users are, regardless of
their location. For standard accelerators, you associate the addresses with Network Load Balancers, Application Load Balancers, Amazon EC2
instances, or Elastic IP addresses that run in a single AWS Region or multiple Regions. For
custom routing accelerators, you direct traffic to EC2 destinations in VPC subnets in one or more Regions.
Routing traffic through the AWS global network improves availability and performance because
traffic doesn't have to take multiple hops over the public internet. Using static IP addresses also
lets you distribute incoming application traffic across multiple endpoint resources in multiple AWS Regions.

In addition, using static IP addresses makes it easier to add your application to more
Regions or to migrate applications between Regions. Using fixed IP addresses means
that users have a consistent way to connect to your application as you make changes.

If you like, you can associate your own custom domain name with the static IP addresses for your
accelerator. For more information, see [Route custom domain traffic to your
accelerator](dns-addressing-custom-domains.md "dns-addressing-custom-domains.md").

The static IP addresses are anycast from the AWS edge network.

For IPv4, Global Accelerator provides two static IPv4
addresses. For dual-stack, Global Accelerator provides a total of four addresses: two static IPv4 addresses and two
static IPv6 addresses. If you bring your own IP address range to AWS (BYOIP) to use with
Global Accelerator (IPv4 only), you can instead assign IPv4 addresses from your own pool to use with your accelerator.
For more information, see [Bring your own IP addresses (BYOIP) in Global Accelerator](using-byoip.md "using-byoip.md").

For accelerators with dual-stack, Global Accelerator allocates the IPv6 addresses from the same two /64 CIDR prefixes. This
can help simplify steps for allow-listing and setting ACL controls.

You can add IPv4-only endpoints to standard accelerators that are configured for IPv4 IP address types,
but accelerators that you configure as dual-stack require that you add only endpoints that also support dual-stack.
For information about endpoints that are supported for dual-stack accelerators, see [Requirements for resources you add as accelerator endpoints](about-endpoints-caveats.md "about-endpoints-caveats.md").

Global Accelerator provides the static IP addresses for you from the Amazon pool of IP addresses, unless
you bring your own IP address range to AWS, and then specify the static IP addresses from that pool.
(For more information, see [Bring your own IP addresses (BYOIP) in Global Accelerator](using-byoip.md "using-byoip.md").)
To create an accelerator on the console, the first step is to prompt Global Accelerator to provision the static IP addresses
by entering a name for your accelerator or choose your own static IP addresses. To see the steps for creating an
accelerator, see [Getting started with AWS Global Accelerator](getting-started.md "getting-started.md").

The static IP addresses remain assigned to your accelerator for as long as it exists, even if
you disable the accelerator and it no longer accepts or routes traffic. However, when
you _delete_ an accelerator, you lose the static IP addresses that
are assigned to it, so you can no longer route traffic by using them. You can use
IAM policies like tag-based permissions with Global Accelerator to limit the users who have
permissions to delete an accelerator. For more information, see [ABAC with Global Accelerator](security_iam_service-with-iam.md#security_iam_service-with-iam-tags "security_iam_service-with-iam.md#security_iam_service-with-iam-tags").

## How Global Accelerator uses health checks

For standard accelerators, AWS Global Accelerator automatically checks the health of the endpoints that are associated
with your static IP addresses, and then directs user traffic only to healthy endpoints.

Global Accelerator includes default health checks that are run automatically, but you can configure the
timing for the checks and other options. If you've configured custom health check
settings, Global Accelerator uses those settings in specific ways, depending on your configuration. You configure
those settings in Global Accelerator for Amazon EC2 instance or Elastic IP address endpoints or by
configuring settings on the ELB console for Network Load Balancers or Application Load Balancers. For more
information, see [Ensure health check access for your accelerator](about-endpoint-groups-health-check-options.md "about-endpoint-groups-health-check-options.md").

When you add an endpoint to a standard accelerator, it must pass a health check to be considered healthy
before traffic is directed to it. If Global Accelerator doesn’t have any healthy endpoints to route traffic to in a
standard accelerator, it routes requests to all endpoints.

##

How you can manage traffic flow with traffic dials and endpoint weights

There are two ways that you can customize how AWS Global Accelerator sends traffic to your endpoints with
a standard accelerator:

- Change the traffic dial to limit the traffic for one or more endpoint groups
- Specify weights to change the proportion of traffic to the endpoints in a group

**How traffic dials work**
For each endpoint group in a standard accelerator, you can set a traffic dial to control the percentage
of traffic that is sent to the endpoint group. The percentage is applied
only to traffic that is already directed to the endpoint group, not to
all listener traffic.

The traffic dial limits the portion of traffic that an endpoint group accepts,
expressed as a percentage of traffic directed to that endpoint group.
For example, if you set the traffic dial for an endpoint group in
`us-east-1` to 50 (that is, 50%) and the accelerator directs
100 user requests to that endpoint group, only 50 requests are accepted
by the group. The accelerator directs the remaining 50 requests to endpoint
groups in other Regions.

For more information, see [Use traffic dials to adjust traffic flow to Regions](about-endpoint-groups-traffic-dial.md "about-endpoint-groups-traffic-dial.md").

**How weights work**
For each endpoint in a standard accelerator, you can specify weights, which are numbers
that change the proportion of traffic that the accelerator routes to each endpoint. This can be useful,
for example, to do performance testing within a Region.

A weight is a value that determines the proportion of traffic that the accelerator directs
to an endpoint. By default, the weight for an endpoint is 128—that is,
half of the maximum value for a weight, 255.

The accelerator calculates the sum of the weights for the endpoints in an endpoint group,
and then directs traffic to the endpoints based on the ratio of each
endpoint's weight to the total. For an example of how weights work, see
[How endpoint weights work to manage traffic volume](about-endpoints-endpoint-weights.md "about-endpoints-endpoint-weights.md").

Traffic dials and weights affect how the standard accelerator serves traffic in different ways:

- You configure traffic dials for _endpoint groups_. The traffic dial lets
  you cut off a percentage of traffic—or all traffic—to the
  group, by "dialing down" traffic that the accelerator has already directed to
  it based on other factors, such as proximity.
- You use weights, on the other hand, to set values for _individual
  endpoints_ within an endpoint group. Weights provide a way to
  divide up traffic within the endpoint group. For example, you can use
  weights to do performance testing for specific endpoints in a Region.

For more information about how traffic dials and weights affect failover, see
[How failover works for unhealthy endpoints](about-endpoints-endpoint-weights.md "about-endpoints-endpoint-weights.md").

##

ICMP response messages and AWS Global Accelerator

ICMP response messages, such as `ICMP Packet Too Big` or `Fragmentation Needed`,
help to ensure availability on the internet. AWS Global Accelerator responds to ICMP echo messages (pings)
at the edge for all global IP addresses. These pings are not forwarded to customers'
endpoints. To accurately test performance with Global Accelerator, use a deeper protocol for your tests.

Here's a brief summary of how ICMP helps to ensure internet availability. The maximum transmission unit
(MTU) of a network connection is the size, in bytes, of the largest permissible packet that can be passed
over the connection. The larger the MTU of a connection, the more data that can be passed in a single packet.
Path MTU Discovery (PMTUD) is used to determine the _path MTU_ between two devices.
The path MTU is the maximum packet size that's supported on the path between the originating host
and the receiving host. When there is a difference in the MTU size in the network between two hosts,
packets that are bigger than the MTU get dropped, and the receiving host that dropped the packet notifies
the sender with an ICMP message. For more information, see [Path MTU Discovery](../../../AWSEC2/latest/UserGuide/network_mtu.md#path_mtu_discovery "../../../AWSEC2/latest/UserGuide/network_mtu.md#path_mtu_discovery").

You cannot block ICMP traffic at your accelerator in Global Accelerator. Blocking all ICMP traffic would also drop ICMP messages
such as `ICMPv6 Packet Too Big (PTB)` (Type 2) and `Destination Unreachable: Fragmentation Needed 
 and Don't Fragment was Set` (Type 3, Code 4). These messages are necessary for traffic to successfully
make it back to the originating host. In turn, these dropped messages would cause TCP and protocols that are
built on top of Global Accelerator to drop traffic from clients that are on networks with smaller-than-typical MTU, preventing PMTUD.

Note that for PMTUD to work, the security groups of your endpoints must also allow ICMP traffic. If
you have availability issues that are specific to certain end-user networks, confirm that your endpoint security
groups allow ICMP traffic.
