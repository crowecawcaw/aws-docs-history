

# Using metrics to troubleshoot problems with your MediaConnect flow
<a name="monitor-with-cloudwatch-metrics-troubleshooting"></a>

You can monitor the health of your stream by reviewing the metrics that AWS Elemental MediaConnect sends to CloudWatch. In particular, if you encounter a problem on your MediaConnect flow, these metrics can help you isolate the problem. The specific metrics to watch depend on the protocol that your source uses. Review the lists below, which are sorted by source protocol.

**Topics**
+ [Metrics to watch if your source uses the RIST protocol](#monitor-with-cloudwatch-metrics-troubleshooting-rist)
+ [Metrics to watch if your source uses the RTP protocol](#monitor-with-cloudwatch-metrics-troubleshooting-rtp)
+ [Metrics to watch if your source uses the RTP-FEC protocol](#monitor-with-cloudwatch-metrics-troubleshooting-rtp-fec)
+ [Metrics to watch if your source uses the SRT protocol](#monitor-with-cloudwatch-metrics-troubleshooting-SRT)
+ [Metrics to watch if your source uses the Zixi push protocol](#monitor-with-cloudwatch-metrics-troubleshooting-zixi-push)
+ [Metrics to watch if your source comes from an entitlement](#monitor-with-cloudwatch-metrics-troubleshooting-entitlement)
+ [Metrics to watch if you are using gateways](#monitor-with-cloudwatch-metrics-troubleshooting-gateway)

## Metrics to watch if your source uses the RIST protocol
<a name="monitor-with-cloudwatch-metrics-troubleshooting-rist"></a>

If the protocol of your source is RIST, watch the metrics below to evaluate the health of your source.
+ `ARQRecovered`
+ `ARQRequests`
+ `DroppedPackets`
+ `NotRecoveredPackets`
+ `OverflowPackets`
+ `PacketLossPercent`
+ `RecoveredPackets`
+ `RoundTripTime`
+ `TotalPackets`

## Metrics to watch if your source uses the RTP protocol
<a name="monitor-with-cloudwatch-metrics-troubleshooting-rtp"></a>

If the protocol of your source is RTP, watch the metrics below to evaluate the health of your source.
+ `DroppedPackets`
+ `OverflowPackets`
+ `RoundTripTime`
+ `TotalPackets`

## Metrics to watch if your source uses the RTP-FEC protocol
<a name="monitor-with-cloudwatch-metrics-troubleshooting-rtp-fec"></a>

If the protocol of your source is RTP-FEC, watch the metrics below to evaluate the health of your source.
+ `DroppedPackets`
+ `FECPackets`
+ `FECRecovered`
+ `NotRecoveredPackets`
+ `OverflowPackets`
+ `RecoveredPackets`
+ `RoundTripTime`
+ `TotalPackets`

## Metrics to watch if your source uses the SRT protocol
<a name="monitor-with-cloudwatch-metrics-troubleshooting-SRT"></a>

If the protocol of your source is SRT (listener or caller), watch the metrics below to evaluate the health of your source.
+ `ARQRecovered`
+ `ARQRequests`
+ `DroppedPackets`
+ `NotRecoveredPackets`
+ `OverflowPackets`
+ `RecoveredPackets`
+ `RoundTripTime`
+ `TotalPackets`

## Metrics to watch if your source uses the Zixi push protocol
<a name="monitor-with-cloudwatch-metrics-troubleshooting-zixi-push"></a>

If the protocol of your source is Zixi push, watch the metrics below to evaluate the health of your source.
+ `ARQRecovered`
+ `ARQRequests`
+ `DroppedPackets`
+ `FECPackets`
+ `FECRecovered`
+ `NotRecoveredPackets`
+ `OverflowPackets`
+ `RecoveredPackets`
+ `RoundTripTime`
+ `TotalPackets`

## Metrics to watch if your source comes from an entitlement
<a name="monitor-with-cloudwatch-metrics-troubleshooting-entitlement"></a>

If your source comes from an entitlement that was granted to your account by another AWS account, watch the metrics below to evaluate the health of your source.
+ `ARQRecovered`
+ `ARQRequests`
+ `DroppedPackets`
+ `FECPackets`
+ `FECRecovered`
+ `NotRecoveredPackets`
+ `OverflowPackets`
+ `RecoveredPackets`
+ `RoundTripTime`
+ `TotalPackets`

## Metrics to watch if you are using gateways
<a name="monitor-with-cloudwatch-metrics-troubleshooting-gateway"></a>

Watch the metrics below to evaluate the health of your gateway.

### Metrics to watch if you are using a gateway with an ingress bridge
<a name="monitor-with-cloudwatch-metrics-troubleshooting-gateway-ingress"></a>

Watch the metrics below to evaluate the health of your gateway's ingress bridge. The recommended ingress bridge troubleshooting metrics are separated by protocol.
+ RTP
  + `IngressBridgeTotalPackets`
  + `IngressBridgeDroppedPackets`
  + `IngressBridgeSourceTotalPackets`
  + `IngressBridgeSourceDroppedPackets`
  + `IngressBridgeSourceOverflowPackets`
  + `IngressBridgeSourceRoundTripTime`
+ RTP-FEC
  + `IngressBridgeTotalPackets`
  + `IngressBridgeDroppedPackets`
  + `IngressBridgeRecoveredPackets`
  + `IngressBridgeNotRecoveredPackets`
  + `IngressBridgeSourceTotalPackets`
  + `IngressBridgeSourceDroppedPackets`
  + `IngressBridgeSourceRecoveredPackets`
  + `IngressBridgeSourceNotRecoveredPackets`
  + `IngressBridgeSourceOverflowPackets`
  + `IngressBridgeSourceFECPackets`
  + `IngressBridgeSourceFECRecovered`
  + `IngressBridgeSourceRoundTripTime`
+ UDP
  + `IngressBridgeTotalPackets`
  + `IngressBridgeSourceTotalPackets`
  + `IngressBridgeSourceOverflowPackets`

### Metrics to watch if you are using a gateway with an egress bridge
<a name="monitor-with-cloudwatch-metrics-troubleshooting-gateway-egress"></a>

Watch the metrics below to evaluate the health of your gateway's egress bridge.
+ `EgressBridgeTotalPackets`
+ `EgressBridgeDroppedPackets`
+ `EgressBridgeRecoveredPackets`
+ `EgressBridgeNotRecoveredPackets`
+ `EgressBridgeSourceTotalPackets`
+ `EgressBridgeSourceDroppedPackets`
+ `EgressBridgeSourceRecoveredPackets`
+ `EgressBridgeSourceNotRecoveredPackets`