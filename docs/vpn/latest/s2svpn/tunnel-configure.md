# Configure tunnel options for AWS Site-to-Site VPN

This section provides comprehensive guidance on configuring tunnel options for
AWS Site-to-Site VPN connections, covering essential parameters such as dead peer
detection, IKE versions, and encryption settings. You can customize these tunnel options
to optimize your VPN connection's security, performance, and compatibility with your
on-premises network infrastructure.

The following are the tunnel options that you can configure.

###### Note

Some tunnel options have multiple default values. For example, **IKE
versions** has two default tunnel option values: `ikev1` and
`ikev2`. All default values will be associated with that tunnel
option if you don't choose specific values. Click to remove any default value that
you don't want associated with the tunnel option. For example, if you only want to
use `ikev1` for the IKE version, click `ikev2` to remove
it.

**Dead peer detection (DPD) timeout**

The number of seconds after which a DPD timeout occurs. A DPD timeout of 30 seconds means that the VPN endpoint will consider the peer dead 30 seconds after the first failed keep-alive. You can specify 30
or higher.

Default: 40

**DPD timeout action**

The action to take after dead peer detection (DPD) timeout occurs. You
can specify the following:

- `Clear`: End the IKE session when DPD timeout
  occurs (stop the tunnel and clear the routes)
- `None`: Take no action when DPD timeout
  occurs
- `Restart`: Restart the IKE session when DPD timeout
  occurs

For more information, see [AWS Site-to-Site VPN tunnel initiation options](initiate-vpn-tunnels.md "initiate-vpn-tunnels.md").

Default: `Clear`

**VPN logging options**

With Site-to-Site VPN logs, you can gain access to details on IP Security (IPsec) tunnel establishment, Internet Key Exchange (IKE) negotiations, and dead peer detection (DPD) protocol messages.

For more information, see [AWS Site-to-Site VPN logs](monitoring-logs.md "monitoring-logs.md").

Available log formats: `json`, `text`

**IKE versions**

The IKE versions that are permitted for the VPN tunnel. You can specify
one or more of the default values.

Defaults: `ikev1`, `ikev2`

**Inside tunnel IPv4 CIDR**

The range of inside (internal) IPv4 addresses for the VPN tunnel. You can
specify a size /30 CIDR block from the `169.254.0.0/16` range. The
CIDR block must be unique across all Site-to-Site VPN connections that use the same virtual
private gateway.

###### Note

The CIDR block does not need to be unique across all connections on a transit gateway. However, if they are not unique, it can create a conflict on your customer gateway. Proceed carefully when re-using the same CIDR block on multiple Site-to-Site VPN connections on a transit gateway.

The following CIDR blocks are reserved and cannot be used:

- `169.254.0.0/30`
- `169.254.1.0/30`
- `169.254.2.0/30`
- `169.254.3.0/30`
- `169.254.4.0/30`
- `169.254.5.0/30`
- `169.254.169.252/30`

Default: A size /30 IPv4 CIDR block from the `169.254.0.0/16`
range.

**Pre-shared key storage**

The type of storage for the pre-shared key:

- **Standard** — The pre-shared key is stored directly
  in the Site-to-Site VPN service.
- **Secrets Manager** — The pre-shared key is stored
  using AWS Secrets Manager. For more information about Secrets Manager, see [Enhanced security features using Secrets Manager](enhanced-security.md "enhanced-security.md").

**Tunnel bandwidth**

The bandwidth supported for the tunnel.

- **Standard** — The tunnel bandwidth is set to a maximum of up to 1.25 Gbps per tunnel (default).
- **Large** — The tunnel bandwidth to a maximum of up to
  5 Gbps per tunnel.

###### Note

**Large** is only available only for VPN connections attached to a transit
gateway or to Cloud WAN. It is not supported for Virtual Private
Gateway connections.

**Inside tunnel IPv6 CIDR**

(IPv6 VPN connections only) The range of inside (internal) IPv6 addresses for
the VPN tunnel. You can specify a size /126 CIDR block from the local
`fd00::/8` range. The CIDR block must be unique across all Site-to-Site VPN
connections that use the same transit gateway. If you don't specify an IPv6
subnet, Amazon automatically selects a /128 subnet from this range. Regardless
of whether you specify the subnet or Amazon selects it, Amazon uses the first
usable IPv6 address in the subnet for its side of the connection, and your side
uses the second usable IPv6 address.

Default: A size /126 IPv6 CIDR block from the local `fd00::/8`
range.

**Outside tunnel IP address type**

The IP address type for the outside (external) tunnel IP addresses. You can specify one of the following:

- `PrivateIpv4`: Use private IPv4 address to deploy Site-to-Site VPN
  connections over Direct Connect.
- `PublicIpv4`: (Default) Use IPv4 addresses for the outer tunnel IPs.
- `Ipv6`: Use IPv6 addresses for the outer tunnel IPs. This
  option is only available for VPN connections on a transit gateway or
  Cloud WAN.

When you select `Ipv6`, AWS automatically configures the outside
tunnel IPv6 addresses for the AWS side of the VPN tunnels. Your customer gateway
device must support IPv6 addressing and be able to establish IPsec tunnels with
IPv6 endpoints.

Default: `PublicIpv4`

**Local IPv4 Network CIDR**

(IPv4 VPN connection only) The CIDR range used during IKE phase 2 negotiation
for the customer (on-premises) side of the VPN tunnel. This range is used to
propose routes but does not enforce traffic restrictions since AWS uses
route-based VPNs exclusively. Policy-based VPNs are not supported as they would
limit AWS' ability to support dynamic routing protocols and multi-region
architectures. This should include the IP ranges from your on-premises network
that need to communicate over the VPN tunnel. Proper route table configurations,
NACLs, and security groups should be used to control actual traffic flow.

