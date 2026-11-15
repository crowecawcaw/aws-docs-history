

# AWS Network Firewall metrics in Amazon CloudWatch
<a name="monitoring-cloudwatch"></a>

You can monitor AWS Network Firewall using CloudWatch, which collects raw data and processes it into readable, near real-time metrics. CloudWatch stores your metrics for 15 months, so that you can access historical information for added perspective on how your web application or service is performing. You can also set alarms that watch for certain thresholds, and send notifications or take actions when those thresholds are met. For more information, see the [Amazon CloudWatch User Guide](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/).

**Note**  
Access to metrics in CloudWatch depends on whether you are a firewall owner or VPC endpoint association owner. A firewall owner can view metrics for firewalls they own, including VPC endpoint associations associated with the firewall. If a VPC endpoint association owner also owns the primary firewall endpoint, they can view metrics in CloudWatch for both the firewall's primary endpoints and any associated secondary endpoints (VPC endpoint associations). However, if a VPC endpoint association owner does not also own the firewall endpoint, they cannot access or view metrics in CloudWatch. For information, see [Considerations for working with firewalls and firewall endpoints](firewall-and-firewall-endpoints-considerations.md).

Use the following procedures to view the metrics for Network Firewall.

**To view metrics using the CloudWatch console**

Metrics are grouped first by the service namespace, and then by the various dimension combinations within each namespace. The CloudWatch namespace for Network Firewall is AWS/NetworkFirewall.

1. Open the CloudWatch console at [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/).

1. In the navigation pane, choose **Metrics**.

1. On the **All metrics** tab, select the Region and then select `AWS/NetworkFirewall`.

**To view metrics using the AWS CLI**
+ For Network Firewall, at a command prompt use the following command:

  ```
  1. aws cloudwatch list-metrics --namespace "AWS/NetworkFirewall" 
  ```

## AWS Network Firewall metrics
<a name="metrics"></a>

The AWS/NetworkFirewall namespace includes the following metrics. The metrics that a firewall reports depend on whether it uses a Next Generation policy or a Classic Network Firewall policy. For information about the policy types, see [AWS Network Firewall firewall policy versions](firewall-policy-versions.md).
<a name="metrics-policy-v2"></a>
**Next Generation policy metrics**  
A firewall that uses a Next Generation policy reports the following metrics. Each metric carries an `Engine` dimension that identifies the inspection engine it's for: `Firewall` for the firewall engine, `IPS` for the IPS engine, `System` for counts that aren't specific to one engine, and `TLS` for TLS inspection. The packet-verdict metrics are reported separately for each engine, so you can see each engine's effect on your traffic. For the `Engine` dimension, see [AWS Network Firewall dimensions](#metricdimensions). For information about Next Generation policies, see [Next Generation policies](firewall-policies-v2.md).


**Next Generation policy CloudWatch metrics**  

