# Listeners for your Network Load Balancers

A _listener_ is a process that checks for connection requests, using
the protocol and port that you configure. Before you start using your Network Load Balancer, you must add
at least one listener. If your load balancer has no listeners, it can't receive traffic
from clients. The rule that you define for a listener determines how the load balancer
routes requests to the targets that you register, such as EC2 instances.

###### Contents

- [Listener configuration](#listener-configuration "#listener-configuration")
- [Default actions](#default-actions "#default-actions")
- [Listener attributes](#listener-attributes "#listener-attributes")
- [Secure listeners](#secure-listeners "#secure-listeners")
- [ALPN policies](#alpn-policies "#alpn-policies")
- [Create a listener](create-listener.md "create-listener.md")
- [Server certificates](tls-listener-certificates.md "tls-listener-certificates.md")
- [Security policies](describe-ssl-policies.md "describe-ssl-policies.md")
- [Update a listener](listener-update-rules.md "listener-update-rules.md")
- [Update idle timeout](update-idle-timeout.md "update-idle-timeout.md")
- [Update a TLS listener](listener-update-certificates.md "listener-update-certificates.md")
- [Delete a listener](delete-listener.md "delete-listener.md")

## Listener configuration

Listeners support the following protocols and ports:

- **Protocols**: TCP, TLS, UDP, TCP_UDP, QUIC, TCP_QUIC
- **Ports**: 1-65535

You can use a TLS listener to offload the work of encryption and decryption to your
load balancer so that your applications can focus on their business logic. If the
listener protocol is TLS, you must deploy at least one SSL server certificate on the
listener. For more information, see [Server certificates](tls-listener-certificates.md "tls-listener-certificates.md").

If you must ensure that the targets decrypt TLS traffic instead of the load balancer,
you can create a TCP listener on port 443 instead of creating a TLS listener. With a
TCP listener, the load balancer passes encrypted traffic through to the targets without
decrypting it.

You can use a QUIC listener to accept QUIC traffic. The Network Load Balancer acts as a pass through load balancer in accordance
with [RFC9000](https://tools.ietf.org/html/rfc9000 "https://tools.ietf.org/html/rfc9000"). Utilize a QUIC listener and QUIC enabled backends
to enable seamless connection migration for mobile devices.

To support both TCP and UDP on the same port, create a TCP_UDP listener. The target
groups for a TCP_UDP listener must use the TCP_UDP protocol.

To support both TCP and QUIC on the same port, create a TCP_QUIC listener. The target
groups for a TCP_QUIC listener must use the TCP_QUIC protocol.

A UDP listener for a dualstack load balancer requires IPv6 target groups.

WebSockets is supported only on TCP, TLS, TCP_UDP, and TCP_QUIC listeners.

QUIC traffic does not support version negotiation. QUIC v1 is the only supported QUIC version.

All network traffic sent to a configured listener is classified as intended traffic.
Network traffic that does not match a configured listener is classified as unintended
traffic. ICMP requests other than Type 3 are also considered unintended traffic. Network Load Balancers
drop unintended traffic without forwarding it to any targets. TCP data packets sent to
the listener port for a configured listeners that are not new connections or part of an
active TCP connection are rejected with a TCP reset (RST).

For more information, see [Request
routing](../userguide/how-elastic-load-balancing-works.md#request-routing "../userguide/how-elastic-load-balancing-works.md#request-routing") in the _Elastic Load Balancing User Guide_.

## Default actions

When you create a listener, you specify a default action for routing requests.
The default action forwards requests to the target groups that you specify.

###### Distribute traffic to multiple target groups

If you specify multiple target groups for a default action, requests are
distributed to these target groups based on their relative weights. You
must specify a weight from 0 to 999 for each target group. A target group
with a weight of 0 receives no traffic. After you add a target group or
update the target group weights, new connections are routed based on the
new target group weights. Existing connections are not affected and continue
until they are closed as usual.

As an example, if you specify two target groups, each with a weight of 10, each
target group receives half the requests. If you specify two target groups, one
with a weight of 10 and the other with a weight of 20, the target group with a
weight of 20 receives twice as many requests as the target group with a weight
of 10.

A common use case is migrating traffic from one target group to another.
Meaning that you gradually increase the weight of the new target group while
decreasing the weight of the original target group until it is 0. If you update
the weight of a target group to 0, after a short period of time, it receives no new
connections and existing connections are closed.

###### Sticky sessions and weighted target groups

Forward actions on listeners can specify whether to enable target group stickiness.
When enabled, target group stickiness causes subsequent connections from the same source IP
address to prefer the previously chosen target group.

###### Considerations

- For TLS listeners, you can't add both TCP target groups and TLS target
  groups to the listener rule. All target groups must use the same protocol.
- For TLS listeners, target group stickiness is not supported.
- For dualstack load balancers, you can't add both IPv4 target groups and
  IPv6 target groups to the same default action. All target groups in the default action
  must use the same IP address type.
- For listeners, if a forward action contains multiple target groups and any of them
  have stickiness enabled, then the forward action must also have target group stickiness enabled.

## Listener attributes

The following are the listener attributes for Network Load Balancers:

`tcp.idle_timeout.seconds`

The tcp idle timeout value, in seconds. The valid range is 60-6000 seconds.
The default is 350 seconds.

For more information, see [Update idle timeout](update-idle-timeout.md "update-idle-timeout.md").

## Secure listeners

To use a TLS listener, you must deploy at least one server certificate on your load
balancer. The load balancer uses a server certificate to terminate the front-end
connection and then to decrypt requests from clients before sending them to the targets.
Note that if you need to pass encrypted traffic to the targets without the load balancer
decrypting it, create a TCP listener on port 443 instead of creating a TLS listener. The
load balancer passes the request to the target as is, without decrypting it.

Elastic Load Balancing uses a TLS negotiation configuration, known as a security policy, to negotiate
TLS connections between a client and the load balancer. A security policy is a
combination of protocols and ciphers. The protocol establishes a secure connection
between a client and a server and ensures that all data passed between the client and
your load balancer is private. A cipher is an encryption algorithm that uses encryption
keys to create a coded message. Protocols use several ciphers to encrypt data over the
internet. During the connection negotiation process, the client and the load balancer
present a list of ciphers and protocols that they each support, in order of preference.
The first cipher on the server's list that matches any one of the client's ciphers is
selected for the secure connection.

Network Load Balancers do not support mutual TLS authentication (mTLS). For mTLS
support, create a TCP listener instead of a TLS listener. The load balancer passes the
request through as is, so you can implement mTLS on the target.

Network Load Balancers support TLS resumption using PSK for TLS 1.3, and session tickets for
TLS 1.2 and older. Resumptions with session ID, or when multiple certificates
are configured in the listener using SNI, are not supported. The 0-RTT data feature
and early_data extension are not implemented.

For related demos, see [TLS Support on Network Load Balancer](https://exampleloadbalancer.com/nlbtls_demo.html "https://exampleloadbalancer.com/nlbtls_demo.html")
and [SNI Support on Network Load Balancer](https://exampleloadbalancer.com/nlbsni_demo.html "https://exampleloadbalancer.com/nlbsni_demo.html").

## ALPN policies

Application-Layer Protocol Negotiation (ALPN) is a TLS extension that is sent on
the initial TLS handshake hello messages. ALPN enables the application layer to
negotiate which protocols should be used over a secure connection, such as HTTP/1
and HTTP/2.

When the client initiates an ALPN connection, the load balancer compares the
client ALPN preference list with its ALPN policy. If the client supports a protocol
from the ALPN policy, the load balancer establishes the connection based on the
preference list of the ALPN policy. Otherwise, the load balancer does not use
ALPN.

###### Supported ALPN Policies

The following are the supported ALPN policies:

`HTTP1Only`

Negotiate only HTTP/1.\*. The ALPN preference list is http/1.1,
http/1.0.

`HTTP2Only`

Negotiate only HTTP/2. The ALPN preference list is h2.

`HTTP2Optional`

Prefer HTTP/1.\* over HTTP/2 (which can be useful for HTTP/2 testing).
The ALPN preference list is http/1.1, http/1.0, h2.

`HTTP2Preferred`

Prefer HTTP/2 over HTTP/1.\*. The ALPN preference list is h2, http/1.1,
http/1.0.

`None`

Do not negotiate ALPN. This is the default.

###### Enable ALPN Connections

You can enable ALPN connections when you create or modify a TLS listener. For
more information, see [Add a listener](create-listener.md#add-listener "create-listener.md#add-listener") and [Update the ALPN policy](listener-update-certificates.md#update-alpn-policy "listener-update-certificates.md#update-alpn-policy").
