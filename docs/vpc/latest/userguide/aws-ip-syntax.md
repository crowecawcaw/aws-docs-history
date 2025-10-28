# Syntax for AWS IP address range JSON

AWS publishes its current IP address ranges in JSON format. To get the JSON file,
see [Download the JSON file](aws-ip-ranges.md#aws-ip-download "aws-ip-ranges.md#aws-ip-download"). The syntax of the JSON file is as follows.

```
{
  "syncToken": "`0123456789`",
  "createDate": "`yyyy`-`mm`-`dd`-`hh`-`mm`-`ss`",
  "prefixes": [
    {
      "ip_prefix": "`cidr`",
      "region": "`region`",
      "network_border_group": "`network_border_group`",
      "service": "`subset`"
    }
  ],
  "ipv6_prefixes": [
    {
      "ipv6_prefix": "`cidr`",
      "region": "`region`",
      "network_border_group": "`network_border_group`",
      "service": "`subset`"
    }
  ]
}
```

**syncToken**

The publication time, in Unix epoch time format.

Type: String

Example: `"syncToken": "1416435608"`

**createDate**

The publication date and time, in UTC YY-MM-DD-hh-mm-ss format.

Type: String

Example: `"createDate": "2014-11-19-23-29-02"`

**prefixes**

The IP prefixes for the IPv4 address ranges.

Type: Array

**ipv6_prefixes**

The IP prefixes for the IPv6 address ranges.

Type: Array

**ip_prefix**

The public IPv4 address range, in CIDR notation. Note that AWS may
advertise a prefix in more specific ranges. For example, prefix
96.127.0.0/17 in the file may be advertised as 96.127.0.0/21, 96.127.8.0/21,
96.127.32.0/19, and 96.127.64.0/18.

Type: String

Example: `"ip_prefix": "198.51.100.2/24"`

**ipv6_prefix**

The public IPv6 address range, in CIDR notation. Note that AWS may
advertise a prefix in more specific ranges.

Type: String

Example: `"ipv6_prefix": "2001:db8:1234::/64"`

**network_border_group**

The name of the network border group, which is a unique set of Availability Zones or Local Zones from which AWS advertises IP addresses, or `GLOBAL`. Traffic for `GLOBAL` services can be attracted to or originate from multiple (up to all) Availability Zones or Local Zones from which AWS advertises IP addresses.

Type: String

Example: `"network_border_group": "us-west-2-lax-1"`

**region**

The AWS Region or `GLOBAL`. Traffic for `GLOBAL` services can be attracted to or originate from multiple (up to all) AWS Regions.

Type: String

Valid values: `af-south-1` | `ap-east-1` | `ap-east-2` |
`ap-northeast-1` | `ap-northeast-2` | `ap-northeast-3` |
`ap-south-1` | `ap-south-2` |
`ap-southeast-1` | `ap-southeast-2` | `ap-southeast-3` | `ap-southeast-4` |
`ap-southeast-5` | `ap-southeast-6` | `ap-southeast-7` |
`ca-central-1` | `ca-west-1` |
`cn-north-1` | `cn-northwest-1` |
`eu-central-1` | `eu-central-2` | `eu-north-1` |
`eu-south-1` | `eu-south-2` |
`eu-west-1` | `eu-west-2` | `eu-west-3` |
`il-central-1` |
`mx-central-1` |
`me-central-1` | `me-south-1` |
`sa-east-1` |
`us-east-1` | `us-east-2` |
`us-gov-east-1` | `us-gov-west-1` |
`us-west-1` | `us-west-2` |
`GLOBAL`

Example: `"region": "us-east-1"`

**service**

The subset of IP address ranges.
The addresses listed for `API_GATEWAY` are egress only.
Specify `AMAZON` to get all IP address ranges (meaning
that every subset is also in the `AMAZON` subset).
However, some IP address ranges are only in the `AMAZON`
subset (meaning that they are not also available in another subset).

Type: String

Valid values: `AMAZON` | `AMAZON_APPFLOW` | `AMAZON_CONNECT` | `API_GATEWAY` |
`AURORA_DSQL` | `CHIME_MEETINGS` | `CHIME_VOICECONNECTOR` | `CLOUD9` |
`CLOUDFRONT` | `CLOUDFRONT_ORIGIN_FACING` | `CODEBUILD` |
`DYNAMODB` |
`EBS` | `EC2` | `EC2_INSTANCE_CONNECT` |
`GLOBALACCELERATOR` | `IVS_LOW_LATENCY` | `IVS_REALTIME` | `KINESIS_VIDEO_STREAMS` | `MEDIA_PACKAGE_V2` |
`ROUTE53` | `ROUTE53_HEALTHCHECKS` | `ROUTE53_HEALTHCHECKS_PUBLISHING` | `ROUTE53_RESOLVER` |
`S3` | `WORKSPACES_GATEWAYS`

Example: `"service": "AMAZON"`

## Range overlaps

The IP address ranges returned by any service code are also returned by the
`AMAZON` service code. For example, all IP address ranges that are
returned by the `S3` service code are also returned by the
`AMAZON` service code.

When service A uses resources from service B, there are IP address ranges that are
returned by the service codes for both service A and service B. However, these IP
address ranges are used exclusively by service A, and can't be used by service B.
For example, Amazon S3 uses resources from Amazon EC2, so there are IP address ranges that are
returned by both the `S3` and `EC2` service codes. However these
IP address ranges are used exclusively by Amazon S3. Therefore, the `S3` service
code returns all IP address ranges that are used exclusively by Amazon S3. To identify the IP
address ranges that are used exclusively by Amazon EC2, find the IP address ranges that are
returned by the `EC2` service code but not the `S3` service code.

## Learn more

This section provides links to additional information for different service codes.

- `AMAZON_APPFLOW` – [IP address ranges](../../../appflow/latest/userguide/general.md "../../../appflow/latest/userguide/general.md")
- `AMAZON_CONNECT` – [Set up your network](../../../connect/latest/adminguide/ccp-networking.md "../../../connect/latest/adminguide/ccp-networking.md")
- `CHIME_MEETINGS` – [Configuring for media and signaling](../../../chime-sdk/latest/dg/network-config.md#media-signaling "../../../chime-sdk/latest/dg/network-config.md#media-signaling")
- `CLOUDFRONT` – [Locations and IP address ranges of CloudFront edge servers](../../../AmazonCloudFront/latest/DeveloperGuide/LocationsOfEdgeServers.md "../../../AmazonCloudFront/latest/DeveloperGuide/LocationsOfEdgeServers.md")
- `DYNAMODB` – [IP address ranges](../../../amazondynamodb/latest/developerguide/AccessingDynamoDB.md#Using.IPRanges "../../../amazondynamodb/latest/developerguide/AccessingDynamoDB.md#Using.IPRanges")
- `EC2` – [Public IPV4 addresses](../../../AWSEC2/latest/UserGuide/using-instance-addressing.md#concepts-public-addresses "../../../AWSEC2/latest/UserGuide/using-instance-addressing.md#concepts-public-addresses")
- `EC2_INSTANCE_CONNECT` – [EC2 Instance Connect prerequisites](../../../AWSEC2/latest/UserGuide/ec2-instance-connect-prerequisites.md#ec2-instance-connect-setup-security-group "../../../AWSEC2/latest/UserGuide/ec2-instance-connect-prerequisites.md#ec2-instance-connect-setup-security-group")
- `GLOBALACCELERATOR` – [Location and IP address ranges of Global Accelerator edge servers](../../../global-accelerator/latest/dg/introduction-ip-ranges.md "../../../global-accelerator/latest/dg/introduction-ip-ranges.md")
- `ROUTE53` – [IP address ranges of Amazon Route 53 servers](../../../Route53/latest/DeveloperGuide/route-53-ip-addresses.md "../../../Route53/latest/DeveloperGuide/route-53-ip-addresses.md")
- `ROUTE53_HEALTHCHECKS` – [IP address ranges of Amazon Route 53 servers](../../../Route53/latest/DeveloperGuide/route-53-ip-addresses.md "../../../Route53/latest/DeveloperGuide/route-53-ip-addresses.md")
- `ROUTE53_HEALTHCHECKS_PUBLISHING` – [IP address ranges of Amazon Route 53 servers](../../../Route53/latest/DeveloperGuide/route-53-ip-addresses.md "../../../Route53/latest/DeveloperGuide/route-53-ip-addresses.md")
- `WORKSPACES_GATEWAYS` – [PCoIP gateway servers](../../../workspaces/latest/adminguide/workspaces-port-requirements.md#gateway_IP "../../../workspaces/latest/adminguide/workspaces-port-requirements.md#gateway_IP")

## Release notes

The following table describes updates to the syntax of `ip-ranges.json`.
We also add new Region codes with each Region launch.

| Description                                                          | Release date       |
| -------------------------------------------------------------------- | ------------------ |
| Added the `IVS_LOW_LATENCY` service code.                            | July 29, 2025      |
| Added the `AURORA_DSQL` service code.                                | May 21, 2025       |
| Added the `IVS_REALTIME` service code.                               | June 11, 2024      |
| Added the `MEDIA_PACKAGE_V2` service code.                           | May 9, 2023        |
| Added the `CLOUDFRONT_ORIGIN_FACING` service code.                   | October 12, 2021   |
| Added the `ROUTE53_RESOLVER` service code.                           | June 24, 2021      |
| Added the `EBS` service code.                                        | May 12, 2021       |
| Added the `KINESIS_VIDEO_STREAMS` service code.                      | November 19, 2020  |
| Added the `CHIME_MEETINGS` and `CHIME_VOICECONNECTOR` service codes. | June 19, 2020      |
| Added the `AMAZON_APPFLOW` service code.                             | June 9, 2020       |
| Add support for the network border group.                            | April 7, 2020      |
| Added the `WORKSPACES_GATEWAYS` service code.                        | March 30, 2020     |
| Added the `ROUTE53_HEALTHCHECK_PUBLISHING` service code.             | January 30, 2020   |
| Added the `API_GATEWAY` service code.                                | September 26, 2019 |
| Added the `EC2_INSTANCE_CONNECT` service code.                       | June 26, 2019      |
| Added the `DYNAMODB` service code.                                   | April 25, 2019     |
| Added the `GLOBALACCELERATOR` service code.                          | December 20, 2018  |
| Added the `AMAZON_CONNECT` service code.                             | June 20, 2018      |
| Added the `CLOUD9` service code.                                     | June 20, 2018      |
| Added the `CODEBUILD` service code.                                  | April 19, 2018     |
| Added the `S3` service code.                                         | February 28, 2017  |
| Added support for IPv6 address ranges.                               | August 22, 2016    |
| Initial release                                                      | November 19, 2014  |
