# Listeners for your Application Load Balancers

A _listener_ is a process that checks for connection requests, using
the protocol and port that you configure. Before you start using your Application Load Balancer, you must add at
least one listener. If your load balancer has no listeners, it can't receive traffic from
clients. The rules that you define for your listeners determine how the load balancer routes
requests to the targets that you register, such as EC2 instances.

###### Contents

- [Listener configuration](#listener-configuration "#listener-configuration")
- [Listener attributes](#listener-attributes "#listener-attributes")
- [Default action](#default-action "#default-action")
- [Create an HTTP listener](create-listener.md "create-listener.md")
- [SSL certificates](https-listener-certificates.md "https-listener-certificates.md")
- [Security policies](describe-ssl-policies.md "describe-ssl-policies.md")
- [Create an HTTPS listener](create-https-listener.md "create-https-listener.md")
- [Update an HTTPS listener](listener-update-certificates.md "listener-update-certificates.md")
- [Listener rules](listener-rules.md "listener-rules.md")
- [Mutual TLS authentication](mutual-authentication.md "mutual-authentication.md")
- [User authentication](listener-authenticate-users.md "listener-authenticate-users.md")
- [X-forwarded headers](x-forwarded-headers.md "x-forwarded-headers.md")
- [HTTP header modification](header-modification.md "header-modification.md")
- [Delete a listener](delete-listener.md "delete-listener.md")

## Listener configuration

Listeners support the following protocols and ports:

- **Protocols**: HTTP, HTTPS
- **Ports**: 1-65535

You can use an HTTPS listener to offload the work of encryption and decryption to your
load balancer so that your applications can focus on their business logic. If the
listener protocol is HTTPS, you must deploy at least one SSL server certificate on the
listener. For more information, see [Create an HTTPS listener for your Application Load Balancer](create-https-listener.md "create-https-listener.md").

If you must ensure that the targets decrypt HTTPS traffic instead of the load balancer,
you can create a Network Load Balancer with a TCP listener on port 443. With a TCP listener, the load
balancer passes encrypted traffic through to the targets without decrypting it. For more
information, see the [User Guide for Network Load Balancers](../network.md "../network.md").

###### WebSockets

Application Load Balancers provide native support for WebSockets. You can upgrade an existing HTTP/1.1
connection into a WebSocket (`ws` or `wss`) connection by using an
HTTP connection upgrade. When you upgrade, the TCP connection used for requests (to the
load balancer as well as to the target) becomes a persistent WebSocket connection
between the client and the target through the load balancer. You can use WebSockets with
both HTTP and HTTPS listeners. The options that you choose for your listener apply to
WebSocket connections as well as to HTTP traffic. For more information, see [How the WebSocket Protocol Works](../../../AmazonCloudFront/latest/DeveloperGuide/distribution-working-with.md#distribution-working-with.websockets.how-it-works "../../../AmazonCloudFront/latest/DeveloperGuide/distribution-working-with.md#distribution-working-with.websockets.how-it-works") in the
_Amazon CloudFront Developer Guide_.

###### HTTP/2

Application Load Balancers provide native support for HTTP/2 with HTTPS listeners. You can send up to 128
requests in parallel using one HTTP/2 connection. You can use the protocol version to
send the request to the targets using HTTP/2. For more information, see [Protocol version](load-balancer-target-groups.md#target-group-protocol-version "load-balancer-target-groups.md#target-group-protocol-version"). Because HTTP/2 uses front-end
connections more efficiently, you might notice fewer connections between clients and the
load balancer. You can't use the server-push feature of HTTP/2.

Mutual TLS authentication for Application Load Balancers supports HTTP/2 in both passthrough and verify modes. For more information, see
[Mutual authentication with TLS in Application Load Balancer](mutual-authentication.md "mutual-authentication.md").

For more information, see [Request
routing](../userguide/how-elastic-load-balancing-works.md#request-routing "../userguide/how-elastic-load-balancing-works.md#request-routing") in the _Elastic Load Balancing User Guide_.

## Listener attributes

The following are the listener attributes for Application Load Balancers:

`routing.http.request.x_amzn_mtls_clientcert_serial_number.header_name`

Enables you to modify the header name of the
**X-Amzn-Mtls-Clientcert-Serial-Number** HTTP request header.

`routing.http.request.x_amzn_mtls_clientcert_issuer.header_name`

Enables you to modify the header name of the
**X-Amzn-Mtls-Clientcert-Issuer** HTTP request header.

`routing.http.request.x_amzn_mtls_clientcert_subject.header_name`

Enables you to modify the header name of the
**X-Amzn-Mtls-Clientcert-Subject** HTTP request header.

`routing.http.request.x_amzn_mtls_clientcert_validity.header_name`

Enables you to modify the header name of the
**X-Amzn-Mtls-Clientcert-Validity** HTTP request header.

`routing.http.request.x_amzn_mtls_clientcert_leaf.header_name`

Enables you to modify the header name of the
**X-Amzn-Mtls-Clientcert-Leaf** HTTP request header.

`routing.http.request.x_amzn_mtls_clientcert.header_name`

Enables you to modify the header name of the
**X-Amzn-Mtls-Clientcert** HTTP request header.

`routing.http.request.x_amzn_tls_version.header_name`

Enables you to modify the header name of the
**X-Amzn-Tls-Version** HTTP request header.

`routing.http.request.x_amzn_tls_cipher_suite.header_name`

Enables you to modify the header name of the
**X-Amzn-Tls-Cipher-Suite** HTTP request header.

`routing.http.response.server.enabled`

Enables you to allow or remove the HTTP response server header.

`routing.http.response.strict_transport_security.header_value`

Informs browsers that the site should only be accessed using
HTTPS, and that any future attempts to access it using HTTP should
automatically be converted to HTTPS.

`routing.http.response.access_control_allow_origin.header_value`

Specifies which origins are allowed to access the server.

`routing.http.response.access_control_allow_methods.header_value`

Returns which HTTP methods are allowed when accessing the server
from a different origin.

`routing.http.response.access_control_allow_headers.header_value`

Specifies which headers can be used during the request.

`routing.http.response.access_control_allow_credentials.header_value`

Indicates whether the browser should include credentials such as
cookies or authentication when making requests.

`routing.http.response.access_control_expose_headers.header_value`

Returns which headers the browser can expose to the requesting client.

`routing.http.response.access_control_max_age.header_value`

Specifies how long the results of a preflight request can be cached,
in seconds.

`routing.http.response.content_security_policy.header_value`

Specifies restrictions enforced by the browser to help minimize the
risk of certain types of security threats.

`routing.http.response.x_content_type_options.header_value`

Indicates whether the MIME types advertised in the
**Content-Type** headers should be followed and not be changed.

`routing.http.response.x_frame_options.header_value`

Indicates whether the browser is allowed to render a page in a
**frame**, **iframe**,
**embed** or **object**.

## Default action

Every listener has a default action, also known as the default rule. The default
rule can't be deleted and is always performed last. You can create additional rules.
These rules consist of a priority, one or more actions, and one or more conditions.
You can add or edit rules at any time. For more information, see [Listener rules](listener-rules.md "listener-rules.md").
