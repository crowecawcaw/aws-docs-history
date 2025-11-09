# HTTP header modification for your Application Load Balancer

HTTP header modification is supported by Application Load Balancers, for both request and response
headers. Without having to update your application code, header modification
allows you more control over your application's traffic and security.

To enable header modification, see [Enable header modification](enable-header-modification.md "enable-header-modification.md").

## Rename mTLS/TLS headers

The header rename capability allows you to configure the names of the mTLS
and TLS headers that the Application Load Balancer generates and adds to requests.

This ability to modify HTTP headers enables your Application Load Balancer to easily support
applications that use specifically formatted request and response headers.

| Header                               | Description                                                                                                                                                                                                                                                        |
| ------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| X-Amzn-Mtls-Clientcert-Serial-Number | Ensures that the target can identify and<br>verify the specific certificate presented by<br>the client during the TLS handshake.                                                                                                                                   |
| X-Amzn-Mtls-Clientcert-Issuer        | Helps the target validate and authenticate<br>the client certificate by identifying the<br>certificate authority that issued the certificate.                                                                                                                      |
| X-Amzn-Mtls-Clientcert-Subject       | Provides the target with detailed information about the entity<br>the client certificate was issued to, which helps in identification,<br>authentication, authorization, and logging during mTLS<br>authentication.                                                |
| X-Amzn-Mtls-Clientcert-Validity      | Allows the target to verify that the client certificate being<br>used is within its defined validity period, ensuring the<br>certificate is not expired or prematurely used.                                                                                       |
| X-Amzn-Mtls-Clientcert-Leaf          | Provides the client certificate used in the mTLS handshake,<br>allowing the server to authenticate the client and validate<br>the certificate chain. This ensures the connection is secure and<br>authorized.                                                      |
| X-Amzn-Mtls-Clientcert               | Carries the full client certificate. Allowing the target<br>to verify the certificate’s authenticity, validate the<br>certificate chain, and authenticate the client during the<br>mTLS handshake process.                                                         |
| X-Amzn-TLS-Version                   | Indicates the version of the TLS protocol used for a<br>connection. It facilitates determining the security level<br>of the communication, troubleshoot connection issues and<br>ensuring compliance.                                                              |
| X-Amzn-TLS-Cipher-Suite              | Indicates the combination of cryptographic algorithms<br>used to secure a connection in TLS. This allows the server<br>to assess the security of the connection, helping with<br>compatibility troubleshooting, and ensuring compliance<br>with security policies. |

## Add response headers

Using insert headers, you can configure your Application Load Balancer to add security-related headers
to responses. With these attributes, you can insert headers including HSTS, CORS,
and CSP.

By default, these headers are empty. When this happens, the Application Load Balancer does not modify this
response header.

When you enable a response header, the Application Load Balancer adds the header with the configured value
to all responses. If the response from target includes the HTTP response header, the load
balancer updates the header value to be the configured value. Otherwise, the load balancer
adds the HTTP response header to the response with the configured value.

| Header                           | Description                                                                                                                                                                                                                                                   |
| -------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Strict-Transport-Security        | Enforces HTTPS-only connections by the browser for a specified duration,<br>helping to protect against man-in-the-middle attacks, protocol downgrades<br>and user errors. ensuring all communications between the client and target<br>is encrypted.          |
| Access-Control-Allow-Origin      | Controls whether resources on a target can be accessed from different<br>origins. This allows secure cross-origin interactions while preventing<br>unauthorized access.                                                                                       |
| Access-Control-Allow-Methods     | Specifies the HTTP methods that are allowed when making cross-origin<br>requests to the target. It provides control over which actions can be<br>performed from different origins.                                                                            |
| Access-Control-Allow-Headers     | Specifies which custom or non-simple headers can be included in a cross-origin<br>request. This header gives targets control over which headers can be sent by<br>clients from different origins.                                                             |
| Access-Control-Allow-Credentials | Specifies whether the client should include credentials such as cookies,<br>HTTP authentication or client certificates in cross-origin requests.                                                                                                              |
| Access-Control-Expose-Headers    | Allows the target to specify which additional response headers can be<br>access by the client in cross-origin requests.                                                                                                                                       |
| Access-Control-Max-Age           | Defines how long the browser can cache the result of a preflight request,<br>reducing the need for repeated preflight checks. This helps to optimize<br>performance by reducing the number of OPTIONS requests required for certain<br>cross-origin requests. |
| Content-Security-Policy          | Security feature that prevents code injection attacks like XSS by controlling<br>which resources such as scripts, styles, images, etc. can be loaded and executed<br>by a website.                                                                            |
| X-Content-Type-Options           | With the no-sniff directive, enhances web security by preventing browsers from<br>guessing the MIME type of a resource. It ensures that browsers only interpret<br>content according to the declared Content-Type                                             |
| X-Frame-Options                  | Header security mechanism that helps prevent click-jacking attacks by controlling<br>whether a web page can be embedded in frames. Values such as DENY and SAMEORIGIN<br>can ensure that content is not embedded on malicious or untrusted websites.          |

## Disable headers

Using disable headers, you can configure your Application Load Balancer to disable the
`server:awselb/2.0` header from the responses. This reduces
exposure of server specific information, while adding an extra
layer of protection to your application.

The attribute name is
`routing.http.response.server.enabled`. The available
values are `true` or `false`. The default
value is `true`.

## Limitations

- Header values can contain the following characters
  - Alphanumeric characters: `a-z`, `A-Z`, and `0-9`
  - Special characters: `_ :;.,\/'?!(){}[]@<>=-+*#&`|~^%`

- The value for the attribute can not exceed 1K bytes in size.
- Elastic Load Balancing performs basic input validations to verify
  the header value is valid. However the validation is unable
  to confirm if the value is supported for a specific header.
- Setting an empty value for any attribute will cause the
  Application Load Balancer to revert to the default behavior.
