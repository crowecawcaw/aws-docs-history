# Amazon EC2 service endpoints

An endpoint is a URL that serves as an entry point for an AWS web service. Amazon EC2 supports the
following endpoint types:

- [IPv4 endpoints](#ipv4 "#ipv4")
- [Dual-stack endpoints](#ipv6 "#ipv6") (support both IPv4 and IPv6)
- [FIPS endpoints](../../../general/latest/gr/rande.md#FIPS-endpoints "../../../general/latest/gr/rande.md#FIPS-endpoints")
  When you make a request, you can specify the endpoint to use. If you do not specify an endpoint,
  the IPv4 endpoint is used by default. To use a different endpoint type, you must specify it in your
  request. For examples of how to do this, see [Specifying endpoints](#examples "#examples").
  For a table of available endpoints, see [Service endpoints by Region](#service-endpoints "#service-endpoints").

## IPv4 endpoints

IPv4 endpoints support IPv4 traffic only. IPv4 endpoints are available for all Regions.

If you specify the general endpoint, `ec2.amazonaws.com`, we use the endpoint
for `us-east-1`. To use a different Region, specify its associated endpoint. For
example, if you specify `ec2.us-east-2.amazonaws.com` as the endpoint, we
direct your request to the `us-east-2` endpoint.

IPv4 endpoint names use the following naming convention:

- ``service`.`region`.amazonaws.com`

For example, the IPv4 endpoint name for the `eu-west-1` Region is
`ec2.eu-west-1.amazonaws.com`.

## Dual-stack (IPv4 and IPv6) endpoints

Dual-stack endpoints support both IPv4 and IPv6 traffic. When you make a request to a dual-stack
endpoint, the endpoint URL resolves to an IPv6 or an IPv4 address, depending on the protocol used by
your network and client.

Amazon EC2 supports only regional dual-stack endpoints, which means that you must specify the Region as part
of the endpoint name. Dual-stack endpoint names use the following naming convention:

- `ec2.`region`.api.aws`

For example, the dual-stack endpoint name for the `eu-west-1` Region is
`ec2.eu-west-1.api.aws`.

## Service endpoints by Region

The following are the service endpoints for Amazon EC2. For more information about Regions, see
[Regions and Availability Zones](../../../AWSEC2/latest/UserGuide/using-regions-availability-zones.md "../../../AWSEC2/latest/UserGuide/using-regions-availability-zones.md")
in the _Amazon EC2 User Guide_.

| Region Name                | Region         | Endpoint                                                                                          | Protocol                         |
| -------------------------- | -------------- | ------------------------------------------------------------------------------------------------- | -------------------------------- |
| US East (Ohio)             | us-east-2      | ec2.us-east-2.amazonaws.com<br>ec2-fips.us-east-2.amazonaws.com<br>ec2.us-east-2.api.aws          | HTTP and HTTPS<br>HTTPS<br>HTTPS |
| US East (N. Virginia)      | us-east-1      | ec2.us-east-1.amazonaws.com<br>ec2-fips.us-east-1.amazonaws.com<br>ec2.us-east-1.api.aws          | HTTP and HTTPS<br>HTTPS<br>HTTPS |
| US West (N. California)    | us-west-1      | ec2.us-west-1.amazonaws.com<br>ec2-fips.us-west-1.amazonaws.com<br>ec2.us-west-1.api.aws          | HTTP and HTTPS<br>HTTPS<br>HTTPS |
| US West (Oregon)           | us-west-2      | ec2.us-west-2.amazonaws.com<br>ec2-fips.us-west-2.amazonaws.com<br>ec2.us-west-2.api.aws          | HTTP and HTTPS<br>HTTPS<br>HTTPS |
| Africa (Cape Town)         | af-south-1     | ec2.af-south-1.amazonaws.com<br>ec2.af-south-1.api.aws                                            | HTTP and HTTPS<br>HTTPS          |
| Asia Pacific (Hong Kong)   | ap-east-1      | ec2.ap-east-1.amazonaws.com<br>ec2.ap-east-1.api.aws                                              | HTTP and HTTPS<br>HTTPS          |
| Asia Pacific (Hyderabad)   | ap-south-2     | ec2.ap-south-2.amazonaws.com                                                                      | HTTPS                            |
| Asia Pacific (Jakarta)     | ap-southeast-3 | ec2.ap-southeast-3.amazonaws.com                                                                  | HTTPS                            |
| Asia Pacific (Malaysia)    | ap-southeast-5 | ec2.ap-southeast-5.amazonaws.com                                                                  | HTTPS                            |
| Asia Pacific (Melbourne)   | ap-southeast-4 | ec2.ap-southeast-4.amazonaws.com                                                                  | HTTPS                            |
| Asia Pacific (Mumbai)      | ap-south-1     | ec2.ap-south-1.amazonaws.com<br>ec2.ap-south-1.api.aws                                            | HTTP and HTTPS<br>HTTPS          |
| Asia Pacific (New Zealand) | ap-southeast-6 | ec2.ap-southeast-6.amazonaws.com                                                                  | HTTPS                            |
| Asia Pacific (Osaka)       | ap-northeast-3 | ec2.ap-northeast-3.amazonaws.com                                                                  | HTTP and HTTPS                   |
| Asia Pacific (Seoul)       | ap-northeast-2 | ec2.ap-northeast-2.amazonaws.com<br>ec2.ap-northeast-2.api.aws                                    | HTTP and HTTPS<br>HTTPS          |
| Asia Pacific (Singapore)   | ap-southeast-1 | ec2.ap-southeast-1.amazonaws.com<br>ec2.ap-southeast-1.api.aws                                    | HTTP and HTTPS<br>HTTPS          |
| Asia Pacific (Sydney)      | ap-southeast-2 | ec2.ap-southeast-2.amazonaws.com<br>ec2.ap-southeast-2.api.aws                                    | HTTP and HTTPS<br>HTTPS          |
| Asia Pacific (Taipei)      | ap-east-2      | ec2.ap-east-2.amazonaws.com                                                                       | HTTPS                            |
| Asia Pacific (Thailand)    | ap-southeast-7 | ec2.ap-southeast-7.amazonaws.com                                                                  | HTTPS                            |
| Asia Pacific (Tokyo)       | ap-northeast-1 | ec2.ap-northeast-1.amazonaws.com<br>ec2.ap-northeast-1.api.aws                                    | HTTP and HTTPS<br>HTTPS          |
| Canada (Central)           | ca-central-1   | ec2.ca-central-1.amazonaws.com<br>ec2-fips.ca-central-1.amazonaws.com<br>ec2.ca-central-1.api.aws | HTTP and HTTPS<br>HTTPS<br>HTTPS |
| Canada West (Calgary)      | ca-west-1      | ec2.ca-west-1.amazonaws.com<br>ec2-fips.ca-west-1.amazonaws.com                                   | HTTPS<br>HTTPS                   |
| Europe (Frankfurt)         | eu-central-1   | ec2.eu-central-1.amazonaws.com<br>ec2.eu-central-1.api.aws                                        | HTTP and HTTPS<br>HTTPS          |
| Europe (Ireland)           | eu-west-1      | ec2.eu-west-1.amazonaws.com<br>ec2.eu-west-1.api.aws                                              | HTTP and HTTPS<br>HTTPS          |
| Europe (London)            | eu-west-2      | ec2.eu-west-2.amazonaws.com<br>ec2.eu-west-2.api.aws                                              | HTTP and HTTPS<br>HTTPS          |
| Europe (Milan)             | eu-south-1     | ec2.eu-south-1.amazonaws.com<br>ec2.eu-south-1.api.aws                                            | HTTP and HTTPS<br>HTTPS          |
| Europe (Paris)             | eu-west-3      | ec2.eu-west-3.amazonaws.com<br>ec2.eu-west-3.api.aws                                              | HTTP and HTTPS<br>HTTPS          |
| Europe (Spain)             | eu-south-2     | ec2.eu-south-2.amazonaws.com                                                                      | HTTPS                            |
| Europe (Stockholm)         | eu-north-1     | ec2.eu-north-1.amazonaws.com<br>ec2.eu-north-1.api.aws                                            | HTTP and HTTPS<br>HTTPS          |
| Europe (Zurich)            | eu-central-2   | ec2.eu-central-2.amazonaws.com                                                                    | HTTPS                            |
| Israel (Tel Aviv)          | il-central-1   | ec2.il-central-1.amazonaws.com                                                                    | HTTPS                            |
| Mexico (Central)           | mx-central-1   | ec2.mx-central-1.amazonaws.com                                                                    | HTTPS                            |
| Middle East (Bahrain)      | me-south-1     | ec2.me-south-1.amazonaws.com<br>ec2.me-south-1.api.aws                                            | HTTP and HTTPS<br>HTTPS          |
| Middle East (UAE)          | me-central-1   | ec2.me-central-1.amazonaws.com                                                                    | HTTPS                            |
| South America (São Paulo)  | sa-east-1      | ec2.sa-east-1.amazonaws.com<br>ec2.sa-east-1.api.aws                                              | HTTP and HTTPS<br>HTTPS          |
| AWS GovCloud (US-East)     | us-gov-east-1  | ec2.us-gov-east-1.amazonaws.com<br>ec2.us-gov-east-1.api.aws                                      | HTTPS<br>HTTPS                   |
| AWS GovCloud (US-West)     | us-gov-west-1  | ec2.us-gov-west-1.amazonaws.com<br>ec2.us-gov-west-1.api.aws                                      | HTTPS<br>HTTPS                   |

## Specifying endpoints

This section provides some examples of how to specify an endpoint when making a request.

AWS CLI
The following examples show how to specify an endpoint for the
`us-east-2` Region using the AWS CLI.

- **Dual-stack**

```
aws ec2 describe-regions --region us-east-2 --endpoint-url https://`ec2.us-east-2.api.aws`
```

- **IPv4**

```
aws ec2 describe-regions --region us-east-2 --endpoint-url https://`ec2.us-east-2.amazonaws.com`
```

AWS SDK for Java 2.x
The following examples show how to specify an endpoint for the
`us-east-2` Region using the AWS SDK for Java 2.x.

- **Dual-stack**

```
Ec2Client client = Ec2Client.builder()
    .region(Region.US_EAST_2)
    .endpointOverride(URI.create("https://`ec2.us-east-2.api.aws`"))
    .build();
```

- **IPv4**

```
Ec2Client client = Ec2Client.builder()
    .region(Region.US_EAST_2)
    .endpointOverride(URI.create("https://`ec2.us-east-2.amazonaws.com`"))
    .build();
```

AWS SDK for Java 1.x
The following examples show how to specify an endpoint for the
`eu-west-1` Region using the AWS SDK for Java 1.x.

- **Dual-stack**

```
AmazonEC2 s3 = AmazonEC2ClientBuilder.standard()
     .withEndpointConfiguration(new EndpointConfiguration(
          "https://`ec2.eu-west-1.api.aws`",
          "eu-west-1"))
     .build();
```

- **IPv4**

```
AmazonEC2 s3 = AmazonEC2ClientBuilder.standard()
     .withEndpointConfiguration(new EndpointConfiguration(
          "https://`ec2.eu-west-1.amazonaws.com`",
          "eu-west-1"))
     .build();
```

AWS SDK for Go
The following examples show how to specify an endpoint for the
`us-east-1` Region using the AWS SDK for Go.

- **Dual-stack**

```
sess := session.Must(session.NewSession())
svc := ec2.New(sess, &aws.Config{
    Region: aws.String(endpoints.UsEast1RegionID),
    Endpoint: aws.String("https://`ec2.us-east-1.api.aws`")
})
```

- **IPv4**

```
sess := session.Must(session.NewSession())
svc := ec2.New(sess, &aws.Config{
    Region: aws.String(endpoints.UsEast1RegionID),
    Endpoint: aws.String("https://`ec2.us-east-1.amazonaws.com`")
})
```
