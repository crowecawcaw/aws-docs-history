# Considerations when

working with TLS inspection configurations in AWS Network Firewall

Before you implement TLS inspection configuration in Network Firewall, understand the following considerations and limitations.

###### Conditions for dropping traffic

Network Firewall drops non-TLS traffic that matches the conditions of the TLS inspection configuration scope
configuration. For example, if the TLS inspection configuration scope configuration includes `port
 80` as `plain HTTP`, Network Firewall drops this traffic because the
service can't identify it as TLS traffic. Network Firewall also drops TLS traffic if the
client hello message in the TLS handshake doesn't include a server name, or if the
server name that's presented in the client hello doesn't match the server name
indication (SNI) that's presented in the downstream server certificate.

###### Decrypted payload inspection for HTTP2

Network Firewall supports decrypted payload inspection for HTTP2.

###### Impact on existing flows

When you add a TLS inspection configuration to an existing firewall, Network Firewall interrupts traffic
flows that match the criteria defined by the TLS inspection configuration scope configuration. New
connections to the firewall begin SSL/TLS decryption and inspection. When you add new TLS inspection configuration to a firewall and there's ongoing TLS traffic that matches the scope criteria, the firewall drops the traffic.

###### Initial latency

Some latency is expected during the initial connection due to the TCP and TLS
handshakes that occur before data can flow to the firewall. If you enable
certificate revocation checking for outbound TLS inspection, you can expect
additional latency when you initially connect to a new domain over a firewall. We
recommend that you conduct your own testing using your rulesets to ensure that TLS inspection configuration
meets your performance expectations.

###### Inspection capabilities

TLS inspection is available for the request and the response for HTTPS traffic and
other TCP-based application protocols that use TLS, such as Secure Mail Transfer
Protocol Secure (SMTPS), and Post Office Protocol 3 Secure (POP3s). At the network
layer, TLS inspection supports both IPv4 and IPv6 traffic.

###### Managed rules

You can use AWS managed rules with TLS inspection. However, due to the TLS
decryption, TLS keywords don't initiate inspection within the stateful engine. You
can benefit from non-TLS rules within managed rule groups and find increased
visibility of those rules because the decrypted traffic is visible to the inspection
engine. You can also create custom rules based on inner protocols, which are
available for inspection. For example, you can match with an HTTP header within the
decrypted HTTPS stream. For more information about using managed rules with Network Firewall,
see [Managed rule groups in AWS Network Firewall](nwfw-managed-rule-groups.md "nwfw-managed-rule-groups.md").

###### Stateful rules

Network Firewall ends the TLS connection that's initiated by the client and decrypts traffic
before it reaches the stateful inspection engine. As a result, the traffic doesn't
match any TLS-based keywords except for `TLS.SNI`.
You can still use all TLS keywords in the stateful rule for traffic that doesn’t match the TLS inspection scope.
Application rules that are based on decrypted payloads are applied, for example, rules that are based on HTTP keywords.

###### Note

`TLS.SNI` keyword rules are still matched for traffic that's in TLS scope, even though the traffic is decrypted before it reaches the stateful inspection engine.

If you configure a drop or reject action for a stateful rule that matches the traffic scope that's
defined in the TLS inspection configuration, Network Firewall closes the connections to clients as soon as it detects
a payload bearing packet that matches the drop or reject rule.

Your traffic is re-encrypted before leaving the Network Firewall host.

###### Supported TLS versions

TLS versions 1.1, 1.2, and 1.3 are supported.

###### TLS cipher suites and SNI

Network Firewall terminates the TLS connection that's initiated by the client, and the TLS
Server Name Identifier (SNI) must match a configured certificate. Network Firewall uses TLS 1.3 to initiate the forward connection to the server.

The client cipher suites must include one or more of the following:

```
TLS 1.1 & TLS 1.2
AES128-GCM-SHA256
AES128-SHA
AES128-SHA256
AES256-GCM-SHA384
AES256-SHA
ECDHE-RSA-AES128-GCM-SHA256
ECDHE-RSA-AES128-SHA
ECDHE-RSA-AES128-SHA256
ECDHE-RSA-AES256-GCM-SHA384
ECDHE-RSA-AES256-SHA

TLS 1.3
TLS_AES_256_GCM_SHA384
TLS_CHACHA20_POLY1305_SHA256
TLS_AES_128_GCM_SHA256
```

###### Idle timeouts

The expected idle timeout for the TLS engine for established connections is about 120 seconds, while the idle timeout for connections that are not yet established is about 5 seconds.

###### Limitations

The following limitations apply to TLS inspection configurations:

- Cross-signed root certificates aren't supported. For more information,
  see [Using
  SSL/TLS certificates with TLS inspection configurations in AWS Network Firewall](tls-inspection-certificate-requirements.md "tls-inspection-certificate-requirements.md").
- Decryption of TLS protocols that rely upon StartTLS aren't supported.
- Network Firewall publishes separate CloudWatch metrics for traffic that's associated with
  TLS inspection configurations. Existing stateful traffic metrics don't reflect data for traffic
  that's decrypted and re-encrypted by your firewall policy's TLS inspection configuration.
- Self-signed certificates aren't supported for inbound inspection. For more
  information about the certificates that Network Firewall supports, see [Using
  SSL/TLS certificates with TLS inspection configurations in AWS Network Firewall](tls-inspection-certificate-requirements.md "tls-inspection-certificate-requirements.md").
- TLS inspection of UDP-based transport protocols such as
  Quick UDP Internet Connections
  (QUIC) isn't supported. You can configure your applications so
  that they don't switch from TCP to UDP-based transport protocols. If you want to
  prevent TLS traffic from using the QUIC protocol, modify your application to
  deny traffic using QUIC or create a firewall stateful rule to block QUIC
  traffic.
- TLS version 1.0 and prior SSL versions aren't supported.
- Traffic encrypted using TLS v1.3 Encrypted SNI and Encrypted Client Hello extensions aren't supported.
  When Network Firewall can't find an SNI in the client hello, the service closes the connection with a `RST` packet.
  If this is an issue for your workloads, you can configure your TLS inspection configuration scope to exclude the workloads using TLS v1.3.
- WebSockets inspection over HTTP2 isn't supported; Network Firewall drops this traffic. However, WebSockets over HTTP1.1 is supported.
- If Network Firewall is deployed behind an Application Load Balancer, its TLS inspection can't inspect the inbound TLS traffic that's terminated at the Application Load Balancer.
- When CA certificates are based on ECC (eliptic-curve cryptography) keys, the key usage extension needs to include the digitalSignature.
