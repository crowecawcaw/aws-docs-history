

# Scenario 6: Implementation of RTB Fabric for RTB workloads on AWS

 AdTech companies can replace public internet connectivity and NAT Gateway-based RTB architectures with AWS RTB Fabric, a purpose-built private network for programmatic advertising that delivers single-digit millisecond latency and transaction-based pricing. RTB Fabric helps AdTech companies connect with their partners over a purpose-built, private network to run real-time bidding workloads with optimized data transfer costs and enhanced infrastructure utilization. 

## Characteristics
<a name="s06-characteristics"></a>
+  High-volume RTB workloads where networking costs (NAT Gateway per-GB charges) are the dominant or second-largest cost category. 
+  Bid traffic requires consistent sub-10 ms network latency that public internet routing can't reliably provide. 
+  Multiple SSP and DSP partners need connectivity, each with different QPS volumes and contractual SLAs. 
+  Operations teams need per-partner visibility into bid traffic health, latency, and filtering effectiveness. 
+  Traditional setups use NLB or HAProxy with ingress controllers, whereas RTB Fabric offloads these layers entirely. 
+  Customers lack implementation guidance for leveraging RTB Fabric to optimize network costs, improve bid efficiency, and increase bid response rates. 

## Reference architecture
<a name="s06-reference-architecture"></a><a name="scenario-06-fig1"></a>

![AWS RTB Fabric architecture showing SSP (Requester) and DSP (Responder) gateways deployed across multiple Availability Zones with Managed Endpoints routing directly to bidder pods, built-in traffic management modules, and the CloudWatch monitoring integration](https://docs.aws.amazon.com/wellarchitected/latest/video-streaming-advertising-lens/images/scenario-06-rtb-fabric.jpg)

*AWS RTB Fabric architecture showing SSP (Requester) and DSP (Responder) gateways deployed across multiple Availability Zones with Managed Endpoints routing directly to bidder pods, built-in traffic management modules, and the CloudWatch monitoring integration*


 The architecture consists of the following components: 

1.  **Requester Gateway (SSP side)**: RTB Fabric gateway that sends bid requests to partner DSPs. Deployed in each Availability Zone where SSP compute runs. Routes traffic over the RTB Fabric private network rather than the public internet. Configured with IAM task roles (ECS) or IRSA (EKS) for least-privilege access. 

1.  **Responder Gateway (DSP side)**: RTB Fabric gateway that receives bid requests from partner SSPs. Colocate in the same Availability Zones as bidder compute. Handles TLS termination and load distribution natively, removing the need for a separate NLB or ingress controller. 

1.  **OpenRTB Filter Module**: Validates and blocks bid requests based on OpenRTB protocol attributes directly in the network path at network speed. Configured with badv (blocked advertiser domains), bcat (blocked categories), and bapp (blocked app identifiers). Uses holdbackPercentage for gradual rollout validation before full deployment. 

1.  **Rate Limiter Module**: Caps inbound QPS per partner link, guarding against a single partner's traffic spike consuming capacity allocated to others. Configured per-link based on contracted QPS levels with graduated thresholds (warn at 80% of cap, enforce hard limit at 100%). 

1.  **Managed Endpoints (EKS)**: RTB Fabric queries the EKS Kubernetes API to discover bidder pod IPs in real time. Routes bid requests directly to individual pods, bypassing the NLB and ingress controller layers that traditional architectures require. This avoids their hourly and LCU-based costs and removes network hops. 

1.  **CloudWatch (AWS/RTBFabric namespace)**: Per-link metrics for request counts, forwarding latency (in microseconds), HTTP status code distribution, and target endpoint health. Note: latency metrics are reported in microseconds, so dashboard thresholds and alarms must account for this unit (for example, a 100 ms alarm threshold = 100,000 microseconds). 

1.  **Bidder compute (EKS pods / EC2 ASG)**: The DSP's bid evaluation infrastructure. Colocate in the same Availability Zones as RTB Fabric Responder Gateways to minimize network traversal and avoid cross-AZ data transfer charges. 

## Configuration notes
<a name="s06-configuration-notes"></a>

### Migration approach
<a name="migration-approach"></a>

 Migrate partner traffic to RTB Fabric one partner at a time. Analyze VPC Flow Logs to identify all RTB traffic routing through NAT Gateways to AdTech partner IP ranges. Calculate monthly NAT Gateway costs (hourly fees \+ per-GB processing) to establish the cost savings baseline. Create RTB Fabric gateways colocate with your VPC's Availability Zones. For each partner, create a link and validate traffic routing before decommissioning NAT Gateways. 

### Traffic management modules
<a name="traffic-management-modules"></a>

 Configure the OpenRTB Filter module targeting the highest-volume no-bid categories identified from bid log analysis. Start with holdbackPercentage at 90 (only 10% filtered) and use the headerTag action for A/B analysis before committing to noBid actions. Reduce holdback gradually over 2–4 weeks as filter accuracy is validated. Configure Rate Limiter per link based on each partner's historical QPS patterns and contracted volumes. 

### Managed Endpoints
<a name="managed-endpoints"></a>

 Enable Managed Endpoints for EKS-based bidder deployments. Configure the EKS cluster credentials so RTB Fabric can discover pod IPs through the Kubernetes API. As the bidder fleet scales (pods start and stop), RTB Fabric automatically updates routing without NLB reconfiguration. Test routing behavior by verifying in VPC Flow Logs that traffic goes directly to pod IPs, not to an NLB virtual IP. 

### Availability Zone affinity and cost optimization
<a name="availability-zone-affinity-and-cost-optimization"></a>

 Deploy RTB Fabric gateways in the same Availability Zones as bidder compute. Coordinate Availability Zone placement with partners using Availability Zone IDs (not Availability Zone names, which map to different physical zones across accounts). This avoids cross-AZ transfer charges for the highest-volume partner links. Disable cross-zone load balancing on any remaining load balancers serving RTB traffic. 

### Monitoring
<a name="monitoring"></a>

 Build CloudWatch dashboards correlating network-layer metrics (RTB Fabric AWSRTBFabric namespace) with application-layer bid metrics (bid win rate, no-bid rate by reason code, timeout rate). Remember that RTB Fabric latency metrics are in microseconds, and configure dashboard Y-axis labels and alarm thresholds accordingly. Use target-ip-count as an immediate health indicator. If it drops to zero, all target endpoints behind that gateway are unhealthy. 