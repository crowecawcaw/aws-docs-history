# Listeners for your VPC Lattice service

Before you start using your VPC Lattice service, you must add a
_listener_. A listener is a process that checks for connection
requests, using the protocol and port that you configure. The rules that you define for a
listener determine how the service routes requests to its registered targets.

![A service with a listener, listener rules, and two target groups.](/images/vpc-lattice/latest/ug/images/service.png)

###### Contents

- [Listener configuration](#listener-configuration "#listener-configuration")
- [HTTP listeners](http-listeners.md "http-listeners.md")
- [HTTPS listeners](https-listeners.md "https-listeners.md")
- [TLS listeners](tls-listeners.md "tls-listeners.md")
- [Listener rules](listener-rules.md "listener-rules.md")
- [Delete a listener](delete-listener.md "delete-listener.md")

## Listener configuration

Listeners support the following protocols and ports:

- **Protocols**: HTTP, HTTPS, TLS
- **Ports**: 1-65535

If the listener protocol is HTTPS, VPC Lattice will provision and manage a TLS
certificate that is associated with the VPC Lattice generated FQDN. VPC Lattice supports TLS
on HTTP/1.1 and HTTP/2. When you configure a service with an HTTPS listener, VPC Lattice
will automatically determine the HTTP protocol using Application-Layer Protocol
Negotiation (ALPN). If ALPN is absent, VPC Lattice defaults to HTTP/1.1. For more
information, see [HTTPS listeners](https-listeners.md "https-listeners.md").

VPC Lattice can listen on HTTP, HTTPS, HTTP/1.1, and HTTP/2 and communicate to targets
in any of these protocols and versions. We do not require that the listener and target
group protocols match. VPC Lattice manages the entire process of upgrading and downgrading
between protocols and versions. For more information, see [Protocol version](target-groups.md#target-group-protocol-version "target-groups.md#target-group-protocol-version").

You can create a TLS listener to ensure that your application decrypts the encrypted
traffic instead of VPC Lattice. For more information, see [TLS listeners](tls-listeners.md "tls-listeners.md").

VPC Lattice does not support WebSockets.
