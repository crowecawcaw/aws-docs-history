

# ADVREL01-BP02 Architect your system with appropriate recovery objectives

 Avoid over- or under-architecting your services by working backward from your service's recovery objectives, and balance them against adjacent pillars such as cost optimization and operational excellence. Use KPIs from the operational excellence pillar to inform your reliability approach. 

 **Desired outcome:** 
+  Recovery Point Objective (RPO) and Recovery Time Objective (RTO) are defined individually for each advertising component based on its business criticality. 
+  Architecture decisions for each component (redundancy level, failover mechanism, backup frequency) are driven by that component's documented recovery objectives. 
+  The cost of implementing recovery capabilities is proportional to the business impact of the data or function being protected. 

 **Common anti-patterns:** 
+  Applying the same (usually maximum) redundancy to all advertising components regardless of their business impact, paying for millisecond failover for batch analytics that could tolerate hours of recovery. 
+  Defining a single workload-level RPO/RTO that obscures the different requirements of auction-critical compared to analytics-only services. 
+  Setting RPO/RTO targets without measuring whether they can actually be met under realistic failure scenarios. 

 **Benefits of establishing this best practice:** 
+  Infrastructure investment is proportional to business value at risk, avoiding both over-spending and under-protection. 
+  Stakeholders have a shared, documented understanding of acceptable risk and recovery trade-offs. 
+  Architecture decisions are justified with concrete business data rather than assumptions. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 Advertising customers accept recovery ranges from milliseconds to hours. Delivery services have the most stringent requirements, whereas analytics and reporting tolerate looser ones. Identify critical parts of the architecture individually and confirm their reliability and RPO/RTO requirements. 

 For real-time bidding, delivery services have stricter RPO and RTO requirements than creative services. The enrichment and auction layers typically require RPO measured in seconds (loss of recent targeting data is acceptable) and RTO measured in seconds (resuming bid processing quickly is critical). Analytics workloads can tolerate RPO of hours (replaying event data from Kinesis) and RTO of hours (rebuilding dashboards from S3 archives). 

 Use AWS Resilience Hub to define, validate, and track application resilience goals, generate recommendations for improvemen, and view a central display of your application resilience posture. 

 Flexible supply and demand in advertising reduces redundancy requirements for some components. If inventory is readily replaceable from other sources, a component that manages it can have more relaxed recovery objectives than a component managing unique publisher relationships. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Classify advertising components by business criticality:** Create a component inventory categorizing each service as: Tier 1 (auction-critical, millisecond RTO), Tier 2 (near-real-time data, second-to-minute RTO), or Tier 3 (analytics and reporting, hour-level RTO acceptable). Document the justification for each classification with the corresponding revenue or compliance impact of unavailability. 

1.  **Define per-component RPO and RTO targets:** For each component, document: RPO (maximum acceptable data loss expressed in time), RTO (maximum acceptable time to restore function), and the measurement methodology for each. For Tier 1 auction components, typical targets are RPO < 30 seconds, RTO < 60 seconds. For Tier 3 analytics, typical targets are RPO < 4 hours, RTO < 8 hours. 

1.  **Validate recovery objectives using AWS Resilience Hub:** Import your application into AWS Resilience Hub and configure the tier-based recovery objectives you've defined. Run the resilience assessment to identify components where your current architecture can't meet your stated objectives. Prioritize improvements for gaps where the cost of downtime exceeds the cost of improvement. 

1.  **Align architecture decisions to recovery objectives:** For each component, select the recovery mechanism appropriate to its tier: Tier 1 (Multi-AZ active-active, automatic failover, no data loss), Tier 2 (Multi-AZ active-passive, automated failover, minimal data loss), Tier 3 (point-in-time snapshots, manual recovery, acceptable data loss window). Document these decisions as Architecture Decision Records. 

1.  **Test recovery objectives regularly:** Run quarterly DR exercises for Tier 1 components that simulate realistic failure scenarios (Availability Zone failure, database primary failure, message broker unavailability). Measure actual RTO and RPO achieved, compare against targets, and update architecture where targets are not met. Use AWS FIS to inject failures in a controlled manner. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [ADVREL01-BP01 Use loosely-coupled architectures to enable graceful recovery from failures](advrel01-bp01.md) 

 **Related documents:** 
+  [Establishing RPO and RTO Targets for Cloud Applications](https://aws.amazon.com/blogs/mt/establishing-rpo-and-rto-targets-for-cloud-applications/) 

 **Related services:** 
+  [AWS Resilience Hub](https://aws.amazon.com/resilience-hub/) 