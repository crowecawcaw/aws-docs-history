# Share your services through AWS PrivateLink

You can host your own AWS PrivateLink powered service, known as an _endpoint
service_, and share it with other AWS customers.

###### Contents

- [Overview](#endpoint-service-overview "#endpoint-service-overview")
- [DNS hostnames](#endpoint-service-dns-hostnames "#endpoint-service-dns-hostnames")
- [Private DNS](#endpoint-service-private-dns "#endpoint-service-private-dns")
- [Subnets and Availability Zones](#endpoint-service-subnets-zones "#endpoint-service-subnets-zones")
- [Cross-Region access](#endpoint-service-cross-region "#endpoint-service-cross-region")
- [IP address types](#endpoint-service-ip-address-type "#endpoint-service-ip-address-type")
- [Create an endpoint service](create-endpoint-service.md "create-endpoint-service.md")
- [Configure an endpoint service](configure-endpoint-service.md "configure-endpoint-service.md")
- [Manage DNS names](manage-dns-names.md "manage-dns-names.md")
- [Receive alerts for endpoint service events](create-notification-endpoint-service.md "create-notification-endpoint-service.md")
- [Delete an endpoint service](delete-endpoint-service.md "delete-endpoint-service.md")

## Overview

The following diagram shows how you share your service that's hosted in AWS with other
AWS customers, and how those customers connect to your service. As the service provider, you
create a Network Load Balancer in your VPC as the service front end. You then select this load balancer when
you create the VPC endpoint service configuration. You grant permission to specific AWS
principals so that they can connect to your service. As a service consumer, the customer
creates an interface VPC endpoint, which establishes connections between the subnets that
they select from their VPC and your endpoint service. The load balancer receives requests
from the service consumer and routes them to the targets hosting your service.

![Service consumers connect to endpoint services hosted by service providers.](images/endpoint-services.png)

For low latency and high availability, we recommend that you make your service available
in at least two Availability Zones.

## DNS hostnames

When a service provider creates a VPC endpoint service, AWS generates an endpoint-specific
DNS hostname for the service. These names have the following syntax:

```
`endpoint_service_id`.`region`.vpce.amazonaws.com
```

The following is an example of a DNS hostname for a VPC endpoint service in the
us-east-2 Region:

```
vpce-svc-071afff70666e61e0.us-east-2.vpce.amazonaws.com
```

When a service consumer creates an interface VPC endpoint, we create Regional and zonal
DNS names that the service consumer can use to communicate with the endpoint service. Regional
names have the following syntax:

```
`endpoint_id`.`endpoint_service_id`.`service_region`.vpce.amazonaws.com
```

Zonal names have the following syntax:

```
`endpoint_id`-`endpoint_zone`.`endpoint_service_id`.`service_region`.vpce.amazonaws.com
```

## Private DNS

A service provider can also associate a private DNS name for their endpoint service, so
that service consumers can continue to access the service using its existing DNS name. If a
service provider associates a private DNS name with their endpoint service, then service
consumers can enable private DNS names for their interface endpoints. If a service provider
doesn't enable private DNS, then service consumers might need to update their applications to
use the public DNS name of the VPC endpoint service. For more information, see [Manage DNS names](manage-dns-names.md "manage-dns-names.md").

## Subnets and Availability Zones

Your endpoint service is available in the Availability Zones that you enable for your
Network Load Balancer. For high availability and resiliency, we recommend that you enable your load balancer
in at least two Availability Zones, deploy EC2 instances in each enabled zone, and register
these instances with your load balancer target group.

You can enable cross-zone load balancing as an alternative to hosting your endpoint
service in multiple Availability Zones. However, consumers will lose access to the
endpoint service from both zones if the zone that hosts the endpoint service fails.
Also consider that when you enable cross-zone load balancing for a Network Load Balancer, EC2 data
transfer charges apply.

The consumer can create interface VPC endpoints in the Availability Zones in which
your endpoint service is available. We create an endpoint network interface in each
subnet that the consumer configures for the VPC endpoint. We assign IP addresses to
each endpoint network interface from its subnet, based on the IP address type of the
VPC endpoint. When a request uses the regional endpoint for the VPC endpoint service,
we select a healthy endpoint network interface, using the round robin algorithm to
alternate between the network interfaces in different Availability Zones. We then resolve
the traffic to the IP address of the selected endpoint network interface.

The consumer can use the zonal endpoints for the VPC endpoint if it's better for their
use case to keep traffic in the same Availability Zone.

## Cross-Region access

A service provider can host a service in one Region and make it available in a set of
supported Regions. A service consumer selects a service Region when creating an
endpoint.

###### Permissions

- By default, IAM entities don't have permission to make an endpoint service available
  in multiple Regions or access an endpoint service across Regions. To grant the permissions
  required for cross-Region access, an IAM administrator can create IAM policies that allow
  the `vpce:AllowMultiRegion` permission-only action.
- To control the Regions that an IAM entity can specify as a supported Region when
  creating an endpoint service, use the `ec2:VpceSupportedRegion` condition key.
- To control the Regions that an IAM entity can specify as a service Region when creating
  a VPC endpoint, use the `ec2:VpceServiceRegion` condition key.

###### Considerations

- A service provider must opt in to an opt-in Region before adding it as a supported
  Region for an endpoint service.
- Your endpoint service must be accessible from its host Region. You can't remove the
  host Region from the set of supported Regions. For redundancy, you can deploy your
  endpoint service in multiple Regions and enable cross-Region access for each endpoint
  service.
- A service consumer must opt in to an opt-in Region before selecting it as the service
  Region for an endpoint. Whenever possible, we recommend that service consumers access a
  service using intra-Region connectivity instead of cross-Region connectivity.
  Intra-Region connectivity provides lower latency and lower costs.
- If a service provider removes a Region from the set of supported Regions, service
  consumers can't select that Region as the service Region when they create new endpoints.
  Note that this does not affect access to the endpoint service from existing endpoints
  that use this Region as the service Region.
- For high availability, providers must use at least two Availability Zones.
  Cross-Region access does not require that providers and consumers use the same
  Availability Zones.
- Cross-Region access is not supported for the following Availability Zones:
  `use1-az3`, `usw1-az2`, `apne1-az3`,
  `apne2-az2`, and `apne2-az4`.
- With cross-Region access, AWS PrivateLink manages failover between Availability Zones.
  It does not manage failover across Regions.
- Cross-Region access is not supported for Network Load Balancers with a custom value configured for the
  TCP idle timeout.
- Cross-Region access is not supported with UDP fragmentation.
- Cross-Region access is only supported for services that you share through AWS PrivateLink.

## IP address types

Service providers can make their service endpoints available to service consumers over
IPv4, IPv6, or both IPv4 and IPv6, even if their backend servers support only IPv4. If you
enable dualstack support, existing consumers can continue to use IPv4 to access your service
and new consumers can choose to use IPv6 to access your service.

If an interface VPC endpoint supports IPv4, the endpoint network interfaces have IPv4
addresses. If an interface VPC endpoint supports IPv6, the endpoint network interfaces have
IPv6 addresses. The IPv6 address for an endpoint network interface is unreachable from the
internet. If you describe an endpoint network interface with an IPv6 address, notice that
`denyAllIgwTraffic` is enabled.

###### Requirements to enable IPv6 for an endpoint service

- The VPC and subnets for the endpoint service must have associated IPv6 CIDR
  blocks.
- All Network Load Balancers for the endpoint service must use the dualstack IP address type. The
  targets do not need to support IPv6 traffic. If the service processes source IP
  addresses from the proxy protocol version 2 header, it must process IPv6 addresses.

###### Requirements to enable IPv6 for an interface endpoint

- The endpoint service must support IPv6 requests.
- The IP address type of an interface endpoint must be compatible with the subnets for
  the interface endpoint, as described here:
  - **IPv4** – Assign IPv4 addresses to your endpoint
    network interfaces. This option is supported only if all selected subnets have
    IPv4 address ranges.
  - **IPv6** – Assign IPv6 addresses to your endpoint
    network interfaces. This option is supported only if all selected subnets are IPv6
    only subnets.
  - **Dualstack** – Assign both IPv4 and IPv6 addresses to
    your endpoint network interfaces. This option is supported only if all selected
    subnets have both IPv4 and IPv6 address ranges.

###### DNS record IP address type for an interface endpoint

The DNS record IP address type that an interface endpoint supports determines the DNS records
that we create. The DNS record IP address type of an interface endpoint must be compatible with
the IP address type of the interface endpoint, as described here:

- **IPv4** – Create A records for the private, Regional,
  and zonal DNS names. The IP address type must be **IPv4** or
  **Dualstack**.
- **IPv6** – Create AAAA records for the private, Regional,
  and zonal DNS names. The IP address type must be **IPv6** or
  **Dualstack**.
- **Dualstack** – Create A and AAAA records for the private,
  Regional, and zonal DNS names. The IP address type must be **Dualstack**.
