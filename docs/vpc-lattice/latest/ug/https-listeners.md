# HTTPS listeners for VPC Lattice services

A listener is a process that checks for connection requests. You define a listener
when you create your service. You can add listeners to your service in VPC Lattice at any
time.

You can create an HTTPS listener, which uses TLS version 1.2 or TLS version 1.3 to terminate HTTPS
connections with VPC Lattice directly. VPC Lattice will provision and manage a TLS
certificate that is associated with the VPC Lattice generated Fully Qualified Domain Name
(FQDN). VPC Lattice supports TLS on HTTP/1.1 and HTTP/2. When you configure a service with
an HTTPS listener, VPC Lattice will automatically determine the HTTP protocol via
Application-Layer Protocol Negotiation (ALPN). If ALPN is absent, VPC Lattice defaults to
HTTP/1.1.

VPC Lattice uses a multi-tenancy architecture, meaning that it can host multiple services
on the same endpoint. VPC Lattice uses TLS with Server Name Indication (SNI) for every
client request. Encrypted Client Hello (ECH) and Encrypted Server Name Indication (ESNI)
aren't supported.

VPC Lattice can listen on HTTP, HTTPS, HTTP/1.1, and HTTP/2 and communicate to targets
in any of these protocols and versions. These listener and target group configurations
do not need to match. VPC Lattice manages the entire process of upgrading and downgrading
between protocols and versions. For more information, see [Protocol version](target-groups.md#target-group-protocol-version "target-groups.md#target-group-protocol-version").

To ensure that your application decrypts the traffic, create a TLS
listener instead. With TLS passthrough, VPC Lattice does not terminate TLS.
For more information, see [TLS listeners](tls-listeners.md "tls-listeners.md").

###### Contents

- [Security policy](https-listeners.md#listener-security-policy "https-listeners.md#listener-security-policy")
- [ALPN policy](https-listeners.md#listener-alpn-policy "https-listeners.md#listener-alpn-policy")
- [Add an HTTPS listener](https-listeners.md#add-https-listener "https-listeners.md#add-https-listener")

## Security policy

VPC Lattice uses a security policy that is a combination a TLSv1.2 protocol and a list of
SSL/TLS ciphers. The protocol establishes a secure connection between a client and a
server and helps to ensure that all data passed between the client and your service
in VPC Lattice is private. A cipher is an encryption algorithm that uses encryption
keys to create a coded message. Protocols use several ciphers to encrypt data.
During the connection negotiation process, the client and VPC Lattice present a list of
ciphers and protocols that they each support, in order of preference. By default,
the first cipher on the server's list that matches any one of the client's ciphers
is selected for the secure connection.

VPC Lattice uses the following TLS 1.2 SSL/TLS ciphers in this order
of preference:

- `ECDHE-RSA-AES128-GCM-SHA256`
- `ECDHE-RSA-AES128-SHA`
- `ECDHE-RSA-AES256-GCM-SHA384`
- `ECDHE-RSA-AES256-SHA`
- `AES128-GCM-SHA256`
- `AES128-SHA`
- `AES256-GCM-SHA384`
- `AES256-SHA`

VPC Lattice also uses the following TLS 1.3 SSL/TLS ciphers in this order
of preference:

- `TLS_AES_128_GCM_SHA256`
- `TLS_AES_256_GCM_SHA384`
- `TLS_CHACHA20_POLY1305_SHA256`

## ALPN policy

_Application-Layer Protocol Negotiation (ALPN)_
is a TLS extension that is sent on the initial TLS handshake hello messages. ALPN
enables the application layer to negotiate which protocols should be used over a
secure connection, such as HTTP/1 and HTTP/2.

When the client initiates an ALPN connection, the VPC Lattice service compares the
client ALPN preference list with its ALPN policy. If the client supports a protocol
from the ALPN policy, the VPC Lattice service establishes the connection based on the
preference list of the ALPN policy. Otherwise, the service does not use ALPN.

VPC Lattice supports the following ALPN policy:

`HTTP2Preferred`

Prefer HTTP/2 over HTTP/1.1. The ALPN preference list is h2,
http/1.1.

## Add an HTTPS listener

You configure a listener with a protocol and a port for connections from clients
to the service, and a target group for the default listener rule. For more
information, see [Listener configuration](listeners.md#listener-configuration "listeners.md#listener-configuration").

###### Prerequisites

- To add a forward action to the default listener rule, you must specify an
  available VPC Lattice target group. For more information, see [Create a VPC Lattice target group](create-target-group.md "create-target-group.md").
- You can specify the same target group in multiple listeners, but these
  listeners must belong to the same VPC Lattice service. To use a target group
  with a VPC Lattice service, you must verify that it is not used by a listener
  for any other VPC Lattice service.
- You can use the certificate provided by VPC Lattice or import your own
  certificate to AWS Certificate Manager. For more information, see [Bring Your Own Certificate (BYOC) for VPC Lattice](service-byoc.md "service-byoc.md").

###### To add an HTTPS listener using the console

1. Open the Amazon VPC console at
   [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
2. In the navigation pane, under **VPC Lattice**, choose
   **Services**.
3. Select the name of the service to open its details page.
4. On the **Routing** tab, choose **Add listener**.
5. For **Listener name**, you can either provide a custom
   listener name or use the protocol and port of your listener as the listener
   name. A custom name that you specify can have up to 63 characters, and it
   must be unique for every service in your account. The valid characters are
   a-z, 0-9, and hyphens (-). You can't use a hyphen as the first or last
   character, or immediately after another hyphen. You cannot change the name
   of a listener after you create it.
6. For **Protocol : port**, choose **HTTPS**
   and enter a port number.
7. For **Default action**, choose the VPC Lattice target group
   to receive traffic and choose the weight to assign to this target group. The
   weight that you assign to a target group sets its priority to receive
   traffic. For example, if two target groups have the same weight, each target
   group receives half of the traffic. If you've specified only one target
   group, then 100 percent of the traffic is sent to the one target
   group.

You can optionally add another target group for the default action. Choose
**Add action** and then choose a target group and specify
its weight. 8. (Optional) To add another rule, choose **Add rule** and then
enter a name, a priority, a condition, and an action for the rule.

You can give each rule a priority number between 1 and 100. A listener
can't have multiple rules with the same priority. Rules are evaluated in
priority order, from the lowest value to the highest value. The default rule
is evaluated last. For more information, see [Listener rules](listener-rules.md "listener-rules.md"). 9. (Optional) To add tags, expand **Listener tags**, choose
Add new tag, and enter a tag key and tag value. 10. For **HTTPS listener certificate settings**, if you did
not specify a custom domain name when you created the service, VPC Lattice
automatically generates a TLS certificate to secure the traffic flowing
though the listener.

If you created the service with a custom domain name, but didn't specify
a matching certificate, you can do so now by choosing the certificate from
**Custom SSL/TLS certificate**. Otherwise, the certificate
that you specified when you created the service is already chosen. 11. Review your configuration, and then choose **Add**.

###### To add an HTTPS listener using the AWS CLI

Use the [create-listener](../../../cli/latest/reference/vpc-lattice/create-listener.md "../../../cli/latest/reference/vpc-lattice/create-listener.md")
command to create a listener with a default rule, and the [create-rule](../../../cli/latest/reference/vpc-lattice/create-rule.md "../../../cli/latest/reference/vpc-lattice/create-rule.md") command to create additional listener rules.
