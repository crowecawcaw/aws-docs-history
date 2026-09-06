

# Access service networks through AWS PrivateLink
<a name="privatelink-access-service-networks"></a>

You can privately connect to a service network from your VPC using a service network VPC endpoint (service-network endpoint). A service-network endpoint lets you privately and securely access the resources and services that are associated to the service network. In this way, you can privately access multiple resources and services through a single VPC endpoint.

A service network is a logical collection of resource configurations and VPC Lattice services. Using a service-network endpoint, you can connect a service network to your VPC, and access those resources and services privately from your VPC or from on-premises. A service-network endpoint lets you connect to one service network. To connect to multiple service networks from your VPC, you can create multiple service-network endpoints, each pointing to a different service network.

Service networks are integrated with AWS Resource Access Manager (AWS RAM). You can share your service network with another account through AWS RAM. When you share a service network with another AWS account, that account can create a service-network endpoint to connect to the service network. You can share a service network using a [resource share](https://docs.aws.amazon.com/ram/latest/userguide/working-with-sharing.html) in AWS RAM.

Use the AWS RAM console, to view the resource shares to which you have been added, the shared service networks that you can access, and the AWS accounts that have shared the resources with you. For more information, see [Resources shared with you ](https://docs.aws.amazon.com/ram/latest/userguide/working-with-shared.html) in the *AWS RAM User Guide*.

**Pricing**  
You are billed hourly for the resource configurations that are associated with your service network. You are also billed per GB of data processed when you access resources through the service network VPC endpoint. You are not billed hourly for the service-network VPC endpoint itself. For more information, see [Amazon VPC Lattice pricing](https://aws.amazon.com/vpc/lattice/pricing/).

**Topics**
+ [Overview](#sn-network-overview)
+ [DNS hostnames](#sn-endpoint-dns)
+ [DNS resolution](#sn-endpoint-dns-resolution)
+ [Private DNS](#sn-endpoint-private-dns)
+ [Subnets and Availability Zones](#sn-endpoint-subnets-zones)
+ [IP address types](#sn-endpoint-ip-address-type)
+ [Create a service-network endpoint](access-with-service-network-endpoint.md)
+ [Manage service-network endpoints](manage-sn-endpoint.md)

## Overview
<a name="sn-network-overview"></a>

You can either create your own service network, or a service network can be shared with you from another account. Either way, you can create a service-network endpoint to connect to it from your VPC. For more information on how to create service network and associate resource configurations to it, see the [Amazon VPC Lattice User Guide](https://docs.aws.amazon.com/vpc-lattice/latest/ug/).

The following diagram shows how a service-network endpoint in your VPC accesses a service network.

![A service-network endpoint connects to a service network.](http://docs.aws.amazon.com/vpc/latest/privatelink/images/service-network-endpoint.png)


Network connections can only be initiated from the VPC that has the service-network endpoint to the resources and services in the service network. The VPC with the resources and services can't initiate network connections into the endpoint VPC.

## DNS hostnames
<a name="sn-endpoint-dns"></a>

With AWS PrivateLink, you send traffic to service networks using private endpoints. When you create a service-network VPC endpoint, we create Regional DNS names (called default DNS name) for each resource and service that you can use to communicate with the resource and service from your VPC and from on premises. IP addresses associated with the endpoint can change. We recommend that you use DNS instead of endpoint IPs to connect to your service networks.

The default DNS name for a resource in the service network has the following syntax:

```
{{endpointId}}-{{snraId}}.{{rcfgId}}.{{randomHash}}.vpc-lattice-rsc.{{region}}.on.aws
```

The default DNS name for a Lattice service in the service-network has the following syntax:

```
{{endpointId}}-{{snsaId}}.{{randomHash}}.vpc-lattice-svcs.{{region}}.on.aws
```

If you're using the AWS Management Console, you can find the DNS name under the **Associations** tab. If you're using the AWS CLI, use the [describe-vpc-endpoint-associations](https://docs.aws.amazon.com/cli/latest/reference/ec2/describe-vpc-endpoint-associations.html) command. 

You can only enable [private DNS](privatelink-access-aws-services.md#interface-endpoint-private-dns) when your service network has an ARN-type resource configuration to an Amazon RDS database service. With private DNS, you can continue to make requests to the resource using the DNS name provisioned for the resource by the AWS service, while leveraging private connectivity through the service-network VPC endpoint. For more information, see [DNS resolution](privatelink-access-resources.md#resource-endpoint-dns-resolution).

## DNS resolution
<a name="sn-endpoint-dns-resolution"></a>

When you create a service network endpoint, we create DNS names for each resource configuration and Lattice service that is associated to the service network. These DNS records are public. Therefore, these DNS names are publicly resolvable. However, DNS requests from outside the VPC still return the private IP addresses of the service network endpoint’s network interfaces. You can use these DNS names to access the resource and services from on premises, as long as you have access to the VPC that the service network endpoint is in, through VPN or Direct Connect.

## Private DNS
<a name="sn-endpoint-private-dns"></a>

If you enable private DNS for your service-network VPC endpoint, and your VPC has both [DNS hostnames and DNS resolution](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-dns.html#vpc-dns-updating) enabled, we create hidden, AWS-managed private hosted zones for the resource configurations that have custom DNS names. The hosted zone contains a record set for the default DNS name for the resource that resolves it to the private IP addresses of the service-network endpoint's network interfaces in your VPC.

Amazon provides a DNS server for your VPC, called the [Route 53 Resolver](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resolver.html). The Route 53 Resolver automatically resolves local VPC domain names and record in private hosted zones. However, you can't use the Route 53 Resolver from outside your VPC. If you'd like to access your VPC endpoint from your on-premises network, you can use the default DNS names or you can use Route 53 Resolver endpoints and Resolver rules. For more information, see [Integrating AWS Transit Gateway with AWS PrivateLink and Amazon Route 53 Resolver](https://aws.amazon.com/blogs/networking-and-content-delivery/integrating-aws-transit-gateway-with-aws-privatelink-and-amazon-route-53-resolver/).

## Subnets and Availability Zones
<a name="sn-endpoint-subnets-zones"></a>

You can configure your service-network endpoint with one subnet per Availability Zone. We create an elastic network interface for the VPC endpoint in each subnet that you specify. We assign IP addresses to each elastic network interface from its subnet as follows:
+ **VPC Lattice services (Layer 7)** – We assign a /28 block (16 contiguous IPv4 addresses) per Availability Zone for all VPC Lattice services associated with the service network. This /28 block is allocated when the service-network endpoint is created, even if there are no services currently in the service network. The /28 block must consist of 16 contiguous, unoccupied IPv4 addresses and it cannot overlap with the five AWS-reserved addresses (first four and last IP). Ensure that sufficient free contiguous address space is available. For IPv6, we also assign a /80 block per Availability Zone for VPC Lattice services.
+ **VPC Lattice resources (Layer 4/TCP)** – We assign one IPv4 address per resource configuration per Availability Zone. Contiguous address space is not required for VPC Lattice resources. We allocate up to 63 IP addresses per elastic network interface. When additional resource configurations exceed this limit, we create another elastic network interface in the same subnet. For IPv6, we assign a /80 block on the first elastic network interface created for resources; no additional elastic network interfaces are created when using IPv6. When you remove a resource configuration from the service network, we release its associated IP address. When all IPv4 addresses on an elastic network interface are released, we remove the elastic network interface.

In a production environment, for high availability and resiliency, we recommend that you configure at least two Availability Zones for each service-network endpoint and ensure that each subnet has sufficient available IPv4 addresses.

## IP address types
<a name="sn-endpoint-ip-address-type"></a>

Service-network endpoints can support IPv4, IPv6, or dual-stack addresses. Endpoints that support IPv6 can respond to DNS queries with AAAA records. The IP address type of a service-network endpoint must be compatible with the subnets for the resource endpoint, as described here:
+ **IPv4** – Assign IPv4 addresses to your endpoint network interfaces. This option is supported only if all selected subnets have IPv4 address ranges.
+ **IPv6** – Assign IPv6 addresses to your endpoint network interfaces. This option is supported only if all selected subnets are IPv6 only subnets.
+ **Dualstack** – Assign both IPv4 and IPv6 addresses to your endpoint network interfaces. This option is supported only if all selected subnets have both IPv4 and IPv6 address ranges.

If a service-network VPC endpoint supports IPv4, the endpoint network interfaces have IPv4 addresses. If a service-network VPC endpoint supports IPv6, the endpoint network interfaces have IPv6 addresses. The IPv6 address for an endpoint network interface is unreachable from the internet. If you describe an endpoint network interface with an IPv6 address, notice that `denyAllIgwTraffic` is enabled.