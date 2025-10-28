# Service endpoints for Recycle Bin

An _endpoint_ is a URL that serves as an entry point for an AWS web service.
Recycle Bin supports the following endpoint types:

- IPv4 endpoints
- Dual-stack endpoints that support both IPv4 and IPv6
- FIPS endpoints
  When you make a request, you can specify the endpoint and Region to use. If you do not specify an
  endpoint, the IPv4 endpoint is used by default. To use a different endpoint type, you must specify
  it in your request. For examples of how to do this, see [Specifying endpoints](#rbin-endpoint-examples "#rbin-endpoint-examples").

For the Recycle Bin, see [Recycle Bin endpoints](../../../general/latest/gr/rbin.md#rbin_region "../../../general/latest/gr/rbin.md#rbin_region") in the _Amazon Web Services General Reference_.

###### Topics

- [IPv4 endpoints](#ipv4 "#ipv4")
- [Dual-stack (IPv4 and IPv6) endpoints](#rbin-ipv6 "#rbin-ipv6")
- [FIPS endpoints](#rbin-fips "#rbin-fips")
- [Specifying endpoints](#rbin-endpoint-examples "#rbin-endpoint-examples")

## IPv4 endpoints

IPv4 endpoints support IPv4 traffic only. IPv4 endpoints are available for all Regions.

You must specify the Region as part of the endpoint name. The endpoint names use the following
naming convention:

- rbin.`region`.amazonaws.com

For example, the IPv4 endpoint for the US East (N. Virginia) Region is
`rbin.us-east-1.amazonaws.com`.

## Dual-stack (IPv4 and IPv6) endpoints

Dual-stack endpoints support both IPv4 and IPv6 traffic. Dual-stack endpoints are available
for all Regions.

To use IPv6, you must use a dual-stack endpoint. When you make a request to a dual-stack
endpoint, the endpoint URL resolves to an IPv6 or an IPv4 address, depending on the protocol
used by your network and client.

You must specify the Region as part of the endpoint name. Dual-stack endpoint names use the
following naming convention:

- `rbin.`region`.api.aws`

For example, the dual-stack endpoint for the US East (N. Virginia) Region is
`rbin.us-east-1.api.aws`.

## FIPS endpoints

Recycle Bin provides FIPS-validated IPv4 and dual-stack (IPv4 and IPv6) endpoints for
the following Regions:

- `us-east-1` — US East (N. Virginia)
- `us-east-2` — US East (Ohio)
- `us-west-1` — US West (N. California)
- `us-west-2` — US West (Oregon)
- `ca-central-1` — Canada (Central)
- `ca-west-1` — Canada West (Calgary)
- `us-gov-east-1` — AWS GovCloud (US-East)
- `us-gov-west-1` — AWS GovCloud (US-West)

**FIPS IPv4 endpoints** use the following naming convention:
`rbin-fips.`region`.amazonaws.com`. For example, the FIPS IPv4
endpoint for the US East (N. Virginia) Region is `rbin-fips.us-east-1.amazonaws.com`.

**FIPS dual-stack endpoints** use the following naming convention:
`rbin-fips.`region`.api.aws`. For example, the FIPS dual-stack
endpoint for the US East (N. Virginia) Region is `rbin-fips.us-east-1.api.aws`.

## Specifying endpoints

The following examples show how to specify an endpoint for the `us-east-2` Region using the AWS CLI.

- **Dual-stack**

```
aws rbin get-rule \
--identifier `rule_id` \
**--endpoint-url https://`rbin.us-east-2.api.aws`**
```

- **IPv4**

```
aws rbin get-rule \
--identifier `rule_id` \
**--endpoint-url https://`rbin.us-east-2.amazonaws.com`**
```