Default: 0.0.0.0/0

**Remote IPv4 Network CIDR**

(IPv4 VPN connection only) The CIDR range used during IKE phase 2 negotiation
for the AWS side of the VPN tunnel. This range is used to propose routes but
does not enforce traffic restrictions since AWS uses route-based VPNs
exclusively. AWS does not support policy-based VPNs because they lack the
flexibility required for complex routing scenarios and are incompatible with
features like transit gateways and VPN Equal Cost Multi-Path (ECMP). For VPCs,
this is typically the CIDR range of your VPC. For transit gateways, this could
include multiple CIDR ranges from attached VPCs or other network.

Default: 0.0.0.0/0

**Local IPv6 Network CIDR**

(IPv6 VPN connection only) The IPv6 CIDR range on the customer gateway
(on-premises) side that is allowed to communicate over the VPN tunnels.

Default: ::/0

**Remote IPv6 Network CIDR**

(IPv6 VPN connection only) The IPv6 CIDR range on the AWS side that is
allowed to communicate over the VPN tunnels.

Default: ::/0

**Phase 1 Diffie-Hellman (DH) group numbers**

The DH group numbers that are permitted for the VPN tunnel for phase 1 of
the IKE negotiations. You can specify one or more of the default
values.

Defaults: 2, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24

**Phase 2 Diffie-Hellman (DH) group numbers**

The DH group numbers that are permitted for the VPN tunnel for phase 2 of
the IKE negotiations. You can specify one or more of the default
values.

Defaults: 2, 5, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24

**Phase 1 encryption algorithms**

The encryption algorithms that are permitted for the VPN tunnel for phase
1 of the IKE negotiations. You can specify one or more of the default
values.

Defaults: AES128, AES256, AES128-GCM-16, AES256-GCM-16

**Phase 2 encryption algorithms**

The encryption algorithms that are permitted for the VPN tunnel for phase
2 IKE negotiations. You can specify one or more of the default
values.

Defaults: AES128, AES256, AES128-GCM-16, AES256-GCM-16

**Phase 1 integrity algorithms**

The integrity algorithms that are permitted for the VPN tunnel for phase
1 of the IKE negotiations. You can specify one or more of the default
values.

Defaults: SHA1, SHA2-256, SHA2-384, SHA2-512

**Phase 2 integrity algorithms**

The integrity algorithms that are permitted for the VPN tunnel for phase
2 of the IKE negotiations. You can specify one or more of the default
values.

Defaults: SHA1, SHA2-256, SHA2-384, SHA2-512

**Phase 1 lifetime**

###### Note

AWS initiate re-keys with the timing values set in the Phase 1 lifetime and
Phase 2 lifetime fields. If such lifetimes are different than the negotiated
handshake values, this may interrupt tunnel connectivity.

The lifetime in seconds for phase 1 of the IKE negotiations. You can
specify a number between 900 and 28,800.

Default: 28,800 (8 hours)

**Phase 2 lifetime**

###### Note

AWS initiate re-keys with the timing values set in the Phase 1 lifetime
and Phase 2 lifetime fields. If such lifetimes are different than the
negotiated handshake values, this may interrupt tunnel connectivity.

The lifetime in seconds for phase 2 of the IKE negotiations. You can
specify a number between 900 and 3,600. The number that you specify must be
less than the number of seconds for the phase 1 lifetime.

Default: 3,600 (1 hour)

**Pre-shared key (PSK)**

The pre-shared key (PSK) to establish the initial internet key
exchange (IKE) security association between the target gateway
and customer gateway.

The PSK must be between 8 and 64 characters in length and cannot start
with zero (0). Allowed characters are alphanumeric characters, periods
(.), and underscores (\_).

Default: A 32-character alphanumeric string.

**Rekey fuzz**

The percentage of the rekey window (determined by the rekey margin
time) within which the rekey time is randomly selected.

You can specify a percentage value between 0 and 100.

Default: 100

**Rekey margin time**

The margin time in seconds before the phase 1 and phase 2 lifetime expires,
during which the AWS side of the VPN connection performs an IKE rekey.

You can specify a number between 60 and half of the value of the phase 2
lifetime.

The exact time of the rekey is randomly selected based on the value
for rekey fuzz.

Default: 270 (4.5 minutes)

**Replay window size packets**

The number of packets in an IKE replay window.

You can specify a value between 64 and 2048.

Default: 1024

**Startup action**

The action to take when establishing the tunnel for a VPN connection.
You can specify the following:

- `Start`: AWS initiates the IKE negotiation to bring
  the tunnel up. Only supported if your customer gateway is
  configured with an IP address.
- `Add`: Your customer gateway device must initiate
  the IKE negotiation to bring the tunnel up.

For more information, see [AWS Site-to-Site VPN tunnel initiation options](initiate-vpn-tunnels.md "initiate-vpn-tunnels.md").

Default: `Add`

**Tunnel endpoint lifecycle control**

Tunnel endpoint lifecycle control provides control over the schedule of endpoint
replacements.

For more information, see [AWS Site-to-Site VPN tunnel endpoint lifecycle control](tunnel-endpoint-lifecycle.md "tunnel-endpoint-lifecycle.md").

Default: `Off`

You can specify the tunnel options when you create a Site-to-Site VPN connection, or you can modify the
tunnel options for an existing VPN connection. For more information, see the following topics:

- [Step 5: Create a VPN connection](SetUpVPNConnections.md#vpn-create-vpn-connection "SetUpVPNConnections.md#vpn-create-vpn-connection")
- [Modify AWS Site-to-Site VPN tunnel options](modify-vpn-tunnel-options.md "modify-vpn-tunnel-options.md")
