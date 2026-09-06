

# Ports and Protocols for AWS Windows AMIs
<a name="ports-and-protocols"></a>

The following tables list the ports, protocols, and directions by workload for AWS Windows Amazon Machine Images (AMIs).

**Topics**
+ [AllJoyn Router](#alljoyntcpin-ports)
+ [Cast to Device](#cast-to-device)
+ [Core Networking](#networking-ports)
+ [Delivery Optimization](#delivery-optimization)
+ [Diag Track](#diag)
+ [DIAL Protocol Server](#dial-protocol)
+ [File and Printer Sharing](#file-and-print)
+ [File Server Remote Management](#file-server-remote)
+ [ICMP v4 All](#icmp-v4)
+ [Microsoft Edge](#protocol-edge)
+ [Microsoft Media Foundation Network Source](#protocol-media-foundation)
+ [Multicast](#multicast)
+ [Remote Desktop](#remote-desktop)
+ [WindowsDevice Management](#device-management)
+ [WindowsFeature Experience Pack](#remote-management)
+ [WindowsFirewall Remote Management](#firewall-remote)
+ [WindowsRemote Management](#remote-management)

## AllJoyn Router
<a name="alljoyntcpin-ports"></a>



- **Windows Server 2016 Windows Server 2019 Windows Server 2022**
  - **Rule:** AllJoyn Router (TCP-In) / **Description:** Inbound rule for AllJoyn Router traffic [TCP] / **Port:** Local: 9955<br />Remote: Any / **Protocol:** TCP / **Direction:** In
  - **Rule:** AllJoyn Router (TCP-Out) / **Description:** Outbound rule for AllJoyn Router traffic [TCP] / **Port:** Local: Any<br />Remote: Any / **Protocol:** TCP / **Direction:** Out
  - **Rule:** AllJoyn Router (UDP-In) / **Description:** Inbound rule for AllJoyn Router traffic [UDP] / **Port:** Local: Any<br />Remote: Any / **Protocol:** UDP / **Direction:** In
  - **Rule:** AllJoyn Router (UDP-Out) / **Description:** Outbound rule for AllJoyn Router traffic [UDP] / **Port:** Local: Any<br />Remote: Any / **Protocol:** UDP / **Direction:** Out



## Cast to Device
<a name="cast-to-device"></a>



- **Windows Server 2016 Windows Server 2019 Windows Server 2022**
  - **Rule:** Cast to Device functionality (qWave-TCP-In) / **Description:** Inbound rule for the Cast to Device functionality to allow use of the Quality Windows Audio Video Experience Service. [TCP 2177] / **Port:** Local: 2177<br />Remote: Any / **Protocol:** TCP / **Direction:** In
  - **Rule:** Cast to Device functionality (qWave-TCP-Out) / **Description:** Outbound rule for the Cast to Device functionality to allow use of the Quality Windows Audio Video Experience Service. [TCP 2177] / **Port:** Local: AnyRemote: 2177 / **Protocol:** TCP / **Direction:** Out
  - **Rule:** Cast to Device functionality (qWave-UDP-In) / **Description:** Inbound rule for the Cast to Device functionality to allow use of the Quality Windows Audio Video Experience Service. [UDP 2177] / **Port:** Local: 2177<br />Remote: Any / **Protocol:** UDP / **Direction:** In
  - **Rule:** Cast to Device functionality (qWave-UDP-Out) / **Description:** Outbound rule for the Cast to Device functionality to allow use of the Quality Windows Audio Video Experience Service. [UDP 2177] / **Port:** Local: AnyRemote: 2177 / **Protocol:** UDP / **Direction:** Out
  - **Rule:** Cast to Device SSDP Discovery (UDP-In) / **Description:** Inbound rule to allow discovery of Cast to Device targets using SSDP / **Port:** Local: Ply2DiscRemote: Any / **Protocol:** UDP / **Direction:** In
  - **Rule:** Cast to Device Streaming Server (HTTP-Streaming-In) / **Description:** Inbound rule for the Cast to Device server to allow streaming using HTTP. [TCP 10246] / **Port:** Local: 10246Remote: Any / **Protocol:** TCP / **Direction:** In
  - **Rule:** Cast to Device Streaming Server (RTCP-Streaming-In) / **Description:** Inbound rule for the Cast to Device server to allow streaming using RTSP and RTP. [UDP] / **Port:** Local: AnyRemote: Any / **Protocol:** UDP / **Direction:** In
  - **Rule:** Cast to Device Streaming Server (RTP-Streaming-Out) / **Description:** Outbound rule for the Cast to Device server to allow streaming using RTSP and RTP. [UDP] / **Port:** Local: AnyRemote: Any / **Protocol:** UDP / **Direction:** Out
  - **Rule:** Cast to Device Streaming Server (RTSP-Streaming-In) / **Description:** Inbound rule for the Cast to Device server to allow streaming using RTSP and RTP. [TCP 23554, 23555, 23556] / **Port:** Local: 235, 542, 355, 523, 556Remote: Any / **Protocol:** TCP / **Direction:** In
  - **Rule:** Cast to Device UPnP Events (TCP-In) / **Description:** Inbound rule to allow receiving UPnP Events from Cast to Device targets / **Port:** Local: 2869Remote: Any / **Protocol:** TCP / **Direction:** In



## Core Networking
<a name="networking-ports"></a>

------
#### [ Windows Server 2016, 2019, and 2022 ]



- ** Windows Server 2016 Windows Server 2019 Windows Server 2022 **
  - **Rule:** Destination Unreachable (ICMPv6-In) / **Definition:** Destination Unreachable error messages are sent from any node that a packet traverses which is unable to forward the packet for any reason except congestion. / **Port:**  / **Protocol:** ICMPv6 / **Direction:** In
  - **Rule:** Destination Unreachable Fragmentation Needed (ICMPv4-In) / **Definition:** Destination Unreachable Fragmentation Needed error messages are sent from any node that a packet traverses which is unable to forward the packet because fragmentation was needed and the don't fragment bit was set. / **Port:**  / **Protocol:** ICMPv4 / **Direction:** In
  - **Rule:** Core Networking - DNS (UDP-Out) / **Definition:** Outbound rule to allow DNS requests. DNS responses based on requests that match this rule are permitted regardless of source address. This behavior is classified as loose source mapping.  / **Port:** Local: Any<br />Remote: 53 / **Protocol:** UDP / **Direction:** Out
  - **Rule:** Dynamic Host Configuration Protocol (DHCP-In) / **Definition:** Allows DHCP (Dynamic Host Configuration Protocol) messages for stateful auto-configuration. / **Port:** Local: 68<br />Remote: 67 / **Protocol:** UDP / **Direction:** In
  - **Rule:** Dynamic Host Configuration Protocol (DHCP-Out) / **Definition:** Allows DHCP (Dynamic Host Configuration Protocol) messages for stateful auto-configuration. / **Port:** Local: 68<br />Remote: 67 / **Protocol:** UDP / **Direction:** Out
  - **Rule:** Dynamic Host Configuration Protocol for IPv6(DHCPV6-In) / **Definition:** Allows DHCPV6 (Dynamic Host Configuration Protocol for IPv6) messages for stateful and stateless configuration. / **Port:** Local: 546<br />Remote: 547 / **Protocol:** UDP / **Direction:** In
  - **Rule:** Dynamic Host Configuration Protocol for IPv6(DHCPV6-Out) / **Definition:** Allows DHCPV6 (Dynamic Host Configuration Protocol for IPv6) messages for stateful and stateless configuration. / **Port:** Local: 546<br />Remote: 547 / **Protocol:** UDP / **Direction:** Out
  - **Rule:** Core Networking - Group Policy (LSASS-Out) / **Definition:** Outbound rule to allow remote LSASS traffic for Group Policy updates. / **Port:** Local: Any<br />Remote: Any / **Protocol:** TCP / **Direction:** Out
  - **Rule:** Core Networking - Group Policy (NP-Out) / **Definition:** Core Networking - Group Policy (NP-Out) / **Port:** Local: Any<br />Remote: 445 / **Protocol:** TCP / **Direction:** Out
  - **Rule:** Core Networking - Group Policy (TCP-Out) / **Definition:** Outbound rule to allow remote RPC traffic for Group Policy updates.  / **Port:** Local: Any<br />Remote: Any / **Protocol:** TCP / **Direction:** Out
  - **Rule:** Internet Group Management Protocol (IGMP-In) / **Definition:** IGMP messages are sent and received by nodes to create, join, and depart multicast groups. / **Port:**  / **Protocol:** 2 / **Direction:** In
  - **Rule:** Core Networking - Internet Group Management Protocol (IGMP-Out) / **Definition:** IGMP messages are sent and received by nodes to create, join, and depart multicast groups. / **Port:**  / **Protocol:** 2 / **Direction:** Out
  - **Rule:** Core Networking - IPHTTPS (TCP-In) / **Definition:** Inbound TCP rule to allow IPHTTPS tunneling technology to provide connectivity across HTTP proxies and firewalls. / **Port:** Local: IPHTPS<br />Remote: Any / **Protocol:** TCP / **Direction:** In
  - **Rule:** Core Networking - IPHTTPS (TCP-Out) / **Definition:** Outbound TCP rule to allow IPHTTPS tunneling technology to provide connectivity across HTTP proxies and firewalls. / **Port:** Local: Any<br />Remote: IPHTPS / **Protocol:** TCP / **Direction:** Out
  - **Rule:** IPv6 (IPv6-In) / **Definition:** Inbound rule required to permit IPv6 traffic for ISATAP (Intra-Site Automatic Tunnel Addressing Protocol) and 6to4 tunneling services. / **Port:**  / **Protocol:** 41 / **Direction:** In
  - **Rule:** IPv6 (IPv6-Out) / **Definition:** Outbound rule required to permit IPv6 traffic for ISATAP (Intra-Site Automatic Tunnel Addressing Protocol) and 6to4 tunneling services. / **Port:**  / **Protocol:** 41 / **Direction:** Out
  - **Rule:** Multicast Listener Done (ICMPv6-In) / **Definition:** Multicast Listener Done messages inform local routers that there are no longer any members remaining for a specific multicast address on the subnet. / **Port:**  / **Protocol:** ICMPv6 / **Direction:** In
  - **Rule:** Multicast Listener Done (ICMPv6-Out) / **Definition:** Multicast Listener Done messages inform local routers that there are no longer any members remaining for a specific multicast address on the subnet. / **Port:**  / **Protocol:** ICMPv6 / **Direction:** Out
  - **Rule:** Multicast Listener Query (ICMPv6-In) / **Definition:** An IPv6 multicast-capable router uses the Multicast Listener Query message to query a link for multicast group membership. / **Port:**  / **Protocol:** ICMPv6 / **Direction:** In
  - **Rule:** Multicast Listener Query (ICMPv6-Out) / **Definition:** An IPv6 multicast-capable router uses the Multicast Listener Query message to query a link for multicast group membership. / **Port:**  / **Protocol:** ICMPv6 / **Direction:** Out
  - **Rule:** Multicast Listener Report (ICMPv6-In) / **Definition:** The Multicast Listener Report message is used by a listening node to either immediately report its interest in receiving multicast traffic at a specific multicast address or in response to a Multicast Listener Query. / **Port:**  / **Protocol:** ICMPv6 / **Direction:** In
  - **Rule:** Multicast Listener Report (ICMPv6-Out) / **Definition:** The Multicast Listener Report message is used by a listening node to either immediately report its interest in receiving multicast traffic at a specific multicast address or in response to a Multicast Listener Query. / **Port:**  / **Protocol:** ICMPv6 / **Direction:** Out
  - **Rule:** Multicast Listener Report v2 (ICMPv6-In) / **Definition:** Multicast Listener Report v2 message is used by a listening node to either immediately report its interest in receiving multicast traffic at a specific multicast address or in response to a Multicast Listener Query. / **Port:**  / **Protocol:** ICMPv6 / **Direction:** In
  - **Rule:** Multicast Listener Report v2 (ICMPv6-Out) / **Definition:** Multicast Listener Report v2 message is used by a listening node to either immediately report its interest in receiving multicast traffic at a specific multicast address or in response to a Multicast Listener Query. / **Port:**  / **Protocol:** ICMPv6 / **Direction:** Out
  - **Rule:** Neighbor Discovery Advertisement (ICMPv6-In) / **Definition:** Neighbor Discovery Advertisement messages are sent by nodes to notify other nodes of link-layer address changes or in response to a Neighbor Discovery Solicitation request. / **Port:**  / **Protocol:** ICMPv6 / **Direction:** In
  - **Rule:** Neighbor Discovery Advertisement (ICMPv6-Out) / **Definition:** Neighbor Discovery Advertisement messages are sent by nodes to notify other nodes of link-layer address changes or in response to a Neighbor Discovery Solicitation request. / **Port:**  / **Protocol:** ICMPv6 / **Direction:** Out
  - **Rule:** Neighbor Discovery Solicitation (ICMPv6-In) / **Definition:** Neighbor Discovery Solicitations are sent by nodes to discover the link-layer address of another on-link IPv6 node. / **Port:**  / **Protocol:** ICMPv6 / **Direction:** In
  - **Rule:** Neighbor Discovery Solicitation (ICMPv6-Out) / **Definition:** Neighbor Discovery Solicitations are sent by nodes to discover the link-layer address of another on-link IPv6 node. / **Port:**  / **Protocol:** ICMPv6 / **Direction:** Out
  - **Rule:** Packet Too Big (ICMPv6-In) / **Definition:** Packet Too Big error messages are sent from any node that a packet traverses which is unable to forward the packet because the packet is too large for the next link. / **Port:**  / **Protocol:** ICMPv6 / **Direction:** In
  - **Rule:** Packet Too Big (ICMPv6-Out) / **Definition:** Packet Too Big error messages are sent from any node that a packet traverses which is unable to forward the packet because the packet is too large for the next link. / **Port:**  / **Protocol:** ICMPv6 / **Direction:** Out
  - **Rule:** Parameter Problem (ICMPv6-In) / **Definition:** Parameter Problem error messages are sent by nodes when packets are incorrectly generated. / **Port:**  / **Protocol:** ICMPv6 / **Direction:** In
  - **Rule:** Parameter Problem (ICMPv6-Out) / **Definition:** Parameter Problem error messages are sent by nodes when packets are incorrectly generated. / **Port:**  / **Protocol:** ICMPv6 / **Direction:** Out
  - **Rule:** Router Advertisement (ICMPv6-In) / **Definition:** Router Advertisement messages are sent by routers to other nodes for stateless auto-configuration. / **Port:**  / **Protocol:** ICMPv6 / **Direction:** In
  - **Rule:** Router Advertisement (ICMPv6-Out) / **Definition:** Router Advertisement messages are sent by routers to other nodes for stateless auto-configuration. / **Port:**  / **Protocol:** ICMPv6 / **Direction:** Out
  - **Rule:** Router Solicitation (ICMPv6-In) / **Definition:** Router Solicitation messages are sent by nodes seeking routers to provide stateless auto-configuration. / **Port:**  / **Protocol:** ICMPv6 / **Direction:** In
  - **Rule:** Router Solicitation (ICMPv6-Out) / **Definition:** Router Solicitation messages are sent by nodes seeking routers to provide stateless auto-configuration. / **Port:**  / **Protocol:** ICMPv6 / **Direction:** Out
  - **Rule:** Core Networking - Teredo (UDP-In) / **Definition:** Inbound UDP rule to allow Teredo edge traversal. This technology provides address assignment and automatic tunneling for unicast IPv6 traffic when an IPv6/IPv4 host is located behind an IPv4 network address translator. / **Port:** Local: Teredo<br />Remote: Any / **Protocol:** UDP / **Direction:** In
  - **Rule:** Core Networking - Teredo (UDP-Out) / **Definition:** Outbound UDP rule to allow Teredo edge traversal. This technology provides address assignment and automatic tunneling for unicast IPv6 traffic when an IPv6/IPv4 host is located behind an IPv4 network address translator. / **Port:** Local: Any<br />Remote: Any / **Protocol:** UDP / **Direction:** Out
  - **Rule:** Time Exceeded (ICMPv6-In) / **Definition:** Time Exceeded error messages are generated from any node that a packet traverses if the Hop Limit value is decremented to zero at any point on the path. / **Port:**  / **Protocol:** ICMPv6 / **Direction:** In
  - **Rule:** Time Exceeded (ICMPv6-Out) / **Definition:** Time Exceeded error messages are generated from any node that a packet traverses if the Hop Limit value is decremented to zero at any point on the path. / **Port:**  / **Protocol:** ICMPv6 / **Direction:** Out



------
#### [ Windows Server 2012 and 2012 R2 ]



- ** Windows Server 2012 Windows Server 2012 R2 **
  - **Rule:** Destination Unreachable (ICMPv6-In) / **Definition:** Destination Unreachable error messages are sent from any node that a packet traverses which is unable to forward the packet for any reason except congestion. / **Port:** Local: 68<br />Remote: 67 / **Protocol:** ICMPv6 / **Direction:** In
  - **Rule:** Destination Unreachable Fragmentation Needed (ICMPv4-In) / **Definition:** Destination Unreachable Fragmentation Needed error messages are sent from any node that a packet traverses which is unable to forward the packet because fragmentation was needed and the don't fragment bit was set. / **Port:** Local: 68<br />Remote: 67 / **Protocol:** ICMPv4 / **Direction:** In
  - **Rule:** Core Networking - DNS (UDP-Out) / **Definition:** Outbound rule to allow DNS requests. DNS responses based on requests that match this rule are permitted regardless of source address. This behavior is classified as loose source mapping.  / **Port:** Local: Any<br />Remote: 53 / **Protocol:** UDP / **Direction:** Out
  - **Rule:** Dynamic Host Configuration Protocol (DHCP-In) / **Definition:** Allows DHCP (Dynamic Host Configuration Protocol) messages for stateful auto-configuration. / **Port:** Local: 68<br />Remote: 67 / **Protocol:** UDP / **Direction:** In
  - **Rule:** Dynamic Host Configuration Protocol (DHCP-Out) / **Definition:** Allows DHCP (Dynamic Host Configuration Protocol) messages for stateful auto-configuration. / **Port:** Local: 68<br />Remote: 67 / **Protocol:** UDP / **Direction:** Out
  - **Rule:** Dynamic Host Configuration Protocol for IPv6(DHCPV6-In) / **Definition:** Allows DHCPV6 (Dynamic Host Configuration Protocol for IPv6) messages for stateful and stateless configuration. / **Port:** Local: 546<br />Remote: 547 / **Protocol:** UDP / **Direction:** In
  - **Rule:** Dynamic Host Configuration Protocol for IPv6(DHCPV6-Out) / **Definition:** Allows DHCPV6 (Dynamic Host Configuration Protocol for IPv6) messages for stateful and stateless configuration. / **Port:** Local: 546<br />Remote: 547 / **Protocol:** UDP / **Direction:** Out
  - **Rule:** Core Networking - Group Policy (LSASS-Out) / **Definition:** Outbound rule to allow remote LSASS traffic for Group Policy updates. / **Port:** Local: Any<br />Remote: Any / **Protocol:** TCP / **Direction:** Out
  - **Rule:** Core Networking - Group Policy (NP-Out) / **Definition:** Core Networking - Group Policy (NP-Out) / **Port:** Local: Any<br />Remote: 445 / **Protocol:** TCP / **Direction:** Out
  - **Rule:** Core Networking - Group Policy (TCP-Out) / **Definition:** Outbound rule to allow remote RPC traffic for Group Policy updates.  / **Port:** Local: Any<br />Remote: Any / **Protocol:** TCP / **Direction:** Out
  - **Rule:** Internet Group Management Protocol (IGMP-In) / **Definition:** IGMP messages are sent and received by nodes to create, join, and depart multicast groups. / **Port:** Local: 68<br />Remote: 67 / **Protocol:** 2 / **Direction:** In
  - **Rule:** Core Networking - Internet Group Management Protocol (IGMP-Out) / **Definition:** IGMP messages are sent and received by nodes to create, join, and depart multicast groups. / **Port:** Local: 68<br />Remote: 67 / **Protocol:** 2 / **Direction:** Out
  - **Rule:** Core Networking - IPHTTPS (TCP-In) / **Definition:** Inbound TCP rule to allow IPHTTPS tunneling technology to provide connectivity across HTTP proxies and firewalls. / **Port:** Local: IPHTPS<br />Remote: Any / **Protocol:** TCP / **Direction:** In
  - **Rule:** Core Networking - IPHTTPS (TCP-Out) / **Definition:** Outbound TCP rule to allow IPHTTPS tunneling technology to provide connectivity across HTTP proxies and firewalls. / **Port:** Local: Any<br />Remote: IPHTPS / **Protocol:** TCP / **Direction:** Out
  - **Rule:** IPv6 (IPv6-In) / **Definition:** Inbound rule required to permit IPv6 traffic for ISATAP (Intra-Site Automatic Tunnel Addressing Protocol) and 6to4 tunneling services. / **Port:** Local: Any<br />Remote: 445 / **Protocol:** 41 / **Direction:** In
  - **Rule:** IPv6 (IPv6-Out) / **Definition:** Outbound rule required to permit IPv6 traffic for ISATAP (Intra-Site Automatic Tunnel Addressing Protocol) and 6to4 tunneling services. / **Port:** Local: Any<br />Remote: 445 / **Protocol:** 41 / **Direction:** Out
  - **Rule:** Multicast Listener Done (ICMPv6-In) / **Definition:** Multicast Listener Done messages inform local routers that there are no longer any members remaining for a specific multicast address on the subnet. / **Port:** Local: 68<br />Remote: 67 / **Protocol:** ICMPv6 / **Direction:** In
  - **Rule:** Multicast Listener Done (ICMPv6-Out) / **Definition:** Multicast Listener Done messages inform local routers that there are no longer any members remaining for a specific multicast address on the subnet. / **Port:** Local: 68<br />Remote: 67 / **Protocol:** ICMPv6 / **Direction:** Out
  - **Rule:** Multicast Listener Query (ICMPv6-In) / **Definition:** An IPv6 multicast-capable router uses the Multicast Listener Query message to query a link for multicast group membership. / **Port:** Local: 68<br />Remote: 67 / **Protocol:** ICMPv6 / **Direction:** In
  - **Rule:** Multicast Listener Query (ICMPv6-Out) / **Definition:** An IPv6 multicast-capable router uses the Multicast Listener Query message to query a link for multicast group membership. / **Port:** Local: 68<br />Remote: 67 / **Protocol:** ICMPv6 / **Direction:** Out
  - **Rule:** Multicast Listener Report (ICMPv6-In) / **Definition:** The Multicast Listener Report message is used by a listening node to either immediately report its interest in receiving multicast traffic at a specific multicast address or in response to a Multicast Listener Query. / **Port:** Local: 68<br />Remote: 67 / **Protocol:** ICMPv6 / **Direction:** In
  - **Rule:** Multicast Listener Report (ICMPv6-Out) / **Definition:** The Multicast Listener Report message is used by a listening node to either immediately report its interest in receiving multicast traffic at a specific multicast address or in response to a Multicast Listener Query. / **Port:** Local: 68<br />Remote: 67 / **Protocol:** ICMPv6 / **Direction:** Out
  - **Rule:** Multicast Listener Report v2 (ICMPv6-In) / **Definition:** Multicast Listener Report v2 message is used by a listening node to either immediately report its interest in receiving multicast traffic at a specific multicast address or in response to a Multicast Listener Query. / **Port:** Local: 68<br />Remote: 67 / **Protocol:** ICMPv6 / **Direction:** In
  - **Rule:** Multicast Listener Report v2 (ICMPv6-Out) / **Definition:** Multicast Listener Report v2 message is used by a listening node to either immediately report its interest in receiving multicast traffic at a specific multicast address or in response to a Multicast Listener Query. / **Port:** Local: 68<br />Remote: 67 / **Protocol:** ICMPv6 / **Direction:** Out
  - **Rule:** Neighbor Discovery Advertisement (ICMPv6-In) / **Definition:** Neighbor Discovery Advertisement messages are sent by nodes to notify other nodes of link-layer address changes or in response to a Neighbor Discovery Solicitation request. / **Port:** Local: 68<br />Remote: 67 / **Protocol:** ICMPv6 / **Direction:** In
  - **Rule:** Neighbor Discovery Advertisement (ICMPv6-Out) / **Definition:** Neighbor Discovery Advertisement messages are sent by nodes to notify other nodes of link-layer address changes or in response to a Neighbor Discovery Solicitation request. / **Port:** Local: 68<br />Remote: 67 / **Protocol:** ICMPv6 / **Direction:** Out
  - **Rule:** Neighbor Discovery Solicitation (ICMPv6-In) / **Definition:** Neighbor Discovery Solicitations are sent by nodes to discover the link-layer address of another on-link IPv6 node. / **Port:** Local: 68<br />Remote: 67 / **Protocol:** ICMPv6 / **Direction:** In
  - **Rule:** Neighbor Discovery Solicitation (ICMPv6-Out) / **Definition:** Neighbor Discovery Solicitations are sent by nodes to discover the link-layer address of another on-link IPv6 node. / **Port:** Local: 68<br />Remote: 67 / **Protocol:** ICMPv6 / **Direction:** Out
  - **Rule:** Packet Too Big (ICMPv6-In) / **Definition:** Packet Too Big error messages are sent from any node that a packet traverses which is unable to forward the packet because the packet is too large for the next link. / **Port:** Local: 68<br />Remote: 67 / **Protocol:** ICMPv6 / **Direction:** In
  - **Rule:** Packet Too Big (ICMPv6-Out) / **Definition:** Packet Too Big error messages are sent from any node that a packet traverses which is unable to forward the packet because the packet is too large for the next link. / **Port:** Local: 68<br />Remote: 67 / **Protocol:** ICMPv6 / **Direction:** Out
  - **Rule:** Parameter Problem (ICMPv6-In) / **Definition:** Parameter Problem error messages are sent by nodes when packets are incorrectly generated. / **Port:** Local: 68<br />Remote: 67 / **Protocol:** ICMPv6 / **Direction:** In
  - **Rule:** Parameter Problem (ICMPv6-Out) / **Definition:** Parameter Problem error messages are sent by nodes when packets are incorrectly generated. / **Port:** Local: 68<br />Remote: 67 / **Protocol:** ICMPv6 / **Direction:** Out
  - **Rule:** Router Advertisement (ICMPv6-In) / **Definition:** Router Advertisement messages are sent by routers to other nodes for stateless auto-configuration. / **Port:** Local: 68<br />Remote: 67 / **Protocol:** ICMPv6 / **Direction:** In
  - **Rule:** Router Advertisement (ICMPv6-Out) / **Definition:** Router Advertisement messages are sent by routers to other nodes for stateless auto-configuration. / **Port:** Local: 68<br />Remote: 67 / **Protocol:** ICMPv6 / **Direction:** Out
  - **Rule:** Router Solicitation (ICMPv6-In) / **Definition:** Router Solicitation messages are sent by nodes seeking routers to provide stateless auto-configuration. / **Port:** Local: 68<br />Remote: 67 / **Protocol:** ICMPv6 / **Direction:** In
  - **Rule:** Router Solicitation (ICMPv6-Out) / **Definition:** Router Solicitation messages are sent by nodes seeking routers to provide stateless auto-configuration. / **Port:** Local: 68<br />Remote: 67 / **Protocol:** ICMPv6 / **Direction:** Out
  - **Rule:** Core Networking - Teredo (UDP-In) / **Definition:** Inbound UDP rule to allow Teredo edge traversal. This technology provides address assignment and automatic tunneling for unicast IPv6 traffic when an IPv6/IPv4 host is located behind an IPv4 network address translator. / **Port:** Local: Teredo<br />Remote: Any / **Protocol:** UDP / **Direction:** In
  - **Rule:** Core Networking - Teredo (UDP-Out) / **Definition:** Outbound UDP rule to allow Teredo edge traversal. This technology provides address assignment and automatic tunneling for unicast IPv6 traffic when an IPv6/IPv4 host is located behind an IPv4 network address translator. / **Port:** Local: Any<br />Remote: Any / **Protocol:** UDP / **Direction:** Out
  - **Rule:** Time Exceeded (ICMPv6-In) / **Definition:** Time Exceeded error messages are generated from any node that a packet traverses if the Hop Limit value is decremented to zero at any point on the path. / **Port:** Local: 68<br />Remote: 67 / **Protocol:** ICMPv6 / **Direction:** In
  - **Rule:** Time Exceeded (ICMPv6-Out) / **Definition:** Time Exceeded error messages are generated from any node that a packet traverses if the Hop Limit value is decremented to zero at any point on the path. / **Port:** Local: 68<br />Remote: 67 / **Protocol:** ICMPv6 / **Direction:** Out



------

## Delivery Optimization
<a name="delivery-optimization"></a>



- **Windows Server 2019 Windows Server 2022**
  - **Rule:** DeliveryOptimization-TCP-In / **Definition:** Inbound rule to allow Delivery Optimization to connect to remote endpoints. / **Port:** Local: 7680<br />Remote: Any / **Protocol:** TCP / **Direction:** In
  - **Rule:** DeliveryOptimization-UDP-In / **Definition:** Inbound rule to allow Delivery Optimization to connect to remote endpoints. / **Port:** Local: 7680<br />Remote: Any / **Protocol:** UDP / **Direction:** In



## Diag Track
<a name="diag"></a>

------
#### [ Windows Server 2019 and 2022 ]


| OS | Rule | Definition | Port | Protocol | Direction | 
| --- | --- | --- | --- | --- | --- | 
| Windows Server 2019<br />Windows Server 2022 | Connected User Experiences and Telemetry | Unified Telemetry Client Outbound Traffic. | Local: Any<br />Remote: 443 | TCP | Out | 

------
#### [ Windows Server 2016 ]


| OS | Rule | Definition | Port | Protocol | Direction | 
| --- | --- | --- | --- | --- | --- | 
| Windows Server 2016 | Connected User Experiences and Telemetry | Unified Telemetry Client Outbound Traffic. | Local: Any<br />Remote: Any | TCP | Out | 

------

## DIAL Protocol Server
<a name="dial-protocol"></a>


| OS | Rule | Definition | Port | Protocol | Direction | 
| --- | --- | --- | --- | --- | --- | 
| Windows Server 2016<br />Windows Server 2019<br />Windows Server 2022 | DIAL protocol server (HTTP-In) | Inbound rule for DIAL protocol server to allow remote control of Apps using HTTP.  | Local: 10247<br />Remote: Any | TCP | In | 

## File and Printer Sharing
<a name="file-and-print"></a>



- ** Windows Server 2012 Windows Server 2012 R2**
  - **Rule:** File and Printer Sharing (Echo Request - ICMPv4-In) / **Definition:** Echo Request messages are sent as ping requests to other nodes. / **Port:** Local: 5355<br />Remote: Any / **Protocol:** ICMPv4 / **Direction:** In
  - **Rule:** File and Printer Sharing (Echo Request - ICMPv4-Out) / **Definition:** Echo Request messages are sent as ping requests to other nodes. / **Port:** Local: 5355<br />Remote: Any / **Protocol:** ICMPv4 / **Direction:** Out
  - **Rule:** File and Printer Sharing (Echo Request - ICMPv6-In) / **Definition:** Echo Request messages are sent as ping requests to other nodes. / **Port:** Local: 5355<br />Remote: Any / **Protocol:** ICMPv6 / **Direction:** In
  - **Rule:** File and Printer Sharing (Echo Request - ICMPv6-Out) / **Definition:** Echo Request messages are sent as ping requests to other nodes. / **Port:** Local: 5355<br />Remote: Any / **Protocol:** ICMPv6 / **Direction:** Out
  - **Rule:** File and Printer Sharing (LLMNR-UDP-In) / **Definition:** Inbound rule for File and Printer Sharing to allow Link Local Multicast Name Resolution.  / **Port:** Local: 5355<br />Remote: Any / **Protocol:** UDP / **Direction:** In
  - **Rule:** File and Printer Sharing (LLMNR-UDP-Out) / **Definition:** Outbound rule for File and Printer Sharing to allow Link Local Multicast Name Resolution. / **Port:** Local: Any<br />Remote: 5355 / **Protocol:** UDP / **Direction:** Out
  - **Rule:** File and Printer Sharing (NB-Datagram-In) / **Definition:** Inbound rule for File and Printer Sharing to allow NetBIOS Datagram transmission and reception.  / **Port:** Local: 138<br />Remote: Any / **Protocol:** UDP / **Direction:** In
  - **Rule:** File and Printer Sharing (NB-Datagram-Out) / **Definition:** Outbound rule for File and Printer Sharing to allow NetBIOS Datagram transmission and reception.  / **Port:** Local: Any<br />Remote: 138 / **Protocol:** UDP / **Direction:** Out
  - **Rule:** File and Printer Sharing (NB-Name-In) / **Definition:** Inbound rule for File and Printer Sharing to allow NetBIOS Name Resolution.  / **Port:** Local: 137<br />Remote: Any / **Protocol:** UDP / **Direction:** In
  - **Rule:** File and Printer Sharing (NB-Name-Out) / **Definition:** Outbound rule for File and Printer Sharing to allow NetBIOS Name Resolution.  / **Port:** Local: Any<br />Remote: 137 / **Protocol:** UDP / **Direction:** Out
  - **Rule:** File and Printer Sharing (NB-Session-In) / **Definition:** Inbound rule for File and Printer Sharing to allow NetBIOS Session Service connections.  / **Port:** Local: 139<br />Remote: Any / **Protocol:** TCP / **Direction:** In
  - **Rule:** File and Printer Sharing (NB-Session-Out) / **Definition:** Outbound rule for File and Printer Sharing to allow NetBIOS Session Service connections.  / **Port:** Local: Any<br />Remote: 139 / **Protocol:** TCP / **Direction:** Out
  - **Rule:** File and Printer Sharing (SMB-In) / **Definition:** Inbound rule for File and Printer Sharing to allow Server Message Block transmission and reception via Named Pipes.  / **Port:** Local: 445<br />Remote: Any / **Protocol:** TCP / **Direction:** In
  - **Rule:** File and Printer Sharing (SMB-Out) / **Definition:** Outbound rule for File and Printer Sharing to allow Server Message Block transmission and reception via Named Pipes.  / **Port:** Local: Any<br />Remote: 445 / **Protocol:** TCP / **Direction:** Out
  - **Rule:** File and Printer Sharing (Spooler Service - RPC) / **Definition:** Inbound rule for File and Printer Sharing to allow the Print Spooler Service to communicate via TCP/RPC. / **Port:** Local: RPC<br />Remote: Any / **Protocol:** TCP / **Direction:** In
  - **Rule:** File and Printer Sharing (Spooler Service - RPC-EPMAP) / **Definition:** Inbound rule for the RPCSS service to allow RPC/TCP traffic for the Spooler Service. / **Port:** Local: RPC-EPMap<br />Remote: Any / **Protocol:** TCP / **Direction:** In



## File Server Remote Management
<a name="file-server-remote"></a>



- ** Windows Server 2012 Windows Server 2012 R2**
  - **Rule:** File Server Remote Management (DCOM-In) / **Definition:** Inbound rule to allow DCOM traffic to manage the File Services role. / **Port:** Local: 135<br />Remote: Any / **Protocol:** TCP / **Direction:** In
  - **Rule:** File Server Remote Management (SMB-In) / **Definition:** Inbound rule to allow SMB traffic to manage the File Services role. / **Port:** Local: 445<br />Remote: Any / **Protocol:** TCP / **Direction:** In
  - **Rule:** WMI-In / **Definition:** Inbound rule to allow WMI traffic to manage the File Services role. / **Port:** Local: RPC<br />Remote: Any / **Protocol:** TCP / **Direction:** In



## ICMP v4 All
<a name="icmp-v4"></a>


| OS | Rule | Port | Protocol | Direction | 
| --- | --- | --- | --- | --- | 
| Windows Server 2012<br />Windows Server 2012 R2 | All ICMP v4 | Local: 139<br />Remote: Any | ICMPv4 | In | 

## Microsoft Edge
<a name="protocol-edge"></a>


| OS | Rule | Port | Protocol | Direction | 
| --- | --- | --- | --- | --- | 
| Windows Server 2022 | Microsoft Edge (mDNS-In) | Local: 5353<br />Remote: Any | UDP | In | 

## Microsoft Media Foundation Network Source
<a name="protocol-media-foundation"></a>



- **Windows Server 2022 **
  - **Rule:** Microsoft Media Foundation Network Source IN [TCP 554]  / **Port:** Local: 554, 8554-8558<br />Remote: Any / **Protocol:** TCP / **Direction:** In
  - **Rule:** Microsoft Media Foundation Network Source IN [UDP 5004-5009]  / **Port:** Local: 5000-5020<br />Remote: Any / **Protocol:** UDP / **Direction:** In
  - **Rule:** Microsoft Media Foundation Network Source OUT [TCP ALL] / **Port:** Local: Any<br />Remote: 554, 8554-8558 / **Protocol:** TCP / **Direction:** In



## Multicast
<a name="multicast"></a>

------
#### [ Windows Server 2019 and 2022 ]



- ** Windows Server 2019 Windows Server 2022 **
  - **Rule:** mDNS (UDP-In) / **Definition:** Inbound rule for mDNS traffic. / **Port:** Local: 5353Remote: Any / **Protocol:** UDP / **Direction:** In
  - **Rule:** mDNS (UDP-Out) / **Definition:** Outbound rule for mDNS traffic. / **Port:** Local: AnyRemote: 5353 / **Protocol:** UDP / **Direction:** Out



------
#### [ Windows Server 2016 ]



- **Windows Server 2016**
  - **Rule:** mDNS (UDP-In) / **Definition:** Inbound rule for mDNS traffic. / **Port:** Local: mDNSRemote: Any / **Protocol:** UDP / **Direction:** In
  - **Rule:** mDNS (UDP-Out) / **Definition:** Outbound rule for mDNS traffic. / **Port:** Local: 5353Remote: Any / **Protocol:** UDP / **Direction:** Out



------

## Remote Desktop
<a name="remote-desktop"></a>

------
#### [ Windows Server 2012 R2, 2016, 2019, and 2022 ]



- ** Windows Server 2012 R2 Windows Server 2016 Windows Server 2019 Windows Server 2022 **
  - **Rule:** Remote Desktop - Shadow (TCP-In) / **Definition:** Inbound rule for the Remote Desktop service to allow shadowing of an existing Remote Desktop session.  / **Port:** Local: Any<br />Remote: Any / **Protocol:** TCP / **Direction:** In
  - **Rule:** Remote Desktop - User Mode (TCP-In) / **Definition:** Inbound rule for the Remote Desktop service to allow RDP traffic.  / **Port:** Local: 3389<br />Remote: Any / **Protocol:** TCP / **Direction:** In
  - **Rule:** Remote Desktop - User Mode (UDP-In) / **Definition:** Inbound rule for the Remote Desktop service to allow RDP traffic.  / **Port:** Local: 3389<br />Remote: Any / **Protocol:** UDP / **Direction:** In



------
#### [ Windows Server 2012 ]



- **Windows Server 2012**
  - **Rule:** Remote Desktop - User Mode (TCP-In) / **Definition:** Inbound rule for the Remote Desktop service to allow RDP traffic.  / **Port:** Local: 3389<br />Remote: Any / **Protocol:** TCP / **Direction:** In
  - **Rule:** Remote Desktop - User Mode (UDP-In) / **Definition:** Inbound rule for the Remote Desktop service to allow RDP traffic.  / **Port:** Local: 3389<br />Remote: Any / **Protocol:** UDP / **Direction:** In



------

## WindowsDevice Management
<a name="device-management"></a>

------
#### [ Windows Server 2022 ]



- **Windows Server 2022**
  - **Rule:** WindowsDevice Management Certificate Installer (TCP out) / **Definition:** Allow outbound TCP traffic from WindowsDevice Management Certificate Installer. / **Port:** Local: Any<br />Remote: Any / **Protocol:** TCP / **Direction:** Out
  - **Rule:** WindowsDevice Management Device Enroller (TCP out) / **Definition:** Allow outbound TCP traffic from WindowsDevice Management Device Enroller. / **Port:** Local: Any<br />Remote: 80, 443 / **Protocol:** TCP / **Direction:** Out
  - **Rule:** WindowsDevice Management Enrollment Service (TCP out) / **Definition:** Allow outbound TCP traffic from WindowsDevice Management Enrollment Service. / **Port:** Local: Any<br />Remote: Any / **Protocol:** TCP / **Direction:** Out
  - **Rule:** WindowsDevice Management Sync Client (TCP out) / **Definition:** Allow outbound TCP traffic from WindowsDevice Management Sync Client. / **Port:** Local: Any<br />Remote: Any / **Protocol:** TCP / **Direction:** Out



------
#### [ Windows Server 2019 ]



- **Windows Server 2019**
  - **Rule:** WindowsDevice Management Certificate Installer (TCP out) / **Definition:** Allow outbound TCP traffic from WindowsDevice Management Certificate Installer. / **Port:** Local: Any<br />Remote: Any / **Protocol:** TCP / **Direction:** Out
  - **Rule:** WindowsDevice Management Enrollment Service (TCP out) / **Definition:** Allow outbound TCP traffic from WindowsDevice Management Enrollment Service. / **Port:** Local: Any<br />Remote: Any / **Protocol:** TCP / **Direction:** Out
  - **Rule:** WindowsDevice Management Sync Client (TCP out) / **Definition:** Allow outbound TCP traffic from WindowsDevice Management Sync Client. / **Port:** Local: Any<br />Remote: Any / **Protocol:** TCP / **Direction:** Out
  - **Rule:** WindowsEnrollment WinRT (TCP Out) / **Definition:** Allow outbound TCP traffic from WindowsEnrollment WinRT. / **Port:** Local: Any<br />Remote: Any / **Protocol:** TCP / **Direction:** Out



------

## WindowsFeature Experience Pack
<a name="remote-management"></a>


| OS | Rule | Definition | Port | Protocol | Direction | 
| --- | --- | --- | --- | --- | --- | 
| Windows Server 2022 | WindowsFeature Experience Pack | WindowsFeature Experience Pack. |  | Any | Out | 

## WindowsFirewall Remote Management
<a name="firewall-remote"></a>



- ** Windows Server 2012 R2**
  - **Rule:** WindowsFirewall Remote Management (RPC) / **Definition:** Inbound rule for the WindowsFirewall to be remotely managed via RPC/TCP. / **Port:** Local: RPC<br />Remote: Any / **Protocol:** TCP / **Direction:** In
  - **Rule:** WindowsFirewall Remote Management (RPC-EPMAP) / **Definition:** Inbound rule for the RPCSS service to allow RPC/TCP traffic for the WindowsFirewall. / **Port:** Local: RPC-EPMap<br />Remote: Any / **Protocol:** TCP / **Direction:** In



## WindowsRemote Management
<a name="remote-management"></a>


| OS | Rule | Definition | Port | Protocol | Direction | 
| --- | --- | --- | --- | --- | --- | 
| Windows Server 2012<br />Windows Server 2012 R2<br />Windows Server 2016<br />Windows Server 2019<br />Windows Server 2022 | WindowsRemote Management (HTTP-In) | Inbound rule for WindowsRemote Management via WS-Management.  | Local: 5985<br />Remote: Any | TCP | In | 

 For more information about Amazon EC2 security groups, see [Amazon EC2 Security Groups for WindowsInstances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-security-groups.html).