

# BGP-specific settings
<a name="bgp-specific-settings"></a>

The following Border Gateway Protocol (BGP) settings are used by Direct Connect:

## BGP settings
<a name="bgp-settings"></a>


| Setting | Value | Notes | 
| --- | --- | --- | 
| Default hold timer | 90 seconds |  | 
| Minimum hold timer | 3 seconds | A hold value of 0 is not supported. | 
| Default keepalive timer | 30 seconds |  | 
| Minimum keepalive timer | 1 second |  | 
| Graceful restart timer | 120 seconds | We recommend that you do not configure graceful restart and BFD at the same time. | 
| BFD liveness detection minimum interval | 300 ms |  | 
| BFD minimum multiplier | 3 |  | 
| BGP Packet TTL Value | 1 | Your device must support accepting BGP packets with a TTL value of 1. Direct Connect currently does not support multihop BGP or setting a different TTL value. | 

BGP timers negotiate down to the lowest configured value between the peers. BFD intervals use the largest mutually agreed upon timer (the slower rate), where the actual transmission rate is the maximum of the local minimum transmission interval (`DesiredMinTxInterval`) and the peer's minimum receive interval (`RequiredMinRxInterval`). Because transmission rates are negotiated independently for each direction, BFD intervals can be asymmetric. The final failure detection time is calculated by multiplying the negotiated transmission interval by the local detection multiplier.

## Autonomous System Number (ASN) ranges
<a name="asn-ranges"></a>

When configuring your virtual interface you must set an ASN. Direct Connect supports 2-byte and 4-byte ASNs. For more information, see [Long ASN support in Direct Connect](long-asn-support.md). The following ranges are supported:

**Customer-side ASN range**: 1 to 4,294,967,294
+ ASNs: 1 to 2,147,483,647
+ Long ASNs: 1 to 4,294,967,294

**Private ASN ranges**:
+ Private ASNs: 64,512 to 65,534
+ Private long ASNs: 4,200,000,000 to 4,294,967,294

**Note**  
For public virtual interfaces, your ASN must be either a private ASN or a public ASN already registered and allowed for use with the virtual interface.