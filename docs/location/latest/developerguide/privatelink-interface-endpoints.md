# AWS PrivateLink for Amazon Location

With AWS PrivateLink for Amazon Location, you can provision _interface
Amazon VPC endpoints_ (interface endpoints) in your virtual private cloud (Amazon VPC).
These endpoints are directly accessible from applications that are on premises over VPN and
AWS Direct Connect, or in a different AWS Region over [Amazon VPC peering](../../../vpc/latest/peering/what-is-vpc-peering.md "../../../vpc/latest/peering/what-is-vpc-peering.md"). Using
AWS PrivateLink and interface endpoints, you can simplify private network connectivity from
your applications to Amazon Location.

Applications in your VPC don't need public IP addresses to communicate with Amazon Location
interface VPC endpoints for Amazon Location operations. Interface endpoints are represented by one
or more elastic network interfaces (ENIs) that are assigned private IP addresses from
subnets in your Amazon VPC. Requests to Amazon Location over interface endpoints stay on the Amazon
network. You can also access interface endpoints in your Amazon VPC from on-premises applications
through AWS Direct Connect or AWS Virtual Private Network (AWS VPN). For more information about how to connect your Amazon VPC
with your on-premises network, see the [AWS Direct Connect User Guide](../../../directconnect/latest/UserGuide/Welcome.md "../../../directconnect/latest/UserGuide/Welcome.md") and the
[AWS Site-to-Site VPN
User Guide](../../../vpn/latest/s2svpn/VPC_VPN.md "../../../vpn/latest/s2svpn/VPC_VPN.md").

For general information about interface endpoints, see [Interface Amazon VPC endpoints
(AWS PrivateLink)](../../../vpc/latest/privatelink/vpce-interface.md "../../../vpc/latest/privatelink/vpce-interface.md") in the _AWS PrivateLink
Guide_.

###### Topics

