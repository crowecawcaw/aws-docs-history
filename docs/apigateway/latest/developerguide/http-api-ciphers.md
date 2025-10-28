# Security policy for HTTP APIs in API Gateway

API Gateway enforces a security policy of `TLS_1_2` for all HTTP API endpoints.

A _security policy_ is a predefined combination of minimum TLS version and cipher suites
offered by Amazon API Gateway. The TLS protocol addresses network security problems such as tampering and eavesdropping
between a client and server. When your clients establish a TLS handshake to your API through the custom domain, the
security policy enforces the TLS version and cipher suite options your clients can choose to use. This security
policy accepts TLS 1.2 and TLS 1.3 traffic and rejects TLS 1.0 traffic.

## Supported TLS protocols and ciphers for HTTP APIs

The following table describes the supported TLS protocols for HTTP APIs.

| **TLS protocols**             | **TLS_1_2 security policy** |
| ----------------------------- | --------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| TLSv1.3                       | Yes                         |
| TLSv1.2                       | Yes                         | The following table describes the TLS ciphers that are available for the TLS 1_2 security policy for HTTP APIs.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| **TLS ciphers**               | **TLS_1_2 security policy** |
| ---                           | ---                         |
| TLS-AES-128-GCM-SHA256        | Yes                         |
| TLS-AES-256-GCM-SHA384        | Yes                         |
| TLS-CHACHA20-POLY1305-SHA256  | Yes                         |
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
| AES256-SHA256                 | Yes                         | ## OpenSSL and RFC cipher names OpenSSL and IETF RFC 5246 use different names for the same ciphers. For a list of the cipher names, see [OpenSSL and RFC cipher names](apigateway-custom-domain-tls-version.md#apigateway-secure-connections-openssl-rfc-cipher-names "apigateway-custom-domain-tls-version.md#apigateway-secure-connections-openssl-rfc-cipher-names"). ## Information about REST APIs and WebSocket APIs For more information about REST APIs and WebSocket APIs, see [Choose a security policy for your REST API custom domain in API Gateway](apigateway-custom-domain-tls-version.md "apigateway-custom-domain-tls-version.md") and [Security policy for WebSocket APIs in API Gateway](websocket-api-ciphers.md "websocket-api-ciphers.md"). |
