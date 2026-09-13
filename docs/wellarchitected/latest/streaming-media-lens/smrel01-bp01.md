

# SMREL01-BP01 Implement redundant live contribution paths with resilient protocols
<a name="smrel01-bp01"></a>

Design your live contribution architecture with multiple redundant paths using protocols that provide automatic error recovery and packet retransmission capabilities.

**Desired outcome:**
+ Live streams continue without interruption even when individual contribution sources, encoders, or network paths fail.

**Benefits of establishing this best practice:**
+ Removes single points of failure in live contribution
+ Maintains stream quality over unreliable networks
+ Reduces viewer-impacting outages from contribution failures
+ Enables smooth failover between contribution sources

**Level of risk exposed if this best practice is not established:** High

## Implementation guidance
<a name="implementation-guidance"></a>

Deploy contribution encoders in geographically diverse locations with redundant network connectivity. Use contribution protocols that support automatic retransmission of lost packets rather than relying solely on forward error correction. Implement dual-path transmission where identical packet streams travel over separate network routes, allowing reconstruction of lost data from either path.

### Implementation steps
<a name="implementation-steps"></a>

1. **Deploy redundant contribution encoders:** Place encoders in different physical locations with diverse network connectivity to AWS. Maintain geographic separation between encoder sites to avoid regional outages. Consider Direct Connect for dedicated network paths with consistent bandwidth and lower latency. Configure reliable internet connectivity for each encoder location and implement diverse network paths between encoder locations and AWS infrastructure.

1. **Configure contribution protocols with packet retransmission:** Use SRT (Secure Reliable Transport) or RIST (Reliable Internet Stream Transport) for automatic packet recovery. Configure appropriate buffer sizes based on network latency and jitter requirements. Avoid protocols like plain Real-time Transport Protocol (RTP) that lack retransmission capabilities.

1. **Create MediaConnect flows in different Availability Zones:** Set up primary MediaConnect flow in Availability Zone A and secondary MediaConnect flow in Availability Zone B for each contribution path. Configure identical flow settings for both paths.

1. **Configure MediaConnect source failover:** For SRT sources, configure failover mode only (merge mode not supported for SRT). For RIST or RTP sources, choose between merge mode for smooth switching or failover mode for primary and backup operation. If using merge mode, verify that sources are binary identical and comply with Society of Motion Picture and Television Engineers (SMPTE) ST 2022-7 standard.

1. **Configure automatic input failover in MediaLive:** Create a MediaLive channel with automatic input failover enabled. Set primary input preference for automatic failback to primary source. Configure failover conditions with thresholds higher than 500ms to account for MediaConnect failover timing. Enable input loss detection and audio silence detection as failover triggers.

1. **Implement cross-region resilience:** Replicate MediaConnect flows and MediaLive channels in a secondary AWS Region. Configure MediaConnect inter-region distribution to send contribution feeds to the secondary region. Set up automatic failover logic to activate secondary region processing when the primary region fails. Keep MediaLive channel configuration identical between primary and secondary regions.

1. **Set up ongoing monitoring:** Monitor MediaConnect flow health metrics and packet loss rates across all regions using Amazon CloudWatch. Create CloudWatch alarms for contribution signal loss and quality degradation. Configure Amazon Simple Notification Service (SNS) notifications for immediate alerting on failover events. Implement cross-region monitoring dashboards for complete visibility.

## Resources
<a name="resources"></a>

**Related documents**
+ AWS Elemental MediaConnect User Guide
+ SMPTE 2022-7 Implementation Guide

**Related services**
+ [AWS Elemental MediaConnect](https://aws.amazon.com/mediaconnect/)
+ [Direct Connect](https://aws.amazon.com/directconnect/)
+ [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/)