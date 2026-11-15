

# TELCOOPS07-BP01 Design geo-redundant architectures using Outposts and multi-AZ deployments within data residency boundaries
<a name="telcoops07-bp01"></a>

 Telco regulators in many jurisdictions require both geographical separation between redundant sites, often 200 km or more, and in-country data residency. These demands conflict where a country has only a single cloud region. This best practice places compute in operator-owned facilities to provide the separation without moving data across borders, and validates that failover helps you adhere to both technical and regulatory targets. 

 **Desired outcome:** 
+  The geo-redundant architecture uses AWS Outposts in geographically separated operator facilities to achieve the required physical distance between sites. 
+  Subscriber data remains within national boundaries at all times, including during failover scenarios. 
+  Failover between sites is tested and confirmed to meet recovery-time, recovery-point, and data-residency requirements simultaneously. 

 **Common anti-patterns:** 
+  Relying on edge or routing-optimization services for geo-redundancy when they don't provide the required physical separation or residency guarantees. 
+  Assuming multi-AZ deployment alone satisfies a minimum separation distance without verifying actual Availability Zone distances. 
+  Deploying to a second Region in another country without confirming that cross-border data transfer is permitted. 
+  Treating geo-redundancy as a binary requirement rather than designing tiered recovery for different workload criticality levels. 

 **Benefits of establishing this best practice:** 
+  Outposts in operator facilities keep data in-country while providing genuine geographical separation. 
+  The Outpost uses the same AWS APIs and tools as the Region, which reduces operational overhead for the DR site. 
+  Tested failover procedures confirm that recovery works within both technical and regulatory constraints. 
+  The design can evolve as new AWS infrastructure becomes available in target countries, which preserves the investment. 

 **Level of risk exposed if this best practice is not established:** High \#\# Implementation guidance A minimum separation distance pushes redundant sites apart, while data residency confines them to one country. In a country with a single Region, those two rules can't both be satisfied with Regions alone. AWS Outposts extend AWS into operator-owned or partner facilities. An Outpost installed 200 km from the nearest Availability Zone provides geographical separation while data processing and storage stay within national borders. The Outpost connects to its parent Region for control-plane operations but keeps data local. Services designed for ultra-low-latency edge access or for routing optimization don't provide compute and storage at a separate location, so they can't serve as the DR site. For architectures that replicate data across locations, apply data classification and encryption with customer-managed keys so that only permitted data categories can move and residency can be proven. Design the DR architecture with asymmetric capacity, because a full-scale standby in a constrained facility is rarely justified. The primary site handles full production load, and the secondary Outpost holds warm standby capacity sized for the critical network functions during failover, with headroom to scale up once an event is confirmed as sustained. Tiering recovery by workload criticality keeps the DR footprint proportionate to the risk. Engage AWS infrastructure planning to keep this design current. The roadmap for new Regions, Local Zones, and Outpost capabilities changes what is possible in a given country over time. \#\#\# Implementation steps 
+  Map regulatory requirements to physical infrastructure: document the separation distance, data-residency, and recovery-time requirements for each jurisdiction, and identify which operator facilities meet the distance requirement from the nearest Availability Zone. 
+  Deploy Outposts in separated operator facilities that satisfy the regulatory separation distance, and configure the Outpost subnet and networking to mirror the primary site's architecture. 
+  Implement data classification and encryption controls: for architectures that replicate across locations, apply data classification and encryption with AWS KMS customer-managed keys so that only permitted data categories can cross geographical boundaries. 
+  Configure replication sized to recovery targets: set up synchronous or asynchronous replication, based on the recovery-point objective, for subscriber state, configuration databases, and session data between the primary site and the Outpost DR site. 
+  Test failover including residency validation: execute failover drills that confirm network functions recover within recovery-time targets and that no subscriber data leaves the national boundary during failover, and document the results for regulatory audit. 
+  Engage AWS infrastructure planning: work with your AWS account team to understand the roadmap for future Regions, Local Zones, or Outpost capabilities in target countries, and design the architecture to adopt new infrastructure as it becomes available. \#\# Resources **Key AWS services:** 
+  [AWS Outposts](https://aws.amazon.com/outposts/) 
+  [AWS Key Management Service](https://aws.amazon.com/kms/) 
+  [AWS Direct Connect](https://aws.amazon.com/directconnect/) 