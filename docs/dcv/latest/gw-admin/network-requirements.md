# Amazon DCV Connection Gateway network requirements

Amazon DCV Connection Gateway is usually installed on dedicated hosts, separate from Amazon DCV server machines.
As depicted in the [high-level overview](what-is-gw.md#how-gw-works "what-is-gw.md#how-gw-works"), the Connection Gateway must have network connectivity
with the other components: the Clients, the Amazon DCV server hosts, the Session Resolver, and the
Web Resources Server.

###### Note

Depending on how the machines and network are configured, the network traffic that flows to and
from the different components may be bound to separate network interfaces.

Please make sure your firewall rules and security groups allow the following:

- The Connection Gateway listens for incoming connection on a TCP port specified in the [configuration](setting-up-configuring.md "setting-up-configuring.md"). This port must be reachable from the clients connecting to the gateway.
- If QUIC support is enabled, Connection Gateway listens for incoming QUIC traffic on a UDP port specified in the [configuration](setting-up-configuring.md "setting-up-configuring.md"). This port must be reachable from the clients connecting to the gateway.
- The Connection Gateway must be able to connect to Amazon DCV server hosts on the [TCP port](../adminguide/manage-port-addr.md "../adminguide/manage-port-addr.md") used for DCV connections, 8443 by default.
- If QUIC support is enabled, Connection Gateway must be able to connect to Amazon DCV server hosts on the [UDP port](../adminguide/enable-quic.md "../adminguide/enable-quic.md") used for DCV QUIC connections, 8443 by default.
- The Connection Gateway must be able to connect to the TCP port of the HTTPS end-point exposed by the Session Resolver.
- If a Web Resources Server is present, Connection Gateway must be able to connect to the TCP port of the HTTPS end-point exposed by the Web Resources Server.
  If you choose to have multiple Amazon DCV Connection Gateway hosts to improve availability, then a network load
  balancer will be present between the clients and the Connection Gateway hosts. In this case the gateway must
  be reachable from the load balancer nodes. When using a load balancer you may also want to use
  a health-check connection; in this case the load balancer need to be able to reach the TCP
  port of the health-check service exposed by the Amazon DCV Connection Gateway.

If using a Network Load Balander, refer to [its documentation](../../../elasticloadbalancing/latest/network/target-group-register-targets.md "../../../elasticloadbalancing/latest/network/target-group-register-targets.md")
for more details.
