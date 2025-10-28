# Access Lightsail

You can access Amazon Lightsail using a variety of interfaces and service endpoints.

###### Topics

- [Lightsail service interfaces](#access-lightsail-interfaces "#access-lightsail-interfaces")
- [Lightsail service endpoints](#lightsail-endpoints "#lightsail-endpoints")
- [Examples of specifying an endpoint](#specify-endpoint-examples "#specify-endpoint-examples")

## Lightsail service interfaces

You can create and manage your Lightsail resources with the following interfaces.

**Amazon Lightsail console**

A simple web interface to create and manage Lightsail instances and
resources. If you've signed up for an AWS account, you can either access the [Lightsail console](https://lightsail.aws.amazon.com/ "https://lightsail.aws.amazon.com/") directly or sign into the
AWS Management Console and choose **Lightsail** from the console home
page.

**AWS Command Line Interface**

Enables you to interact with AWS services using commands in your
command-line shell. It is supported on Windows, Mac, and Linux. For more
information about the AWS CLI, see [AWS Command Line Interface User Guide](../../../cli/latest/userguide.md "../../../cli/latest/userguide.md"). You can find the Lightsail
commands in the [Lightsail section of the AWS CLI Command Reference](../../../cli/latest/reference/lightsail.md#cli-aws-lightsail "../../../cli/latest/reference/lightsail.md#cli-aws-lightsail").

**AWS CloudShell**

CloudShell is a browser-based, pre-authenticated shell that you can launch
directly from the AWS Management Console. You can run AWS CLI commands using your preferred
shell, such as Bash, PowerShell, or Z shell. For
examples of how to use AWS CloudShell to manage your Lightsail resources, see [Manage Lightsail resources with
AWS CloudShell](amazon-lightsail-cloudshell.md "amazon-lightsail-cloudshell.md").

**Query API**

Lightsail provides a Query API. These requests are HTTP or HTTPS requests
that use the HTTP verbs GET or POST and a Query parameter named
`Action`. For more information about the API actions for
Lightsail, see [Actions](../../2016-11-28/api-reference/API_Operations.md "../../2016-11-28/api-reference/API_Operations.md") in the _Amazon Lightsail API
Reference_.

**AWS SDKs**

If you prefer to build applications using language-specific APIs instead of
submitting a request over HTTP or HTTPS, AWS provides libraries, sample code,
tutorials, and other resources for software developers. These libraries provide
basic functions that automate tasks such as cryptographically signing your
requests, retrying requests, and handling error responses, making it easier for
you to get started. For more information, see [Tools to Build on
AWS](https://aws.amazon.com/developer/tools/ "https://aws.amazon.com/developer/tools/").

**AWS Tools for PowerShell**

A set of PowerShell modules that are built on the functionality exposed by the
SDK for .NET. The Tools for PowerShell enable you to script operations on your AWS resources from
the PowerShell command line. To get started, see the [AWS Tools for PowerShell User Guide](../../../powershell/latest/userguide.md "../../../powershell/latest/userguide.md"). You can find
the cmdlets for Lightsail, in the [AWS Tools for PowerShell Cmdlet Reference](../../../powershell/latest/reference/Index.md "../../../powershell/latest/reference/Index.md").

## Lightsail service endpoints

An endpoint is a URL that serves as an entry point for an AWS web service. For programmatic access methods in the previously described interfaces,
Lightsail supports the following endpoint types:

- [IPv4 endpoints](#ipv4-endpoints "#ipv4-endpoints")
- [Dual-stack endpoints](#dual-stack-endpoints "#dual-stack-endpoints") (support both IPv4 and
  IPv6)

When you make a request, you can specify the endpoint to use. If you do not specify an
endpoint, the IPv4 endpoint is used by default. To use a different endpoint type, you
must specify it in your request.

### IPv4 endpoints

IPv4 endpoints support IPv4 traffic only. IPv4 endpoints are available for all
Regions. For more information about the regional service endpoints, see
[Service endpoints by Region](#service-endpoints "#service-endpoints").

IPv4 endpoint names use the following naming convention:

- ``service`.`region`.amazonaws.com`

For example, the IPv4 endpoint name for the `us-east-2` Region is
`lightsail.us-east-2.amazonaws.com`.

### Dual-stack (IPv4 and IPv6) endpoints

Dual-stack endpoints support both IPv4 and IPv6 traffic. When you make a request
to a dual-stack endpoint, the endpoint URL resolves to an IPv6 or an IPv4 address,
depending on the protocol used by your network and client.

- `lightsail.`region`.api.aws`

For example, the dual-stack endpoint name for the `us-east-2` Region is
`lightsail.us-east-2.api.aws`.

### Service endpoints by Region

The following are the service endpoints for Lightsail. For more information
about the Regions available for Lightsail, see [Regions and
Availability Zones for Lightsail](understanding-regions-and-availability-zones-in-amazon-lightsail.md "understanding-regions-and-availability-zones-in-amazon-lightsail.md").

| Region Name              | Region         | Endpoint                                                                | Protocol    |
| ------------------------ | -------------- | ----------------------------------------------------------------------- | ----------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| US East (Ohio)           | us-east-2      | lightsail.us-east-2.amazonaws.com lightsail.us-east-2.api.aws           | HTTPS HTTPS |
| US East (N. Virginia)    | us-east-1      | lightsail.us-east-1.amazonaws.com lightsail.us-east-1.api.aws           | HTTPS HTTPS |
| US West (Oregon)         | us-west-2      | lightsail.us-west-2.amazonaws.com lightsail.us-west-2.api.aws           | HTTPS HTTPS |
| Asia Pacific (Jakarta)   | ap-southeast-3 | lightsail.ap-southeast-3.amazonaws.com lightsail.ap-southeast-3.api.aws | HTTPS HTTPS |
| Asia Pacific (Mumbai)    | ap-south-1     | lightsail.ap-south-1.amazonaws.com lightsail.ap-south-1.api.aws         | HTTPS HTTPS |
| Asia Pacific (Seoul)     | ap-northeast-2 | lightsail.ap-northeast-2.amazonaws.com lightsail.ap-northeast-2.api.aws | HTTPS HTTPS |
| Asia Pacific (Singapore) | ap-southeast-1 | lightsail.ap-southeast-1.amazonaws.com lightsail.ap-southeast-1.api.aws | HTTPS HTTPS |
| Asia Pacific (Sydney)    | ap-southeast-2 | lightsail.ap-southeast-2.amazonaws.com lightsail.ap-southeast-2.api.aws | HTTPS HTTPS |
| Asia Pacific (Tokyo)     | ap-northeast-1 | lightsail.ap-northeast-1.amazonaws.com lightsail.ap-northeast-1.api.aws | HTTPS HTTPS |
| Canada (Central)         | ca-central-1   | lightsail.ca-central-1.amazonaws.com lightsail.ca-central-1.api.aws     | HTTPS HTTPS |
| Europe (Frankfurt)       | eu-central-1   | lightsail.eu-central-1.amazonaws.com lightsail.eu-central-1.api.aws     | HTTPS HTTPS |
| Europe (Ireland)         | eu-west-1      | lightsail.eu-west-1.amazonaws.com lightsail.eu-west-1.api.aws           | HTTPS HTTPS |
| Europe (London)          | eu-west-2      | lightsail.eu-west-2.amazonaws.com lightsail.eu-west-2.api.aws           | HTTPS HTTPS |
| Europe (Paris)           | eu-west-3      | lightsail.eu-west-3.amazonaws.com lightsail.eu-west-3.api.aws           | HTTPS HTTPS |
| Europe (Stockholm)       | eu-north-1     | lightsail.eu-north-1.amazonaws.com lightsail.eu-north-1.api.aws         | HTTPS HTTPS | ## Examples of specifying an endpoint This section provides some examples of how to specify an endpoint when making a request. ###### Note If you do not specify an endpoint, the IPv4 endpoint is used by default. AWS CLI The following examples show how to specify an endpoint for the `us-east-2` Region using the AWS CLI. <br>• **IPv4** `` aws lightsail get-regions --region us-east-2 --endpoint-url https://`lightsail.us-east-2.amazonaws.com` `` <br>• **Dual-stack** `` aws lightsail get-regions --region us-east-2 --endpoint-url https://`lightsail.us-east-2.api.aws` `` AWS SDK for Java 2.x The following examples show how to specify an endpoint for the `us-east-2` Region using the AWS SDK for Java 2.x. <br>• **IPv4** ``LightsailClient client = LightsailClient.builder() .region(Region.US_EAST_2) .endpointOverride(URI.create("https://`lightsail.us-east-2.amazonaws.com`")) .build();`` <br>• **Dual-stack** ``LightsailClient client = LightsailClient.builder() .region(Region.US_EAST_2) .endpointOverride(URI.create("https://`lightsail.us-east-2.api.aws`")) .build();`` AWS SDK for Java 1.x The following examples show how to specify an endpoint for the `us-east-2` Region using the AWS SDK for Java 1.x. <br>• **IPv4** ``AmazonLightsail lightsail = AmazonLightsailClientBuilder.standard() .withEndpointConfiguration(new EndpointConfiguration( "https://`lightsail.us-east-2.amazonaws.com`", "us-east-2")) .build();`` <br>• **Dual-stack** ``AmazonLightsail lightsail = AmazonLightsailClientBuilder.standard() .withEndpointConfiguration(new EndpointConfiguration( "https://`lightsail.us-east-2.api.aws`", "us-east-2")) .build();`` AWS SDK for Go The following examples show how to specify an endpoint for the `us-east-2` Region using the AWS SDK for Go. <br>• **IPv4** ``sess := session.Must(session.NewSession()) svc := lightsail.New(sess, &aws.Config{ Region: aws.String(endpoints.UsEast2RegionID), Endpoint: aws.String("https://`lightsail.us-east-2.amazonaws.com`") })`` <br>• **Dual-stack** ``sess := session.Must(session.NewSession()) svc := lightsail.New(sess, &aws.Config{ Region: aws.String(endpoints.UsEast2RegionID), Endpoint: aws.String("https://`lightsail.us-east-2.api.aws`") })`` |