- [Types of Amazon VPC endpoints for Amazon Location
  Service](#types-of-vpc-endpoints-for-al "#types-of-vpc-endpoints-for-al")
- [Considerations when using AWS PrivateLink for
  Amazon Location Service](#privatelink-considerations "#privatelink-considerations")
- [Create an interface endpoint for Amazon Location Service](#al-creating-vpc "#al-creating-vpc")
- [Access Amazon Location API
  operations from Amazon Location interface endpoints](#accessing-apis-from-interface-endpoints "#accessing-apis-from-interface-endpoints")
- [Update an on-premises DNS
  configuration](#updating-on-premises-dns-config "#updating-on-premises-dns-config")
- [Create an Amazon VPC endpoint policy for
  Amazon Location](#creating-vpc-endpoint-policy "#creating-vpc-endpoint-policy")

## Types of Amazon VPC endpoints for Amazon Location

Service

You can use one type of Amazon VPC endpoint to access Amazon Location Service: _interface endpoints_ (by using AWS PrivateLink). _Interface endpoints_ use private IP addresses to route
requests to Amazon Location from within your Amazon VPC, on premises, or from an Amazon VPC in another
AWS Region by using Amazon VPC peering. For more information, see [What is
Amazon VPC peering?](../../../vpc/latest/peering/what-is-vpc-peering.md "../../../vpc/latest/peering/what-is-vpc-peering.md") and [Transit Gateway vs Amazon VPC peering](../../../whitepapers/latest/building-scalable-secure-multi-vpc-network-infrastructure/transit-gateway-vs-vpc-peering.md "../../../whitepapers/latest/building-scalable-secure-multi-vpc-network-infrastructure/transit-gateway-vs-vpc-peering.md").

Interface endpoints are compatible with gateway endpoints. If you have an existing
gateway endpoint in the Amazon VPC, you can use both types of endpoints in the same
Amazon VPC.

Interface endpoints for Amazon Location have the following properties:

- Your network traffic remains on the AWS network
- Use private IP addresses from your Amazon VPC to access Amazon Location Service
- Allows access from on premises
- Allows access from an Amazon VPC endpoint in another AWS Region by using Amazon VPC
  peering or AWS Transit Gateway
- Interface endpoints are billed

## Considerations when using AWS PrivateLink for

Amazon Location Service

Amazon VPC considerations apply to AWS PrivateLink for Amazon Location Service. For more information, see
[Interface endpoint considerations](../../../vpc/latest/privatelink/vpce-interface.md#vpce-interface-limitations "../../../vpc/latest/privatelink/vpce-interface.md#vpce-interface-limitations") and [AWS PrivateLink quotas](../../../vpc/latest/privatelink/vpc-limits-endpoints.md "../../../vpc/latest/privatelink/vpc-limits-endpoints.md")
in the _AWS PrivateLink Guide_. In addition, the
following restrictions apply.

AWS PrivateLink for Amazon Location Service doesn't support the following:

- Transport Layer Security (TLS) 1.1
- Private and Hybrid Domain Name System (DNS) services

Amazon VPC endpoints:

- Don't support [Amazon Location Service Maps API](../APIReference/API_Operations_Amazon_Location_Service_Maps.md "../APIReference/API_Operations_Amazon_Location_Service_Maps.md") operations, including: `GetGlyphs`,
  `GetSprites`, and `GetStyleDescriptor`
- Don't support cross-region requests. Ensure that you create your endpoint in
  the same region where you plan to issue your API calls to Amazon Location Service.
- Only support Amazon-provided DNS through Amazon Route 53. If you want to use your
  own DNS, use conditional DNS forwarding. For more information, see [DHCP
  Options Sets](../../../vpc/latest/userguide/VPC_DHCP_Options.md "../../../vpc/latest/userguide/VPC_DHCP_Options.md") in the _Amazon VPC User
  Guide_.
- Must allow incoming connections on port 443 from the private subnet of the VPC
  through the security group attached to the VPC endpoint

You can submit up to 50,000 requests per second for each AWS PrivateLink endpoint that
you enable.

###### Note

Network connectivity timeouts to AWS PrivateLink endpoints are not within the scope
of Amazon Location error responses and need to be appropriately handled by your
applications connecting to the AWS PrivateLink endpoints.

## Create an interface endpoint for Amazon Location Service

You can create an interface endpoint for Amazon Location Service using either the Amazon VPC Console or the
AWS Command Line Interface (AWS CLI). For more information, see [Create
an interface endpoint](../../../vpc/latest/privatelink/vpce-interface.md#create-interface-endpoint "../../../vpc/latest/privatelink/vpce-interface.md#create-interface-endpoint") in the _AWS PrivateLink
Guide_.

There are six different VPC endpoints, one for each feature offered by
Amazon Location Service.

| Category  | Endpoint                                |
| --------- | --------------------------------------- |
| Maps      | `com.amazonaws.`region`.geo.maps`       |
| Places    | `com.amazonaws.`region`.geo.places`     |
| Routes    | `com.amazonaws.`region`.geo.routes`     |
| Geofences | `com.amazonaws.`region`.geo.geofencing` |
| Trackers  | `com.amazonaws.`region`.geo.tracking`   |
| Metadata  | `com.amazonaws.`region`.geo.metadata`   |

**For example:**

```
com.amazonaws.`us-east-2`.geo.maps
```

After you create the endpoint, you have the option to enable a private DNS hostname.
To enable, select **Enable Private DNS Name** in the Amazon VPC Console when
you create the VPC endpoint.

If you enable private DNS for the interface endpoint, you can make API requests to
Amazon Location Service service using its default Regional DNS name. The following examples show the
default Regional DNS names format.

- `maps.geo.`region`.amazonaws.com`
- `places.geo.`region`.amazonaws.com`
- `routes.geo.`region`.amazonaws.com`
- `tracking.geo.`region`.amazonaws.com`
- `geofencing.geo.`region`.amazonaws.com`
- `metadata.geo.`region`.amazonaws.com`

The previous DNS names are for IPv4 domains. The following IPV6 DNS names can also be
used for interface endpoints.

- `maps.geo.`region`.api.aws`
- `places.geo.`region`.api.aws`
- `routes.geo.`region`.api.aws`
- `tracking.geo.`region`.api.aws`
- `geofencing.geo.`region`.api.aws`
- `metadata.geo.`region`.api.aws`

## Access Amazon Location API

operations from Amazon Location interface endpoints

You can use the [AWS CLI](../../../cli/latest/reference/location.md "../../../cli/latest/reference/location.md") or [AWS SDKs](dev-sdks.md "dev-sdks.md") to access
Amazon Location API operations through Amazon Location interface endpoints.

**Example: Create a VPC endpoint**

```
aws ec2 create-vpc-endpoint \
--region us-east-1 \
--service-name location-service-name \
--vpc-id client-vpc-id \
--subnet-ids client-subnet-id \
--vpc-endpoint-type Interface \
--security-group-ids client-sg-id
```

**Example: Modify a VPC endpoint**

```
aws ec2 modify-vpc-endpoint \
--region us-east-1 \
--vpc-endpoint-id client-vpc-endpoint-id \
--policy-document policy-document \ #example optional parameter
--add-security-group-ids security-group-ids \ #example optional parameter
# any additional parameters needed, see PrivateLink documentation for more details
```

## Update an on-premises DNS

configuration

When using endpoint-specific DNS names to access the interface endpoints for
Amazon Location, you don't have to update your on-premises DNS resolver. You can resolve the
endpoint-specific DNS name with the private IP address of the interface endpoint from
the public Amazon Location DNS domain.

Use interface endpoints to access Amazon Location without a gateway endpoint or an internet
gateway in the Amazon VPC

Interface endpoints in your Amazon VPC can route both in-Amazon VPC applications and on-premises
applications to Amazon Location over the Amazon network.

## Create an Amazon VPC endpoint policy for

Amazon Location

You can attach an endpoint policy to your Amazon VPC endpoint that controls access to
Amazon Location. The policy specifies the following information:

- The AWS Identity and Access Management (IAM) principal that can perform actions
- The actions that can be performed
- The resources on which actions can be performed

**Example:** Sample VPCe policy for accessing Amazon Location Service
Places APIs:

```
{
	"Version": "2012-10-17",
	"Statement": [
		{
			"Sid": "Allow-access-to-location-service-places-opeartions",
			"Effect": "Allow",
			"Action": [
				"geo-places:*",
				"geo:*"
			],
			"Resource": [
				"arn:aws:geo-places:`us-east-1`::provider/default",
				"arn:aws:geo:us-east-1:*:place-index/*"
			]
		}
	]
}
```
