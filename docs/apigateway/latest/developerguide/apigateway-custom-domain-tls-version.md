# Choose a security policy for

your REST API custom domain in API Gateway

For greater security of your Amazon API Gateway custom domain, you can choose a security policy in
the API Gateway console, the AWS CLI, or an AWS SDK.

A _security policy_ is a predefined combination of minimum TLS version and cipher suites
offered by API Gateway. You can choose either a TLS version 1.2 or TLS version 1.0 security policy. The TLS protocol addresses network security problems such as tampering and eavesdropping
between a client and server. When your clients establish a TLS handshake to your API through the custom domain, the
security policy enforces the TLS version and cipher suite options your clients can choose to use.

In custom domain settings, a security policy determines two settings:

- The minimum TLS version that API Gateway uses to communicate with API clients
- The cipher that API Gateway uses to encrypt the content that it returns to API
  clients
  If you choose a TLS 1.0 security policy, the security policy accepts TLS 1.0, TLS 1.1, TLS 1.2, and TLS 1.3 traffic. If
  you choose a TLS 1.2 security policy, the security policy accepts TLS 1.2 and TLS 1.3 traffic and rejects TLS 1.0
  traffic.

###### Note

You can only specify a security policy for a custom domain. For an API using a default endpoint, API Gateway
uses the following security policy:

- For edge-optimized APIs: `TLS-1-0`
- For Regional APIs: `TLS-1-0`
- For private APIs: `TLS-1-2`
  The ciphers for each security policy are described in the following tables on this page.

###### Topics

