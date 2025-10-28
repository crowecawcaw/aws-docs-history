# Service endpoints for EBS direct APIs

An _endpoint_ is a URL that serves as an entry point for an AWS web service.
EBS direct APIs supports the following endpoint types:

- IPv4 endpoints
- Dual-stack endpoints that support both IPv4 and IPv6
- FIPS endpoints
  When you make a request, you can specify the endpoint and Region to use. If you do not specify an
  endpoint, the IPv4 endpoint is used by default. To use a different endpoint type, you must specify it
  in your request. For examples of how to do this, see [Specifying endpoints](#examples "#examples").

For more information about Regions, see [Regions and Availability Zones](../../../AWSEC2/latest/UserGuide/using-regions-availability-zones.md "../../../AWSEC2/latest/UserGuide/using-regions-availability-zones.md") in the _Amazon EC2 User Guide_. For a list of
endpoints for EBS direct APIs, see [Endpoints for the EBS direct APIs](../../../general/latest/gr/ebs-service.md#ebs_direct_apis "../../../general/latest/gr/ebs-service.md#ebs_direct_apis") in the _Amazon Web Services General Reference_.

###### Topics

- [IPv4 endpoints](#ipv4 "#ipv4")
- [Dual-stack (IPv4 and IPv6) endpoints](#ipv6 "#ipv6")
- [FIPS endpoints](#fips "#fips")
- [Specifying endpoints](#examples "#examples")

## IPv4 endpoints

IPv4 endpoints support IPv4 traffic only. IPv4 endpoints are available for all Regions.

EBS direct APIs supports only Regional IPv4 endpoints that you can use to make your requests. You must
specify the Region as part of the endpoint name. The endpoint names use the following naming convention:

- `ebs.`region`.amazonaws.com`

For example, to direct your requests to the `us-east-2` IPv4
endpoint, you must specify `ebs.us-east-2.amazonaws.com` as the endpoint. For a
list of endpoints for EBS direct APIs, see [Endpoints for the EBS direct APIs](../../../general/latest/gr/ebs-service.md#ebs_direct_apis "../../../general/latest/gr/ebs-service.md#ebs_direct_apis") in the _Amazon Web Services General Reference_.

###### Pricing

You are not charged for data transferred directly between EBS direct APIs and Amazon EC2
instances using an IPv4 endpoint in the same Region. However, if there are intermediate
services, such as AWS PrivateLink endpoints, NAT Gateway, or Amazon VPC Transit Gateways, you are
charged their associated costs.

## Dual-stack (IPv4 and IPv6) endpoints

Dual-stack endpoints support both IPv4 and IPv6 traffic. Dual-stack endpoints are available
for all Regions.

To use IPv6, you must use a dual-stack endpoint. When you make a request to a dual-stack
endpoint, the endpoint URL resolves to an IPv6 or an IPv4 address, depending on the protocol
used by your network and client.

EBS direct APIs supports only regional dual-stack endpoints, which means that you must specify the
Region as part of the endpoint name. Dual-stack endpoint names use the following naming
convention:

- `ebs.`region`.api.aws`

For example, the dual-stack endpoint name for the `eu-west-1` Region is
`ebs.eu-west-1.api.aws`. For a list of endpoints for EBS direct APIs, see
[Endpoints
for the EBS direct APIs](../../../general/latest/gr/ebs-service.md#ebs_direct_apis "../../../general/latest/gr/ebs-service.md#ebs_direct_apis") in the _Amazon Web Services General Reference_.

###### Pricing

You are not charged for data transferred directly between EBS direct APIs and Amazon EC2
instances using a dual-stack endpoint in the same Region. However, if there are
intermediate services, such as AWS PrivateLink endpoints, NAT Gateway, or Amazon VPC Transit Gateways,
you are charged their associated costs.

## FIPS endpoints

EBS direct APIs provides FIPS-validated IPv4 and dual-stack (IPv4 and IPv6) endpoints for
the following Regions:

- `us-east-1` — US East (N. Virginia)
- `us-east-2` — US East (Ohio)
- `us-west-1` — US West (N. California)
- `us-west-2` — US West (Oregon)
- `ca-central-1` — Canada (Central)
- `ca-west-1` — Canada West (Calgary)

**FIPS IPv4 endpoints** use the following naming convention:
`ebs-fips.`region`.amazonaws.com`. For example, the FIPS IPv4
endpoint for `us-east-1` is `ebs-fips.us-east-1.amazonaws.com`.

**FIPS dual-stack endpoints** use the following naming convention:
`ebs-fips.`region`.api.aws`. For example, the FIPS dual-stack
endpoint for `us-east-1` is `ebs-fips.us-east-1.api.aws`.

For more information about FIPS endpoints see, [FIPS endpoints](../../../general/latest/gr/rande.md#FIPS-endpoints "../../../general/latest/gr/rande.md#FIPS-endpoints") in the _Amazon Web Services General Reference_.

## Specifying endpoints

This section provides some examples of how to specify an endpoint when making a request.

AWS CLI
The following examples show how to specify an endpoint for the
`us-east-2` Region using the AWS CLI.

- **Dual-stack**

```
aws ebs list-snapshot-blocks --snapshot-id snap-0987654321 --starting-block-index 1000 --endpoint-url https://`ebs.us-east-2.api.aws`
```

- **IPv4**

```
aws ebs list-snapshot-blocks --snapshot-id snap-0987654321 --starting-block-index 1000 --endpoint-url https://`ebs.us-east-2.amazonaws.com`
```

AWS SDK for Java 2.x
The following examples show how to specify an endpoint for the
`us-east-2` Region using the AWS SDK for Java 2.x.

- **Dual-stack**

```
AwsClientBuilder.EndpointConfiguration config = new AwsClientBuilder.EndpointConfiguration("https://`ebs.us-east-2.api.aws`", "`us-east-2`");
AmazonEBS ebs = AmazonEBSClientBuilder.standard()
    .withEndpointConfiguration(config)
    .build();
```

- **IPv4**

```
AwsClientBuilder.EndpointConfiguration config = new AwsClientBuilder.EndpointConfiguration("https://`ebs.us-east-2.amazonaws.com`", "`us-east-2`");
AmazonEBS ebs = AmazonEBSClientBuilder.standard()
    .withEndpointConfiguration(config)
    .build();
```

AWS SDK for Go
The following examples show how to specify an endpoint for the
`us-east-2` Region using the AWS SDK for Go.

- **Dual-stack**

```
sess := session.Must(session.NewSession())
svc := ebs.New(sess, &aws.Config{
    Region: aws.String(endpoints.UsEast2RegionID),
    Endpoint: aws.String("https://`ebs.us-east-2.api.aws`")
})
```

- **IPv4**

```
sess := session.Must(session.NewSession())
svc := ebs.New(sess, &aws.Config{
    Region: aws.String(endpoints.UsEast2RegionID),
    Endpoint: aws.String("https://`ebs.us-east-2.amazonaws.com`")
})
```
