

# Considerations for AWS IoT Managed Integrations VPC endpoints
<a name="vpc-endpoints-considerations"></a>

Before you set up an interface VPC endpoint for AWS IoT Managed Integrations, review [ Interface endpoint properties and limitations](https://docs.aws.amazon.com/vpc/latest/privatelink/vpce-interface.html#vpce-interface-limitations) in the *AWS PrivateLink Guide*.

AWS IoT Managed Integrations supports making calls to all of its API actions from your VPC through interface VPC endpoints.

## Supported endpoints
<a name="vpc-endpoints-supported"></a>

AWS IoT Managed Integrations supports VPC endpoints for the following service interfaces:
+ **Control plane API**: `com.amazonaws.region.iotmanagedintegrations.api`

## Unsupported endpoints
<a name="vpc-endpoints-unsupported"></a>

The following AWS IoT Managed Integrations endpoints do not support VPC endpoints:
+ **MQTT endpoints**: MQTT devices are typically deployed in end-user environments rather than within AWS VPCs, making AWS PrivateLink integration unnecessary.
+ **OAuth callback endpoints**: Many third-party platforms do not operate within AWS infrastructure, reducing the benefits of AWS PrivateLink support for OAuth flows.

## Availability
<a name="vpc-endpoints-availability"></a>

AWS IoT Managed Integrations VPC endpoints are available in the following AWS Regions:
+ Canada (Central) - ca-central-1
+ Europe (Ireland) - eu-west-1

Additional regions will be supported as AWS IoT Managed Integrations expands its availability.

## Dual-stack support
<a name="vpc-endpoints-dual-stack"></a>

AWS IoT Managed Integrations VPC endpoints support both IPv4 and IPv6 traffic. You can create VPC endpoints with the following IP address types:
+ **IPv4**: Assigns IPv4 addresses to endpoint network interfaces
+ **IPv6**: Assigns IPv6 addresses to endpoint network interfaces (requires IPv6-only subnets)
+ **Dualstack**: Assigns both IPv4 and IPv6 addresses to endpoint network interfaces