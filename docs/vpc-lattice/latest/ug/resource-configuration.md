

# Resource configurations for VPC resources

A resource configuration represents an individual resource, a group of resources, or a list of Classless Inter-Domain Routing (CIDR) ranges that you want to make accessible to clients in other VPCs and accounts. By defining a resource configuration, you can allow private, secure, unidirectional network connectivity to resources in your VPC from clients in other VPCs and accounts. A resource configuration is associated with a resource gateway through which it receives traffic. For a resource to be accessed from another VPC, it needs to have a resource configuration.

**Topics**
+ [Types of resource configurations](#resource-configuration-types)
+ [Protocol](#resource-configuration-protocol)
+ [Resource gateway](#resource-gateway)
+ [Custom domain names for resource providers](#custom-domain-name-resource-providers)
+ [Custom domain names for resource consumers](#custom-domain-name-resource-consumers)
+ [Custom domain names for service network owners](#resource-configuration-custom-domain-name-service-network-owners)
+ [Resource definition](#resource-definition)
+ [Port ranges](#resource-configuration-port)
+ [Accessing resources](#resource-configuration-accessing)
+ [Association with service network type](#resource-configuration-service-network-association)
+ [Types of service networks](#service-network-types)
+ [Sharing resource configurations through AWS RAM](#sharing-resource-configuration-ram)
+ [Monitoring](#resource-configuration-monitoring)
+ [Create and verify a domain](create-and-verify.md)
+ [Create a resource configuration](create-resource-configuration.md)
+ [Manage associations](resource-configuration-associations.md)

## Types of resource configurations
<a name="resource-configuration-types"></a>

A resource configuration can be of several types. The different types help represent different kinds of resources. The types are:

Single resource configuration  
Represents an IP address or a domain name. It can be shared independently.

Group resource configuration  
It is a collection of child resource configurations. It can be used to represent a group of DNS and IP address endpoints.

Child resource configuration  
It is a member of a group resource configuration. It represents an IP address or a domain name. It can't be shared independently; it can only be shared as part of a group. It can be added and removed from a group. When added, it's automatically accessible to those who can access the group.

ARN resource configuration  
Represents a supported resource-type that is provisioned by an AWS service. Any group-child relationship is automatically taken care of. It can be shared independently.

CIDR resource configuration  
A list of CIDR ranges. It can be shared independently.

The following image shows a single, child, and group resource configuration:

![Single, child, and group resource configurations.](https://docs.aws.amazon.com/vpc-lattice/latest/ug/images/resource-config-types.png)


## Protocol
<a name="resource-configuration-protocol"></a>

When you create a resource configuration you can define the protocol that the resource will support. The default protocol is TCP.

For CIDR resource configurations, specify `TCP_UDP` so that you can send DNS queries over UDP. All other traffic must use TCP. Other resource configuration types support only TCP.

**Note**  
The `TCP_UDP` protocol applies only to CIDR resource configurations, which you access through a tunnel endpoint. CIDR resource configurations can't be associated with a service network, so `TCP_UDP` doesn't apply to service network endpoints or to resource endpoints. Traffic through those endpoints uses TCP.

## Resource gateway
<a name="resource-gateway"></a>

A resource configuration is associated with a resource gateway. A resource gateway is a set of ENIs that serve as a point of ingress into the VPC that the resource is in. Multiple resource configurations can be associated with the same resource gateway. When clients in other VPCs or accounts access a resource in your VPC, the resource sees traffic coming locally from the resource gateway's IP addresses in that VPC.

## Custom domain names for resource providers
<a name="custom-domain-name-resource-providers"></a>

Resource providers can attach a custom domain name to a resource configuration, such as `example.com`, which resource consumers can use to access the resource configuration. The custom domain name can be owned and verified by the resource provider, or it can be a third-party or AWS domain. Resource providers can use resource configurations to share cache clusters and Kafka clusters, TLS-based applications, or other AWS resources.

The following considerations apply to providers of resource configurations:
+ A resource configuration can only have one custom domain.
+ The custom domain name of a resource configuration cannot be changed. 
+ The custom domain name is visible to all resource configuration consumers.
+ You can verify your custom domain name using the domain name verification process in VPC Lattice. For more information, see [Create and verify a domain](create-and-verify.md).
+ For resource configurations of type group and child, you must first specify a group domain on the group resource configuration. Afterward, the child resource configurations can have custom domains that are subdomains of the group domain. If the group doesn't have a group domain, you can use any custom domain name for the child, but VPC Lattice will not provision any hosted zones for the child domain names in the resource consumer's VPC. 
+ Custom domain names are not supported for CIDR resource configurations.

## Custom domain names for resource consumers
<a name="custom-domain-name-resource-consumers"></a>

When resource consumers enable connectivity to a resource configuration that has a custom domain name, they can allow VPC Lattice to manage a Route 53 private hosted zone in their VPC. Resource consumers have granular options for which domains they want to allow VPC Lattice to manage private hosted zones for.

Resource consumers can set the `private-dns-enabled` parameter when enabling connectivity to resource configurations through a resource endpoint, a service network endpoint, or a service network VPC association. Along with the `private-dns-enabled` parameter, consumers can use DNS options to specify which domains that they want VPC Lattice to manage private hosted zones for. Consumers can choose between the following private DNS preferences:

**`ALL_DOMAINS`**  
VPC Lattice provisions private hosted zones for all custom domain names. 

**`VERIFIED_DOMAINS_ONLY`**  
VPC Lattice provisions a private hosted zone only if the custom domain name has been verified by the provider.

**`VERIFIED_DOMAINS_AND_SPECIFIED_DOMAINS`**  
VPC Lattice provisions private hosted zones for all verified custom domain names and other domain names that the resource consumer specifies. The resource consumer specifies the domain names in the `private DNS specified domains` parameter.

**`SPECIFIED_DOMAINS_ONLY`**  
VPC Lattice provisions a private hosted zone for domain names specified by the resource consumer. The resource consumer specifies the domain names in the `private DNS specified domains ` parameter.

When you enable private DNS, VPC Lattice creates a private hosted zone in your VPC for the custom domain name associated with the resource configuration. By default, the private DNS preference is set to `VERIFIED_DOMAINS_ONLY`. This means that private hosted zones are created only if the custom domain name has been verified by the resource provider. If you set your private DNS preference to `ALL_DOMAINS` or `SPECIFIED_DOMAINS_ONLY` then VPC Lattice creates private hosted zones regardless of the verification status of the custom domain name. When a private hosted zone is created for a given domain, all traffic to that domain from your VPC is routed through VPC Lattice. We recommend that you use the `ALL_DOMAINS`, `VERIFIED_DOMAINS_AND_SPECIFIED_DOMAINS`, or `SPECIFIED_DOMAINS_ONLY` preferences only when you want traffic to these custom domain names to go through VPC Lattice.

We recommend that resource consumers set their private DNS preference to `VERIFIED_DOMAINS_ONLY`. This lets consumers tighten their security perimeter by only allowing VPC Lattice to provision private hosted zones for verified domains in the resource consumer's account.

To select domains in the private DNS specified domains, resource consumers can enter a fully qualified domain name, such as `my.example.com` or use a wildcard such as `*.example.com`.

The following considerations apply to consumers of resource configurations:
+ You can enable or disable private DNS after you create the endpoint or VPC association. The change applies only to resource configurations connected afterward. Before you enable private DNS, turn on the `enableDnsHostnames` and `enableDnsSupport` attributes for your VPC. VPC Lattice doesn't check these attributes when you update the endpoint or VPC association, so the update succeeds, but names don't resolve until both attributes are on. For more information, see [Update private DNS settings](#update-private-dns-settings).
+ Private DNS should be enabled on a service network resource association for private hosted zones to be created in a VPC. For a resource configuration, the private DNS enabled status of the service network resource association overrides the private DNS enabled status of either the service network endpoint or service network VPC association.

For resource configurations that are domain-name targets, a private hosted zone entry is not created if the following are true:
+ Resource gateway is in the same VPC as the service network VPC endpoint/service network VPC association.
+ DNS resolution is set to IN\_VPC on the resource gateway.
+ The custom domain name or group domain is the same or higher-level domain of the domain-name target.

For resource configurations of type ARN, VPC Lattice does not create a private hosted zone entry if the following is true:
+ The resource gateway is in the same VPC as the service network VPC endpoint or service network VPC association.

### Update private DNS settings
<a name="update-private-dns-settings"></a>

After you create a resource VPC endpoint, service-network VPC endpoint, or service network VPC association, you can enable or disable private DNS, change its private DNS preference, and change its private DNS specified domains. To update a resource VPC endpoint or service-network VPC endpoint, use the `modify-vpc-endpoint` command. To update a service network VPC association, use the `update-service-network-vpc-association` command.

The new settings apply only to resource configurations that are connected after you make the change. Resource configurations that are already connected keep working, and their existing DNS records don't change. To apply new settings to a resource configuration that's already connected, reconnect it: delete and re-create the endpoint or VPC association, or, for a service network, the service network owner can remove the resource configuration from the service network and add it back. Both interrupt connectivity to the resource configuration. For a resource VPC endpoint to a single resource configuration, an update doesn't take effect, so re-create the endpoint with the settings you want. For a resource VPC endpoint to a group resource configuration, each child resource configuration added to the group afterward uses the endpoint's current settings.

Updates to a resource VPC endpoint or service-network VPC endpoint are applied during the call. Updates to a service network VPC association are asynchronous, and the association status is `UPDATE_IN_PROGRESS` until the update completes. You can update security groups and private DNS settings in the same request.

When you update a resource VPC endpoint or service-network VPC endpoint, DNS options that you leave out don't change, with these exceptions. If you specify a private DNS preference without specified domains, the list of specified domains is cleared. If you specify domains without a preference, the update has no effect and the current settings stay. If you turn on private DNS without DNS options, the preference is set to `VERIFIED_DOMAINS_ONLY` with the specified domain `*`. If you turn off private DNS, the preference and the specified domains are cleared.

For a group resource configuration, specify a wildcard for the group domain as a private DNS specified domain, for example, `*.example.com`. If you specify only the child domain names, or only the group domain, VPC Lattice doesn't create private DNS records for the group. For a single resource configuration, specify its custom domain name or a wildcard that covers it. A wildcard such as `*.example.com` matches example.com and every name under it.

A private hosted zone that VPC Lattice creates for a domain answers for every name under that domain in your VPC. For example, a private hosted zone for example.com stops other example.com names from resolving in that VPC. Enable private DNS only for domains whose traffic you want to route through VPC Lattice.

### Private hosted zone reuse
<a name="private-hosted-zone-reuse"></a>

If VPC Lattice already created a private hosted zone in your VPC for the group domain of a group resource configuration, and you connect another group resource configuration with the same group domain through another resource VPC endpoint, service-network VPC endpoint, or service network VPC association, VPC Lattice reuses the existing private hosted zone and adds records for the new child resource configurations to it. VPC Lattice creates records only for child domain names, not for the group domain itself. You can then access multiple group resource configurations that share a group domain (for example, several groups under example.com) from the same VPC. Reuse applies only to group resource configurations.

VPC Lattice keeps a shared private hosted zone until the last endpoint or VPC association that uses it is deleted. A connection's records are removed when its resource configuration is disconnected or the connection is deleted.

Reuse applies to different child domain names under the same group domain. If two endpoints or VPC associations in the same VPC claim the same domain name, the first one keeps the DNS record. On the second connection, only the resource configuration with that name fails and is unreachable, and its other resource configurations work. If the connection that holds the record is deleted, the other connection doesn't take it over. To get the record, re-create the other connection. For resource VPC endpoints and service-network VPC endpoints, `describe-vpc-endpoint-associations` shows `PrivateDnsAlreadyExists` for the resource configuration that failed.

If a private hosted zone that you own for the same domain is associated with the VPC, VPC Lattice reports `PrivateDnsAlreadyExists` for that domain and doesn't change your private hosted zone. To keep using your own private hosted zone, exclude the domain from the private DNS settings before you connect. Then, in your private hosted zone, create a record for each resource configuration that maps its custom domain name (for example, db.example.com) to the endpoint-specific domain name that VPC Lattice generates for that resource configuration (for example, `vpce-0123456789abcdef0-snra-0123456789abcdef0.rcfg-0123456789abcdef0.4x5y6z.vpc-lattice-rsc.us-east-1.on.aws`). Without this mapping, the custom domain name doesn't resolve to the endpoint. To find the generated domain names, use the `describe-vpc-endpoint-associations` command.

A private hosted zone can contain up to 10,000 records (Route 53 quota). For service-network VPC endpoints, this is about 1,000 domain names per domain in a VPC. The exact number depends on the number of Availability Zones.

Connections that failed with `PrivateDnsAlreadyExists` before reuse was available aren't retried. To get private DNS for them, re-create the connection.

### Differences between connection types
<a name="differences-between-connection-types"></a>

You can connect to resource configurations through a resource VPC endpoint, a service-network VPC endpoint, or a service network VPC association. The following table shows how they differ when you update them.


| Characteristic | Resource VPC endpoint | Service-network VPC endpoint | Service network VPC association | 
| --- | --- | --- | --- | 
| Connects to | One resource configuration (single, group, or ARN) | A service network | A service network | 
| Update API | ModifyVpcEndpoint (Amazon EC2) | ModifyVpcEndpoint (Amazon EC2) | UpdateServiceNetworkVpcAssociation (VPC Lattice) | 
| When the update is applied | During the call | During the call | Asynchronously. Status is UPDATE\_IN\_PROGRESS until it completes | 
| Updating DNS options | --dns-options. Options you leave out don't change, except that a preference without specified domains clears the domain list | Same as resource VPC endpoint | --dns-options together with --private-dns-enabled. Omitted options reset to defaults | 
| Applying new DNS settings to resource configurations that are already connected | Single resource configuration: the update never applies, so re-create the endpoint. Group: each child added afterward uses the endpoint's current settings | Re-create the endpoint, or the service network owner removes the resource configuration and adds it back | Re-create the VPC association, or the service network owner removes the resource configuration and adds it back | 
| Service network owner's private DNS setting | Not applicable (no service network) | Can only turn private DNS off for a resource configuration, never on. Doesn't apply to ARN (Amazon RDS) resource configurations | Same as service-network VPC endpoint | 
| Same-name DNS conflicts reported | Yes: describe-vpc-endpoint-associations shows PrivateDnsAlreadyExists | Yes: same as resource VPC endpoint | Not reported per resource today. To check, resolve the name from an instance in the VPC | 
| Subnets | Chosen at creation | Chosen at creation. Add only, in a separate request | You don't choose subnets | 
| Security groups | Can be updated | Can be updated | Can be updated, but you can't remove all of them | 
| DNS options field names | PrivateDnsPreference, PrivateDnsSpecifiedDomains (0-10 domains) | Same as resource VPC endpoint | privateDnsPreference, privateDnsSpecifiedDomains (1-10 domains) | 

## Custom domain names for service network owners
<a name="resource-configuration-custom-domain-name-service-network-owners"></a>

The private DNS enabled property of the service network resource association overrides the private DNS enabled property of the service network endpoint and the service network VPC association. 

If a service network owner creates a service network resource association and doesn't enable private DNS, VPC Lattice won't provision private hosted zones for that resource configuration in any VPCs that the service network is connected to, even though private DNS is enabled on the service network endpoint or service network VPC associations. 

For resource configurations of type ARN, the private DNS flag is true and immutable. VPC Lattice provisions private hosted zones for ARN resource types regardless of the private DNS property setting of the service network endpoint and the service network VPC association. The exception is when the resource gateway is in the same VPC. In other words, when a VPC is both a consumer and a provider for an ARN type of resource configuration, VPC Lattice skips the creation of the private hosted zones in that VPC.

## Resource definition
<a name="resource-definition"></a>

In the resource configuration, identify the resource in one of the following ways:
+ By an **Amazon Resource Name (ARN)**: Supported resource-types that are provisioned by AWS services, can be identified by their ARN. Only Amazon RDS databases are supported. You can't create a resource configuration for a publicly accessible cluster.
+ By a **domain-name target**: You can use any domain name. If you use a private DNS server or your domain is in a Route 53 private hosted zone, then the resource gateway must have DNS resolution set to IN\_VPC. If your domain name points to an IP that's outside of your VPC, you must have a NAT gateway in your VPC. Domain-name targets that resolve to public IPv6 addresses are not supported.
+ By an **IP-address**: For IPv4, specify a private IP from the following ranges: 10.0.0.0/8, 100.64.0.0/10, 172.16.0.0/12, 192.168.0.0/16. For IPv6, specify an IP from the VPC. Public IPs aren't supported.
+ By a **CIDR range**: For a resource configuration of type CIDR, specify the list of CIDRs you want to share (for example, 10.0.0.0/24). The CIDRs should be reachable from the resource gateway. To provide full network access, specify 0.0.0.0/0 if using IPv4 or ::/0 if using IPv6.

## Port ranges
<a name="resource-configuration-port"></a>

When you create a resource configuration you can define the ports it will accept requests on. Client access on other ports will not be allowed.

## Accessing resources
<a name="resource-configuration-accessing"></a>

Consumers can access resource configurations directly from their VPC using a VPC endpoint or through a service network. As a consumer, you can enable access from your VPC to a resource configuration that is in your account or that has been shared with you from another account through AWS RAM.
+ * Accessing a resource configuration directly*

  You can access resource configurations directly through AWS PrivateLink-based resource endpoints and tunnel endpoints. You can create a resource endpoint in your VPC to access resource configurations of types ARN, Single, and Group, and you can create a tunnel endpoint to access resource configurations of type CIDR. For more information on how to create resource and tunnel endpoints, see [Accessing VPC resources](https://docs.aws.amazon.com/vpc/latest/privatelink/privatelink-access-resources.html) and [Accessing network segments](https://docs.aws.amazon.com/vpc/latest/privatelink/privatelink-access-cidr-ranges.html) in the *AWS PrivateLink user guide*.
+ *Accessing a resource configuration through a service network*

  You can associate a resource configuration with a service network and connect your VPC to the service network. You can connect your VPC to the service network either through an association or using a AWS PrivateLink-based service network endpoint. CIDR resource configurations cannot be associated with a service network.

  For more information on service network associations, see [Manage the associations for a VPC Lattice service network](https://docs.aws.amazon.com/vpc-lattice/latest/ug/service-network-associations.html).

  For more information on service network VPC endpoints, see [Access service networks](https://docs.aws.amazon.com/vpc/latest/privatelink/privatelink-access-service-networks.html) in the *AWS PrivateLink user guide*.

When private DNS is enabled for your VPC, you can't access the same resource configuration through both a resource endpoint and a service-network endpoint in that VPC. The first endpoint to claim the domain name keeps the DNS record, and the association for the second endpoint fails. For more information, see [Private hosted zone reuse](#private-hosted-zone-reuse). To access the resource configuration through both, turn off private DNS on one of them before you connect it, and use its VPC Lattice-generated DNS name.

## Association with service network type
<a name="resource-configuration-service-network-association"></a>

When you share a resource configuration with a consumer account, for example, Account-B, through AWS RAM, Account-B can access the resource configuration either directly through a resource endpoint or tunnel endpoint, or through a service network. CIDR resource configurations cannot be accessed through a service network. They can only be accessed directly through a tunnel endpoint.

To access a resource configuration through a service network, Account-B would have to associate the resource configuration with a service network. Service networks are shareable between accounts. So, Account-B can share their service network (that the resource configuration is associated to) with Account-C, making your resource accessible from Account-C.

In order to prevent such transitive sharing, you can specify that your resource configuration cannot be added to service networks that are shareable between accounts. If you specify this, then Account-B won't be able to add your resource configuration to service networks that are shared or can be shared with another account in the future.

## Types of service networks
<a name="service-network-types"></a>

When you share a resource configuration with another account, for example, Account-B, through AWS RAM, Account-B can access the resource in one of four ways:
+ Using a AWS PrivateLink-based resource endpoint (for Single, Group, and ARN resource configurations).
+ Using a AWS PrivateLink-based tunnel endpoint (for CIDR resource configurations).
+ Using a AWS PrivateLink-based service network endpoint.
+ Using a service network VPC association.

When you use a service-network association, each resource is assigned an IP per subnet from the 129.224.0.0/17 block, which is AWS owned and non-routable. This is in addition to the [managed prefix list](security-groups.md#managed-prefix-list) that VPC Lattice uses to route traffic to services over the VPC Lattice network. Both of these IPs are updated to your VPC route table.

For a service network endpoint and a service network VPC association, the resource configuration would have to be associated with a service network in Account-B. Service networks are shareable between accounts. So, Account-B can share their service network (that contains the resource configuration) with Account-C, making your resource accessible from Account-C. To prevent such transitive sharing, you can disallow your resource configuration from being added to service networks that are shareable between accounts. If you disallow this, then Account-B won't be able to add your resource configuration to a service network that is shared or can be shared with another account.

## Sharing resource configurations through AWS RAM
<a name="sharing-resource-configuration-ram"></a>

Resource configurations are integrated with AWS Resource Access Manager. You can share your resource configuration with another account through AWS RAM. When you share a resource configuration with an AWS account, clients in that account can privately access the resource. You can share a resource configuration using a [resource share](https://docs.aws.amazon.com/ram/latest/userguide/working-with-sharing.html) in AWS RAM. 

Use the AWS RAM console, to view the resource shares to which you have been added, the shared resources that you can access, and the AWS accounts that have shared resources with you. For more information, see [Resources shared with you ](https://docs.aws.amazon.com/ram/latest/userguide/working-with-shared.html) in the *AWS RAM User Guide*.

To access a resource from another VPC in the same account as the resource configuration, you don't need to share the resource configuration through AWS RAM.

## Monitoring
<a name="resource-configuration-monitoring"></a>

You can enable monitoring logs on your resource configuration. You can choose a destination to send the logs to.

VPC Lattice also publishes Amazon CloudWatch metrics for each resource configuration to the `AWS/VpcLattice` namespace. You can view metrics for the resource configuration overall, per Availability Zone, or per association (service network resource association or VPC endpoint association). For a group resource configuration, the group's metrics are the sum of the metrics of its child resource configurations, and each child resource configuration also has its own metrics. For more information, see [Resource gateway and resource configuration metrics](monitoring-cloudwatch.md#resource-gateway-resource-configuration-metrics).