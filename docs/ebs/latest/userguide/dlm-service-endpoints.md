# Service endpoints for Amazon Data Lifecycle Manager

An _endpoint_ is a URL that serves as an entry point for an AWS web service.
Amazon Data Lifecycle Manager supports the following endpoint types:

- IPv4 endpoints
- Dual-stack endpoints that support both IPv4 and IPv6
- FIPS endpoints
  When you make a request, you can specify the endpoint and Region to use. If you do not specify an
  endpoint, the IPv4 endpoint is used by default. To use a different endpoint type, you must specify
  it in your request. For examples of how to do this, see [Specifying endpoints](#dlm-endpoint-examples "#dlm-endpoint-examples").

For the Amazon Data Lifecycle Manager, see [Amazon Data Lifecycle Manager endpoints](../../../general/latest/gr/dlm.md "../../../general/latest/gr/dlm.md") in the _Amazon Web Services General Reference_.

###### Topics

- [IPv4 endpoints](#dlm-ipv4 "#dlm-ipv4")
- [Dual-stack (IPv4 and IPv6) endpoints](#dlm-ipv6 "#dlm-ipv6")
- [FIPS endpoints](#dlm-fips "#dlm-fips")
- [Specifying endpoints](#dlm-endpoint-examples "#dlm-endpoint-examples")

## IPv4 endpoints

IPv4 endpoints support IPv4 traffic only. IPv4 endpoints are available for all Regions.

You must specify the Region as part of the endpoint name. The endpoint names use the following
naming convention:

- dlm.`region`.amazonaws.com

For example, the IPv4 endpoint for the US East (N. Virginia) Region is
`dlm.us-east-1.amazonaws.com`.

## Dual-stack (IPv4 and IPv6) endpoints

Dual-stack endpoints support both IPv4 and IPv6 traffic. Dual-stack endpoints are available
for all Regions.

To use IPv6, you must use a dual-stack endpoint. When you make a request to a dual-stack
endpoint, the endpoint URL resolves to an IPv6 or an IPv4 address, depending on the protocol
used by your network and client.

You must specify the Region as part of the endpoint name. Dual-stack endpoint names use the
following naming convention:

- `dlm.`region`.api.aws`

For example, the dual-stack endpoint for the US East (N. Virginia) Region is
`dlm.us-east-1.api.aws`.

## FIPS endpoints

Amazon Data Lifecycle Manager provides FIPS-validated dual-stack (IPv4 and IPv6) endpoints for the following Regions:

- `us-east-1` — US East (N. Virginia)
- `us-east-2` — US East (Ohio)
- `us-west-1` — US West (N. California)
- `us-west-2` — US West (Oregon)
- `ca-central-1` — Canada (Central)
- `ca-west-1` — Canada West (Calgary)

FIPS dual-stack endpoints use the following naming convention:
`dlm-fips.`region`.api.aws`. For example, the FIPS dual-stack
endpoint for the US East (N. Virginia) Region is `dlm-fips.us-east-1.api.aws`.

## Specifying endpoints

The following examples show how to specify an endpoint for the `US East (N. Virginia)` Region using the AWS CLI.

- **Dual-stack**

```
aws dlm create-default-role \
--resource-type snapshot \
**--endpoint-url https://`dlm.us-east-2.api.aws`**
```

- **IPv4**

```
aws dlm create-default-role \
--resource-type snapshot \
**--endpoint-url https://`dlm.us-east-2.amazonaws.com`**
```
