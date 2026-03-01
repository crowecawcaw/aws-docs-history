# ElastiCache API and interface VPC endpoints (AWS PrivateLink)

You can establish a private connection between your VPC and Amazon ElastiCache API endpoints by
creating an _interface VPC endpoint_. Interface endpoints
are
powered by
[AWS PrivateLink](https://aws.amazon.com/privatelink "https://aws.amazon.com/privatelink"). AWS PrivateLink allows
you to privately access Amazon ElastiCache API operations without an internet gateway, NAT device,
VPN connection, or AWS Direct Connect connection.

Instances in your VPC don't need public IP addresses to communicate with Amazon ElastiCache API
endpoints. Your instances also don't need public IP addresses to use any of the available
ElastiCache API operations. Traffic between your VPC and Amazon ElastiCache doesn't leave the Amazon
network. Each interface endpoint is represented by one or more elastic network interfaces in
your subnets. For more information on elastic network interfaces, see [Elastic network
interfaces](../../../AWSEC2/latest/UserGuide/using-eni.md "../../../AWSEC2/latest/UserGuide/using-eni.md") in the _Amazon EC2 User Guide_.

- For more information about VPC endpoints, see [Interface VPC endpoints (AWS
  PrivateLink)](../../../vpc/latest/userguide/vpce-interface.md "../../../vpc/latest/userguide/vpce-interface.md") in the _Amazon VPC User Guide_.
- For more information about ElastiCache API operations, see [ElastiCache API
  operations](../APIReference/Welcome.md "../APIReference/Welcome.md").
  After you create an interface VPC endpoint, if you enable [private DNS](../../../vpc/latest/userguide/vpce-interface.md#vpce-private-dns "../../../vpc/latest/userguide/vpce-interface.md#vpce-private-dns")
  hostnames for the endpoint, the default ElastiCache endpoint
  (https://elasticache.`Region`.amazonaws.com) and dualstack
  endpoint (https://elasticache.`Region`.api.aws) resolve to your VPC
  endpoint. If you do not enable private DNS hostnames, Amazon VPC provides a DNS endpoint name
  that you can use in the following format:

```
VPC_Endpoint_ID.elasticache.Region.vpce.amazonaws.com
```

For more information, see [Interface VPC Endpoints (AWS
PrivateLink)](../../../vpc/latest/userguide/vpce-interface.md "../../../vpc/latest/userguide/vpce-interface.md") in the _Amazon VPC User Guide_. ElastiCache supports
making calls to all of its [API Actions](../APIReference/API_Operations.md "../APIReference/API_Operations.md")
inside your VPC.

###### Note

Private DNS hostnames can be enabled for only one VPC endpoint in the VPC. If you want
to create an additional VPC endpoint then private DNS hostname should be disabled for
that endpoint.

| Available Privatelink Regions | Code                      | Location       | Region |
| ----------------------------- | ------------------------- | -------------- | ------ |
| CPT                           | Africa (Cape Town)        | AF-SOUTH-1     |
| HKG                           | Asia Pacific (Hong Kong)  | AP-EAST-1      |
| TPE                           | Asia Pacific (Taipei)     | AP-EAST-2      |
| NRT                           | Asia Pacific (Tokyo)      | AP-NORTHEAST-1 |
| ICN                           | Asia Pacific (Seoul)      | AP-NORTHEAST-2 |
| KIX                           | Asia Pacific (Osaka)      | AP-NORTHEAST-3 |
| BOM                           | Asia Pacific (Mumbai)     | AP-SOUTH-1     |
| HYD                           | Asia Pacific (Hyderabad)  | AP-SOUTH-2     |
| SIN                           | Asia Pacific (Singapore)  | AP-SOUTHEAST-1 |
| SYD                           | Asia Pacific (Sydney)     | AP-SOUTHEAST-2 |
| CGK                           | Asia Pacific (Jakarta)    | AP-SOUTHEAST-3 |
| MEL                           | Asia Pacific (Melbourne)  | AP-SOUTHEAST-4 |
| KUL                           | Asia Pacific (Malaysia)   | AP-SOUTHEAST-5 |
| BKK                           | Asia Pacific (Thailand)   | AP-SOUTHEAST-7 |
| YUL                           | Canada (Central)          | CA-CENTRAL-1   |
| YYC                           | Canada West (Calgary)     | CA-WEST-1      |
| BJS                           | China (Beijing)           | CN-NORTH-1     |
| ZHY                           | China (Ningxia)           | CN-NORTHWEST-1 |
| FRA                           | Europe (Frankfurt)        | EU-CENTRAL-1   |
| ZRH                           | Europe (Zurich)           | EU-CENTRAL-2   |
| ARN                           | Europe (Stockholm)        | EU-NORTH-1     |
| MXP                           | Europe (Milan)            | EU-SOUTH-1     |
| ZAZ                           | Europe (Spain)            | EU-SOUTH-2     |
| DUB                           | Europe (Ireland)          | EU-WEST-1      |
| LHR                           | Europe (London)           | EU-WEST-2      |
| CDG                           | Europe (Paris)            | EU-WEST-3      |
| TLV                           | Tel Aviv (Israel)         | IL-CENTRAL-1   |
| DXB                           | Middle East (UAE)         | ME-CENTRAL-1   |
| BAH                           | Middle East (Bahrain)     | ME-SOUTH-1     |
| QRO                           | Mexico (Central)          | MX-CENTRAL-1   |
| GRU                           | South America (Sao Paulo) | SA-EAST-1      |
| IAD                           | US East (N. Virginia)     | US-EAST-1      |
| CMH                           | US East (Ohio)            | US-EAST-2      |
| OSU                           | AWS GovCloud (US-East)    | US-GOV-EAST-1  |
| SFO                           | US West (N. California)   | US-WEST-1      |
| PDX                           | US West (Oregon)          | US-WEST-2      |
| PDT                           | AWS GovCloud (US-West)    | US-WEST-1      |

## Considerations for VPC endpoints

Before you set up an interface VPC endpoint for Amazon ElastiCache API endpoints, ensure that
you review [Interface endpoint
properties and limitations](../../../vpc/latest/privatelink/endpoint-services-overview.md "../../../vpc/latest/privatelink/endpoint-services-overview.md") in the _Amazon VPC User
Guide_. All ElastiCache API operations relevant to managing Amazon ElastiCache resources are
available from your VPC using AWS PrivateLink.

VPC endpoint policies are supported for ElastiCache API endpoints. By default, full access
to ElastiCache API operations is allowed through the endpoint. For more information, see
[Controlling access to services with VPC endpoints](../../../vpc/latest/userguide/vpc-endpoints-access.md "../../../vpc/latest/userguide/vpc-endpoints-access.md") in the _Amazon
VPC User Guide_.

## Creating an interface VPC endpoint for the ElastiCache API

You can create a VPC endpoint for the Amazon ElastiCache API using either the Amazon VPC console or
the AWS CLI. For more information, see [Creating an interface
endpoint](../../../vpc/latest/privatelink/create-endpoint-service.md "../../../vpc/latest/privatelink/create-endpoint-service.md") in the _Amazon VPC User Guide_.

After you create an interface VPC endpoint, you can enable private DNS hostnames for
the endpoint. When you do, the default Amazon ElastiCache endpoint
(https://elasticache.`Region`.amazonaws.com) and dualstack endpoint (https://elasticache.`Region`.api.aws) resolve to your VPC endpoint.

For the China (Beijing) and China (Ningxia) AWS Regions, you can make API requests with the VPC endpoint by using `elasticache.cn-north-1.amazonaws.com.cn` and `elasticache.cn-north-1.api.amazonwebservices.com.cn` for Beijing, and `elasticache.cn-northwest-1.amazonaws.com.cn` and `elasticache.cn-northwest-1.api.amazonwebservices.com.cn` for Ningxia. For more
information, see [Accessing a service through an interface endpoint](../../../vpc/latest/userguide/vpce-interface.md#access-service-though-endpoint "../../../vpc/latest/userguide/vpce-interface.md#access-service-though-endpoint") in the _Amazon
VPC User Guide_.

## Creating a VPC endpoint policy for the Amazon ElastiCache API

You can attach an endpoint policy to your VPC endpoint that controls access to the
ElastiCache API. The policy specifies the following:

- The principal that can perform actions.
- The actions that can be performed.
- The resources on which actions can be performed.

For more information, see [Controlling access to services
with VPC endpoints](../../../vpc/latest/userguide/vpc-endpoints-access.md "../../../vpc/latest/userguide/vpc-endpoints-access.md") in the _Amazon VPC User Guide_.

###### Example VPC endpoint policy for ElastiCache API actions with Valkey or Redis OSS

The following is an example of an endpoint policy for the ElastiCache API. When attached
to an endpoint, this policy grants access to the listed ElastiCache API actions for all
principals on all resources.

```
{
	"Statement": [{
		"Principal": "*",
		"Effect": "Allow",
		"Action": [
			"elasticache:CreateCacheCluster",
			"elasticache:ModifyCacheCluster",
			"elasticache:CreateSnapshot"
		],
		"Resource": "*"
	}]
}
```

###### Example VPC endpoint policy for ElastiCache for Memcached API actions

The following is an example of an endpoint policy for the ElastiCache API. When attached
to an endpoint, this policy grants access to the listed ElastiCache API actions for all
principals on all resources.

```
{
	"Statement": [{
		"Principal": "*",
		"Effect": "Allow",
		"Action": [
			"elasticache:CreateCacheCluster",
			"elasticache:ModifyCacheCluster"
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