| Metric | Description | Engine dimension | 
| --- | --- | --- | 
| `PassedPackets` | Number of packets that the firewall engine allowed to pass.<br />Reporting criteria: There is a nonzero value.<br />Valid statistics: Sum | `Firewall` | 
| `PassedPackets` | Number of packets that the IPS engine allowed to pass.<br />Reporting criteria: There is a nonzero value.<br />Valid statistics: Sum | `IPS` | 
| `DroppedPackets` | Number of packets that the firewall engine dropped.<br />Reporting criteria: There is a nonzero value.<br />Valid statistics: Sum | `Firewall` | 
| `DroppedPackets` | Number of packets that the IPS engine dropped.<br />Reporting criteria: There is a nonzero value.<br />Valid statistics: Sum | `IPS` | 
| `RejectedPackets` | Number of packets that the firewall engine rejected.<br />Reporting criteria: There is a nonzero value.<br />Valid statistics: Sum | `Firewall` | 
| `RejectedPackets` | Number of packets that the IPS engine rejected.<br />Reporting criteria: There is a nonzero value.<br />Valid statistics: Sum | `IPS` | 
| `TLSPassedPackets` | Number of TLS-inspected packets that the firewall engine allowed to pass.<br />Reporting criteria: There is a nonzero value.<br />Valid statistics: Sum | `Firewall` | 
| `TLSPassedPackets` | Number of TLS-inspected packets that the IPS engine allowed to pass.<br />Reporting criteria: There is a nonzero value.<br />Valid statistics: Sum | `IPS` | 
| `TLSDroppedPackets` | Number of TLS-inspected packets that the firewall engine dropped.<br />Reporting criteria: There is a nonzero value.<br />Valid statistics: Sum | `Firewall` | 
| `TLSDroppedPackets` | Number of TLS-inspected packets that the IPS engine dropped.<br />Reporting criteria: There is a nonzero value.<br />Valid statistics: Sum | `IPS` | 
| `TLSRejectedPackets` | Number of TLS-inspected packets that the firewall engine rejected.<br />Reporting criteria: There is a nonzero value.<br />Valid statistics: Sum | `Firewall` | 
| `TLSRejectedPackets` | Number of TLS-inspected packets that the IPS engine rejected.<br />Reporting criteria: There is a nonzero value.<br />Valid statistics: Sum | `IPS` | 
| `FirewallDefaultActionApplied` | Number of packets that the firewall engine's default action was applied to—that is, packets that didn't match any firewall rule at a hook. This counts applications of the default action regardless of whether it allows, drops, or rejects the traffic. For more information, see [Firewall default action](firewall-policy-v2-default-action.md).<br />Reporting criteria: There is a nonzero value.<br />Valid statistics: Sum | `Firewall` | 
| `ReceivedPackets` | Number of packets received by the firewall engine.<br />Reporting criteria: There is a nonzero value.<br />Valid statistics: Sum | `Firewall` | 
| `ReceivedPackets` | Number of packets received, reported at the system level rather than for a specific engine.<br />Reporting criteria: There is a nonzero value.<br />Valid statistics: Sum | `System` | 
| `ReceivedBytes` | Number of bytes received by the firewall engine.<br />Reporting criteria: There is a nonzero value.<br />Valid statistics: Sum | `Firewall` | 
| `ReceivedBytes` | Number of bytes received, reported at the system level rather than for a specific engine.<br />Reporting criteria: There is a nonzero value.<br />Valid statistics: Sum | `System` | 
| `TLSReceivedPackets` | Number of TLS packets received for TLS inspection.<br />Reporting criteria: There is a nonzero value.<br />Valid statistics: Sum | `System` | 
| `TLSErrors` | Number of errors observed by Network Firewall while inspecting SSL/TLS packets. Reported only when the policy has a TLS inspection configuration.<br />Reporting criteria: There is a nonzero value.<br />Valid statistics: Sum | `TLS` | 
| `TLSTimedOutConnections` | Number of SSL/TLS connections that timed out during SSL/TLS inspection by Network Firewall. Reported only when the policy has a TLS inspection configuration.<br />Reporting criteria: There is a nonzero value.<br />Valid statistics: Sum | `TLS` | 
| `TLSRevocationStatusOKConnections` | Number of SSL/TLS connections to TLS servers whose certificates have been confirmed as not revoked. Reported only when the policy has a TLS inspection configuration with certificate revocation checking.<br />Reporting criteria: There is a nonzero value.<br />Valid statistics: Sum | `TLS` | 
| `TLSRevocationStatusRevokedConnections` | Number of SSL/TLS connections to TLS servers whose certificates have been confirmed as revoked. Reported only when the policy has a TLS inspection configuration with certificate revocation checking.<br />Reporting criteria: There is a nonzero value.<br />Valid statistics: Sum | `TLS` | 
| `TLSRevocationStatusUnknownConnections` | Number of SSL/TLS connections to TLS servers whose certificate revocation status is unknown or couldn't be determined by the firewall. This can occur when the OCSP responder for a server certificate returns an unknown status, or when the firewall can't connect to the CRL or OCSP endpoints provided in the certificate. Reported only when the policy has a TLS inspection configuration with certificate revocation checking.<br />Reporting criteria: There is a nonzero value.<br />Valid statistics: Sum | `TLS` | 
| `StreamExceptionPolicyPackets` | Number of packets handled by the stream exception policy. This count isn't specific to one inspection engine.<br />Reporting criteria: There is a nonzero value.<br />Valid statistics: Sum | `System` | 
| `InvalidDroppedPackets` | Number of packets dropped for failing packet validation due to issues with the packet. This count isn't specific to one inspection engine.<br />Reporting criteria: There is a nonzero value.<br />Valid statistics: Sum | `System` | 
| `OtherDroppedPackets` | Number of packets dropped for reasons other than those described by `InvalidDroppedPackets` or `DroppedPackets`, including packets throttled due to bursting traffic. This count isn't specific to one inspection engine.<br />Reporting criteria: There is a nonzero value.<br />Valid statistics: Sum | `System` | 
| `DnsResolvedFlows` | Number of flows whose destination IP address matched an IP address that Amazon Route 53 resolved for an allowed domain. Reported when you use firewall rules that match by Route 53 resolved domain. Counted per flow, at the first verdict for the flow. For more information, see [Generating firewall rules from domain names](firewall-rule-groups-fqdn.md).<br />Reporting criteria: There is a nonzero value.<br />Valid statistics: Sum | `System` | 
| `DnsUnresolvedFlows` | Number of flows whose destination IP address didn't match a resolved IP address for an allowed domain. Counted per flow, at the first verdict for the flow.<br />Reporting criteria: There is a nonzero value.<br />Valid statistics: Sum | `System` | 
| `DnsResolutionErrorFlows` | Number of flows for which the resolved domain validation couldn't be completed. Counted per flow, at the first verdict for the flow.<br />Reporting criteria: There is a nonzero value.<br />Valid statistics: Sum | `System` | 
| `DnsAzUnavailableFlows` | Number of flows whose source Availability Zone wasn't available for resolved domain validation. Counted per flow, at the first verdict for the flow.<br />Reporting criteria: There is a nonzero value.<br />Valid statistics: Sum | `System` | 

