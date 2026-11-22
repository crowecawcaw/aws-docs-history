

# Private endpoint health checks

A private endpoint health check monitors an endpoint that is reachable from your VPC, such as a specific IP address, domain name, or port. Amazon Route 53 checks the endpoint from a health check source that you create in your VPC. You don't need to expose any endpoint to the internet.

When an endpoint becomes unhealthy, the private endpoint health check marks any associated DNS records as unhealthy. Route 53 can then redirect traffic to healthy endpoints. This extends Route 53 health checks and DNS failover from public endpoints to your private resources.

Private endpoint health checks are fully managed. You set them up through the Route 53 console, the AWS CLI, or CloudFormation, the same way that you set up public endpoint health checks.

## How private endpoint health checks work
<a name="health-checks-private-endpoints-how-it-works"></a>

Private endpoint health checks work in three stages.

1. **Create a health check source** – A health check source is the location inside your VPC that health-check traffic comes from. You set up a health check source one time and use it for up to 200 private endpoint health checks. Each health check source has an IP address in each of three subnets, in three Availability Zones in the same Region as the VPC. For more information, see [Health check sources](health-check-sources.md).

1. **Create a health check that uses the source** – You create a private endpoint health check that uses the health check source. The health check monitors a specific private IP address, domain name, or port over HTTP, HTTPS, or TCP. You can also turn on string matching and 10-second fast checks.

1. **Associate the health check with your DNS records** – You can use any routing policy. When the endpoint becomes unhealthy, the health check marks the associated records as unhealthy, so that Route 53 routes traffic to healthy endpoints.

Note the following about private endpoint health checks:
+ A private endpoint health check runs only from the AWS Region of its health check source.
+ A private endpoint health check uses a single health check source.
+ A private endpoint health check and its health check source must be in the same AWS account.
+ You can't reference a private endpoint health check from a calculated health check.

## Availability at launch
<a name="health-checks-private-endpoints-scope"></a>

At launch, private endpoint health checks support the following:


**Private endpoint health check support at launch**  

| Supported at launch | Not supported at launch | 
| --- | --- | 
|  +  Private VPC endpoints. <br />+  On-premises and hybrid endpoints that are reachable from the health check source VPC.   |  +  Calculated health checks that reference private endpoint health checks. <br />+  A combination of private and public health checks.   | 

## Setup considerations
<a name="health-checks-private-endpoints-considerations"></a>

Review the following considerations before you set up private endpoint health checks:
+ **Network access** — Security groups and network ACLs must allow traffic from the health check source to your target endpoints.
+ **Availability Zones** — A health check source covers three Availability Zones. If your VPC spans more than three Availability Zones, you can create additional health check sources to cover target endpoints in the other Availability Zones.
+ **Account scope** — You can associate a private endpoint health check only with DNS records in the same AWS account. Cross-account association isn't supported.
+ **FQDN endpoints** — Route 53 resolves names only through the Amazon VPC's Route 53 Resolver, not custom DNS servers in your DHCP options set. The Amazon VPC must have DNS resolution enabled and a primary IPv4 CIDR block in a private IP address range.

  For names that only your DNS servers resolve, you have three options. You can associate the private hosted zone with the Amazon VPC, add a Resolver forwarding rule, or use an IP address health check.

## Regional considerations
<a name="health-checks-private-endpoints-regional"></a>

A private endpoint health check is a Regional resource. Route 53 performs the health check from the AWS Region of its health check source. The health check's status, CloudWatch metrics, and alarms are in that Region.

A private endpoint health check runs within a single Region. A service event in that Region can affect your ability to health-check your endpoints from that Region.

As a best practice, create health check sources in more than one Region. This reduces the risk that a single Region's outage affects your health checks. Alternatively, use a health check source whose Amazon VPC has connectivity to another Region (for example, through Amazon VPC peering or Transit Gateway). Either approach lets Route 53 continue to health-check your endpoints if one Region is unavailable.