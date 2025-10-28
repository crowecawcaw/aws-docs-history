# Best practices for an AWS Site-to-Site VPN customer gateway device

###### Use IKEv2

We strongly recommend using IKEv2 for your Site-to-Site VPN connection. IKEv2 is a simpler, more robust, and more secure protocol than IKEv1. You should only use IKEv1 if your customer gateway device does not support IKEv2. For more details on the differences between IKEv1 and IKEv2, see [Appendix A of RFC7296](https://www.rfc-editor.org/rfc/rfc7296#appendix-A "https://www.rfc-editor.org/rfc/rfc7296#appendix-A").

###### Reset the "Don't Fragment (DF)" flag on packets

Some packets carry a flag, known as the Don't Fragment (DF) flag, which indicates that the packet should not be fragmented. If the packets carry the flag, the gateways generate an ICMP Path MTU Exceeded message. In some cases, applications do not contain adequate mechanisms for processing these ICMP messages and for reducing the amount of data transmitted in each packet. Some VPN devices can override the DF flag and fragment packets unconditionally as required. If your customer gateway device has this ability, we recommend that you use it as appropriate. See [RFC 791](https://datatracker.ietf.org/doc/html/rfc791 "https://datatracker.ietf.org/doc/html/rfc791") for more details.

###### Fragment IP packets before encryption

If packets being sent to over your Site-to-Site VPN connection exceed the MTU size, they must be fragmented. To avoid decreased performance, we recommend that you configure your customer gateway device to fragment the packets _before_ they are encrypted. Site-to-Site VPN will then reassemble any fragmented packets before forwarding them to the next destination, in order to achieve higher packet-per-second flows through the AWS network. See [RFC 4459](https://datatracker.ietf.org/doc/html/rfc4459 "https://datatracker.ietf.org/doc/html/rfc4459") for more details.

###### Ensure packet size does not exceed MTU for destination networks

Since Site-to-Site VPN will reassemble any fragmented packets received from your customer
gateway device before forwarding to the next destination, keep in mind, there may be
packet size/MTU considerations for destination networks where these packets get
forwarded next, such as over AWS Direct Connect, or with certain protocols, such as
Radius.

###### Adjust MTU and MSS sizes according to the algorithms in use

TCP packets are often the most common type of packet across IPsec tunnels. Site-to-Site VPN supports a maximum transmission unit (MTU) of 1446 bytes and a corresponding maximum segment size (MSS) of 1406 bytes. However, encryption algorithms have varying header sizes and can prevent the ability to achieve these maximum values. To obtain optimal performance by avoiding fragmentation, we recommend that you set the MTU and MSS based specifically on the algorithms being used.

Use the following table to set your MTU/MSS to avoid fragmentation and achieve optimal performance:

| Encryption Algorithm | Hashing Algorithm | NAT-Traversal | MTU  | MSS (IPv4) | MSS (IPv6-in-IPv4) |
| -------------------- | ----------------- | ------------- | ---- | ---------- | ------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| AES-GCM-16           | N/A               | disabled      | 1446 | 1406       | 1386               |
| AES-GCM-16           | N/A               | enabled       | 1438 | 1398       | 1378               |
| AES-CBC              | SHA1/SHA2-256     | disabled      | 1438 | 1398       | 1378               |
| AES-CBC              | SHA1/SHA2-256     | enabled       | 1422 | 1382       | 1362               |
| AES-CBC              | SHA2-384          | disabled      | 1422 | 1382       | 1362               |
| AES-CBC              | SHA2-384          | enabled       | 1422 | 1382       | 1362               |
| AES-CBC              | SHA2-512          | disabled      | 1422 | 1382       | 1362               |
| AES-CBC              | SHA2-512          | enabled       | 1406 | 1366       | 1346               | ###### Note The AES-GCM algorithms cover both encryption and authentication, so there is no distinct authentication algorithm choice which would affect MTU. ###### Disable IKE unique IDs Some customer gateway devices support a setting which ensures that at most, one Phase 1 security association exists per tunnel configuration. This setting can result in inconsistent Phase 2 states between VPN peers. If your customer gateway device supports this setting, we recommend disabling it. |