In the preceding table, `TLSReceivedPackets` is published with `Engine=System`. The TLS inspection error, timeout, and certificate revocation metrics (such as `TLSErrors`, `TLSTimedOutConnections`, and the certificate revocation status metrics) are published with `Engine=TLS`. Those error, timeout, and revocation metrics behave the same as for a Classic Network Firewall policy, and appear in the rows of the preceding table.
<a name="metrics-classic"></a>
**Classic Network Firewall metrics**  
A firewall that uses a Classic Network Firewall policy reports the following metrics.


| Metric | Description | Applicable resource | 
| --- | --- | --- | 
| `DroppedPackets` | Number of packets dropped due to rule actions.<br />Reporting criteria: There is a nonzero value.<br />Valid statistics: Sum | Firewalls and VPC endpoint associations | 
| `DnsResolvedFlows` | Number of flows for which resolved IP validation confirmed that the destination IP address was one that the Amazon Route 53 Resolver resolved for a domain. Counted once for each flow, at the first validation verdict, not for each packet.<br />Reporting criteria: There is a nonzero value.<br />Valid statistics: Sum | Firewalls | 
| `DnsUnresolvedFlows` | Number of flows for which resolved IP validation ran but the destination IP address was not one that the Amazon Route 53 Resolver resolved for a domain. This count reflects the resolution outcome and is independent of the configured action. For example, it increments even when the action is `ALERT` and no traffic is blocked.<br />Reporting criteria: There is a nonzero value.<br />Valid statistics: Sum | Firewalls | 
| `DnsResolutionErrorFlows` | Number of flows for which resolved IP validation didn't complete because of an error.<br />Reporting criteria: There is a nonzero value.<br />Valid statistics: Sum | Firewalls | 
| `DnsAzUnavailableFlows` | Number of flows that resolved IP validation can't evaluate because the Availability Zone doesn't support the feature. For a transit gateway-attached firewall, this is the Availability Zone of the client. For other firewalls, it's the Availability Zone where you deploy the firewall endpoint.<br />Reporting criteria: There is a nonzero value.<br />Valid statistics: Sum | Firewalls | 
| `InvalidDroppedPackets` | Number of packets dropped for failing packet validation due to issues with the packet.<br />Reporting criteria: There is a nonzero value.<br />Valid statistics: Sum | Firewalls and VPC endpoint associations | 
| `OtherDroppedPackets` | Number of packets dropped due to reasons other than those described by `InvalidDroppedPackets` or `DroppedPackets`, including packets that are throttled due to bursting traffic.<br />Reporting criteria: There is a nonzero value.<br />Valid statistics: Sum | Firewalls and VPC endpoint associations | 
| `Packets` | Number of packets inspected for a firewall policy or stateless rulegroup for which a custom action is defined. This metric is only used for the dimension `CustomAction`. <br />Reporting criteria: There is a nonzero value.<br />Valid statistics: Sum | Firewall only | 
| `PassedPackets` | Number of packets that the Network Firewall firewall allowed through to their destinations.<br />Reporting criteria: There is a nonzero value.<br />Valid statistics: Sum | Firewalls and VPC endpoint associations | 
| `ReceivedPackets` | Number of packets received by the Network Firewall firewall.<br />Reporting criteria: There is a nonzero value.<br />Valid statistics: Sum | Firewalls and VPC endpoint associations | 
| `ReceivedBytes` | Number of bytes received by the Network Firewall firewall.<br />Reporting criteria: There is a nonzero value.<br />Valid statistics: Sum | Firewall only | 
| `RejectedPackets` | The number of packets rejected due to `Reject` stateful rule actions. For information about stateful actions, see [Actions for stateful rules](rule-action.md#rule-action-stateful).<br />Reporting criteria: There is a nonzero value.<br />Valid statistics: Sum | Firewall only | 
| `StreamExceptionPolicyPackets` | The number of packets matching the firewall policy's stream exception policy. You can configure stream exception policy settings while creating a firewall policy in the console, or by the [StatefulEngineOptions](https://docs.aws.amazon.com/network-firewall/latest/APIReference/API_StatefulEngineOptions.html) structure when using the API. For more information about stream exception policy settings, see the **Stream exception policy** option in the [Creating a firewall policy in AWS Network Firewall](firewall-policy-creating.md) procedure.<br />Reporting criteria: There is a nonzero value.<br />Valid statistics: Sum | Firewall only | 
| `TLSDroppedPackets` | Number of packets dropped by Network Firewall while inspecting SSL/TLS packets. The value of this metric might differ between stateless and stateful rule processing due to the TCP and TLS connection termination that occurs prior to stateful packet inspection.<br />Reporting criteria: There is a nonzero value.<br />Valid statistics: Sum | Firewall only | 
| `TLSErrors` | Number of errors observed by Network Firewall while inspecting SSL/TLS packets.<br />Reporting criteria: There is a nonzero value.<br />Valid statistics: Sum | Firewall only | 
| `TLSPassedPackets` | Number of packets passed by Network Firewall while inspecting SSL/TLS packets. The value of this metric might differ between stateless and stateful rule processing due to the TCP and TLS connection termination that occurs prior to stateful packet inspection.<br />Reporting criteria: There is a nonzero value.<br />Valid statistics: Sum | Firewall only | 
| `TLSReceivedPackets` | Number of SSL/TLS packets received by the Network Firewall firewall. The value of this metric might differ between stateless and stateful rule processing due to the TCP and TLS connection termination that occurs prior to stateful packet inspection.<br />Reporting criteria: There is a nonzero value.<br />Valid statistics: Sum | Firewall only | 
| `TLSRejectedPackets` | Number of packets rejected by Network Firewall while inspecting SSL/TLS packets. The value of this metric might differ between stateless and stateful rule processing due to the TCP and TLS connection termination that occurs prior to stateful packet inspection.<br />Reporting criteria: There is a nonzero value.<br />Valid statistics: Sum | Firewall only | 
| `TLSRevocationStatusOKConnections` | The number of SSL/TLS connections to TLS servers whose certificates have been confirmed as not revoked.<br />Reporting criteria: There is a nonzero value.<br />Valid statistics: Sum | Firewall only | 
| `TLSRevocationStatusRevokedConnections` | The number of SSL/TLS connections to TLS servers whose certificates have been confirmed as revoked.<br />Reporting criteria: There is a nonzero value.<br />Valid statistics: Sum | Firewall only | 
| `TLSRevocationStatusUnknownConnections` | The number of SSL/TLS connections to TLS servers whose certificates revocation status is unknown or could not be determined by the firewall. This can occur when the OCSP responder for a server certificate returns an unknown status, or when the firewall is unable to connect to the CRL or OCSP endpoints provided in the certificate.<br />Reporting criteria: There is a nonzero value.<br />Valid statistics: Sum | Firewall only | 
| `TLSTimedOutConnections` | Number of SSL/TLS connections that timed out during SSL/TLS inspection by Network Firewall.<br />Reporting criteria: There is a nonzero value.<br />Valid statistics: Sum | Firewall only | 

## AWS Network Firewall dimensions
<a name="metricdimensions"></a>

Network Firewall can use the following dimension combinations to categorize your metrics: 


| Dimension | Description | 
| --- | --- | 
| `AvailabilityZone` | Availability Zone in the Region where the Network Firewall firewall is active.  | 
| `CustomAction` | Dimension for a publish metrics custom action that you defined. You can define this for a rule action in a stateless rule group or for a stateless default action in a firewall policy.  | 
| `Engine` | Rules engine that processed the packet. For a firewall that uses a Classic Network Firewall policy, the value is either Stateful or Stateless. For a firewall that uses a Next Generation policy, the value identifies which inspection engine the metric is for: Firewall for the firewall engine, IPS for the IPS engine, System for counts that aren't specific to one engine, and TLS for TLS inspection. For information about Next Generation policies, see [Next Generation policies](firewall-policies-v2.md).  | 
| `FirewallName` | Name that you specified for the Network Firewall firewall.  | 
| `EndpointName` | Name that is generated for the Network Firewall `VpcEndpointAssociation`.  | 