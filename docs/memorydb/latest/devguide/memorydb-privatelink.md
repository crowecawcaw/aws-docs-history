# MemoryDB API and interface VPC endpoints

(AWS PrivateLink)

You can establish a private connection between your VPC and Amazon
MemoryDB API endpoints by creating an
_interface
VPC endpoint_. Interface endpoints
are
powered by
[AWS PrivateLink](https://aws.amazon.com/privatelink "https://aws.amazon.com/privatelink"). AWS PrivateLink
allows
you to privately access MemoryDB API operations without an internet
gateway, NAT device, VPN connection, or AWS Direct Connect connection.

Instances in your VPC don't need public IP addresses to communicate with
MemoryDB API endpoints. Your instances also don't need public IP addresses to use any of
the available MemoryDB API operations. Traffic between your VPC and MemoryDB doesn't leave the
Amazon network. Each interface endpoint is represented by one or more elastic network
interfaces in your subnets. For more information on elastic network interfaces, see [Elastic network
interfaces](../../../AWSEC2/latest/UserGuide/using-eni.md "../../../AWSEC2/latest/UserGuide/using-eni.md") in the _Amazon EC2 User Guide_.

- For more information about VPC endpoints, see [Interface VPC endpoints (AWS
  PrivateLink)](../../../vpc/latest/userguide/vpce-interface.md "../../../vpc/latest/userguide/vpce-interface.md") in the _Amazon VPC User Guide_.
- For more information about MemoryDB API operations, see [MemoryDB API operations](../APIReference/Welcome.md "../APIReference/Welcome.md").
  After you create an interface VPC endpoint, if you enable [private DNS](../../../vpc/latest/userguide/vpce-interface.md#vpce-private-dns "../../../vpc/latest/userguide/vpce-interface.md#vpce-private-dns") hostnames for the endpoint, the default
  MemoryDB endpoint (https://memorydb.`Region`.amazonaws.com) resolves to your VPC endpoint.
  If you do not enable private DNS hostnames, Amazon VPC provides a DNS endpoint name that you can use in the following format:

```
VPC_Endpoint_ID.memorydb.Region.vpce.amazonaws.com
```

For more information, see [Interface VPC Endpoints (AWS PrivateLink)](../../../vpc/latest/userguide/vpce-interface.md "../../../vpc/latest/userguide/vpce-interface.md") in the _Amazon VPC User Guide_. MemoryDB supports making calls to all
of its [API Actions](../APIReference/API_Operations.md "../APIReference/API_Operations.md") inside your VPC.

###### Note

Private DNS hostnames can be enabled for only one VPC endpoint in the VPC. If you want to create an additional VPC endpoint then private
DNS hostname should be disabled for it.

## Considerations for VPC

endpoints

Before you set up an interface VPC endpoint for MemoryDB API endpoints, ensure that
you review [Interface endpoint
properties and limitations](../../../vpc/latest/privatelink/endpoint-services-overview.md "../../../vpc/latest/privatelink/endpoint-services-overview.md") in the _Amazon VPC User
Guide_. All MemoryDB API operations
that are
relevant to managing MemoryDB resources are available from your VPC
using AWS PrivateLink. VPC endpoint policies are supported for MemoryDB API endpoints. By
default, full access to MemoryDB API operations is allowed through the endpoint. For more
information, see [Controlling access to services
with VPC endpoints](../../../vpc/latest/userguide/vpc-endpoints-access.md "../../../vpc/latest/userguide/vpc-endpoints-access.md") in the _Amazon VPC User Guide_.

### Creating an interface VPC

endpoint for
the
MemoryDB API

You can create a VPC endpoint for the MemoryDB API using either the Amazon VPC console or the AWS CLI. For more information,
see [Creating an interface endpoint](../../../vpc/latest/privatelink/create-endpoint-service.md "../../../vpc/latest/privatelink/create-endpoint-service.md")
in the _Amazon VPC User Guide_.

After you create an interface VPC endpoint, you can enable private DNS host names for the endpoint. When you do, the default MemoryDB endpoint (https://memorydb.`Region`.amazonaws.com) resolves to your VPC endpoint.
For more information, see [Accessing a service through an interface endpoint](../../../vpc/latest/userguide/vpce-interface.md#access-service-though-endpoint "../../../vpc/latest/userguide/vpce-interface.md#access-service-though-endpoint") in the
_Amazon VPC User Guide_.

### Creating a VPC endpoint policy for

the
Amazon MemoryDB API

You can attach an endpoint policy to your VPC endpoint that controls access to the
MemoryDB API. The policy specifies the following:

- The principal that can perform actions.
- The actions that can be performed.
- The resources on which actions can be performed.

For more information, see [Controlling access to services
with VPC endpoints](../../../vpc/latest/userguide/vpc-endpoints-access.md "../../../vpc/latest/userguide/vpc-endpoints-access.md") in the _Amazon VPC User Guide_.

###### Example VPC endpoint policy for MemoryDB API actions

The following is an example of an endpoint policy for the MemoryDB API. When attached
to an endpoint, this policy grants access to the listed MemoryDB API actions for all
principals on all resources.

```
{
	"Statement": [{
		"Principal": "*",
		"Effect": "Allow",
		"Action": [
			"memorydb:CreateCluster",
			"memorydb:UpdateCluster",
			"memorydb:CreateSnapshot"
		],
		"Resource": "*"
	}]
}
```

###### Example VPC endpoint policy that denies all access from a specified AWS account

The following VPC endpoint policy denies AWS account
`123456789012` all access to resources using the
endpoint. The policy allows all actions from other accounts.

```
{
	"Statement": [{
			"Action": "*",
			"Effect": "Allow",
			"Resource": "*",
			"Principal": "*"
		},
		{
			"Action": "*",
			"Effect": "Deny",
			"Resource": "*",
			"Principal": {
				"AWS": [
					"123456789012"
				]
			}
		}
	]
}
```
