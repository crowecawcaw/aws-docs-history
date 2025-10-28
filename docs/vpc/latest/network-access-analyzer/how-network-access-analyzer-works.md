# How Network Access Analyzer works

Network Access Analyzer uses automated reasoning algorithms to analyze the network paths that a packet can
take between resources in an AWS network. It then produces findings for paths that match a
customer defined Network Access Scope. Network Access Analyzer performs a static analysis of a network
configuration, meaning that no packets are transmitted in the network as part of this analysis.
Because Network Access Analyzer only considers the state of the network as described in the network configuration,
packet loss that is due to transient network interruptions or service failures is not considered
in the analysis.

Network Access Analyzer makes a best effort attempt to return a diverse, representative set of findings from
among all possible findings.

Not all AWS network configurations are supported by Network Access Analyzer. The following sections describe
the types of network paths that Network Access Analyzer produces as findings. For more information about resources
that you can reference in Network Access Scopes, see [Network Access Scopes in Network Access Analyzer](working-with-network-access-scopes.md "working-with-network-access-scopes.md").

###### Contents

- [Supported source and destination resources](#supported-configs-paths "#supported-configs-paths")
- [Supported path resources](#path-components "#path-components")
- [Unsupported resources](#unsupported-resources "#unsupported-resources")
- [Unsupported network configurations](#unsupported-configurations "#unsupported-configurations")
- [Limitations](#analyzer-limitations "#analyzer-limitations")

## Supported source and destination resources

A Network Access Analyzer finding is a network path that a packet can take in a network. Network Access Analyzer can only
produce findings for network paths that start or end at the following types of
resources:

- Internet gateways
- Network interfaces
- Transit gateway attachments
- VPC interface endpoints
- VPC gateway endpoints
- VPC gateway load balancer endpoints
- VPC service endpoints
- VPC peering connections
- Virtual private gateways

## Supported path resources

A Network Access Analyzer network path can pass through multiple resources from the start to the end of the
network path. Only the following resource types are supported as resources on network paths in
Network Access Analyzer findings:

- Internet gateways
- Load balancers
- NAT gateways
- Network ACLs
- Network firewalls
- Network interfaces
- VPC route
  tables
- Security groups
- Target groups
- Transit gateway route tables
- Transit gateway attachments
- VPC interface endpoints
- VPC gateway endpoints
- VPC gateway load balancer endpoints
- VPC endpoints services
- VPC peering connections
- Virtual private gateways

## Unsupported resources

- Network Access Analyzer does not produce network paths through resources that are associated with
  Amazon API Gateway, AWS Global Accelerator, Traffic Mirroring, AWS Wavelength, or AWS Direct Connect. Network Access Analyzer can't produce
  network paths containing customer managed Amazon EC2 instances that modify packet forwarding
  behavior.
- Network Access Analyzer doesn't support nested Resource Groups.

## Unsupported network configurations

The following network configurations are not supported by Network Access Analyzer.

###### Internet gateways and virtual private gateways

- Network Access Analyzer supports internet gateways and virtual private gateways at the beginning or end
  of a path, but does not report paths that pass through internet gateways or virtual
  private gateways. For example, Network Access Analyzer does not produce paths that start in one VPC, pass
  through the internet, and end in a second Amazon VPC after passing through an internet gateway.
  These resources are outside of AWS networking and therefore out of scope.
- Network Access Analyzer does not support NAT reflection at internet gateways. For example, Network Access Analyzer does
  not report network paths from one network interface to another network interface that are
  addressed to the second network interface's public IPV4 address.

###### Application Load Balancers

- Network Access Analyzer does not support [advanced forwarding rules](https://aws.amazon.com/blogs/aws/new-advanced-request-routing-for-aws-application-load-balancers/ "https://aws.amazon.com/blogs/aws/new-advanced-request-routing-for-aws-application-load-balancers/").

###### Gateway Load Balancers

- Packet transformations applied by Gateway Load Balancer targets are ignored. A packet
  is reflected from the targets back to the Gateway Load Balancer untouched.
- Findings through a Gateway Load Balancer must start at a Gateway Load Balancer endpoint service.

###### Gateway Load Balancer endpoints

- Paths through a Gateway Load Balancer endpoint do not include the load balancer and its targets.

###### Network interfaces

- Network Access Analyzer does not produce findings that start or terminate at network interfaces that
  belong to a NAT gateway or Network Load Balancer.

###### Network Load Balancers

- Network Access Analyzer does not support instance targets without [client IP
  preservation](../../../elasticloadbalancing/latest/network/load-balancer-target-groups.md#client-ip-preservation "../../../elasticloadbalancing/latest/network/load-balancer-target-groups.md#client-ip-preservation") enabled.

###### Network firewalls

- Network Access Analyzer does not analyze network firewall rules. Paths as reported in findings
  containing network firewalls may be spurious if the firewall on the path is configured
  with rules that would otherwise block the reported network traffic.

###### Transit gateways

- Network Access Analyzer does not support paths through AWS Transit Gateway peering
  connections to other regions or accounts, or AWS Transit Gateway direct
  connections.

## Limitations

- The analysis that Network Access Analyzer performs is limited to IPv4, using UDP or TCP.
- Network Access Analyzer does not report paths that contain resources in accounts or Regions other than
  the account or Region being analyzed. In particular, Network Access Analyzer does not produce paths
  containing resources in subnets shared from other accounts, or to resources connected by
  VPC peering connections, virtual private gateways, internet gateways, or transit gateways
  to resources in other accounts or in different Regions.
- The paths that Network Access Analyzer reports contain a bounded number of resources. Network Access Analyzer does not
  produce arbitrary length network paths through atypical network configurations, such as
  load balancers that target themselves, or NAT gateways that send packets immediately to
  another NAT gateway.
- Network Access Analyzer does not ensure that the same findings are produced if you analyze the same
  Network Access Scope in the same network. Network Access Analyzer might produce new findings for existing
  Network Access Scope analyses if new configurations are supported in the future.
- Network Access Analyzer reports only unidirectional analysis. That is, Network Access Analyzer findings only indicate that
  a packet can be sent successfully from a source to a destination.
- Network Access Analyzer does not report connectivity due to traffic mirroring.
- Network Access Analyzer does not consider the health of registered targets.
- Network Access Analyzer does not consider the advertised state of BYOIP address ranges. If a BYOIP
  address range is not advertised, resources that use these addresses might not be reachable
  from the internet.
- A running analysis times out after 4 hours.
- Your account has quotas related to Network Access Analyzer. For more information, see [Quotas and considerations for Network Access Analyzer](network-access-analyzer-limits.md "network-access-analyzer-limits.md").
