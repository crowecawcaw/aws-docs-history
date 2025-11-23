# Security policies for REST APIs in API Gateway

A _security policy_ is a predefined combination of minimum TLS version and cipher suites
offered by API Gateway. When your clients establish a TLS handshake to your API or custom domain name, the security
policy enforces the TLS version and cipher suite accepted by API Gateway. Security policies protect your APIs and custom
domain names from network security problems such as tampering and eavesdropping between a client and server.

API Gateway supports legacy security policies and enhanced security policies. `TLS_1_0` and
`TLS_1_2` are legacy security policies. Use these security policies for backwards compatibility. Any
policy that starts with `SecurityPolicy_` is an enhanced security policy. Use these policies for
regulated workloads, advanced governance, or to use post-quantum cryptography. When you use an enhanced security
policy, you must also set the endpoint access mode for additional governance. For more information, see [Endpoint access mode](#apigateway-security-policies-endpoint-access-mode "#apigateway-security-policies-endpoint-access-mode").

## How API Gateway applies security policies

The following example shows how API Gateway applies security policies using the
`SecurityPolicy_TLS13_1_3_2025_09` security policy as an example.

The `SecurityPolicy_TLS13_1_3_2025_09` security policy accepts TLS 1.3 traffic and rejects TLS 1.2
and TLS 1.0 traffic. For TLS 1.3 traffic, the security policy accepts the following cipher suites:

- `TLS_AES_128_GCM_SHA256`
- `TLS_AES_256_GCM_SHA384`
- `TLS_CHACHA20_POLY1305_SHA256`

API Gateway does not accept any other cipher suites. For instance, the security policy would reject any TLS 1.3
traffic that uses the `AES128-SHA` cipher suite. For more information about the supported TLS versions
and ciphers, see [Supported security policies](apigateway-security-policies-list.md "apigateway-security-policies-list.md").

To monitor which TLS protocol and ciphers clients used to access your API Gateway, you can use the
`$context.tlsVersion` and `$context.cipherSuite` context variables in your access logs.
For more information, see [Monitor REST APIs in API Gateway](rest-api-monitor.md "rest-api-monitor.md").

## Endpoint access mode

Endpoint access mode is an additional parameter that you must specify for any REST API or custom domain name
that uses an enhanced security policy that begins with `SecurityPolicy_`. You do this when you create
your resource or if you change the security policy from a legacy policy to an enhanced policy.

When the endpoint access mode is set to `STRICT`, any requests to your REST API or custom domain
name must pass the following checks:

- The request must originate from the same API Gateway endpoint type as your
  resource. This could be from a Regional, an edge-optimized, or a private endpoint.
- If you use a Regional or private endpoint, API Gateway uses SNI host matching. If you use an edge-optimized
  endpoint, API Gateway conforms to CloudFront's domain fronting protection. For more
  information, see
  [Domain
  fronting](../../../AmazonCloudFront/latest/DeveloperGuide/CNAMEs.md#alternate-domain-names-restrictions "../../../AmazonCloudFront/latest/DeveloperGuide/CNAMEs.md#alternate-domain-names-restrictions").

If either of these conditions are not met, API Gateway rejects the request. We recommend that you use
`STRICT` endpoint access mode when possible.

To migrate an existing API or domain name to use strict
endpoint access mode, first update your security policy to an enhanced security policy and keep the endpoint
access mode set to `BASIC`. After you validate your traffic and access logs, set the endpoint access
mode to `STRICT`. When you migrate the endpoint access mode from
`STRICT` to `BASIC`, your endpoint will be unavailable for around 15 minutes as the
changes propagate.

You should not set the endpoint access mode to `STRICT` for certain application architectures and
instead set the endpoint access mode to `BASIC`. The following table shows some
application architectures and a recommendation so your REST API or custom domain name can use `STRICT`
endpoint access mode.

| Architecture                                                                                            | Suggested migration                                                                                                                                                                                                                               |
| ------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Using a VPC endpoint to access a public custom domain name.                                             | This architecture uses cross-endpoint type traffic. We recommend that you migrate to [Custom domain names for private APIs in API Gateway](apigateway-private-custom-domains.md "apigateway-private-custom-domains.md").                          |
| Using any method to invoke a private API that doesn't use a custom domain name or private DNS<br>names. | This architecture creates a mismatch between the host header and the SNI used in the TLS<br>handshake and does not pass CloudFront's domain fronting restrictions. We recommend you migrate your VPC to use private DNS.                          |
| Using domain sharding to distribute content across multiple domains or<br>subdomains.                   | This architecture creates a mismatch between the host header and the SNI used in the TLS<br>handshake and does not pass CloudFront's domain fronting restrictions. We recommend that you use `HTTP/2` and migrate away from this<br>anti-pattern. |

The following are considerations for using endpoint access mode:

- If the endpoint access mode of an API or domain name is `STRICT`, you can't change the endpoint type. To
  change the endpoint type, first change the endpoint access mode to `BASIC`.
- After you change the endpoint access mode from `BASIC` to `STRICT`, there is a 15
  minute delay for API Gateway to enforce the strict endpoint access mode.
- When you change a security policy from a policy that begins with `SecurityPolicy_` to a legacy
  policy, you must unset the endpoint access mode to `""`.

## Considerations

The following are considerations for security policies for REST APIs in API Gateway:

- You can import the security policy in an OpenAPI definition file. For more information, see [x-amazon-apigateway-endpoint-access-mode](openapi-extensions-security-policy.md "openapi-extensions-security-policy.md").
- Your API can be mapped to a custom domain name with a different security policy than your API. When you
  invoke that custom domain name, API Gateway uses the security policy of the API to negotiate the TLS handshake. If
  you disable your default API endpoint, this might affect how callers can invoke your API.
- If you change your security policy, it takes about 15 minutes for the update to complete. You can monitor
  the `apiStatus` of your API. As your API updates, the `apiStatus` is
  `UPDATING` and when it completes, it will be `AVAILABLE`. When your API status is
  `UPDATING`, you can still invoke it.
- API Gateway supports security policies on all APIs. However, you can only choose a security policy for REST
  APIs. API Gateway only supports the `TLS_1_2` security policy for HTTP or WebSocket APIs.
- You can't update the security policy for an API from `TLS_1_0` to `TLS_1_2`.
- Some security policies support both ECDSA and RSA cipher suites. If you use this type of policy with a
  custom domain name, the cipher suites match the customer-provided certificate key type, either RSA or ECDSA.
  If you use this type of policy with a REST API, the cipher suites match the cipher suites compatible with RSA
  certificate types.
