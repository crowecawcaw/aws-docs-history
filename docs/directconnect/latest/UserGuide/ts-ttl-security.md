

# Troubleshoot BGP TTL security (GTSM) issues
<a name="ts-ttl-security"></a>

If your BGP session with Direct Connect fails to establish, BGP TTL security on your router might be the cause. Direct Connect uses single-hop external BGP (eBGP) on virtual interfaces and sends BGP packets with an IP Time-to-Live (TTL) value of 1. Some routers support BGP TTL security, also known as the Generalized TTL Security Mechanism (GTSM). For more information about GTSM, see [RFC 5082](https://datatracker.ietf.org/doc/html/rfc5082) on the Internet Engineering Task Force (IETF) website. When this feature is enabled (for example, with the `neighbor ttl-security hops` command), your router expects incoming BGP packets to arrive with a high TTL value. Your router discards the low-TTL packets that AWS sends.

**BGP session remains in the Active or OpenSent state**  
*Symptoms*: The BGP session does not establish and remains in the Active or OpenSent state. This occurs even though a packet capture on your device shows the AWS BGP packets arriving on the interface.  
*Cause*: BGP TTL security is configured on the BGP neighbor facing Direct Connect, causing your router to discard the BGP packets that AWS sends with a TTL of 1.  
*Resolution*:  

1. Remove the TTL security (GTSM) configuration from the BGP neighbor facing Direct Connect.

1. Verify that the BGP session state transitions to Established.
Direct Connect uses single-hop eBGP and does not support multihop eBGP on virtual interfaces by default. The single-hop protection that GTSM provides is already inherent in this peering.

**Note**  
Use this guidance for the BGP session on a Direct Connect virtual interface. BGP peering to a Transit Gateway over a transit virtual interface uses multihop BGP and is configured differently.

If the BGP session does not establish after you remove the TTL security configuration, [contact AWS Support](https://aws.amazon.com/support/createCase).