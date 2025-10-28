# Considerations for AWS IoT Managed integrations VPC endpoints

Before you set up an interface VPC endpoint for AWS IoT Managed integrations, review
[Interface endpoint properties and limitations](../../../vpc/latest/privatelink/vpce-interface.md#vpce-interface-limitations "../../../vpc/latest/privatelink/vpce-interface.md#vpce-interface-limitations") in the
_AWS PrivateLink Guide_.

AWS IoT Managed integrations supports making calls to all of its API actions from your VPC through interface VPC endpoints.

## Supported endpoints

AWS IoT Managed integrations supports VPC endpoints for the following service interfaces:

- **Control plane API**: `com.amazonaws.region.iotmanagedintegrations.api`

## Unsupported endpoints

The following AWS IoT Managed integrations endpoints do not support VPC endpoints:

- **MQTT endpoints**: MQTT devices are typically deployed in end-user environments rather than within AWS VPCs, making AWS PrivateLink integration unnecessary.
- **OAuth callback endpoints**: Many third-party platforms do not operate within AWS infrastructure,
  reducing the benefits of AWS PrivateLink support for OAuth flows.

## Availability

AWS IoT Managed integrations VPC endpoints are available in the following AWS Regions:

- Canada (Central) - ca-central-1
- Europe (Ireland) - eu-west-1

Additional regions will be supported as AWS IoT Managed integrations expands its availability.

## Dual-stack support

AWS IoT Managed integrations VPC endpoints support both IPv4 and IPv6 traffic. You can create VPC endpoints with the following IP address types:

- **IPv4**: Assigns IPv4 addresses to endpoint network interfaces
- **IPv6**: Assigns IPv6 addresses to endpoint network interfaces (requires IPv6-only subnets)
- **Dualstack**: Assigns both IPv4 and IPv6 addresses to endpoint network interfaces