- [How to specify a
  security policy for custom domains](#apigateway-custom-domain-tls-version-how-to "#apigateway-custom-domain-tls-version-how-to")
- [Supported
  security policies, TLS protocol versions, and ciphers for edge-optimized custom domains](#apigateway-custom-domain-tls-version-edge-optimized "#apigateway-custom-domain-tls-version-edge-optimized")
- [Supported
  security policies, TLS protocol versions, and ciphers for Regional custom domains](#apigateway-custom-domain-tls-version-regional-and-websocket "#apigateway-custom-domain-tls-version-regional-and-websocket")
- [Supported TLS protocol versions and ciphers for private APIs](#apigateway-private-api-ciphers "#apigateway-private-api-ciphers")
- [OpenSSL and
  RFC cipher names](#apigateway-secure-connections-openssl-rfc-cipher-names "#apigateway-secure-connections-openssl-rfc-cipher-names")
- [Information about HTTP APIs and WebSocket APIs](#apigateway-rest-additional-apis "#apigateway-rest-additional-apis")

## How to specify a

security policy for custom domains

When you create a custom domain name, you specify the security policy for it. To learn how to create a custom
domain, see [Set up an edge-optimized custom domain name in API Gateway](how-to-edge-optimized-custom-domain-name.md "how-to-edge-optimized-custom-domain-name.md") or [Set up a Regional custom
domain name in API Gateway](apigateway-regional-api-custom-domain-create.md "apigateway-regional-api-custom-domain-create.md").

To change the security policy of your custom domain name, update the custom domain settings. You can update your
custom domain name settings using the AWS Management Console, the AWS CLI, or an AWS SDK.

When you use the API Gateway REST API or
AWS CLI, specify the new TLS version, `TLS_1_0` or `TLS_1_2` in the
`securityPolicy` parameter. For more information, see [domainname:update](../api/API_UpdateDomainName.md "../api/API_UpdateDomainName.md") in the _Amazon API Gateway REST API Reference_ or [update-domain-name](../../../cli/latest/reference/apigateway/update-domain-name.md "../../../cli/latest/reference/apigateway/update-domain-name.md") in the _AWS CLI Reference_.

The update operation may take few minutes to complete.

## Supported

security policies, TLS protocol versions, and ciphers for edge-optimized custom domains

The following table describes the security policies that can be specified for edge-optimized custom domain names.

| **TLS protocols** | **TLS_1_0 security policy** | **TLS_1_2 security policy** |
| ----------------- | --------------------------- | --------------------------- |
| TLSv1.3           | Yes                         | Yes                         |
| TLSv1.2           | Yes                         | Yes                         |
| TLSv1.1           | Yes                         | No                          |
| TLSv1             | Yes                         | No                          |

The following table describes the TLS ciphers that are available for each security policy.

| **TLS ciphers**               | **TLS_1_0 security policy** | **TLS_1_2 security policy** |
| ----------------------------- | --------------------------- | --------------------------- |
| TLS_AES_128_GCM_SHA256        | Yes                         | Yes                         |
| TLS_AES_256_GCM_SHA384        | Yes                         | Yes                         |
| TLS_CHACHA20_POLY1305_SHA256  | Yes                         | Yes                         |
| ECDHE-ECDSA-AES128-GCM-SHA256 | Yes                         | Yes                         |
| ECDHE-ECDSA-AES128-SHA256     | Yes                         | Yes                         |
| ECDHE-ECDSA-AES128-SHA        | Yes                         | No                          |
| ECDHE-ECDSA-AES256-GCM-SHA384 | Yes                         | Yes                         |
| ECDHE-ECDSA-CHACHA20-POLY1305 | Yes                         | Yes                         |
| ECDHE-ECDSA-AES256-SHA384     | Yes                         | Yes                         |
| ECDHE-ECDSA-AES256-SHA        | Yes                         | No                          |
| ECDHE-RSA-AES128-GCM-SHA256   | Yes                         | Yes                         |
| ECDHE-RSA-AES128-SHA256       | Yes                         | Yes                         |
| ECDHE-RSA-AES128-SHA          | Yes                         | No                          |
| ECDHE-RSA-AES256-GCM-SHA384   | Yes                         | Yes                         |
| ECDHE-RSA-CHACHA20-POLY1305   | Yes                         | Yes                         |
| ECDHE-RSA-AES256-SHA384       | Yes                         | Yes                         |
| ECDHE-RSA-AES256-SHA          | Yes                         | No                          |
| AES128-GCM-SHA256             | Yes                         | No                          |
| AES256-GCM-SHA384             | Yes                         | Yes                         |
| AES128-SHA256                 | Yes                         | Yes                         |
| AES256-SHA                    | Yes                         | No                          |
| AES128-SHA                    | Yes                         | No                          |
| DES-CBC3-SHA                  | Yes                         | No                          |

## Supported

security policies, TLS protocol versions, and ciphers for Regional custom domains

The following table describes the security policies for Regional custom domain names.

| **TLS protocols** | **TLS_1_0 security policy** | **TLS_1_2 security policy** |
| ----------------- | --------------------------- | --------------------------- |
| TLSv1.3           | Yes                         | Yes                         |
| TLSv1.2           | Yes                         | Yes                         |
| TLSv1.1           | Yes                         | No                          |
| TLSv1             | Yes                         | No                          |

The following table describes the TLS ciphers that are available for each security policy.

| **TLS ciphers**               | **TLS_1_0 security policy** | **TLS_1_2 security policy** |
| ----------------------------- | --------------------------- | --------------------------- |
| TLS_AES_128_GCM_SHA256        | Yes                         | Yes                         |
| TLS_AES_256_GCM_SHA384        | Yes                         | Yes                         |
| TLS_CHACHA20_POLY1305_SHA256  | Yes                         | Yes                         |
| ECDHE-ECDSA-AES128-GCM-SHA256 | Yes                         | Yes                         |
| ECDHE-RSA-AES128-GCM-SHA256   | Yes                         | Yes                         |
| ECDHE-ECDSA-AES128-SHA256     | Yes                         | Yes                         |
| ECDHE-RSA-AES128-SHA256       | Yes                         | Yes                         |
| ECDHE-ECDSA-AES128-SHA        | Yes                         | No                          |
| ECDHE-RSA-AES128-SHA          | Yes                         | No                          |
| ECDHE-ECDSA-AES256-GCM-SHA384 | Yes                         | Yes                         |
| ECDHE-RSA-AES256-GCM-SHA384   | Yes                         | Yes                         |
| ECDHE-ECDSA-AES256-SHA384     | Yes                         | Yes                         |
| ECDHE-RSA-AES256-SHA384       | Yes                         | Yes                         |
| ECDHE-RSA-AES256-SHA          | Yes                         | No                          |
| ECDHE-ECDSA-AES256-SHA        | Yes                         | No                          |
| AES128-GCM-SHA256             | Yes                         | Yes                         |
| AES128-SHA256                 | Yes                         | Yes                         |
| AES128-SHA                    | Yes                         | No                          |
| AES256-GCM-SHA384             | Yes                         | Yes                         |
| AES256-SHA256                 | Yes                         | Yes                         |
| AES256-SHA                    | Yes                         | No                          |

## Supported TLS protocol versions and ciphers for private APIs

The following table describes the supported TLS protocols for private APIs. Specifying a security policy for private APIs is not supported.

| **TLS protocols** | **TLS_1_2 security policy** |
| ----------------- | --------------------------- |
| TLSv1.2           | Yes                         |

The following table describes the TLS ciphers that are available for the `TLS_1_2` security policy for private APIs.

| **TLS ciphers**               | **TLS_1_2 security policy** |
| ----------------------------- | --------------------------- |
| ECDHE-ECDSA-AES128-GCM-SHA256 | Yes                         |
| ECDHE-RSA-AES128-GCM-SHA256   | Yes                         |
| ECDHE-ECDSA-AES128-SHA256     | Yes                         |
| ECDHE-RSA-AES128-SHA256       | Yes                         |
| ECDHE-ECDSA-AES256-GCM-SHA384 | Yes                         |
| ECDHE-RSA-AES256-GCM-SHA384   | Yes                         |
| ECDHE-ECDSA-AES256-SHA384     | Yes                         |
| ECDHE-RSA-AES256-SHA384       | Yes                         |
| AES128-GCM-SHA256             | Yes                         |
| AES128-SHA256                 | Yes                         |
| AES256-GCM-SHA384             | Yes                         |
| AES256-SHA256                 | Yes                         |

## OpenSSL and

RFC cipher names

OpenSSL and IETF RFC 5246 use different names
for the same ciphers. The following table maps the OpenSSL name to the RFC name for
each cipher. For more information, see
[ciphers](https://docs.openssl.org/1.1.1/man1/ciphers/ "https://docs.openssl.org/1.1.1/man1/ciphers/") in the OpenSSL Documentation.

| **OpenSSL cipher name**      | **RFC cipher name**                   |
| ---------------------------- | ------------------------------------- |
| TLS_AES_128_GCM_SHA256       | TLS_AES_128_GCM_SHA256                |
| TLS_AES_256_GCM_SHA384       | TLS_AES_256_GCM_SHA384                |
| TLS_CHACHA20_POLY1305_SHA256 | TLS_CHACHA20_POLY1305_SHA256          |
| ECDHE-RSA-AES128-GCM-SHA256  | TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256 |
| ECDHE-RSA-AES128-SHA256      | TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA256 |
| ECDHE-RSA-AES128-SHA         | TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA    |
| ECDHE-RSA-AES256-GCM-SHA384  | TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384 |
| ECDHE-RSA-AES256-SHA384      | TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA384 |
| ECDHE-RSA-AES256-SHA         | TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA    |
| AES128-GCM-SHA256            | TLS_RSA_WITH_AES_128_GCM_SHA256       |
| AES256-GCM-SHA384            | TLS_RSA_WITH_AES_256_GCM_SHA384       |
| AES128-SHA256                | TLS_RSA_WITH_AES_128_CBC_SHA256       |
| AES256-SHA                   | TLS_RSA_WITH_AES_256_CBC_SHA          |
| AES128-SHA                   | TLS_RSA_WITH_AES_128_CBC_SHA          |
| DES-CBC3-SHA                 | TLS_RSA_WITH_3DES_EDE_CBC_SHA         |

## Information about HTTP APIs and WebSocket APIs

For more information about HTTP APIs and WebSocket APIs, see [Security policy for HTTP APIs in API Gateway](http-api-ciphers.md "http-api-ciphers.md")
and [Security policy for WebSocket APIs in API Gateway](websocket-api-ciphers.md "websocket-api-ciphers.md").
